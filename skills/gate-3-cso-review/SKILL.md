---
name: gate-3-cso-review
title: Gate 3 CSO Security & Review
description: Gate 3 Chief Security Officer & Adversarial Review workflow.
version: 1.0.0
---

# Gate 3: Chief Security Officer (CSO) & Code Review

Before shipping, execute adversarial inspection inspired by gstack `/cso` and `/review`:

1. **CSO Secret Scan**:
   - Check all commits and untracked files for API keys, private keys, and tokens.
   - Run `app-factory gate 3` to execute automated pattern scanning.
2. **Adversarial Code Review**:
   - Review diffs for race conditions, error handling, unhandled edge cases, and memory leaks.
   - Record findings in `docs/REVIEW.md`.
3. **Zero Critical/High Tolerance**:
   - Any Critical or High issue blocks release until remediated.
