# amici_fb Features

Questa pagina deriva dal codice attivo auditato con `#604927`.

## Mappa funzionale dal codice
- `_shared/telegram_notify.py`: _first_env, _config, validate_config, _masked, config_summary, fix_mojibake, _telegram_url, _raise_for_response
- `amici_fb.py`: DiagLogger, BrowserProcessWatcher, iso_utc_z, filename_stamp_utc, ensure_output_dir, project_path, output_dir_path, storage_state_path
- `amici_fb_task_runner.py`: _sanitize_log_text, _failure_reason, _push_url_base, push_kuma, main
- `telegram_notify.py`: _load_project_env, _first_env, _config, validate_config, _masked, config_summary, fix_mojibake, _telegram_url

## Confini operativi
- fb_storage_state.json:1:{"cookies": [{"name": "dbln", "value": "%7B%22100014592815674%22%3A%222eEvA3fb%22%7D", "domain": ".facebook.com", "path": "/login/device-based/", "expires":
- _shared/telegram_notify.py:6:- TELEGRAM_BOT_TOKEN
- _shared/telegram_notify.py:22:TOKEN_ENV_NAMES = ("TELEGRAM_BOT_TOKEN",)
- _shared/telegram_notify.py:35:_, token = _first_env(TOKEN_ENV_NAMES)
- _shared/telegram_notify.py:37:if not token or not chat_id:
- _shared/telegram_notify.py:39:"Missing Telegram configuration: TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID must be set."
- _shared/telegram_notify.py:41:return token, chat_id
- _shared/telegram_notify.py:57:token_name, token = _first_env(TOKEN_ENV_NAMES)
- _shared/telegram_notify.py:39:"Missing Telegram configuration: TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID must be set."
- amici_fb.py:70:"temporarily blocked",
- amici_fb.py:198:self._lock = threading.Lock()
- amici_fb.py:208:with self._lock:
