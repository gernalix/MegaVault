# Prompt 918472 Oracle Backup Fallback Cleanup
scope=oracle-backup-service;Oracle VM;local fallback cleanup;StorageLimitExceeded
host=ubuntu@150.230.148.128
date_utc=2026-06-13

CONTEXT:
structural_fix=prompt 486219 already enforces local fallback quota before restic writes.
remote_state=OCI object storage still returns `StorageLimitExceeded`; remote backups remain degraded.
target=/var/lib/oracle_backup/emergency_repo
maintenance_dir=/home/ubuntu/maintenance-918472
rule=cleanup operated only on the local fallback restic repo; no remote restic repo was targeted.

BEFORE:
root=`/dev/sda1 45G 44G 1.2G 98% /`
emergency_repo_physical=14G
emergency_repo_raw_data=13.337GiB
local_snapshots=82
inventory_existing=/home/ubuntu/maintenance-486219/reports/fallback_inventory_20260613T000454Z.txt
inventory_new=/home/ubuntu/maintenance-918472/reports/snapshots_before.json

PLAN:
plan_file=/home/ubuntu/maintenance-918472/reports/cleanup_plan_readonly.txt
candidate_keep_latest_3_complete_runs=23 snapshots;9.859GiB raw-data;above quota
candidate_keep_latest_2_complete_runs=22 snapshots;4.643GiB raw-data;initial least-invasive attempt
candidate_keep_latest_1_complete_run=11 snapshots;3.805GiB raw-data;final physical repo below quota after prune
safety=oracle-backup.timer stopped only during local forget/prune windows and restarted afterward.

CLEANUP_COMMANDS:
cmd=sudo systemctl stop oracle-backup.timer
cmd=restic -r /var/lib/oracle_backup/emergency_repo forget <non-kept-local-snapshot-ids>
cmd=restic -r /var/lib/oracle_backup/emergency_repo prune --max-repack-size 512M
cmd=restic -r /var/lib/oracle_backup/emergency_repo forget <second-pass-local-snapshot-ids>
cmd=restic -r /var/lib/oracle_backup/emergency_repo prune --max-repack-size 4G
cmd=restic -r /var/lib/oracle_backup/emergency_repo prune --max-unused 0
cmd=sudo systemctl start oracle-backup.timer
remote_touched=no
remote_deleted=no
local_target_only=yes

LOGS:
log=/home/ubuntu/maintenance-918472/logs/cleanup_20260613T003615Z.log
log=/home/ubuntu/maintenance-918472/logs/cleanup_second_20260613T003741Z.log
log=/home/ubuntu/maintenance-918472/logs/cleanup_compact_20260613T004104Z.log
log=/home/ubuntu/maintenance-918472/logs/restic_check_20260613T004445Z.log

AFTER:
root=`/dev/sda1 45G 34G 12G 75% /`
emergency_repo_physical=3.9G
emergency_repo_raw_data=3.805GiB
local_snapshots=11
snapshot_window=2026-06-12T23:01:50Z..2026-06-12T23:04:04Z
snapshots_after=/home/ubuntu/maintenance-918472/reports/snapshots_after.json
space_freed_physical=about 10G from emergency_repo;root recovered about 11G free.

FINAL_QUOTA:
local_fallback_quota_status=OK
quota_detail=local fallback quota OK: repo 3.81 GiB < soft 4.00 GiB, hard 5.00 GiB; root free 11.30 GiB
fallback_quota=LOCAL_FALLBACK_MAX_GB=5
soft_threshold=LOCAL_FALLBACK_SOFT_PCT=80
prewrite_reserve=LOCAL_FALLBACK_PREWRITE_RESERVE_GB=1

HEALTHCHECK:
restic_check=PASS;`no errors were found`
healthcheck_dry_run=rc 0;WARNING `REMOTE_DEGRADED: remote failed; local fallback valid`
monitor_dry_run=rc 0;WARNING `REMOTE_DEGRADED`
oracle_backup_service=inactive;not failed after reset
oracle_backup_timer=active
docker_kuma=`sudo docker exec uptime-kuma true` PASS

CODE_ADJUSTMENT:
repo=/home/daniele/codex-workspace/projects/vm_oracle/oracle-backup-service
changed=scripts/check_backup_health.py and scripts/oracle-backup-healthcheck.sh now treat stale `BACKUP_BLOCKED_FALLBACK_QUOTA` as CRITICAL only when current fallback quota is still not OK.
reason=after cleanup, `local_fallback_quota_status=OK` plus valid local fallback should report WARNING/REMOTE_DEGRADED, not stale quota CRITICAL.
deployed=/opt/oracle_backup/check_backup_health.py;/usr/local/bin/oracle-backup-healthcheck.sh
backup_before_deploy=/home/ubuntu/maintenance-918472/before/20260613T004358Z

VERIFY:
cmd=df -h /
cmd=sudo du -sh /var/lib/oracle_backup/emergency_repo
cmd=sudo restic -r /var/lib/oracle_backup/emergency_repo snapshots --tag oracle-vm
cmd=sudo restic -r /var/lib/oracle_backup/emergency_repo check
cmd=sudo ORACLE_BACKUP_DISABLE_TELEGRAM=1 ORACLE_BACKUP_QUOTA_CHECK_ONLY=1 /opt/oracle_backup/backup.sh
cmd=sudo ORACLE_BACKUP_HEALTHCHECK_DRY_RUN=1 /usr/local/bin/oracle-backup-healthcheck.sh
cmd=sudo BACKUP_MONITOR_DRY_RUN=1 /opt/oracle_backup/check_backup_health.py
cmd=sudo docker exec uptime-kuma true

OPEN:
open=OCI remote capacity remains unresolved. The system is now degraded but controlled; local fallback can run only while quota and root-free preflight pass.
