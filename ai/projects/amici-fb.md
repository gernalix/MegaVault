META:
name=amici_fb
slug=amici-fb
path=/home/daniele/codex-workspace/scripts/amici_fb
remote=https://github.com/gernalix/amici_fb.git
branch=master
verified_commit=0e021f6
verified_at=2026-06-01T13:59:53+02:00
last_ops_check=2026-06-10T13:35:36+02:00
protocol=MEGAVAULT_PROTOCOL.md:v2
PURPOSE:
purpose=Linux Mint user-level Facebook automation that opens Facebook with a browser profile, processes friends/URLs, and records local state in SQLite; treat credentials and browser session data as sensit
STACK:
lang=Python,Shell
fw=Playwright
db=SQLite
platform=UNKNOWN
tools=Uptime Kuma,systemd
MAP:
entry=UNKNOWN
ui=UNKNOWN
core=_shared/__init__.py,_shared/telegram_notify.py,amici_fb.service,amici_fb.timer,amici_fb.py
db=fb_storage_state.json
tests=UNKNOWN
scripts=install_ubuntu_autorun.sh
build=UNKNOWN
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
core=_shared/telegram_notify.py:_first_env,_config,validate_config,_masked,config_summary,fix_mojibake
core=amici_fb.py:DiagLogger,BrowserProcessWatcher,iso_utc_z,filename_stamp_utc,ensure_output_dir,project_path
core=amici_fb_task_runner.py:_sanitize_log_text,_failure_reason,_push_url_base,push_kuma,main
core=telegram_notify.py:_load_project_env,_first_env,_config,validate_config,_masked,config_summary
FLOW:
flow=script->install_ubuntu_autorun.sh=>fb_storage_state.json
flow=data->fb_storage_state.json
flow=_shared/telegram_notify.py:16:from pathlib import Path
flow=_shared/telegram_notify.py:17:from typing import Iterable
flow=amici_fb.service:EnvironmentFile=-/home/daniele/codex-workspace/scripts/amici_fb/.env
flow=amici_fb.service:ExecStart=/home/daniele/codex-workspace/scripts/amici_fb/.venv/bin/python -u -X faulthandler /home/daniele/codex-workspace/scripts/amici_fb/amici_fb_task_runner.py --headless
flow=amici_fb.timer:OnCalendar=09:00 Persistent=true Unit=amici_fb.service
INV:
arch=_shared/telegram_notify.py:_first_env,_config,validate_config,_masked,config_summary; amici_fb.py:DiagLogger,BrowserProcessWatcher,iso_utc_z,filename_stamp_utc,ensure_output_dir; amici_fb_task_runner.py:_sanitize_log_text,_failure_reason...
data=_shared/telegram_notify.py:94:response = requests.post(_telegram_url("sendMessage"), json=payload, timeout=20); data/amici_2025-11-24.csv:73:2025-11-24,https://www.facebook.com/guido.notoladiega,guido.notoladiega,Guido Noto La Diega
ux=data/amici_2025-11-24.csv:73:2025-11-24,https://www.facebook.com/guido.notoladiega,guido.notoladiega,Guido Noto La Diega; data/amici_2025-11-28.csv:73:2025-11-28,https://www.facebook.com/guido.notoladiega,guido.notoladiega,Guido Noto La...
backup=preserve_csv_sqlite_cookie_session_files; no_delete_without_explicit_request
migration=UNKNOWN
version=dev/project.metadata.json:9:"metadata_version": 1,; amici_fb.py:383:page.on("crash", lambda: (_log(f'crash url="{safe_page_url(page)}"'), save_page_artifacts(page, diag_dir, f"{label}_crash", logger)))
i18n=UNKNOWN
security=_shared/telegram_notify.py:39:"Missing Telegram configuration: TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID must be set."; telegram_notify.py:57:"Missing Telegram configuration: TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID must be set."
perf=_shared/telegram_notify.py:94:response = requests.post(_telegram_url("sendMessage"), json=payload, timeout=20); _shared/telegram_notify.py:104:timeout=20,
BUILD:
files=requirements.txt,.venv/bin/python,amici_fb.service,amici_fb.timer
cmd=.venv/bin/python -m playwright install chromium
TEST:
files=amici_fb_task_runner.py,systemd-user
cmd=.venv/bin/python -u -X faulthandler amici_fb_task_runner.py --headless
DATA:
db=amici_fb.sqlite3
paths=amici_fb.py:51:DB_NAME = "amici_fb.sqlite3"
backup=preserve_csv_sqlite_cookie_session_files; no_delete_without_explicit_request
restore=_shared/telegram_notify.py:16:from pathlib import Path; _shared/telegram_notify.py:17:from typing import Iterable
import=_shared/telegram_notify.py:16:from pathlib import Path; _shared/telegram_notify.py:17:from typing import Iterable
export=_shared/telegram_notify.py:94:response = requests.post(_telegram_url("sendMessage"), json=payload, timeout=20); _shared/telegram_notify.py:103:json={"chat_id": chat_id, "text": text, "parse_mode": "HTML"},
migration=UNKNOWN
retention=UNKNOWN
DNB:
dnb=fb_storage_state.json:1:{"cookies": [{"name": "dbln", "value": "%7B%22100014592815674%22%3A%222eEvA3fb%22%7D", "domain": ".facebook.com", "path": "/login/device-based/", "expires": 1778165737.066748, "httpOnly": true,...
dnb=_shared/telegram_notify.py:6:- TELEGRAM_BOT_TOKEN
dnb=_shared/telegram_notify.py:22:TOKEN_ENV_NAMES = ("TELEGRAM_BOT_TOKEN",)
dnb=_shared/telegram_notify.py:35:_, token = _first_env(TOKEN_ENV_NAMES)
dnb=_shared/telegram_notify.py:37:if not token or not chat_id:
dnb=_shared/telegram_notify.py:39:"Missing Telegram configuration: TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID must be set."
dnb=preserve=dev/project.metadata.json,dev/legacy,AI/Human links; docs-only tasks must not touch app code/DB
dnb=systemd_canonical=use amici_fb.service+amici_fb.timer only; obsolete amici-fb.* caused ambiguity and did not load .env in repo template
BUG:
issue=amici_fb.py:183:def debug_rejected_csv_path(run_stamp: str):
issue=amici_fb.py:184:return str(output_dir_path() / f"debug_rejected_{run_stamp}.csv")
issue=amici_fb.py:187:def debug_cards_csv_path(run_stamp: str):
issue=amici_fb.py:188:return str(output_dir_path() / f"debug_cards_{run_stamp}.csv")
issue=2026-06-10 service_failed_at_timer
cause=Playwright venv expected chromium_headless_shell-1223 but cache only had older 1217; active amici_fb.service did load .env and Telegram config was present
fix=.venv/bin/python -m playwright install chromium; removed obsolete repo unit files amici-fb.service/amici-fb.timer; kept installed canonical user timer amici_fb.timer
verify_manual=manual runner exit0 with Snapshot salvato, Diff salvato, telegram_notify.sent, kuma_push.sent status=up msg=OK
verify=systemctl --user start amici_fb.service exit0/status=0/SUCCESS; journal has Snapshot salvato, Diff salvato, telegram_notify.sent; Kuma warning curl_rc=28 nonfatal on systemd retry
RISK:
risk=fb_storage_state.json:1:{"cookies": [{"name": "dbln", "value": "%7B%22100014592815674%22%3A%222eEvA3fb%22%7D", "domain": ".facebook.com", "path": "/login/device-based/", "expires": 1778165737.066748, "httpOnly": true,...
risk=_shared/telegram_notify.py:6:- TELEGRAM_BOT_TOKEN
risk=_shared/telegram_notify.py:22:TOKEN_ENV_NAMES = ("TELEGRAM_BOT_TOKEN",)
risk=_shared/telegram_notify.py:35:_, token = _first_env(TOKEN_ENV_NAMES)
risk=_shared/telegram_notify.py:37:if not token or not chat_id:
risk=_shared/telegram_notify.py:39:"Missing Telegram configuration: TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID must be set."
risk=Playwright browser cache may drift after package upgrades; rerun .venv/bin/python -m playwright install chromium when journal says BrowserType.launch executable missing
risk=Kuma push can timeout independently of successful snapshot job; inspect journal/state before treating as automation failure
ROAD:
now=UNKNOWN
next=UNKNOWN
later=UNKNOWN
LINK:
meta=../../../scripts/amici_fb/dev/project.metadata.json
human=../../human/projects/amici-fb/overview.md
legacy=../../../scripts/amici_fb/dev/legacy
repo=../../../scripts/amici_fb
OPEN:
open=tests=UNKNOWN_OR_ABSENT
