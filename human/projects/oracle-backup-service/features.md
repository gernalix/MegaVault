# Oracle backup service — funzionalità

- Backup Restic remoto su OCI Object Storage.
- Snapshot SQLite coerenti tramite online backup API.
- Fallback locale con quota rigida 7 GiB.
- Retention remota preventiva prima dell’upload, sotto lo stesso lock del backup.
- Quota remota, freschezza, spazio disco e stato retention monitorati.
- Registro incidenti SQLite con eventi append-only.
- Alert deduplicati e output di trasporto redatto.

Dettagli correnti: [documentazione proprietaria](../../../projects/oracle-backup-service/docs/ai/PROJECT.md).
