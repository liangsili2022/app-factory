"""Exercise the packaged CLI from an isolated extraction, including failures."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile
from package_workbuddy import build, validate


def main():
    archive = build()
    checks = []
    with tempfile.TemporaryDirectory(prefix='workbuddy-smoke-') as tmp:
        root = Path(tmp)
        with zipfile.ZipFile(archive) as package:
            assert package.testzip() is None
            package.extractall(root)
        plugin = root / 'app-factory-expert'
        validate(plugin)
        manifest = json.loads((plugin / 'BUILD-MANIFEST.json').read_text())
        for rel, digest in manifest['files_sha256'].items():
            assert hashlib.sha256((plugin / rel).read_bytes()).hexdigest() == digest
        checks.append('archive structure and all manifest hashes')
        runner = plugin / 'skills/app-factory-delivery/scripts/run_factory.py'
        planner = runner.with_name('plan_release.py')
        release = root / 'release plan.md'

        def plan(args, expected):
            result = subprocess.run([sys.executable, str(planner)] + args,
                                    cwd=root, text=True, capture_output=True)
            assert result.returncode == expected, (result.stdout, result.stderr)
            return result

        listing = plan(['--list'], 0).stdout
        assert len(listing.splitlines()) == 11
        checks.append('release catalog contains 11 routes')
        base_plan = ['--output', str(release)]
        plan(base_plan + ['--platform', 'apple', '--system', 'android'], 2)
        assert not release.exists()
        checks.append('reject incompatible release system without writing')
        plan(base_plan + ['--platform', 'unknown', '--system', 'android'], 2)
        assert not release.exists()
        checks.append('reject unknown release platform without writing')
        targets = ['--platform', 'apple', '--platform', 'google-play',
                   '--system', 'ios', '--system', 'android']
        plan(base_plan + targets, 0)
        original = release.read_bytes()
        assert original.decode().count('| 待准备 |') == 2
        assert '| 已上线 |' not in original.decode()
        checks.append('multi-system plan leaves both releases unsubmitted')
        plan(base_plan + targets, 2)
        assert release.read_bytes() == original
        checks.append('existing release plan preserved byte for byte')
        regional = root / 'regional plan.md'
        regional_args = ['--platform', 'apple', '--platform', 'google-play',
                         '--platform', 'xiaomi', '--system', 'ios', '--system', 'android',
                         '--market', 'apple=CN', '--market', 'apple=US',
                         '--market', 'google-play=US', '--market', 'xiaomi=CN',
                         '--extension', 'huawei-harmony', '--account-state', 'unregistered',
                         '--account-creation', 'no', '--output', str(regional)]
        plan(regional_args, 0)
        body = regional.read_text()
        matrix = [line for line in body.splitlines() if '| 待准备 |' in line]
        assert len(matrix) == 4
        assert all('未注册' in line and '未构建' in line for line in matrix)
        assert all(('中国大陆APP备案' in line) == (' / CN |' in line) for line in matrix)
        checks.append('regions separated without leaking China requirements into US rows')
        assert 'APP/源码版本：待定' in body
        assert '专家包版本：' + manifest['version'] in body
        assert '账号删除功能不适用' in body and 'DevEco Studio' in body
        assert 'huawei-harmony' not in '\n'.join(matrix)
        assert body.count('- [ ]') >= 15 and '{{' not in body
        checks.append('first plan has independent versions conditional deletion and phased actions')
        bad_region = root / 'bad region.md'
        plan(['--platform', 'apple', '--system', 'ios', '--market', 'xiaomi=CN',
              '--output', str(bad_region)], 2)
        assert not bad_region.exists()
        checks.append('reject region assigned to an unselected platform')
        explicit = root / 'explicit version.md'
        plan(['--platform', 'apple', '--system', 'ios', '--app-version', '9.4.2',
              '--account-creation', 'yes', '--output', str(explicit)], 0)
        assert 'APP/源码版本：9.4.2' in explicit.read_text()
        assert '用户说明提供账号创建' in explicit.read_text()
        checks.append('explicit app version and account creation preserved')
        project = root / 'sample project with spaces'
        project.mkdir()
        env = dict(os.environ)
        env.pop('PYTHONPATH', None)
        env['PYTHONDONTWRITEBYTECODE'] = '1'

        def run(name, args, expected):
            result = subprocess.run([sys.executable, str(runner)] + args,
                                    cwd=root, env=env, text=True, capture_output=True)
            assert result.returncode == expected, (name, result.stdout, result.stderr)
            checks.append(name)

        run('init from extracted bundle', ['init', str(project)], 0)
        (project / 'docs/PRD.md').write_text('''# Tiny CLI
## Target User
Developer verifying a portable bundle.
## Core Value
Print a greeting from a runnable zipapp.
## Out of Scope
Network and deployment.
## Acceptance Criteria
Greeting tested; zipapp runs in a clean directory.
''')
        (project / 'docs/TASKS.md').write_text('- [x] Implement greeting and test\n- [x] Build zipapp\n')
        (project / 'app.py').write_text("def greet():\n    return 'Hello, App Factory!'\n")
        (project / 'test_app.py').write_text("import unittest\nfrom app import greet\nclass GreetingTest(unittest.TestCase):\n    def test_greeting(self):\n        self.assertEqual(greet(), 'Hello, App Factory!')\n")
        (project / 'build.py').write_text("from pathlib import Path\nimport zipfile\nPath('dist').mkdir(exist_ok=True)\nwith zipfile.ZipFile('dist/demo.pyz', 'w') as z:\n    z.write('app.py')\n    z.writestr('__main__.py', 'from app import greet\\nprint(greet())\\n')\n")
        (project / 'fail.py').write_text('raise SystemExit(7)\n')
        base = ['--path', str(project)]
        # Use a project-local executable script name to avoid spaces in inner commands.
        py = Path(sys.executable).name
        test = f'{py} -m unittest discover -v'
        build_cmd = f'{py} build.py'
        run('reject implicit build', ['gate', '4'] + base, 2)
        run('reject reordered implicit build', ['gate'] + base + ['4'], 2)
        run('reject missing artifact argument', ['gate', '4'] + base + ['--build-cmd', build_cmd], 2)
        run('reject artifact outside project', ['gate', '4'] + base + ['--build-cmd', build_cmd, '--artifact', '../escape'], 2)
        run('propagate failed test', ['gate', '2'] + base + ['--test-cmd', f'{py} fail.py'], 1)
        run('propagate failed build', ['gate', '4'] + base + ['--build-cmd', f'{py} fail.py', '--artifact', 'dist/demo.pyz'], 1)
        run('reject missing output after successful command', ['gate', '4'] + base + ['--build-cmd', test, '--artifact', 'dist/missing.pyz'], 1)
        run('four gates with real tests and zipapp build', ['check'] + base + ['--test-cmd', test, '--build-cmd', build_cmd, '--artifact', 'dist/demo.pyz'], 0)
        result = subprocess.run([sys.executable, str(project / 'dist/demo.pyz')], cwd=root, env=env, capture_output=True, text=True)
        assert result.returncode == 0 and result.stdout.strip() == 'Hello, App Factory!'
        checks.append('built zipapp executes with expected output')
        run('read status from extracted bundle', ['status'] + base, 0)
    report = {'checks': checks, 'passed': len(checks), 'workbuddy_import': 'not tested', 'archive': str(archive), 'sha256': hashlib.sha256(archive.read_bytes()).hexdigest()}
    (archive.parent / 'workbuddy-validation.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
