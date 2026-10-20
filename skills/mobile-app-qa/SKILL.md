---
name: mobile-app-qa
title: Mobile App QA & Simulator Verification
description: Automated mobile quality audit for iOS (Swift/SwiftUI) and Flutter. Tests UI responsiveness, simulator rendering, and touch ergonomics.
version: 1.0.0
license: MIT
metadata:
  tags: [mobile, ios, flutter, qa, simulator, testing]
---

# Mobile App QA & Simulator Verification

Automated quality assurance playbook for iOS (SwiftUI) and Flutter mobile apps. Validates device responsiveness, touch interactions, permission flows, and edge cases before submitting to Gate 4.

## Core Verification Checkpoints

### 1. Xcode Simulator Headless Verification
Drive Xcode simulators programmatically to verify app launch, layout stability, and crash-free runtime:
```bash
# List available iOS simulators
xcrun simctl list devices available | grep -E "iPhone (15|16)"

# Boot target simulator
xcrun simctl boot "iPhone 16 Pro"

# Install and launch app bundle
xcrun simctl install booted path/to/App.app
xcrun simctl launch booted com.example.app

# Capture screenshot for visual audit
xcrun simctl io booted screenshot ./docs/screenshots/launch-verification.png
```

### 2. Flutter Native Health Audit
For Flutter cross-platform projects:
```bash
# 1. Static analysis and deprecation warnings
flutter analyze --fatal-infos

# 2. Complete unit and widget tests
flutter test --coverage

# 3. Dry-run release compilation
flutter build ipa --no-codesign --release
```

### 3. Gesture & Touch Target Ergonomics
- Minimum touch target 44×44 pt for all interactive buttons and list items.
- Support for dynamic type scaling (accessibility font sizing) without text truncation or layout overflow (`RenderFlex overflowed`).
- Proper keyboard avoidance: Text inputs must automatically scroll above software keyboard when focused.

### 4. Network Offline & Low-Bandwidth Handling
- Graceful degradation when offline: display cached data or helpful empty states, not generic red error screens or infinite spinners.
- Network retry with exponential backoff on transient 5xx / timeout errors.
- Skeleton loaders instead of blocking full-screen loaders.
