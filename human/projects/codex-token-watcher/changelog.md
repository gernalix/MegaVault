# codex-token-watcher Changelog

## Eventi MegaVault
- 2026-06-01: `#739482` ha migrato docs locali in `dev/legacy` e creato metadata/MegaVault.
- 2026-06-01: `#842915` ha arricchito AI/Human docs da legacy e repo structure.
- 2026-06-01T13:39:31+02:00: `#604927` ha auditato codice attivo, arricchito Human docs e compresso AI doc.
- 2026-06-02: spostata architettura finale sul PC Linux Mint locale; VM Oracle lasciata solo come endpoint Kuma. Parser Analytics v3 per 5h/weekly percent, reset, stato weekly atomico, Telegram solo su cambio weekly, diagnostica raw/html/png e Uptime Kuma up/down.

## Evidenza audit
- Runtime autorevole verificato: `/home/daniele/codex-workspace/codex-token-watcher`.
- Blocco attuale: Cloudflare `Just a moment...` impedisce lettura live quote locale finche' il profilo Chrome dedicato non viene verificato.
- 2026-06-10 `#482913`: riparato monitor Kuma rosso. Cause verificate: backend browser systemd spingeva `down` per Cloudflare `Just a moment...`; monitor Kuma id `10` aveva intervallo `60s` incompatibile con timer orario; systemd usava `/usr/bin/codex` `0.128.0` invece di `/home/daniele/.npm-global/bin/codex` `0.139.0`; push CLI duplicava query `status/msg/ping`. Stato finale: service CLI-only, Kuma interval `4200s`, heartbeat remoto `status=1`.
- 2026-06-10 `#914672`: semplificata notifica Telegram quota: default breve, solo percentuali rimaste, variazioni sopra soglia, reset locali; debug tecnico dietro `CODEX_QUOTA_TELEGRAM_VERBOSE=1`. Verificato che le quote arrivano da cache locale `token_count`, non da CLI live o dashboard browser.
