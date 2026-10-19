---
name: gate-1-requirements
description: Gate 1 Requirements & Architecture discovery workflow.
version: 1.0.0
---

# Gate 1: Requirements & Architecture Discovery

Before writing any code, execute Gate 1 to freeze scope and prevent scope creep:

1. **Conduct Product Discovery**:
   - Who is the exact target user?
   - What single painful problem does this release solve?
   - What are the explicit boundaries (What will we NOT build)?
2. **Draft `docs/PRD.md`**:
   - Fill in Target User, Core Value, Out of Scope, and Acceptance Criteria.
3. **Draft `docs/TASKS.md`**:
   - Decompose into bite-sized tasks formatted as `- [ ] Task N: Description`.
4. **Verification**:
   - Run `app-factory gate 1` to ensure compliance.
