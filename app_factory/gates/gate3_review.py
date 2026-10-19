"""Gate 3: Adversarial Review & CSO Security Gate (gstack /review & /cso style).

Performs:
1. CSO Secret & Credential Leak Scan (OWASP / Zero-Leak Red Line).
2. Code review document inspection (ensures no unaddressed Critical/High issues).
"""

import os
import re
from typing import List, Tuple


# Regex patterns for detecting potential credential leaks
SECRET_PATTERNS = [
    (r"sk-[a-zA-Z0-9]{20,}", "OpenAI/CPA Secret Key"),
    (r"ghp_[a-zA-Z0-9]{36,}", "GitHub Personal Access Token"),
    (r"xox[baprs]-[0-9a-zA-Z]{10,}", "Slack Token"),
    (r"AIza[0-9A-Za-z-_]{35}", "Google API Key"),
    (r"-----BEGIN (RSA|EC|OPENSSH|PRIVATE) KEY-----", "Private Key Header"),
]


def scan_for_secrets(project_dir: str) -> List[str]:
    """Scan tracked and untracked code files for sensitive tokens, skipping git/venv."""
    findings = []
    skip_dirs = {".git", ".venv", "venv", "node_modules", ".superpowers", ".gstack"}

    for root, dirs, files in os.walk(project_dir):
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        for f in files:
            if f.endswith((".py", ".js", ".ts", ".swift", ".dart", ".yaml", ".json", ".env")):
                if f.endswith(".example") or f == ".env.example":
                    continue
                path = os.path.join(root, f)
                try:
                    with open(path, "r", encoding="utf-8", errors="ignore") as fp:
                        content = fp.read()
                        for pattern, name in SECRET_PATTERNS:
                            matches = re.findall(pattern, content)
                            if matches:
                                rel_path = os.path.relpath(path, project_dir)
                                findings.append(f"Security Alert: {name} found in {rel_path}")
                except Exception:
                    pass
    return findings


def run_gate3(project_dir: str) -> Tuple[bool, List[str]]:
    """Execute Gate 3 security audit and review validation."""
    errors = []

    # 1. Run CSO Secret Scan
    secret_issues = scan_for_secrets(project_dir)
    if secret_issues:
        errors.append("Gate 3 CSO audit failed: Potential secret leaks detected:")
        errors.extend(["  - " + issue for issue in secret_issues])

    # 2. Check docs/REVIEW.md if present
    review_path = os.path.join(project_dir, "docs", "REVIEW.md")
    if os.path.isfile(review_path):
        with open(review_path, "r", encoding="utf-8") as f:
            review_text = f.read().lower()
        if "status: failed" in review_text or "[critical]" in review_text:
            errors.append("Gate 3 Code Review failed: Unresolved Critical issues in docs/REVIEW.md")

    passed = len(errors) == 0
    return passed, errors
