---
name: gate-4-native-shipping
description: Gate 4 Host compiler verification & production shipping workflow.
version: 1.0.0
---

# Gate 4: Host Compiler Verification & Shipping

Never trust AI self-reports that a build succeeded. Only real compiler exit codes matter.

1. **Host Compilation**:
   - iOS: Run real `xcodebuild` build against target scheme.
   - Flutter: Run `flutter analyze && flutter build ipa --no-codesign` (or appbundle/web).
   - Rust: Run `cargo check && cargo build --release`.
   - Python: Run `python3 -m compileall -q .`.
2. **Verification**:
   - Run `app-factory gate 4` or `app-factory check`.
   - Gate 4 only passes when the host compiler returns exit code 0.
