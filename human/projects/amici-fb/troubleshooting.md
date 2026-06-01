# amici_fb Troubleshooting

## Problemi e sintomi rilevati nel codice
- _shared/telegram_notify.py:38:raise RuntimeError(
- _shared/telegram_notify.py:72:except Exception:
- _shared/telegram_notify.py:85:raise RuntimeError(f"{action} failed: HTTP {response.status_code}: {body}")
- _shared/telegram_notify.py:94:response = requests.post(_telegram_url("sendMessage"), json=payload, timeout=20)
- _shared/telegram_notify.py:104:timeout=20,
- _shared/telegram_notify.py:119:raise FileNotFoundError(str(path))
- _shared/telegram_notify.py:133:timeout=60,
- _shared/telegram_notify.py:160:parser.error("title and message are required unless --check is used")
- amici_fb.py:52:DEFAULT_NAVIGATION_TIMEOUT_MS = 120000
- amici_fb.py:53:POST_FRIENDS_GOTO_TIMEOUT_MS = 10000
- amici_fb.py:114:def exceptions_file_path() -> Path:
- amici_fb.py:183:def debug_rejected_csv_path(run_stamp: str):
- amici_fb.py:184:return str(output_dir_path() / f"debug_rejected_{run_stamp}.csv")
- amici_fb.py:187:def debug_cards_csv_path(run_stamp: str):
- amici_fb.py:188:return str(output_dir_path() / f"debug_cards_{run_stamp}.csv")
- amici_fb.py:245:self._thread.join(timeout=1.0)
- amici_fb_task_runner.py:18:KUMA_CONNECT_TIMEOUT_ENV = "UPTIME_KUMA_CONNECT_TIMEOUT_SECONDS"
- amici_fb_task_runner.py:29:def _failure_reason(exc: BaseException / str) -> str:

## Comandi/verifiche utili trovati
- install_ubuntu_autorun.sh:1:#!/usr/bin/env bash
- install_ubuntu_autorun.sh:7:PYTHON_BIN="$VENV_DIR/bin/python3"
- install_ubuntu_autorun.sh:12:python3 -m venv "$VENV_DIR"
- install_ubuntu_autorun.sh:22:systemctl --user daemon-reload
- install_ubuntu_autorun.sh:23:systemctl --user enable --now amici_fb.timer
- install_ubuntu_autorun.sh:27:systemctl --user start amici_fb.service
- install_ubuntu_autorun.sh:31:systemctl --user list-timers amici_fb.timer --no-pager

## Safety prima di correggere
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
