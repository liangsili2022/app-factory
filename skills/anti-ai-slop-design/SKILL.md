---
name: anti-ai-slop-design
title: Anti-AI-Slop Design & UI Review
description: Eliminates generic, unpolished AI slop in web and mobile apps to meet commercial standards (Apple HIG / Material 3).
version: 1.0.0
license: MIT
metadata:
  tags: [design, ui-review, gstack, apple-hig, frontend]
---

# Anti-AI-Slop Design & UI Review

Inspired by Garry Tan's **gstack `/design-review`** methodology. AI-generated UIs frequently suffer from "AI Slop" — generic purple/blue gradients, centered floating cards, missing active states, inconsistent spacing tokens, and non-native feel. This skill audits interfaces and upgrades them to consumer-grade excellence.

## Common "AI Slop" Anti-Patterns to Kill

1. **The Purple/Indigo Gradient Trap**: Overuse of generic `#6366F1` / `#8B5CF6` gradient hero buttons.
2. **Missing Interaction States**: Buttons without `:hover`, `:active`, `:focus-visible`, or disabled styling.
3. **Floating Card Syndrome**: Excessive nested borders, multiple drop shadows, and ungrounded centered boxes.
4. **Non-Native Mobile Slop**: Web-like back buttons on iOS instead of standard navigation bars and native swipe-to-pop.
5. **Arbitrary Padding & Type Scale**: Random `13px`, `17px`, `22px` values instead of a strict 4px/8px rhythm grid.

## The 5-Point Design Quality Audit

Before submitting UI code, verify against these 5 pillars:

### 1. Platform-Native Ergonomics
- **iOS / macOS**: Respect safe areas, Dynamic Island, status bar heights, and system standard icons (SF Symbols).
- **Android**: Follow Material 3 elevation, dynamic color rules, and system navigation bar padding.
- **Web**: Responsive layout from 320px mobile to 4K ultrawide; avoid horizontal scrollbars on desktop.

### 2. Spacing Rhythm & Typography
- Strict 8-point baseline grid: `4px`, `8px`, `12px`, `16px`, `24px`, `32px`, `48px`, `64px`.
- High-contrast typography: Body text minimum 16px on mobile (prevents iOS auto-zoom on input focus).
- Content-informed layout: Truncation with ellipsis (`text-overflow: ellipsis`) for dynamic text fields.

### 3. Polish & Tactility
- Add subtle haptics on mobile interactions (`UIImpactFeedbackGenerator`).
- Smooth animations (150ms-250ms with ease-out cubic-bezier curves; never laggy 500ms+ linear fades).
- Empty states with illustrative prompts and clear primary calls-to-action (CTAs).

### 4. Accessibility & Contrast
- Minimum WCAG AA color contrast ratio (4.5:1 for normal text, 3:1 for large text).
- Minimum touch target size: 44x44 pt (iOS) or 48x48 dp (Android).

### 5. Verification Checklist
- [ ] Tested on dark mode and light mode without unreadable text.
- [ ] No unstyled raw browser defaults (checkboxes, select dropdowns, alerts).
- [ ] Keyboard navigation and Tab focus rings work cleanly.
