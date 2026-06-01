META:
name=WindowTabNotes
slug=windowtabnotes
path=/home/daniele/codex-workspace/WindowTabNotes
remote=git@github.com:gernalix/WindowTabNotes.git
branch=codex/prompt-581472
verified_commit=68e0170
verified_at=2026-06-01T13:59:53+02:00
protocol=MEGAVAULT_PROTOCOL.md:v2
PURPOSE:
purpose=Root repository: `WindowTabNotes/`
STACK:
lang=JS/TS,Python,Shell
fw=UNKNOWN
db=SQLite
platform=UNKNOWN
tools=Chrome,systemd
MAP:
entry=browser-extension/manifest.json,system/windowtabnotes/cli.py
ui=UNKNOWN
core=browser-extension/content_script.js,browser-extension/content_style.css,browser-extension/dashboard.css,browser-extension/dashboard.html,browser-extension/dashboard.js
db=UNKNOWN
tests=UNKNOWN
scripts=system/scripts/install.sh,system/scripts/uninstall.sh
build=UNKNOWN
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
entry=system/windowtabnotes/cli.py:main,create_note_for_active_window,anchored_note_geometry,check_status
core=browser-extension/content_script.js:cleanupLegacyUi,LEGACY_SELECTORS
core=browser-extension/dashboard.js:openGlobalDashboard,statusEl,params,focusSearch,response
core=browser-extension/focus.js:params
core=browser-extension/popup.js:setStatus,setTabInfo,load,statusEl,tabInfoEl,openNoteEl
core=browser-extension/service_worker.js:createEmptyState,sanitizeState,loadState,saveState,enqueueMutation,mutateState
core=system/windowtabnotes/active_watch.py:OverlayController,sync_open_windows,active_note_for_current_context,handle_active_window,run_active_window_watch,active_window_watch_debug
core=system/windowtabnotes/api.py:handle_native_message,_record_from_tab,_tab_row,_is_internal_focus_tab,_require_dict,_require_str
FLOW:
flow=entry->browser-extension/manifest.json=>browser-extension/content_script.js
flow=script->system/scripts/install.sh=>browser-extension/content_script.js
flow=browser-extension/manifest.json:21:"service_worker": "service_worker.js"
flow=system/windowtabnotes/cli.py:6:from pathlib import Path
flow=system/windowtabnotes/cli.py:8:from . import db, overlay_runtime
INV:
arch=system/windowtabnotes/cli.py:main,create_note_for_active_window,anchored_note_geometry,check_status; browser-extension/content_script.js:cleanupLegacyUi,LEGACY_SELECTORS; browser-extension/dashboard.js:openGlobalDashboard,statusEl,params...
data=browser-extension/manifest.json:2:"manifest_version": 3,; browser-extension/manifest.json:4:"version": "20.0.0",
ux=browser-extension/manifest.json:2:"manifest_version": 3,; browser-extension/manifest.json:4:"version": "20.0.0",
backup=system/windowtabnotes/logging_setup.py:27:file_handler = RotatingFileHandler(path, maxBytes=512_000, backupCount=3); browser-extension/service_worker.js:138:delete snapshot[String(tabId)];
migration=system/windowtabnotes/db.py:18:SCHEMA_VERSION = 4; system/windowtabnotes/db.py:76:current = get_schema_version(conn)
version=browser-extension/manifest.json:2:"manifest_version": 3,; browser-extension/manifest.json:4:"version": "20.0.0",
i18n=UNKNOWN
security=system/windowtabnotes/active_watch.py:101:overlay_runtime.cleanup_overlays_locked(reason=event_origin, current_context_key=note_key); system/windowtabnotes/overlay_runtime.py:42:return cleanup_overlays_locked(keep_pid, keep_note_id, reas...
perf=browser-extension/service_worker.js:256:clearTimeout(pending.timer);; browser-extension/service_worker.js:258:const timer = setTimeout(() => {
BUILD:
files=UNKNOWN
cmd=UNKNOWN
TEST:
files=UNKNOWN
cmd=UNKNOWN
DATA:
db=system/windowtabnotes/cli.py:8:from . import db, overlay_runtime; system/windowtabnotes/cli.py:10:from .config import db_path, load_settings, log_path
paths=system/windowtabnotes/cli.py:10:from .config import db_path, load_settings, log_path; system/windowtabnotes/config.py:38:return Path(os.environ.get("WTN_DB", data_dir() / "windowtabnotes.sqlite3"))
backup=system/windowtabnotes/logging_setup.py:27:file_handler = RotatingFileHandler(path, maxBytes=512_000, backupCount=3); system/windowtabnotes/active_watch.py:129:for snap in snapshots:
restore=system/windowtabnotes/cli.py:6:from pathlib import Path; system/windowtabnotes/cli.py:8:from . import db, overlay_runtime
import=system/windowtabnotes/cli.py:6:from pathlib import Path; system/windowtabnotes/cli.py:8:from . import db, overlay_runtime
export=system/windowtabnotes/api.py:17:return _error("invalid_request", "Il messaggio deve essere un oggetto JSON."); system/windowtabnotes/config.py:46:return config_dir() / "settings.json"
migration=system/windowtabnotes/db.py:18:SCHEMA_VERSION = 4; system/windowtabnotes/db.py:76:current = get_schema_version(conn)
retention=system/windowtabnotes/active_watch.py:33:overlay_runtime.cleanup_overlays_locked(reason=event_origin); system/windowtabnotes/active_watch.py:77:overlay_runtime.cleanup_overlays_locked(
DNB:
dnb=browser-extension/service_worker.js:138:delete snapshot[String(tabId)];
dnb=browser-extension/service_worker.js:259:pendingTabSyncs.delete(key);
dnb=browser-extension/service_worker.js:414:delete state.tabBindings[String(tabId)];
dnb=system/windowtabnotes/active_watch.py:32:with overlay_runtime.overlay_lock():
dnb=system/windowtabnotes/active_watch.py:33:overlay_runtime.cleanup_overlays_locked(reason=event_origin)
dnb=system/windowtabnotes/active_watch.py:73:with overlay_runtime.overlay_lock():
dnb=preserve=dev/project.metadata.json,dev/legacy,AI/Human links; docs-only tasks must not touch app code/DB
BUG:
issue=system/windowtabnotes/cli.py:9:from .active_watch import active_note_for_current_context, active_window_watch_debug, sync_open_windows
issue=system/windowtabnotes/cli.py:12:from .gtk_ui import dashboard_debug, open_dashboard, open_note_window, overlay_debug
issue=system/windowtabnotes/cli.py:14:from .native_debug import run_native_debug
issue=system/windowtabnotes/cli.py:16:from .rofi import install_search_launcher, run_global_search, run_search_launcher, search_debug
issue=system/windowtabnotes/cli.py:35:overlay_debug_parser = sub.add_parser("overlay-debug")
RISK:
risk=browser-extension/service_worker.js:138:delete snapshot[String(tabId)];
risk=browser-extension/service_worker.js:259:pendingTabSyncs.delete(key);
risk=browser-extension/service_worker.js:414:delete state.tabBindings[String(tabId)];
risk=system/windowtabnotes/active_watch.py:32:with overlay_runtime.overlay_lock():
risk=system/windowtabnotes/active_watch.py:33:overlay_runtime.cleanup_overlays_locked(reason=event_origin)
risk=system/windowtabnotes/active_watch.py:73:with overlay_runtime.overlay_lock():
ROAD:
now=UNKNOWN
next=UNKNOWN
later=UNKNOWN
LINK:
meta=../../../WindowTabNotes/dev/project.metadata.json
human=../../human/projects/windowtabnotes/overview.md
legacy=../../../WindowTabNotes/dev/legacy
repo=../../../WindowTabNotes
OPEN:
open=tests=UNKNOWN_OR_ABSENT
