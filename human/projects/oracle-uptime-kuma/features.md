# Features

- Dashboard Uptime Kuma su Oracle VM.
- Monitor push per backup, audit, automazioni, spedizioni e freeze analysis.
- Una notifica Telegram condivisa (`id=1`) associata ai monitor non-gruppo.
- Status page `Mint Freeze Analysis` su slug `mint-freeze-analysis`, con monitor 13-17.
- DB SQLite ispezionabile in sola lettura via SSH.
- Backup DB sotto `/opt/uptime-kuma/backups` prima di ogni modifica.
- Monitor obsoleti disattivabili senza cancellare storico.
- Collegamento servizi locali tramite URL push segreti in env file fuori da Git.
- Verifica push tramite HTTP 200 e heartbeat fresco nel DB Kuma.
- Runbook AI completo in `ai/projects/oracle-uptime-kuma.md`.
