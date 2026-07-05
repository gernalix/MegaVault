# Codex weekly limit monitor VM fix - 2026-07-05

STATUS=PASS
HOST=ubuntu@150.230.148.128
HOSTNAME=instance-20260201-1126
SERVICE=codex-weekly-limit-monitor.service
RUNTIME=/home/ubuntu/codex/automazione/codex_weekly_limit_monitor
HELPER=/home/ubuntu/telegram_notify.py

## Root Cause

Il monitor systemd era vivo ma non produceva letture valide. Usava `codex_binary=/opt/codex-native/bin/codex`, versione `codex-cli 0.120.0`. Quel binario chiamava `account/rateLimits/read`, ma falliva sulla risposta `https://chatgpt.com/backend-api/wham/usage` per `plan_type=prolite`: `unknown variant prolite`. Il body conteneva le quote reali, ma il codice trattava tutto come errore e scriveva nel log il body grezzo.

Telegram non era ripristinabile in modo sicuro perche' i valori reali erano nella vecchia copia hardcoded di `/home/ubuntu/telegram_notify.py`; `config.ini` conteneva placeholder `%TELEGRAM_BOT_TOKEN%` e `%TELEGRAM_CHAT_ID%`, e `/etc/codex-weekly-limit-monitor.env` era un template senza valori.

## Fix

- `/home/ubuntu/codex/automazione/codex_weekly_limit_monitor/codex_weekly_limit_watcher.py`
  - usa `/usr/bin/codex` tramite `config.ini`, versione `codex-cli 0.137.0`;
  - aggiunge parser robusto per payload `wham/usage` snake_case e fallback da errore JSON-RPC con body valido;
  - mantiene il parser del formato normale `rateLimits`;
  - separa fetch/parsing/stato/notifica gia' presenti e aggiunge sanitizzazione comune per log e stato;
  - rimuove `logger.exception` sui body grezzi e salva errori redatti.
- `/home/ubuntu/telegram_notify.py`
  - sostituito con helper riusabile senza token/chat_id hardcoded;
  - API compatibile: `send_text_raw`, `send_message`, `send_file`, `notify`, CLI `--check`;
  - usa env vars `TELEGRAM_BOT_TOKEN` e `TELEGRAM_CHAT_ID` o env file leggibili.
- `/etc/codex-weekly-limit-monitor.env`
  - migrati i valori dal vecchio helper hardcoded in env root-only;
  - permessi verificati `600`.
- `config.ini`
  - `codex_binary = /usr/bin/codex`;
  - `module_path = /home/ubuntu/telegram_notify.py`;
  - permessi portati a `600` perche' contiene placeholder/secret config.
- Backup creati in `/home/ubuntu/codex/automazione/codex_weekly_limit_monitor/backups/`; le copie backup del vecchio helper sono state redatte dopo la migrazione dei segreti.

## Tests

- `python3 -m py_compile codex_weekly_limit_watcher.py /home/ubuntu/telegram_notify.py test_watcher_local.py` -> PASS.
- `python3 test_watcher_local.py` su Windows mirror e su VM -> `local-tests: ok`.
- Dry-run senza Telegram reale:
  - comando: `python3 codex_weekly_limit_watcher.py --config /tmp/codex_weekly_dry.ini --once --console`;
  - risultato: `dry_state_status=success`;
  - quota letta: weekly_left `64.0`, five_hour_left `95.0`, source `codex-app-server`.
- Telegram import/config:
  - `telegram_notify.py --check` con env migrate -> `TELEGRAM_BOT_TOKEN set=True; TELEGRAM_CHAT_ID set=True`.
- Telegram reale:
  - messaggio controllato `Codex monitor Telegram test OK 2026-07-05` -> `telegram_send=ok`.
- Service run reale:
  - `systemctl start codex-weekly-limit-monitor.service`;
  - servizio `active (running)`;
  - lettura registrata: weekly_left `64.0%`, weekly_used `36.0%`, five_hour_left `94.0%`, five_hour_used `6.0%`;
  - `Telegram notification sent: weekly_left_change:2->64:2026-07-09T00:47:20+00:00`.
- Security scan perimetro monitor:
  - `email_matches=0`;
  - `user_id_matches=0`;
  - `telegram_bot_url_matches=0`;
  - `literal_bot_token_matches=0`.
- Scheduler/reboot safety:
  - `systemctl is-enabled codex-weekly-limit-monitor.service` -> `enabled`;
  - `systemctl is-active codex-weekly-limit-monitor.service` -> `active`;
  - `systemctl --failed` -> nessuna unita' fallita.

## Useful Commands

Manual run without daemon:

```bash
cd /home/ubuntu/codex/automazione/codex_weekly_limit_monitor
python3 codex_weekly_limit_watcher.py --config config.ini --once --console
```

Service status and logs:

```bash
systemctl status codex-weekly-limit-monitor.service --no-pager -l
journalctl -u codex-weekly-limit-monitor.service -n 80 --no-pager
tail -n 80 /home/ubuntu/codex/automazione/codex_weekly_limit_monitor/logs/codex_weekly_limit_monitor.log
```

Telegram helper check:

```bash
sudo systemctl restart codex-weekly-limit-monitor.service
python3 /home/ubuntu/telegram_notify.py --check
```

Note: il comando helper standalone richiede le env caricate; nel service path sono fornite da `/etc/codex-weekly-limit-monitor.env` e/o `config.ini`.

## Residual Risks

- `/opt/oracle_backup/lib/telegram_notify.py` e altri helper legacy VM risultavano storicamente hardcoded nell'audit Telegram; non sono stati modificati per non rompere altri workflow fuori scope.
- Il monitor dipende ancora dall'API sperimentale `codex app-server account/rateLimits/read`; il fallback `wham/usage` riduce il rischio, ma un cambio radicale del protocollo richiedera' un adapter nuovo.
- Nessun repo Git operativo e' collegato alla directory runtime del weekly monitor; il fix e' stato applicato live con backup, non con commit runtime.

## Follow-Up Hardening Prompts

- Migrare tutti gli helper Telegram VM legacy verso `/opt/megavault/telegram_notify.py` con env file root-only unico.
- Creare un repo Git per `codex_weekly_limit_monitor` o inserirlo in un repo MegaVault VM dedicato.
- Aggiungere un `--notify-test --dry-run/--force` nativo al watcher per test Telegram senza snippet esterni.
