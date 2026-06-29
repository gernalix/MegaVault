# Database

Path live: `/home/ubuntu/db/strano_anello.db`.

Prima intervento 2026-06-29:
- DB `6576418816` byte, WAL `10683192` byte.
- `page_size=4096`, `page_count=1605571`, `freelist_count=0`, `journal_mode=wal`.
- Tabella dominante: `watcher_comment_diagnostics` `6573776896` byte.
- Righe diagnostiche: `14693332`.

Dopo intervento:
- DB `2351104` byte, WAL `0`, SHM `32768`.
- `page_size=4096`, `page_count=574`, `freelist_count=0`, `journal_mode=wal`.
- `watcher_comment_diagnostics=102` righe, duplicate hash `0`.

Backup pre-intervento: `/var/lib/oracle_backup/manual_db_backups/strano_anello.pre-maintenance-20260629T145430Z.db.zst`, testato con `zstd -t`.
