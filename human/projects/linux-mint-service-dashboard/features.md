# linux-mint-service-dashboard Features

Questa pagina deriva dal codice attivo auditato con `#604927`.

## Mappa funzionale dal codice
- `app/server.py`: DashboardHandler, parse_args, main
- `app/collectors.py`: CommandResult, now_local, iso_now, display_now, version, redact_text, redact, run
- `app/static/app.js`: escapeHtml, statusClass, scalar, renderOverview, statCard, renderTabs, renderPanel, renderOverviewPanel
- `tests/playwright-smoke.js`: URL, VIEWPORTS, browser, errors, page, tabs, info
- `tests/test_dashboard.py`: DashboardTests

## Confini operativi
- app/server.py:9:import traceback
- app/server.py:58:"trace": redact_text(traceback.format_exc(limit=3)),
- app/server.py:86:relative = path.removeprefix("/static/")
- app/collectors.py:24:SECRET_PATTERNS = [
- app/collectors.py:26:re.compile(r"((?:token/secret/password/passwd/api[_-]?key/key/restic_password/b2_account_key/aws_secret_access_key/kuma_push_url)\s*[=:]\s*)[^\s\"']+", re.I),
- app/collectors.py:44:r"error/failed/fail/warning/warn/critical/blocked/stalled/corrupt/I/O/input/output/timeout/degraded/"
- app/collectors.py:45:r"storage/lock/TRUE_PRE_EMERGENCY/PRE_EMERGENCY/abort/skipped",
- app/collectors.py:77:for pattern in SECRET_PATTERNS:
- app/server.py:18:from app.collectors import collect_all, display_now, redact_text, version
- app/server.py:26:server_version = f"LinuxMintServiceDashboard/{version()}"
- app/server.py:60:"version": version(),
- app/server.py:80:self.send_json({"status": "ok", "version": version(), "refresh_display": display_now(), "read_only": True})
