"""Portable entry point with explicit build and artifact requirements."""
import argparse
from pathlib import Path
import sys


def main():
    args = sys.argv[1:]
    if not args or args[0] in ('-h', '--help'):
        print('App Factory WorkBuddy: init/gate/check/status/doctor. '
              'gate 4/check require --build-cmd and --artifact (relative to --path).')
        return 0
    if args[0] not in ('init', 'gate', 'check', 'status', 'doctor'):
        print('Unsupported command; global skill export is not available.', file=sys.stderr)
        return 2
    guard = argparse.ArgumentParser(add_help=False)
    guard.add_argument('--artifact')
    guard.add_argument('--build-cmd')
    guard.add_argument('--path', default='.')
    if args[0] == 'gate':
        guard.add_argument('gate_number', type=int)
    options, _ = guard.parse_known_args(args[1:])
    shipping = args[0] == 'check' or getattr(options, 'gate_number', None) == 4
    if shipping and (not options.build_cmd or not options.artifact):
        print('Build verification requires explicit --build-cmd and --artifact.', file=sys.stderr)
        return 2
    artifact = None
    if shipping:
        project = Path(options.path).resolve()
        artifact = (project / options.artifact).resolve()
        if project not in artifact.parents or artifact == project:
            print('Artifact must be inside the project directory.', file=sys.stderr)
            return 2
    # Remove only the wrapper argument; retain core CLI arguments unchanged.
    strip = argparse.ArgumentParser(add_help=False)
    strip.add_argument('--artifact')
    _, core_args = strip.parse_known_args(args)
    sys.path.insert(0, str(Path(__file__).resolve().parent / 'core'))
    from app_factory.cli import main as core_main
    sys.argv = ['app-factory'] + core_args
    try:
        core_main()
    except SystemExit as exc:
        if exc.code:
            return exc.code
    if artifact is not None:
        if not artifact.exists() or (artifact.is_file() and artifact.stat().st_size == 0):
            print('Build command finished but expected artifact is missing or empty.', file=sys.stderr)
            return 1
        print('Artifact exists:', artifact)
        print('Verify freshness and runtime behavior before claiming delivery.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
