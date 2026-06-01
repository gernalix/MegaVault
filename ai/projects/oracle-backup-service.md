META:
name=oracle-backup-service
slug=oracle-backup-service
path=/home/daniele/codex-workspace/projects/vm_oracle/oracle-backup-service
remote=https://github.com/gernalix/oracle-backup-service.git
branch=fix/degraded-healthcheck-state
verified_commit=058c59b
verified_at=2026-06-01T13:39:31+02:00
PURPOSE:
- Restic-based backup service for the Oracle VM. It snapshots SQLite databases with the SQLite online backup API, backs up `/home/ubuntu`...
STACK:
lang=Python,Shell;fw=UNKNOWN;db=SQLite;platform=UNKNOWN;tools=restic,systemd
MAP:
entry=UNKNOWN
core=dev/project.metadata.json
ui=UNKNOWN
db=scripts/backup.sh
db=scripts/check_backup_health.py
db=scripts/oracle-backup-healthcheck.sh
db=scripts/prune_local_snapshots.sh
db=systemd/oracle-backup-healthcheck.service
db=systemd/oracle-backup-healthcheck.timer
db=systemd/oracle-backup-localprune.service
db=systemd/oracle-backup-localprune.timer
tests=UNKNOWN
scripts=scripts/check_remote_quota.py,scripts/prune.sh
build=UNKNOWN
ci=UNKNOWN
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
- scripts/backup.sh=>heartbeat_loop,cleanup_failed_snapshot,cleanup_on_exit,snapshot_one_db,record_remote_failure,reco
- scripts/check_backup_health.py=>load_env_file,read_text,read_epoch,notify,int_cfg,load_json,save_json
- scripts/prune_local_snapshots.sh=>bytes_from_gb,snapshot_dirs,count_dirs,total_bytes,free_bytes,delete_oldest
- scripts/backup.sh:4:ENV_FILE="/etc/oracle_backup/oracle_backup.env"
- scripts/backup.sh:5:STATE_DIR="/var/lib/oracle_backup"
- scripts/backup.sh:6:LOG_DIR="/var/log/oracle_backup"
- scripts/backup.sh:15:BACKUP_ACTIVE_FILE="$STATE_DIR/backup_active_epoch"
- scripts/backup.sh:16:BACKUP_HEARTBEAT_FILE="$STATE_DIR/backup_heartbeat_epoch"
- scripts/backup.sh:17:BACKUP_HEARTBEAT_PID_FILE="$STATE_DIR/backup_heartbeat_pid"
FLOW:
- scripts/backup.sh:4:ENV_FILE="/etc/oracle_backup/oracle_backup.env"
- scripts/backup.sh:5:STATE_DIR="/var/lib/oracle_backup"
- scripts/backup.sh:6:LOG_DIR="/var/log/oracle_backup"
- scripts/backup.sh:15:BACKUP_ACTIVE_FILE="$STATE_DIR/backup_active_epoch"
- scripts/backup.sh:16:BACKUP_HEARTBEAT_FILE="$STATE_DIR/backup_heartbeat_epoch"
- scripts/backup.sh:17:BACKUP_HEARTBEAT_PID_FILE="$STATE_DIR/backup_heartbeat_pid"
- scripts/backup.sh:24:export RESTIC_PASSWORD
- scripts/backup.sh:25:if [[ -n "${RCLONE_BWLIMIT:-}" ]]; then export RCLONE_BWLIMIT="$RCLONE_BWLIMIT"; fi
- scripts/check_backup_health.py:2:import fcntl
- scripts/check_backup_health.py:3:import json
- scripts/check_backup_health.py:4:import os
- scripts/check_backup_health.py:5:import subprocess
INV:
arch=scripts/backup.sh:4:ENV_FILE="/etc/oracle_backup/oracle_backup.env"
arch=scripts/backup.sh:5:STATE_DIR="/var/lib/oracle_backup"
arch=scripts/backup.sh:6:LOG_DIR="/var/log/oracle_backup"
arch=scripts/backup.sh:8:RESTIC_RUN_LOCK="$STATE_DIR/restic-job.lock"
arch=scripts/backup.sh:15:BACKUP_ACTIVE_FILE="$STATE_DIR/backup_active_epoch"
arch=scripts/backup.sh:16:BACKUP_HEARTBEAT_FILE="$STATE_DIR/backup_heartbeat_epoch"
data=scripts/backup.sh:4:ENV_FILE="/etc/oracle_backup/oracle_backup.env"
data=scripts/backup.sh:5:STATE_DIR="/var/lib/oracle_backup"
data=scripts/backup.sh:6:LOG_DIR="/var/log/oracle_backup"
data=scripts/backup.sh:7:SQLITE_SNAP_DIR="$STATE_DIR/sqlite_snapshots"
data=scripts/backup.sh:15:BACKUP_ACTIVE_FILE="$STATE_DIR/backup_active_epoch"
data=scripts/backup.sh:16:BACKUP_HEARTBEAT_FILE="$STATE_DIR/backup_heartbeat_epoch"
safety=scripts/backup.sh:8:RESTIC_RUN_LOCK="$STATE_DIR/restic-job.lock"
safety=scripts/backup.sh:24:export RESTIC_PASSWORD
safety=scripts/backup.sh:59:if [[ "${FORCE_ORACLE_BACKUP:-0}" != "1" && "$last_any_success" =~ ^[0-9]+$ && "$MIN_BACKUP
safety=scripts/backup.sh:68:exec 9>"$RESTIC_RUN_LOCK"
safety=scripts/backup.sh:69:if ! flock -n 9; then
safety=scripts/backup.sh:85:rm -rf -- "$snap_run_dir"
safety=scripts/backup.sh:92:kill "$heartbeat_pid" 2>/dev/null // true
ux=UNKNOWN
version=dev/project.metadata.json:9:"metadata_version": 1,
i18n=UNKNOWN
BUILD:
- scripts/check_remote_quota.py:1:#!/usr/bin/env python3
- scripts/prune.sh:1:#!/usr/bin/env bash
- scripts/prune.sh:7:RESTIC_RUN_LOCK="$STATE_DIR/restic-job.lock"
- scripts/prune.sh:51:if timeout --kill-after=60s "$RESTIC_PRUNE_TIMEOUT_SECONDS" restic -r "$repo" unlock && \
- scripts/prune.sh:53:restic -r "$repo" forget \
- scripts/prune.sh:58:restic -r "$repo" prune \
TEST:
- UNKNOWN
DATA:
db=scripts/backup.sh:4:ENV_FILE="/etc/oracle_backup/oracle_backup.env"
db=scripts/backup.sh:5:STATE_DIR="/var/lib/oracle_backup"
db=scripts/backup.sh:6:LOG_DIR="/var/log/oracle_backup"
db=scripts/backup.sh:7:SQLITE_SNAP_DIR="$STATE_DIR/sqlite_snapshots"
db=scripts/backup.sh:15:BACKUP_ACTIVE_FILE="$STATE_DIR/backup_active_epoch"
db=scripts/backup.sh:16:BACKUP_HEARTBEAT_FILE="$STATE_DIR/backup_heartbeat_epoch"
backup=scripts/backup.sh:4:ENV_FILE="/etc/oracle_backup/oracle_backup.env"
backup=scripts/backup.sh:5:STATE_DIR="/var/lib/oracle_backup"
backup=scripts/backup.sh:6:LOG_DIR="/var/log/oracle_backup"
backup=scripts/backup.sh:7:SQLITE_SNAP_DIR="$STATE_DIR/sqlite_snapshots"
import=scripts/check_backup_health.py:2:import fcntl
import=scripts/check_backup_health.py:3:import json
import=scripts/check_backup_health.py:4:import os
export=scripts/backup.sh:24:export RESTIC_PASSWORD
export=scripts/backup.sh:25:if [[ -n "${RCLONE_BWLIMIT:-}" ]]; then export RCLONE_BWLIMIT="$RCLONE_BWLIMIT"; fi
migration=UNKNOWN
retention=scripts/prune_local_snapshots.sh:4:STATE_DIR="/var/lib/oracle_backup"
retention=scripts/prune_local_snapshots.sh:5:SNAP_DIR="$STATE_DIR/sqlite_snapshots"
retention=scripts/prune_local_snapshots.sh:7:ENV_FILE="/etc/oracle_backup/oracle_backup.env"
DNB:
- scripts/backup.sh:8:RESTIC_RUN_LOCK="$STATE_DIR/restic-job.lock"
- scripts/backup.sh:24:export RESTIC_PASSWORD
- scripts/backup.sh:59:if [[ "${FORCE_ORACLE_BACKUP:-0}" != "1" && "$last_any_success" =~ ^[0-9]+$ && "$MIN_BACKUP_INT
- scripts/backup.sh:68:exec 9>"$RESTIC_RUN_LOCK"
- scripts/backup.sh:69:if ! flock -n 9; then
- scripts/backup.sh:85:rm -rf -- "$snap_run_dir"
- scripts/backup.sh:92:kill "$heartbeat_pid" 2>/dev/null // true
- scripts/backup.sh:105:ORACLE_BACKUP_LOCK_HELD=1 /opt/oracle_backup/prune_local_snapshots.sh // true
- scripts/backup.sh:4:ENV_FILE="/etc/oracle_backup/oracle_backup.env"
- scripts/backup.sh:5:STATE_DIR="/var/lib/oracle_backup"
BUG:
- scripts/backup.sh:2:set -euo pipefail
- scripts/backup.sh:13:LAST_REMOTE_ERROR_FILE="$STATE_DIR/last_remote_error"
- scripts/backup.sh:14:LAST_REMOTE_FAILURE_EPOCH_FILE="$STATE_DIR/last_remote_failure_epoch"
- scripts/backup.sh:36:RESTIC_BACKUP_TIMEOUT_SECONDS="${RESTIC_BACKUP_TIMEOUT_SECONDS:-5400}"
- scripts/backup.sh:37:RESTIC_PRUNE_TIMEOUT_SECONDS="${RESTIC_PRUNE_TIMEOUT_SECONDS:-3600}"
- scripts/backup.sh:38:REMOTE_PREFLIGHT_FAILURE_COOLDOWN_SECONDS="${REMOTE_PREFLIGHT_FAILURE_COOLDOWN_SECONDS:-21600}"
- scripts/backup.sh:82:cleanup_failed_snapshot() {
- scripts/backup.sh:96:cleanup_failed_snapshot
- scripts/check_backup_health.py:20:LAST_FAILED_REPOS_FILE = STATE_DIR / "last_failed_repos"
- scripts/check_backup_health.py:22:LAST_REMOTE_ERROR_FILE = STATE_DIR / "last_remote_error"
RISK:
- scripts/backup.sh:8:RESTIC_RUN_LOCK="$STATE_DIR/restic-job.lock"
- scripts/backup.sh:24:export RESTIC_PASSWORD
- scripts/backup.sh:59:if [[ "${FORCE_ORACLE_BACKUP:-0}" != "1" && "$last_any_success" =~ ^[0-9]+$ && "$MIN_BACKUP_INT
- scripts/backup.sh:68:exec 9>"$RESTIC_RUN_LOCK"
- scripts/backup.sh:69:if ! flock -n 9; then
- scripts/backup.sh:85:rm -rf -- "$snap_run_dir"
- scripts/backup.sh:92:kill "$heartbeat_pid" 2>/dev/null // true
- scripts/backup.sh:105:ORACLE_BACKUP_LOCK_HELD=1 /opt/oracle_backup/prune_local_snapshots.sh // true
- scripts/check_backup_health.py:8:import traceback
- scripts/check_backup_health.py:144:active_grace_min = int_cfg(cfg, "BACKUP_ACTIVE_GRACE_MINUTES", max(threshold_min
ROAD:
now=scripts/oracle-backup-healthcheck.sh:379:f"/ usage {root_used_pct}% >= {ROOT_USAGE_WARN_PCT}% first observation; war
next=UNKNOWN
later=UNKNOWN
LINK:
meta=../../../projects/vm_oracle/oracle-backup-service/dev/project.metadata.json
human=../../human/projects/oracle-backup-service/overview.md
legacy=../../../projects/vm_oracle/oracle-backup-service/dev/legacy
repo=../../../projects/vm_oracle/oracle-backup-service
OPEN:
- no tests detected by static scan
