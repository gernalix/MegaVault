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
- Autorita' corrente: [GLOBAL_INDEX](../../../ai/GLOBAL_INDEX.md), [Service Registry](../../../ai/global/SERVICE_REGISTRY.md) e [Alert Registry](../../../ai/global/ALERT_REGISTRY.md). Snapshot storico: [oracle-uptime-kuma](../../../ai/archive/projects_legacy/oracle-uptime-kuma.md).
