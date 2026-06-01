META:
name=remote_opt_oracle_backup
slug=remote-opt-oracle-backup
path=/home/daniele/codex-workspace/projects/vm_oracle/remote_opt_oracle_backup
remote=none
branch=main
verified_commit=62254c3
verified_at=2026-06-01T13:39:31+02:00
PURPOSE:
- Remote Oracle backup script set for restic backup/prune/systemd units under the Oracle backup runtime path; source docs are sparse, so ...
STACK:
lang=Python,Shell;fw=UNKNOWN;db=SQLite;platform=UNKNOWN;tools=restic
MAP:
entry=UNKNOWN
core=dev/project.metadata.json
ui=UNKNOWN
db=backup.sh,check_backup_health.py,oracle-backup.service,oracle-backup.timer,prune_local_snapshots.sh
tests=UNKNOWN
scripts=prune.sh
build=UNKNOWN
ci=UNKNOWN
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
- backup.sh=>cleanup_failed_snapshot,snapshot_one_db,run_backup_repo
- check_backup_health.py=>load_env_file,notify,main
- prune_local_snapshots.sh=>bytes_from_gb,snapshot_dirs,count_dirs,total_bytes,free_bytes,delete_oldest
- backup.sh:4:ENV_FILE="/etc/oracle_backup/oracle_backup.env"
- backup.sh:5:STATE_DIR="/var/lib/oracle_backup"
- backup.sh:6:LOG_DIR="/var/log/oracle_backup"
- backup.sh:15:export RESTIC_PASSWORD
- backup.sh:16:if [[ -n "${RCLONE_BWLIMIT:-}" ]]; then export RCLONE_BWLIMIT="$RCLONE_BWLIMIT"; fi
- backup.sh:17:export RESTIC_CACHE_DIR="${RESTIC_CACHE_DIR:-$STATE_DIR/restic_cache}"
FLOW:
- backup.sh:4:ENV_FILE="/etc/oracle_backup/oracle_backup.env"
- backup.sh:5:STATE_DIR="/var/lib/oracle_backup"
- backup.sh:6:LOG_DIR="/var/log/oracle_backup"
- backup.sh:15:export RESTIC_PASSWORD
- backup.sh:16:if [[ -n "${RCLONE_BWLIMIT:-}" ]]; then export RCLONE_BWLIMIT="$RCLONE_BWLIMIT"; fi
- backup.sh:17:export RESTIC_CACHE_DIR="${RESTIC_CACHE_DIR:-$STATE_DIR/restic_cache}"
- backup.sh:21:log="$LOG_DIR/backup_${ts}.log"
- backup.sh:25:echo "[*] oracle-backup @ $ts"
- check_backup_health.py:3:import os, time, sys, traceback
- check_backup_health.py:5:STATE_FILE = "/var/lib/oracle_backup/last_successful_epoch"
- check_backup_health.py:6:ENV_FILE = "/etc/oracle_backup/oracle_backup.env"
- check_backup_health.py:7:LIB_DIR = "/opt/oracle_backup/lib"
INV:
arch=backup.sh:4:ENV_FILE="/etc/oracle_backup/oracle_backup.env"
arch=backup.sh:5:STATE_DIR="/var/lib/oracle_backup"
arch=backup.sh:6:LOG_DIR="/var/log/oracle_backup"
arch=backup.sh:8:RESTIC_RUN_LOCK="$STATE_DIR/restic-job.lock"
arch=backup.sh:21:log="$LOG_DIR/backup_${ts}.log"
arch=backup.sh:25:echo "[*] oracle-backup @ $ts"
data=backup.sh:4:ENV_FILE="/etc/oracle_backup/oracle_backup.env"
data=backup.sh:5:STATE_DIR="/var/lib/oracle_backup"
data=backup.sh:6:LOG_DIR="/var/log/oracle_backup"
data=backup.sh:7:SQLITE_SNAP_DIR="$STATE_DIR/sqlite_snapshots"
data=backup.sh:10:mkdir -p "$STATE_DIR" "$LOG_DIR" "$SQLITE_SNAP_DIR"
data=backup.sh:15:export RESTIC_PASSWORD
safety=backup.sh:8:RESTIC_RUN_LOCK="$STATE_DIR/restic-job.lock"
safety=backup.sh:15:export RESTIC_PASSWORD
safety=backup.sh:36:exec 9>"$RESTIC_RUN_LOCK"
safety=backup.sh:37:if ! flock -n 9; then
safety=backup.sh:42:ORACLE_BACKUP_LOCK_HELD=1 KEEP_LOCAL_SNAPSHOTS=3 MAX_LOCAL_SNAPSHOT_GB=8 MIN_FREE_GB=8 \
safety=backup.sh:52:rm -rf -- "$snap_run_dir"
safety=backup.sh:102:rclone deletefile "$remote_path/.oracle-backup-write-test" // true
ux=check_backup_health.py:50:f"🚨 Backup NON eseguito da {age_min:.1f} minuti (soglia {threshold_min} min).\n"
ux=prune.sh:26:echo "[!] Could not acquire backup lock for prune."
version=dev/project.metadata.json:9:"metadata_version": 1,
i18n=UNKNOWN
BUILD:
- prune.sh:1:#!/usr/bin/env bash
- prune.sh:7:RESTIC_RUN_LOCK="$STATE_DIR/restic-job.lock"
- prune.sh:41:if restic -r "$repo" unlock && \
- prune.sh:43:restic -r "$repo" forget \
- prune.sh:48:restic -r "$repo" prune \
TEST:
- UNKNOWN
DATA:
db=backup.sh:4:ENV_FILE="/etc/oracle_backup/oracle_backup.env"
db=backup.sh:5:STATE_DIR="/var/lib/oracle_backup"
db=backup.sh:6:LOG_DIR="/var/log/oracle_backup"
db=backup.sh:7:SQLITE_SNAP_DIR="$STATE_DIR/sqlite_snapshots"
db=backup.sh:10:mkdir -p "$STATE_DIR" "$LOG_DIR" "$SQLITE_SNAP_DIR"
db=backup.sh:15:export RESTIC_PASSWORD
backup=backup.sh:4:ENV_FILE="/etc/oracle_backup/oracle_backup.env"
backup=backup.sh:5:STATE_DIR="/var/lib/oracle_backup"
backup=backup.sh:6:LOG_DIR="/var/log/oracle_backup"
backup=backup.sh:7:SQLITE_SNAP_DIR="$STATE_DIR/sqlite_snapshots"
import=check_backup_health.py:3:import os, time, sys, traceback
import=check_backup_health.py:26:import telegram_notify # user-provided module
export=backup.sh:15:export RESTIC_PASSWORD
export=backup.sh:16:if [[ -n "${RCLONE_BWLIMIT:-}" ]]; then export RCLONE_BWLIMIT="$RCLONE_BWLIMIT"; fi
export=backup.sh:17:export RESTIC_CACHE_DIR="${RESTIC_CACHE_DIR:-$STATE_DIR/restic_cache}"
migration=UNKNOWN
retention=check_backup_health.py:50:f"🚨 Backup NON eseguito da {age_min:.1f} minuti (soglia {threshold_min} min).\n"
retention=prune_local_snapshots.sh:4:STATE_DIR="/var/lib/oracle_backup"
retention=prune_local_snapshots.sh:5:SNAP_DIR="$STATE_DIR/sqlite_snapshots"
DNB:
- backup.sh:8:RESTIC_RUN_LOCK="$STATE_DIR/restic-job.lock"
- backup.sh:15:export RESTIC_PASSWORD
- backup.sh:36:exec 9>"$RESTIC_RUN_LOCK"
- backup.sh:37:if ! flock -n 9; then
- backup.sh:42:ORACLE_BACKUP_LOCK_HELD=1 KEEP_LOCAL_SNAPSHOTS=3 MAX_LOCAL_SNAPSHOT_GB=8 MIN_FREE_GB=8 \
- backup.sh:52:rm -rf -- "$snap_run_dir"
- backup.sh:102:rclone deletefile "$remote_path/.oracle-backup-write-test" // true
- backup.sh:110:restic -r "$repo" unlock
- backup.sh:4:ENV_FILE="/etc/oracle_backup/oracle_backup.env"
- backup.sh:5:STATE_DIR="/var/lib/oracle_backup"
BUG:
- backup.sh:2:set -euo pipefail
- backup.sh:49:cleanup_failed_snapshot() {
- backup.sh:55:trap cleanup_failed_snapshot EXIT
- backup.sh:66:sqlite3 "$src" ".timeout 5000" ".backup '$dst'"
- backup.sh:84:repo_fail=0
- backup.sh:85:failed_repos=()
- backup.sh:98:echo "[!] repo write preflight failed: $repo"
- backup.sh:128:repo_fail=$((repo_fail + 1))
- check_backup_health.py:20:except FileNotFoundError:
- check_backup_health.py:38:f"Probabile che i backup non siano mai partiti o che ci sia un errore di permessi.\n"
RISK:
- backup.sh:8:RESTIC_RUN_LOCK="$STATE_DIR/restic-job.lock"
- backup.sh:15:export RESTIC_PASSWORD
- backup.sh:36:exec 9>"$RESTIC_RUN_LOCK"
- backup.sh:37:if ! flock -n 9; then
- backup.sh:42:ORACLE_BACKUP_LOCK_HELD=1 KEEP_LOCAL_SNAPSHOTS=3 MAX_LOCAL_SNAPSHOT_GB=8 MIN_FREE_GB=8 \
- backup.sh:52:rm -rf -- "$snap_run_dir"
- backup.sh:102:rclone deletefile "$remote_path/.oracle-backup-write-test" // true
- backup.sh:110:restic -r "$repo" unlock
- check_backup_health.py:3:import os, time, sys, traceback
- check_backup_health.py:63:notify("❌ Errore monitor backup:\n" + traceback.format_exc(), title="Backup monitor error"
ROAD:
now=backup.sh:2:set -euo pipefail
next=backup.sh:49:cleanup_failed_snapshot() {
later=backup.sh:55:trap cleanup_failed_snapshot EXIT
LINK:
meta=../../../projects/vm_oracle/remote_opt_oracle_backup/dev/project.metadata.json
human=../../human/projects/remote-opt-oracle-backup/overview.md
legacy=../../../projects/vm_oracle/remote_opt_oracle_backup/dev/legacy
repo=../../../projects/vm_oracle/remote_opt_oracle_backup
OPEN:
- no tests detected by static scan
