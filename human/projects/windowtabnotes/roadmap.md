# WindowTabNotes Roadmap

## Segnali dal codice
- system/windowtabnotes/cli.py:1:from __future__ import annotations
- system/windowtabnotes/active_watch.py:1:from __future__ import annotations
- system/windowtabnotes/api.py:1:from __future__ import annotations
- system/windowtabnotes/config.py:1:from __future__ import annotations
- system/windowtabnotes/daemon.py:1:from __future__ import annotations
- system/windowtabnotes/db.py:1:from __future__ import annotations
- system/windowtabnotes/gtk_ui.py:1:from __future__ import annotations
- system/windowtabnotes/gtk_ui.py:233:next_x = max(0, min(int(event.x_root) - dragging["dx"], screen_w - 40))
- system/windowtabnotes/gtk_ui.py:234:next_y = max(0, min(int(event.y_root) - dragging["dy"], screen_h - 30))
- system/windowtabnotes/gtk_ui.py:235:win.move(next_x, next_y)
- system/windowtabnotes/gtk_ui.py:366:associated_context = next(
- system/windowtabnotes/gtk_ui.py:661:context = next((entry for entry in entries if entry["context_id"] == note["context_id"] and entry["context_type"] == note["context_type"]), {})

## Debito/rischi da considerare
- system/windowtabnotes/cli.py:9:from .active_watch import active_note_for_current_context, active_window_watch_debug, sync_open_windows
- system/windowtabnotes/cli.py:12:from .gtk_ui import dashboard_debug, open_dashboard, open_note_window, overlay_debug
- system/windowtabnotes/cli.py:14:from .native_debug import run_native_debug
- system/windowtabnotes/cli.py:16:from .rofi import install_search_launcher, run_global_search, run_search_launcher, search_debug
- system/windowtabnotes/cli.py:35:overlay_debug_parser = sub.add_parser("overlay-debug")
- system/windowtabnotes/cli.py:36:overlay_debug_parser.add_argument("--fix", action="store_true")
- system/windowtabnotes/cli.py:37:overlay_debug_parser.add_argument("--fix-geometry", action="store_true")
- system/windowtabnotes/cli.py:39:sub.add_parser("active-window-watch-debug")
- browser-extension/content_script.js:13:element.remove();
- browser-extension/focus.js:9:return chrome.tabs.remove(tab.id);
- browser-extension/service_worker.js:135:async function removeOpenTab(tabId) {
- browser-extension/service_worker.js:138:delete snapshot[String(tabId)];
- browser-extension/service_worker.js:259:pendingTabSyncs.delete(key);
- browser-extension/service_worker.js:312:await chrome.tabs.remove(numericTabId);
