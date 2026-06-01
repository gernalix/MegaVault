# MultiTimeTracker Troubleshooting

Use this page for symptoms and checks. For operational decisions, confirm against the AI doc first.

## Known Problems And Symptoms
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

## Useful Checks Or Commands
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

## Safety Checks Before Fixing
- dev/archive/transient/codex log.txt: - read-only
- dev/archive/transient/codex log.txt: 3) Da quel momento tutta l’app entra in read-only.
- dev/archive/transient/codex log.txt: - DATABASE TIME
- dev/archive/transient/codex log.txt: - scrivere nel database
- dev/archive/transient/codex log.txt: Tutti i timestamp scritti nel database devono sempre usare il tempo reale del dispositivo.
- dev/archive/transient/codex log.txt: - espone effectiveNowMs / read-only flags / banner state
- dev/archive/transient/codex log.txt: - eventuale history/versioning o eventi strutturati replayabili se semplici timestamp non bastano
- dev/archive/transient/codex log.txt: - history/version table minima
- dev/archive/transient/codex log.txt: Migrazioni DB devono essere backward-safe.
- dev/archive/transient/codex log.txt: Ma non limitarti a spostare il versioning lì:
- dev/archive/transient/codex log.txt: - NON incrementare la versione durante i normali build/test intermedi della patch
- dev/archive/transient/codex log.txt: - incrementa la versione solo nel packaging/release finale della patch
- dev/archive/transient/codex log.txt: - eventuale patch version runtime-only mostrata nell'app
- dev/archive/transient/codex log.txt: Clone com.example.multitimetracker.devicetest installato e avviabile sul Pixel via adb.
