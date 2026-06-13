META:
name=oracle-backup-service
slug=oracle-backup-service
path=/home/daniele/codex-workspace/projects/vm_oracle/oracle-backup-service
remote=https://github.com/gernalix/oracle-backup-service.git
branch=fix/degraded-healthcheck-state
verified_commit=552cbbe
verified_at=2026-06-13T00:47Z
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
data=scripts/backup.sh:heartbeat_loop,cleanup_failed_snapshot,cleanup_on_exit,snapshot_one_db,record_remote_failure,record_remote_skip,check_local_fallback_quota,write_local_fallback_quota_state,send_local_fallback_alert
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
files=scripts/backup.sh,scripts/check_backup_health.py,scripts/oracle-backup-healthcheck.sh,scripts/check_remote_quota.py
cmd=shellcheck scripts/backup.sh scripts/oracle-backup-healthcheck.sh; python3 -m py_compile scripts/check_backup_health.py scripts/check_remote_quota.py; ORACLE_BACKUP_QUOTA_CHECK_ONLY isolated /tmp tests; live FORCE_ORACLE_BACKUP=1 ORACLE_BACKUP_QUOTA_CHECK_ONLY=1
DATA:
db=scripts/backup.sh:7:SQLITE_SNAP_DIR="$STATE_DIR/sqlite_snapshots"; scripts/backup.sh:19:mkdir -p "$STATE_DIR" "$LOG_DIR" "$SQLITE_SNAP_DIR"
paths=scripts/backup.sh:4:ENV_FILE="/etc/oracle_backup/oracle_backup.env"; scripts/backup.sh:5:STATE_DIR="/var/lib/oracle_backup"
backup=scripts/backup.sh:4:ENV_FILE="/etc/oracle_backup/oracle_backup.env"; scripts/backup.sh:5:STATE_DIR="/var/lib/oracle_backup"
quota=LOCAL_FALLBACK_MAX_GB=5;LOCAL_FALLBACK_SOFT_PCT=80;LOCAL_FALLBACK_PREWRITE_RESERVE_GB=1;LOCAL_FALLBACK_ROOT_MIN_FREE_GB=1;state=/var/lib/oracle_backup/local_fallback_quota_state.json
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
risk=fallback local repo must never grow past LOCAL_FALLBACK_MAX_GB; BACKUP_BLOCKED_FALLBACK_QUOTA is intentional nonzero fail-safe when OCI is full and emergency_repo is over quota.
OPS:
ops=2026-06-10 prompt 492837: live CRITICAL root cause was backup job starting but failing before restic fallback because retained `/var/lib/oracle_backup/sqlite_snapshots/20260608_180131` used 4.9GiB and `/` had ~4.7GiB free; copying `/home/ubuntu/db/strano_anello.db` (~4.9GiB) as a second SQLite snapshot hit `database or disk is full`.
ops=2026-06-10 prompt 492837 fix: `/opt/oracle_backup/backup.sh` low-space auto mode now streams SQLite `.dump | gzip -c` directly into restic with `--stdin-filename .../*.db.sql.gz`, excludes live `*.db/*.db-wal/*.db-shm` from the path backup in stream mode, and preserves existing retained SQLite snapshot dirs; no backup/repo/snapshot/log/DB/prune/forget/compact was deleted or run.
ops=2026-06-10 prompt 492837 verification: manual `oracle-backup.service` completed `REMOTE_DEGRADED` via `/var/lib/oracle_backup/emergency_repo`; `last_any_success_epoch=1781117071`, `last_local_fallback_success_epoch=1781117071`, `last_backup_status=REMOTE_DEGRADED`, `last_failed_repos=rclone:oci:bucket-20260206-0730/oraclevm`.
ops=2026-06-10 prompt 492837 healthcheck: `oracle-backup-healthcheck.service` exited 0; backup_state WARNING not CRITICAL: `REMOTE_DEGRADED: quota remota piena, fallback locale valido; any_success_age=88s; local_fallback_age=88s`; root_usage/root_free remained ALERT due `/` 91%, 4.1GiB free.
ops=2026-06-10 prompt 492837 remote remains degraded: `remote_quota_state.json` current status CRITICAL, path `oci:bucket-20260206-0730`, used 22.262GBytes / assumed 22GiB; do not run no-lock remote prune/forget/compact without explicit approval or quota headroom.
ops=2026-06-12 prompt 914721 space recovery: copied retained SQLite snapshot `/var/lib/oracle_backup/sqlite_snapshots/20260608_180131` to Seagate `/media/daniele/Seagate6TB2/oracle-vm-offloads/prompt_914721_20260612T175857Z/sqlite_snapshots/20260608_180131`, verified 11 manifest entries + 10 sha256 rows, then removed only that snapshot from VM; `/` moved from 100%/0B free to 82%/8.3G free after automatic fallback backup/retention completed.
ops=2026-06-12 prompt 914721 current state: `sqlite_snapshots` now 40K; `emergency_repo` remains required local fallback and must not be deleted while OCI remote remains `StorageLimitExceeded`/CRITICAL; latest automatic `oracle-backup.service` completed `REMOTE_DEGRADED` with `last_successful_repo=/var/lib/oracle_backup/emergency_repo`.
ops=2026-06-13 prompt 486219 cause: OCI remote still `StorageLimitExceeded`; local fallback wrote repeated stream snapshots into `/var/lib/oracle_backup/emergency_repo`; before fix `/` was 98% used with 1.2G free, `/var/lib/oracle_backup` 20G, emergency_repo 14G, sqlite_snapshots 5.2G.
ops=2026-06-13 prompt 486219 fix: `/opt/oracle_backup/backup.sh` enforces local fallback hard quota before restic write; defaults `LOCAL_FALLBACK_MAX_GB=5`, `LOCAL_FALLBACK_SOFT_PCT=80`, `LOCAL_FALLBACK_PREWRITE_RESERVE_GB=1`, `LOCAL_FALLBACK_ROOT_MIN_FREE_GB=1`; blocked state writes `BACKUP_BLOCKED_FALLBACK_QUOTA` and `/var/lib/oracle_backup/local_fallback_quota_*`.
ops=2026-06-13 prompt 486219 live verification: quota-only live preflight rc=1, `local_fallback_quota_status=BLOCKED`, `last_backup_status=BACKUP_BLOCKED_FALLBACK_QUOTA`, detail=`local fallback repo 13.95 GiB >= hard quota 5.00 GiB`; no restic fallback write started.
ops=2026-06-13 prompt 486219 cleanup report: no deletion/prune performed; inventory at `/home/ubuntu/maintenance-486219/reports/fallback_inventory_20260613T000454Z.txt`; emergency_repo restic has 82 snapshots and 13.337GiB raw-data.
ops=2026-06-13 prompt 486219 tests: shellcheck/bash -n/python py_compile passed; isolated 1M quota test blocked rc=1 before write; isolated 5G-under-threshold test rc=0; healthcheck dry-run CRITICAL for `BACKUP_BLOCKED_FALLBACK_QUOTA`; monitor dry-run rc=1; `docker exec uptime-kuma true` OK; `/run` 27%.
ops=2026-06-13 prompt 918472 cleanup: local-only restic cleanup reduced `/var/lib/oracle_backup/emergency_repo` from 82 snapshots / 14G physical / 13.337GiB raw-data to 11 snapshots / 3.9G physical / 3.805GiB raw-data; `/` moved from 98% with 1.2G free to 75% with 12G free.
ops=2026-06-13 prompt 918472 commands: only `/var/lib/oracle_backup/emergency_repo` was targeted with `restic -r /var/lib/oracle_backup/emergency_repo forget ...` and `restic -r /var/lib/oracle_backup/emergency_repo prune`; no remote repo was touched and Kuma/Docker were not modified.
ops=2026-06-13 prompt 918472 final state: `local_fallback_quota_status=OK`, quota detail `repo 3.81 GiB < soft 4.00 GiB, hard 5.00 GiB`; `restic check` passed; healthcheck/monitor are WARNING/REMOTE_DEGRADED because OCI remains `StorageLimitExceeded`; `docker exec uptime-kuma true` OK; timer active and service not failed.
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
open=2026-06-10 prompt 492837: root filesystem still tight after fix (`/` 91%, 4.1GiB free) and healthcheck root_usage/root_free remain ALERT; remote OCI quota still StorageLimitExceeded/CRITICAL. Backup freshness is restored by local fallback, but quota/disk capacity remain operational risks.
open=2026-06-12 prompt 914721: root recovered to 82%, 8.3G free after offloading/removing retained SQLite snapshot; OCI remote remains CRITICAL and fallback repo remains the only currently successful backup target, so long-term quota/remediation is still open.
open=2026-06-12 prompt 672184: during unrelated Kuma docker-exec verification, automatic oracle-backup.service started at 20:01:20Z, skipped OCI remote due StorageLimitExceeded cooldown, and wrote to /var/lib/oracle_backup/emergency_repo; / rose to 94%, 3.1G free while service remained activating. Treat as continuing capacity risk; do not interrupt/delete fallback casually.
open=2026-06-13 prompt 918472: local fallback repo is now below the 5G hard quota, but OCI remote remains `StorageLimitExceeded`; the system is degraded but controlled. Future local fallback growth is still bounded by `LOCAL_FALLBACK_MAX_GB=5` plus pre-write reserve and root free checks.
