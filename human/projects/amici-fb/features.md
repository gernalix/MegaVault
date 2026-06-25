# amici_fb Features

## Funzioni principali

- Login/sessione Facebook tramite `fb_storage_state.json`.
- Refresh manuale della sessione con attesa automatica tramite `--login-wait-seconds`.
- Riconoscimento e diagnostica del selettore profilo Facebook.
- Estrazione amici Facebook con Playwright Chromium.
- Snapshot CSV in `data\amici_<timestamp>.csv`.
- Diff CSV in `data\diff_<precedente>_vs_<corrente>.csv`.
- Persistenza in `amici_fb.sqlite3`.
- Eccezioni profili da DB e `eccezioni.ini`.
- Diagnostica browser in `data\browser_diag_<timestamp>\`.
- Notifiche Telegram opzionali.
- Push Uptime Kuma opzionale dal runner.
- Esecuzione giornaliera via Windows Task Scheduler.

## File operativi

- `amici_fb.py`: scraping, snapshot, diff, SQLite.
- `telegram_notify.py`: notifiche Telegram e lettura `.env`.
- `amici_fb_task_runner.py`: wrapper con faulthandler e Uptime Kuma via `requests`.
- `amici_fb_daily.cmd`: launcher giornaliero Windows con log in `data\scheduler_logs\`.
- `install_windows_task.ps1`: registra il task giornaliero.
- `fb_storage_state.json`: runtime locale sensibile, ignorato e non da committare.

## Configurazione

I segreti stanno in `.env` o nelle variabili ambiente Windows. Non documentare
mai token Telegram, chat id reali, URL/token Uptime Kuma o cookie Facebook.
