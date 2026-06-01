META:
name=remote_opt_oracle_backup
slug=remote-opt-oracle-backup
path=/home/daniele/codex-workspace/projects/vm_oracle/remote_opt_oracle_backup
remote=none
branch=main
verified_commit=62254c3
verified_at=2026-06-01T13:59:53+02:00
protocol=MEGAVAULT_PROTOCOL.md:v2
PURPOSE:
purpose=Remote Oracle backup script set for restic backup/prune/systemd units under the Oracle backup runtime path; source docs are sparse, so verify remote runtime before edits
STACK:
lang=Python,Shell
fw=UNKNOWN
db=SQLite
platform=UNKNOWN
tools=restic
MAP:
entry=UNKNOWN
ui=UNKNOWN
core=dev/project.metadata.json
db=backup.sh,check_backup_health.py,oracle-backup.service,oracle-backup.timer,prune_local_snapshots.sh
tests=UNKNOWN
scripts=prune.sh
build=UNKNOWN
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
data=backup.sh:cleanup_failed_snapshot,snapshot_one_db,run_backup_repo
data=check_backup_health.py:load_env_file,notify,main
data=prune_local_snapshots.sh:bytes_from_gb,snapshot_dirs,count_dirs,total_bytes,free_bytes,delete_oldest
FLOW:
flow=script->prune.sh=>backup.sh
flow=data->backup.sh
flow=backup.sh:4:ENV_FILE="/etc/oracle_backup/oracle_backup.env"
flow=backup.sh:5:STATE_DIR="/var/lib/oracle_backup"
flow=backup.sh:6:LOG_DIR="/var/log/oracle_backup"
INV:
arch=backup.sh:cleanup_failed_snapshot,snapshot_one_db,run_backup_repo; check_backup_health.py:load_env_file,notify,main; prune_local_snapshots.sh:bytes_from_gb,snapshot_dirs,count_dirs,total_bytes,free_bytes
data=dev/project.metadata.json:2:"project_name": "remote_opt_oracle_backup",; dev/project.metadata.json:3:"project_slug": "remote-opt-oracle-backup",
ux=check_backup_health.py:50:f" Backup NON eseguito da {age_min:.1f} minuti (soglia {threshold_min} min).\n"; prune.sh:26:echo "[!] Could not acquire backup lock for prune."
backup=backup.sh:4:ENV_FILE="/etc/oracle_backup/oracle_backup.env"; backup.sh:5:STATE_DIR="/var/lib/oracle_backup"
migration=UNKNOWN
version=dev/project.metadata.json:9:"metadata_version": 1,
i18n=UNKNOWN
security=backup.sh:15:export RESTIC_PASSWORD; prune.sh:13:export RESTIC_PASSWORD
perf=backup.sh:8:RESTIC_RUN_LOCK="$STATE_DIR/restic-job.lock"; backup.sh:36:exec 9>"$RESTIC_RUN_LOCK"
BUILD:
files=UNKNOWN
cmd=UNKNOWN
TEST:
files=UNKNOWN
cmd=UNKNOWN
DATA:
db=backup.sh:7:SQLITE_SNAP_DIR="$STATE_DIR/sqlite_snapshots"; backup.sh:10:mkdir -p "$STATE_DIR" "$LOG_DIR" "$SQLITE_SNAP_DIR"
paths=backup.sh:4:ENV_FILE="/etc/oracle_backup/oracle_backup.env"; backup.sh:5:STATE_DIR="/var/lib/oracle_backup"
backup=backup.sh:4:ENV_FILE="/etc/oracle_backup/oracle_backup.env"; backup.sh:5:STATE_DIR="/var/lib/oracle_backup"
restore=UNKNOWN
import=dev/project.metadata.json:2:"project_name": "remote_opt_oracle_backup",; dev/project.metadata.json:3:"project_slug": "remote-opt-oracle-backup",
export=backup.sh:15:export RESTIC_PASSWORD; backup.sh:16:if [[ -n "${RCLONE_BWLIMIT:-}" ]]; then export RCLONE_BWLIMIT="$RCLONE_BWLIMIT"; fi
migration=UNKNOWN
retention=prune_local_snapshots.sh:4:STATE_DIR="/var/lib/oracle_backup"; prune_local_snapshots.sh:5:SNAP_DIR="$STATE_DIR/sqlite_snapshots"
DNB:
dnb=backup.sh:8:RESTIC_RUN_LOCK="$STATE_DIR/restic-job.lock"
dnb=backup.sh:36:exec 9>"$RESTIC_RUN_LOCK"
dnb=backup.sh:37:if ! flock -n 9; then
dnb=backup.sh:42:ORACLE_BACKUP_LOCK_HELD=1 KEEP_LOCAL_SNAPSHOTS=3 MAX_LOCAL_SNAPSHOT_GB=8 MIN_FREE_GB=8 \
dnb=backup.sh:102:rclone deletefile "$remote_path/.oracle-backup-write-test" || true
dnb=backup.sh:110:restic -r "$repo" unlock
dnb=preserve=dev/project.metadata.json,dev/legacy,AI/Human links; docs-only tasks must not touch app code/DB
BUG:
issue=UNKNOWN
RISK:
risk=backup.sh:8:RESTIC_RUN_LOCK="$STATE_DIR/restic-job.lock"
risk=backup.sh:36:exec 9>"$RESTIC_RUN_LOCK"
risk=backup.sh:37:if ! flock -n 9; then
risk=backup.sh:42:ORACLE_BACKUP_LOCK_HELD=1 KEEP_LOCAL_SNAPSHOTS=3 MAX_LOCAL_SNAPSHOT_GB=8 MIN_FREE_GB=8 \
risk=backup.sh:102:rclone deletefile "$remote_path/.oracle-backup-write-test" || true
risk=backup.sh:110:restic -r "$repo" unlock
ROAD:
now=UNKNOWN
next=UNKNOWN
later=UNKNOWN
LINK:
meta=../../../projects/vm_oracle/remote_opt_oracle_backup/dev/project.metadata.json
human=../../human/projects/remote-opt-oracle-backup/overview.md
legacy=../../../projects/vm_oracle/remote_opt_oracle_backup/dev/legacy
repo=../../../projects/vm_oracle/remote_opt_oracle_backup
OPEN:
open=tests=UNKNOWN_OR_ABSENT
