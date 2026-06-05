META:
name=codex-token-watcher
slug=codex-token-watcher
path=/home/daniele/codex-workspace/codex-token-watcher
vm_path=/home/ubuntu/codex-workspace/codex-usage-monitor
vm_host=ubuntu@150.230.148.128
remote=none
branch=codex/prompt-384921
verified_commit=UNKNOWN
verified_at=2026-06-05T12:36:18+02:00
protocol=MEGAVAULT_PROTOCOL.md:v3
PURPOSE:
purpose=Monitor Codex CLI health/status from Oracle VM without browser automation; persist small redacted CLI stdout/stderr logs and SQLite observations; keep Chrome/Playwright only as legacy fallback disabled by default.
STACK:
lang=Python3 stdlib
source=Codex_CLI
db=SQLite
platform=Oracle_VM_user_systemd
tools=codex-cli,npm,nodejs,systemd_user_timer
MAP:
entry=/home/ubuntu/codex-workspace/codex-usage-monitor/codex_cli_status_watcher.py
legacy_browser=/home/ubuntu/codex-workspace/codex-usage-monitor/codex_usage_monitor.py
local_stage=/home/daniele/codex-workspace/codex-token-watcher
db=/home/ubuntu/.local/share/codex-usage-monitor/codex_usage.sqlite3
table=cli_status_observations
raw_logs=/home/ubuntu/.local/state/codex-usage-monitor/cli-status-logs
systemd=/home/ubuntu/.config/systemd/user/codex-usage-monitor.service
timer=/home/ubuntu/.config/systemd/user/codex-usage-monitor.timer
env=/home/ubuntu/.config/codex-usage-monitor/codex-usage-monitor.env
ARCH:
arch=Oracle VM authoritative runtime. Normal path is CLI-only: codex doctor --json + codex login status -> redacted raw log -> SQLite cli_status_observations -> optional Kuma push.
legacy=Chrome/Playwright code remains for manual fallback only; systemd normal path does not call browser, Chrome, Playwright, Cloudflare, or web login.
FLOW:
flow=systemd_user_timer_hourly->codex_cli_status_watcher.py once->codex --version->codex login status->codex doctor --json->parse auth/runtime fields->save raw redacted JSON log->insert SQLite row source=cli_status->Kuma if env URL configured.
INV:
source=All new rows use source=cli_status.
states=ok,unavailable,parse_error
security=Do not read/copy/commit ~/.codex/auth.json; do not store tokens/cookies/API keys; redact stdout/stderr; raw logs capped and retained max 30 timestamped logs plus latest.
data=Historical SQLite data is preserved; new table is additive.
runtime=VM path is authoritative; Mint local repo is staging/versioning.
browser=Do not open browser for normal run.
package=Codex CLI fixed 2026-06-05 by NodeSource nodejs 22.22.3 and npm @openai/codex 0.137.0; stale /usr/local/bin/codex removed; active codex=/usr/bin/codex.
BUILD:
cmd=python3 -m py_compile codex_cli_status_watcher.py codex_usage_monitor.py
deploy=scp script+systemd+docs to VM; install -m 755 script; install -m 644 units; systemctl --user daemon-reload
TEST:
cmd=which codex; codex --help; codex status; codex /status; codex login status; codex doctor --json; codex exec --skip-git-repo-check --json smoke; ./codex_cli_status_watcher.py once; sqlite3 latest row; systemctl --user status service/timer
result=2026-06-05 service code=0/SUCCESS; timer active(waiting), next=2026-06-05T11:00:00Z; latest DB row id=5 status=ok source=cli_status codex_version=0.137.0 auth_mode=chatgpt stored_chatgpt_tokens=1 model=gpt-5.4 websocket_status=ok quota_fields_available=0.
DATA:
db=/home/ubuntu/.local/share/codex-usage-monitor/codex_usage.sqlite3
table=cli_status_observations columns=id,ts_utc,source,status,codex_bin,codex_version,login_status,auth_mode,auth_configured,stored_chatgpt_tokens,stored_api_key,overall_status,model,model_provider,websocket_status,websocket_summary,provider_reachability_status,provider_reachability_summary,quota_fields_available,quota_fields_json,raw_log_path,error,created_at
logs=/home/ubuntu/.local/state/codex-usage-monitor/cli-status-logs/YYYYMMDDTHHMMSSZ-cli-status.json; latest-cli-status.json
log_size=observed about 15-16KB each on 2026-06-05; retention=30 timestamped logs
backup=No historical DB deletion performed.
DNB:
dnb=Do not create duplicate project/repo/service names.
dnb=Do not use Chrome/Playwright/Cloudflare/login web in normal backend.
dnb=Do not commit DB/logs/env/auth files.
dnb=Do not store secrets from ~/.codex/auth.json or env files.
dnb=Do not treat codex status or codex /status as automation-safe; they require TTY and open interactive UI.
BUG:
issue=2026-06-05 pre-migration CLI existed at /usr/local/bin/codex but failed with Node v12 SyntaxError top-level await. Fixed by installing NodeSource nodejs 22.22.3 and @openai/codex 0.137.0 under /usr; removed stale /usr/local/bin/codex.
issue=2026-06-05 codex status and codex /status over non-TTY return Error: stdin is not a terminal; with TTY they open interactive UI and produce no parsable status before timeout.
RISK:
risk=Codex CLI 0.137.0 exposes auth/runtime health but not quota/token-budget fields non-interactively; watcher records quota_fields_available=0.
risk=doctor --json takes about 20-30s because it checks websocket and Codex SQLite state.
risk=Kuma URL not configured on VM as of 2026-06-05; Telegram helper /home/ubuntu/telegram_notify.py missing.
ROAD:
now=CLI-only watcher deployed on VM; browser backend disabled in service/timer.
next=If future Codex CLI exposes non-interactive quota fields, extend parser and set quota_fields_available=1 without reintroducing browser.
later=Optional Telegram integration only after helper/env exists on VM; keep secrets outside repo.
LINK:
meta=../../../codex-token-watcher/dev/project.metadata.json
human=../../human/projects/codex-token-watcher/overview.md
legacy=../../../codex-token-watcher/dev/legacy
repo=../../../codex-token-watcher
OPEN:
open=Kuma not configured: no CODEX_USAGE_KUMA_PUSH_URL in /home/ubuntu/.config/codex-usage-monitor/codex-usage-monitor.env on 2026-06-05.
open=Telegram not configured: /home/ubuntu/telegram_notify.py missing on 2026-06-05.
open=No non-interactive Codex quota fields found in CLI 0.137.0; current extracted fields are runtime/auth/model/websocket/provider status.
