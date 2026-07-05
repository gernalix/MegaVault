# Prompt 486219 Oracle Backup Fallback Quota
scope=oracle-backup-service;Oracle VM;local fallback quota;StorageLimitExceeded
host=ubuntu@150.230.148.128
date_utc=2026-06-13

CAUSE:
structural_cause=OCI object storage remains write-blocked by `StorageLimitExceeded`; oracle-backup therefore degraded to `/var/lib/oracle_backup/emergency_repo`.
failure_mode=local fallback repo lives on `/`; repeated fallback writes can consume root filesystem.
initial_root=`/dev/sda1 45G 44G 1.2G 98% /`
initial_backup_usage=`/var/lib/oracle_backup` 20G;`/var/lib/oracle_backup/emergency_repo` 14G;`/var/lib/oracle_backup/sqlite_snapshots` 5.2G
latest_growth_evidence=2026-06-12T23:03Z fallback added ~46MiB path data plus ~809MiB compressed `strano_anello.db` stream.

IMPLEMENTATION:
repo=/home/daniele/codex-workspace/projects/vm_oracle/oracle-backup-service
runtime=/opt/oracle_backup on Oracle VM
changed=backup.sh adds `check_local_fallback_quota` before local restic write.
changed=check_backup_health.py treats `BACKUP_BLOCKED_FALLBACK_QUOTA` or `local_fallback_quota_status=BLOCKED` as CRITICAL.
changed=oracle-backup-healthcheck.sh reports `local_fallback_quota` and backup_state CRITICAL when blocked.
changed=config/oracle_backup.env.example documents quota defaults.
deployed=/opt/oracle_backup/backup.sh;/opt/oracle_backup/check_backup_health.py;/usr/local/bin/oracle-backup-healthcheck.sh;/etc/oracle_backup/oracle_backup.env
backup_before_write=/home/ubuntu/maintenance-486219/before

CONFIG:
LOCAL_FALLBACK_MAX_GB=5
LOCAL_FALLBACK_SOFT_PCT=80
LOCAL_FALLBACK_PREWRITE_RESERVE_GB=1
LOCAL_FALLBACK_ROOT_MIN_FREE_GB=1
LOCAL_FALLBACK_ALERT_REMINDER_SECONDS=21600
state_files=/var/lib/oracle_backup/local_fallback_quota_status;/var/lib/oracle_backup/local_fallback_quota_last_error;/var/lib/oracle_backup/local_fallback_quota_state.json

BEHAVIOR:
remote_ok=normal restic remote success writes OK markers.
remote_storage_limit=remote is skipped/failed with `StorageLimitExceeded`; local fallback is considered only after all remote repos fail.
fallback_under_quota=backup writes to `/var/lib/oracle_backup/emergency_repo`; status `REMOTE_DEGRADED`; healthcheck WARNING/DEGRADED; soft 80% sends rate-limited warning.
fallback_over_quota=backup refuses local restic write; status `BACKUP_BLOCKED_FALLBACK_QUOTA`; healthcheck/monitor CRITICAL; exit non-zero controlled.
root_safety=local fallback will not start if repo is >=5G, repo+1G reserve would exceed 5G, or root free is <=1G.

CLEANUP:
deleted=none
remote_deleted=none
local_deleted=none
inventory=/home/ubuntu/maintenance-486219/reports/fallback_inventory_20260613T000454Z.txt
inventory_result=82 local fallback snapshots;restic raw-data 13.337GiB
next_cleanup_rule=offload/prune only after explicit plan; never delete remote; never delete local fallback ad hoc.

TESTS:
test=local shellcheck `scripts/backup.sh scripts/oracle-backup-healthcheck.sh` PASS
test=local `bash -n` + `python3 -m py_compile` PASS
test=remote `bash -n` + `py_compile` PASS
test=isolated 1M quota `/tmp` rc=1;status=BLOCKED;no restic write
test=isolated 5G quota `/tmp` rc=0;status=OK
test=live quota-only `FORCE_ORACLE_BACKUP=1 ORACLE_BACKUP_QUOTA_CHECK_ONLY=1 /opt/oracle_backup/backup.sh` rc=1;status=BLOCKED;last_backup_status=BACKUP_BLOCKED_FALLBACK_QUOTA
test=healthcheck dry-run reports `backup_state` CRITICAL and `local_fallback_quota` CRITICAL
test=monitor dry-run rc=1 with `BACKUP_BLOCKED_FALLBACK_QUOTA`
test=docker exec uptime-kuma true PASS
test=df `/` remains 98%;df `/run` 27%

KUMA:
changed=none
not_changed=Kuma hardening/admin/tunnel/push proxy/Telegram token/Kuma push URL
status=docker exec OK;Kuma container unaffected

CURRENT:
oracle_backup_service=inactive after controlled runs;timer active waiting next run
last_backup_status=BACKUP_BLOCKED_FALLBACK_QUOTA
local_fallback_quota_status=BLOCKED
root=/dev/sda1 45G 44G 1.2G 98%
run_tmpfs=96M 26M 70M 27%

VERIFY:
cmd=df -h /
cmd=sudo du -sh /var/lib/oracle_backup /var/lib/oracle_backup/emergency_repo /var/lib/oracle_backup/sqlite_snapshots 2>/dev/null
cmd=sudo cat /var/lib/oracle_backup/local_fallback_quota_status
cmd=sudo cat /var/lib/oracle_backup/local_fallback_quota_last_error
cmd=sudo python3 -m json.tool /var/lib/oracle_backup/local_fallback_quota_state.json
cmd=sudo ORACLE_BACKUP_HEALTHCHECK_DRY_RUN=1 /usr/local/bin/oracle-backup-healthcheck.sh
cmd=sudo BACKUP_MONITOR_DRY_RUN=1 /opt/oracle_backup/check_backup_health.py
cmd=journalctl -u oracle-backup.service -n 100 --no-pager
cmd=sudo docker exec uptime-kuma true
