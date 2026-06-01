# facebook-video-archiver Features

Questa pagina deriva dal codice attivo auditato con `#604927`.

## Mappa funzionale dal codice
- `facebook_archive_dashboard.py`: human_bytes, count_files_and_bytes, read_urls, recent_log, tail_lines, process_status, active_part_file, parse_progress
- `facebook_session_browser.py`: expand, load_env_file, safe_print, normalize_facebook_url, read_existing_urls, write_deduped_urls, write_json, read_checkpoint
- `facebook_video_archiver.sh`: usage, log, die, load_env, require_archive_mount, rel_or_abs, mask_path, expand_path

## Confini operativi
- facebook_archive_dashboard.py:124:if any(token in line.lower() for token in ("warning", "error", "failed", "unsupported", "unable")):
- facebook_session_browser.py:5:import http.cookiejar
- facebook_session_browser.py:17:DEFAULT_COOKIE_EXPORT = "~/.config/facebook-video-archiver/facebook-cookies.txt"
- facebook_session_browser.py:133:cookies = await context.cookies("https://www.facebook.com")
- facebook_session_browser.py:134:cookie_names = {cookie.get("name", "") for cookie in cookies}
- facebook_session_browser.py:135:if "c_user" in cookie_names or "xs" in cookie_names:
- facebook_session_browser.py:205:safe_print("Nessun URL trovato. Possibili limiti: cookie/sessione scaduti, checkpoint, rendering Facebook non estraibile, contenuto privato/non auto
- facebook_session_browser.py:339:def cookie_expires(cookie: dict) -> int:
- dev/project.metadata.json:9:"metadata_version": 1,
- facebook_session_browser.py:43:def safe_print(message: str) -> None:
- facebook_session_browser.py:101:safe_print(f"ERROR: Playwright is not available in this environment: {exc}")
- facebook_session_browser.py:102:safe_print("Run: ./facebook_video_archiver.sh --setup")
