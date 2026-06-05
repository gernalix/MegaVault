# codex-token-watcher Features

Questa pagina deriva dalla verifica runtime locale del 2026-06-02.

## Mappa funzionale dal codice
- Poll ogni 5 minuti via systemd user timer.
- Chrome persistente locale dedicato per `https://chatgpt.com/codex/cloud/settings/analytics#usage`.
- Parser v3 per blocchi `Saldo`, `Limite di utilizzo di 5 ore`, `Limite di utilizzo settimanale`, reset 5h e reset weekly.
- Storico in SQLite/CSV con migrazioni idempotenti.
- Stato atomico `last_weekly_percent.json`.
- Telegram solo quando `weekly_percent` cambia rispetto all'ultimo valore salvato; baseline iniziale silenziosa salvo env esplicito.
- Diagnostica HTML, screenshot e raw text su parsing/login/challenge failure.
- Push Uptime Kuma remoto `up` su ciclo leggibile e `down` su parsing fallito.

## Confini operativi
- Non committare token, cookie, env o profilo Chromium.
- Runtime autorevole locale: `/home/daniele/codex-workspace/codex-token-watcher`.
- VM Oracle solo endpoint Kuma; non deve fare scraping della dashboard Codex.
