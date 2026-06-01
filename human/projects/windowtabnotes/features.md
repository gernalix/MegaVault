# WindowTabNotes Features

Questa pagina deriva dal codice attivo auditato con `#604927`.

## Mappa funzionale dal codice
- `system/windowtabnotes/cli.py`: main, create_note_for_active_window, anchored_note_geometry, check_status
- `browser-extension/content_script.js`: cleanupLegacyUi, LEGACY_SELECTORS
- `browser-extension/dashboard.js`: openGlobalDashboard, statusEl, params, focusSearch, response
- `browser-extension/focus.js`: params
- `browser-extension/popup.js`: setStatus, setTabInfo, load, statusEl, tabInfoEl, openNoteEl, dashboardEl, searchEl
- `browser-extension/service_worker.js`: createEmptyState, sanitizeState, loadState, saveState, enqueueMutation, mutateState, nativeMessage, nativeError
- `system/windowtabnotes/active_watch.py`: OverlayController, sync_open_windows, active_note_for_current_context, handle_active_window, run_active_window_watch, active_window_watch_debug, _start_xprop_spy, _current_active_id
- `system/windowtabnotes/api.py`: handle_native_message, _record_from_tab, _tab_row, _is_internal_focus_tab, _require_dict, _require_str, _require_int, _error
- `system/windowtabnotes/config.py`: Settings, xdg_data_home, xdg_config_home, xdg_cache_home, data_dir, config_dir, cache_dir, db_path
- `system/windowtabnotes/daemon.py`: run_daemon
- `system/windowtabnotes/db.py`: now_ms, new_id, connect, db, init_db, migrate, get_schema_version, set_metadata
- `system/windowtabnotes/gtk_ui.py`: _gtk, open_note_window, open_dashboard, overlay_debug, dashboard_debug, _context_row, _populate_settings, _activate_context
- `system/windowtabnotes/logging_setup.py`: setup_logging
- `system/windowtabnotes/native_debug.py`: native_host_path, repo_root, native_manifest_paths, expected_manifest, run_native_debug, build_report, write_manifest, inspect_manifest
- `system/windowtabnotes/native_host.py`: main, _write, native_host_status, _record_start, _record_message, _read_metrics, _metrics_path, _metrics_lock_path
- `system/windowtabnotes/overlay_runtime.py`: overlay_lock, cleanup_overlays, cleanup_overlays_locked, list_overlay_processes, overlay_count, find_overlay_process, write_overlay_state, read_json_metadata
- `system/windowtabnotes/rofi.py`: SearchItem, RuntimeSearchState, refresh_runtime_contexts, run_search_launcher, install_search_launcher, run_global_search, _runtime_search_state, _build_search_items
- `system/windowtabnotes/shortcuts.py`: expected_command, install_shortcuts, shortcuts_status, print_shortcuts_status, _run, _run_optional, _xfsettingsd_running, _start_xfsettingsd
- `system/windowtabnotes/version.py`: version_label
- `system/windowtabnotes/windows.py`: WindowSnapshot, WindowGeometry, dependency_status, require_x11_tools, active_window, active_window_id, window_snapshot, is_manageable_window
- `system/scripts/install.sh`: usage

## Confini operativi
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
