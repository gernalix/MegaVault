# linux-mint-service-dashboard Troubleshooting

## Problemi e sintomi rilevati nel codice
- app/server.py:53:except Exception as exc: # pragma: no cover - defensive server boundary
- app/server.py:56:"status": "error",
- app/server.py:57:"error": redact_text(str(exc)),
- app/server.py:62:HTTPStatus.INTERNAL_SERVER_ERROR,
- app/collectors.py:10:import urllib.error
- app/collectors.py:36:NO_RECENT_ERROR = "nessun errore recente"
- app/collectors.py:44:r"error/failed/fail/warning/warn/critical/blocked/stalled/corrupt/I/O/input/output/timeout/degraded/"
- app/collectors.py:71:except OSError:
- app/collectors.py:98:def run(args: list[str], timeout: float = 2.0) -> CommandResult:
- app/collectors.py:100:proc = subprocess.run(args, text=True, capture_output=True, timeout=timeout, check=False)
- app/collectors.py:102:except (OSError, subprocess.TimeoutExpired) as exc:
- app/collectors.py:111:except (OSError, json.JSONDecodeError):
- systemd/system-service-dashboard.service:10:Restart=on-failure
- app/static/app.js:10:error: "ERROR",
- app/static/app.js:28:return ["ok", "warning", "error", "unknown"].includes(status) ? status : "unknown";
- app/static/app.js:49:statCard("Errori", counts.error ?? 0, "error"),
- app/static/app.js:106:${section("Warning / errori", lineList(service.warnings // [], "warn"))}
- app/static/app.js:217:if (!response.ok) throw new Error(`HTTP ${response.status}`);

## Comandi/verifiche utili trovati
- UNKNOWN: nessun comando rilevato in build/script/CI.

## Safety prima di correggere
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
