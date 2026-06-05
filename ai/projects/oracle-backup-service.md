META:
name=oracle-backup-service
slug=oracle-backup-service
path=/home/daniele/codex-workspace/projects/vm_oracle/oracle-backup-service
remote=https://github.com/gernalix/oracle-backup-service.git
branch=fix/degraded-healthcheck-state
verified_commit=058c59b
verified_at=2026-06-01T13:59:53+02:00
protocol=MEGAVAULT_PROTOCOL.md:v2
PURPOSE:
purpose=Restic-based backup service for the Oracle VM. It snapshots SQLite databases with the SQLite online backup API, backs up `/home/ubuntu`, `/etc`, and the current SQLite snapshot directory, then reco
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
FLOW:
flow=script->scripts/check_remote_quota.py=>scripts/backup.sh
flow=data->scripts/backup.sh
flow=scripts/backup.sh:4:ENV_FILE="/etc/oracle_backup/oracle_backup.env"
flow=scripts/backup.sh:5:STATE_DIR="/var/lib/oracle_backup"
flow=scripts/backup.sh:6:LOG_DIR="/var/log/oracle_backup"
INV:
arch=scripts/backup.sh:heartbeat_loop,cleanup_failed_snapshot,cleanup_on_exit,snapshot_one_db,record_remote_failure; scripts/check_backup_health.py:load_env_file,read_text,read_epoch,notify,int_cfg; scripts/prune_local_snapshots.sh:bytes_from...
data=scripts/oracle-backup-healthcheck.sh:5:LEGACY_STATE_FILE="${ORACLE_BACKUP_HEALTHCHECK_STATE_FILE:-/var/lib/oracle_backup/healthcheck_state.json}"; systemd/oracle-backup-healthcheck.service:2:Description=Oracle backup preventive healthcheck
ux=scripts/oracle-backup-healthcheck.sh:82:echo "[ERROR] could not acquire healthcheck alert lock: $HEALTHCHECK_ALERT_LOCK_FILE" >&2; scripts/check_backup_health.py:94:["systemctl", "is-active", "--quiet", name],
backup=scripts/backup.sh:4:ENV_FILE="/etc/oracle_backup/oracle_backup.env"; scripts/backup.sh:5:STATE_DIR="/var/lib/oracle_backup"
migration=UNKNOWN
version=dev/project.metadata.json:9:"metadata_version": 1,
i18n=UNKNOWN
security=scripts/backup.sh:24:export RESTIC_PASSWORD; scripts/prune.sh:13:export RESTIC_PASSWORD
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
backup=scripts/backup.sh:4:ENV_FILE="/etc/oracle_backup/oracle_backup.env"; scripts/backup.sh:5:STATE_DIR="/var/lib/oracle_backup"
restore=scripts/check_backup_health.py:9:from pathlib import Path; scripts/oracle-backup-healthcheck.sh:10:LAST_LOCAL_FALLBACK_SUCCESS_FILE="/var/lib/oracle_backup/last_local_fallback_success_epoch"
import=scripts/check_backup_health.py:9:from pathlib import Path; scripts/oracle-backup-healthcheck.sh:5:LEGACY_STATE_FILE="${ORACLE_BACKUP_HEALTHCHECK_STATE_FILE:-/var/lib/oracle_backup/healthcheck_state.json}"
export=scripts/backup.sh:24:export RESTIC_PASSWORD; scripts/backup.sh:25:if [[ -n "${RCLONE_BWLIMIT:-}" ]]; then export RCLONE_BWLIMIT="$RCLONE_BWLIMIT"; fi
migration=UNKNOWN
retention=scripts/prune_local_snapshots.sh:4:STATE_DIR="/var/lib/oracle_backup"; scripts/prune_local_snapshots.sh:5:SNAP_DIR="$STATE_DIR/sqlite_snapshots"
DNB:
dnb=scripts/backup.sh:8:RESTIC_RUN_LOCK="$STATE_DIR/restic-job.lock"
dnb=scripts/backup.sh:68:exec 9>"$RESTIC_RUN_LOCK"
dnb=scripts/backup.sh:69:if ! flock -n 9; then
dnb=scripts/backup.sh:105:ORACLE_BACKUP_LOCK_HELD=1 /opt/oracle_backup/prune_local_snapshots.sh || true
dnb=scripts/check_backup_health.py:144:active_grace_min = int_cfg(cfg, "BACKUP_ACTIVE_GRACE_MINUTES", max(threshold_min * 3, 60))
dnb=scripts/check_backup_health.py:145:active_grace_seconds = active_grace_min * 60
dnb=preserve=dev/project.metadata.json,dev/legacy,AI/Human links; docs-only tasks must not touch app code/DB
BUG:
issue=scripts/oracle-backup-healthcheck.sh:19:LOCAL_FALLBACK_RETENTION_ERROR_FILE="/var/lib/oracle_backup/local_fallback_retention_last_error"
issue=scripts/oracle-backup-healthcheck.sh:56:export LOCAL_FALLBACK_RETENTION_STATUS_FILE LOCAL_FALLBACK_RETENTION_ERROR_FILE
RISK:
risk=scripts/backup.sh:8:RESTIC_RUN_LOCK="$STATE_DIR/restic-job.lock"
risk=scripts/backup.sh:68:exec 9>"$RESTIC_RUN_LOCK"
risk=scripts/backup.sh:69:if ! flock -n 9; then
risk=scripts/backup.sh:105:ORACLE_BACKUP_LOCK_HELD=1 /opt/oracle_backup/prune_local_snapshots.sh || true
risk=scripts/check_backup_health.py:144:active_grace_min = int_cfg(cfg, "BACKUP_ACTIVE_GRACE_MINUTES", max(threshold_min * 3, 60))
risk=scripts/check_backup_health.py:145:active_grace_seconds = active_grace_min * 60
ROAD:
now=UNKNOWN
next=UNKNOWN
later=UNKNOWN
LINK:
meta=../../../projects/vm_oracle/oracle-backup-service/dev/project.metadata.json
human=../../human/projects/oracle-backup-service/overview.md
legacy=../../../projects/vm_oracle/oracle-backup-service/dev/legacy
repo=../../../projects/vm_oracle/oracle-backup-service
OPEN:
open=tests=UNKNOWN_OR_ABSENT
open=2026-06-05 prompt 918364: Oracle VM live state checked. /dev/sda1 was 45G total, 39G used, 6.6G free, 86%; after safe cleanup it is 38G used, 7.5G free, 84%. Cleanup applied only to apt cache, archived journald vacuum to 300M, and gzip compression of /var/log/syslog.1. No restic repo, emergency repo, sqlite snapshot, DB, WAL, or current log was deleted.
open=2026-06-05 remote quota remains critical: REMOTE_QUOTA_PATH=oci:bucket-20260206-0730, used=22.262 GBytes / 23903533548 bytes, critical=21GiB, assumed limit=22GiB. Remote repo rclone:oci:bucket-20260206-0730/oraclevm has 837 snapshots in group host=instance-20260201-1126 tags=oracle-vm,autosnap-5min, oldest 2026-05-02T01:33:03Z, newest 2026-05-05T05:27:01Z. Policy is RESTIC_KEEP_LAST=48 and RESTIC_FORGET_GROUP_BY=host,tags, but standard restic operations cannot create locks because OCI returns StorageLimitExceeded on locks/*. Do not run destructive no-lock prune without explicit operator approval or temporary quota headroom.
open=2026-06-05 alert posture: backup monitor and healthcheck are rate-limited/deduplicated; check_remote_quota.py only writes /var/lib/oracle_backup/remote_quota_state.json and logs to journald. Fallback local repo /var/lib/oracle_backup/emergency_repo is valid with 27 snapshots and 9.572GiB raw-data; do not delete it while remote is degraded.
