# os-observer AI OPERATIONS

PROJECT
- name: os-observer
- slug: os-observer
- purpose: Linux Mint black-box recorder: user-systemd timer records read-only telemetry into SQLite, maintains diagnostic knowledge, exports bounded context for ChatGPT/Codex, and has guarded autofix/heartbeat logic.
- current_status: Working tree has 10 non-clean entries; do not mix unrelated changes. First entries: M codex_freeze_runner.py, M config/codex-resource-presets.json, M tests/test_codex_freeze_runner.py, ?? .codexmeta, ?? .codexmeta.bak.20260528_191731
- repo_path: `/home/daniele/codex-workspace/os-observer`
- remote: `none`
- branch: `codex/prompt-914582`
- last_verified_commit/date: `b1ed3b0` / `2026-06-01T13:20:29+02:00`

STACK
- languages: Python, Shell
- frameworks: UNKNOWN
- DB: SQLite
- platform: UNKNOWN
- external_tools/services: systemd

CODE_MAP
entrypoints:
- `codex_freeze_runner.py`
- `kuma_auto_healer.py`
- `os_observer_ai_diagnostics.py`
- `os_observer_autofix_agent.py`
important_folders:
- `config`
- `dev`
- `docs`
- `systemd`
- `tests`
important_files:
- `dev/README.md`
tests:
- `tests/test_autofix_agent.py`
- `tests/test_codex_freeze_runner.py`
scripts:
- `codex_freeze_runner.py`
- `kuma_auto_healer.py`
- `os_observer.sh`
- `os_observer_ai_diagnostics.py`
- `os_observer_autofix_agent.py`
- `os_observer_autofix_dashboard.sh`
- `os_observer_cleanup.sh`
- `os_observer_dashboard.sh`
- `os_observer_export.sh`
- `os_observer_memory.sh`
- `tests/test_autofix_agent.py`
- `tests/test_codex_freeze_runner.py`
generated/runtime/avoid_touch_casually:
- `dev/legacy`

ARCH
summary:
- dev/legacy/README.md: `os-observer` e un black-box recorder diagnostico leggero per Linux Mint. Mantiene un DB SQLite sempre aggiornato tramite timer systemd user e produce export bounded per ChatGPT/Codex.
- dev/legacy/dev/INDEX.md: # os-observer autofix agent v19
- dev/legacy/ARCHITECTURE.md: `os-observer.timer` avvia `os_observer.sh --once`. Il run prende il lock, inizializza schema/WAL, raccoglie metriche read-only, salva snapshot/eventi in `telemetry.sqlite`, aggiorna memoria diagnostica in `knowledge.sqlite`, valuta 
- dev/legacy/dev/ARCHITECTURE.md: - `os_observer_autofix_agent.py`: correlazione, dedup, fix allowlist, watcher Uptime Kuma dashboard #8, freeze-risk guard locale e heartbeat Kuma indipendente dal ciclo recovery.
- dev/legacy/dev/AGENT_RULES.md: - Usa timeout per comandi lenti.
- dev/legacy/PATCH_WORKFLOW.md: ## Perche non sostituire piu il DB live
- dev/legacy/dev/TEST_PLAN.md: - `python -m py_compile os_observer_autofix_agent.py`
- dev/legacy/TROUBLESHOOTING.md: ./os_observer.sh --smart-retention
- dev/legacy/dev/CHANGELOG.md: - Added configurable cgroups v2 containment for Codex/Android/adb/heavy local jobs through `codex_freeze_runner.py` and `config/codex-resource-presets.json`.
- dev/legacy/OPERATIONS.md: systemctl --user enable --now os-observer.timer
components/dataflow/design_decisions:
| source | fact |
|---|---|
| `dev/legacy/README.md` | # os-observer v19 |
| `dev/legacy/README.md` | ## Cosa fa |
| `dev/legacy/README.md` | ## Cosa non fa |
| `dev/legacy/README.md` | ## Path principali |
| `dev/legacy/README.md` | ## Timer 24/7 |
| `dev/legacy/README.md` | ## Comandi principali |
| `dev/legacy/README.md` | ## Autofix Kuma |
| `dev/legacy/README.md` | ## Codex freeze runner |
| `dev/legacy/README.md` | ## Export per ChatGPT |
| `dev/legacy/README.md` | ## Troubleshooting rapido |
| `dev/legacy/dev/INDEX.md` | # os-observer autofix agent v19 |
| `dev/legacy/dev/INDEX.md` | ## Checklist rapida |
| `dev/legacy/dev/INDEX.md` | ## Invarianti |
| `dev/legacy/dev/INDEX.md` | ## Monitor Kuma -> recovery handler |
| `dev/legacy/dev/INDEX.md` | ## Anti-loop e memoria |
| `dev/legacy/dev/INDEX.md` | ## Cleanup incidente backup SQLite |
| `dev/legacy/dev/INDEX.md` | ## Docs |
| `dev/legacy/ARCHITECTURE.md` | # Architecture |

INVARIANTS
architecture/data/UX/safety/versioning/localization:
| source | fact |
|---|---|
| `dev/legacy/README.md` | - Produce export ChatGPT-friendly con snapshot SQLite readonly e workflow patch SQL. |
| `dev/legacy/README.md` | ## Cosa non fa |
| `dev/legacy/README.md` | - Non avvia backup. |
| `dev/legacy/README.md` | - Non avvia rsync. |
| `dev/legacy/README.md` | - Non avvia build Android, Gradle o Android Studio. |
| `dev/legacy/README.md` | - Il recorder principale non modifica i servizi osservati. L'agente separato `os_observer_autofix_agent.py` puo tentare recovery allowlist/safe-guard quando `OS_OBSERVER_AUTOFIX_DRY_RUN=0`. |
| `dev/legacy/README.md` | - Non salva segreti, token Telegram, env sensibili o transcript infiniti. |
| `dev/legacy/README.md` | - Non fa export continui o log raw illimitati. |
| `dev/legacy/README.md` | - Non accetta piu DB completi modificati da ChatGPT/Codex come sorgente live: usare `--apply-patch`. |
| `dev/legacy/README.md` | `/home/daniele/os_observer/db/os_observer.sqlite` resta path legacy/compatibilita. Nel prompt #847 e stato sostituito una tantum da `os_observer_updated2.sqlite`; il recorder v17 scrive su `telemetry.sqlite`. |
| `dev/legacy/README.md` | `os_observer_autofix_agent.py` v17 monitora anche Uptime Kuma dashboard #8 (`http://150.230.148.128:3001/dashboard/8`) in modo read-only. I monitor noti sono mappati a handler locali con cooldown e safe-guard: |
| `dev/legacy/README.md` | `os-observer-autofix`, `alert os-observer-autofix`, `rsync-transfer`, `mint-home-backup`, `mint-home-backup-retention`, `cloud backup`, `amici_fb`, `mint heartbeat`, `parcel-tracker`. |
| `dev/legacy/README.md` | Ogni recovery attempt viene scritto in `knowledge.sqlite`. Monitor down senza mapping registrano `NO_MAPPING` e non eseguono comandi. Il runtime locale v17 usa `OS_OBSERVER_AUTOFIX_DRY_RUN=0`; data mover, backup e cloud backup restano pro |
| `dev/legacy/README.md` | v17 legge anche `heartbeatList` Socket.IO, quindi i push monitor reali non restano `unknown`: `status=0` o heartbeat stale diventano DOWN recuperabili. Per `mint-home-backup-retention` la recovery consentita e non distruttiva: refresh del |
| `dev/legacy/README.md` | Se Kuma segnala ID 8 down per `No heartbeat in the time window` ma `os-observer-autofix-agent.service` e ancora `active/running`, v17 non riavvia il servizio: manda un heartbeat refresh e registra `HEARTBEAT_REFRESHED_PROCESS_ALIVE`. Il r |
| `dev/legacy/README.md` | La guardia locale freeze-risk non dipende dal watcher Kuma: se vede load/PSI alto insieme a observer stalled, registra `FREEZE_RISK_LOCAL_PROTECTION` in `knowledge.sqlite`; in apply mode ferma o declassa diagnostici propri e declassa proc |
| `dev/legacy/README.md` | Admission control valuta MemAvailable, SwapFree, load, PSI CPU/I/O/memory, rsync/backup attivi e Gradle/Kotlin gia attivi. Le decisioni sono `ALLOW`, `ALLOW_ULTRA_LIGHT`, `DEFER`, `QUEUE`, `SKIP`, `ABORT_EMERGENCY`; Gradle non viene forza |
| `dev/legacy/README.md` | Durante `run`, il heartbeat e ultra-leggero: scrive solo `git status --short` troncato a pochi KB e non esegue mai `git diff --binary`, stash o snapshot completi. I diff completi sono ammessi solo per `preflight`, `checkpoint` manuale, `P |
| `dev/legacy/README.md` | Il tarball contiene copie compatte di `telemetry.sqlite` e `knowledge.sqlite`, una copia compatibile `os_observer.sqlite`, `schema.sql`, `summary.txt`, `latest_events.txt`, `memory_summary.txt`, `chatgpt_context.txt`, `summary_for_chatgpt |
| `dev/legacy/README.md` | Gli export sono snapshot readonly. Eventuali modifiche devono tornare come patch SQL incrementale: |
| `dev/legacy/README.md` | `patch_backups` conserva solo backup completi pre-patch/manual repair con nomi `knowledge_before_patch_*.sqlite` o `telemetry_before_patch_*.sqlite`. Gli eventi runtime autofix scrivono righe nei DB e non clonano `telemetry.sqlite`. |
| `dev/legacy/README.md` | - DB non aggiornato: controllare `seconds_since_last_update` in `--status` o dashboard. |
| `dev/legacy/README.md` | - Backup SQLite fuori controllo: `./os_observer_cleanup.sh --sqlite-backups`. |
| `dev/legacy/dev/INDEX.md` | - Non avviare backup, rsync, Gradle, Android Studio. |
| `dev/legacy/dev/INDEX.md` | - Kuma dashboard watcher: legge `http://150.230.148.128:3001/dashboard/8` via endpoint web + Socket.IO read-only. Se `OS_OBSERVER_KUMA_AUTH_TOKEN_FILE` o `OS_OBSERVER_KUMA_AUTH_TOKEN` contiene un JWT valido usa `loginByToken` e legge ` |
| `dev/legacy/dev/INDEX.md` | - Transfer detector: `TRANSFER_RSYNC_STALLED` se il PID rsync dati e vivo ma log/progress non avanzano oltre soglia. |

BUILD_TEST
build_files:
- UNKNOWN
commands_found:
| source | fact |
|---|---|
| `dev/legacy/README.md` | - Non avvia rsync. |
| `dev/legacy/README.md` | systemctl --user daemon-reload |
| `dev/legacy/README.md` | systemctl --user enable --now os-observer.timer |
| `dev/legacy/README.md` | systemctl --user list-timers os-observer.timer |
| `dev/legacy/README.md` | python3 ./codex_freeze_runner.py preflight --repo /path/repo --prompt 936 |
| `dev/legacy/README.md` | python3 ./codex_freeze_runner.py run --repo /path/repo --prompt 936 -- codex |
| `dev/legacy/README.md` | python3 ./codex_freeze_runner.py checkpoint --repo /path/repo --prompt 936 --label manual |
| `dev/legacy/README.md` | python3 ./codex_freeze_runner.py recover --prompt 936 |
| `dev/legacy/README.md` | python3 ./codex_freeze_runner.py status --capabilities |
| `dev/legacy/README.md` | python3 ./codex_freeze_runner.py enqueue --cwd /path/repo --prompt 936 --preset codex_light -- codex |
| `dev/legacy/README.md` | python3 ./codex_freeze_runner.py run-next |
| `dev/legacy/README.md` | python3 ./codex_freeze_runner.py android --repo /path/android --prompt 936 build assembleDebug |
| `dev/legacy/README.md` | Admission control valuta MemAvailable, SwapFree, load, PSI CPU/I/O/memory, rsync/backup attivi e Gradle/Kotlin gia attivi. Le decisioni sono `ALLOW`, `ALLOW_ULTRA_LIGHT`, `DEFER`, `QUEUE`, `SKIP`, `ABORT_EMERGENCY`; Gradle non viene forza |
| `dev/legacy/README.md` | python3 ./codex_freeze_runner.py list |
| `dev/legacy/README.md` | python3 ./codex_freeze_runner.py run-next --debug-run-next --trace-admission --trace-systemd --trace-queue |
| `dev/legacy/README.md` | python3 ./codex_freeze_runner.py status --detailed |
| `dev/legacy/README.md` | python3 ./codex_freeze_runner.py active-operation |
| `dev/legacy/README.md` | python3 ./codex_freeze_runner.py current-phase |
| `dev/legacy/README.md` | python3 ./codex_freeze_runner.py queue-lock-info |
| `dev/legacy/README.md` | python3 ./codex_freeze_runner.py current-throttle-state |
| `dev/legacy/README.md` | python3 ./codex_freeze_runner.py reconcile |
| `dev/legacy/README.md` | python3 ./codex_freeze_runner.py recover-stale |
| `dev/legacy/README.md` | python3 ./codex_freeze_runner.py inspect-job 1 |
| `dev/legacy/README.md` | python3 ./codex_freeze_runner.py inspect-unit codex-contained-example.service |
test_targets:
- `tests/test_autofix_agent.py`
- `tests/test_codex_freeze_runner.py`
known_test_flakiness_or_requirements:
- dev/legacy/README.md: - Mantiene knowledge diagnostica stabile in `knowledge.sqlite`: soluzioni note, tentativi di fix, incident registry, root cause, regressioni, decisioni di tuning e import patch.
- dev/legacy/README.md: - Entra in protezione quando load/PSI e stallo observer indicano freeze-risk: salva snapshot minimo, salta diagnostici invasivi e rinvia retention/VACUUM.
- dev/legacy/README.md: Il timer esegue `os_observer.sh --once` ogni minuto con `flock`, `timeout` systemd e diagnostici bounded. Se `load1`, PSI I/O/memory o `OBSERVER_STALLED` superano soglia, il run registra `FREEZE_RISK_PROTECTION_MODE`, raccoglie solo dati 
- dev/legacy/README.md: La guardia locale freeze-risk non dipende dal watcher Kuma: se vede load/PSI alto insieme a observer stalled, registra `FREEZE_RISK_LOCAL_PROTECTION` in `knowledge.sqlite`; in apply mode ferma o declassa diagnostici propri e declassa proc
- dev/legacy/dev/INDEX.md: - Freeze-risk guard: se load/PSI cresce e l'observer risulta stalled, registra `FREEZE_RISK_LOCAL_PROTECTION` in `knowledge.sqlite`; in dry-run non agisce, in apply mode tocca solo diagnostici propri (`os-observer.service`, `journalctl
- dev/legacy/dev/INDEX.md: - Il recorder principale usa shedding diagnostico sotto freeze-risk: snapshot minimo, dedup/fingerprint, output bounded, retention/VACUUM rinviati finche load/PSI restano alti.
- dev/legacy/ARCHITECTURE.md: ## Lock e timeout
- dev/legacy/ARCHITECTURE.md: Il lock e `/tmp/os-observer.lock` con `flock -n`. I comandi shell potenzialmente lenti usano `timeout`, `MAX_OUTPUT_LINES` e `MAX_OUTPUT_BYTES`. SQLite usa timeout busy e WAL mode.
- dev/legacy/ARCHITECTURE.md: Il collector legge `journalctl -k` con lookback limitato e filtra keyword diagnostiche: freeze, PRE_EMERGENCY, EMERGENCY, CRITICAL, I/O, DID_ERROR, xhci, usb, reset, disconnect, ext4, oom, killed, hung, blocked, rsync, failed, timeo
- dev/legacy/dev/ARCHITECTURE.md: - `os_observer_autofix_agent.py`: correlazione, dedup, fix allowlist, watcher Uptime Kuma dashboard #8, freeze-risk guard locale e heartbeat Kuma indipendente dal ciclo recovery.

VERSIONING_RELEASE
rules/artifacts/commit_push/release_blockers:
| source | fact |
|---|---|
| `dev/legacy/README.md` | v17 legge anche `heartbeatList` Socket.IO, quindi i push monitor reali non restano `unknown`: `status=0` o heartbeat stale diventano DOWN recuperabili. Per `mint-home-backup-retention` la recovery consentita e non distruttiva: refresh del |
| `dev/legacy/dev/INDEX.md` | / `os-observer-autofix` / `os-observer-autofix-agent.service` user / Restart differito via `systemd-run --user --on-active=5` per non tagliare la scrittura corrente. / |
| `dev/legacy/dev/ARCHITECTURE.md` | - Avvia un thread heartbeat dedicato che invia sempre il push `os-observer-autofix` ogni `KUMA_HEARTBEAT_SECONDS`, anche quando `run_once()` e occupato in dashboard/recovery/cooldown/freeze-protection. |
| `dev/legacy/dev/ARCHITECTURE.md` | - Legge la dashboard Kuma #8 in modo read-only. Con JWT remember-me locale usa `loginByToken` e legge `monitorList` piu `heartbeatList` via Socket.IO; senza token usa fallback locale read-only sui push monitor noti. |
| `dev/legacy/dev/ARCHITECTURE.md` | - Mantiene i push monitor `mint-home-backup` e `mint-home-backup-retention` con timer user dedicati (`home-backup-kuma-push.timer`, `home-backup-retention-kuma-push.timer`) che chiamano solo lo script heartbeat read-only. |
| `dev/legacy/dev/ARCHITECTURE.md` | - Al boot/login entra in state machine `BOOTING -> WARMING_UP -> HEALTHY`, oppure `RECOVERING` quando applica recovery reali. Durante `WARMING_UP` i gap heartbeat dei push monitor noti sono rinviati e non generano recovery/alert |
| `dev/legacy/dev/ARCHITECTURE.md` | - Sotto freeze-risk, `os_observer.sh` registra lo stato e fa shedding: evita diagnostici invasivi ripetuti, limita output/tail, rinvia retention e non lancia VACUUM. |
| `dev/legacy/dev/ARCHITECTURE.md` | - Il heartbeat periodico non dipende da `run_once()`; `RECOVERY_CYCLE_DURATION` e `MAX_LOOP_DURATION` misurano quanto il ciclo lento resta occupato senza bloccare il push. |
| `dev/legacy/dev/ARCHITECTURE.md` | - Push monitor Kuma senza heartbeat recente espongono `WHY_DOWN`, `LAST_HEARTBEAT_AGE`, `RECOVERY_ACTION` e `RECOVERY_RESULT` nei log dell'autofix. |
| `dev/legacy/dev/AGENT_RULES.md` | - Non salvare `OS_OBSERVER_KUMA_AUTH_TOKEN` o push URL reali in repo. |
| `dev/legacy/dev/AGENT_RULES.md` | - Non cambiare nomi file tra versioni. |
| `dev/legacy/dev/AGENT_RULES.md` | - Nessun push remoto automatico. |
| `dev/legacy/dev/CHANGELOG.md` | - Hardened backup, retention and rsync pushers for post-reboot: backup has a dedicated idle heartbeat timer, retention waits before sending persistent mount-down, and rsync sends `OK idle` heartbeats after a fresh boot without star |
| `dev/legacy/dev/CHANGELOG.md` | - Added `os_observer_autofix_agent.py --doctor` and extended status output with heartbeat age, next expected heartbeat, and independent-heartbeat state. |
| `dev/legacy/dev/CHANGELOG.md` | - Added reboot/login resilience bootstrap: `os-observer-startup-bootstrap.service` runs at user `default.target`, enables the required user timers/services, starts the autofix daemon and both Kuma pushers, and sends initial `BOOTIN |
| `dev/legacy/dev/CHANGELOG.md` | - During boot grace, known push-monitor heartbeat gaps are deferred instead of recorded as recovery attempts, avoiding false-positive Kuma alert churn while the local pusher services come up. |
| `dev/legacy/dev/CHANGELOG.md` | - Parsed authenticated Kuma `heartbeatList` in addition to `monitorList`, so push monitors get real up/down status instead of remaining `unknown`. |
| `dev/legacy/dev/CHANGELOG.md` | - Added `home-backup-retention-kuma-push.service` and `.timer` for a safe 45s retention heartbeat that does not start backups or prune snapshots. |
| `dev/legacy/dev/CHANGELOG.md` | - Split the retention push secret into `/home/daniele/.config/home-backup/kuma-retention.env` so monitor ID 9 is updated independently from `mint-home-backup` ID 4. |
| `dev/legacy/dev/CHANGELOG.md` | - Changed local home-backup heartbeat cadence from 300s to 45s for future backup runs, matching Kuma's 60s push interval. |

DATA_STORAGE
DB_paths/backup/import/export/migration/retention/user_data_safety:
| source | fact |
|---|---|
| `dev/legacy/README.md` | - Produce export ChatGPT-friendly con snapshot SQLite readonly e workflow patch SQL. |
| `dev/legacy/README.md` | - Non avvia backup. |
| `dev/legacy/README.md` | - Non fa export continui o log raw illimitati. |
| `dev/legacy/README.md` | - Non accetta piu DB completi modificati da ChatGPT/Codex come sorgente live: usare `--apply-patch`. |
| `dev/legacy/README.md` | `/home/daniele/os_observer/db/os_observer.sqlite` resta path legacy/compatibilita. Nel prompt #847 e stato sostituito una tantum da `os_observer_updated2.sqlite`; il recorder v17 scrive su `telemetry.sqlite`. |
| `dev/legacy/README.md` | `os-observer-autofix`, `alert os-observer-autofix`, `rsync-transfer`, `mint-home-backup`, `mint-home-backup-retention`, `cloud backup`, `amici_fb`, `mint heartbeat`, `parcel-tracker`. |
| `dev/legacy/README.md` | Ogni recovery attempt viene scritto in `knowledge.sqlite`. Monitor down senza mapping registrano `NO_MAPPING` e non eseguono comandi. Il runtime locale v17 usa `OS_OBSERVER_AUTOFIX_DRY_RUN=0`; data mover, backup e cloud backup restano pro |
| `dev/legacy/README.md` | v17 legge anche `heartbeatList` Socket.IO, quindi i push monitor reali non restano `unknown`: `status=0` o heartbeat stale diventano DOWN recuperabili. Per `mint-home-backup-retention` la recovery consentita e non distruttiva: refresh del |
| `dev/legacy/README.md` | La guardia locale freeze-risk non dipende dal watcher Kuma: se vede load/PSI alto insieme a observer stalled, registra `FREEZE_RISK_LOCAL_PROTECTION` in `knowledge.sqlite`; in apply mode ferma o declassa diagnostici propri e declassa proc |
| `dev/legacy/README.md` | Admission control valuta MemAvailable, SwapFree, load, PSI CPU/I/O/memory, rsync/backup attivi e Gradle/Kotlin gia attivi. Le decisioni sono `ALLOW`, `ALLOW_ULTRA_LIGHT`, `DEFER`, `QUEUE`, `SKIP`, `ABORT_EMERGENCY`; Gradle non viene forza |
| `dev/legacy/README.md` | Il tarball contiene copie compatte di `telemetry.sqlite` e `knowledge.sqlite`, una copia compatibile `os_observer.sqlite`, `schema.sql`, `summary.txt`, `latest_events.txt`, `memory_summary.txt`, `chatgpt_context.txt`, `summary_for_chatgpt |
| `dev/legacy/README.md` | Gli export sono snapshot readonly. Eventuali modifiche devono tornare come patch SQL incrementale: |
| `dev/legacy/README.md` | `patch_backups` conserva solo backup completi pre-patch/manual repair con nomi `knowledge_before_patch_*.sqlite` o `telemetry_before_patch_*.sqlite`. Gli eventi runtime autofix scrivono righe nei DB e non clonano `telemetry.sqlite`. |
| `dev/legacy/README.md` | - DB non aggiornato: controllare `seconds_since_last_update` in `--status` o dashboard. |
| `dev/legacy/README.md` | - Backup SQLite fuori controllo: `./os_observer_cleanup.sh --sqlite-backups`. |
| `dev/legacy/dev/INDEX.md` | - Non avviare backup, rsync, Gradle, Android Studio. |
| `dev/legacy/dev/INDEX.md` | - Kuma dashboard watcher: legge `http://150.230.148.128:3001/dashboard/8` via endpoint web + Socket.IO read-only. Se `OS_OBSERVER_KUMA_AUTH_TOKEN_FILE` o `OS_OBSERVER_KUMA_AUTH_TOKEN` contiene un JWT valido usa `loginByToken` e legge ` |
| `dev/legacy/dev/INDEX.md` | - Transfer detector: `TRANSFER_RSYNC_STALLED` se il PID rsync dati e vivo ma log/progress non avanzano oltre soglia. |
| `dev/legacy/dev/INDEX.md` | - Telemetry guard: se `telemetry.sqlite` supera `OS_OBSERVER_TELEMETRY_STALE_SECONDS`, l'agent emette `TELEMETRY_STALE`, tenta checkpoint WAL o restart sicuro di `os-observer.timer`/`os-observer.service`, registra l'intervento in `know |
| `dev/legacy/dev/INDEX.md` | - Freeze-risk guard: se load/PSI cresce e l'observer risulta stalled, registra `FREEZE_RISK_LOCAL_PROTECTION` in `knowledge.sqlite`; in dry-run non agisce, in apply mode tocca solo diagnostici propri (`os-observer.service`, `journalctl |
| `dev/legacy/dev/INDEX.md` | - Scritture runtime: transazione e `integrity_check`, senza clone completo del DB. |
| `dev/legacy/dev/INDEX.md` | - Backup completi SQLite solo per `--apply-patch` o manual repair, con SQLite backup API e nomi allowlist `knowledge_before_patch_*.sqlite` / `telemetry_before_patch_*.sqlite`. |

KNOWN_BUGS
active/historical/root_causes/regression_checklist:
| source | fact |
|---|---|
| `dev/legacy/README.md` | - Ingerisce eventi kernel/journald filtrati per freeze, USB, I/O, ext4, OOM, hung task e errori. |
| `dev/legacy/README.md` | - Mantiene knowledge diagnostica stabile in `knowledge.sqlite`: soluzioni note, tentativi di fix, incident registry, root cause, regressioni, decisioni di tuning e import patch. |
| `dev/legacy/README.md` | - Entra in protezione quando load/PSI e stallo observer indicano freeze-risk: salva snapshot minimo, salta diagnostici invasivi e rinvia retention/VACUUM. |
| `dev/legacy/README.md` | Il timer esegue `os_observer.sh --once` ogni minuto con `flock`, `timeout` systemd e diagnostici bounded. Se `load1`, PSI I/O/memory o `OBSERVER_STALLED` superano soglia, il run registra `FREEZE_RISK_PROTECTION_MODE`, raccoglie solo dati  |
| `dev/legacy/README.md` | La guardia locale freeze-risk non dipende dal watcher Kuma: se vede load/PSI alto insieme a observer stalled, registra `FREEZE_RISK_LOCAL_PROTECTION` in `knowledge.sqlite`; in apply mode ferma o declassa diagnostici propri e declassa proc |
| `dev/legacy/README.md` | ## Codex freeze runner |
| `dev/legacy/dev/INDEX.md` | - Freeze-risk guard: se load/PSI cresce e l'observer risulta stalled, registra `FREEZE_RISK_LOCAL_PROTECTION` in `knowledge.sqlite`; in dry-run non agisce, in apply mode tocca solo diagnostici propri (`os-observer.service`, `journalctl |
| `dev/legacy/dev/INDEX.md` | - Il recorder principale usa shedding diagnostico sotto freeze-risk: snapshot minimo, dedup/fingerprint, output bounded, retention/VACUUM rinviati finche load/PSI restano alti. |
| `dev/legacy/dev/INDEX.md` | / `mint-home-backup-retention` / `/home/daniele/home_incremental_backup.sh --retention-report` / Refresh non distruttivo del report retention solo se DEST montata, lock non vivo e zero I/O error recenti. / |
| `dev/legacy/dev/INDEX.md` | / `mint heartbeat` / `system-watchdog.service`, `freeze-reboot-monitor.service`, fallback `os-observer.timer` / Restart/start solo del primo candidato caricato ma non attivo; se nessuno e inattivo registra safe-guard. / |
| `dev/legacy/ARCHITECTURE.md` | ## Lock e timeout |
| `dev/legacy/ARCHITECTURE.md` | Il lock e `/tmp/os-observer.lock` con `flock -n`. I comandi shell potenzialmente lenti usano `timeout`, `MAX_OUTPUT_LINES` e `MAX_OUTPUT_BYTES`. SQLite usa timeout busy e WAL mode. |
| `dev/legacy/ARCHITECTURE.md` | Il collector legge `journalctl -k` con lookback limitato e filtra keyword diagnostiche: freeze, PRE_EMERGENCY, EMERGENCY, CRITICAL, I/O, DID_ERROR, xhci, usb, reset, disconnect, ext4, oom, killed, hung, blocked, rsync, failed, timeo |
| `dev/legacy/dev/ARCHITECTURE.md` | - `os_observer_autofix_agent.py`: correlazione, dedup, fix allowlist, watcher Uptime Kuma dashboard #8, freeze-risk guard locale e heartbeat Kuma indipendente dal ciclo recovery. |
| `dev/legacy/dev/ARCHITECTURE.md` | - Avvia un thread heartbeat dedicato che invia sempre il push `os-observer-autofix` ogni `KUMA_HEARTBEAT_SECONDS`, anche quando `run_once()` e occupato in dashboard/recovery/cooldown/freeze-protection. |
| `dev/legacy/dev/ARCHITECTURE.md` | - Sotto freeze-risk, `os_observer.sh` registra lo stato e fa shedding: evita diagnostici invasivi ripetuti, limita output/tail, rinvia retention e non lancia VACUUM. |
| `dev/legacy/dev/ARCHITECTURE.md` | - La protezione freeze-risk puo agire solo su diagnostici propri e conserva `rsync_touched=0`; data mover e backup restano fuori dall'autofix locale. |
| `dev/legacy/dev/AGENT_RULES.md` | - Usa timeout per comandi lenti. |
| `dev/legacy/PATCH_WORKFLOW.md` | "SELECT ts,patch_filename,sha256,success,affected_tables,target_db,backup_path,error FROM patch_imports ORDER BY id DESC LIMIT 5;" |
| `dev/legacy/PATCH_WORKFLOW.md` | Se la validazione fallisce, il DB target non viene modificato. Controllare `patch_imports.error`, correggere la patch e riapplicarla. |
| `dev/legacy/dev/TEST_PLAN.md` | - Known root cause. |
| `dev/legacy/dev/TEST_PLAN.md` | - Freeze-risk guard with high load/I/O and RAM/swap OK records dry-run protection. |
| `dev/legacy/dev/TEST_PLAN.md` | - ID 8 heartbeat timeout with `os-observer-autofix-agent.service active/running` refreshes heartbeat and does not restart the service. |
| `dev/legacy/TROUBLESHOOTING.md` | "SELECT ts,patch_filename,success,target_db,backup_path,error FROM patch_imports ORDER BY id DESC LIMIT 5;" |

DO_NOT_BREAK
- Preserve `dev/project.metadata.json` -> this AI doc -> Human docs workflow.
- Preserve `dev/legacy/`; do not delete or rewrite historical docs without explicit migration intent.
- dev/legacy/README.md: - Non avvia backup.
- dev/legacy/README.md: - Il recorder principale non modifica i servizi osservati. L'agente separato `os_observer_autofix_agent.py` puo tentare recovery allowlist/safe-guard quando `OS_OBSERVER_AUTOFIX_DRY_RUN=0`.
- dev/legacy/README.md: `os_observer_autofix_agent.py` v17 monitora anche Uptime Kuma dashboard #8 (`http://150.230.148.128:3001/dashboard/8`) in modo read-only. I monitor noti sono mappati a handler locali con cooldown e safe-guard:
- dev/legacy/README.md: `os-observer-autofix`, `alert os-observer-autofix`, `rsync-transfer`, `mint-home-backup`, `mint-home-backup-retention`, `cloud backup`, `amici_fb`, `mint heartbeat`, `parcel-tracker`.
- dev/legacy/README.md: Ogni recovery attempt viene scritto in `knowledge.sqlite`. Monitor down senza mapping registrano `NO_MAPPING` e non eseguono comandi. Il runtime locale v17 usa `OS_OBSERVER_AUTOFIX_DRY_RUN=0`; data mover, backup e cloud backup restano pro
- dev/legacy/README.md: v17 legge anche `heartbeatList` Socket.IO, quindi i push monitor reali non restano `unknown`: `status=0` o heartbeat stale diventano DOWN recuperabili. Per `mint-home-backup-retention` la recovery consentita e non distruttiva: refresh del
- dev/legacy/README.md: La guardia locale freeze-risk non dipende dal watcher Kuma: se vede load/PSI alto insieme a observer stalled, registra `FREEZE_RISK_LOCAL_PROTECTION` in `knowledge.sqlite`; in apply mode ferma o declassa diagnostici propri e declassa proc
- dev/legacy/README.md: Admission control valuta MemAvailable, SwapFree, load, PSI CPU/I/O/memory, rsync/backup attivi e Gradle/Kotlin gia attivi. Le decisioni sono `ALLOW`, `ALLOW_ULTRA_LIGHT`, `DEFER`, `QUEUE`, `SKIP`, `ABORT_EMERGENCY`; Gradle non viene forza
- dev/legacy/README.md: `patch_backups` conserva solo backup completi pre-patch/manual repair con nomi `knowledge_before_patch_*.sqlite` o `telemetry_before_patch_*.sqlite`. Gli eventi runtime autofix scrivono righe nei DB e non clonano `telemetry.sqlite`.
- dev/legacy/README.md: - Backup SQLite fuori controllo: `./os_observer_cleanup.sh --sqlite-backups`.
- dev/legacy/dev/INDEX.md: - Non avviare backup, rsync, Gradle, Android Studio.
- dev/legacy/dev/INDEX.md: - Telemetry guard: se `telemetry.sqlite` supera `OS_OBSERVER_TELEMETRY_STALE_SECONDS`, l'agent emette `TELEMETRY_STALE`, tenta checkpoint WAL o restart sicuro di `os-observer.timer`/`os-observer.service`, registra l'intervento in `know
- dev/legacy/dev/INDEX.md: - Freeze-risk guard: se load/PSI cresce e l'observer risulta stalled, registra `FREEZE_RISK_LOCAL_PROTECTION` in `knowledge.sqlite`; in dry-run non agisce, in apply mode tocca solo diagnostici propri (`os-observer.service`, `journalctl
- dev/legacy/dev/INDEX.md: - Backup completi SQLite solo per `--apply-patch` o manual repair, con SQLite backup API e nomi allowlist `knowledge_before_patch_*.sqlite` / `telemetry_before_patch_*.sqlite`.
- dev/legacy/dev/INDEX.md: - Vietati `telemetry_autofix_*_autofix_event.sqlite` e backup ricorsivi da Trash/export/snapshot/quarantine.
- dev/legacy/dev/INDEX.md: - Data mover, backup, rsync, restic, Timeshift e transfer non vengono riavviati automaticamente anche se finiscono in failed.

RECENT_DECISIONS
| source | fact |
|---|---|
| `dev/legacy/dev/CHANGELOG.md` | # Changelog |
| `dev/legacy/dev/CHANGELOG.md` | ## v17 prompt #914582 |
| `dev/legacy/dev/CHANGELOG.md` | - Added configurable cgroups v2 containment for Codex/Android/adb/heavy local jobs through `codex_freeze_runner.py` and `config/codex-resource-presets.json`. |
| `dev/legacy/dev/CHANGELOG.md` | - Added CPU reservation via automatic `AllowedCPUs`, preserving at least one logical CPU for UI/system work. |
| `dev/legacy/dev/CHANGELOG.md` | - Added admission control decisions `ALLOW`, `ALLOW_ULTRA_LIGHT`, `DEFER`, `QUEUE`, `SKIP`, `ABORT_EMERGENCY` using RAM, swap, load, PSI, active rsync/backup and active Gradle/Kotlin evidence. |
| `dev/legacy/dev/CHANGELOG.md` | - Added PSI-driven adaptive throttling with smoothing and hysteresis; pressure raises reduce `CPUQuota`/`IOWeight`, increase cooldown and suppress heavy snapshot/diff work. |
| `dev/legacy/dev/CHANGELOG.md` | - Added local SQLite job queue with `enqueue`, `list`, `run-next`, `cancel`, `retry`, `pause`, `resume`. |
| `dev/legacy/dev/CHANGELOG.md` | - Added Android ultra-light wrappers for build, install, adb and instrumentation; wrappers queue by default and apply single-worker/no-daemon/no-parallel Gradle flags. |
| `dev/legacy/dev/CHANGELOG.md` | - Added tests for PSI hysteresis, admission decisions, cpuset selection, cgroup command generation, queue persistence, unsupported feature fallback and no forced Gradle under critical pressure. |
| `dev/legacy/dev/CHANGELOG.md` | ## v16 prompt #276 |
| `dev/legacy/dev/CHANGELOG.md` | - Root cause fixed for Kuma monitor ID 8 `os-observer-autofix`: the daemon heartbeat is now sent by a dedicated thread, independent from the slow recovery/dashboard/freeze-protection cycle. |
| `dev/legacy/dev/CHANGELOG.md` | - Added heartbeat metrics in `/home/daniele/os_observer/state/autofix_heartbeat_state.json`: `LAST_HEARTBEAT_SENT_AT`, `HEARTBEAT_SEND_RESULT`, `HEARTBEAT_LAG_SECONDS`, `WHY_HEARTBEAT_SKIPPED`, and send duration/status. |
| `dev/legacy/dev/CHANGELOG.md` | - Added recovery-loop timing fields `RECOVERY_CYCLE_DURATION` and `MAX_LOOP_DURATION` to `run_complete` logs. |
| `dev/legacy/dev/CHANGELOG.md` | - Changed the ID 8 self-healer policy: when Kuma reports heartbeat timeout but `os-observer-autofix-agent.service` is loaded, active and running, the agent sends a heartbeat refresh and does not restart itself. |
| `dev/legacy/dev/CHANGELOG.md` | - Added `os_observer_autofix_agent.py --doctor` and extended status output with heartbeat age, next expected heartbeat, and independent-heartbeat state. |
| `dev/legacy/dev/CHANGELOG.md` | ## v15 prompt #944 |
| `dev/legacy/dev/CHANGELOG.md` | - Added reboot/login resilience bootstrap: `os-observer-startup-bootstrap.service` runs at user `default.target`, enables the required user timers/services, starts the autofix daemon and both Kuma pushers, and sends initial `BOOTIN |
| `dev/legacy/dev/CHANGELOG.md` | - Added startup state machine fields `BOOTING`, `WARMING_UP`, `HEALTHY`, `RECOVERING` with `OS_OBSERVER_BOOT_GRACE_SECONDS` and `OS_OBSERVER_HEARTBEAT_STARTUP_DELAY_SECONDS`. |

ROADMAP
active/deferred/risky:
| source | fact |
|---|---|
| `dev/legacy/README.md` | python3 ./codex_freeze_runner.py run-next |
| `dev/legacy/README.md` | v19 mantiene la protezione `contain -> throttle -> degrade gracefully` e rende la queue self-healing: `run-next` esegue reconciliation dei job `running` all'avvio, persiste unit/PID/cgroup/heartbeat in SQLite, aggiorna `last_seen` durante |
| `dev/legacy/README.md` | python3 ./codex_freeze_runner.py run-next --debug-run-next --trace-admission --trace-systemd --trace-queue |
| `dev/legacy/README.md` | python3 ./codex_freeze_runner.py current-phase |
| `dev/legacy/ARCHITECTURE.md` | La queue locale e SQLite e vive in `/home/daniele/os_observer/codex-runner/queue/jobs.sqlite`. `enqueue`, `list`, `run-next`, `cancel`, `retry`, `pause`, `resume` serializzano workload e passano sempre da admission control prima del |
| `dev/legacy/dev/TEST_PLAN.md` | - Queue persistence and dry-run/deferred scheduling. |
| `dev/legacy/dev/CHANGELOG.md` | - Added local SQLite job queue with `enqueue`, `list`, `run-next`, `cancel`, `retry`, `pause`, `resume`. |
| `dev/legacy/dev/CHANGELOG.md` | - Added `os_observer_autofix_agent.py --doctor` and extended status output with heartbeat age, next expected heartbeat, and independent-heartbeat state. |
| `dev/legacy/dev/CHANGELOG.md` | - During boot grace, known push-monitor heartbeat gaps are deferred instead of recorded as recovery attempts, avoiding false-positive Kuma alert churn while the local pusher services come up. |
| `dev/legacy/dev/CHANGELOG.md` | - Changed local home-backup heartbeat cadence from 300s to 45s for future backup runs, matching Kuma's 60s push interval. |
| `dev/legacy/dev/CHANGELOG.md` | - Added high-priority `DEST I/O error durante transfer rsync` alert when DEST transport errors and the validated transfer rsync coexist. |
| `dev/legacy/dev/CHANGELOG.md` | - Telegram and Kuma are triggered immediately for blocked or human-review high-priority incidents, not only for successful autofix actions. |
| `dev/legacy/dev/CHANGELOG.md` | - Autofix prioritizes emergency transfer alerts ahead of low-priority backlog when `OS_OBSERVER_AUTOFIX_MAX_EVENTS_PER_RUN` is small. |
| `dev/legacy/OPERATIONS.md` | "SELECT ts,priority,substr(message,1,240) FROM kernel_events WHERE usefulness_score>=95 ORDER BY id DESC LIMIT 80;" |
| `dev/legacy/OPERATIONS.md` | python3 ./codex_freeze_runner.py run-next |
| `dev/legacy/OPERATIONS.md` | python3 ./codex_freeze_runner.py run-next --debug-run-next --trace-admission --trace-systemd --trace-queue |
| `dev/legacy/OPERATIONS.md` | `status --capabilities` mostra controller cgroups v2, proprieta systemd supportate/non supportate, preset effettivo e CPU riservate al sistema. `run-next` non forza Gradle/Codex sotto pressione critica: aggiorna il job a `deferred` co |
| `dev/legacy/RETENTION_POLICY.md` | Le modifiche future a knowledge devono essere patch SQL incrementali applicate con `--apply-patch`, non DB completi sostitutivi. Se una patch cambia retention deve documentare `usefulness_score`, `importance_score`, `keep_reason |
| `codex_freeze_runner.py` | PHASE_DEFERRED = "deferred" |
| `codex_freeze_runner.py` | phase TEXT NOT NULL DEFAULT 'queued', |

LEGACY_SUMMARY
- legacy_docs_read_count: 38
- legacy_docs_read:
- `dev/README.md`
- `dev/legacy/README.md`
- `dev/legacy/dev/INDEX.md`
- `dev/legacy/ARCHITECTURE.md`
- `dev/legacy/dev/ARCHITECTURE.md`
- `dev/legacy/dev/AGENT_RULES.md`
- `dev/legacy/PATCH_WORKFLOW.md`
- `dev/legacy/dev/TEST_PLAN.md`
- `dev/legacy/TROUBLESHOOTING.md`
- `dev/legacy/dev/CHANGELOG.md`
- `dev/legacy/OPERATIONS.md`
- `dev/legacy/AGENTS.md`
- `dev/legacy/RETENTION_POLICY.md`
- `dev/legacy/dev/AUTOFIX_ALLOWLIST.md`
- `dev/legacy/dev/BOOT_SEQUENCE.md`
- `dev/legacy/dev/FALSE_POSITIVE_STRATEGY.md`
- `dev/legacy/dev/MONITOR_MAPPING.md`
- `dev/legacy/dev/RECOVERY_POLICY.md`
- `dev/legacy/dev/ROLLBACK.md`
- `dev/legacy/dev/SAFETY.md`
- `dev/legacy/dev/SQLITE_SCHEMA_NOTES.md`
- `dev/legacy/docs/prompt_731_seagate_usb_diagnosis.md`
- `dev/legacy/docs/prompt_734_seagate_recovery_report.md`
- `dev/legacy/docs/prompt_735_recovery_and_v7_report.md`
- `dev/legacy/docs/registro_soluzioni.md`
- `dev/legacy/dev/ai-diagnostics/SCHEMA.md`
- `codex_freeze_runner.py`
- `kuma_auto_healer.py`
- `os_observer.sh`
- `os_observer_ai_diagnostics.py`
- `os_observer_autofix_agent.py`
- `os_observer_autofix_dashboard.sh`
- `os_observer_cleanup.sh`
- `os_observer_dashboard.sh`
- `os_observer_export.sh`
- `os_observer_memory.sh`
- `tests/test_autofix_agent.py`
- `tests/test_codex_freeze_runner.py`
- extracted: purpose, stack, commands, invariants, bugs, roadmap, changelog, code map.
- historical_only: original local docs in `dev/legacy`; use only when AI doc lacks detail or for audit history.

LINKS
- metadata: [dev/project.metadata.json](../../../os-observer/dev/project.metadata.json)
- human_overview: [human overview](../../human/projects/os-observer/overview.md)
- human_folder: [human folder](../../human/projects/os-observer)
- legacy_docs: [dev/legacy](../../../os-observer/dev/legacy)
- repo_path: [repo](../../../os-observer)

OPEN_QUESTIONS
- dev/legacy/dev/CHANGELOG.md: - Added dry-run tests for fresh telemetry, stale telemetry, fresh knowledge with stale telemetry, stale main DB with fresh WAL, missing DB, locked DB, and permission denied.
- dev/legacy/dev/MONITOR_MAPPING.md: Con auth disponibile, v16 usa `heartbeatList`: `status=0`, heartbeat stale o messaggi di timeout attivano la recovery mappata; per ID 8 la recovery distingue processo vivo da servizio morto.
- dev/legacy/docs/prompt_735_recovery_and_v7_report.md: - Finestra post-recovery: nessun nuovo `reset`, `DID_ERROR`, `I/O error`, `Buffer I/O error` osservato durante open/mount/read superficiale.
