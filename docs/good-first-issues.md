# Good first issues

Five small, independent starter tasks. These are proposed contributions, not
completed features or issues already filed on GitHub. Pick one per pull request.
Run `python3 -m unittest discover -s tests -v` from the repository root to verify
changes; keep tests independent of installed agent CLIs and network access.

## 1. Document CLI exit codes

- **Start here:** `app_factory/cli.py`, `README.md`.
- **Task:** add a short reference for success, failed gates/doctor checks, and
  invalid command-line arguments.
- **Acceptance:** include reproducible commands and observed exit codes 0, 1,
  and 2; use a temporary directory for the failing Gate 1 example.

## 2. Cover repeated project initialization

- **Start here:** `app_factory/cli.py:init_project`, `tests/test_cli.py`.
- **Task:** add a regression test that initializes a temporary project, replaces
  template text with custom content, and initializes it again.
- **Acceptance:** both custom documents remain byte-for-byte unchanged; a
  separate case confirms a missing document is created without altering the
  existing one. Clean up temporary directories.

## 3. Cover case-insensitive PRD section matching

- **Start here:** `app_factory/gates/gate1_architecture.py`, `tests/test_gates.py`.
- **Task:** add focused tests for lowercase/mixed-case required section names
  and for a PRD missing one required section.
- **Acceptance:** case variations pass with a valid task checklist; the missing
  section fails with a finding naming that section. Use temporary fixtures.

## 4. Add examples for checking another directory

- **Start here:** `app_factory/cli.py`, `docs/demo/README.md`.
- **Task:** document `init <path>`, `gate 1 --path <path>`, and
  `status --path <path>` using a sample directory containing spaces.
- **Acceptance:** all commands work when copied from outside the target
  directory; paths are quoted, expected output is explained, and the guide
  notes that individual `gate` runs do not persist pipeline history.

## 5. Cover malformed pipeline state recovery

- **Start here:** `app_factory/orchestrator.py:load_state`, `tests/test_cli.py`.
- **Task:** add a test for an invalid JSON `.app-factory-state.json` file in a
  temporary project.
- **Acceptance:** loading does not raise, returns the default current gate 1
  and empty history, and leaves the original malformed file unchanged. Include
  a valid-state case confirming stored history still loads.
