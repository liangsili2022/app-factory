# 🏭 App Factory (应用工厂)

> **Multi-Agent Software Engineering Pipeline**
> Combining Garry Tan's **gstack** role disciplines, Jesse Vincent's **Superpowers** engineering rigor, and real-machine compiler verification.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Multi-Agent](https://img.shields.io/badge/Agents-Claude%20%7C%20Codex%20%7C%20Hermes-purple.svg)](#multi-agent-matrix)
[![Quality Gates](https://img.shields.io/badge/Gates-4--Stage%20Enforced-green.svg)](#the-4-quality-gates)

---

## 💡 Overview

Single-agent coding tools are prone to **hallucinated success**: an LLM will claim "build succeeded" or "all tests pass" when code fails to compile or tests were never executed.

**App Factory** solves this by establishing a disciplined, heterogeneous multi-agent software factory with **4 enforceable quality gates** backed by physical host compilers (Xcode, Flutter, Rust, Node, Python).

- **Inspired by [gstack](https://github.com/garrytan/gstack) (Garry Tan / Y Combinator)**: Adopts startup executive personas — Chief Product Officer (`/office-hours`, `/autoplan`), Chief Security Officer (`/cso`), and Design Review (`/design-review`).
- **Inspired by [Superpowers](https://github.com/obra/superpowers) (Jesse Vincent / obra)**: Adopts strict engineering mechanics — Red-Green Test-Driven Development (TDD), atomic implementation plans, and worktree isolation.
- **Powered by Hermes Agent & Host Toolchains**: Rejects self-reported completion; only real compiler exit codes (`exit code 0`) and physical test execution allow an app to ship.

---

## 🏛 Architecture & Multi-Agent Matrix

```
                     ┌────────────────────────────────────────┐
                     │         Commander & Orchestrator       │
                     │    Hermes Agent / Gemini 3.8 Flash     │
                     └───────────────────┬────────────────────┘
                                         │
        ┌────────────────────────────────┼────────────────────────────────┐
        ▼                                ▼                                ▼
┌───────────────────────┐  ┌───────────────────────────┐  ┌───────────────────────────────┐
│     Gate 1: PRD       │  │       Gate 2: TDD         │  │     Gate 3: Security & Review │
│   Claude Code (CPO)   │  │   Superpowers Red-Green   │  │       Codex CLI (CSO)         │
│  - /office-hours      │  │  - Write failing test     │  │  - Zero-leak credential scan  │
│  - /plan-ceo-review   │  │  - Implement minimal code │  │  - Adversarial code review    │
│  - Freeze docs/PRD.md │  │  - Host verification pass │  │  - Zero Critical/High policy  │
└───────────────────────┘  └───────────────────────────┘  └───────────────────────────────┘
                                         │
                                         ▼
                     ┌────────────────────────────────────────┐
                     │       Gate 4: Native Shipping Gate     │
                     │     Host Native Toolchain & Compilers  │
                     │  - xcodebuild / flutter build / cargo  │
                     │  - Physical exit code 0 required       │
                     └────────────────────────────────────────┘
```

| Role | Agent / Engine | Preferred Model | Primary Responsibility |
|------|----------------|-----------------|------------------------|
| **Delivery Commander** | Hermes Agent | Gemini 3.8 Flash | Pipeline orchestration, gate enforcement, build logs, TestFlight/store release |
| **CPO & Architect** | Claude Code CLI | Claude 3.7 / 4.6 | Requirements discovery (`/office-hours`), anti-AI-slop design, PRD locking |
| **CSO & Tech Lead** | Codex CLI | GPT-5 / GPT-6 | Security audit (`/cso`), secret leak scanning, adversarial code review |
| **Physical QA** | Host Toolchain | Local compilers | Real `xcodebuild`, `flutter build`, `pytest`, `cargo check` execution |

---

## 🚦 The 4 Quality Gates

1. **Gate 1: Architecture & PRD Gate**
   - Validates `docs/PRD.md` and `docs/TASKS.md`.
   - Mandates: **Target User**, **Core Value**, **Out of Scope** (what NOT to build), and verifiable checklist tasks (`- [ ]`).
2. **Gate 2: Implementation & TDD Gate**
   - Enforces Red-Green-Refactor testing discipline.
   - Tests must exist and pass natively on the host machine.
3. **Gate 3: Security (CSO) & Code Review Gate**
   - Automated scan for hardcoded tokens, secret keys (`sk-...`, `ghp_...`), and credentials.
   - Audits `docs/REVIEW.md` for unresolved Critical or High defects.
4. **Gate 4: Native Shipping & Compilation Gate**
   - Triggers native compilers (`xcodebuild`, `flutter build`, `cargo check`, etc.).
   - Discards agent self-reports: only host compiler exit code `0` passes.

---

## 🚀 Quick Start

### 1. Installation

Clone and install locally:

```bash
git clone https://github.com/huppy-ai/app-factory.git
cd app-factory
pip install -e .
```

Or run directly without installation:

```bash
./bin/app-factory --help
```

### 2. Check Toolchain Health

Inspect available compilers, runtimes, and AI agent CLIs on your machine:

```bash
app-factory doctor
```

Example output:
```text
🏭 App Factory Toolchain Doctor
========================================

[Core Runtimes]
  ✓ Git                        : git version 2.50.1
  ✓ Python 3                   : Python 3.9.6
  ✓ Node.js                    : v22.23.1

[AI Agent CLIs]
  ✓ Claude Code                : 2.1.237 (Claude Code)
  ✓ Codex CLI                  : codex-cli 0.163.0
  ✓ Hermes Agent               : Hermes Agent v0.21.5
  ✓ Cursor CLI                 : 3.25.9

[Native Compilers & SDKs]
  ✓ Xcode CLI (xcodebuild)     : Xcode 26.3
  ✓ Flutter SDK                : Flutter 3.41.0
  ✓ Rust (cargo)               : cargo 1.94.1
  ✓ Go (go)                    : go version go1.26.0

========================================
✓ All essential runtime dependencies are satisfied!
```

### 3. Initialize a Project

Initialize standard PRD, Task, and Review templates in any existing or new repo:

```bash
cd my-app
app-factory init
```

This creates:
- `docs/PRD.md`
- `docs/TASKS.md`

### 4. Run Quality Gates

Verify individual gates during development:

```bash
# Validate Gate 1 (PRD & Scope boundaries)
app-factory gate 1

# Validate Gate 2 (Run test suite)
app-factory gate 2

# Validate Gate 3 (CSO secret scan & code review)
app-factory gate 3

# Validate Gate 4 (Host compiler check)
app-factory gate 4
```

Or run all 4 gates sequentially before shipping:

```bash
app-factory check
```

---

## 🧩 Portable Skills

App Factory ships with ready-to-use skills in `skills/` compatible with:
- **Claude Code** (`~/.claude/skills/`)
- **Codex CLI** (`~/.codex/skills/`)
- **Hermes Agent** (`~/.hermes/skills/`)
- **Cursor IDE** (Rules & Composer)

---

## 🇨🇳 中文说明 (Chinese Overview)

**App Factory** 是一个结构化的多模型/多 Agent 软件工程工厂流水线：
- **融合两大家之长**：将 Garry Tan 的 **gstack**（角色分工、CPO 架构、CSO 安全审计）与 Jesse Vincent 的 **Superpowers**（极端严苛的 TDD 红绿测试、原子化任务拆解、独立工作区隔离）深度结合。
- **异构编队最优解**：Claude Code 负责前端需求与防 AI 粗制感（CPO）；Codex 负责安全防御与对抗式代码审查（CSO）；Hermes (Gemini 3.8 Flash) 担任总指挥调度本地真机编译器。
- **四道物理门禁（4-Gate）**：
  1. **Gate 1**：需求与范围锁死（PRD 必须包含 Target User, Core Value, Out of Scope，杜绝需求蔓延）。
  2. **Gate 2**：TDD 红绿测试驱动（必须有测试且真实跑通）。
  3. **Gate 3**：CSO 凭据泄露扫描与对抗式 Review（严禁任何未脱敏 Key 进代码）。
  4. **Gate 4**：宿主机编译器真机验证（Xcode / Flutter / Cargo 真实返回 Exit Code 0 才算完成）。

---

## 📄 License

MIT License. Copyright (c) 2026 Huppy AI & Liang Sili.
Contributions and extensions are welcome!
