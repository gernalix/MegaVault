META:
name=codex-token-watcher
slug=codex-token-watcher
path=/home/daniele/codex-workspace/codex-token-watcher
remote=none
branch=codex/prompt-384921
verified_commit=fa7b3b0
verified_at=2026-06-02T10:10:00+02:00
protocol=MEGAVAULT_PROTOCOL.md:v2
PURPOSE:
purpose=Monitor ChatGPT Codex Analytics quota from Linux Mint local persistent Chrome profile; persist local SQLite/CSV diagnostics; notify Telegram on weekly percent changes; push remote Uptime Kuma heartbeat on Oracle VM.
STACK:
lang=Python3
fw=Playwright+Chromium/CDP
db=SQLite+CSV
platform=Linux_Mint_local; Oracle_VM_only_Kuma_endpoint
tools=systemd_user_timer,telegram_notify.py,Uptime_Kuma
MAP:
entry=/home/daniele/codex-workspace/codex-token-watcher/codex_usage_monitor.py
ui=UNKNOWN
core=extract_dashboard,command_once,maybe_notify_weekly_change,push_kuma,command_doctor,command_stats,command_setup_login/open-login
db=/home/daniele/.local/share/codex-usage-monitor/codex_usage.sqlite3
tests=py_compile+stats+doctor+sqlite_last_record+systemd_status
scripts=systemd/codex-usage-monitor.service,systemd/codex-usage-monitor.timer
build=.venv+requirements.txt local
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
arch=Local Mint authoritative runtime. Browser profile/env/db/state live outside repo. Oracle VM must not scrape Codex; it is only remote Uptime Kuma endpoint. Timer runs local oneshot poll hourly after login/challenge is cleared.
FLOW:
flow=local_systemd_timer_hourly->codex_usage_monitor.py once->local Chrome persistent profile->Codex Analytics visible text->parse 5h/weekly percent+reset->local SQLite/CSV->weekly state atomic->Telegram on weekly change->remote Kuma up/down.
INV:
arch=Do not duplicate project slug; local repo path is runtime source; VM scraping disabled.
data=dev/project.metadata.json:9:"metadata_version": 1,; dev/project.metadata.json:2:"project_name": "codex-token-watcher",
ux=UNKNOWN
backup=Runtime DB/CSV/state outside git; diagnostics html/png/txt under /home/daniele/.local/state/codex-usage-monitor/diagnostics.
migration=UNKNOWN
version=script_VERSION=v3 deployed_local_hourly
i18n=UNKNOWN
security=env_file mode 600; never log Telegram tokens/cookies/Kuma URL token; Chrome profile outside repo.
perf=one compact log line per cycle; timeout managed by systemd; hourly polling reduces browser launches from 288/day to about 24/day.
BUILD:
files=/home/daniele/codex-workspace/codex-token-watcher/requirements.txt
cmd=python3 -m py_compile codex_usage_monitor.py
TEST:
files=codex_usage_monitor.py
cmd=python3 -m py_compile codex_usage_monitor.py; synthetic extract_dashboard sample; weekly state dry-run with fake Telegram helper; ./codex_usage_monitor.py once local
DATA:
db=SQLite /home/daniele/.local/share/codex-usage-monitor/codex_usage.sqlite3
paths=CSV /home/daniele/.local/share/codex-usage-monitor/codex_usage.csv; state /home/daniele/.local/state/codex-usage-monitor/last_weekly_percent.json; diagnostics /home/daniele/.local/state/codex-usage-monitor/diagnostics
backup=external runtime data not committed
restore=UNKNOWN
import=dashboard visible text
export=SQLite observations,notification_events,monitor_state; CSV observation log
migration=init_db ALTER TABLE adds v3 fields idempotently
retention=hourly observations are small; diagnostics html/png/txt are only written on dashboard/parse errors.
DNB:
dnb=dev/project.metadata.json:2:"project_name": "codex-token-watcher",
dnb=dev/project.metadata.json:3:"project_slug": "codex-token-watcher",
dnb=dev/project.metadata.json:4:"project_root": "/home/daniele/codex-workspace/codex-token-watcher",
dnb=dev/project.metadata.json:6:"ai_doc": "/home/daniele/codex-workspace/MegaVault/ai/projects/codex-token-watcher.md",
dnb=dev/project.metadata.json:7:"human_doc": "/home/daniele/codex-workspace/MegaVault/human/projects/codex-token-watcher",
dnb=do_not_print_or_commit_env_tokens_cookies
dnb=do_not_notify_weekly_on_identical_polling_value
dnb=first_successful_weekly_percent_is_baseline_unless_TELEGRAM_NOTIFY_WEEKLY_BASELINE=1
dnb=save diagnostics on parse failure before returning status=error
dnb=Kuma push down on parse failure, up on readable cycle
dnb=Oracle_VM_must_not_scrape_Codex_dashboard
dnb=do_not_bypass_Cloudflare_or_automate_challenge
BUG:
issue=2026-06-02 old parser looked for generic usage contexts and missed new Codex Analytics Saldo blocks; VM scraping disabled because Cloudflare/login is unstable; local dedicated Chrome profile currently also sees Cloudflare challenge until manual profile verification.
issue=2026-06-02 local Cloudflare diagnosis: URL=https://chatgpt.com/codex/cloud/settings/analytics#usage; Chrome=/usr/bin/google-chrome Google Chrome 148; profile=/home/daniele/.local/share/codex-usage-monitor/chrome-profile/Default; chatgpt/openai cookies present; systemd graphical env OK DISPLAY=:0 DBUS/XDG_RUNTIME_DIR present; latest challenge screenshot shows Cloudflare "Verify you are human"; doctor reports navigator.webdriver=True in Playwright session.
RISK:
risk=Cloudflare/login challenge blocks headless scraping; headed local Playwright uses real Chrome+dedicated profile but exposes navigator.webdriver=True. Do not add aggressive bypasses or stealth workarounds.
risk=Dashboard text labels can drift; parser must stay label+percent contextual, not selector-specific.
ROAD:
now=Local watcher installed with hourly user timer; Oracle VM remains Kuma-only; doctor exposes browser/profile/env/last diagnostics; open-login opens same profile for manual login/challenge.
next=Use stats before design changes; current all-history sample is 12 runs over 1.30h, success=50%, Cloudflare=33.3%, recommendation=observe more. Run open-login manually only if Cloudflare becomes sustained.
later=Add fixture from real successful dashboard HTML/text if labels drift again.
LINK:
meta=../../../codex-token-watcher/dev/project.metadata.json
human=../../human/projects/codex-token-watcher/overview.md
legacy=../../../codex-token-watcher/dev/legacy
repo=../../../codex-token-watcher
OPEN:
open=2026-06-05 Cloudflare remains current blocker: latest local systemd run id=71 at 2026-06-05T06:00:01Z wrote DB status=error, page_title="Just a moment...", Kuma down push returned ok, diagnostics at /home/daniele/.local/state/codex-usage-monitor/diagnostics/20260605T060053Z-dashboard-parse.{txt,html,png}. Timer/service and DB are healthy. Manual open-login is required; do not bypass Cloudflare and do not move scraping to Oracle VM.
open=Manual recovery command: cd /home/daniele/codex-workspace/codex-token-watcher && CODEX_USAGE_HEADLESS=0 ./codex_usage_monitor.py open-login. Use profile /home/daniele/.local/share/codex-usage-monitor/chrome-profile/Default, resolve Cloudflare/login manually, confirm Codex Analytics is visible, close Chrome, then run ./codex_usage_monitor.py doctor and ./codex_usage_monitor.py once.
