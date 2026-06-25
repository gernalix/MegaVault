META:
name=amici_fb
slug=amici-fb
path=C:\codex_clean_repos\amici_fb
linux_export=C:\codex\amici_fb
remote=https://github.com/gernalix/amici_fb.git
branch=master
verified_at=2026-06-25T16:44:23+02:00
protocol=MEGAVAULT_PROTOCOL.md:v3

PURPOSE:
Windows 11 automation that opens Facebook with Playwright, snapshots the friend list to CSV, stores SQLite state, computes CSV diffs, writes scheduler logs, and optionally reports to Telegram and Uptime Kuma.

STACK:
lang=Python,CMD,PowerShell
runtime=global Python only; no venv/.venv/virtualenv
python=C:\Users\seste\AppData\Local\Programs\Python\Python314\python.exe
libs=playwright,requests
browser=C:\Users\seste\AppData\Local\ms-playwright\chromium_headless_shell-1223
db=SQLite
scheduler=Windows Task Scheduler

ARCH:
entry_scheduled=amici_fb_daily.cmd -> amici_fb_task_runner.py --headless -> amici_fb.py
entry_manual=python -u -X faulthandler .\amici_fb_task_runner.py --headless
entry_login_refresh=python -u .\amici_fb_task_runner.py --login --login-wait-seconds 600
core=amici_fb.py
notifications=telegram_notify.py
task_installer=install_windows_task.ps1
metadata=dev/project.metadata.json
local_state=.env,fb_storage_state.json,amici_fb.sqlite3,data\

FLOW:
1=Load ignored local config from .env in task runner.
2=Launch global Python and Playwright Chromium/headless shell.
3=Load fb_storage_state.json.
4=Navigate to /me and /me/friends.
5=Detect login/checkpoint/consent/profile chooser states.
6=If profile chooser appears, try bounded Continue clicks and fail with artifacts if Facebook loops.
7=Scroll friends page, extract links, apply exceptions, write CSV and SQLite.
8=Compare with previous healthy snapshot, write diff CSV.
9=Close browser/context/page/DB in cleanup; runner sends Kuma OK/down and returns correct exit code.

INV:
valid_repo=C:\codex_clean_repos\amici_fb
invalid_git_source=C:\codex\amici_fb must remain a file snapshot only
task_name=amici_fb Daily Snapshot 0900
task_state_required=Ready after each run
no_local_python_envs=true
do_not_commit=.env,fb_storage_state.json,amici_fb.sqlite3,*.sqlite3,data\,data\scheduler_logs\,*.log,cache,temp,generated outputs
secrets_never_print=Telegram token/chat id,Kuma push URL,cookies,Facebook storage state

BUILD:
install_deps=python -m pip install -r requirements.txt
install_browser=python -m playwright install chromium
compile_check=python -m py_compile amici_fb.py amici_fb_task_runner.py telegram_notify.py _shared\telegram_notify.py
register_task=powershell -NoProfile -ExecutionPolicy Bypass -File .\install_windows_task.ps1

DATA:
latest_snapshot=C:\codex_clean_repos\amici_fb\data\amici_2026-06-25T144337Z.csv
latest_snapshot_rows=185
latest_diff=C:\codex_clean_repos\amici_fb\data\diff_2026-06-25T144228Z_vs_2026-06-25T144337Z.csv
latest_diff_rows=0
latest_log=C:\codex_clean_repos\amici_fb\data\scheduler_logs\amici_fb_daily_2026-06-25T164336.log
latest_diag=C:\codex_clean_repos\amici_fb\data\browser_diag_2026-06-25T144337Z
local_db=C:\codex_clean_repos\amici_fb\data\amici_fb.sqlite3 or C:\codex_clean_repos\amici_fb\amici_fb.sqlite3 when legacy file exists

DNB:
Do not bypass Facebook login or 2FA.
Do not kill unrelated Chrome/Edge/Codex processes.
Do not delete local data while removing files from Git tracking; use git rm --cached for runtime state.
Do not push project changes without explicit confirmation.
Do not reintroduce Linux cron/systemd launchers as active Windows instructions.

BUG:
2026-06-25 root cause: the user-observed Running task had already finished by inspection; LastTaskResult=1. The log showed Facebook redirected /me and /me/friends to the saved-profile/device-login page. The old detector misclassified it as consent because the normal Facebook footer contains Cookies. Clicking Continue looped until manual 2FA refreshed the Playwright session.
fix=Added precise profile_chooser detection, removed generic cookie/consent false positives, added bounded profile chooser click attempts, added --login-wait-seconds for console-free manual login refresh, reduced task ExecutionTimeLimit to PT45M, and untracked runtime data/session files from Git index.

RISK:
Facebook can expire or challenge the saved session again; use --login --login-wait-seconds 600 to refresh.
Telegram is not configured on this machine; runs succeed but Telegram messages are skipped.
Task Scheduler Operational event log is disabled and could not be enabled without elevation.
The registered task uses Interactive logon because Windows denied S4U registration in this user context.

ROAD:
Commit pending project changes after review.
Push only after user confirmation.
Monitor next 09:00 scheduled run.
Optionally configure Telegram environment values.
Keep data and fb_storage_state.json out of future commits.

MIGRATION:
date=2026-06-25
source_snapshot=C:\codex\amici_fb
clean_clone=C:\codex_clean_repos\amici_fb
recovered=.env local config, SQLite DB, historical data as local runtime state
windows_changes=global Python launcher, Task Scheduler installer, Kuma via requests, Python 3.14 UTC fix, no venv references

SCHEDULER:
task_name=amici_fb Daily Snapshot 0900
time=09:00 daily
start_when_available=true
execution_time_limit=PT45M
multiple_instances=IgnoreNew
allow_hard_terminate=true
action=C:\Windows\System32\cmd.exe /d /c ""C:\codex_clean_repos\amici_fb\amici_fb_daily.cmd""
working_directory=C:\codex_clean_repos\amici_fb
user=seste
logon=Interactive
last_run=2026-06-25T16:43:35+02:00
last_result=0
next_run=2026-06-26T09:00:00+02:00

TEST:
direct_headless=2026-06-25T16:40:07+02:00 duration 37.812s exit 0; 185 friends; CSV/diff/log OK; Kuma OK; Telegram skipped not configured
scheduled=2026-06-25T16:43:35+02:00 duration 47.424s LastTaskResult 0; task returned Ready; 185 friends; CSV/diff/log OK; Kuma OK; no task child processes remained

LINK:
human=../../human/projects/amici-fb/overview.md
repo=C:\codex_clean_repos\amici_fb
metadata=C:\codex_clean_repos\amici_fb\dev\project.metadata.json
