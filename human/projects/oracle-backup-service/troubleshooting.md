# Oracle backup service — troubleshooting

La guida operativa corrente vive nel repository:

- [troubleshooting](../../../projects/oracle-backup-service/docs/human/troubleshooting.md)
- [runbook](../../../projects/oracle-backup-service/docs/ai/OPERATIONS.md)

Stato sano atteso:

- `last_backup_status=OK`;
- `last_successful_repo=rclone:oci:bucket-20260206-0730/oraclevm`;
- `last_failed_repos` e `last_remote_error` vuoti;
- `remote_retention_status=OK` o `SKIPPED_RECENT`;
- quota OCI sotto warning;
- backup, check e restore riusciti.

Non cancellare il fallback locale e non alzare le soglie per nascondere `REMOTE_DEGRADED`. Un URL Telegram completo in un errore deve essere trattato come esposizione di credenziale.
