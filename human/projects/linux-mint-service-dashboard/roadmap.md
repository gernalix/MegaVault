# linux-mint-service-dashboard Roadmap

## Segnali dal codice
- app/server.py:2:from __future__ import annotations
- app/collectors.py:1:from __future__ import annotations
- app/collectors.py:238:"NextElapseUSecRealtime",
- app/collectors.py:276:def timer_next_from_list(timer_unit: str / None, scope: str) -> str:
- app/collectors.py:304:def timer_next(timer: dict[str, str] / None) -> str:
- app/collectors.py:309:return timer.get("NextElapseUSecRealtime") or timer_next_from_list(timer.get("unit"), timer.get("scope", "system"))
- app/collectors.py:745:last_run = next((item for item in reversed(json_events) if item.get("message") == "run_complete"), {})
- app/static/app.js:201:next_run: timer.NextElapseUSecRealtime // metrics.next_run // "non disponibile: timer senza prossima run esposta",
- tests/test_dashboard.py:1:from __future__ import annotations
- tests/test_dashboard.py:86:service = next(service for service in data["services"] if service["id"] == "dashboard")

## Debito/rischi da considerare
- app/server.py:53:except Exception as exc: # pragma: no cover - defensive server boundary
- app/server.py:56:"status": "error",
- app/server.py:57:"error": redact_text(str(exc)),
- app/server.py:62:HTTPStatus.INTERNAL_SERVER_ERROR,
- app/collectors.py:10:import urllib.error
- app/collectors.py:36:NO_RECENT_ERROR = "nessun errore recente"
- app/collectors.py:44:r"error/failed/fail/warning/warn/critical/blocked/stalled/corrupt/I/O/input/output/timeout/degraded/"
- app/collectors.py:71:except OSError:
- app/server.py:9:import traceback
- app/server.py:58:"trace": redact_text(traceback.format_exc(limit=3)),
- app/server.py:86:relative = path.removeprefix("/static/")
- app/collectors.py:24:SECRET_PATTERNS = [
- app/collectors.py:26:re.compile(r"((?:token/secret/password/passwd/api[_-]?key/key/restic_password/b2_account_key/aws_secret_access_key/kuma_push_url)\s*[=:]\s*)[^\s\"']+", re.I),
- app/collectors.py:44:r"error/failed/fail/warning/warn/critical/blocked/stalled/corrupt/I/O/input/output/timeout/degraded/"
