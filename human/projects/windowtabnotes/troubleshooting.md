# WindowTabNotes Troubleshooting

## Problemi e sintomi rilevati nel codice
- system/windowtabnotes/cli.py:9:from .active_watch import active_note_for_current_context, active_window_watch_debug, sync_open_windows
- system/windowtabnotes/cli.py:12:from .gtk_ui import dashboard_debug, open_dashboard, open_note_window, overlay_debug
- system/windowtabnotes/cli.py:14:from .native_debug import run_native_debug
- system/windowtabnotes/cli.py:16:from .rofi import install_search_launcher, run_global_search, run_search_launcher, search_debug
- system/windowtabnotes/cli.py:35:overlay_debug_parser = sub.add_parser("overlay-debug")
- system/windowtabnotes/cli.py:36:overlay_debug_parser.add_argument("--fix", action="store_true")
- system/windowtabnotes/cli.py:37:overlay_debug_parser.add_argument("--fix-geometry", action="store_true")
- system/windowtabnotes/cli.py:39:sub.add_parser("active-window-watch-debug")
- browser-extension/dashboard.js:6:const response = await chrome.runtime.sendMessage({ type: "OPEN_DASHBOARD", focusSearch }).catch((error) => ({
- browser-extension/dashboard.js:8:error: String(error),
- browser-extension/dashboard.js:14:statusEl.textContent = response?.error // "Native Messaging host unavailable.";
- browser-extension/popup.js:18:const response = await chrome.runtime.sendMessage({ type: "GET_ACTIVE_TAB_RECORD" }).catch((error) => ({
- browser-extension/popup.js:20:error: String(error),
- browser-extension/popup.js:24:tabInfoEl.textContent = response?.error // "Native Messaging non configurato";
- browser-extension/service_worker.js:10:const NATIVE_FAILURE_BACKOFF_MS = 5000;
- browser-extension/service_worker.js:64:return { ok: false, skipped: true, error: { code: "native_backoff", message: "Native host backoff active." } };
- browser-extension/service_worker.js:68:const code = response?.error?.code // "";
- browser-extension/service_worker.js:70:nativeBackoffUntil = Date.now() + NATIVE_FAILURE_BACKOFF_MS;

## Comandi/verifiche utili trovati
- system/scripts/install.sh:1:#!/usr/bin/env bash
- system/scripts/install.sh:47:sudo apt-get install -y python3 python3-gi gir1.2-gtk-3.0 sqlite3 rofi wmctrl xdotool x11-utils jq
- system/scripts/install.sh:54:python3 - "$CONFIG_DIR/settings.json" "$EXTENSION_ID" <<'PY'
- system/scripts/install.sh:78:systemctl --user daemon-reload // true
- system/scripts/install.sh:79:systemctl --user enable --now windowtabnotes.service // true
- system/scripts/uninstall.sh:1:#!/usr/bin/env bash
- system/scripts/uninstall.sh:5:systemctl --user disable --now windowtabnotes.service 2>/dev/null // true
- system/scripts/uninstall.sh:9:systemctl --user daemon-reload 2>/dev/null // true

## Safety prima di correggere
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
- browser-extension/manifest.json:5:"version_name": "v20",
- system/windowtabnotes/cli.py:18:from .version import version_label
