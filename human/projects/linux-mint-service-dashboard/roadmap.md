# linux-mint-service-dashboard Roadmap

Roadmap items are extracted from legacy roadmap, changelog, TODO, operations, and troubleshooting material. Dates are only included when they were present in source text.

## Active Or Near-Term Work
| source | fact |
|---|---|
| `dev/legacy/dev/neodocs/METRICS.neodoc` | mint_home_backup=status,phase,snapshot,latest_snapshot,retention,seed_critical,transferred_bytes,snapshot_size,throughput,eta,guardrail,skip_reason,last_success,last_error |
| `app/collectors.py` | "summary": f"{status_json.get('status', 'unknown')} {status_json.get('phase', '')}".strip(), |
| `app/collectors.py` | "phase": status_json.get("phase", NOT_AVAILABLE_SOURCE), |
| `app/collectors.py` | last_run = next((item for item in reversed(json_events) if item.get("message") == "run_complete"), {}) |
| `app/collectors.py` | last_event = next((item for item in reversed(json_events) if item.get("message") == "event_processed"), {}) |
| `tests/test_dashboard.py` | service = next(service for service in data["services"] if service["id"] == "dashboard") |

## Deferred Or Risky Work
- dev/legacy/README.md: - `os-observer-autofix`: ultimo evento, stato Kuma/watchdog, telemetry health, freeze risk, fix_attempts e incidenti recenti.
- dev/legacy/dev/neodocs/UI.neodoc: colors=ok:green,warning:yellow,error:red,unknown:gray
- app/collectors.py: r"error/failed/fail/warning/warn/critical/blocked/stalled/corrupt/I/O/input/output/timeout/degraded/"
- app/collectors.py: if re.search(r"BLOCKED/ERROR/FAILED/WARNING/CRITICAL/PRE_EMERGENCY", classification, re.I):
- app/collectors.py: data["error"] = result.out
- app/collectors.py: data = fetch_json_url("http://127.0.0.1:8765/api/status", timeout=2.5)
- app/collectors.py: if health.get("status") in ("ERROR", "CRITICAL") or data.get("backup_state") == "error":
- app/collectors.py: counts = {"ok": 0, "warning": 0, "error": 0, "unknown": 0}
- dev/legacy/docs/OPERATIONS_HUMAN.md: Se lo script non esiste, usare il controllo Playwright ad hoc documentato nel changelog del prompt #392 o verificare manualmente ogni tab.

## Practical Priority
- First preserve the invariants listed in the AI doc.
- Then resolve active bugs/regressions from troubleshooting evidence.
- Only then expand features or release workflows.
