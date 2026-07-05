# Codex weekly limit monitor real 5h source fix - 2026-07-05

STATUS=PASS
HOST=ubuntu@150.230.148.128
SERVICE=codex-weekly-limit-monitor.service
RUNTIME=/home/ubuntu/codex/automazione/codex_weekly_limit_monitor
HELPER=/home/ubuntu/telegram_notify.py
CONFIG=/home/ubuntu/codex/automazione/codex_weekly_limit_monitor/config.ini

## Root Cause

La quota weekly era corretta ed era letta dal limite principale `rateLimits.secondary`.

La quota 5h era sbagliata per mappatura del campo JSON: il runtime stava leggendo `rateLimitsByLimitId.codex_bengalfox.primary`, che e' un limite reale ma corrisponde alla card separata `GPT-5.3-Codex-Spark Limite di utilizzo di 5 ore`, mostrata dalla UI al 100%. Non e' la card principale `Limite di utilizzo di 5 ore` che l'utente voleva monitorare.

Il dato corretto per la card principale e' `rateLimits.primary` nella risposta `account/rateLimits/read` del Codex app-server. Nel fallback `wham/usage` normalizzato corrisponde a `rate_limit.primary_window`.

Non sono stati trovati valori fake, fixture o percentuali hardcoded nella notifica runtime. L'errore era una source reale ma semanticamente sbagliata. Lo state precedente conteneva `last_five_hour_source=rateLimitsByLimitId.codex_bengalfox.primary (GPT-5.3-Codex-Spark)` e quindi e' stato ignorato come precedente valido dopo il cambio source.

## Fix

- `/home/ubuntu/codex/automazione/codex_weekly_limit_monitor/codex_weekly_limit_watcher.py`
  - weekly resta mappato a `rateLimits.secondary`;
  - 5h ora e' mappata esplicitamente a `rateLimits.primary (codex)`;
  - se `rateLimits.primary` manca o non e' una finestra da 300 minuti, la notifica mostra `5h left: unavailable`;
  - `codex_bengalfox` non viene piu' usato per la 5h principale;
  - il precedente 5h viene ignorato quando `last_five_hour_source` cambia, evitando confronti tra Spark e main quota;
  - i timestamp user-facing restano nel formato `dd/mm/yy hh:mm`.
- `/home/ubuntu/codex/automazione/codex_weekly_limit_monitor/test_watcher_local.py`
  - aggiunto test che fallisce se la 5h principale viene presa da `codex_bengalfox`/Spark;
  - aggiornati test su parser weekly, parser 5h, fallback `wham/usage`, dry-run notifica, timestamp, state/history e import `telegram_notify.py`.

`telegram_notify.py` resta l'unico helper Telegram e continua a essere caricato da `/home/ubuntu/telegram_notify.py`; token e chat id restano fuori dal codice.

## Live Evidence

Stato prima del fix definitivo:

```text
last_weekly_percent_left=58.0
last_five_hour_percent_left=100.0
last_five_hour_source=rateLimitsByLimitId.codex_bengalfox.primary (GPT-5.3-Codex-Spark)
```

Dry-run live post-fix con Telegram non usato:

```text
weekly_left=57.0
weekly_reset=09/07/26 00:47
five_hour_left=49%
five_hour_reset=05/07/26 18:55
five_hour_source=rateLimits.primary (codex)
source=codex-app-server
```

Run reale systemd post-fix:

```text
5h source changed: rateLimitsByLimitId.codex_bengalfox.primary (GPT-5.3-Codex-Spark) -> rateLimits.primary (codex)
Weekly percent left changed: 58.0% -> 57.0%
Telegram notification sent: weekly_left_change:58->57:09/07/26 00:47
Recorded reading: weekly_left=57.0% weekly_used=43.0% weekly_reset=09/07/26 00:47 five_hour_left=49% five_hour_used=51% five_hour_reset=05/07/26 18:55 five_hour_source=rateLimits.primary (codex) last_check=05/07/26 16:13 source=codex-app-server
```

Screenshot utente post-fix: UI Codex Analytics mostra `5h=49%` e `weekly=57%`, allineati allo state remoto.

State finale:

```text
last_success_at=2026-07-05T16:13:00+00:00
last_error=
last_weekly_percent_left=57.0
last_weekly_reset_at=2026-07-09T00:47:21+00:00
last_five_hour_percent_left=49.0
last_five_hour_reset_at=2026-07-05T18:55:45+00:00
last_five_hour_source=rateLimits.primary (codex)
last_notification_sent_at=2026-07-05T16:13:00+00:00
```

## Example Real Notification

Prima notifica reale post-fix:

```text
Codex weekly left changed.
Weekly left: 58% -> 57%
Weekly reset: 09/07/26 00:47
5h left: unavailable -> 49% (previous unavailable)
5h reset: 05/07/26 18:55
5h source: rateLimits.primary (codex)
Last check: 05/07/26 16:13
```

Il precedente 5h e' intenzionalmente `unavailable` solo nella prima notifica post-fix, perche' il precedente salvato proveniva dalla source Spark sbagliata. Dalla notifica successiva, con source invariata, il formato torna `valore precedente -> valore nuovo`.

## Tests

- Local Windows mirror:
  - `py -3 test_watcher_local.py` -> `local-tests: ok`.
- Oracle VM:
  - `python3 -m py_compile codex_weekly_limit_watcher.py test_watcher_local.py /home/ubuntu/telegram_notify.py` -> PASS.
  - `python3 test_watcher_local.py` -> `local-tests: ok`.
- Dry-run live:
  - `collect_reading()` via Codex app-server;
  - nessun invio Telegram;
  - 5h source `rateLimits.primary (codex)`;
  - valori allineati a UI: 5h `49%`, weekly `57%`.
- Real notification:
  - inviata dal servizio con configurazione Telegram gia' presente;
  - nessun token/chat id stampato.
- Scheduler:
  - `codex-weekly-limit-monitor.service` -> `enabled` e `active`;
  - `systemctl list-timers --all 'codex-weekly-limit-monitor*'` -> `0 timers listed`;
  - cron user/system cercati per questo monitor -> nessuna entry.
- Logging:
  - log file runtime: `/home/ubuntu/codex/automazione/codex_weekly_limit_monitor/logs/codex_weekly_limit_monitor.log`.

## Security

- Nessun token, cookie, Authorization header, chat_id o sessione Codex e' stato stampato nel report.
- Config Telegram redatta durante le verifiche.
- Scan nel perimetro `codex_weekly_limit_watcher.py`, `test_watcher_local.py`, `config.ini`, `data`, `logs` per pattern Telegram sensibili -> nessun match.
- Backup runtime creati prima del deploy:
  - `/home/ubuntu/codex/automazione/codex_weekly_limit_monitor/backups/codex_weekly_limit_watcher.py.bak.real5h-main.20260705T161148Z`
  - `/home/ubuntu/codex/automazione/codex_weekly_limit_monitor/backups/test_watcher_local.py.bak.real5h-main.20260705T161148Z`

## Useful Commands

```bash
cd /home/ubuntu/codex/automazione/codex_weekly_limit_monitor
python3 test_watcher_local.py
sudo systemctl status codex-weekly-limit-monitor.service --no-pager
journalctl -u codex-weekly-limit-monitor.service -n 80 --no-pager
tail -n 80 logs/codex_weekly_limit_monitor.log
python3 -m py_compile codex_weekly_limit_watcher.py test_watcher_local.py /home/ubuntu/telegram_notify.py
```

## Residual Risks

- Il reset della UI e' mostrato in timezone/browser locale, mentre il monitor conserva ISO UTC nello state e formatta user-facing in `dd/mm/yy hh:mm`. Il valore orario visualizzato resta allineato nel formato richiesto, ma il report operativo conserva anche l'ISO UTC nello state per debug.
- Se OpenAI cambia di nuovo il payload `account/rateLimits/read`, il monitor deve cadere su `5h left: unavailable` invece di inventare percentuali.

## Future Hardening Prompts

- Aggiungere snapshot JSON redatto periodico del payload Codex per audit parser, con retention breve.
- Aggiungere un alert distinto quando `rateLimits.primary` manca ma `codex_bengalfox` e' presente, cosi' si vede subito una divergenza tra main quota e quota Spark.
