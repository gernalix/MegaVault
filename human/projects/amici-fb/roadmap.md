# amici_fb Roadmap

## Ora

- Usare solo `/home/daniele/projects/amici_fb` come checkout Git canonico.
- Trattare `C:\codex_clean_repos\amici_fb` e `C:\codex\amici_fb` come copie/runtime Windows esterne, non come branch operativi Fedora.
- Su Fedora eseguire tramite Python di sistema e `amici-fb.timer`; le istruzioni Task Scheduler restano storiche per Windows.
- Mantenere `.env` e `data\` fuori dal versionamento futuro.
- Tenere fuori dai commit `fb_storage_state.json`, `amici_fb.sqlite3`, log e
  output generati.

## Prossimi controlli

- Configurare `TELEGRAM_BOT_TOKEN` e `TELEGRAM_CHAT_ID` se si vogliono le notifiche Telegram.
- Verificare nei prossimi giorni i log in `data\scheduler_logs\`.
- Committare le modifiche pendenti dopo revisione: fix Task Scheduler/login e
  rimozione dal tracking di `data\`/`fb_storage_state.json`.
- Pushare solo dopo conferma esplicita.

## Non fare

- Non creare ambienti Python locali dentro il progetto.
- Non usare la `.git` dell'export Linux.
- Non pubblicare `.env`, cookie Facebook, token Telegram o URL/token Uptime Kuma.
