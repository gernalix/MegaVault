# Codex weekly limit notification format - 2026-07-05

STATUS=PASS
HOST=ubuntu@150.230.148.128
SERVICE=codex-weekly-limit-monitor.service
RUNTIME=/home/ubuntu/codex/automazione/codex_weekly_limit_monitor
HELPER=/home/ubuntu/telegram_notify.py

## Scope

Aggiornare il monitor VM delle quote Codex residue per includere nella notifica Telegram anche la finestra da 5 ore e convertire reset/deadline/last check in formato `dd/mm/yy hh:mm`.

## Changes

- `codex_weekly_limit_watcher.py`
  - aggiunta `format_display_timestamp(value)` con output `dd/mm/yy hh:mm`;
  - aggiunta `fmt_percent(value)` per fallback leggibile;
  - notifiche weekly ora includono sempre:
    - weekly precedente -> nuovo;
    - reset weekly formattato;
    - 5h precedente -> nuovo;
    - reset 5h formattato;
    - last check formattato;
  - se la quota 5h precedente non esiste, la notifica mostra `non disponibile -> valore (precedente non disponibile)`;
  - log user-facing `Recorded reading`, `Weekly reset changed`, `5h reset changed`, e chiavi evento Telegram usano formato leggibile.
- `test_watcher_local.py`
  - test formato timestamp;
  - test dry-run notifica;
  - test fallback 5h precedente non disponibile;
  - assert chiave evento senza ISO timestamp.

## Example Notification

```text
Codex weekly left changed.
Weekly left: 61% -> 60%
Weekly reset: 09/07/26 00:47
5h left: 95% -> 94%
5h reset: 05/07/26 18:55
Last check: 05/07/26 15:47
```

## Tests

- Local Windows mirror:
  - `python test_watcher_local.py` -> `local-tests: ok`.
- Oracle VM:
  - `python3 -m py_compile codex_weekly_limit_watcher.py test_watcher_local.py /home/ubuntu/telegram_notify.py` -> PASS.
  - `python3 test_watcher_local.py` -> `local-tests: ok`.
- Dry-run notifica:
  - output include weekly, 5h, reset weekly, reset 5h e last check in formato `dd/mm/yy hh:mm`.
- Notifica Telegram reale:
  - helper unico `/home/ubuntu/telegram_notify.py`;
  - env caricate da `/etc/codex-weekly-limit-monitor.env`;
  - test reale controllato -> `telegram_send=ok`.
- Scheduler:
  - `systemctl is-enabled codex-weekly-limit-monitor.service` -> `enabled`;
  - `systemctl is-active codex-weekly-limit-monitor.service` -> `active`.
- Log post-run:
  - `Recorded reading: weekly_left=60.0% weekly_used=40.0% weekly_reset=09/07/26 00:47 five_hour_left=64.0% five_hour_used=36.0% five_hour_reset=05/07/26 18:55 last_check=05/07/26 15:49 source=codex-app-server`.

## Security

- Nessun token/chat_id stampato nei comandi o nel report.
- `telegram_notify.py` resta helper unico per l'invio Telegram.
- Le credenziali restano fuori codice in `/etc/codex-weekly-limit-monitor.env`.

## Runtime State

Il servizio e' stato riavviato dopo il deploy ed e' risultato `enabled` e `active`. Il monitor non usa cron; il metodo operativo resta systemd service persistente.
