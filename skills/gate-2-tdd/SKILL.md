---
name: gate-2-tdd
title: Gate 2 TDD & Implementation
description: Gate 2 Test-Driven Development execution workflow.
version: 1.0.0
---

# Gate 2: Test-Driven Development (TDD)

Follow the Red-Green-Refactor iron rule from Superpowers:

1. **Write Failing Test First (RED)**:
   - Create tests specifying expected behavior before writing feature code.
   - Run the test suite on host to verify failure.
2. **Implement Minimal Code (GREEN)**:
   - Write only enough code to make tests pass.
   - Verify tests pass on host toolchain.
3. **Refactor**:
   - Clean up code and remove duplication while keeping tests green.
4. **Verification**:
   - Run `app-factory gate 2` to confirm test suite integrity.
