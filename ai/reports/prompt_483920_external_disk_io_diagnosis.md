# prompt_483920 external disk I/O diagnosis

date=2026-06-13
host=daniele-Surface-Pro
scope=read_only_diagnosis;no_kill,no_restart,no_service_change,no_mount_change
protocol=../MEGAVAULT_PROTOCOL.md
host_profile=../global/HOST_PROFILE.md

SUMMARY:
cause_primary=home-incremental-backup.service running scheduled /home rsync snapshot to Seagate6TB2.
cause_secondary=transfer-vecchio-disco-adaptive-throttle.service present with stopped/stale transfer rsync PIDs holding files open; not current I/O source during sample.
confidenza=high

DISKS:
root_t7=/dev/sda2 ext4 uuid=a4bf0d13-b036-490e-9a14-aea83baf37a6 mount=/ model=PSSD_T7_Shield serial=S6YGNS0Y903440H usb
source_4tb=/dev/mapper/source_bitlocker fuseblk ro uuid=22E02106E020E1B1 mount="/media/daniele/Seagate Expansion Drive" parent=/dev/sdb2 serial=WFF0FEX8
dest_6tb=/dev/sdc1 ext4 rw,noatime uuid=75e5363d-6736-4a7e-84be-5242f4735a27 mount=/media/daniele/Seagate6TB2 serial=ZCT3KG54
topology=all_primary_external_storage_shared_SABRENT_USB_hub;activity_on_root_or_dest_can_make_multiple_external_drives_LED_active

EVIDENCE:
mounts=lsblk/findmnt/mount confirmed source_4tb ro and dest_6tb rw; Seagate6TB2 also has systemd autofs wrapper above real /dev/sdc1 row.
service=home-incremental-backup.service user;ActiveState=activating;SubState=start;MainPID=3671550;started=2026-06-13T05:25:53+02:00;trigger=home-incremental-backup.timer
unit=/home/daniele/.config/systemd/user/home-incremental-backup.service;ExecStart=/home/daniele/home_incremental_backup.sh;Nice=19;IOSchedulingClass=idle;TimeoutStartSec=7h
cmd=rsync -aAX --numeric-ids --one-file-system --partial --stats --info=progress2 --bwlimit=512 --link-dest=/media/daniele/Seagate6TB2/home-backups/snapshots/20260519122928 -R /home/daniele/./Documents /media/daniele/Seagate6TB2/home-backups/snapshots/.incomplete-20260613052609-3671550/
pids=3671550 bash main;3676798 timeout;3676819 rsync sender;3676867 rsync child;3676881 rsync receiver
cgroup=/user.slice/user-1000.slice/user@1000.service/app.slice/home-incremental-backup.service
iotop=rsync receiver PID 3676881 wrote about 460-716 KiB/s in samples; sender PID 3676819 read bursts up to 14.81 MiB/s; command bwlimit=512 KiB/s effective progress about 493-512 KiB/s.
proc_io_10s=PID3676819 read_delta=1638.4KiB/s write_delta=0.4KiB/s;PID3676881 write_delta=537.6KiB/s;backup shell PID3676799 read_delta=10559.6KiB/s likely status/sizing helper.
diskstats_10s=dest /dev/sdc1 mostly idle but wrote 120KiB/s and one 4232KiB/s burst;root /dev/sda2 had 1.9-11.4MiB/s writes plus read bursts;source /dev/sdb2 and dm-0 were 0KiB/s during the same sample.
lsof_dest=Seagate6TB2 had open FDs from backup rsync log and incomplete snapshot; transfer rsync root PIDs also held dest/source files open but were not active in diskstats.
fuser_dest=kernel mount, transfer rsync root PIDs, backup timeout/rsync PIDs, and transient du helper were visible on /media/daniele/Seagate6TB2.
status_json=/media/daniele/Seagate6TB2/home-backups/state/status.json status=RUNNING phase=rsync snapshot=20260613052609 latest_snapshot_at=20260519122928 free_gb=2888 bwlimit_kb=512
coexist=status_json reports COEXIST_ALLOWED_URGENT_BACKUP with mega_pid=1243360, mega_bwlimit=5120KiB/s, backup_bwlimit=512KiB/s, nice=19, ionice=idle.
transfer_status=/home/daniele/.local/bin/rsync-transfer-status final_state=RUNNING service_status=active/running metrics_status=stale/log_age_seconds=38606;root rsync PIDs present but ps STAT=TN and source device sample=0KiB/s.
desktop_processes=gvfs,udisks,tumblerd present;not responsible for high I/O in sampled iotop/proc_io.
cloud_backup=mint-cloud-backup-monitor/dashboard running;mint-cloud-backup.service not active/running during service list;restic/rclone/borg not observed as active data movers.

COMMANDS_USEFUL:
realtime_process_io=sudo iotop -oP -d 1
device_io_no_iostat=bash -lc 'awk "$3~/^(sda|sdb|sdc|dm-0)$/{print $3,$6,$10}" /proc/diskstats'
open_files_dest=sudo lsof -w -nP +f -- /media/daniele/Seagate6TB2
backup_status=systemctl --user status home-incremental-backup.service home-incremental-backup.timer --no-pager
backup_state=sed -n '1,160p' /media/daniele/Seagate6TB2/home-backups/state/status.json
transfer_status=/home/daniele/.local/bin/rsync-transfer-status

SAFE_ACTIONS:
diagnosis_complete=yes
fix_applied=no
safe_fix_option_1=let backup finish; progress log showed around 96-97 percent with roughly minutes remaining during diagnosis.
safe_fix_option_2=if disk activity must stop immediately, only after user approval stop home-incremental-backup.service gracefully via systemctl --user stop home-incremental-backup.service; this leaves incomplete snapshot state and should be followed by status/log review.
safe_followup=review why home backup allowed coexistence with stale/stopped transfer metrics and whether urgent coexistence policy should be tightened; do not change policy without separate task.

