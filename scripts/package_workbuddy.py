"""Build a portable, allowlisted WorkBuddy expert archive with no dependencies."""
import hashlib
import json
from pathlib import Path
import re
import shutil
import struct
import subprocess
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'integrations/workbuddy/app-factory-expert'


def validate(root):
    config = json.loads((root / '.codebuddy-plugin/plugin.json').read_text())
    required = ('name', 'version', 'description', 'author', 'agents', 'agentName',
                'expertType', 'displayName', 'profession', 'displayDescription',
                'avatar', 'categoryId', 'defaultInitPrompt', 'plugin', 'tags', 'quickPrompts')
    assert all(config.get(key) for key in required), 'Missing expert field'
    assert re.fullmatch(r'[a-z]+(?:-[a-z]+)*', config['name'])
    assert config['expertType'] == 'agent'
    assert config['plugin'] == config['name']
    assert config['defaultInitPrompt'] == config['quickPrompts'][0]
    assert len(config['tags']) == len(config['quickPrompts']) == 3
    assert 40 <= len(config['displayDescription']['zh']) <= 50
    assert config['author']['email'].endswith('@users.noreply.github.com')
    for field in ('displayName', 'profession', 'displayDescription', 'defaultInitPrompt'):
        assert all(config[field].get(lang) for lang in ('zh', 'en'))
    for rel in config['agents'] + config['skills'] + [config['avatar']]:
        path = (root / rel).resolve()
        assert root.resolve() in path.parents and path.exists(), rel
    agent = (root / config['agents'][0]).read_text()
    assert f"name: {config['agentName']}\n" in agent and '\ntools:' not in agent
    for rel in config['skills']:
        skill = (root / rel / 'SKILL.md').read_text()
        front = skill.split('---', 2)[1]
        for field in ('name', 'display_name', 'display_name_en', 'description',
                      'description_zh', 'description_en', 'version', 'author'):
            assert re.search(r'^' + field + r': .+', front, re.M), field
        assert (root / rel / 'scripts/run_factory.py').is_file()
    avatar = (root / config['avatar']).read_bytes()
    assert avatar[:8] == b'\x89PNG\r\n\x1a\n' and len(avatar) <= 500 * 1024
    assert struct.unpack('>II', avatar[16:24]) == (512, 512)
    return config


def build():
    config = validate(SOURCE)
    output = ROOT / 'dist' / f"{config['name']}-{config['version']}.zip"
    output.parent.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='app-factory-package-') as tmp:
        stage = Path(tmp) / config['name']
        shutil.copytree(SOURCE, stage, ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '.DS_Store'))
        shutil.copy2(ROOT / 'LICENSE', stage / 'LICENSE')
        core = stage / 'skills/app-factory-delivery/scripts/core/app_factory'
        # Only Python source is vendored; no state, credentials, or project files.
        for src in sorted((ROOT / 'app_factory').rglob('*.py')):
            dst = core / src.relative_to(ROOT / 'app_factory')
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
        validate(stage)
        files = {p.relative_to(stage).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                 for p in sorted(stage.rglob('*')) if p.is_file()}
        manifest = {'version': config['version'], 'upstream_commit': subprocess.check_output(
            ['git', '-C', str(ROOT), 'rev-parse', 'HEAD'], text=True).strip(),
            'files_sha256': files, 'validation': 'local; WorkBuddy import not yet verified'}
        (stage / 'BUILD-MANIFEST.json').write_text(json.dumps(manifest, indent=2) + '\n')
        with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
            for path in sorted(stage.rglob('*')):
                if path.is_file():
                    info = zipfile.ZipInfo(path.relative_to(Path(tmp)).as_posix(), (2026, 11, 5, 0, 0, 0))
                    info.compress_type = zipfile.ZIP_DEFLATED
                    info.external_attr = 0o100644 << 16
                    archive.writestr(info, path.read_bytes())
    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    output.with_suffix('.zip.sha256').write_text(f'{digest}  {output.name}\n')
    print(output)
    print('SHA-256:', digest)
    return output


if __name__ == '__main__':
    build()
