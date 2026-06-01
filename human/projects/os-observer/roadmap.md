# os-observer Roadmap

Roadmap items are extracted from legacy roadmap, changelog, TODO, operations, and troubleshooting material. Dates are only included when they were present in source text.

## Active Or Near-Term Work
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

## Deferred Or Risky Work
- dev/legacy/README.md: - Entra in protezione quando load/PSI e stallo observer indicano freeze-risk: salva snapshot minimo, salta diagnostici invasivi e rinvia retention/VACUUM.
- dev/legacy/README.md: Il timer esegue `os_observer.sh --once` ogni minuto con `flock`, `timeout` systemd e diagnostici bounded. Se `load1`, PSI I/O/memory o `OBSERVER_STALLED` superano soglia, il run registra `FREEZE_RISK_PROTECTION_MODE`, raccoglie solo dati 
- dev/legacy/README.md: La guardia locale freeze-risk non dipende dal watcher Kuma: se vede load/PSI alto insieme a observer stalled, registra `FREEZE_RISK_LOCAL_PROTECTION` in `knowledge.sqlite`; in apply mode ferma o declassa diagnostici propri e declassa proc
- dev/legacy/dev/INDEX.md: - Freeze-risk guard: se load/PSI cresce e l'observer risulta stalled, registra `FREEZE_RISK_LOCAL_PROTECTION` in `knowledge.sqlite`; in dry-run non agisce, in apply mode tocca solo diagnostici propri (`os-observer.service`, `journalctl
- dev/legacy/dev/INDEX.md: - Il recorder principale usa shedding diagnostico sotto freeze-risk: snapshot minimo, dedup/fingerprint, output bounded, retention/VACUUM rinviati finche load/PSI restano alti.
- dev/legacy/ARCHITECTURE.md: Il collector legge `journalctl -k` con lookback limitato e filtra keyword diagnostiche: freeze, PRE_EMERGENCY, EMERGENCY, CRITICAL, I/O, DID_ERROR, xhci, usb, reset, disconnect, ext4, oom, killed, hung, blocked, rsync, failed, timeo
- dev/legacy/dev/ARCHITECTURE.md: - `os_observer_autofix_agent.py`: correlazione, dedup, fix allowlist, watcher Uptime Kuma dashboard #8, freeze-risk guard locale e heartbeat Kuma indipendente dal ciclo recovery.
- dev/legacy/dev/ARCHITECTURE.md: - Sotto freeze-risk, `os_observer.sh` registra lo stato e fa shedding: evita diagnostici invasivi ripetuti, limita output/tail, rinvia retention e non lancia VACUUM.
- dev/legacy/dev/ARCHITECTURE.md: - La protezione freeze-risk puo agire solo su diagnostici propri e conserva `rsync_touched=0`; data mover e backup restano fuori dall'autofix locale.
- dev/legacy/dev/TEST_PLAN.md: - Freeze-risk guard with high load/I/O and RAM/swap OK records dry-run protection.
- dev/legacy/dev/CHANGELOG.md: - During boot grace, known push-monitor heartbeat gaps are deferred instead of recorded as recovery attempts, avoiding false-positive Kuma alert churn while the local pusher services come up.
- dev/legacy/dev/CHANGELOG.md: - Added load/PSI based freeze-risk protection. `os_observer.sh` now emits `FREEZE_RISK_PROTECTION_MODE` when load, PSI I/O/memory, or observer-stall thresholds trip; in that mode it skips invasive diagnostics, bounds tails more agg

## Practical Priority
- First preserve the invariants listed in the AI doc.
- Then resolve active bugs/regressions from troubleshooting evidence.
- Only then expand features or release workflows.
