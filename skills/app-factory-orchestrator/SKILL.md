---
name: app-factory-orchestrator
title: App Factory Multi-Agent Orchestrator
description: Systematic multi-agent pipeline for end-to-end software and mobile app development (Flutter, iOS Swift, Web, CLI).
version: 1.0.0
license: MIT
metadata:
  tags: [gstack, superpowers, multi-agent, app-development, orchestration]
---

# App Factory Multi-Agent Orchestrator

Systematic multi-agent pipeline for end-to-end software and mobile app development. Combines Garry Tan's **gstack** role disciplines (CPO, CSO, Review), Jesse Vincent's **Superpowers** engineering rigor (TDD, atomic plans, worktree isolation), and native host compiler verification.

## Architecture

| Role | Preferred Engine / Model | Responsibility |
|------|--------------------------|----------------|
| **Commander & Delivery Lead** | Hermes Agent / Gemini 3.8 Flash | Pipeline orchestration, Gate enforcement, host toolchain verification |
| **Chief Product Officer & Architect** | Claude Code CLI (Claude 3.7 / 4.6) | Requirements discovery, `/office-hours`, PRD freezing, anti-AI-slop design review |
| **Lead Engineer & Chief Security Officer** | Codex CLI (GPT-5 / GPT-6) | Security auditing (`/cso`), credential leak detection, adversarial code review |
| **Host Toolchain & Compiler** | Real Native Compilers (Xcode / Flutter / Rust / Go) | Physical compiler verification: `xcodebuild`, `flutter build`, `pytest`, `cargo check` |

## The 4 Quality Gates

1. **Gate 1: Architecture & PRD Gate**
   - Validates `docs/PRD.md` and `docs/TASKS.md`.
   - Requires explicit Target User, Core Value, Out of Scope limits, and checklist tasks.
2. **Gate 2: TDD & Implementation Gate**
   - Red-Green TDD discipline.
   - Tests must run and pass on host before proceeding.
3. **Gate 3: Security (CSO) & Code Review Gate**
   - Scans for exposed tokens, private keys, and credential leaks.
   - Audits `docs/REVIEW.md` for unaddressed Critical/High flaws.
4. **Gate 4: Native Shipping & Compilation Gate**
   - Invokes host compilers (`xcodebuild`, `flutter build`, `cargo check`, etc.).
   - Rejects AI self-reports; only exit code 0 permits release.
