# amici_fb Roadmap

## Ora

- Usare solo `C:\codex_clean_repos\amici_fb` come repository Git valido.
- Lasciare intatto `C:\codex\amici_fb` come export storico.
- Eseguire tramite Python globale e Task Scheduler Windows.
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
