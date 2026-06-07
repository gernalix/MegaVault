META:
name=WindowTabNotes
slug=windowtabnotes
path=/home/daniele/codex-workspace/WindowTabNotes
remote=git@github.com:gernalix/WindowTabNotes.git
branch=codex/prompt-581472
verified_commit=7a19e0e+dirty_prompt_739284_service
verified_at=2026-06-07T09:02:18+02:00
megavault_branch=codex/prompt-927384-android-studio-download-guard
protocol=MEGAVAULT_PROTOCOL.md:v2

PURPOSE:
purpose=Linux/X11 + Chrome/Firefox tab note overlay; stores notes in local SQLite and binds each note to a normal window, browser tab, or workspace context.

STACK:
lang=Python,JavaScript,Shell
ui=GTK via PyGObject,Chrome MV3 extension,Firefox MV3 extension,rofi
db=SQLite WAL
service=systemd --user windowtabnotes.service
platform=Linux Mint/XFCE/X11,Chrome/Chromium Native Messaging,Firefox Native Messaging

MAP:
entry=system/bin/windowtabnotes -> python3 -m windowtabnotes.cli
status=system/bin/windowtabnotes-status -> windowtabnotes status
daemon=system/windowtabnotes/daemon.py,system/windowtabnotes/active_watch.py
db=system/windowtabnotes/db.py
native=system/bin/windowtabnotes-native-host,system/windowtabnotes/native_host.py,system/windowtabnotes/api.py
chrome=browser-extension/manifest.json,browser-extension/service_worker.js,browser-extension/content_script.js,browser-extension/popup.js
firefox=browser-extension-firefox/manifest.json + symlinked common files from browser-extension/
ui=system/windowtabnotes/gtk_ui.py,browser-extension/dashboard.html,browser-extension/dashboard.js
search=system/windowtabnotes/rofi.py
shortcuts=system/windowtabnotes/shortcuts.py
systemd=system/systemd/windowtabnotes.service.in,~/.config/systemd/user/windowtabnotes.service
install=system/scripts/install.sh
tests=tests/test_context_persistence.py
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated,__pycache__

ARCH:
cli=argparse commands version/init-db/daemon/status/check/native-debug/search/overlay/shortcuts
daemon=active window watcher: xprop -spy _NET_ACTIVE_WINDOW + fallback poll + Chrome active-tab metadata
windows=wmctrl lists normal windows; xprop/xdotool read active id,title,class,pid,geometry
overlay=GTK note process launched per note; overlay_runtime tracks visible note in DB metadata and cleans stale overlay windows
db=single local SQLite DB; note rows keep relational context_id plus v5 denormalized context snapshot
native_host=Chrome starts stdio host per native message; wrapper and Python metrics throttle reconnect storms
browser_bridge=shared service_worker.js syncs open tabs/active tab to native host; backend stores browser_tabs and active_browser_tab metadata
search=rofi/global search reads DB search index and queues Chrome focus requests through DB metadata

FLOW:
normal_window=daemon active_window -> upsert_window_context -> ensure/create note -> notes.context_* snapshot -> GTK overlay
chrome_tab=Chrome service_worker snapshotTab -> native UPSERT_TAB/SYNC_OPEN_TABS -> upsert_browser_tab -> note_for_browser_tab -> notes.context_url/title/tab/window snapshot -> GTK overlay when requested
chrome_focus=search queues chrome_focus_request metadata -> service_worker GET_FOCUS_REQUEST poll -> chrome.tabs/window focus or close
save_text=content/GTK -> native SAVE_NOTE_TEXT or local UI -> db.update_note_text -> refresh context snapshot -> notes.updated_at
service=~/.config/systemd/user/windowtabnotes.service -> system/bin/windowtabnotes daemon -> Restart=always
service_prompt_739284=enabled+active; MainPID restarts after SIGTERM; linger=yes; ExecStart=/home/daniele/codex-workspace/WindowTabNotes/system/bin/windowtabnotes daemon; WorkingDirectory=/home/daniele/codex-workspace/WindowTabNotes

INV:
data=do_not_delete_real_notes_during_tests_or_repair
data=DB path default ~/.local/share/windowtabnotes/windowtabnotes.sqlite3; override WTN_DB
data=notes table owns text, created_at, updated_at, context_type, context_id, geometry, visibility, context_app, context_title, context_window_id, context_workspace, context_url, context_browser_tab_id, context_browser_window_id, context_key
data=window_contexts owns window_id,app_class,title,workspace,pid,wm_name,last_seen_at
data=browser_tabs owns browser_tab_id,browser_window_id,url,title,fav_icon_url,active,incognito,index,profile_key,normalized_url,note_key,last_seen_at
data=browser note identity prefers normalized_url+profile note_key; falls back to Chrome window/tab ids
service=user unit must stay enabled and active; linger currently yes on host
service=daemon must log and skip transient sqlite locked/xdotool timeout rather than exiting
service=human_status=systemctl --user status windowtabnotes.service --no-pager; logs=journalctl --user -u windowtabnotes.service -n 80 --no-pager; restart=systemctl --user restart windowtabnotes.service
chrome=Native Messaging host name com.windowtabnotes.host; installed manifests under Chrome/Chromium NativeMessagingHosts
firefox=Native Messaging host name com.windowtabnotes.host; add-on id windowtabnotes@local; manifest under ~/.mozilla/native-messaging-hosts/
ux=do not break overlay/search behavior while changing persistence/service code
version=monotonic integer in system/windowtabnotes/version.py,browser-extension/manifest.json,browser-extension-firefox/manifest.json

BUILD:
cmd=none
run=system/bin/windowtabnotes <command>
install_chrome=system/scripts/install.sh --extension-id <chrome_extension_id>
install_firefox=system/scripts/install-firefox.sh [windowtabnotes@local]
deps=python3,python3-gi,GTK3,sqlite3,rofi,wmctrl,xdotool,xprop,jq optional

TEST:
compile=python3 -m compileall -q system/windowtabnotes tests
unit=PYTHONPATH=system python3 -m unittest tests/test_context_persistence.py
service=systemctl --user is-active windowtabnotes.service; systemctl --user is-enabled windowtabnotes.service; journalctl --user -u windowtabnotes.service --since '2 minutes ago'
status=system/bin/windowtabnotes-status --json
prompt_739284=daemon-reload+enable --now; is-enabled=enabled; is-active=active; status active running; journal readable; restart active; SIGTERM MainPID -> NRestarts=1 active; dashboard-debug ok; search-debug ok; overlay-debug ok; check --json db ok with window_sync skipped on live DB lock
native_chrome=system/bin/windowtabnotes native-debug --extension-id <chrome_extension_id> --json
native_firefox=system/bin/windowtabnotes native-debug --browser firefox --firefox-extension-id windowtabnotes@local --json

DATA:
DB=SQLite
Schema=5
Path=~/.local/share/windowtabnotes/windowtabnotes.sqlite3
Override=WTN_DB
Log=~/.cache/windowtabnotes/windowtabnotes.log
NativeMetrics=~/.cache/windowtabnotes/native_host_metrics.json
Settings=~/.config/windowtabnotes/settings.json
Migration=v5 adds note context snapshot columns and backfills from extant window_contexts/browser_tabs/workspaces
Backup=manual copy DB before destructive recovery; WAL active
Restore=UNKNOWN
Import=UNKNOWN
Export=UNKNOWN
Retention=logs rotate; native metrics overwrite JSON

DNB:
* real_user_notes
* browser-extension/service_worker.js tab sync/focus request polling
* browser-extension-firefox/manifest.json must use background.scripts; Firefox does not support background.service_worker
* system/windowtabnotes/rofi.py search launcher free-text behavior
* overlay_runtime cleanup state and manual overlay suppression
* Native Messaging host manifest path/id
* MegaVault metadata+AI/Human links; legacy docs are historical only

BUG:
issue=Old journal showed daemon crashes from sqlite3.OperationalError database is locked and subprocess.TimeoutExpired xdotool getactivewindow.
fix=v21 active_watch skips/logs transient DB lock and xdotool timeout; service Restart=always.
issue=381 legacy browser_tab notes on live DB had no reconstructable tab row at v5 migration time.
impact=URL/title snapshot cannot be invented for those orphan historical notes; future writes and notes with extant context are snapshotted.
issue=Native host metrics show high GET_FOCUS_REQUEST starts/rate-limited starts.
impact=Chrome bridge works but polling can be noisy; monitor via windowtabnotes-status/native-host-status.
issue=v21 daemon stayed active but showed no overlay for windows without pre-existing notes.
fix=v22 handle_active_window uses create_if_missing=True for the active context; verified overlay_count=1/open_notes=1.
issue=Prompt #739284 live `check --json` failed on transient SQLite lock while daemon was active.
fix=check_status retries DB init and reports window_sync separately; DB ok returns exit 0 even when live sync is skipped due daemon-held lock.

RISK:
risk=SQLite lock contention from daemon + many Chrome native-host invocations.
risk=Chrome unpacked extension may keep stale service_worker until reloaded in chrome://extensions.
risk=xdotool/xprop can timeout or fail under X11/session transitions.
risk=Killing native-host or Chrome processes can interrupt active browser bridge; avoid unless user approves.
risk=Deleting orphan browser notes would destroy user data; do not clean automatically.
risk=`journalctl -n 80` can include older Jun 01 crash traces; current status command uses recent error scan and reports last_service_error empty after Jun 07 restart/kill tests.

ROAD:
now=v22 service hardening/context snapshot/status command; daemon auto-creates active context note when missing
next=reduce Native Messaging GET_FOCUS_REQUEST process churn if Chrome bridge remains noisy
later=explicit backup/export/restore commands

LINK:
meta=../../../WindowTabNotes/dev/project.metadata.json
human=../../human/projects/windowtabnotes/overview.md
changelog=../../human/projects/windowtabnotes/changelog.md
legacy=../../../WindowTabNotes/dev/legacy
repo=../../../WindowTabNotes

OPEN:
open=No safe CLI command exists to create/read/delete a real test note transactionally; current tests use temp DB.
open=381 historical Chrome notes lack recoverable URL because referenced browser_tabs rows were absent during v5 migration.
open=Build/package process remains undefined beyond scripts/install.sh.
