---
name: subagent-delegation
title: Subagent Delegation & Worktree Isolation
description: Coordinate parallel or sequential subagent execution in isolated git worktrees with strict ledger tracking.
version: 1.0.0
license: MIT
metadata:
  tags: [subagents, superpowers, git-worktrees, delegation, orchestration]
---

# Subagent Delegation & Worktree Isolation

Inspired by Jesse Vincent's **Superpowers Subagent-Driven Development (SDD)**. Prevents AI context pollution and branch collisions by executing independent tasks in isolated Git worktrees with dedicated task briefs and progress ledgers.

## When to Use

- Running multi-task implementations where a single context window would overflow or degrade in quality.
- Dispatching parallel tasks across different subagents (e.g. Claude Code for frontend, Codex for backend).
- Protecting the main working tree from unverified experimental edits and temporary build artifacts.

## Core Rules of Subagent Delegation

### 1. The Worktree Isolation Rule
Never allow subagents to execute write operations directly on the user's primary working tree while they are actively coding.
```bash
# Create dedicated task worktree
git worktree add -b "task/feature-subtask" ".worktrees/task-1" HEAD
```

### 2. The Plan-Scoped Progress Ledger
Every delegated plan must maintain a verifiable ledger recording exact commit SHAs and test outcomes:
- Location: `.app-factory/sdd/<plan-id>/ledger.jsonl`
- Format per task:
  ```json
  {"task_id": 1, "commit_sha": "a1b2c3d", "test_exit_code": 0, "status": "GREEN", "timestamp": 1792442000}
  ```

### 3. Self-Contained Task Briefs
Never instruct a subagent with vague directives like "implement Task 2". Provide a complete self-contained brief:
1. Target files to modify or create.
2. Exact function signatures and interfaces.
3. Specific test command to verify completion.
4. Boundaries of what NOT to touch.

### 4. Reconcile & Cleanup
Once all subtasks in a worktree pass Gate 2 (TDD) and Gate 3 (CSO):
1. Review diff against target branch (`git diff main...HEAD`).
2. Fast-forward merge or squash merge into target feature branch.
3. Prune the temporary worktree:
   ```bash
   git worktree remove --force ".worktrees/task-1"
   git branch -d "task/feature-subtask"
   ```
