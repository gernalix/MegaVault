# linux-mint-service-dashboard AI OPERATIONS

PROJECT
- name: linux-mint-service-dashboard
- slug: linux-mint-service-dashboard
- purpose: Dashboard locale read-only per i servizi operativi importanti di questo host Linux Mint/XFCE.
- current_status: Working tree has 11 non-clean entries; do not mix unrelated changes. First entries: M VERSION, M app/collectors.py, M app/static/app.js, M tests/test_dashboard.py, ?? .codexmeta
- repo_path: `/home/daniele/codex-workspace/linux-mint-service-dashboard`
- remote: `none`
- branch: `prompt-816-local-dashboard`
- last_verified_commit/date: `487ca7e` / `2026-06-01T13:20:29+02:00`

STACK
- languages: JavaScript/TypeScript, Python
- frameworks: UNKNOWN
- DB: UNKNOWN
- platform: UNKNOWN
- external_tools/services: systemd

CODE_MAP
entrypoints:
- `app/server.py`
important_folders:
- `app`
- `dev`
- `launchers`
- `scripts`
- `systemd`
- `tests`
important_files:
- `dev/README.md`
tests:
- `tests/playwright-smoke.js`
- `tests/test_dashboard.py`
scripts:
- `app/__init__.py`
- `app/collectors.py`
- `app/server.py`
- `scripts/dashboard-healthcheck`
- `scripts/dashboardctl`
- `scripts/open-dashboard`
- `tests/test_dashboard.py`
generated/runtime/avoid_touch_casually:
- `dev/legacy`

ARCH
summary:
- dev/legacy/README.md: Dashboard locale read-only per i servizi operativi importanti di questo host Linux Mint/XFCE.
- dev/legacy/dev/neodocs/CHANGELOG.neodoc: 1=initial_structure_neodocs_rules_readme
- dev/legacy/dev/neodocs/INDEX.neodoc: project=linux-mint-service-dashboard
- dev/legacy/dev/neodocs/METRICS.neodoc: common=service_state,timer_state,next_run,last_trigger,last_result,pid,log_tail,path_log,last_success,last_error,data_age,recent_events
- dev/legacy/dev/neodocs/PROJECT.neodoc: name=linux-mint-service-dashboard
- dev/legacy/dev/neodocs/SERVICES.neodoc: required=amici_fb,cloud-backup,disk-usage-monitor,mint-heartbeat,mint-home-backup,mint-home-backup-retention,os-observer-autofix,parcel-tracker,rsync-transfer
- dev/legacy/dev/neodocs/SYSTEMD.neodoc: user_service=system-service-dashboard.service
- dev/legacy/dev/neodocs/TESTS.neodoc: commands=python3 -m unittest discover -s tests/python3 -m py_compile app/server.py app/collectors.py/node tests/playwright-smoke.js/./scripts/dashboardctl status/./scripts/dashboardctl healthcheck
- dev/legacy/dev/neodocs/UI.neodoc: footer=Ultimo refresh automatico: YYYY-MM-DD HH:MM:SS
- dev/legacy/docs/ARCHITECTURE_HUMAN.md: La dashboard espone un server HTTP locale Python su `127.0.0.1:8788`.
components/dataflow/design_decisions:
| source | fact |
|---|---|
| `dev/legacy/README.md` | # Linux Mint Service Dashboard |
| `dev/legacy/README.md` | ## Avvio |
| `dev/legacy/README.md` | ## Sicurezza |
| `dev/legacy/README.md` | ## Tab principali |
| `dev/legacy/README.md` | ## Dati non disponibili |
| `dev/legacy/docs/ARCHITECTURE_HUMAN.md` | # Architecture |
| `dev/legacy/docs/ARCHITECTURE_HUMAN.md` | ## Collector |
| `dev/legacy/docs/ARCHITECTURE_HUMAN.md` | ## Availability Labels |
| `dev/legacy/dev/AGENT_RULES.md` | # Agent Rules |
| `dev/legacy/docs/OPERATIONS_HUMAN.md` | # Operations |
| `app/server.py` | #!/usr/bin/env python3 |
| `dev/legacy/README.md` | Dashboard locale read-only per i servizi operativi importanti di questo host Linux Mint/XFCE. |
| `dev/legacy/dev/neodocs/CHANGELOG.neodoc` | 1=initial_structure_neodocs_rules_readme |
| `dev/legacy/dev/neodocs/INDEX.neodoc` | project=linux-mint-service-dashboard |
| `dev/legacy/dev/neodocs/METRICS.neodoc` | common=service_state,timer_state,next_run,last_trigger,last_result,pid,log_tail,path_log,last_success,last_error,data_age,recent_events |
| `dev/legacy/dev/neodocs/PROJECT.neodoc` | name=linux-mint-service-dashboard |
| `dev/legacy/dev/neodocs/SERVICES.neodoc` | required=amici_fb,cloud-backup,disk-usage-monitor,mint-heartbeat,mint-home-backup,mint-home-backup-retention,os-observer-autofix,parcel-tracker,rsync-transfer |
| `dev/legacy/dev/neodocs/SYSTEMD.neodoc` | user_service=system-service-dashboard.service |

INVARIANTS
architecture/data/UX/safety/versioning/localization:
| source | fact |
|---|---|
| `dev/legacy/README.md` | Dashboard locale read-only per i servizi operativi importanti di questo host Linux Mint/XFCE. |
| `dev/legacy/README.md` | La dashboard legge stato da systemd, file JSON/env/log già esistenti e endpoint locali. Non riavvia i servizi monitorati, non cancella file e maschera token, password, chiavi e URL Kuma completi. |
| `dev/legacy/README.md` | - `rsync-transfer`: label stato (`in esecuzione`, `completato`, `idle`, `non configurato`, `fallito`), processo, lock, mount source/dest, byte totali/fatti/rimanenti, percentuale, throughput da progress log, ETA, stale metrics, log e warn |
| `dev/legacy/README.md` | - `mint-home-backup`: stato snapshot, fase, retention, seed-critical, guardrail, spazio libero, eventi systemd. |
| `dev/legacy/README.md` | - `cloud backup`: stato restic dal dashboard locale esistente, snapshot, lock, throughput, ETA e timer. |
| `dev/legacy/README.md` | - job/timer: `amici_fb`, `parcel-tracker`, `disk-usage-monitor`, `mint-heartbeat`, `mint-home-backup-retention`. |
| `dev/legacy/README.md` | ## Dati non disponibili |
| `dev/legacy/README.md` | - Le metriche non calcolabili mostrano una spiegazione `non disponibile: ...` invece di un `n/d` generico. |
| `dev/legacy/README.md` | - `rsync-transfer` non mostra una media globale quando il log non espone una base temporale affidabile. |
| `dev/legacy/README.md` | - `rsync-transfer` marca `metrics_stale` quando restano dati vecchi da log/cache ma non esiste un processo rsync vivo; in quel caso non calcola un `completion_time` futuro da throughput residuo. |
| `dev/legacy/README.md` | - `mint-home-backup` non mostra ETA quando il sorgente non lo espone in modo affidabile. |
| `dev/legacy/README.md` | - `cloud backup` non legge direttamente file root-only: usa l'endpoint locale sanificato e spiega i campi non esposti. |
| `dev/legacy/README.md` | - Il cloud backup viene letto tramite `http://127.0.0.1:8765/api/status`; se quel servizio è down, la tab degrada ai soli dati systemd. |
| `dev/legacy/README.md` | - La dashboard non usa privilegi root e non legge direttamente file root-only quando esiste un endpoint locale già sanificato. |
| `dev/legacy/dev/neodocs/CHANGELOG.neodoc` | version=10 |
| `dev/legacy/dev/neodocs/INDEX.neodoc` | version=10 |
| `dev/legacy/dev/neodocs/INDEX.neodoc` | version_file=VERSION |
| `dev/legacy/dev/neodocs/INDEX.neodoc` | update_rule=increment VERSION and neodocs on every patch |
| `dev/legacy/dev/neodocs/METRICS.neodoc` | version=10 |
| `dev/legacy/dev/neodocs/METRICS.neodoc` | dashboard_self=version,uptime,systemd_state,autostart,last_api_refresh,api_status_response,backend_recent_errors,health_status |
| `dev/legacy/dev/neodocs/PROJECT.neodoc` | version=10 |
| `dev/legacy/dev/neodocs/PROJECT.neodoc` | version_file=VERSION |
| `dev/legacy/dev/neodocs/SERVICES.neodoc` | version=10 |
| `dev/legacy/dev/neodocs/SERVICES.neodoc` | required=amici_fb,cloud-backup,disk-usage-monitor,mint-heartbeat,mint-home-backup,mint-home-backup-retention,os-observer-autofix,parcel-tracker,rsync-transfer |
| `dev/legacy/dev/neodocs/SERVICES.neodoc` | user_units=amici_fb.service,amici_fb.timer,home-incremental-backup.service,home-incremental-backup.timer,home-backup-retention-kuma-push.service,home-backup-retention-kuma-push.timer,os-observer-autofix-agent.service,os- |
| `dev/legacy/dev/neodocs/SERVICES.neodoc` | system_units=mint-cloud-backup.service,mint-cloud-backup.timer,mint-cloud-backup-monitor.service,mint-cloud-backup-dashboard.service,mint-cloud-backup-kuma-push.service,mint-cloud-backup-kuma-push.timer,disk-usage-monito |

BUILD_TEST
build_files:
- UNKNOWN
commands_found:
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
test_targets:
- `tests/playwright-smoke.js`
- `tests/test_dashboard.py`
known_test_flakiness_or_requirements:
- dev/legacy/README.md: - `os-observer-autofix`: ultimo evento, stato Kuma/watchdog, telemetry health, freeze risk, fix_attempts e incidenti recenti.
- dev/legacy/docs/ARCHITECTURE_HUMAN.md: Ogni comando esterno è limitato da timeout. I log sono letti dal fondo con byte limit.
- app/collectors.py: r"error/failed/fail/warning/warn/critical/blocked/stalled/corrupt/I/O/input/output/timeout/degraded/"
- app/collectors.py: def run(args: list[str], timeout: float = 2.0) -> CommandResult:
- app/collectors.py: proc = subprocess.run(args, text=True, capture_output=True, timeout=timeout, check=False)
- app/collectors.py: result = run(cmd, timeout=2.0)
- app/collectors.py: result = run(cmd, timeout=2.5)
- app/collectors.py: result = run([*base, "list-timers", "--all", "--no-legend", "--no-pager"], timeout=2.5)
- app/collectors.py: result = run(["date", "-d", value, "+%s"], timeout=1.0)
- app/collectors.py: result = run(["findmnt", "-T", path, "--json", "-o", "TARGET,SOURCE,FSTYPE,OPTIONS"], timeout=1.8)

VERSIONING_RELEASE
rules/artifacts/commit_push/release_blockers:
| source | fact |
|---|---|
| `dev/legacy/dev/neodocs/CHANGELOG.neodoc` | version=10 |
| `dev/legacy/dev/neodocs/INDEX.neodoc` | version=10 |
| `dev/legacy/dev/neodocs/INDEX.neodoc` | version_file=VERSION |
| `dev/legacy/dev/neodocs/INDEX.neodoc` | update_rule=increment VERSION and neodocs on every patch |
| `dev/legacy/dev/neodocs/METRICS.neodoc` | version=10 |
| `dev/legacy/dev/neodocs/METRICS.neodoc` | dashboard_self=version,uptime,systemd_state,autostart,last_api_refresh,api_status_response,backend_recent_errors,health_status |
| `dev/legacy/dev/neodocs/PROJECT.neodoc` | version=10 |
| `dev/legacy/dev/neodocs/PROJECT.neodoc` | version_file=VERSION |
| `dev/legacy/dev/neodocs/SERVICES.neodoc` | version=10 |
| `dev/legacy/dev/neodocs/SERVICES.neodoc` | user_units=amici_fb.service,amici_fb.timer,home-incremental-backup.service,home-incremental-backup.timer,home-backup-retention-kuma-push.service,home-backup-retention-kuma-push.timer,os-observer-autofix-agent.service,os- |
| `dev/legacy/dev/neodocs/SERVICES.neodoc` | system_units=mint-cloud-backup.service,mint-cloud-backup.timer,mint-cloud-backup-monitor.service,mint-cloud-backup-dashboard.service,mint-cloud-backup-kuma-push.service,mint-cloud-backup-kuma-push.timer,disk-usage-monito |
| `dev/legacy/dev/neodocs/SYSTEMD.neodoc` | version=10 |
| `dev/legacy/dev/neodocs/TESTS.neodoc` | version=10 |
| `dev/legacy/dev/neodocs/UI.neodoc` | version=10 |
| `dev/legacy/dev/AGENT_RULES.md` | - Incrementare `VERSION` con versione intera monotona a ogni patch. |
| `dev/legacy/docs/OPERATIONS_HUMAN.md` | Se lo script non esiste, usare il controllo Playwright ad hoc documentato nel changelog del prompt #392 o verificare manualmente ogni tab. |
| `app/collectors.py` | VERSION_FILE = PROJECT_ROOT / "VERSION" |
| `app/collectors.py` | re.compile(r"(https?://[^\s\"']*/api/push/)[^\s\"'&?]+", re.I), |
| `app/collectors.py` | def version() -> str: |
| `app/collectors.py` | "summary": f"v{version()} {service_summary(service)}", |

DATA_STORAGE
DB_paths/backup/import/export/migration/retention/user_data_safety:
| source | fact |
|---|---|
| `dev/legacy/README.md` | Dashboard locale read-only per i servizi operativi importanti di questo host Linux Mint/XFCE. |
| `dev/legacy/README.md` | La dashboard legge stato da systemd, file JSON/env/log già esistenti e endpoint locali. Non riavvia i servizi monitorati, non cancella file e maschera token, password, chiavi e URL Kuma completi. |
| `dev/legacy/README.md` | - `rsync-transfer`: label stato (`in esecuzione`, `completato`, `idle`, `non configurato`, `fallito`), processo, lock, mount source/dest, byte totali/fatti/rimanenti, percentuale, throughput da progress log, ETA, stale metrics, log e warn |
| `dev/legacy/README.md` | - `mint-home-backup`: stato snapshot, fase, retention, seed-critical, guardrail, spazio libero, eventi systemd. |
| `dev/legacy/README.md` | - `cloud backup`: stato restic dal dashboard locale esistente, snapshot, lock, throughput, ETA e timer. |
| `dev/legacy/README.md` | - job/timer: `amici_fb`, `parcel-tracker`, `disk-usage-monitor`, `mint-heartbeat`, `mint-home-backup-retention`. |
| `dev/legacy/README.md` | - `rsync-transfer` non mostra una media globale quando il log non espone una base temporale affidabile. |
| `dev/legacy/README.md` | - `rsync-transfer` marca `metrics_stale` quando restano dati vecchi da log/cache ma non esiste un processo rsync vivo; in quel caso non calcola un `completion_time` futuro da throughput residuo. |
| `dev/legacy/README.md` | - `mint-home-backup` non mostra ETA quando il sorgente non lo espone in modo affidabile. |
| `dev/legacy/README.md` | - `cloud backup` non legge direttamente file root-only: usa l'endpoint locale sanificato e spiega i campi non esposti. |
| `dev/legacy/README.md` | - Il cloud backup viene letto tramite `http://127.0.0.1:8765/api/status`; se quel servizio è down, la tab degrada ai soli dati systemd. |
| `dev/legacy/dev/neodocs/CHANGELOG.neodoc` | version=10 |
| `dev/legacy/dev/neodocs/METRICS.neodoc` | dashboard_self=version,uptime,systemd_state,autostart,last_api_refresh,api_status_response,backend_recent_errors,health_status |
| `dev/legacy/dev/neodocs/SERVICES.neodoc` | required=amici_fb,cloud-backup,disk-usage-monitor,mint-heartbeat,mint-home-backup,mint-home-backup-retention,os-observer-autofix,parcel-tracker,rsync-transfer |
| `dev/legacy/dev/neodocs/SERVICES.neodoc` | user_units=amici_fb.service,amici_fb.timer,home-incremental-backup.service,home-incremental-backup.timer,home-backup-retention-kuma-push.service,home-backup-retention-kuma-push.timer,os-observer-autofix-agent.service,os- |
| `dev/legacy/dev/neodocs/SERVICES.neodoc` | system_units=mint-cloud-backup.service,mint-cloud-backup.timer,mint-cloud-backup-monitor.service,mint-cloud-backup-dashboard.service,mint-cloud-backup-kuma-push.service,mint-cloud-backup-kuma-push.timer,disk-usage-monito |
| `dev/legacy/dev/neodocs/SERVICES.neodoc` | implemented_tabs=overview,dashboard,rsync-transfer,mint-home-backup,cloud-backup,os-observer-autofix,amici_fb,parcel-tracker,disk-usage-monitor,mint-heartbeat,mint-home-backup-retention |
| `dev/legacy/docs/ARCHITECTURE_HUMAN.md` | - endpoint locale già esistente del cloud backup; |
| `dev/legacy/docs/ARCHITECTURE_HUMAN.md` | - query SQLite read-only per os-observer quando disponibili. |
| `dev/legacy/docs/ARCHITECTURE_HUMAN.md` | - `collect_rsync_transfer`: legge `transfer_vecchio_disco_phase2_status.env`, cache total/dest, log progress2, lock, mount e watchdog USB/I/O; distingue run attiva, completata, idle, non configurata, fallita e metriche st |
| `dev/legacy/docs/ARCHITECTURE_HUMAN.md` | - `collect_home_backup`: legge `~/.local/state/home-backup/*.json` e stato retention/seed. |
| `dev/legacy/docs/ARCHITECTURE_HUMAN.md` | - `collect_cloud_backup`: usa `http://127.0.0.1:8765/api/status` per evitare letture root-only non necessarie. |

KNOWN_BUGS
active/historical/root_causes/regression_checklist:
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

DO_NOT_BREAK
- Preserve `dev/project.metadata.json` -> this AI doc -> Human docs workflow.
- Preserve `dev/legacy/`; do not delete or rewrite historical docs without explicit migration intent.
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
- dev/legacy/dev/neodocs/PROJECT.neodoc: version_file=VERSION
- dev/legacy/dev/neodocs/SERVICES.neodoc: version=10
- dev/legacy/dev/neodocs/SERVICES.neodoc: required=amici_fb,cloud-backup,disk-usage-monitor,mint-heartbeat,mint-home-backup,mint-home-backup-retention,os-observer-autofix,parcel-tracker,rsync-transfer

RECENT_DECISIONS
| source | fact |
|---|---|
| `dev/legacy/dev/neodocs/CHANGELOG.neodoc` | 1=initial_structure_neodocs_rules_readme |
| `dev/legacy/dev/neodocs/CHANGELOG.neodoc` | 2=backend_collectors_systemd_logs_json_sqlite_rsync_home_cloud_osobserver |
| `dev/legacy/dev/neodocs/CHANGELOG.neodoc` | 3=http_server_api_health_static_local_bind |
| `dev/legacy/dev/neodocs/CHANGELOG.neodoc` | 4=frontend_overview_tabs_compact_dark_refresh_footer |
| `dev/legacy/dev/neodocs/CHANGELOG.neodoc` | 5=systemd_user_service_launcher_start_stop_status_restart |
| `dev/legacy/dev/neodocs/CHANGELOG.neodoc` | 6=unittest_parser_secret_collectors_http_startup |
| `dev/legacy/dev/neodocs/CHANGELOG.neodoc` | 7=docs_metrics_limits_neodocs_sync |
| `dev/legacy/dev/neodocs/CHANGELOG.neodoc` | 8=prompt392_verify_all_tabs_remove_generic_nd_add_availability_reasons_timer_duration_warning_cause |
| `dev/legacy/dev/neodocs/CHANGELOG.neodoc` | 9=prompt649_enable_autostart_add_dashboard_self_monitoring_healthcheck_desktop_and_terminal_launchers |
| `dev/legacy/dev/neodocs/CHANGELOG.neodoc` | 10=prompt583_rsync_transfer_state_labels_and_stale_metrics |
| `dev/legacy/dev/neodocs/METRICS.neodoc` | mint_home_backup=status,phase,snapshot,latest_snapshot,retention,seed_critical,transferred_bytes,snapshot_size,throughput,eta,guardrail,skip_reason,last_success,last_error |
| `app/collectors.py` | "summary": f"{status_json.get('status', 'unknown')} {status_json.get('phase', '')}".strip(), |
| `app/collectors.py` | "phase": status_json.get("phase", NOT_AVAILABLE_SOURCE), |
| `app/collectors.py` | last_run = next((item for item in reversed(json_events) if item.get("message") == "run_complete"), {}) |
| `app/collectors.py` | last_event = next((item for item in reversed(json_events) if item.get("message") == "event_processed"), {}) |
| `tests/test_dashboard.py` | service = next(service for service in data["services"] if service["id"] == "dashboard") |

ROADMAP
active/deferred/risky:
| source | fact |
|---|---|
| `dev/legacy/dev/neodocs/METRICS.neodoc` | mint_home_backup=status,phase,snapshot,latest_snapshot,retention,seed_critical,transferred_bytes,snapshot_size,throughput,eta,guardrail,skip_reason,last_success,last_error |
| `app/collectors.py` | "summary": f"{status_json.get('status', 'unknown')} {status_json.get('phase', '')}".strip(), |
| `app/collectors.py` | "phase": status_json.get("phase", NOT_AVAILABLE_SOURCE), |
| `app/collectors.py` | last_run = next((item for item in reversed(json_events) if item.get("message") == "run_complete"), {}) |
| `app/collectors.py` | last_event = next((item for item in reversed(json_events) if item.get("message") == "event_processed"), {}) |
| `tests/test_dashboard.py` | service = next(service for service in data["services"] if service["id"] == "dashboard") |

LEGACY_SUMMARY
- legacy_docs_read_count: 18
- legacy_docs_read:
- `dev/README.md`
- `dev/legacy/README.md`
- `dev/legacy/dev/neodocs/CHANGELOG.neodoc`
- `dev/legacy/dev/neodocs/INDEX.neodoc`
- `dev/legacy/dev/neodocs/METRICS.neodoc`
- `dev/legacy/dev/neodocs/PROJECT.neodoc`
- `dev/legacy/dev/neodocs/SERVICES.neodoc`
- `dev/legacy/dev/neodocs/SYSTEMD.neodoc`
- `dev/legacy/dev/neodocs/TESTS.neodoc`
- `dev/legacy/dev/neodocs/UI.neodoc`
- `dev/legacy/docs/ARCHITECTURE_HUMAN.md`
- `dev/legacy/dev/AGENT_RULES.md`
- `dev/legacy/docs/OPERATIONS_HUMAN.md`
- `app/__init__.py`
- `app/collectors.py`
- `app/server.py`
- `tests/test_dashboard.py`
- `tests/playwright-smoke.js`
- extracted: purpose, stack, commands, invariants, bugs, roadmap, changelog, code map.
- historical_only: original local docs in `dev/legacy`; use only when AI doc lacks detail or for audit history.

LINKS
- metadata: [dev/project.metadata.json](../../../linux-mint-service-dashboard/dev/project.metadata.json)
- human_overview: [human overview](../../human/projects/linux-mint-service-dashboard/overview.md)
- human_folder: [human folder](../../human/projects/linux-mint-service-dashboard)
- legacy_docs: [dev/legacy](../../../linux-mint-service-dashboard/dev/legacy)
- repo_path: [repo](../../../linux-mint-service-dashboard)

OPEN_QUESTIONS
- dev/legacy/dev/neodocs/UI.neodoc: colors=ok:green,warning:yellow,error:red,unknown:gray
- app/collectors.py: return {"status": "error", "label": "fallito", "summary": "fallito", "metrics_stale": metrics_stale}
- app/collectors.py: with urllib.request.urlopen(url, timeout=timeout) as response:
- app/collectors.py: counts = {"ok": 0, "warning": 0, "error": 0, "unknown": 0}
- tests/test_dashboard.py: with urllib.request.urlopen(f"http://127.0.0.1:{port}/api/health", timeout=2) as response:
