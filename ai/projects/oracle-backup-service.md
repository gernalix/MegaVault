META:
name=oracle-backup-service
slug=oracle-backup-service
path=/home/daniele/codex-workspace/projects/vm_oracle/oracle-backup-service
remote=https://github.com/gernalix/oracle-backup-service.git
branch=fix/degraded-healthcheck-state
verified_commit=18f7e1f
verified_at=2026-06-29T13:55:44Z
protocol=MEGAVAULT_PROTOCOL.md:v3
PURPOSE:
purpose=Restic-based Oracle VM backup service. It backs up `/home/ubuntu`, `/etc`, and SQLite DBs; when remote OCI is full it uses `/var/lib/oracle_backup/emergency_repo` with enforced retention and healthcheck state.
STACK:
lang=Python,Shell
fw=UNKNOWN
db=SQLite
platform=UNKNOWN
tools=restic,systemd
MAP:
entry=UNKNOWN
ui=UNKNOWN
core=dev/project.metadata.json
db=scripts/backup.sh,scripts/check_backup_health.py,scripts/oracle-backup-healthcheck.sh,scripts/prune_local_snapshots.sh,systemd/oracle-backup-healthcheck.service
tests=UNKNOWN
scripts=scripts/check_remote_quota.py,scripts/prune.sh
build=UNKNOWN
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
data=scripts/backup.sh:heartbeat_loop,cleanup_failed_snapshot,cleanup_on_exit,snapshot_one_db,record_remote_failure,record_remote_skip
data=scripts/check_backup_health.py:load_env_file,read_text,read_epoch,notify,int_cfg,load_json
data=scripts/prune_local_snapshots.sh:bytes_from_gb,snapshot_dirs,count_dirs,total_bytes,free_bytes,delete_oldest
script=scripts/check_remote_quota.py:load_env,parse_gb,run_rclone_size,read_state,write_state,fmt_gib
component=backup.sh orchestrates remote preflight, SQLite snapshot/stream, restic backup, local fallback, retention, success markers.
component=oracle-backup-healthcheck.sh read-only preventive checker; reports root, snapshot, fallback quota, backup_state, retention, strano growth.
component=check_backup_health.py freshness monitor; distinguishes OK, REMOTE_DEGRADED fallback valid, BACKUP_BLOCKED_FALLBACK_QUOTA.
component=prune.sh remote+fallback restic forget/prune under RESTIC_RUN_LOCK.
component=check_remote_quota.py read-only rclone size monitor writing remote_quota_state.json.
FLOW:
flow=script->scripts/check_remote_quota.py=>scripts/backup.sh
flow=data->scripts/backup.sh
flow=scripts/backup.sh:4:ENV_FILE="/etc/oracle_backup/oracle_backup.env"
flow=scripts/backup.sh:5:STATE_DIR="/var/lib/oracle_backup"
flow=scripts/backup.sh:6:LOG_DIR="/var/log/oracle_backup"
flow=fallback_quota=backup.sh runs LOCAL_FALLBACK retention before refusing BACKUP_BLOCKED_FALLBACK_QUOTA and forces retention again after successful local fallback.
flow=remote_ok: rclone preflight OK -> sqlite disk/stream decision -> restic remote backup -> last_remote_success_epoch + last_backup_status=OK/DEGRADED.
flow=remote_full: StorageLimitExceeded -> cooldown records last_remote_error/failure_epoch -> fallback quota check -> forced fallback retention if needed -> local fallback backup.
flow=fallback_success: last_any_success_epoch + last_local_fallback_success_epoch + last_successful_repo=emergency_repo -> forced fallback retention -> quota state refresh -> last_backup_status=REMOTE_DEGRADED.
flow=quota_check_only: ORACLE_BACKUP_QUOTA_CHECK_ONLY=1 bypasses MIN_BACKUP_INTERVAL_SECONDS and only refreshes local_fallback_quota_state.
INV:
arch=scripts/backup.sh:heartbeat_loop,cleanup_failed_snapshot,cleanup_on_exit,snapshot_one_db,record_remote_failure; scripts/check_backup_health.py:load_env_file,read_text,read_epoch,notify,int_cfg; scripts/prune_local_snapshots.sh:bytes_from...
data=scripts/oracle-backup-healthcheck.sh:5:LEGACY_STATE_FILE="${ORACLE_BACKUP_HEALTHCHECK_STATE_FILE:-/var/lib/oracle_backup/healthcheck_state.json}"; systemd/oracle-backup-healthcheck.service:2:Description=Oracle backup preventive healthcheck
ux=scripts/oracle-backup-healthcheck.sh:82:echo "[ERROR] could not acquire healthcheck alert lock: $HEALTHCHECK_ALERT_LOCK_FILE" >&2; scripts/check_backup_health.py:94:["systemctl", "is-active", "--quiet", name],
backup=scripts/backup.sh:4:ENV_FILE="/etc/oracle_backup/oracle_backup.env"; scripts/backup.sh:5:STATE_DIR="/var/lib/oracle_backup"
backup=LOCAL_FALLBACK_QUOTA_CHECK_ONLY must bypass MIN_BACKUP_INTERVAL_SECONDS; quota check updates /var/lib/oracle_backup/local_fallback_quota_state.json without starting backup.
backup=If remote StorageLimitExceeded and fallback quota projected full, run configured restic retention first; block only if quota still fails after retention.
backup=Never report BACKUP_BLOCKED_FALLBACK_QUOTA while configured local fallback retention can recover enough space.
backup=After any successful local fallback write, force local fallback retention before final quota state refresh.
backup=Healthcheck is read-only: no deletion, no restart, no unlock/prune.
data=last_any_success_epoch records any successful repo; last_remote_success_epoch remote only; last_local_fallback_success_epoch fallback only.
data=last_backup_status=REMOTE_DEGRADED is valid when remote fails but local fallback success is recent.
security=Do not store SSH key contents or RESTIC_PASSWORD in MegaVault.
migration=UNKNOWN
version=dev/project.metadata.json:9:"metadata_version": 1,
i18n=UNKNOWN
security=scripts/backup.sh:24:export RESTIC_PASSWORD; scripts/prune.sh:13:export RESTIC_PASSWORD
access=vm_host=ubuntu@150.230.148.128; hostname=instance-20260201-1126; ssh_key_primary_windows=C:\Users\seste\Downloads\Telegram Desktop\ssh-key-2026-02-01.key; do_not_store_key_contents.
access=ssh_cmd=ssh -i "C:\Users\seste\Downloads\Telegram Desktop\ssh-key-2026-02-01.key" -o IdentitiesOnly=yes ubuntu@150.230.148.128
access=windows_acl_note=OpenSSH may reject primary key if ACL too open; fix/copy with restrictive ACL or use validated maintenance key C:\Users\seste\Documents\windows\maintenance\ssh\oracle-uptime-kuma-reset.key.
perf=scripts/backup.sh:8:RESTIC_RUN_LOCK="$STATE_DIR/restic-job.lock"; scripts/backup.sh:16:BACKUP_HEARTBEAT_FILE="$STATE_DIR/backup_heartbeat_epoch"
BUILD:
files=UNKNOWN
cmd=UNKNOWN
TEST:
files=UNKNOWN
cmd=UNKNOWN
DATA:
db=scripts/backup.sh:7:SQLITE_SNAP_DIR="$STATE_DIR/sqlite_snapshots"; scripts/backup.sh:19:mkdir -p "$STATE_DIR" "$LOG_DIR" "$SQLITE_SNAP_DIR"
paths=scripts/backup.sh:4:ENV_FILE="/etc/oracle_backup/oracle_backup.env"; scripts/backup.sh:5:STATE_DIR="/var/lib/oracle_backup"
paths=vm_env=/etc/oracle_backup/oracle_backup.env; runtime=/opt/oracle_backup; state=/var/lib/oracle_backup; logs=/var/log/oracle_backup.
paths=remote_repo=rclone:oci:bucket-20260206-0730/oraclevm; remote_quota_path=oci:bucket-20260206-0730.
paths=local_fallback_repo=/var/lib/oracle_backup/emergency_repo; sqlite_snapshots=/var/lib/oracle_backup/sqlite_snapshots.
state=local_fallback_quota_status,local_fallback_quota_last_error,local_fallback_quota_state.json.
state=last_backup_status,last_successful_repo,last_failed_repos,last_remote_error,last_remote_failure_epoch.
state=last_any_success_epoch,last_remote_success_epoch,last_local_fallback_success_epoch.
backup=scripts/backup.sh:4:ENV_FILE="/etc/oracle_backup/oracle_backup.env"; scripts/backup.sh:5:STATE_DIR="/var/lib/oracle_backup"
restore=scripts/check_backup_health.py:9:from pathlib import Path; scripts/oracle-backup-healthcheck.sh:10:LAST_LOCAL_FALLBACK_SUCCESS_FILE="/var/lib/oracle_backup/last_local_fallback_success_epoch"
import=scripts/check_backup_health.py:9:from pathlib import Path; scripts/oracle-backup-healthcheck.sh:5:LEGACY_STATE_FILE="${ORACLE_BACKUP_HEALTHCHECK_STATE_FILE:-/var/lib/oracle_backup/healthcheck_state.json}"
export=scripts/backup.sh:24:export RESTIC_PASSWORD; scripts/backup.sh:25:if [[ -n "${RCLONE_BWLIMIT:-}" ]]; then export RCLONE_BWLIMIT="$RCLONE_BWLIMIT"; fi
migration=UNKNOWN
retention=scripts/prune_local_snapshots.sh:4:STATE_DIR="/var/lib/oracle_backup"; scripts/prune_local_snapshots.sh:5:SNAP_DIR="$STATE_DIR/sqlite_snapshots"
retention=local_fallback uses LOCAL_FALLBACK_KEEP_LAST=11 default, LOCAL_FALLBACK_RETENTION_GROUP_BY=host,tags default; backup.sh force-runs it pre-write on quota pressure and post-success after fallback.
retention=remote uses RESTIC_KEEP_LAST=48 and RESTIC_FORGET_GROUP_BY=host,tags; blocked while OCI rejects lock writes.
quota=LOCAL_FALLBACK_MAX_GB=7; LOCAL_FALLBACK_SOFT_PCT=80; LOCAL_FALLBACK_PREWRITE_RESERVE_GB=1; LOCAL_FALLBACK_ROOT_MIN_FREE_GB=1.
live=2026-06-29 strano_anello.db=6573379584 bytes, wal~11MiB, shm=32KiB.
DNB:
dnb=scripts/backup.sh:8:RESTIC_RUN_LOCK="$STATE_DIR/restic-job.lock"
dnb=scripts/backup.sh:68:exec 9>"$RESTIC_RUN_LOCK"
dnb=scripts/backup.sh:69:if ! flock -n 9; then
dnb=scripts/backup.sh:105:ORACLE_BACKUP_LOCK_HELD=1 /opt/oracle_backup/prune_local_snapshots.sh || true
dnb=scripts/check_backup_health.py:144:active_grace_min = int_cfg(cfg, "BACKUP_ACTIVE_GRACE_MINUTES", max(threshold_min * 3, 60))
dnb=scripts/check_backup_health.py:145:active_grace_seconds = active_grace_min * 60
dnb=fallback_quota_must_force_retention_before_blocking.
dnb=fallback_success_must_force_retention_after_write_before_quota_refresh.
dnb=do_not_raise_LOCAL_FALLBACK_MAX_GB_to_hide_retention_failure.
dnb=do_not_delete_restic_repo_files_manually; use restic forget/prune policy only.
dnb=do_not_run remote destructive --no-lock prune without explicit operator approval or temporary quota headroom.
dnb=preserve=dev/project.metadata.json,dev/legacy,AI/Human links; docs-only tasks must not touch app code/DB
BUG:
issue=scripts/oracle-backup-healthcheck.sh:19:LOCAL_FALLBACK_RETENTION_ERROR_FILE="/var/lib/oracle_backup/local_fallback_retention_last_error"
issue=scripts/oracle-backup-healthcheck.sh:56:export LOCAL_FALLBACK_RETENTION_STATUS_FILE LOCAL_FALLBACK_RETENTION_ERROR_FILE
resolved=2026-06-29 BACKUP_BLOCKED_FALLBACK_QUOTA root cause: remote OCI StorageLimitExceeded forced local fallback; fallback repo had reclaimable snapshots but backup.sh checked quota before forcing retention and post-success retention skipped due interval.
fix=2026-06-29 backup.sh ensure_local_fallback_quota_available forces configured local retention before refusing fallback write; local fallback success forces retention again; quota-check-only bypasses min interval.
workaround_still_needed=remote OCI remains full; final state should be WARNING REMOTE_DEGRADED until remote capacity/prune is restored.
RISK:
risk=scripts/backup.sh:8:RESTIC_RUN_LOCK="$STATE_DIR/restic-job.lock"
risk=scripts/backup.sh:68:exec 9>"$RESTIC_RUN_LOCK"
risk=scripts/backup.sh:69:if ! flock -n 9; then
risk=scripts/backup.sh:105:ORACLE_BACKUP_LOCK_HELD=1 /opt/oracle_backup/prune_local_snapshots.sh || true
risk=scripts/check_backup_health.py:144:active_grace_min = int_cfg(cfg, "BACKUP_ACTIVE_GRACE_MINUTES", max(threshold_min * 3, 60))
risk=scripts/check_backup_health.py:145:active_grace_seconds = active_grace_min * 60
risk=remote OCI StorageLimitExceeded blocks restic locks and standard remote prune.
risk=strano_anello.db about 6.2G means one fallback stream can consume much of 1GiB prewrite reserve if retention does not run after write.
risk=manual deletion inside restic repo can corrupt backup; only use restic policy commands.
risk=Windows OpenSSH may reject primary key due permissive ACL; use restrictive copy or verified maintenance key.
ROAD:
now=REMOTE_DEGRADED accepted while fallback valid and quota OK; monitor healthcheck for recurrence.
next=restore remote OCI headroom, then run standard /opt/oracle_backup/prune.sh without --no-lock.
later=consider right-sizing remote quota/retention based on strano_anello.db growth and backup cadence.
LINK:
meta=https://github.com/gernalix/oracle-backup-service/blob/fix/degraded-healthcheck-state/dev/project.metadata.json
human=../../human/projects/oracle-backup-service/overview.md
legacy=https://github.com/gernalix/oracle-backup-service/tree/fix/degraded-healthcheck-state/dev/legacy
repo=https://github.com/gernalix/oracle-backup-service/tree/fix/degraded-healthcheck-state
OPEN:
open=tests=UNKNOWN_OR_ABSENT
open=2026-06-05 prompt 918364: Oracle VM live state checked. /dev/sda1 was 45G total, 39G used, 6.6G free, 86%; after safe cleanup it is 38G used, 7.5G free, 84%. Cleanup applied only to apt cache, archived journald vacuum to 300M, and gzip compression of /var/log/syslog.1. No restic repo, emergency repo, sqlite snapshot, DB, WAL, or current log was deleted.
open=2026-06-05 remote quota remains critical: REMOTE_QUOTA_PATH=oci:bucket-20260206-0730, used=22.262 GBytes / 23903533548 bytes, critical=21GiB, assumed limit=22GiB. Remote repo rclone:oci:bucket-20260206-0730/oraclevm has 837 snapshots in group host=instance-20260201-1126 tags=oracle-vm,autosnap-5min, oldest 2026-05-02T01:33:03Z, newest 2026-05-05T05:27:01Z. Policy is RESTIC_KEEP_LAST=48 and RESTIC_FORGET_GROUP_BY=host,tags, but standard restic operations cannot create locks because OCI returns StorageLimitExceeded on locks/*. Do not run destructive no-lock prune without explicit operator approval or temporary quota headroom.
open=2026-06-05 alert posture: backup monitor and healthcheck are rate-limited/deduplicated; check_remote_quota.py only writes /var/lib/oracle_backup/remote_quota_state.json and logs to journald. Fallback local repo /var/lib/oracle_backup/emergency_repo is valid with 27 snapshots and 9.572GiB raw-data; do not delete it while remote is degraded.
open=2026-06-29 live healthcheck after fix: WARNING only for REMOTE_DEGRADED remote quota full; local_fallback_quota=OK repo 5.25GiB < soft 5.60GiB hard 7.00GiB, last local fallback success 2026-06-29T13:43:27Z.
open=validation_note=Git-authenticated checks confirm dev/project.metadata.json and dev/legacy exist on origin/fix/degraded-healthcheck-state; unauthenticated GitHub HEAD may return 404 if repository access is private.
