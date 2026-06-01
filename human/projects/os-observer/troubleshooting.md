# os-observer Troubleshooting

Use this page for symptoms and checks. For operational decisions, confirm against the AI doc first.

## Known Problems And Symptoms
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

## Useful Checks Or Commands
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

## Safety Checks Before Fixing
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
- dev/legacy/dev/INDEX.md: - Kuma dashboard watcher: legge `http://150.230.148.128:3001/dashboard/8` via endpoint web + Socket.IO read-only. Se `OS_OBSERVER_KUMA_AUTH_TOKEN_FILE` o `OS_OBSERVER_KUMA_AUTH_TOKEN` contiene un JWT valido usa `loginByToken` e legge `
- dev/legacy/dev/INDEX.md: - Telemetry guard: se `telemetry.sqlite` supera `OS_OBSERVER_TELEMETRY_STALE_SECONDS`, l'agent emette `TELEMETRY_STALE`, tenta checkpoint WAL o restart sicuro di `os-observer.timer`/`os-observer.service`, registra l'intervento in `know
- dev/legacy/dev/INDEX.md: - Freeze-risk guard: se load/PSI cresce e l'observer risulta stalled, registra `FREEZE_RISK_LOCAL_PROTECTION` in `knowledge.sqlite`; in dry-run non agisce, in apply mode tocca solo diagnostici propri (`os-observer.service`, `journalctl
