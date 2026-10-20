# 🏭 App Factory (应用工厂)

> **Multi-Agent Software Engineering Pipeline**
> Combining Garry Tan's **gstack** role disciplines, Jesse Vincent's **Superpowers** engineering rigor, and real-machine compiler verification.
> Built for the Top 10+ mainstream AI coding agents across big tech and open source.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Multi-Agent](https://img.shields.io/badge/Top%2010+%20Agents-Supported-purple.svg)](#supported-top-ai-coding-agents)
[![Quality Gates](https://img.shields.io/badge/Gates-4--Stage%20Enforced-green.svg)](#the-4-quality-gates)
[![Skills](https://img.shields.io/badge/Skills-10%20Portable%20Packs-orange.svg)](#-10-battle-tested-cross-platform-skills)

---

## 💡 Overview

Single-agent coding tools are prone to **hallucinated success**: an LLM will claim "build succeeded" or "all tests pass" when code fails to compile or tests were never executed.

**App Factory** solves this by establishing a disciplined, heterogeneous multi-agent software factory with **4 enforceable quality gates** backed by physical host compilers (Xcode, Flutter, Rust, Node, Python, Go).

- **Inspired by [gstack](https://github.com/garrytan/gstack) (Garry Tan / Y Combinator)**: Adopts startup executive personas — Chief Product Officer (`/office-hours`, `/autoplan`), Chief Security Officer (`/cso`), and Design Review (`/design-review`).
- **Inspired by [Superpowers](https://github.com/obra/superpowers) (Jesse Vincent / obra)**: Adopts strict engineering mechanics — Red-Green Test-Driven Development (TDD), atomic implementation plans, and worktree isolation.
- **Powered by Hermes Agent & Host Toolchains**: Rejects self-reported completion; only real compiler exit codes (`exit code 0`) and physical test execution allow an app to ship.

---

## 🤖 Supported Top AI Coding Agents

App Factory automatically detects, orchestrates, and exports skills to the top 10+ mainstream AI coding agents:

| Agent / CLI | Command | Maintainer / Ecosystem | Role in App Factory |
|-------------|---------|------------------------|---------------------|
| **Claude Code** | `claude` | Anthropic | CPO & Architect (`/office-hours`, PRD locking) |
| **OpenAI Codex** | `codex` | OpenAI | Lead Engineer & CSO (`/cso`, security audit) |
| **Hermes Agent** | `hermes` | Nous Research | Factory Commander & host pipeline orchestrator |
| **Cursor CLI** | `cursor` | Anysphere | Interactive IDE agent & Composer driver |
| **Muse** | `muse` | Apple | Swift / Apple platform-native specialist |
| **Grok Bot / CLI** | `grok` / `grok-bot` | xAI | Fast reasoning & real-time knowledge assistant |
| **GitHub Copilot CLI** | `copilot` / `gh copilot` | GitHub / Microsoft | Git workflow & enterprise compliance checks |
| **Antigravity** | `agy` | Google Antigravity / Gemini | Unlimited batch reasoning & high-concurrency loops |
| **OpenCode** | `opencode` | OpenCode Community | Self-hosted open coding agent |
| **Aider** | `aider` | Paul Gauthier | Multi-file git-integrated terminal pair programmer |
| **Windsurf** | `windsurf` | Codeium | Flow-state inline assistant |
| **Devin CLI** | `devin` | Cognition AI | Autonomous background software engineer |

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

## 🧩 10 Battle-Tested Cross-Platform Skills

App Factory comes preloaded with **10 standardized, agent-agnostic skills** located in `skills/`:

| # | Skill Name | Description |
|---|------------|-------------|
| 1 | **`app-factory-orchestrator`** | Master pipeline controller enforcing all 4 gates across agents. |
| 2 | **`gate-1-requirements`** | CPO requirements discovery, scope freeze, and PRD generation. |
| 3 | **`gate-2-tdd`** | Superpowers-style Red-Green-Refactor test-driven development. |
| 4 | **`gate-3-cso-review`** | Chief Security Officer credential scan & adversarial review. |
| 5 | **`gate-4-native-shipping`** | Real host compiler execution (`xcodebuild`, `flutter`, `cargo`). |
| 6 | **`anti-ai-slop-design`** | Eliminates generic AI UI slop; enforces Apple HIG & Material 3. |
| 7 | **`subagent-delegation`** | Dispatches subagents in isolated git worktrees with progress ledgers. |
| 8 | **`systematic-debugging`** | Multi-hypothesis root cause tracing & test polluter detection. |
| 9 | **`mobile-app-qa`** | iOS & Flutter simulator automation, touch targets, and responsiveness. |
| 10 | **`release-packaging`** | Code signing audits, semantic changelog, and store readiness. |

---

## 🚀 Quick Start

### 1. Installation

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

Inspect all compilers, runtimes, and the Top 10+ AI agent CLIs:

```bash
app-factory doctor
```

Example output:
```text
🏭 App Factory Toolchain Doctor
=======================================================

[Core Runtimes]
  Status: 3/3 available
  ✓ Git                        : git version 2.50.1
  ✓ Python 3                   : Python 3.9.6
  ✓ Node.js                    : v22.23.1

[Top AI Coding Agents]
  Status: 6/12 available
  ✓ Claude Code                : 2.1.237 (Claude Code)
  ✓ OpenAI Codex               : codex-cli 0.163.0
  ✓ Hermes Agent               : Hermes Agent v0.21.5
  ✓ Cursor CLI                 : 3.25.9
  · Muse                       : Not found in PATH
  ✓ Grok Bot / CLI             : grok 1.0.25
  · GitHub Copilot CLI         : Not found in PATH
  ✓ Antigravity (agy)          : 1.4.3
  · OpenCode                   : Not found in PATH
  · Aider                      : Not found in PATH
  · Windsurf                   : Not found in PATH
  · Devin CLI                  : Not found in PATH

[Native Compilers & SDKs]
  Status: 4/4 available
  ✓ Xcode CLI (xcodebuild)     : Xcode 26.3
  ✓ Flutter SDK                : Flutter 3.41.5
  ✓ Rust (cargo)               : cargo 1.94.1
  ✓ Go (go)                    : go version go1.26.0

=======================================================
✓ All essential runtime dependencies are satisfied!
```

### 3. List and Export Skills to Agents

Inspect the 10 built-in skills:
```bash
app-factory skills
```

Export skills directly into your preferred AI agent environment:
```bash
# Export to Claude Code (~/.claude/skills/)
app-factory skills --export claude

# Export to Codex (~/.codex/skills/)
app-factory skills --export codex

# Export to Hermes Agent (~/.hermes/skills/app-factory/)
app-factory skills --export hermes

# Export to all available agents at once
app-factory skills --export all
```

### 4. Initialize a Project

Initialize standard PRD and Task templates in any repository:

```bash
cd my-app
app-factory init
```

### 5. Run Quality Gates

```bash
# Verify individual gates
app-factory gate 1
app-factory gate 2
app-factory gate 3
app-factory gate 4

# Run all 4 gates sequentially before shipping
app-factory check
```

---

## 🇨🇳 中文说明 (Chinese Overview)

**App Factory** 是一个结构化的多模型/多 Agent 软件工程工厂流水线：
- **覆盖主流前 10+ 款 AI Agent**：
  - 深度支持并自动体检：**Claude Code、OpenAI Codex、Hermes Agent、Cursor、Muse、Grok Bot、GitHub Copilot、Antigravity、OpenCode、Aider、Windsurf、Devin**。
- **融合两大家之长**：将 Garry Tan 的 **gstack**（角色分工、CPO 架构、CSO 安全审计、UI 去 Slop）与 Jesse Vincent 的 **Superpowers**（极端严苛的 TDD 红绿测试、原子化任务拆解、独立工作区隔离）深度结合。
- **开箱即用 10 大跨平台技能包**：
  1. `app-factory-orchestrator`：全周期 4-Gate 总指挥调度
  2. `gate-1-requirements`：CPO 需求推敲与边界锁定
  3. `gate-2-tdd`：Superpowers 红绿测试驱动开发
  4. `gate-3-cso-review`：CSO 凭据防泄露与对抗审查
  5. `gate-4-native-shipping`：物理真机编译门禁
  6. `anti-ai-slop-design`：UI 质感审查（干掉 AI 廉价感，符合 Apple HIG / Material 3）
  7. `subagent-delegation`：Git Worktree 独立工作区与子 Agent 委派
  8. `systematic-debugging`：科学归因排障（拒绝瞎猜乱改，精准抓出污染源）
  9. `mobile-app-qa`：移动端 iOS / Flutter 模拟器真机巡检
  10. `release-packaging`：发版打包、签名校验与更新日志自动化
- **一键导出技能到任意 Agent**：
  运行 `app-factory skills --export all`，一键将 10 大技能分发至 Claude Code、Codex、Hermes 与 Cursor。

---

## 📄 License

MIT License. Copyright (c) 2026 Huppy AI & Liang Sili.
Contributions and extensions are welcome!
