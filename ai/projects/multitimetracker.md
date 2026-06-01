# MultiTimeTracker AI OPERATIONS

PROJECT
- name: MultiTimeTracker
- slug: multitimetracker
- purpose: MultiTimeTracker is a local-first Android time tracker. The main data lives in the app SQLite database, with sessions and shared tags as the core model.
- current_status: Working tree has 9 non-clean entries; do not mix unrelated changes. First entries: ?? .codexmeta, ?? .codexmeta.bak.20260528_191731, ?? .codexmeta.bak.20260528_191758, ?? .codexmeta.bak.20260528_191912, ?? .codexmeta.bak.20260528_193715
- repo_path: `/home/daniele/codex-workspace/projects/MultiTimeTracker`
- remote: `https://github.com/gernalix/MultiTimeTracker.git`
- branch: `codex/v488-release-safe-ui-lockdown`
- last_verified_commit/date: `80f88c0` / `2026-06-01T13:20:29+02:00`

STACK
- languages: Kotlin, Python, Shell
- frameworks: Gradle, Jetpack Compose
- DB: SQLite
- platform: Android
- external_tools/services: ADB/Android device

CODE_MAP
entrypoints:
- `app/src/main/AndroidManifest.xml`
- `app/src/main/java/com/example/multitimetracker/MainActivity.kt`
- `dev/tools/check_hardcoded_ui_strings.py`
- `tools/mtt_helper.py`
important_folders:
- `app`
- `benchmark`
- `dev`
- `forensic`
- `gradle`
- `tools`
important_files:
- `build.gradle.kts`
- `settings.gradle.kts`
- `gradle.properties`
- `dev/README.md`
- `dev/archive/transient/codex log.txt`
- `dev/archive/transient/last_fix_attempts.txt`
tests:
- `app/src/androidTest/java/com/example/multitimetracker/ExampleInstrumentedTest.kt`
- `app/src/androidTest/java/com/example/multitimetracker/MainViewModelRecoveryTest.kt`
- `app/src/androidTest/java/com/example/multitimetracker/SessionOnlyE2eTest.kt`
- `app/src/androidTest/java/com/example/multitimetracker/TimedSessionNotificationFlowTest.kt`
- `app/src/androidTest/java/com/example/multitimetracker/capsules/importexport/ImportExportCapsuleViewModelTest.kt`
- `app/src/androidTest/java/com/example/multitimetracker/export/AuthoritativeExportPayloadBuilderTest.kt`
- `app/src/androidTest/java/com/example/multitimetracker/persistence/AuthoritativeSessionRuntimeTest.kt`
- `app/src/androidTest/java/com/example/multitimetracker/persistence/PersistenceImportExportTest.kt`
- `app/src/androidTest/java/com/example/multitimetracker/persistence/PersistenceImportExportTestSupport.kt`
- `app/src/androidTest/java/com/example/multitimetracker/persistence/QuickEventRepositoryTest.kt`
- `app/src/test/java/com/example/multitimetracker/EffectiveTimeContextTest.kt`
- `app/src/test/java/com/example/multitimetracker/FirstRunRestoreContractTest.kt`
- `app/src/test/java/com/example/multitimetracker/MainViewModelStartAlertRegressionTest.kt`
- `app/src/test/java/com/example/multitimetracker/SessionOnlyGuardsTest.kt`
- `app/src/test/java/com/example/multitimetracker/SingleSubmitGuardTest.kt`
- `app/src/test/java/com/example/multitimetracker/TagRenamePropagationTest.kt`
- `app/src/test/java/com/example/multitimetracker/TimeFenceTimerReceiverTest.kt`
- `app/src/test/java/com/example/multitimetracker/capsules/alerts/AlertsCapsuleViewModelTest.kt`
- `app/src/test/java/com/example/multitimetracker/capsules/alerts/TimeFenceAlarmReconciliationTest.kt`
- `app/src/test/java/com/example/multitimetracker/export/SessionOnlyRuntimeTasksTest.kt`
- `app/src/test/java/com/example/multitimetracker/model/QuickEventFiltersTest.kt`
- `app/src/test/java/com/example/multitimetracker/model/TimeEngineTagCrudTest.kt`
- `app/src/test/java/com/example/multitimetracker/persistence/AuthoritativeSessionCacheBuilderTest.kt`
- `app/src/test/java/com/example/multitimetracker/persistence/AuthoritativeSessionCoreSmokeTest.kt`
- `app/src/test/java/com/example/multitimetracker/persistence/BackupFolderPolicyTest.kt`
- `app/src/test/java/com/example/multitimetracker/persistence/SnapshotHistoryCodecTest.kt`
- `app/src/test/java/com/example/multitimetracker/ui/alerts/AlertMessageParserTest.kt`
- `app/src/test/java/com/example/multitimetracker/ui/screens/AuditLogScreenTest.kt`
- `app/src/test/java/com/example/multitimetracker/ui/screens/LifePeriodsScreenTest.kt`
- `app/src/test/java/com/example/multitimetracker/ui/screens/NewSessionDraftTest.kt`
scripts:
- `dev/tools/check_hardcoded_ui_strings.py`
- `dev/tools/check_single_submit_confirm_buttons.sh`
- `dev/tools/clean_transients.sh`
- `gradlew`
- `preflight_check.ps1`
- `tools/mtt_helper.py`
generated/runtime/avoid_touch_casually:
- `dev/legacy`
- `build`
- `.gradle`
- `forensic`
- `*.db/*.sqlite user/runtime data`

ARCH
summary:
- dev/archive/transient/codex log.txt: Leggi solo questi file, in quest’ordine, e non fare repo tour:
- dev/archive/transient/last_fix_attempts.txt: - Fix: replace gradle.buildFinished(...) with gradle.addBuildListener(BuildAdapter.buildFinished) to avoid Kotlin DSL/Closure mismatch on Gradle 9.x.
- dev/legacy/dev/human/PROJECT_OVERVIEW.md: MultiTimeTracker is a local-first Android time tracker. The main data lives in the app SQLite database, with sessions and shared tags as the core model.
- dev/legacy/dev/CAPSULE_INDEX.md: Capsule ownership notes moved to `dev/ai/CAPSULES.md`.
- dev/legacy/dev/ai/CAPSULE_INDEX.md: / NOW / capsules/now, NowScreen.kt /
- dev/legacy/dev/ai/INDEX.md: STYLE=neocodecs; terse; tables; no_long_prose
- dev/legacy/dev/archive/INDEX.md: `dev/archive/*` is historical evidence only.
- dev/legacy/dev/human/INDEX.md: They explain status and decisions in readable form.
- dev/legacy/dev/ARCHITECTURE_LOCK.md: Architecture and Time Machine storage locks moved to `dev/ai/ARCHITECTURE_LOCK.md`.
- dev/legacy/dev/ai/ARCHITECTURE_LOCK.md: STATUS: CANONICAL AGENT REFERENCE
components/dataflow/design_decisions:
| source | fact |
|---|---|
| `dev/archive/transient/codex log.txt` | OBIETTIVO |
| `dev/archive/transient/codex log.txt` | TAGS |
| `dev/archive/transient/codex log.txt` | CHRONOLOGY |
| `dev/archive/transient/codex log.txt` | SINCE WHEN |
| `dev/archive/transient/codex log.txt` | ALERT |
| `dev/archive/transient/codex log.txt` | CHAINS |
| `dev/archive/transient/codex log.txt` | AUDIT LOG |
| `dev/archive/transient/codex log.txt` | SETTINGS |
| `dev/archive/transient/codex log.txt` | REGOLE FUNZIONALI |
| `dev/archive/transient/codex log.txt` | BANNER GLOBALE |
| `dev/archive/transient/codex log.txt` | ARCHITETTURA OBBLIGATORIA |
| `dev/archive/transient/codex log.txt` | SEPARAZIONE CRITICA DEL TEMPO |
| `dev/archive/transient/codex log.txt` | WRITE GATE CENTRALE |
| `dev/archive/transient/codex log.txt` | FEATURE CAPSULE |
| `dev/archive/transient/codex log.txt` | RICOSTRUZIONE STORICA REALE |
| `dev/archive/transient/codex log.txt` | EVENT HISTORY STRUTTURATA |
| `dev/archive/transient/codex log.txt` | QUERY TEMPORALI |
| `dev/archive/transient/codex log.txt` | SCANSIONE OBBLIGATORIA ANTI-BUG SUL TEMPO |

INVARIANTS
architecture/data/UX/safety/versioning/localization:
| source | fact |
|---|---|
| `dev/archive/transient/codex log.txt` | Leggi solo questi file, in quest’ordine, e non fare repo tour: |
| `dev/archive/transient/codex log.txt` | - evita refactor larghi non necessari |
| `dev/archive/transient/codex log.txt` | - read-only |
| `dev/archive/transient/codex log.txt` | La Time Machine deve essere reale, non cosmetica. |
| `dev/archive/transient/codex log.txt` | 3) Da quel momento tutta l’app entra in read-only. |
| `dev/archive/transient/codex log.txt` | 5) Qualsiasi write action deve essere vietata finché non si esce dalla Time Machine. |
| `dev/archive/transient/codex log.txt` | - durata mostrata = 2 giorni, non 14 |
| `dev/archive/transient/codex log.txt` | - non sovrapposto al contenuto utile |
| `dev/archive/transient/codex log.txt` | - non flottante sopra elementi cliccabili importanti |
| `dev/archive/transient/codex log.txt` | - sta nel root layout dell’app, non replicato nelle singole schermate |
| `dev/archive/transient/codex log.txt` | Non implementare patch UI tab-per-tab. |
| `dev/archive/transient/codex log.txt` | Non usare il clock reale nei punti che influenzano la UI storica. |
| `dev/archive/transient/codex log.txt` | - DATABASE TIME |
| `dev/archive/transient/codex log.txt` | effectiveNowMs NON deve MAI essere usato per: |
| `dev/archive/transient/codex log.txt` | - scrivere nel database |
| `dev/archive/transient/codex log.txt` | Tutti i timestamp scritti nel database devono sempre usare il tempo reale del dispositivo. |
| `dev/archive/transient/codex log.txt` | La Time Machine è una lente di lettura storica, non una simulazione temporale dell’app. |
| `dev/archive/transient/codex log.txt` | Il blocco delle scritture deve stare nel ViewModel / action layer, non solo nei bottoni UI. |
| `dev/archive/transient/codex log.txt` | - espone effectiveNowMs / read-only flags / banner state |
| `dev/archive/transient/codex log.txt` | - non contiene hack UI |
| `dev/archive/transient/codex log.txt` | Non distribuire logica temporale nelle schermate. |
| `dev/archive/transient/codex log.txt` | Non fare scorciatoie cross-layer. |
| `dev/archive/transient/codex log.txt` | - Time Machine non muta stato persistito |
| `dev/archive/transient/codex log.txt` | - Time Machine non scrive nel DB |
| `dev/archive/transient/codex log.txt` | - Time Machine non altera import/export |
| `dev/archive/transient/codex log.txt` | - Time Machine non rompe il flusso live quando disattivata |

BUILD_TEST
build_files:
- `build.gradle.kts`
- `settings.gradle.kts`
- `gradle.properties`
commands_found:
| source | fact |
|---|---|
| `dev/archive/transient/codex log.txt` | - gradle.properties |
| `dev/archive/transient/codex log.txt` | Usa gradle.properties come sorgente unica del versioning ufficiale. |
| `dev/archive/transient/codex log.txt` | - gradle.properties resta la fonte ufficiale |
| `dev/archive/transient/codex log.txt` | Se adb non è nel PATH della sessione, usa quello di Android Studio con path esplicito. |
| `dev/archive/transient/codex log.txt` | - regola adb Android Studio per clone app Pixel |
| `dev/archive/transient/codex log.txt` | Clone com.example.multitimetracker.devicetest installato e avviabile sul Pixel via adb. |
| `dev/archive/transient/codex log.txt` | La parte codice è allineata; adesso faccio davvero lo smoke manuale sul clone Pixel usando adb, dump UI e screenshot per entrare in Time Machine e verificare i punti minimi richiesti senza inventare risultati. |
| `dev/archive/transient/last_fix_attempts.txt` | - Fix: replace gradle.buildFinished(...) with gradle.addBuildListener(BuildAdapter.buildFinished) to avoid Kotlin DSL/Closure mismatch on Gradle 9.x. |
| `dev/legacy/dev/ai/OPERATING_RULES.md` | / MTT_VERSION / gradle.properties / |
| `dev/legacy/dev/ai/OPERATING_RULES.md` | Allowed routine bump: gradle.properties + patch-version.txt. |
| `dev/legacy/dev/ai/OPERATING_RULES.md` | / gradle.properties / |
| `dev/legacy/dev/ai/OPERATING_RULES.md` | / gradle/libs.versions.toml / |
| `dev/legacy/dev/ai/OPERATING_RULES.md` | If no device listed by adb: mark PENDING_DEVICE_UNAVAILABLE. |
| `dev/legacy/dev/ai/RELEASE_PROTOCOL.md` | / unit / ./gradlew --console=plain --stacktrace --max-workers=1 :app:testDebugUnitTest / |
| `dev/legacy/dev/ai/RELEASE_PROTOCOL.md` | / debug_apk / ./gradlew --console=plain --stacktrace --max-workers=1 :app:assembleDebug / |
| `dev/legacy/dev/ai/RELEASE_PROTOCOL.md` | / strings / python3 dev/tools/check_hardcoded_ui_strings.py / |
| `dev/legacy/dev/ai/TEST_GATES.md` | / 525 / ./gradlew --console=plain --stacktrace --max-workers=1 :app:compileDebugKotlin / PASS; 3m13s / |
| `dev/legacy/dev/ai/TEST_GATES.md` | / 525 / python3 dev/tools/check_hardcoded_ui_strings.py / PASS / |
| `dev/legacy/dev/ai/TEST_GATES.md` | / 525 / ./gradlew --console=plain --stacktrace --max-workers=1 :app:testDebugUnitTest / PASS; 1m57s / |
| `dev/legacy/dev/ai/TEST_GATES.md` | / 525 / ./gradlew --console=plain --stacktrace --max-workers=1 :app:assembleDebug / PASS; app/build/outputs/apk/debug/app-debug.apk / |
| `dev/legacy/dev/ai/TEST_GATES.md` | / 525 / ./gradlew --console=plain --stacktrace --max-workers=1 :app:assembleDeviceTest :app:assembleDebugAndroidTest / PASS; 5m16s / |
| `dev/legacy/dev/ai/TEST_GATES.md` | / 525 / ./gradlew --console=plain --stacktrace --max-workers=1 :app:lintDebug / PASS; 4m05s / |
| `dev/legacy/dev/ai/TEST_GATES.md` | / 525 / adb Pixel / PENDING_DEVICE_UNAVAILABLE; adb devices empty; mDNS 192.168.1.37:38795 announced but adb connect refused / |
| `dev/legacy/dev/ai/TEST_GATES.md` | / 524b / ./gradlew --console=plain --stacktrace --max-workers=1 :app:testDebugUnitTest :app:assembleDebug / PASS; prompt #492638 final code / |
test_targets:
- `app/src/androidTest/java/com/example/multitimetracker/ExampleInstrumentedTest.kt`
- `app/src/androidTest/java/com/example/multitimetracker/MainViewModelRecoveryTest.kt`
- `app/src/androidTest/java/com/example/multitimetracker/SessionOnlyE2eTest.kt`
- `app/src/androidTest/java/com/example/multitimetracker/TimedSessionNotificationFlowTest.kt`
- `app/src/androidTest/java/com/example/multitimetracker/capsules/importexport/ImportExportCapsuleViewModelTest.kt`
- `app/src/androidTest/java/com/example/multitimetracker/export/AuthoritativeExportPayloadBuilderTest.kt`
- `app/src/androidTest/java/com/example/multitimetracker/persistence/AuthoritativeSessionRuntimeTest.kt`
- `app/src/androidTest/java/com/example/multitimetracker/persistence/PersistenceImportExportTest.kt`
- `app/src/androidTest/java/com/example/multitimetracker/persistence/PersistenceImportExportTestSupport.kt`
- `app/src/androidTest/java/com/example/multitimetracker/persistence/QuickEventRepositoryTest.kt`
- `app/src/test/java/com/example/multitimetracker/EffectiveTimeContextTest.kt`
- `app/src/test/java/com/example/multitimetracker/FirstRunRestoreContractTest.kt`
- `app/src/test/java/com/example/multitimetracker/MainViewModelStartAlertRegressionTest.kt`
- `app/src/test/java/com/example/multitimetracker/SessionOnlyGuardsTest.kt`
- `app/src/test/java/com/example/multitimetracker/SingleSubmitGuardTest.kt`
- `app/src/test/java/com/example/multitimetracker/TagRenamePropagationTest.kt`
- `app/src/test/java/com/example/multitimetracker/TimeFenceTimerReceiverTest.kt`
- `app/src/test/java/com/example/multitimetracker/capsules/alerts/AlertsCapsuleViewModelTest.kt`
- `app/src/test/java/com/example/multitimetracker/capsules/alerts/TimeFenceAlarmReconciliationTest.kt`
- `app/src/test/java/com/example/multitimetracker/export/SessionOnlyRuntimeTasksTest.kt`
- `app/src/test/java/com/example/multitimetracker/model/QuickEventFiltersTest.kt`
- `app/src/test/java/com/example/multitimetracker/model/TimeEngineTagCrudTest.kt`
- `app/src/test/java/com/example/multitimetracker/persistence/AuthoritativeSessionCacheBuilderTest.kt`
- `app/src/test/java/com/example/multitimetracker/persistence/AuthoritativeSessionCoreSmokeTest.kt`
- `app/src/test/java/com/example/multitimetracker/persistence/BackupFolderPolicyTest.kt`
known_test_flakiness_or_requirements:
- dev/legacy/dev/ai/TEST_GATES.md: / 524b / connectedDeviceTestAndroidTest clone / BLOCKED_BY_ANDROID_UTP; runner NoClassDefFoundError com.google.common.util.concurrent.AbstractFuture$Failure$1; no main-package reset used /
- dev/legacy/en/Troubleshooting/Troubleshooting.md: A gap is not automatically a failure. Use [[en/Interface/Chronology/Chronology]] to decide whether the gap should stay as untracked life or be reconstructed from memory. Focus on restoring coherence, not fictio
- dev/legacy/dev/ai/ROADMAP_ACTIVE.md: / connected_clone / BLOCKED_BY_ANDROID_UTP; deviceTest runner crashed with NoClassDefFoundError in com.google.common.util.concurrent.AbstractFuture$Failure$1 after local code fix /
- dev/legacy/dev/human/CHANGELOG.md: - Fixed the v516 Pixel clone failure set without starting PATCH 8.
- dev/legacy/.codex_patch_current_v474/dev/ROADMAP_ACTIVE.md: - Fixed the startup crash introduced in the suspicious v472 timeframe by hardening snapshot bootstrap against legacy session rows still serialized with `taskId` and `taskName` aliases inside `closedSe
- dev/legacy/.codex_patch_current_v474/dev/ROADMAP_ACTIVE.md: - Preserved the conservative cross-tab UI cleanup from v472, with only a compatibility-layer patch in persistence plus a targeted regression test and bootstrap-focused documentation updates.
- dev/legacy/.codex_patch_current_v474/dev/ROADMAP_ACTIVE.md: - Dev impact: alert matching is now consistent between runtime and receiver paths, with small unit tests guarding the regression.
- dev/legacy/.codex_patch_current_v474/dev/ROADMAP_HISTORY.md: - Tight regression patch: real-time timed-session expiry reconciliation, Since When stale render cleanup plus compact `d/h/m` duration labels, and alarm-mode full-screen permission check/guidance.
- dev/legacy/.codex_patch_snapshot_v474/dev/ROADMAP_ACTIVE.md: - Fixed the startup crash introduced in the suspicious v472 timeframe by hardening snapshot bootstrap against legacy session rows still serialized with `taskId` and `taskName` aliases inside `closedS
- dev/legacy/.codex_patch_snapshot_v474/dev/ROADMAP_ACTIVE.md: - Preserved the conservative cross-tab UI cleanup from v472, with only a compatibility-layer patch in persistence plus a targeted regression test and bootstrap-focused documentation updates.

VERSIONING_RELEASE
rules/artifacts/commit_push/release_blockers:
| source | fact |
|---|---|
| `dev/archive/transient/codex log.txt` | - eventuale history/versioning o eventi strutturati replayabili se semplici timestamp non bastano |
| `dev/archive/transient/codex log.txt` | Se un’entità può cambiare contenuto nel tempo (es. nome tag, colore, configurazione alert, ecc.), non basta sapere che esisteva: serve poter ricostruire quale stato/valore avesse a T. |
| `dev/archive/transient/codex log.txt` | - history/version table minima |
| `dev/archive/transient/codex log.txt` | Ma non limitarti a spostare il versioning lì: |
| `dev/archive/transient/codex log.txt` | - NON incrementare la versione durante i normali build/test intermedi della patch |
| `dev/archive/transient/codex log.txt` | - incrementa la versione solo nel packaging/release finale della patch |
| `dev/archive/transient/codex log.txt` | - eventuale patch version runtime-only mostrata nell'app |
| `dev/legacy/dev/human/PROJECT_OVERVIEW.md` | MultiTimeTracker is a local-first Android time tracker. The main data lives in the app SQLite database, with sessions and shared tags as the core model. |
| `dev/legacy/dev/human/PROJECT_OVERVIEW.md` | Current focus: keep real data safe, make Events fast enough for one-tap logging, and keep backup/restore understandable. |
| `dev/legacy/dev/ai/INDEX.md` | / 4 / dev/ai/ARCHITECTURE_LOCK.md / behavior/data/runtime/UX/release / |
| `dev/legacy/dev/ai/INDEX.md` | / 8 / dev/ai/RELEASE_PROTOCOL.md / release/build / |
| `dev/legacy/dev/ai/ARCHITECTURE_LOCK.md` | - Authoritative tracked-history truth: `sessions` + `session_tags`. |
| `dev/archive/transient/codex log.txt` | Usa gradle.properties come sorgente unica del versioning ufficiale. |
| `dev/legacy/dev/ai/OPERATING_RULES.md` | / MTT_VERSION / gradle.properties / |
| `dev/legacy/dev/ai/OPERATING_RULES.md` | Allowed routine bump: gradle.properties + patch-version.txt. |
| `dev/legacy/dev/ai/OPERATING_RULES.md` | / gradle/libs.versions.toml / |
| `dev/legacy/dev/ai/RELEASE_PROTOCOL.md` | / unit / ./gradlew --console=plain --stacktrace --max-workers=1 :app:testDebugUnitTest / |
| `dev/legacy/dev/ai/RELEASE_PROTOCOL.md` | / debug_apk / ./gradlew --console=plain --stacktrace --max-workers=1 :app:assembleDebug / |
| `dev/legacy/dev/ai/RELEASE_PROTOCOL.md` | / strings / python3 dev/tools/check_hardcoded_ui_strings.py / |
| `dev/legacy/dev/ai/TEST_GATES.md` | / 525 / ./gradlew --console=plain --stacktrace --max-workers=1 :app:assembleDebug / PASS; app/build/outputs/apk/debug/app-debug.apk / |

DATA_STORAGE
DB_paths/backup/import/export/migration/retention/user_data_safety:
| source | fact |
|---|---|
| `dev/archive/transient/codex log.txt` | Leggi solo questi file, in quest’ordine, e non fare repo tour: |
| `dev/archive/transient/codex log.txt` | - evita refactor larghi non necessari |
| `dev/archive/transient/codex log.txt` | - read-only |
| `dev/archive/transient/codex log.txt` | La Time Machine deve essere reale, non cosmetica. |
| `dev/archive/transient/codex log.txt` | 3) Da quel momento tutta l’app entra in read-only. |
| `dev/archive/transient/codex log.txt` | 5) Qualsiasi write action deve essere vietata finché non si esce dalla Time Machine. |
| `dev/archive/transient/codex log.txt` | - durata mostrata = 2 giorni, non 14 |
| `dev/archive/transient/codex log.txt` | - non sovrapposto al contenuto utile |
| `dev/archive/transient/codex log.txt` | - non flottante sopra elementi cliccabili importanti |
| `dev/archive/transient/codex log.txt` | - sta nel root layout dell’app, non replicato nelle singole schermate |
| `dev/archive/transient/codex log.txt` | Non implementare patch UI tab-per-tab. |
| `dev/archive/transient/codex log.txt` | Non usare il clock reale nei punti che influenzano la UI storica. |
| `dev/archive/transient/codex log.txt` | - DATABASE TIME |
| `dev/archive/transient/codex log.txt` | effectiveNowMs NON deve MAI essere usato per: |
| `dev/archive/transient/codex log.txt` | - scrivere nel database |
| `dev/archive/transient/codex log.txt` | Tutti i timestamp scritti nel database devono sempre usare il tempo reale del dispositivo. |
| `dev/archive/transient/codex log.txt` | La Time Machine è una lente di lettura storica, non una simulazione temporale dell’app. |
| `dev/archive/transient/codex log.txt` | Il blocco delle scritture deve stare nel ViewModel / action layer, non solo nei bottoni UI. |
| `dev/archive/transient/codex log.txt` | - espone effectiveNowMs / read-only flags / banner state |
| `dev/archive/transient/codex log.txt` | - non contiene hack UI |
| `dev/archive/transient/codex log.txt` | Non distribuire logica temporale nelle schermate. |
| `dev/archive/transient/codex log.txt` | Non fare scorciatoie cross-layer. |

KNOWN_BUGS
active/historical/root_causes/regression_checklist:
| source | fact |
|---|---|
| `dev/archive/transient/codex log.txt` | SCANSIONE OBBLIGATORIA ANTI-BUG SUL TEMPO |
| `dev/archive/transient/codex log.txt` | - bug registry se scopri/correggi bug |
| `dev/archive/transient/last_fix_attempts.txt` | - Expectation: build scripts compile; on build FAIL after configuration, logs should be created in dev/build_fail_history/. |
| `dev/legacy/dev/ai/ARCHITECTURE_LOCK.md` | Flows that overwrite or swap the internal DB must create a meaningful local backup, stage and validate the candidate DB, apply it, run the critical integrity gate, verify runtime activation, and rollback automatically on |
| `dev/legacy/en/Workflows/Common Tracking Workflows.md` | Minimal use works best when paired with a small, stable tag set. It is better to track five important blocks clearly than to fail trying to capture everything. |
| `dev/legacy/dev/ai/TEST_GATES.md` | / 524b / connectedDeviceTestAndroidTest clone / BLOCKED_BY_ANDROID_UTP; runner NoClassDefFoundError com.google.common.util.concurrent.AbstractFuture$Failure$1; no main-package reset used / |
| `dev/legacy/dev/BUG_REGISTRY.md` | Current blocker/high/medium/low risk state moved to `dev/ai/RISK_REGISTER.md`. |
| `dev/legacy/dev/ai/RISK_REGISTER.md` | ## BLOCKER |
| `dev/legacy/dev/ai/RISK_REGISTER.md` | / 516 / receiver flag lint blocker fixed / |
| `dev/legacy/dev/human/TROUBLESHOOTING.md` | If counts are present but UI looks empty, treat it as a UI/filter issue before attempting restore. |
| `dev/legacy/en/Troubleshooting/Troubleshooting.md` | A gap is not automatically a failure. Use [[en/Interface/Chronology/Chronology]] to decide whether the gap should stay as untracked life or be reconstructed from memory. Focus on restoring coherence, not fictio |
| `dev/legacy/dev/ai/ROADMAP_ACTIVE.md` | / connected_clone / BLOCKED_BY_ANDROID_UTP; deviceTest runner crashed with NoClassDefFoundError in com.google.common.util.concurrent.AbstractFuture$Failure$1 after local code fix / |
| `dev/legacy/dev/human/ROADMAP_EXPLAINED.md` | - Closed the v515 static lint blocker for app-open snapshot-change receiver registration. |
| `dev/legacy/dev/human/CHANGELOG.md` | - Fixed the v516 Pixel clone failure set without starting PATCH 8. |
| `dev/legacy/dev/human/CHANGELOG.md` | - Fixed the remaining v515 lint blocker by registering the app-open snapshot-change receiver as not exported through AndroidX `ContextCompat`. |
| `dev/legacy/dev/human/CHANGELOG.md` | - `v513`: fixed startup/reopen regression by avoiding repeated Time Machine VACUUM, moving background persistence/vault export I/O off the main thread, and keeping drawer state process-local. |
| `dev/legacy/en/Features/Timed Sessions and Alerts.md` | Timed sessions are best when the duration belongs naturally to the tag itself. Examples include focused intervals, standard breaks, review blocks, or routines with a known length. A timed tag can also choose |
| `dev/legacy/.codex_patch_current_v474/dev/ROADMAP_ACTIVE.md` | - Fixed the startup crash introduced in the suspicious v472 timeframe by hardening snapshot bootstrap against legacy session rows still serialized with `taskId` and `taskName` aliases inside `closedSe |
| `dev/legacy/.codex_patch_current_v474/dev/ROADMAP_ACTIVE.md` | - Preserved the conservative cross-tab UI cleanup from v472, with only a compatibility-layer patch in persistence plus a targeted regression test and bootstrap-focused documentation updates. |
| `dev/legacy/.codex_patch_current_v474/dev/ROADMAP_ACTIVE.md` | - Final removal of all task-layer remnants from the active session runtime: closed-session contracts, snapshot runtime markers, chain state, quick widget path, and fail-fast text are now session-nativ |
| `dev/legacy/.codex_patch_current_v474/dev/ROADMAP_ACTIVE.md` | - Added fail-fast guardrails on leftover legacy task entry points and fallback bootstrap/export paths, plus JVM coverage for the new session-only guards and timer payload parsing. |
| `dev/legacy/.codex_patch_current_v474/dev/ROADMAP_ACTIVE.md` | - Registered the open `ALERT_START_TIMER_OFFSET` bug so the known delayed START-timer drift stays visible while the alert stack evolves. |
| `dev/legacy/.codex_patch_current_v474/dev/ROADMAP_ACTIVE.md` | - Fixed the remaining START-only alert regression for sessions created blank and completed via the NOW editor, so the first real title/tag save now emits `ON_START` once. |
| `dev/legacy/.codex_patch_current_v474/dev/ROADMAP_ACTIVE.md` | - Added a small pure runtime eligibility seam for alert matching and expanded JVM regression coverage across immediate START/END, delayed START scheduling/fire guards, cooldown, one-time disable, inva |

DO_NOT_BREAK
- Preserve `dev/project.metadata.json` -> this AI doc -> Human docs workflow.
- Preserve `dev/legacy/`; do not delete or rewrite historical docs without explicit migration intent.
- dev/archive/transient/codex log.txt: - DATABASE TIME
- dev/archive/transient/codex log.txt: - scrivere nel database
- dev/archive/transient/codex log.txt: Tutti i timestamp scritti nel database devono sempre usare il tempo reale del dispositivo.
- dev/archive/transient/codex log.txt: - eventuale history/versioning o eventi strutturati replayabili se semplici timestamp non bastano
- dev/archive/transient/codex log.txt: - history/version table minima
- dev/archive/transient/codex log.txt: Migrazioni DB devono essere backward-safe.
- dev/archive/transient/codex log.txt: Ma non limitarti a spostare il versioning lì:
- dev/archive/transient/codex log.txt: - NON incrementare la versione durante i normali build/test intermedi della patch
- dev/archive/transient/codex log.txt: - incrementa la versione solo nel packaging/release finale della patch
- dev/archive/transient/codex log.txt: - eventuale patch version runtime-only mostrata nell'app
- dev/archive/transient/codex log.txt: connectedAndroidTest sul clone parte ma fallisce 1 test esistente non-Time-Machine: SQLiteDatabaseLockedException in SessionOnlyE2eTest.
- dev/archive/transient/last_fix_attempts.txt: - Fix: replace gradle.buildFinished(...) with gradle.addBuildListener(BuildAdapter.buildFinished) to avoid Kotlin DSL/Closure mismatch on Gradle 9.x.
- dev/legacy/dev/human/PROJECT_OVERVIEW.md: MultiTimeTracker is a local-first Android time tracker. The main data lives in the app SQLite database, with sessions and shared tags as the core model.
- dev/legacy/dev/human/PROJECT_OVERVIEW.md: Current focus: keep real data safe, make Events fast enough for one-tap logging, and keep backup/restore understandable.
- dev/legacy/dev/CAPSULE_INDEX.md: Do not use this file as source of truth.
- dev/legacy/dev/ai/INDEX.md: / patch_524 / DONE; REAL_DB_IMPORT_MACRO_ID; prompt #917426; real backup import PASS /

RECENT_DECISIONS
| source | fact |
|---|---|
| `dev/legacy/dev/ai/RELEASE_PROTOCOL.md` | # RELEASE_PROTOCOL |
| `dev/legacy/dev/ai/RELEASE_PROTOCOL.md` | ## LOCAL_GATES |
| `dev/legacy/dev/ai/RELEASE_PROTOCOL.md` | ## DEVICE_GATES |
| `dev/legacy/dev/ROADMAP_HISTORY.md` | # MOVED: HUMAN CHANGELOG |
| `dev/legacy/dev/ai/ROADMAP_HISTORY.md` | # ROADMAP_HISTORY |
| `dev/legacy/dev/ai/ROADMAP_HISTORY.md` | ## RECENT_PATCHES |
| `dev/legacy/dev/human/CHANGELOG.md` | # Changelog |
| `dev/legacy/dev/human/CHANGELOG.md` | ## v525 |
| `dev/legacy/dev/human/CHANGELOG.md` | - Improved SQLite/runtime performance with query-aligned indexes for sessions, audit events, and Events tables. |
| `dev/legacy/dev/human/CHANGELOG.md` | - Events now refreshes screen data progressively while full exports still read the complete Events state from SQLite. |
| `dev/legacy/dev/human/CHANGELOG.md` | - Made the Events tab denser by removing the redundant intro block, tightening action buttons, and collapsing recent entries by default. |
| `dev/legacy/dev/human/CHANGELOG.md` | - Extended the app report with app version, DB version, active DB path, DB size, core table counts, and backup/import context. |
| `dev/legacy/dev/human/CHANGELOG.md` | - Hardened the backup policy so vault switching/export paths no longer create retained timestamped SQLite autoexports. |
| `dev/legacy/dev/human/CHANGELOG.md` | - Completed the `dev/ai/*` and `dev/human/*` dual-doc structure requested by prompt #581943. |
| `dev/legacy/dev/human/CHANGELOG.md` | - Bumped patch version from `524` to `525`. |
| `dev/legacy/dev/human/CHANGELOG.md` | ## v523 |
| `dev/legacy/dev/human/CHANGELOG.md` | - Renamed the quick-events experience to `Events` / `Eventi`. |
| `dev/legacy/dev/human/CHANGELOG.md` | - Added quick actions with timestamp-only entries, custom fields, and macros that can record multiple actions with the same timestamp. |

ROADMAP
active/deferred/risky:
| source | fact |
|---|---|
| `dev/archive/transient/codex log.txt` | - roadmap attiva/storica |
| `dev/legacy/dev/human/INDEX.md` | - `ROADMAP.md`: readable active/later roadmap. |
| `dev/legacy/dev/human/INDEX.md` | - `PLAYSTORE_READINESS_REPORT.md`: Play Store readiness status and pending checks. |
| `dev/legacy/dev/human/INDEX.md` | - `ROADMAP_EXPLAINED.md`: readable roadmap state. |
| `dev/legacy/dev/ai/ARCHITECTURE_LOCK.md` | Future device tests must use only the clone package and must preserve the main app. |
| `dev/legacy/dev/ai/OPERATING_RULES.md` | ## PRIORITY |
| `dev/legacy/dev/ai/BUG_REGISTRY.md` | / TCL_DEVICE / PENDING / no TCL validation device currently confirmed / |
| `dev/legacy/dev/ai/RISK_REGISTER.md` | / startup_reopen_ANR / WATCH / v521 recovery/startup clone tests PASS; release/main smoke pending / |
| `dev/legacy/dev/ai/RISK_REGISTER.md` | / exact_alarm_OEM_behavior / WATCH / v518 copy scoped; device/OEM still pending / |
| `dev/legacy/dev/ai/RISK_REGISTER.md` | / fullscreen_policy / WATCH / v518 runtime copy scoped; store/artifact/device still pending / |
| `dev/legacy/dev/ai/RISK_REGISTER.md` | / screenshot_listing_cleanliness / pending visual pass / |
| `dev/legacy/dev/ai/RISK_REGISTER.md` | / accessibility_static_sanity / pending UI pass / |
| `dev/legacy/en/Troubleshooting/Troubleshooting.md` | If it is a concrete stretch of activity, it is a session. If it is a broader phase that answers “since when,” it probably belongs in [[en/Features/Life Periods/Life Periods]]. |
| `dev/legacy/dev/ROADMAP_ACTIVE.md` | # MOVED: ROADMAP ACTIVE |
| `dev/legacy/dev/ROADMAP_ACTIVE.md` | Active roadmap status moved to `dev/ai/ROADMAP_ACTIVE.md`. |
| `dev/legacy/dev/ROADMAP_HISTORY.md` | Operational roadmap status lives in `dev/ai/ROADMAP_ACTIVE.md`. |
| `dev/legacy/dev/ai/ROADMAP_ACTIVE.md` | / next / PATCH_11_OUT_OF_SCOPE / |
| `dev/legacy/dev/ai/ROADMAP_ACTIVE.md` | / 521 / 521 / DONE_PARTIAL_BLOCKED / HIGH / release signing + Pixel clone final gate / lint/test/assembleDebug PASS; Pixel clone PASS; signing env missing; TCL pending / |
| `dev/legacy/dev/ai/ROADMAP_ACTIVE.md` | / NOW_acceptance / code invariant preserved; device validation pending / |
| `dev/legacy/dev/ai/ROADMAP_ACTIVE.md` | - Do not mark next patch DONE before gates pass. |

LEGACY_SUMMARY
- legacy_docs_read_count: 140
- legacy_docs_read:
- `dev/README.md`
- `dev/archive/transient/codex log.txt`
- `dev/archive/transient/last_fix_attempts.txt`
- `dev/legacy/dev/human/PROJECT_OVERVIEW.md`
- `dev/legacy/dev/CAPSULE_INDEX.md`
- `dev/legacy/dev/ai/CAPSULE_INDEX.md`
- `dev/legacy/dev/ai/INDEX.md`
- `dev/legacy/dev/archive/INDEX.md`
- `dev/legacy/dev/human/INDEX.md`
- `dev/legacy/dev/ARCHITECTURE_LOCK.md`
- `dev/legacy/dev/ai/ARCHITECTURE_LOCK.md`
- `dev/legacy/dev/ai/OPERATING_RULES.md`
- `dev/legacy/dev/AGENT_RULES.md`
- `dev/legacy/dev/ai/AGENT_RULES.md`
- `dev/legacy/dev/WORKFLOW.md`
- `dev/legacy/en/Workflows/Common Tracking Workflows.md`
- `dev/legacy/en/Workflows/Workflows.md`
- `dev/legacy/dev/ai/RELEASE_PROTOCOL.md`
- `dev/legacy/dev/ai/TEST_GATES.md`
- `dev/legacy/dev/BUG_REGISTRY.md`
- `dev/legacy/dev/ai/BUG_REGISTRY.md`
- `dev/legacy/dev/ai/RISK_REGISTER.md`
- `dev/legacy/dev/human/TROUBLESHOOTING.md`
- `dev/legacy/en/Troubleshooting/Troubleshooting.md`
- `dev/legacy/dev/ROADMAP_ACTIVE.md`
- `dev/legacy/dev/ROADMAP_HISTORY.md`
- `dev/legacy/dev/ai/ROADMAP_ACTIVE.md`
- `dev/legacy/dev/ai/ROADMAP_HISTORY.md`
- `dev/legacy/dev/human/ROADMAP.md`
- `dev/legacy/dev/human/ROADMAP_EXPLAINED.md`
- `dev/legacy/dev/human/CHANGELOG.md`
- `dev/legacy/dev/human/FEATURES.md`
- `dev/legacy/en/Features/Chains.md`
- `dev/legacy/en/Features/Features.md`
- `dev/legacy/en/Features/Home Screen Widget.md`
- `dev/legacy/en/Features/Import, Export, and Vaults.md`
- `dev/legacy/en/Features/Life Periods.md`
- `dev/legacy/en/Features/Timed Sessions and Alerts.md`
- `dev/legacy/.codex_patch_current_v474/dev/ROADMAP_ACTIVE.md`
- `dev/legacy/.codex_patch_current_v474/dev/ROADMAP_HISTORY.md`
- `dev/legacy/.codex_patch_snapshot_v474/dev/ROADMAP_ACTIVE.md`
- `dev/legacy/.codex_patch_snapshot_v474/dev/ROADMAP_HISTORY.md`
- `dev/legacy/dev/CODEBASE_MAP.md`
- `dev/legacy/dev/CONTRACT.md`
- `dev/legacy/en/Home.md`
- `dev/legacy/it/Home.md`
- `dev/legacy/submission/v493_submission_checklist.md`
- `dev/legacy/dev/ai/CAPSULES.md`
- `dev/legacy/dev/ai/DB_SCHEMA.md`
- `dev/legacy/dev/ai/PLAYSTORE_GATEKEEPER.md`
- `dev/legacy/dev/archive/AGENTS.md`
- `dev/legacy/dev/archive/FUTURE_PATCHES.md`
- `dev/legacy/dev/archive/UI_CONTRACT.md`
- `dev/legacy/dev/human/PLAYSTORE_READINESS_REPORT.md`
- `dev/legacy/en/Core Concepts/Continuity.md`
- `dev/legacy/en/Core Concepts/Core Concepts.md`
- `dev/legacy/en/Core Concepts/Session.md`
- `dev/legacy/en/Core Concepts/Tag.md`
- `dev/legacy/en/Core Concepts/Time Machine.md`
- `dev/legacy/en/Core Concepts/Time Reconstruction.md`
- `dev/legacy/en/FAQ/FAQ.md`
- `dev/legacy/en/Getting Started/First Launch and Setup.md`
- `dev/legacy/en/Getting Started/Start Here.md`
- `dev/legacy/en/Getting Started/Your First Session.md`
- `dev/legacy/en/Interface/Chronology.md`
- `dev/legacy/en/Interface/Interface.md`
- `dev/legacy/en/Interface/Now.md`
- `dev/legacy/en/Interface/Secondary Areas and Settings.md`
- `dev/legacy/en/Interface/Tags.md`
- `dev/legacy/en/Philosophy/Philosophy.md`
- `dev/legacy/en/Use Cases/Real-World Scenarios.md`
- `dev/legacy/en/Use Cases/Use Cases.md`
- `dev/legacy/it/Casi d'Uso/Casi d'Uso.md`
- `dev/legacy/it/Casi d'Uso/Scenari Reali.md`
- `dev/legacy/it/Concetti Base/Concetti Base.md`
- `dev/legacy/it/Concetti Base/Continuita.md`
- `dev/legacy/it/Concetti Base/Macchina del Tempo.md`
- `dev/legacy/it/Concetti Base/Ricostruzione del Tempo.md`
- `dev/legacy/it/Concetti Base/Sessione.md`
- `dev/legacy/it/Concetti Base/Tag.md`
- `dev/legacy/it/FAQ/Domande Frequenti.md`
- `dev/legacy/it/Filosofia/Filosofia.md`
- `dev/legacy/it/Flussi di Lavoro/Flussi di Lavoro.md`
- `dev/legacy/it/Flussi di Lavoro/Flussi di Tracciamento Comuni.md`
- `dev/legacy/it/Funzioni/Catene.md`
- `dev/legacy/it/Funzioni/Funzioni.md`
- `dev/legacy/it/Funzioni/Importazione, Esportazione e Vault.md`
- `dev/legacy/it/Funzioni/Periodi di Vita.md`
- `dev/legacy/it/Funzioni/Sessioni Temporizzate e Alert.md`
- `dev/legacy/it/Funzioni/Widget Schermata Home.md`
- `dev/legacy/it/Guida Introduttiva/Inizia da Qui.md`
- `dev/legacy/it/Guida Introduttiva/La Prima Sessione.md`
- `dev/legacy/it/Guida Introduttiva/Primo Avvio e Configurazione.md`
- `dev/legacy/it/Interfaccia/Adesso.md`
- `dev/legacy/it/Interfaccia/Aree Secondarie e Impostazioni.md`
- `dev/legacy/it/Interfaccia/Cronologia.md`
- `dev/legacy/it/Interfaccia/Interfaccia.md`
- `dev/legacy/it/Interfaccia/Tag.md`
- `dev/legacy/it/Risoluzione Problemi/Risoluzione Problemi.md`
- `dev/legacy/forensic/914683_20260529_154033/db_report.md`
- `build.gradle.kts`
- `settings.gradle.kts`
- `gradle.properties`
- `dev/tools/check_hardcoded_ui_strings.py`
- `dev/tools/check_single_submit_confirm_buttons.sh`
- `dev/tools/clean_transients.sh`
- `preflight_check.ps1`
- `tools/mtt_helper.py`
- `app/src/androidTest/java/com/example/multitimetracker/ExampleInstrumentedTest.kt`
- `app/src/androidTest/java/com/example/multitimetracker/MainViewModelRecoveryTest.kt`
- `app/src/androidTest/java/com/example/multitimetracker/SessionOnlyE2eTest.kt`
- `app/src/androidTest/java/com/example/multitimetracker/TimedSessionNotificationFlowTest.kt`
- `app/src/androidTest/java/com/example/multitimetracker/capsules/importexport/ImportExportCapsuleViewModelTest.kt`
- `app/src/androidTest/java/com/example/multitimetracker/export/AuthoritativeExportPayloadBuilderTest.kt`
- `app/src/androidTest/java/com/example/multitimetracker/persistence/AuthoritativeSessionRuntimeTest.kt`
- `app/src/androidTest/java/com/example/multitimetracker/persistence/PersistenceImportExportTest.kt`
- `app/src/androidTest/java/com/example/multitimetracker/persistence/PersistenceImportExportTestSupport.kt`
- `app/src/androidTest/java/com/example/multitimetracker/persistence/QuickEventRepositoryTest.kt`
- `app/src/test/java/com/example/multitimetracker/EffectiveTimeContextTest.kt`
- `app/src/test/java/com/example/multitimetracker/FirstRunRestoreContractTest.kt`
- extracted: purpose, stack, commands, invariants, bugs, roadmap, changelog, code map.
- historical_only: original local docs in `dev/legacy`; use only when AI doc lacks detail or for audit history.

LINKS
- metadata: [dev/project.metadata.json](../../../projects/MultiTimeTracker/dev/project.metadata.json)
- human_overview: [human overview](../../human/projects/multitimetracker/overview.md)
- human_folder: [human folder](../../human/projects/multitimetracker)
- legacy_docs: [dev/legacy](../../../projects/MultiTimeTracker/dev/legacy)
- repo_path: [repo](../../../projects/MultiTimeTracker)

OPEN_QUESTIONS
- dev/legacy/dev/human/ROADMAP_EXPLAINED.md: - Closed the v515 static lint blocker for app-open snapshot-change receiver registration.
- dev/legacy/dev/human/CHANGELOG.md: - Fixed the remaining v515 lint blocker by registering the app-open snapshot-change receiver as not exported through AndroidX `ContextCompat`.
- dev/legacy/dev/human/CHANGELOG.md: - `v513`: fixed startup/reopen regression by avoiding repeated Time Machine VACUUM, moving background persistence/vault export I/O off the main thread, and keeping drawer state process-local.
- dev/legacy/.codex_patch_current_v474/dev/ROADMAP_ACTIVE.md: - Registered the open `ALERT_START_TIMER_OFFSET` bug so the known delayed START-timer drift stays visible while the alert stack evolves.
- dev/legacy/.codex_patch_current_v474/dev/ROADMAP_ACTIVE.md: - Fixed the alert regression by making timed `ON_START` scheduling work again in session-only mode and by hardening scheduled delivery checks against stale/ghost fires.
- dev/legacy/.codex_patch_current_v474/dev/ROADMAP_HISTORY.md: - Follow-up regression patch: fixed the startup crash by making snapshot bootstrap accept legacy task-shaped rows in `closedSessions` and `tagSessions` instead of throwing on missing `sessionId`, whi
- dev/legacy/.codex_patch_current_v474/dev/ROADMAP_HISTORY.md: - Follow-up regression patch: completed the core JVM smoke net for authoritative session start/stop/expiry/recovery flows and recorded the still-open START-timer offset bug for future repair.
- dev/legacy/.codex_patch_current_v474/dev/ROADMAP_HISTORY.md: - Follow-up regression patch: fixed broken alert firing by reconnecting timed start alerts to the real running session and by stopping stale delayed alerts from notifying after the session had alread
- dev/legacy/.codex_patch_current_v474/dev/ROADMAP_HISTORY.md: - Tight regression patch: real-time timed-session expiry reconciliation, Since When stale render cleanup plus compact `d/h/m` duration labels, and alarm-mode full-screen permission check/guidance.
- dev/legacy/.codex_patch_snapshot_v474/dev/ROADMAP_ACTIVE.md: - Registered the open `ALERT_START_TIMER_OFFSET` bug so the known delayed START-timer drift stays visible while the alert stack evolves.
- dev/legacy/.codex_patch_snapshot_v474/dev/ROADMAP_ACTIVE.md: - Fixed the alert regression by making timed `ON_START` scheduling work again in session-only mode and by hardening scheduled delivery checks against stale/ghost fires.
- dev/legacy/.codex_patch_snapshot_v474/dev/ROADMAP_HISTORY.md: - Follow-up regression patch: fixed the startup crash by making snapshot bootstrap accept legacy task-shaped rows in `closedSessions` and `tagSessions` instead of throwing on missing `sessionId`, wh
