# os-observer Features

This page translates extracted project facts into a user-readable feature view. Items marked `UNKNOWN` need manual confirmation before product or release decisions.

## Main Capabilities
- dev/legacy/README.md: ## Export per ChatGPT
- dev/legacy/dev/INDEX.md: ## Monitor Kuma -> recovery handler
- dev/legacy/dev/INDEX.md: ## Cleanup incidente backup SQLite
- dev/legacy/ARCHITECTURE.md: ## Export pipeline
- dev/legacy/ARCHITECTURE.md: ## Patch import
- dev/legacy/ARCHITECTURE.md: ## Health monitoring
- dev/legacy/PATCH_WORKFLOW.md: # Patch Workflow
- dev/legacy/PATCH_WORKFLOW.md: ## Perche non sostituire piu il DB live
- dev/legacy/PATCH_WORKFLOW.md: ## Recuperare da import fallito
- dev/legacy/TROUBLESHOOTING.md: ## Export enorme
- dev/legacy/TROUBLESHOOTING.md: ## Import patch fallito
- dev/legacy/TROUBLESHOOTING.md: ## Fork DB da export
- dev/legacy/OPERATIONS.md: ## Status e dashboard
- dev/legacy/OPERATIONS.md: ## Export

## Useful Limits And Boundaries
- dev/legacy/README.md: - Produce export ChatGPT-friendly con snapshot SQLite readonly e workflow patch SQL.
- dev/legacy/README.md: - Non avvia backup.
- dev/legacy/README.md: - Il recorder principale non modifica i servizi osservati. L'agente separato `os_observer_autofix_agent.py` puo tentare recovery allowlist/safe-guard quando `OS_OBSERVER_AUTOFIX_DRY_RUN=0`.
- dev/legacy/README.md: - Non fa export continui o log raw illimitati.
- dev/legacy/README.md: `os_observer_autofix_agent.py` v17 monitora anche Uptime Kuma dashboard #8 (`http://150.230.148.128:3001/dashboard/8`) in modo read-only. I monitor noti sono mappati a handler locali con cooldown e safe-guard:
- dev/legacy/README.md: `os-observer-autofix`, `alert os-observer-autofix`, `rsync-transfer`, `mint-home-backup`, `mint-home-backup-retention`, `cloud backup`, `amici_fb`, `mint heartbeat`, `parcel-tracker`.
- dev/legacy/README.md: Ogni recovery attempt viene scritto in `knowledge.sqlite`. Monitor down senza mapping registrano `NO_MAPPING` e non eseguono comandi. Il runtime locale v17 usa `OS_OBSERVER_AUTOFIX_DRY_RUN=0`; data mover, backup e cloud backup restano pro
- dev/legacy/README.md: v17 legge anche `heartbeatList` Socket.IO, quindi i push monitor reali non restano `unknown`: `status=0` o heartbeat stale diventano DOWN recuperabili. Per `mint-home-backup-retention` la recovery consentita e non distruttiva: refresh del
- dev/legacy/README.md: La guardia locale freeze-risk non dipende dal watcher Kuma: se vede load/PSI alto insieme a observer stalled, registra `FREEZE_RISK_LOCAL_PROTECTION` in `knowledge.sqlite`; in apply mode ferma o declassa diagnostici propri e declassa proc
- dev/legacy/README.md: Admission control valuta MemAvailable, SwapFree, load, PSI CPU/I/O/memory, rsync/backup attivi e Gradle/Kotlin gia attivi. Le decisioni sono `ALLOW`, `ALLOW_ULTRA_LIGHT`, `DEFER`, `QUEUE`, `SKIP`, `ABORT_EMERGENCY`; Gradle non viene forza
- dev/legacy/README.md: Durante `run`, il heartbeat e ultra-leggero: scrive solo `git status --short` troncato a pochi KB e non esegue mai `git diff --binary`, stash o snapshot completi. I diff completi sono ammessi solo per `preflight`, `checkpoint` manuale, `P
- dev/legacy/README.md: Gli export sono snapshot readonly. Eventuali modifiche devono tornare come patch SQL incrementale:

## Where The Feature Code Appears To Live
- `codex_freeze_runner.py`
- `kuma_auto_healer.py`
- `os_observer_ai_diagnostics.py`
- `os_observer_autofix_agent.py`
- `os_observer.sh`
- `os_observer_autofix_dashboard.sh`
- `os_observer_cleanup.sh`
- `os_observer_dashboard.sh`
- `os_observer_export.sh`
- `os_observer_memory.sh`
- `tests/test_autofix_agent.py`
- `tests/test_codex_freeze_runner.py`
