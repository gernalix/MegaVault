# codex-token-watcher Troubleshooting

## Problemi e sintomi rilevati nel codice
- Parser v2 obsoleto: cercava contesti generici `usage/week/5h` e non salvava percentuali strutturate.
- Stato locale attuale: la diagnostica mostra pagina Cloudflare `Just a moment...`; finche' resta cosi', le quote reali non sono leggibili.
- Sintomo journal precedente: `dashboard loaded but expected Codex usage text was not visible`.

## Comandi/verifiche utili trovati
- `cd /home/daniele/codex-workspace/codex-token-watcher && ./codex_usage_monitor.py doctor`
- `cd /home/daniele/codex-workspace/codex-token-watcher && ./codex_usage_monitor.py once`
- `systemctl --user status codex-usage-monitor.service codex-usage-monitor.timer --no-pager`
- `journalctl --user -u codex-usage-monitor.service -n 80 --no-pager`
- `sqlite3 ~/.local/share/codex-usage-monitor/codex_usage.sqlite3 'select id,ts_utc,status,five_hour_percent,weekly_percent,error from observations order by id desc limit 5;'`

## Stato 2026-06-05
- Timer e DB sono sani, ma la pagina e' bloccata da Cloudflare/challenge: ultimo run id `71`, `2026-06-05T06:00:01Z`, `status=error`, titolo `Just a moment...`, Kuma `down:ok`.
- Diagnostica: `/home/daniele/.local/state/codex-usage-monitor/diagnostics/20260605T060053Z-dashboard-parse.{txt,html,png}`.
- Profilo Chrome corretto: `/home/daniele/.local/share/codex-usage-monitor/chrome-profile/Default`.
- Recovery manuale senza bypass:
  - `systemctl --user stop codex-usage-monitor.timer`
  - `cd /home/daniele/codex-workspace/codex-token-watcher && CODEX_USAGE_HEADLESS=0 ./codex_usage_monitor.py open-login`
  - risolvere Cloudflare/login nel browser aperto, verificare la pagina Codex Analytics, chiudere Chrome;
  - `./codex_usage_monitor.py doctor && ./codex_usage_monitor.py once`
  - `systemctl --user start codex-usage-monitor.timer`

## Safety prima di correggere
- Stop timer prima di login/debug profilo Chrome.
- VM Oracle non deve eseguire scraping Codex; lasciare `codex-usage-monitor.timer` disabilitato sulla VM.
- Non stampare env file o token Telegram/Kuma.
- Env file deve restare mode `600`.
- Non tentare bypass Cloudflare, stealth scraping o automazioni della challenge.

## Stato 2026-06-10
- Service normale: `codex_cli_status_watcher.py once`, non `codex_usage_monitor.py once`.
- Env richiesto: `CODEX_CLI_BIN=/home/daniele/.npm-global/bin/codex`; `/usr/bin/codex` e' obsoleto e fallisce la config corrente.
- Kuma monitor: id `10`, nome `codex-token-watcher`, tipo `push`, intervallo `4200s`, retry `300s`.
- Ultimo stato verificato: SQLite `cli_status_observations` id `4` `status=ok`, Codex `0.139.0`, WebSocket/provider `ok`; Kuma heartbeat remoto `status=1`.
- Se torna rosso: controllare prima `journalctl --user -u codex-usage-monitor.service -n 40 --no-pager`, poi `sqlite3 ~/.local/share/codex-usage-monitor/codex_usage.sqlite3 'select id,ts_utc,status,codex_bin,codex_version,error from cli_status_observations order by id desc limit 5;'`.
