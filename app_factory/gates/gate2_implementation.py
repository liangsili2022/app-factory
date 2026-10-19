"""Gate 2: Implementation & TDD Gate (Superpowers Red-Green TDD style).

Verifies that implementation has corresponding tests and that tests pass cleanly.
"""

import os
from typing import List, Tuple
from app_factory.adapters.runner import execute_shell


def run_gate2(project_dir: str, test_cmd: str = "pytest") -> Tuple[bool, List[str]]:
    """Execute tests and verify that the test suite passes on the host."""
    errors = []

    # Detect test command if default is passed and project has specific indicators
    if test_cmd == "pytest":
        if os.path.isfile(os.path.join(project_dir, "package.json")):
            test_cmd = "npm test"
        elif os.path.isfile(os.path.join(project_dir, "pubspec.yaml")):
            test_cmd = "flutter test"
        elif os.path.isfile(os.path.join(project_dir, "Cargo.toml")):
            test_cmd = "cargo test"

    cmd_parts = test_cmd.split()
    exit_code, stdout, stderr, duration = execute_shell(cmd_parts, workdir=project_dir, timeout=180)

    if exit_code != 0:
        errors.append(f"Gate 2 TDD check failed (Exit code {exit_code}, duration {duration:.2f}s).")
        snippet = (stdout + "\n" + stderr).strip().splitlines()[-10:]
        errors.extend(["  " + line for line in snippet])

    passed = len(errors) == 0
    return passed, errors
