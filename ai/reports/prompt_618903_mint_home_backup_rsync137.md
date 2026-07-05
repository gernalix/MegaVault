# prompt_618903 mint-home-backup rsync_exit 137

date=2026-06-06
scope=mint-home-backup only
prior=/home/daniele/codex-workspace/MegaVault/ai/reports/prompt_482917_kuma_noise_reduction.md

## Summary

root_cause=runtime guard aborted rsync after sustained high load; parent process lost abort reason because guard ran in background subshell; final wait saw rsync_exit=137 and wrote FAILURE.
not_cause=OOM,systemd_timeout,disk_full,destination_permission,rsync-transfer_conflict,kernel_io_error.
kuma_policy=ABORTED_SAFE is UP/WARNING only when status has persisted WHY_ABORTED reason; rsync_exit=137 without that reason remains DOWN failure.

## Evidence

service=home-incremental-backup.service user; TimeoutStartSec=7h; old run exited status=137 at 2026-06-06 05:38:04 CEST.
timer=home-incremental-backup.timer active; next observed 2026-06-07 04:19:21 CEST.
backup_log=/media/daniele/Seagate6TB2/home-backups/logs/backup-20260606.log
events=PAUSED load_x100 640>600 -> PAUSED_RECOVERED -> PAUSED load_x100 623>600 -> ABORTED_SAFE load_x100 622>600 -> final FAILURE rsync_exit=137.
kernel=journalctl -k during 03:30-06:00 found no OOM, memory-cgroup kill, severe destination I/O, ext4, USB, or sdc errors.
resources=MemAvailable about 4.3GiB and SwapFree about 4.1GiB at failure; load guard threshold normal_load_x100_max=600.
destination=/media/daniele/Seagate6TB2/home-backups on /dev/sdc1 ext4 rw,noatime; free about 3.0T; inode use about 2%; owned daniele:daniele.
conflict=no active rsync-transfer or transfer rsync process found during diagnosis.

## Changes

live_script=/home/daniele/home_incremental_backup.sh
repo_copy=/home/daniele/backup_docs/bin/home_incremental_backup.sh
fix=runtime guard writes /home/daniele/.local/state/home-backup/runtime_abort_reason.env before terminating rsync process group; parent rereads it after wait.
fix=KILL is sent only if the target process/group is still alive after TERM.
fix=HOME_BACKUP_RESOURCE_PAUSE_SECONDS added; live config 90.
fix=HOME_BACKUP_BWLIMIT_KB changed live 1024 -> 512.

live_kuma=/home/daniele/home_backup_kuma_push.sh
repo_kuma=/home/daniele/backup_docs/bin/home_backup_kuma_push.sh
fix=ABORTED_SAFE,LOW_RESOURCE_SKIP,WAITING_SAFE_WINDOW are backup WARNING states, not DOWN.
fix=backup reason in Kuma messages now prefers backup skip reason over retention reason unless backup succeeded.
fix=push state split: state/kuma_backup_push.json and state/kuma_retention_push.json.

config_live=/home/daniele/.config/home-backup/home-backup.env
config_example=/home/daniele/backup_docs/config/home-backup.env.example

## Runtime State After Fix

status=/media/daniele/Seagate6TB2/home-backups/state/status.json status=ABORTED_SAFE phase=aborted snapshot=20260606045340 last_error=rsync_exit=137 skip_reason="WHY_ABORTED load_x100 622 above 600".
kuma_backup_push=/media/daniele/Seagate6TB2/home-backups/state/kuma_backup_push.json result=sent kuma_status=up message="WARNING ABORTED_SAFE ... error=rsync_exit=137".
kuma_retention_push=/media/daniele/Seagate6TB2/home-backups/state/kuma_retention_push.json result=sent kuma_status=up.
systemd=home-incremental-backup.service reset-failed; ActiveState=inactive SubState=dead Result=success; old ExecMainStatus=137 remains in metadata/logs as historical run evidence.

## Tests

syntax=bash -n live and backup_docs copies of home_incremental_backup.sh and home_backup_kuma_push.sh.
dry_run_safe=small dry-run with /tmp root was blocked by non-root destination guard as DISK_UNAVAILABLE.
dry_run_rsync=small source dry-run on real mounted backup root with Kuma disabled and force-conservative load bypass exited rc=0 SUCCESS dry_run; no real snapshot promoted.
kuma_abort_test=synthetic ABORTED_SAFE state on temporary mounted test root produced DRY_OR_DISABLED status=up message WARNING ABORTED_SAFE ... error=rsync_exit=137.
kuma_real_push=/home/daniele/home_backup_kuma_push.sh HEARTBEAT sent status=up for backup monitor after corrected ABORTED_SAFE status.

## Residual Risk

risk=No full real /home backup was run after the patch because current load/I/O pressure was high; next scheduled timer is expected to either complete, pause/recover, or ABORTED_SAFE without false DOWN.
risk=ABORTED_SAFE is not a successful backup and does not update latest; next completed full snapshot is still required for fresh protection.
