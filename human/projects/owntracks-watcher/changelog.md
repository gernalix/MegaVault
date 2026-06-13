# owntracks-watcher Changelog

## Eventi MegaVault
- 2026-06-13: `#739284` ha verificato live il runtime Oracle, ricostruito la configurazione Android OwnTracks e documentato endpoint HTTP Cloudflare, DB, servizio, test esterno e limiti auth/Kuma/Telegram.
- 2026-06-01: `#739482` ha migrato docs locali in `dev/legacy` e creato metadata/MegaVault.
- 2026-06-01: `#842915` ha arricchito AI/Human docs da legacy e repo structure.
- 2026-06-01T13:39:31+02:00: `#604927` ha auditato codice attivo, arricchito Human docs e compresso AI doc.

## Evidenza audit
- Test reale #739284: POST esterno a `https://owntracks.danielegalati.com/owntracks` ha restituito HTTP 200 e scritto `positions.id=321333`, `moves.id=7341` nel DB `/home/ubuntu/sync_root/db/owntracks.db`.
- Runtime #739284: `owntracks-http-server.service` attivo su `8083`; `cloudflared.service` inoltra `owntracks.danielegalati.com` a `127.0.0.1:8083`; nessun monitor Kuma OwnTracks dedicato verificato.
