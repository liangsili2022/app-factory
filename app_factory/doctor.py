"""Environment and toolchain health diagnosis for App Factory.

Supports the Top 10+ mainstream AI coding agents, core runtimes, and native compilers.
"""

import shutil
import subprocess
from typing import Dict, List, Tuple


# Top 10+ Mainstream Coding Agents / AI CLIs
AI_AGENT_SPECS = [
    ("Claude Code", "claude", "--version"),
    ("OpenAI Codex", "codex", "--version"),
    ("Hermes Agent", "hermes", "--version"),
    ("Cursor CLI", "cursor", "--version"),
    ("Muse", "muse", "--version"),
    ("Grok Bot / CLI", "grok", "--version"),
    ("GitHub Copilot CLI", "copilot", "--version"),
    ("Antigravity (agy)", "agy", "--version"),
    ("OpenCode", "opencode", "--version"),
    ("Aider", "aider", "--version"),
    ("Windsurf", "windsurf", "--version"),
    ("Devin CLI", "devin", "--version"),
]


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


def check_special_agent(name: str, primary_cmd: str, version_arg: str = "--version") -> Tuple[bool, str]:
    """Check agent with fallbacks (e.g. grok-bot for grok, gh copilot for copilot)."""
    ok, desc = check_command(primary_cmd, version_arg)
    if ok:
        return True, desc

    # Fallbacks for specific agent variants
    if primary_cmd == "grok":
        for alt in ["grok-bot", "xurl"]:
            ok_alt, desc_alt = check_command(alt, version_arg)
            if ok_alt:
                return True, f"via {alt}: {desc_alt}"
    elif primary_cmd == "copilot":
        # check gh copilot extension
        gh_path = shutil.which("gh")
        if gh_path:
            try:
                res = subprocess.run(["gh", "copilot", "--version"], capture_output=True, text=True, timeout=5)
                if res.returncode == 0:
                    first = res.stdout.strip().splitlines()[0] if res.stdout else "gh extension"
                    return True, f"via gh: {first[:60]}"
            except Exception:
                pass

    return False, "Not found in PATH"


def run_doctor() -> Dict[str, List[Tuple[str, bool, str]]]:
    """Run full diagnostic checks across core runtimes, Top 10+ AI agents, and compilers."""
    agent_checks = []
    for name, cmd, varg in AI_AGENT_SPECS:
        ok, desc = check_special_agent(name, cmd, varg)
        agent_checks.append((name, ok, desc))

    report = {
        "Core Runtimes": [
            ("Git", *check_command("git", "--version")),
            ("Python 3", *check_command("python3", "--version")),
            ("Node.js", *check_command("node", "--version")),
        ],
        "Top AI Coding Agents": agent_checks,
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
    print("\n🏭 App Factory Toolchain Doctor\n" + "=" * 55)
    for category, checks in report.items():
        print(f"\n[{category}]")
        installed_count = sum(1 for _, ok, _ in checks if ok)
        total_count = len(checks)
        print(f"  Status: {installed_count}/{total_count} available")
        for name, ok, desc in checks:
            status = "✓" if ok else "·"
            print(f"  {status} {name:<26} : {desc}")
            if not ok and category == "Core Runtimes":
                all_ok = False
    print("\n" + "=" * 55)
    if all_ok:
        print("✓ All essential runtime dependencies are satisfied!\n")
    else:
        print("⚠ Some essential core dependencies are missing.\n")
    return all_ok
