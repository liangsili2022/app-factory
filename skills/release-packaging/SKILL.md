---
name: release-packaging
title: Release Packaging & Store Readiness
description: Automated production packaging, code signing verification, changelog generation, and distribution readiness.
version: 1.0.0
license: MIT
metadata:
  tags: [release, packaging, app-store, testflight, codesign, devops]
---

# Release Packaging & Store Readiness

End-to-end workflow for packaging production-ready artifacts, auditing code signing, generating semantic changelogs, and verifying distribution readiness across mobile stores, package registries, and GitHub Releases.

## Pre-Release Audit Checklist

Before tagging or shipping any release, verify the 5 readiness gates:

### 1. Versioning & Manifest Consistency
- Version number follows Semantic Versioning (`MAJOR.MINOR.PATCH`).
- All platform manifests are synchronized:
  - iOS: `CFBundleShortVersionString` and `CFBundleVersion` in `Info.plist` or `project.pbxproj`.
  - Flutter: `version: X.Y.Z+BUILD` in `pubspec.yaml`.
  - Python: `version = "X.Y.Z"` in `pyproject.toml`.
  - Node: `"version": "X.Y.Z"` in `package.json`.

### 2. Code Signing & Entitlements Security
- **iOS / macOS**:
  - Verify provisioning profile validity and bundle identifier match.
  - Audit `*.entitlements` file: ensure no unnecessary capabilities are claimed (e.g. HealthKit, CarPlay without justification).
  ```bash
  codesign -dv --entitlements - path/to/App.app
  ```
- **Android / Cross-Platform**:
  - Confirm release APK/AAB is signed with production keystore, not debug keystore.
  - Proguard/R8 obfuscation rules configured without breaking reflection-dependent libraries.

### 3. Automated Changelog Generation
Generate a structured, user-facing changelog from git commits since the last tag:
```bash
# Extract user-facing commits since previous release tag
PREV_TAG=$(git describe --tags --abbrev=0 2>/dev/null || git rev-list --max-parents=0 HEAD)
git log "$PREV_TAG..HEAD" --pretty=format:"* %s (%h)" --no-merges
```

### 4. Build Artifact Integrity
- Compute and record SHA-256 checksums for all release binaries:
  ```bash
  shasum -a 256 dist/* > dist/SHA256SUMS.txt
  ```
- Ensure no debug flags, mock backends, or development environment variables are baked into production builds.

### 5. Final Release Verification Command
Run App Factory's complete verification suite against the project:
```bash
app-factory check --path .
```
Only proceed to upload or distribute when all 4 gates pass with exit code 0.
