# codex-token-watcher Features

Questa pagina deriva dalla verifica runtime locale aggiornata al 2026-06-10.

## Mappa funzionale dal codice
- Poll orario via systemd user timer.
- Percorso normale CLI-only: `codex_cli_status_watcher.py once`.
- Health Codex da `codex --version`, `codex login status`, `codex doctor --json`.
- Quote da cache locale `~/.codex/sessions/**/*.jsonl` evento `token_count`, salvata in `cli_status_deep_observations`.
- `human-status --json` mostra `source`, `updated_at`, `age_seconds`, `stale`.
- Telegram quota breve: solo percentuali rimaste, variazione sopra soglia, reset locali `Europe/Copenhagen`.
- `CODEX_QUOTA_TELEGRAM_VERBOSE=1` riabilita formato tecnico/debug.
- Push Uptime Kuma remoto separato dal risultato Telegram.
- Backend Chrome/Playwright resta fallback manuale, non service normale.

## Confini operativi
- Non committare token, cookie, env o profilo Chromium.
- Runtime autorevole locale: `/home/daniele/codex-workspace/codex-token-watcher`.
- VM Oracle solo endpoint Kuma; non deve fare scraping della dashboard Codex.
