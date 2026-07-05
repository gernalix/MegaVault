# MultiTimeTracker Overview

MultiTimeTracker is a local-first Android time tracker. The main data lives in the app SQLite database, with sessions and shared tags as the core model.

## Stato e codice
- Repository: `/home/daniele/codex-workspace/projects/MultiTimeTracker`
- Branch/commit verificati: `codex/v488-release-safe-ui-lockdown` / `5b7e76a2de28d9974235d5f8fcc2623c64251fca` (`#294816`, v527 docs validation; APK/code v527 validato da `2548034f6c4fc7e4950f45600b41101faae7d764`)
- File codice/config/test/script analizzati: 224 su 224
- Stack rilevato: Kotlin, Python, Shell, Gradle, Jetpack Compose, Android
- Validazione `#462918`: `compileDebugKotlin`, `testDebugUnitTest`, `assembleDebug`; Pixel 8a clone `com.example.multitimetracker.devicetest` v525 con 53 instrumentation test, 3 skipped, 0 failed; clone install/launch ADB verificato con PID.
- Validazione `#817463/#294816`: `compileDebugKotlin`, `assembleDebug`, `assembleDeviceTest`, `check_hardcoded_ui_strings`, `testDebugUnitTest`, `lintDebug`, `assembleDebugAndroidTest` verdi; TCL debug v527 installato e test UI reale completato; Pixel debug v527 installato con smoke minimo.
- Performance `#817463/#294816`: onCreate real DB ridotto da ~79 ms a ~31 ms; schema ensure steady da ~51 ms a ~2.3 ms; su TCL sbloccato clone cold `am start -W` medio 669 ms e warm medio 10.2 ms.
- Capsulizzazione `#462918`: 100 percento strict stimato per ownership feature auditata; NOW, TAGS, TIMELINE, QUICK_EVENTS, CHAINS, ALERTS, IMPORT_EXPORT, AUDIT_LOG e SINCE_WHEN hanno owner capsule espliciti, MainViewModel resta shell/composition root.
- Integrita dati `#739284`: v528 blocca sparizioni silenziose di entita persistenti e valida ogni export/import SQLite con integrity, schema e conteggi critici prima della promozione.

## Orientamento rapido
- Entrypoint: `app/src/main/AndroidManifest.xml,app/src/main/java/com/example/multitimetracker/MainActivity.kt,benchmark/src/main/AndroidManifest.xml`
- Core/data: `app/src/main/java/com/example/multitimetracker/AppPatchVersion.kt,app/src/main/java/com/example/multitimetracker/SessionOnlyGuards.kt,app/src/main/java/com/example/multitimetracker/SingleSubmitGuard.kt,app/src/main/java/com/example/multitimetracker/FirstRunRestoreContract.kt,app/src/main/java/com/example/multitimetracker/MainViewModelSnapshotCoordinator.kt,app/src/main/java/com/example/multitimetracker/capsules/sessions/SessionOwnerCapsuleViewModel.kt,app/src/main/java/com/example/multitimetracker/capsules/auditlog/AuditLogCapsuleViewModel.kt,app/src/main/java/com/example/multitimetracker/capsules/sincewhen/SinceWhenCapsuleViewModel.kt,app/src/main/java/com/example/multitimetracker/capsules/importexport/ImportExportCapsuleViewModel.kt`
- Test: `app/src/test/java/com/example/multitimetracker/capsules/CapsuleBoundaryOwnershipTest.kt,app/src/test/java/com/example/multitimetracker/capsules/auditlog/AuditLogCapsuleViewModelTest.kt,app/src/test/java/com/example/multitimetracker/capsules/sincewhen/SinceWhenCapsuleViewModelTest.kt,app/src/test/java/com/example/multitimetracker/capsules/alerts/AlertsCapsuleViewModelTest.kt,app/src/androidTest/java/com/example/multitimetracker/ExampleInstrumentedTest.kt,app/src/androidTest/java/com/example/multitimetracker/MainViewModelRecoveryTest.kt,app/src/androidTest/java/com/example/multitimetracker/SessionOnlyE2eTest.kt,app/src/androidTest/java/com/example/multitimetracker/TimedSessionNotificationFlowTest.kt,app/src/androidTest/java/com/example/multitimetracker/capsules/importexport/ImportExportCapsuleViewModelTest.kt`
- Script/build: `dev/tools/check_hardcoded_ui_strings.py,dev/tools/check_single_submit_confirm_buttons.sh,dev/tools/clean_transients.sh,preflight_check.ps1,app/build.gradle,app/build.gradle.kts,benchmark/build.gradle.kts,build.gradle.kts`

## Link
- AI doc: [AI doc](../../../ai/projects/multitimetracker.md)
- Metadata: [dev/project.metadata.json](../../../../projects/MultiTimeTracker/dev/project.metadata.json)
- Legacy docs: [dev/legacy](../../../../projects/MultiTimeTracker/dev/legacy)
- Repository: [repo path](../../../../projects/MultiTimeTracker)

---

## Merged GitHub Branch Details 20260705

- Repository locale Windows: `C:/Users/seste/Documents/MTT`
- Branch/commit verificati: `master` / `44c2b33e53ce98e02f95437bd5bc7eb3f16aa688` (`#628914`)
- Validazione `#914506`: `compileDebugKotlin`, `testDebugUnitTest`, `assembleDebug`, `lintDebug`, `assembleRelease`, `bundleRelease` verdi; versione `489`; `applicationId=com.example.multitimetracker`; APK/AAB release generati ma unsigned per secret signing mancanti.
- Validazione `#517284`: upload keystore locale ignorato creato; `app-release.apk` e `app-release.aab` firmati e verificati con `apksigner`/`jarsigner`; install smoke saltato per proteggere device gia occupati da build debug v534.
- Validazione `#947263`: recupero branch corretto, `master` fast-forward a `MTT_VERSION=534`, `compileDebugKotlin`, `testDebugUnitTest`, `assembleDebug` PASS; APK debug `versionCode=534`, `versionName=534`, asset patch `534`; Pixel non usato.
- Validazione `#395842`: port Play Store su branch v534-derived `codex/v534-play-store-readiness-port`, `MTT_VERSION=535`; `compileDebugKotlin`, `testDebugUnitTest`, `assembleDebug`, `lintDebug`, `assembleRelease`, `bundleRelease`, `apksigner`, `jarsigner` PASS; APK/AAB firmati con upload key locale ignorata.
- Validazione `#628914`: `master` fast-forwardato a v535; backup `backup/master-before-v535-play-store-merge-20260622-133603`; `compileDebugKotlin`, `testDebugUnitTest`, `assembleDebug`, `lintDebug`, `assembleRelease`, `bundleRelease`, `apksigner`, `jarsigner` PASS.
- Play Store `#628914`: lavoro Play Store presente su `master` v535; readiness stimata 92 percento per closed testing offline, con residui owner-only Play Console/privacy URL/assets/tester list.

## Incident #947263
- Nome: `wrong_branch_play_store_work_v489_instead_of_v528`.
- Branch sbagliato: `codex/play-store-readiness-roadmap` / `a8a28e20a4be8fab0439ba28fb7f491b32747c9c` / `MTT_VERSION=489`.
- Linea corretta: `origin/codex/v488-release-safe-ui-lockdown` promossa a `master` / `00ecfd85a50ba30b927e759d4ed766040a25081c` / `MTT_VERSION=534`; v528 esiste come commit storico `8061d232e4afbf0e80e2cebbbf76233f7fa2fa18`.
- Backup pushati: `backup/master-before-v528-recovery-20260622-093346` e `backup/v489-play-store-work-20260622-093346`.
- Regola permanente: prima di lavoro release/Play Store verificare branch attuale, branch remoto piu recente, versionCode piu alto fra tutti i branch, coerenza MegaVault e roadmap attiva; se il branch corrente non contiene la versione piu alta nota, fermarsi e chiedere conferma.

## Port #395842
- Recuperato: Play Store docs, Data Safety, privacy policy, store listing, release notes, closed testing steps, Play Console copy-paste docs, asset checklist, CI workflow, release signing wiring, ignore rules.
- Escluso: codice app vecchio v489, vecchie capsule/MainActivity/MainViewModel, DB/SAF/import/export regressions, version 489, artifact, keystore e secrets.
- Commit app: `44c2b33e53ce98e02f95437bd5bc7eb3f16aa688`.
- Stato storico: pronto per review/merge manuale su `master`; chiuso da merge #628914.

## Merge #628914
- `master` ora contiene la linea v535 Play Store readiness.
- Commit master: `44c2b33e53ce98e02f95437bd5bc7eb3f16aa688`.
- Branch integrato: `codex/v534-play-store-readiness-port`.
- Branch da usare d'ora in poi: `master` v535 o superiore.

- Play handoff: presente su `master` v535; sorgente storica portata da `backup/v489-play-store-work-20260622-093346:dev/human/play_store` e `backup/v489-play-store-work-20260622-093346:dev/ai/play_store_readiness.md`
