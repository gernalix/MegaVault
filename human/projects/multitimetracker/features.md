# MultiTimeTracker Features

This page translates extracted project facts into a user-readable feature view. Items marked `UNKNOWN` need manual confirmation before product or release decisions.

## Main Capabilities
- dev/archive/transient/codex log.txt: REGOLE FUNZIONALI
- dev/archive/transient/codex log.txt: FEATURE CAPSULE
- dev/legacy/dev/archive/INDEX.md: # ARCHIVE INDEX
- dev/legacy/en/Workflows/Common Tracking Workflows.md: # Common Tracking Workflows
- dev/legacy/en/Workflows/Common Tracking Workflows.md: ## Daily Live Workflow
- dev/legacy/en/Workflows/Common Tracking Workflows.md: ## Minimal Workflow
- dev/legacy/en/Workflows/Common Tracking Workflows.md: ## Catch-Up Workflow
- dev/legacy/en/Workflows/Common Tracking Workflows.md: ## Advanced Review Workflow
- dev/legacy/en/Workflows/Workflows.md: # Workflows
- dev/legacy/dev/ai/TEST_GATES.md: ## QUICK_EVENTS_ACCEPTANCE
- dev/legacy/dev/human/TROUBLESHOOTING.md: ## Backups
- dev/archive/transient/last_fix_attempts.txt: - Fix: replace gradle.buildFinished(...) with gradle.addBuildListener(BuildAdapter.buildFinished) to avoid Kotlin DSL/Closure mismatch on Gradle 9.x.
- dev/legacy/dev/human/PROJECT_OVERVIEW.md: MultiTimeTracker is a local-first Android time tracker. The main data lives in the app SQLite database, with sessions and shared tags as the core model.
- dev/legacy/dev/archive/INDEX.md: `dev/archive/*` is historical evidence only.

## Useful Limits And Boundaries
- dev/archive/transient/codex log.txt: - read-only
- dev/archive/transient/codex log.txt: 3) Da quel momento tutta l’app entra in read-only.
- dev/archive/transient/codex log.txt: - espone effectiveNowMs / read-only flags / banner state
- dev/archive/transient/codex log.txt: Migrazioni DB devono essere backward-safe.
- dev/archive/transient/codex log.txt: Ma non limitarti a spostare il versioning lì:
- dev/archive/transient/codex log.txt: - eventuale patch version runtime-only mostrata nell'app
- dev/archive/transient/codex log.txt: connectedAndroidTest sul clone parte ma fallisce 1 test esistente non-Time-Machine: SQLiteDatabaseLockedException in SessionOnlyE2eTest.
- dev/archive/transient/codex log.txt: Non ho potuto chiudere da terminale lo smoke manuale end-to-end della nuova UI Time Machine sul device.
- dev/archive/transient/codex log.txt: 3) applica read-only reale a tutte le write actions raggiungibili da ogni tab
- dev/archive/transient/codex log.txt: 4) esegui smoke test manuale minimo sul clone app Pixel della nuova UI Time Machine
- dev/archive/transient/codex log.txt: Sto chiudendo la copertura tab-per-tab sul serio: ora verifico i punti ancora live nei capsule/screens, completo i blocchi write raggiungibili dai menu/settings e poi faccio uno smoke manuale sul clone Pixel della nuova UI.
- dev/archive/transient/codex log.txt: La parte codice è allineata; adesso faccio davvero lo smoke manuale sul clone Pixel usando adb, dump UI e screenshot per entrare in Time Machine e verificare i punti minimi richiesti senza inventare risultati.

## Where The Feature Code Appears To Live
- `app/src/main/AndroidManifest.xml`
- `app/src/main/java/com/example/multitimetracker/MainActivity.kt`
- `dev/tools/check_hardcoded_ui_strings.py`
- `tools/mtt_helper.py`
- `dev/tools/check_single_submit_confirm_buttons.sh`
- `dev/tools/clean_transients.sh`
- `gradlew`
- `preflight_check.ps1`
