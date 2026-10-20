"""Command-line interface for App Factory."""

import argparse
import os
import shutil
import sys
from typing import Dict, List
from app_factory.doctor import print_doctor_report, run_doctor
from app_factory.orchestrator import PipelineOrchestrator


PRD_TEMPLATE = """# Product Requirements Document (PRD)

## Target User
[Describe exactly who this app or feature is built for]

## Core Value
[Single, crisp statement of the user problem solved]

## Out of Scope
[Explicit list of features and tangents we will NOT build in this release]

## Acceptance Criteria
- [ ] AC 1: Core flow operates without errors
- [ ] AC 2: Automated test coverage validates edge cases
- [ ] AC 3: Host compilation returns exit code 0
"""

TASKS_TEMPLATE = """# Implementation Tasks

- [ ] Task 1: Setup project structure and core models
- [ ] Task 2: Implement core logic with TDD unit tests
- [ ] Task 3: Security audit and clean build verification
"""


def get_skills_dir() -> str:
    """Return the absolute path to the bundled skills directory."""
    pkg_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    return os.path.join(pkg_root, "skills")


def load_skills_catalog() -> List[Dict[str, str]]:
    """Inspect and return metadata for all bundled skills."""
    skills_dir = get_skills_dir()
    catalog = []
    if not os.path.isdir(skills_dir):
        return catalog

    for name in sorted(os.listdir(skills_dir)):
        skill_path = os.path.join(skills_dir, name, "SKILL.md")
        if os.path.isfile(skill_path):
            desc = "No description provided."
            title = name
            with open(skill_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                for line in content.splitlines():
                    if line.startswith("title:"):
                        title = line.split(":", 1)[1].strip().strip("\"'")
                    elif line.startswith("description:"):
                        desc = line.split(":", 1)[1].strip().strip("\"'")
            catalog.append({"name": name, "title": title, "description": desc, "path": os.path.dirname(skill_path)})
    return catalog


def export_skills(target_agent: str) -> None:
    """Export bundled skills to target agent environments (Claude, Codex, Hermes, Cursor, all)."""
    catalog = load_skills_catalog()
    home = os.path.expanduser("~")

    targets = {
        "claude": os.path.join(home, ".claude", "skills"),
        "codex": os.path.join(home, ".codex", "skills"),
        "hermes": os.path.join(home, ".hermes", "skills", "app-factory"),
        "cursor": os.path.join(home, ".cursor", "skills"),
    }

    selected = targets.keys() if target_agent == "all" else [target_agent.lower()]

    print(f"\n📦 Exporting {len(catalog)} App Factory Skills to '{target_agent}'...")
    for agent in selected:
        if agent not in targets:
            print(f"  ⚠ Unknown agent target '{agent}'. Valid: claude, codex, hermes, cursor, all")
            continue
        dest_dir = targets[agent]
        os.makedirs(dest_dir, exist_ok=True)
        count = 0
        for skill in catalog:
            dest_skill_dir = os.path.join(dest_dir, skill["name"])
            if os.path.exists(dest_skill_dir) or os.path.islink(dest_skill_dir):
                if os.path.islink(dest_skill_dir):
                    os.unlink(dest_skill_dir)
                else:
                    shutil.rmtree(dest_skill_dir, ignore_errors=True)
            try:
                os.symlink(skill["path"], dest_skill_dir)
                count += 1
            except Exception:
                shutil.copytree(skill["path"], dest_skill_dir)
                count += 1
        print(f"  ✓ Installed {count} skills to {dest_dir}")
    print("\n✓ Skill export complete.\n")


def init_project(target_dir: str) -> None:
    """Initialize docs/PRD.md and docs/TASKS.md in the target directory."""
    docs_dir = os.path.join(target_dir, "docs")
    os.makedirs(docs_dir, exist_ok=True)

    prd_path = os.path.join(docs_dir, "PRD.md")
    if not os.path.exists(prd_path):
        with open(prd_path, "w", encoding="utf-8") as f:
            f.write(PRD_TEMPLATE)
        print(f"✓ Created {prd_path}")
    else:
        print(f"· Existing {prd_path} kept")

    tasks_path = os.path.join(docs_dir, "TASKS.md")
    if not os.path.exists(tasks_path):
        with open(tasks_path, "w", encoding="utf-8") as f:
            f.write(TASKS_TEMPLATE)
        print(f"✓ Created {tasks_path}")
    else:
        print(f"· Existing {tasks_path} kept")

    print("\nProject initialized for App Factory 4-Gate lifecycle.\n")


def main():
    parser = argparse.ArgumentParser(
        prog="app-factory",
        description="Multi-Agent Software Factory combining gstack, Superpowers TDD, and host compiler verification.",
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # doctor
    subparsers.add_parser("doctor", help="Check local toolchains, Top 10+ AI CLIs, and compilers")

    # init
    init_p = subparsers.add_parser("init", help="Initialize App Factory templates in a project")
    init_p.add_argument("path", nargs="?", default=".", help="Target project directory")

    # gate
    gate_p = subparsers.add_parser("gate", help="Run a specific quality gate (1-4)")
    gate_p.add_argument("gate_num", type=int, choices=[1, 2, 3, 4], help="Gate number")
    gate_p.add_argument("--test-cmd", default="pytest", help="Custom test command for Gate 2")
    gate_p.add_argument("--build-cmd", default=None, help="Custom build command for Gate 4")
    gate_p.add_argument("--path", default=".", help="Target project directory")

    # check
    check_p = subparsers.add_parser("check", help="Run all 4 gates sequentially")
    check_p.add_argument("--test-cmd", default="pytest", help="Custom test command for Gate 2")
    check_p.add_argument("--build-cmd", default=None, help="Custom build command for Gate 4")
    check_p.add_argument("--path", default=".", help="Target project directory")

    # status
    status_p = subparsers.add_parser("status", help="Show current pipeline state")
    status_p.add_argument("--path", default=".", help="Target project directory")

    # skills
    skills_p = subparsers.add_parser("skills", help="List or export 10 built-in cross-platform skills")
    skills_p.add_argument(
        "--export",
        choices=["claude", "codex", "hermes", "cursor", "all"],
        help="Export/install skills into target agent environment",
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    if args.command == "doctor":
        report = run_doctor()
        ok = print_doctor_report(report)
        sys.exit(0 if ok else 1)

    elif args.command == "skills":
        if args.export:
            export_skills(args.export)
        else:
            catalog = load_skills_catalog()
            print(f"\n🧩 App Factory Cross-Platform Skills ({len(catalog)} available)\n" + "=" * 60)
            for idx, s in enumerate(catalog, 1):
                print(f"{idx:2d}. {s['name']:<28} : {s['title']}")
                print(f"    {s['description']}")
            print("=" * 60)
            print("Install into agents via: app-factory skills --export [claude|codex|hermes|cursor|all]\n")

    elif args.command == "init":
        init_project(args.path)

    elif args.command == "gate":
        orch = PipelineOrchestrator(args.path)
        res = orch.verify_gate(args.gate_num, test_cmd=args.test_cmd, build_cmd=args.build_cmd)
        status_symbol = "✓ PASSED" if res["passed"] else "✗ FAILED"
        print(f"\n{res['name']}: {status_symbol}")
        if res["errors"]:
            print("\nFindings / Errors:")
            for err in res["errors"]:
                print(f"  {err}")
        print()
        sys.exit(0 if res["passed"] else 1)

    elif args.command == "check":
        orch = PipelineOrchestrator(args.path)
        results = orch.run_all_gates(test_cmd=args.test_cmd, build_cmd=args.build_cmd)
        all_passed = True
        print("\n🏭 App Factory 4-Gate Execution Run\n" + "=" * 45)
        for res in results:
            mark = "✓" if res["passed"] else "✗"
            print(f"[{mark}] Gate {res['gate']}: {res['name']}")
            if not res["passed"]:
                all_passed = False
                for err in res["errors"]:
                    print(f"    {err}")
                break
        print("=" * 45)
        if all_passed:
            print("🚀 All 4 Quality Gates PASSED! Ready for deployment.\\n")
            sys.exit(0)
        else:
            print("🛑 Pipeline blocked at current gate. Fix findings before proceeding.\\n")
            sys.exit(1)

    elif args.command == "status":
        orch = PipelineOrchestrator(args.path)
        state = orch.load_state()
        print("\n📊 App Factory Pipeline Status")
        print(f"  Target Directory: {orch.project_dir}")
        print(f"  Current Gate    : Gate {state.get('current_gate', 1)}")
        print(f"  Completed       : {state.get('completed', False)}")
        print("\nGate History:")
        for g, data in state.get("gate_history", {}).items():
            st = "PASSED" if data.get("passed") else "FAILED"
            print(f"  Gate {g}: {st}")
        print()


if __name__ == "__main__":
    main()
