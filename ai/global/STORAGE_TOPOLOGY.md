# STORAGE_TOPOLOGY
VERSION=4
STATUS=ACTIVE
MODE=codex_first
FORMAT=ultracompressed
SOURCE=HOST_PROFILE+findmnt+df+lsblk_2026-07-09
PROTOCOL=../MEGAVAULT_PROTOCOL.md
HOST_PROFILE=HOST_PROFILE.md
HUMAN=../../human/global/STORAGE_TOPOLOGY.md

CURRENT_FEDORA:
host=fedora
machine=Lenovo_ThinkPad_P14s_Gen_5_AMD
root=/dev/mapper/luks-0c261c5f-02dd-484f-b266-13ff4ee02abb btrfs encrypted size=951.3GiB available=935.9GiB mounts=/,/home
home=/home/daniele
repo=/home/daniele/MegaVault
nvme=KXG8AZNV1T02_LA_KIOXIA size=953.9GiB
external_seagate=/run/media/daniele/Seagate Expansion Drive ntfs source=udisks_encrypted_volume_mapping size=3.5TiB
external_ntfs=/run/media/daniele/09FA16D309FA16D3 ntfs size=155.9GiB role=UNKNOWN
t7=/run/media/daniele/Ventoy exfat device=/dev/sdb1 size=931.5GiB
recovery_media=/run/media/daniele/VEEAMRE vfat device=/dev/sdc1 size=14.6GiB
storage_health=mounted_filesystems_readable_at_2026-07-09_scan;full_backup_health_not_tested

BACKUP_STORAGE:
current_backup_policy=UNKNOWN_after_Fedora_migration
rotated_media_rule=mount_paths_and_device_names_can_change;re-enumerate_before_conclusion
t7_rule=currently_Ventoy;do_not_assume_backup_role_without_live_verification

CONSTRAINTS:
constraint=current_local_paths_use_/home/daniele_and_/run/media/daniele
constraint=large_artifacts_outside_MegaVault
constraint=backup/cleanup_requires_current_findmnt+lsblk+df
constraint=do_not_prune/delete/format/unlock_without_explicit_user_intent

OPEN:
open=current_Fedora_backup_repository_and_retention_UNKNOWN
open=external_NTFS_and_T7_current_operational_roles_UNKNOWN
