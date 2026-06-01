META:
name=WindowTabNotes
slug=windowtabnotes
path=/home/daniele/codex-workspace/WindowTabNotes
remote=git@github.com:gernalix/WindowTabNotes.git
branch=codex/prompt-581472
verified_commit=68e0170
verified_at=2026-06-01T13:39:31+02:00
PURPOSE:
- Root repository: `WindowTabNotes/`.
STACK:
lang=JS/TS,Python,Shell;fw=UNKNOWN;db=SQLite;platform=UNKNOWN;tools=Chrome,systemd
MAP:
entry=browser-extension/manifest.json,system/windowtabnotes/cli.py
core=browser-extension/content_script.js
core=browser-extension/content_style.css
core=browser-extension/dashboard.css
core=browser-extension/dashboard.html
core=browser-extension/dashboard.js
core=browser-extension/focus.html
core=browser-extension/focus.js
core=browser-extension/popup.css
ui=UNKNOWN
db=UNKNOWN
tests=UNKNOWN
scripts=system/scripts/install.sh,system/scripts/uninstall.sh
build=UNKNOWN
ci=UNKNOWN
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
- system/windowtabnotes/cli.py=>main,create_note_for_active_window,anchored_note_geometry,check_status
- browser-extension/content_script.js=>cleanupLegacyUi,LEGACY_SELECTORS
- browser-extension/dashboard.js=>openGlobalDashboard,statusEl,params,focusSearch,response
- browser-extension/focus.js=>params
- browser-extension/popup.js=>setStatus,setTabInfo,load,statusEl,tabInfoEl,openNoteEl,dashboardEl
- browser-extension/service_worker.js=>createEmptyState,sanitizeState,loadState,saveState,enqueueMutation,mutateState,
- system/windowtabnotes/active_watch.py=>OverlayController,sync_open_windows,active_note_for_current_context,handle_ac
- system/windowtabnotes/api.py=>handle_native_message,_record_from_tab,_tab_row,_is_internal_focus_tab,_require_dict,_
- system/windowtabnotes/config.py=>Settings,xdg_data_home,xdg_config_home,xdg_cache_home,data_dir,config_dir,cache_dir
- system/windowtabnotes/daemon.py=>run_daemon
- system/windowtabnotes/db.py=>now_ms,new_id,connect,db,init_db,migrate,get_schema_version
- system/windowtabnotes/gtk_ui.py=>_gtk,open_note_window,open_dashboard,overlay_debug,dashboard_debug,_context_row,_po
- system/windowtabnotes/logging_setup.py=>setup_logging
- system/windowtabnotes/native_debug.py=>native_host_path,repo_root,native_manifest_paths,expected_manifest,run_native
- browser-extension/manifest.json:21:"service_worker": "service_worker.js"
- system/windowtabnotes/cli.py:1:from __future__ import annotations
FLOW:
- browser-extension/manifest.json:21:"service_worker": "service_worker.js"
- system/windowtabnotes/cli.py:1:from __future__ import annotations
- system/windowtabnotes/cli.py:3:import argparse
- system/windowtabnotes/cli.py:4:import json
- system/windowtabnotes/cli.py:5:import sys
- system/windowtabnotes/cli.py:6:from pathlib import Path
- system/windowtabnotes/cli.py:8:from . import db, overlay_runtime
- system/windowtabnotes/cli.py:9:from .active_watch import active_note_for_current_context, active_window_watch_debug,
- system/windowtabnotes/cli.py:10:from .config import db_path, load_settings, log_path
- browser-extension/content_script.js:20:chrome.runtime.onMessage.addListener((message, _sender, sendResponse) => {
- browser-extension/content_script.js:25:sendResponse({ ok: true });
- browser-extension/dashboard.js:6:const response = await chrome.runtime.sendMessage({ type: "OPEN_DASHBOARD", focusSe
INV:
arch=browser-extension/manifest.json:2:"manifest_version": 3,
arch=browser-extension/manifest.json:4:"version": "20.0.0",
arch=browser-extension/manifest.json:5:"version_name": "v20",
arch=browser-extension/manifest.json:7:"permissions": [
arch=browser-extension/manifest.json:13:"host_permissions": [
arch=system/windowtabnotes/cli.py:18:from .version import version_label
data=system/windowtabnotes/cli.py:1:from __future__ import annotations
data=system/windowtabnotes/cli.py:3:import argparse
data=system/windowtabnotes/cli.py:4:import json
data=system/windowtabnotes/cli.py:5:import sys
safety=browser-extension/content_script.js:13:element.remove();
safety=browser-extension/focus.js:9:return chrome.tabs.remove(tab.id);
safety=browser-extension/service_worker.js:135:async function removeOpenTab(tabId) {
safety=browser-extension/service_worker.js:138:delete snapshot[String(tabId)];
safety=browser-extension/service_worker.js:259:pendingTabSyncs.delete(key);
safety=browser-extension/service_worker.js:312:await chrome.tabs.remove(numericTabId);
safety=browser-extension/service_worker.js:410:chrome.tabs.onRemoved.addListener((tabId) => {
ux=system/windowtabnotes/cli.py:170:width = min(width if width > 0 else 360, max(1, geometry.screen_width - 2 * saf
ux=system/windowtabnotes/cli.py:171:height = min(height if height > 0 else 220, max(1, geometry.screen_height - 2 *
ux=system/windowtabnotes/active_watch.py:449:width = min(width if width > 0 else 360, max(1, geometry.screen_width
ux=system/windowtabnotes/gtk_ui.py:10:from .version import version_label
version=browser-extension/manifest.json:2:"manifest_version": 3,
version=browser-extension/manifest.json:4:"version": "20.0.0",
version=browser-extension/manifest.json:5:"version_name": "v20",
version=system/windowtabnotes/cli.py:18:from .version import version_label
i18n=UNKNOWN
BUILD:
- system/scripts/install.sh:1:#!/usr/bin/env bash
- system/scripts/install.sh:47:sudo apt-get install -y python3 python3-gi gir1.2-gtk-3.0 sqlite3 rofi wmctrl xdotool x
- system/scripts/install.sh:54:python3 - "$CONFIG_DIR/settings.json" "$EXTENSION_ID" <<'PY'
- system/scripts/install.sh:78:systemctl --user daemon-reload // true
- system/scripts/install.sh:79:systemctl --user enable --now windowtabnotes.service // true
- system/scripts/uninstall.sh:1:#!/usr/bin/env bash
- system/scripts/uninstall.sh:5:systemctl --user disable --now windowtabnotes.service 2>/dev/null // true
- system/scripts/uninstall.sh:9:systemctl --user daemon-reload 2>/dev/null // true
TEST:
- UNKNOWN
DATA:
db=system/windowtabnotes/cli.py:1:from __future__ import annotations
db=system/windowtabnotes/cli.py:3:import argparse
db=system/windowtabnotes/cli.py:4:import json
db=system/windowtabnotes/cli.py:5:import sys
backup=system/windowtabnotes/logging_setup.py:27:file_handler = RotatingFileHandler(path, maxBytes=512_000, backupCount
import=system/windowtabnotes/cli.py:1:from __future__ import annotations
import=system/windowtabnotes/cli.py:3:import argparse
import=system/windowtabnotes/cli.py:4:import json
export=UNKNOWN
migration=UNKNOWN
retention=browser-extension/service_worker.js:138:delete snapshot[String(tabId)];
retention=browser-extension/service_worker.js:259:pendingTabSyncs.delete(key);
retention=browser-extension/service_worker.js:414:delete state.tabBindings[String(tabId)];
DNB:
- browser-extension/content_script.js:13:element.remove();
- browser-extension/focus.js:9:return chrome.tabs.remove(tab.id);
- browser-extension/service_worker.js:135:async function removeOpenTab(tabId) {
- browser-extension/service_worker.js:138:delete snapshot[String(tabId)];
- browser-extension/service_worker.js:259:pendingTabSyncs.delete(key);
- browser-extension/service_worker.js:312:await chrome.tabs.remove(numericTabId);
- browser-extension/service_worker.js:410:chrome.tabs.onRemoved.addListener((tabId) => {
- browser-extension/service_worker.js:411:removeOpenTab(tabId).catch(() => {});
- browser-extension/manifest.json:2:"manifest_version": 3,
- browser-extension/manifest.json:4:"version": "20.0.0",
BUG:
- system/windowtabnotes/cli.py:9:from .active_watch import active_note_for_current_context, active_window_watch_debug,
- system/windowtabnotes/cli.py:12:from .gtk_ui import dashboard_debug, open_dashboard, open_note_window, overlay_debug
- system/windowtabnotes/cli.py:14:from .native_debug import run_native_debug
- system/windowtabnotes/cli.py:16:from .rofi import install_search_launcher, run_global_search, run_search_launcher, s
- system/windowtabnotes/cli.py:35:overlay_debug_parser = sub.add_parser("overlay-debug")
- system/windowtabnotes/cli.py:36:overlay_debug_parser.add_argument("--fix", action="store_true")
- system/windowtabnotes/cli.py:37:overlay_debug_parser.add_argument("--fix-geometry", action="store_true")
- system/windowtabnotes/cli.py:39:sub.add_parser("active-window-watch-debug")
- browser-extension/dashboard.js:6:const response = await chrome.runtime.sendMessage({ type: "OPEN_DASHBOARD", focusSe
- browser-extension/dashboard.js:8:error: String(error),
RISK:
- browser-extension/content_script.js:13:element.remove();
- browser-extension/focus.js:9:return chrome.tabs.remove(tab.id);
- browser-extension/service_worker.js:135:async function removeOpenTab(tabId) {
- browser-extension/service_worker.js:138:delete snapshot[String(tabId)];
- browser-extension/service_worker.js:259:pendingTabSyncs.delete(key);
- browser-extension/service_worker.js:312:await chrome.tabs.remove(numericTabId);
- browser-extension/service_worker.js:410:chrome.tabs.onRemoved.addListener((tabId) => {
- browser-extension/service_worker.js:411:removeOpenTab(tabId).catch(() => {});
- browser-extension/service_worker.js:412:nativeMessage("REMOVE_TAB", { tabId }).catch(() => {});
- browser-extension/service_worker.js:414:delete state.tabBindings[String(tabId)];
ROAD:
now=system/windowtabnotes/cli.py:1:from __future__ import annotations
next=system/windowtabnotes/active_watch.py:1:from __future__ import annotations
later=system/windowtabnotes/api.py:1:from __future__ import annotations
LINK:
meta=../../../WindowTabNotes/dev/project.metadata.json
human=../../human/projects/windowtabnotes/overview.md
legacy=../../../WindowTabNotes/dev/legacy
repo=../../../WindowTabNotes
OPEN:
- no tests detected by static scan
