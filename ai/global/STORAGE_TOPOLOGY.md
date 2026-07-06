# STORAGE_TOPOLOGY
VERSION=2
STATUS=ACTIVE
MODE=codex_first
FORMAT=ultracompressed
DOC_CLASS=topology
LIFECYCLE=ACTIVE
AUTHORITY_LEVEL=L2
SOURCE_OF_TRUTH=yes
SOURCE=HOST_PROFILE+Get-Disk+Get-Volume_2026-07-05
PROTOCOL=../MEGAVAULT_PROTOCOL.md
HOST_PROFILE=HOST_PROFILE.md
HUMAN=../../human/global/STORAGE_TOPOLOGY.md

CURRENT_WINDOWS:
host=DANIELE_PC
machine=Lenovo_ThinkPad_P14s_Gen_5_AMD
root_volume=C:\ NTFS Windows size=951.5GB free=804.0GB disk=KXG8AZNV1T02_LA_KIOXIA_NVMe_953.9GB
documents_root=C:\Users\seste\Documents
repo=C:\Users\seste\Documents\megavault_content_aware_merge_20260705
external_D=D:\ Seagate_Expansion_Drive NTFS USB size=3570.0GB free=32.3GB serial=NAA37NFE
volume_E=E:\ NTFS fixed size=155.9GB free=116.5GB role=UNKNOWN
t7=not_connected_current_scan
storage_health=current_disks_online_healthy

BACKUP_STORAGE:
veeam=VeeamEndpointBackupSvc_running;target_UNKNOWN;use_ProgramData_Veeam_DB/logs_if_diagnosing
rotated_media_rule=drive_letters_can_change;re-enumerate_before_conclusion
t7_rule=do_not_assume_T7_mounted;current_scan_absent;verify_before_use
backblaze=Windows_client_not_detected;Backblaze_B2_mentions_may_be_legacy_or_remote_until_reverified

CONSTRAINTS:
constraint=Windows_paths_use_C:\Users\seste\Documents\...
constraint=large_artifacts_outside_MegaVault
constraint=backup/cleanup_requires_current_Get-Disk+Get-Volume
constraint=do_not_apply_Linux_ext4_mount_rules_to_current_host
constraint=do_not_prune/delete/format_without_explicit_user_intent

LEGACY_2026-06_SURFACE_MINT:
status=historical_not_primary
legacy_host=daniele-Surface-Pro
legacy_root=/dev/sda2 ext4 on Samsung_PSSD_T7_Shield USB
hub=SABRENT_HB-BUP7 powered_USB_hub;single_Surface_USB_path
legacy_backup=/media/daniele/Seagate6TB2/home-backups
legacy_transfer=/media/daniele/Seagate6TB2/vecchio disco
projects=mint-cloud-backup(restic_Backblaze_B2),backup_docs(home_rsync),surface-recovery-hardening(BitLocker_readonly_transfer)

OPEN:
open=current_Veeam_repository_letter_and_retention_UNKNOWN
open=current_T7_role_UNKNOWN_until_connected
