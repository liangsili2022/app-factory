"""Gate 1: Requirement & Architecture Gate (gstack office-hours & autoplan style).

Verifies that PRD and atomic task breakdown exist with required forcing sections:
- Target User
- Core Value / Problem Statement
- Out of Scope (What NOT to build)
- Measurable Acceptance Criteria
"""

import os
from typing import List, Tuple


REQUIRED_PRD_SECTIONS = [
    "Target User",
    "Core Value",
    "Out of Scope",
    "Acceptance Criteria",
]


def run_gate1(project_dir: str) -> Tuple[bool, List[str]]:
    """Validate Gate 1 artifacts (docs/PRD.md and docs/TASKS.md)."""
    errors = []
    prd_path = os.path.join(project_dir, "docs", "PRD.md")
    tasks_path = os.path.join(project_dir, "docs", "TASKS.md")

    if not os.path.isfile(prd_path):
        errors.append("Missing docs/PRD.md. Run Gate 1 to generate architectural spec.")
    else:
        with open(prd_path, "r", encoding="utf-8") as f:
            content = f.read()
        for sec in REQUIRED_PRD_SECTIONS:
            if sec.lower() not in content.lower():
                errors.append(f"PRD is missing required forcing section: '{sec}'")

    if not os.path.isfile(tasks_path):
        errors.append("Missing docs/TASKS.md. Run Gate 1 task decomposition.")
    else:
        with open(tasks_path, "r", encoding="utf-8") as f:
            tasks_content = f.read()
        if "- [ ]" not in tasks_content and "- [x]" not in tasks_content:
            errors.append("docs/TASKS.md contains no verifiable checkbox tasks (- [ ]).")

    passed = len(errors) == 0
    return passed, errors
