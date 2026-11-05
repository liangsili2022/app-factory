# Quick start demo

A two-minute terminal walkthrough for first-time contributors. Requires Bash
and Python 3.9+ on PATH; no package installation, network access, agent account,
or native SDK is needed.

From the repository root:

```bash
bash docs/demo/quick-start.sh
```

The script resolves the checkout relative to its own location, so it also works
when invoked by absolute path from another directory.

## Presenter script

1. **Introduce the CLI:** show `--help` and the bundled skills catalog. Explain
   that listing skills does not install or export them into an agent's settings.
2. **Show a blocked project:** run Gate 1 on an empty temporary directory. Expect
   `FAILED`, findings for missing `docs/PRD.md` and `docs/TASKS.md`, and exit code 1.
   The script treats this failure as an expected demonstration step.
3. **Initialize the documents:** `init` creates PRD and task templates. Explain
   the Target User, Core Value, Out of Scope, and Acceptance Criteria sections.
4. **Repeat the gate:** expect `Gate 1: Architecture & PRD: ✓ PASSED` and the
   final `Demo complete` message. The script exits with code 0 and deletes its
   temporary directory, including on an unexpected failure.

Gate 1 currently checks section names and task checkboxes, so placeholders can
pass. This demo proves the document-checking flow, not product readiness or a
complete four-gate release. Fill in real requirements before implementation;
Gates 2–4 require the project's tests, review, and relevant build tools.

If `python3` is missing or older than 3.9, install a supported Python version and
retry. An unexpected command failure stops the script; inspect its findings
before rerunning.
