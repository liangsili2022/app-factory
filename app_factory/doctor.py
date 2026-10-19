"""Environment and toolchain health diagnosis for App Factory."""

import shutil
import subprocess
from typing import Dict, List, Tuple


def check_command(cmd: str, version_arg: str = "--version") -> Tuple[bool, str]:
    """Check if a CLI binary exists and return its version."""
    path = shutil.which(cmd)
    if not path:
        return False, "Not found in PATH"
    try:
        res = subprocess.run(
            [cmd, version_arg],
            capture_output=True,
            text=True,
            timeout=5,
        )
        output = (res.stdout or res.stderr or "").strip().splitlines()
        first_line = output[0] if output else "Available"
        return True, first_line[:60]
    except Exception as e:
        return True, f"Found at {path} ({e})"


def run_doctor() -> Dict[str, List[Tuple[str, bool, str]]]:
    """Run full diagnostic checks across core runtimes, AI agents, and compilers."""
    report = {
        "Core Runtimes": [
            ("Git", *check_command("git", "--version")),
            ("Python 3", *check_command("python3", "--version")),
            ("Node.js", *check_command("node", "--version")),
        ],
        "AI Agent CLIs": [
            ("Claude Code", *check_command("claude", "--version")),
            ("Codex CLI", *check_command("codex", "--version")),
            ("Hermes Agent", *check_command("hermes", "--version")),
            ("Cursor CLI", *check_command("cursor", "--version")),
        ],
        "Native Compilers & SDKs": [
            ("Xcode CLI (xcodebuild)", *check_command("xcodebuild", "-version")),
            ("Flutter SDK", *check_command("flutter", "--version")),
            ("Rust (cargo)", *check_command("cargo", "--version")),
            ("Go (go)", *check_command("go", "version")),
        ],
    }
    return report


def print_doctor_report(report: Dict[str, List[Tuple[str, bool, str]]]) -> bool:
    """Print the formatted report to stdout. Returns True if basic requirements pass."""
    all_ok = True
    print("\n🏭 App Factory Toolchain Doctor\n" + "=" * 40)
    for category, checks in report.items():
        print(f"\n[{category}]")
        for name, ok, desc in checks:
            status = "✓" if ok else "✗"
            print(f"  {status} {name:<26} : {desc}")
            if not ok and category == "Core Runtimes":
                all_ok = False
    print("\n" + "=" * 40)
    if all_ok:
        print("✓ All essential runtime dependencies are satisfied!\n")
    else:
        print("⚠ Some essential core dependencies are missing.\n")
    return all_ok
