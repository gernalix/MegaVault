# Android App Template

Reusable terminal-only Android Studio starter template.

- Template path: `/home/daniele/codex-workspace/android-app-template`
- Generator: `create_android_app_from_template`
- Template package: `com.gernalix.androidapptemplate`
- Preserved stack: Gradle wrapper, Android Gradle Plugin 9.2.1, Kotlin 2.2.10, Compose BOM 2026.02.01, `libs.versions.toml`
- Origin: one-time frozen snapshot extracted from the original clean `Soldi` starter.
- Guardrail: `Soldi` is now a real app, not a live template.
- New apps must be generated from this template, never from `Soldi`.
- Future `Soldi` changes must not flow back into this template unless an explicit template migration is requested.
- Verified generated apps: `Soldi`, `Sostanze`, `Luoghi`

Generate a new app:

```bash
/home/daniele/codex-workspace/android-app-template/create_android_app_from_template APP_NAME PACKAGE_NAME DESTINATION
```
