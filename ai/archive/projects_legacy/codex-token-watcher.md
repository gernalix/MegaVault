META:
name=codex-token-watcher
slug=codex-token-watcher
path=/home/daniele/codex-workspace/codex-token-watcher
vm_host=ubuntu@150.230.148.128
vm_role=Uptime_Kuma_endpoint_only
remote=none
branch=codex/prompt-384921
verified_commit=UNKNOWN
verified_at=2026-06-10T20:24:00+02:00
protocol=MEGAVAULT_PROTOCOL.md:v8
PURPOSE:
purpose=Monitor Codex CLI health/status and local Codex session quota cache from Linux Mint; persist redacted logs and SQLite observations; push health to Oracle VM Kuma; keep Chrome/Playwright only as legacy manual fallback.
STACK:
lang=Python3 stdlib
source=Codex_CLI+local_session_token_count_cache
db=SQLite
platform=Linux_Mint_user_systemd
tools=codex-cli,npm,nodejs,systemd_user_timer,Uptime_Kuma_push
MAP:
entry=/home/daniele/codex-workspace/codex-token-watcher/codex_cli_status_watcher.py
legacy_browser=/home/daniele/codex-workspace/codex-token-watcher/codex_usage_monitor.py
commands=once,status,deep-once,deep-status,deep-debug-limits,human-status,human-status --json,notify-test --dry-run,notify-test --force
db=/home/daniele/.local/share/codex-usage-monitor/codex_usage.sqlite3
table=cli_status_observations
deep_table=cli_status_deep_observations
raw_logs=/home/daniele/.local/state/codex-usage-monitor/cli-status-logs
systemd=/home/daniele/.config/systemd/user/codex-usage-monitor.service
timer=/home/daniele/.config/systemd/user/codex-usage-monitor.timer
env=/home/daniele/.config/codex-usage-monitor/codex-usage-monitor.env
kuma_monitor=Oracle_VM_Uptime_Kuma monitor_id=10 name=codex-token-watcher type=push interval=4200 retry_interval=300
ARCH:
normal=CLI-only systemd timer; no browser, no Cloudflare, no ChatGPT web scraping in service path.
flow=timer_hourly->codex_cli_status_watcher.py once->CODEX_CLI_BIN codex --version/login status/doctor --json->redacted raw log->SQLite cli_status_observations->Kuma push.
deep=manual/service deep-once reads newest ~/.codex/sessions/**/*.jsonl event_msg payload type=token_count -> cli_status_deep_observations.
telegram=default brief Italian remaining-only quota notification from deep cache; verbose debug only if CODEX_QUOTA_TELEGRAM_VERBOSE=1.
legacy=codex_usage_monitor.py still exists for manual dashboard/Chrome fallback; not used by service because Cloudflare challenge can block it and data becomes non-authoritative.
INV:
source=All CLI service rows use source=cli_status.
deep_source=All quota-cache rows use source=cli_status_deep.
quota_truth=token_count_session_cache_not_CLI_live_not_SQLite_origin_not_legacy_browser;SQLite stores parsed cache rows.
states=ok,unavailable,parse_error
systemd=oneshot exits 0 after persisting measurement; monitor truth is SQLite status+Kuma heartbeat, not systemd success alone.
security=Do not read/copy/commit ~/.codex/auth.json; do not store tokens/cookies/API keys; redact stdout/stderr; raw logs capped and retained max 30 timestamped logs plus latest.
runtime=Linux Mint local path is authoritative; VM is Kuma only.
package=Systemd must use CODEX_CLI_BIN=/home/daniele/.npm-global/bin/codex; /usr/bin/codex is stale 0.128.0 and fails current config.
BUILD:
cmd=python3 -m py_compile *.py
deploy=install -m 644 systemd units to ~/.config/systemd/user; systemctl --user daemon-reload; enable --now codex-usage-monitor.timer
TEST:
cmd=python3 -m py_compile *.py; ./codex_cli_status_watcher.py human-status; ./codex_cli_status_watcher.py human-status --json; ./codex_cli_status_watcher.py deep-once; ./codex_cli_status_watcher.py notify-test --dry-run; ./codex_cli_status_watcher.py notify-test --force; ./codex_cli_status_watcher.py once; systemctl --user start/status service; journalctl; sqlite3 latest rows; remote Kuma latest heartbeat.
result=2026-06-10 systemd service code=0/SUCCESS; cli row id=6 status=ok source=cli_status codex_bin=/home/daniele/.npm-global/bin/codex codex_version=0.139.0 auth_mode=chatgpt stored_chatgpt_tokens=1 model=gpt-5.5 websocket_status=ok provider_reachability_status=ok quota_fields_available=0; Kuma heartbeat monitor_id=10 status=1 msg="codex cli status ok; version=0.139.0".
deep_result=2026-06-10 deep row id=2 status=ok source=cli_status_deep event=/home/daniele/.codex/sessions/2026/06/10/rollout-2026-06-10T19-14-44-019eb287-7eb0-7a51-bb3e-86bab8260b19.jsonl:92 limit_id=codex plan_type=prolite primary_used_percent=23 primary_remaining_percent=77 secondary_used_percent=54 secondary_remaining_percent=46 quota_fields_available=1.
DATA:
db=/home/daniele/.local/share/codex-usage-monitor/codex_usage.sqlite3
logs=/home/daniele/.local/state/codex-usage-monitor/cli-status-logs/YYYYMMDDTHHMMSSZ-cli-status.json; latest-cli-status.json
deep_logs=/home/daniele/.local/state/codex-usage-monitor/cli-status-logs/YYYYMMDDTHHMMSSZ-cli-status-deep.json; latest-cli-status-deep.json
human_status=read-only; no new DB rows; reads latest valid cli_status_deep_observations row; exposes source,updated_at,age_seconds,stale.
telegram_state=SQLite monitor_state.quota_telegram_last_snapshot; notification_events stores send history.
DNB:
dnb=Do not create duplicate project/repo/service names.
dnb=Do not use Chrome/Playwright/Cloudflare/login web in normal service backend.
dnb=Do not commit DB/logs/env/auth files.
dnb=Do not print Kuma push tokens or Telegram/OpenAI secrets.
dnb=Do not treat codex status or codex /status as automation-safe; they require TTY and open interactive UI.
dnb=Do not put used/window/Unix/ISO/debug fields in default Telegram quota message.
BUG:
issue=2026-06-10 Kuma red causes: legacy browser service pushed down from Cloudflare `Just a moment...`; Kuma interval was 60s while timer was hourly; systemd resolved stale /usr/bin/codex 0.128.0; CLI push URL appended duplicate status/msg/ping query params and Kuma kept old status. Fixed by CLI-only unit, CODEX_CLI_BIN, query replacement, and Kuma interval 4200s.
issue=codex status and codex /status over non-TTY return stdin/TTY errors or open interactive UI; not valid for timers.
RISK:
risk=Codex CLI exposes auth/runtime health but not quota/token-budget fields via non-interactive command; watcher once records quota_fields_available=0.
risk=Deep quota values are cache-derived from session token_count events and can be stale if no Codex session has run recently; stale warning threshold defaults to 60m.
risk=Kuma monitor interval must remain longer than timer cadence; current monitor id=10 interval=4200 retry_interval=300.
ROAD:
now=CLI-only watcher deployed locally; deep local session-cache quota collector available manually; browser backend disabled in service/timer.
next=If future Codex CLI exposes non-interactive quota endpoint/command, prefer it over session-cache freshness.
later=Optional Telegram integration only after helper/env exists and secrets remain outside repo.
LINK:
meta=../../../codex-token-watcher/dev/project.metadata.json
human=../../human/projects/codex-token-watcher/overview.md
legacy=../../../codex-token-watcher/dev/legacy
repo=../../../codex-token-watcher
OPEN:
open=Telegram delivery not retested in 2026-06-10 repair; normal CLI service path does not require Telegram.
open=No non-interactive Codex quota command found in CLI 0.139.0; deep collector reads local session event cache, not a live quota refresh endpoint.
open=2026-06-10 #914672 cache-vs-dashboard drift was timing/staleness class; check deep-debug-limits before declaring mismatch.
