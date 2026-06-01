# MultiTimeTracker Overview

MultiTimeTracker is a local-first Android time tracker. The main data lives in the app SQLite database, with sessions and shared tags as the core model.

## Stato e codice
- Repository: `/home/daniele/codex-workspace/projects/MultiTimeTracker`
- Branch/commit verificati: `codex/v488-release-safe-ui-lockdown` / `6ddeebb` (`#847261`)
- File codice/config/test/script analizzati: 224 su 224
- Stack rilevato: Kotlin, Python, Shell, Gradle, Jetpack Compose, Android
- Validazione `#847261`: `compileDebugKotlin`, `testDebugUnitTest`, `assembleDebug`; Pixel 8a clone `com.example.multitimetracker.devicetest` v525 con 53 instrumentation test, 3 skipped, 0 failed.

## Orientamento rapido
- Entrypoint: `app/src/main/AndroidManifest.xml,app/src/main/java/com/example/multitimetracker/MainActivity.kt,benchmark/src/main/AndroidManifest.xml`
- Core/data: `app/src/main/java/com/example/multitimetracker/AppPatchVersion.kt,app/src/main/java/com/example/multitimetracker/SessionOnlyGuards.kt,app/src/main/java/com/example/multitimetracker/SingleSubmitGuard.kt,app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt,app/src/main/java/com/example/multitimetracker/MainViewModelSnapshotCoordinator.kt,app/src/main/java/com/example/multitimetracker/capsules/importexport/ImportExportCapsuleViewModel.kt`
- Test: `app/src/test/java/com/example/multitimetracker/capsules/CapsuleBoundaryOwnershipTest.kt,app/src/test/java/com/example/multitimetracker/capsules/alerts/AlertsCapsuleViewModelTest.kt,app/src/androidTest/java/com/example/multitimetracker/ExampleInstrumentedTest.kt,app/src/androidTest/java/com/example/multitimetracker/MainViewModelRecoveryTest.kt,app/src/androidTest/java/com/example/multitimetracker/SessionOnlyE2eTest.kt,app/src/androidTest/java/com/example/multitimetracker/TimedSessionNotificationFlowTest.kt,app/src/androidTest/java/com/example/multitimetracker/capsules/importexport/ImportExportCapsuleViewModelTest.kt`
- Script/build: `dev/tools/check_hardcoded_ui_strings.py,dev/tools/check_single_submit_confirm_buttons.sh,dev/tools/clean_transients.sh,preflight_check.ps1,app/build.gradle,app/build.gradle.kts,benchmark/build.gradle.kts,build.gradle.kts`

## Link
- AI doc: [AI doc](../../../ai/projects/multitimetracker.md)
- Metadata: [dev/project.metadata.json](../../../../projects/MultiTimeTracker/dev/project.metadata.json)
- Legacy docs: [dev/legacy](../../../../projects/MultiTimeTracker/dev/legacy)
- Repository: [repo path](../../../../projects/MultiTimeTracker)
