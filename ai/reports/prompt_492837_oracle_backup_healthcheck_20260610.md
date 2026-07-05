# Prompt 492837 - oracle-backup healthcheck CRITICAL

prompt=492837
host=ubuntu@150.230.148.128
date_utc=2026-06-10
scope=oracle-backup CRITICAL last_any_success_epoch stale + no valid local fallback

## Guardrail
- no_deleted=backup,repo,snapshot,log,DB
- no_prune_forget_compact=yes
- no_reboot=yes
- no_threshold_silencing=yes
- no_manual_success_marker=yes
- read_only_phase_completed_before_fix=yes

## Root Cause
- Timers and services were active; backup jobs started regularly.
- The job failed before restic fallback on SQLite snapshot creation: `Error: database or disk is full`.
- `/var/lib/oracle_backup/sqlite_snapshots` retained one valid snapshot dir (`20260608_180131`) at ~4.9GiB and `/` had only ~4.7GiB free.
- Creating a second on-disk SQLite backup of `/home/ubuntu/db/strano_anello.db` (~4.9GiB) exhausted root before any new restic fallback success marker could be written.
- Remote OCI remained `StorageLimitExceeded`, so freshness depended on local fallback; once local snapshot creation failed, `last_any_success_epoch` and `last_local_fallback_success_epoch` aged past thresholds.

## Diagnosis
- `oracle-backup.timer`: enabled/active; next run observed.
- `oracle-backup.service`: failed repeatedly with `database or disk is full`.
- `oracle-backup-healthcheck.service`: pre-fix CRITICAL on `backup_state`.
- `oracle-backup-monitor.service`: pre-fix CRITICAL freshness path; post-fix WARNING.
- `oracle-backup-remote-quota.service`: remote quota status CRITICAL.
- Emergency repo existed/readable/writable: `/var/lib/oracle_backup/emergency_repo`.
- Emergency repo locks: no lock files observed in read-only lock listing.
- State before fix: `last_any_success_epoch=1780942379`, `last_local_fallback_success_epoch=1780942379`, age ~170k seconds, status `REMOTE_DEGRADED`.
- Disk before fix: `/` ~90-91%, `/var/lib/oracle_backup` ~16G, `sqlite_snapshots` ~5.0G, `emergency_repo` ~11G.

## Fix
- Modified live `/opt/oracle_backup/backup.sh`.
- Low-space auto mode now avoids creating another full SQLite snapshot directory.
- In stream mode, path backup excludes live SQLite `*.db`, `*.db-wal`, `*.db-shm` under `DB_ROOTS`.
- SQLite DBs are backed up into restic as compressed SQL dumps via `sqlite3 ".dump" | gzip -c | restic backup --stdin --stdin-filename .../*.db.sql.gz`.
- Existing retained snapshot directory was preserved; no old snapshot was deleted.
- A first uncompressed stream attempt was stopped at `/` 96%/2.0GiB free to avoid full disk; no marker was written from that interrupted attempt.

## Runtime Backups
- `/opt/oracle_backup/backups/prompt492837-20260610T174229Z/backup.sh`; manifest `/opt/oracle_backup/backups/prompt492837-20260610T174229Z/MANIFEST.txt`; original sha `2d0898595dbeb825f1f86b1d16bbf88c8591ab6a3524ded79f34b5f2e24dff38`; installed sha `3ccb7a1512c967a7dda39d7976a0a786af982e4d82d5452581b02880b5f219f0`.
- `/opt/oracle_backup/backups/prompt492837-20260610T180906Z/backup.sh`; manifest `/opt/oracle_backup/backups/prompt492837-20260610T180906Z/MANIFEST.txt`; original sha `3ccb7a1512c967a7dda39d7976a0a786af982e4d82d5452581b02880b5f219f0`; installed sha `0323dc7a92da3a4d40977a7f3ed9b22d7dfdce5d02d2bbdbd959047b664a4201`.
- `/opt/oracle_backup/backups/prompt492837-20260610T182138Z/backup.sh`; manifest `/opt/oracle_backup/backups/prompt492837-20260610T182138Z/MANIFEST.txt`; original sha `0323dc7a92da3a4d40977a7f3ed9b22d7dfdce5d02d2bbdbd959047b664a4201`; installed sha `0d029e20e5fb790875ded7759c90aed3c60d9d9c277211a6aa1ee84043af1944`.

## MegaVault Backups
- `/home/daniele/codex-workspace/MegaVault/ai/reports/prompt_492837_backups_20260610T184700Z/oracle-backup-service.md`.
- `/home/daniele/codex-workspace/MegaVault/ai/reports/prompt_492837_backups_20260610T184700Z/changelog.md`.
- `/home/daniele/codex-workspace/MegaVault/ai/reports/prompt_492837_backups_20260610T184700Z/MANIFEST.txt`.

## Verification
- `sudo systemctl start oracle-backup.service`: exit 0 on final run.
- Final backup log: `/var/log/oracle_backup/backup_20260610_182157.log`.
- Final backup result: `backup REMOTE_DEGRADED with repo_success=1 repo_fail=1`.
- Final state:
  - `last_any_success_epoch=1781117071`.
  - `last_local_fallback_success_epoch=1781117071`.
  - `last_successful_repo=/var/lib/oracle_backup/emergency_repo`.
  - `last_failed_repos=rclone:oci:bucket-20260206-0730/oraclevm`.
  - `last_backup_status=REMOTE_DEGRADED`.
  - `last_remote_error=StorageLimitExceeded during write preflight`.
  - `local_fallback_retention_status=OK`.
- `sudo systemctl start oracle-backup-healthcheck.service`: exit 0.
- Post-fix healthcheck backup_state: `WARNING`, not `CRITICAL`.
- Post-fix healthcheck detail: `REMOTE_DEGRADED: quota remota piena, fallback locale valido; any_success_age=88s; local_fallback_age=88s`.
- `sudo systemctl start oracle-backup-monitor.service`: exit 0; `WARNING`, rate-limited, fallback locale valido.
- Timers verified: `oracle-backup.timer`, `oracle-backup-monitor.timer`, `oracle-backup-healthcheck.timer`, `oracle-backup-localprune.timer`, `oracle-backup-remote-quota.timer`, `oracle-backup-prune.timer`.

## Remaining Degradation
- Remote OCI is still full/degraded: `remote_quota_state.json` current status `CRITICAL`, path `oci:bucket-20260206-0730`, used `22.262 GBytes` / assumed limit `22GiB`.
- Healthcheck still reports root storage alerts: `/` 91%, 4.1GiB free after final run.
- Emergency repo grew during failed/successful attempts; final observed size ~12G, below 20GiB warning threshold.

## Future Verification Commands
- `sudo systemctl start oracle-backup.service && systemctl status oracle-backup.service --no-pager --lines=80`
- `sudo systemctl start oracle-backup-healthcheck.service && systemctl status oracle-backup-healthcheck.service --no-pager --lines=80`
- `sudo python3 -m json.tool /var/lib/oracle_backup/healthcheck_alert_state.json`
- `systemctl list-timers 'oracle-backup*' --all --no-pager`
- `df -h / /var/lib/oracle_backup /home /var/log`
