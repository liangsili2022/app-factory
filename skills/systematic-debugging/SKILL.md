---
name: systematic-debugging
title: Systematic Debugging & Root Cause Forensics
description: Multi-hypothesis, evidence-backed root cause tracing. Replaces trial-and-error code thrashing with scientific diagnostics.
version: 1.0.0
license: MIT
metadata:
  tags: [debugging, troubleshooting, forensics, root-cause, superpowers]
---

# Systematic Debugging & Root Cause Forensics

Inspired by Jesse Vincent's **Superpowers Systematic Debugging**. Prohibits "shotgun debugging" (blindly guessing and tweaking code until tests pass). Mandates scientific hypothesis testing, minimal reproduction, and evidence-first isolation.

## The Iron Laws of Debugging

1. **Never guess**: Every fix must be preceded by an identified, proven root cause.
2. **Reproduce first**: If you cannot reproduce the bug with a deterministic command, script, or test, you do not understand the bug.
3. **Change one variable at a time**: Never apply multiple speculative changes simultaneously.

## 4-Phase Diagnostic Cycle

### Phase 1: Observation & Minimal Reproduction
- Capture the exact failure message, stack trace, and exit code.
- Write a minimal failing test (RED) that reproduces the failure in isolation:
  ```bash
  # Python
  pytest tests/test_failing_case.py -k "test_specific_bug" -vv
  # Node
  npm test -- -t "should reproduce bug"
  ```

### Phase 2: Hypothesis Generation & Tree Search
- Formulate 2 to 3 distinct falsifiable hypotheses:
  - *Hypothesis A (Input boundary)*: Malformed payload or encoding mismatch.
  - *Hypothesis B (State mutation)*: Shared mutable state across async turns.
  - *Hypothesis C (Dependency / Environment)*: Version incompatibility or missing sys lib.
- Add minimal assertions or tracepoints to disprove or confirm each hypothesis.

### Phase 3: Root Cause Isolation (Find the Polluter)
- If test pollution is suspected (a test passes alone but fails in full suite):
  - Run binary search over test order to find the polluter.
  - Check for leaky global variables, unclosed DB connections, or uncleaned temp files.
- If environmental drift is suspected:
  - Diff environment variables, python path, node version, or compiler flags.

### Phase 4: Targeted Fix & Regression Proof
- Implement the minimal fix addressing the confirmed root cause.
- Verify:
  1. The failing reproduction test now passes (GREEN).
  2. The full test suite passes without regressions.
  3. No new speculative flags or workarounds remain in the codebase.
