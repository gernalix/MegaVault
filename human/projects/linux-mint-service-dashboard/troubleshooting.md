# linux-mint-service-dashboard Troubleshooting

Use this page for symptoms and checks. For operational decisions, confirm against the AI doc first.

## Known Problems And Symptoms
| source | fact |
|---|---|
| `dev/legacy/README.md` | - `os-observer-autofix`: ultimo evento, stato Kuma/watchdog, telemetry health, freeze risk, fix_attempts e incidenti recenti. |
| `dev/legacy/dev/neodocs/UI.neodoc` | colors=ok:green,warning:yellow,error:red,unknown:gray |
| `dev/legacy/docs/ARCHITECTURE_HUMAN.md` | Ogni comando esterno è limitato da timeout. I log sono letti dal fondo con byte limit. |
| `app/collectors.py` | import urllib.error |
| `app/collectors.py` | r"error/failed/fail/warning/warn/critical/blocked/stalled/corrupt/I/O/input/output/timeout/degraded/" |
| `app/collectors.py` | def run(args: list[str], timeout: float = 2.0) -> CommandResult: |
| `app/collectors.py` | proc = subprocess.run(args, text=True, capture_output=True, timeout=timeout, check=False) |
| `app/collectors.py` | if level in {"WARNING", "ERROR", "CRITICAL"}: |
| `app/collectors.py` | error = item.get("error") |
| `app/collectors.py` | if error not in (None, "", False): |
| `app/collectors.py` | if re.search(r"BLOCKED/ERROR/FAILED/WARNING/CRITICAL/PRE_EMERGENCY", classification, re.I): |
| `app/collectors.py` | result = run(cmd, timeout=2.0) |
| `app/collectors.py` | data["error"] = result.out |
| `app/collectors.py` | result = run(cmd, timeout=2.5) |
| `app/collectors.py` | result = run([*base, "list-timers", "--all", "--no-legend", "--no-pager"], timeout=2.5) |
| `app/collectors.py` | result = run(["date", "-d", value, "+%s"], timeout=1.0) |
| `app/collectors.py` | return "error" |
| `app/collectors.py` | result = run(["findmnt", "-T", path, "--json", "-o", "TARGET,SOURCE,FSTYPE,OPTIONS"], timeout=1.8) |
| `app/collectors.py` | result = run(["df", "-B1", "--output=source,size,used,avail,pcent,target", path], timeout=1.8) |
| `app/collectors.py` | return {"error": result.out} |
| `app/collectors.py` | return {"status": "error", "label": "fallito", "summary": "fallito", "metrics_stale": metrics_stale} |
| `app/collectors.py` | data = fetch_json_url("http://127.0.0.1:8765/api/status", timeout=2.5) |
| `app/collectors.py` | if health.get("status") in ("ERROR", "CRITICAL") or data.get("backup_state") == "error": |
| `app/collectors.py` | status = "error" |

## Useful Checks Or Commands
| source | fact |
|---|---|
| `dev/legacy/README.md` | systemctl --user start system-service-dashboard.service |
| `dev/legacy/README.md` | systemctl --user enable system-service-dashboard.service |
| `dev/legacy/README.md` | - `rsync-transfer` marca `metrics_stale` quando restano dati vecchi da log/cache ma non esiste un processo rsync vivo; in quel caso non calcola un `completion_time` futuro da throughput residuo. |
| `dev/legacy/docs/ARCHITECTURE_HUMAN.md` | - metriche stale da una run rsync non piu' attiva; |
| `dev/legacy/docs/OPERATIONS_HUMAN.md` | systemctl --user start system-service-dashboard.service |
| `dev/legacy/docs/OPERATIONS_HUMAN.md` | systemctl --user enable system-service-dashboard.service |
| `dev/legacy/docs/OPERATIONS_HUMAN.md` | python3 -m py_compile app/server.py app/collectors.py |
| `dev/legacy/docs/OPERATIONS_HUMAN.md` | python3 -m unittest discover -s tests |
| `app/collectors.py` | import sqlite3 |
| `app/collectors.py` | "average_throughput": "non disponibile: rsync non espone una media globale affidabile", |
| `app/collectors.py` | conn = sqlite3.connect(uri, uri=True, timeout=1.0) |
| `app/collectors.py` | conn.row_factory = sqlite3.Row |
| `app/collectors.py` | except sqlite3.Error: |
| `app/server.py` | #!/usr/bin/env python3 |

## Safety Checks Before Fixing
- dev/legacy/README.md: Dashboard locale read-only per i servizi operativi importanti di questo host Linux Mint/XFCE.
- dev/legacy/README.md: - `mint-home-backup`: stato snapshot, fase, retention, seed-critical, guardrail, spazio libero, eventi systemd.
- dev/legacy/README.md: - `cloud backup`: stato restic dal dashboard locale esistente, snapshot, lock, throughput, ETA e timer.
- dev/legacy/README.md: - job/timer: `amici_fb`, `parcel-tracker`, `disk-usage-monitor`, `mint-heartbeat`, `mint-home-backup-retention`.
- dev/legacy/README.md: - `mint-home-backup` non mostra ETA quando il sorgente non lo espone in modo affidabile.
- dev/legacy/README.md: - `cloud backup` non legge direttamente file root-only: usa l'endpoint locale sanificato e spiega i campi non esposti.
- dev/legacy/README.md: - Il cloud backup viene letto tramite `http://127.0.0.1:8765/api/status`; se quel servizio è down, la tab degrada ai soli dati systemd.
- dev/legacy/dev/neodocs/CHANGELOG.neodoc: version=10
- dev/legacy/dev/neodocs/INDEX.neodoc: version=10
- dev/legacy/dev/neodocs/INDEX.neodoc: version_file=VERSION
- dev/legacy/dev/neodocs/INDEX.neodoc: update_rule=increment VERSION and neodocs on every patch
- dev/legacy/dev/neodocs/METRICS.neodoc: version=10
- dev/legacy/dev/neodocs/METRICS.neodoc: dashboard_self=version,uptime,systemd_state,autostart,last_api_refresh,api_status_response,backend_recent_errors,health_status
- dev/legacy/dev/neodocs/PROJECT.neodoc: version=10
