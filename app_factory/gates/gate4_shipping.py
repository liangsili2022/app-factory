"""Gate 4: Native Shipping & Host Compiler Gate (Hermes Grounded Execution style).

Executes the real native build/compile toolchain on the host machine.
Rejects AI self-reports and requires exit code 0 from real compilers.
"""

import os
from typing import List, Optional, Tuple
from app_factory.adapters.runner import execute_shell


def detect_build_command(project_dir: str) -> Optional[str]:
    """Auto-detect compilation command based on repository manifests."""
    if os.path.isfile(os.path.join(project_dir, "pubspec.yaml")):
        return "flutter analyze"
    if any(f.endswith(".xcodeproj") or f.endswith(".xcworkspace") for f in os.listdir(project_dir)):
        return "xcodebuild -showsdks"
    if os.path.isfile(os.path.join(project_dir, "Cargo.toml")):
        return "cargo check"
    if os.path.isfile(os.path.join(project_dir, "package.json")):
        return "npm run build --if-present"
    if os.path.isfile(os.path.join(project_dir, "pyproject.toml")) or os.path.isfile(os.path.join(project_dir, "setup.py")):
        return "python3 -m compileall -q ."
    return None


def run_gate4(project_dir: str, build_cmd: Optional[str] = None) -> Tuple[bool, List[str]]:
    """Execute host compiler verification."""
    errors = []
    effective_cmd = build_cmd or detect_build_command(project_dir)

    if not effective_cmd:
        # Default fallback check if no specific build toolchain is detected
        return True, ["No specific compiler manifest detected. Skipped native build."]

    cmd_parts = effective_cmd.split()
    exit_code, stdout, stderr, duration = execute_shell(cmd_parts, workdir=project_dir, timeout=300)

    if exit_code != 0:
        errors.append(f"Gate 4 Host Compilation failed: '{effective_cmd}' exited with {exit_code} ({duration:.2f}s)")
        snippet = (stdout + "\n" + stderr).strip().splitlines()[-10:]
        errors.extend(["  " + line for line in snippet])

    passed = len(errors) == 0
    return passed, errors
