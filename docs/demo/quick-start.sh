#!/usr/bin/env bash
# Demonstrate Gate 1 without installing packages or invoking external agents.
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
python3 -c 'import sys; sys.exit(0 if sys.version_info >= (3, 9) else "Python 3.9+ is required")'
demo_dir="$(mktemp -d "${TMPDIR:-/tmp}/app-factory-demo.XXXXXX")"
trap 'rm -rf -- "$demo_dir"' EXIT

factory() {
    python3 "$repo_root/bin/app-factory" "$@"
}

printf '\n1. Inspect the CLI and bundled skills\n'
factory --help
factory skills

printf '\n2. Verify that an empty project fails Gate 1\n'
if factory gate 1 --path "$demo_dir"; then
    printf 'Unexpected success: an empty project should fail Gate 1.\n' >&2
    exit 1
else
    result=$?
    if [[ "$result" -ne 1 ]]; then
        printf 'Unexpected CLI exit code: %s\n' "$result" >&2
        exit "$result"
    fi
fi

printf '\n3. Initialize PRD and task templates\n'
factory init "$demo_dir"

printf '\n4. Verify Gate 1 now passes\n'
factory gate 1 --path "$demo_dir"
printf '\nDemo complete. Replace template placeholders before using a real project.\n'
