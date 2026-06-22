# MultiTimeTracker Overview

MultiTimeTracker is a local-first Android time tracker. The main data lives in the app SQLite database, with sessions and shared tags as the core model.

## Stato e codice
- Repository: `/home/daniele/codex-workspace/projects/MultiTimeTracker`
- Repository locale Windows: `C:/Users/seste/Documents/MTT`
- Branch/commit verificati: `codex/play-store-readiness-roadmap` / `f5938e537ccc94007dd5ed9da6eb0ec643a44a8d` (`#517284`)
- File codice/config/test/script analizzati: 224 su 224
- Stack rilevato: Kotlin, Python, Shell, Gradle, Jetpack Compose, Android
- Validazione `#462918`: `compileDebugKotlin`, `testDebugUnitTest`, `assembleDebug`; Pixel 8a clone `com.example.multitimetracker.devicetest` v525 con 53 instrumentation test, 3 skipped, 0 failed; clone install/launch ADB verificato con PID.
- Validazione `#914506`: `compileDebugKotlin`, `testDebugUnitTest`, `assembleDebug`, `lintDebug`, `assembleRelease`, `bundleRelease` verdi; versione `489`; `applicationId=com.example.multitimetracker`; APK/AAB release generati ma unsigned per secret signing mancanti.
- Validazione `#517284`: upload keystore locale ignorato creato; `app-release.apk` e `app-release.aab` firmati e verificati con `apksigner`/`jarsigner`; install smoke saltato per proteggere device gia occupati da build debug v534.
- Capsulizzazione `#462918`: 100 percento strict stimato per ownership feature auditata; NOW, TAGS, TIMELINE, QUICK_EVENTS, CHAINS, ALERTS, IMPORT_EXPORT, AUDIT_LOG e SINCE_WHEN hanno owner capsule espliciti, MainViewModel resta shell/composition root.
- Play Store `#517284`: readiness offline stimata 88 percento; resta lavoro manuale Play Console/asset/privacy, non lavoro tecnico offline.

## Orientamento rapido
- Entrypoint: `app/src/main/AndroidManifest.xml,app/src/main/java/com/example/multitimetracker/MainActivity.kt,benchmark/src/main/AndroidManifest.xml`
- Core/data: `app/src/main/java/com/example/multitimetracker/AppPatchVersion.kt,app/src/main/java/com/example/multitimetracker/SessionOnlyGuards.kt,app/src/main/java/com/example/multitimetracker/SingleSubmitGuard.kt,app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt,app/src/main/java/com/example/multitimetracker/MainViewModelSnapshotCoordinator.kt,app/src/main/java/com/example/multitimetracker/capsules/sessions/SessionOwnerCapsuleViewModel.kt,app/src/main/java/com/example/multitimetracker/capsules/auditlog/AuditLogCapsuleViewModel.kt,app/src/main/java/com/example/multitimetracker/capsules/sincewhen/SinceWhenCapsuleViewModel.kt,app/src/main/java/com/example/multitimetracker/capsules/importexport/ImportExportCapsuleViewModel.kt`
- Test: `app/src/test/java/com/example/multitimetracker/capsules/CapsuleBoundaryOwnershipTest.kt,app/src/test/java/com/example/multitimetracker/capsules/auditlog/AuditLogCapsuleViewModelTest.kt,app/src/test/java/com/example/multitimetracker/capsules/sincewhen/SinceWhenCapsuleViewModelTest.kt,app/src/test/java/com/example/multitimetracker/capsules/alerts/AlertsCapsuleViewModelTest.kt,app/src/androidTest/java/com/example/multitimetracker/ExampleInstrumentedTest.kt,app/src/androidTest/java/com/example/multitimetracker/MainViewModelRecoveryTest.kt,app/src/androidTest/java/com/example/multitimetracker/SessionOnlyE2eTest.kt,app/src/androidTest/java/com/example/multitimetracker/TimedSessionNotificationFlowTest.kt,app/src/androidTest/java/com/example/multitimetracker/capsules/importexport/ImportExportCapsuleViewModelTest.kt`
- Script/build: `dev/tools/check_hardcoded_ui_strings.py,dev/tools/check_single_submit_confirm_buttons.sh,dev/tools/clean_transients.sh,preflight_check.ps1,app/build.gradle,app/build.gradle.kts,benchmark/build.gradle.kts,build.gradle.kts`
- Play handoff: `dev/human/play_store/privacy_policy.md,dev/human/play_store/data_safety_form.md,dev/human/play_store/store_listing.md,dev/human/play_store/assets_checklist.md,dev/human/play_store/release_signing.md,dev/human/play_store/release_checklist.md,dev/ai/play_store_readiness.md`

## Link
- AI doc: [AI doc](../../../ai/projects/multitimetracker.md)
- Metadata: [dev/project.metadata.json](../../../../projects/MultiTimeTracker/dev/project.metadata.json)
- Legacy docs: [dev/legacy](../../../../projects/MultiTimeTracker/dev/legacy)
- Repository: [repo path](../../../../projects/MultiTimeTracker)
