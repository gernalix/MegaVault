# STORAGE_TOPOLOGY
VERSION=8
STATUS=ACTIVE
MODE=codex_first
FORMAT=ultracompressed
SOURCE=HOST_PROFILE+findmnt+df+lsblk_2026-07-14+activity_593184+activity_842731+activity_583921+activity_684219+activity_826417
PROTOCOL=../MEGAVAULT_PROTOCOL.md
HOST_PROFILE=HOST_PROFILE.md
HUMAN=../../human/global/STORAGE_TOPOLOGY.md

CURRENT_FEDORA:
host=fedora
machine=Lenovo_ThinkPad_P14s_Gen_5_AMD
root=/dev/mapper/luks-0c261c5f-02dd-484f-b266-13ff4ee02abb btrfs encrypted size=951.3GiB available=844GiB mounts=/,/home
home=/home/daniele
monitor_db=/var/lib/fedora-system-monitor/monitor.sqlite3;schema=2;WAL=yes;backup=/var/lib/fedora-system-monitor/backups;retention=enabled;integrity=ok_2026-07-10
prometheus_tsdb=/var/lib/prometheus/metrics2;retention=30d_or_5GB_first;size_growth_measured_about_96.9KiB_per_minute;projection_about_4.2GiB_per_30d;activity=826417
prometheus_external_filesystems=real_fuseblk_under_/run/media_included_via_execute_only_ACL;virtual+tmpfs+overlay+squashfs+erofs+portal_FUSE_excluded;disconnected_media_absent_without_target_failure
monitor_external_labels=Ventoy+VTOYEFI+VEEAMRE+Seagate_Expansion_Drive;identity=filesystem_UUID_or_hardware_serial_hash;never_dev_sdX
incident=external-ntfs-disconnect-during-mounted-io;first_seen=2026-07-09T19:07:00+02:00;status=OPEN;details=INCIDENT_REGISTRY.md
repo=/home/daniele/MegaVault
nvme=KXG8AZNV1T02_LA_KIOXIA size=953.9GiB
external_seagate=/run/media/daniele/Seagate Expansion Drive ntfs source=udisks_encrypted_volume_mapping size=3.5TiB
external_ntfs=/run/media/daniele/09FA16D309FA16D3 ntfs size=155.9GiB role=UNKNOWN
t7=name=T7 normally=physically_disconnected_or_USB_present_unmounted mount_when_job_active=/mnt/T7_BACKUP ext4 label=T7_BACKUP uuid=4c75ac03-4c73-43f8-afd9-f90db49a74fc model=Samsung_PSSD_T7_Shield serial=S6YGNS0Y903440H size=931.5GiB free_about=761GiB persistent_fstab=yes udisks_hint=T7 activity=684219
recovery_media=historical_distinct_vfat label=VEEAMRE uuid=16B8-BC99 size=14.6GiB disconnected=2026-07-12T01:09:47+02:00
storage_health=T7_identity_verified+Restic_full_read_check_PASS_2026-07-12+connect_backup_unmount_PASS

BACKUP_STORAGE:
current_backup_policy=Restic_encrypted_to_T7;backup_every_physical_connect_via_udev+systemd;forget_each_success;light_check+prune_weekly_max;full_check_monthly_max;retention=7d+5w+12m+3y;activity=684219
repository=/mnt/T7_BACKUP/restic-fedora;id=5872c043e0;snapshots=2;full_check_historical=3955/3955_packs_no_errors;current_light_check=198/198_packs_5percent_PASS;restore_SHA256=PASS
credential=/etc/credstore.encrypted/t7-restic-password;mode=root_root_0600;plaintext=systemd_tmpfs_only;external_escrow=pending_user
rotated_media_rule=mount_paths_and_device_names_can_change;re-enumerate_before_conclusion
t7_rule=name_T7+backup_target_T7_BACKUP;identify_by_model+serial+uuid+separate_mount;never_assume_/dev/sdX;sync+normal_unmount_before_safe_disconnect_notice

CONSTRAINTS:
constraint=current_local_paths_use_/home/daniele_and_/run/media/daniele
constraint=large_artifacts_outside_MegaVault
constraint=backup/cleanup_requires_current_findmnt+lsblk+df
constraint=do_not_prune/delete/format/unlock_without_explicit_user_intent

OPEN:
open=offsite_second_copy_not_configured
open=T7_Restic_password_external_escrow_pending_user
