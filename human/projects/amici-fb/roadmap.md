# amici_fb Roadmap

## Segnali dal codice
- _shared/telegram_notify.py:10:from __future__ import annotations
- amici_fb_task_runner.py:4:from __future__ import annotations
- amici_fb_task_runner.py:92:faulthandler.dump_traceback_later(dump_seconds, repeat=True)
- telegram_notify.py:10:from __future__ import annotations

## Debito/rischi da considerare
- _shared/telegram_notify.py:38:raise RuntimeError(
- _shared/telegram_notify.py:72:except Exception:
- _shared/telegram_notify.py:85:raise RuntimeError(f"{action} failed: HTTP {response.status_code}: {body}")
- _shared/telegram_notify.py:94:response = requests.post(_telegram_url("sendMessage"), json=payload, timeout=20)
- _shared/telegram_notify.py:104:timeout=20,
- _shared/telegram_notify.py:119:raise FileNotFoundError(str(path))
- _shared/telegram_notify.py:133:timeout=60,
- _shared/telegram_notify.py:160:parser.error("title and message are required unless --check is used")
- fb_storage_state.json:1:{"cookies": [{"name": "dbln", "value": "%7B%22100014592815674%22%3A%222eEvA3fb%22%7D", "domain": ".facebook.com", "path": "/login/device-based/", "expires":
- _shared/telegram_notify.py:6:- TELEGRAM_BOT_TOKEN
- _shared/telegram_notify.py:22:TOKEN_ENV_NAMES = ("TELEGRAM_BOT_TOKEN",)
- _shared/telegram_notify.py:35:_, token = _first_env(TOKEN_ENV_NAMES)
- _shared/telegram_notify.py:37:if not token or not chat_id:
- _shared/telegram_notify.py:39:"Missing Telegram configuration: TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID must be set."
