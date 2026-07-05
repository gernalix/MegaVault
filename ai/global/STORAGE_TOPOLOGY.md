# STORAGE_TOPOLOGY
VERSION=1
STATUS=LEGACY_SURFACE_SNAPSHOT_CURRENT_WINDOWS_UNKNOWN
MODE=codex_first
FORMAT=ultracompressed
SOURCE=HOST_PROFILE+lsblk_live_2026-06-08;current_windows_not_scanned_prompt_483920
PROTOCOL=../MEGAVAULT_PROTOCOL.md
HOST_PROFILE=HOST_PROFILE.md
HUMAN=../../human/global/STORAGE_TOPOLOGY.md

CURRENT_HOST_STORAGE:
host=ThinkPad_P14s_Gen_5_AMD
os=Windows_11_Pro
internal_ssd=1TB
system_drive=UNKNOWN
volume_layout=UNKNOWN
bitlocker=UNKNOWN
repo_workspace=UNKNOWN
backup_paths_windows=UNKNOWN
external_drives_current=UNKNOWN
usb_topology_current=UNKNOWN
constraint=do_not_apply_legacy_Surface_USB_hub_topology_to_current_ThinkPad_without_live_verification

LEGACY_SURFACE_STORAGE:
host=daniele-Surface-Pro
root=/dev/sda2
root_fs=ext4
root_mount=/
root_disk=/dev/sda Samsung_PSSD_T7_Shield serial=S6YGNS0Y903440H usb 931.5G
efi=/dev/sda1 vfat /boot/efi
internal_disk=/dev/nvme0n1 KBG30ZPZ256G_TOSHIBA serial=285Y11F5YMAS nvme 238.5G
internal_role=Windows_BitLocker_partitions_not_Linux_root
external_source=/dev/sdb ST4000LM024-2AN17V serial=WFF0FEX8 usb 3.6T
external_source_partition=/dev/sdb2 BitLocker 3.5T
external_backup=/dev/sdc ST6000DM003-2CY186 serial=ZCT3KG54 usb 5.5T
external_backup_partition=/dev/sdc1 ext4 label=Seagate6TB mounted=/media/daniele/Seagate6TB2
backup_path=/media/daniele/Seagate6TB2/home-backups
transfer_dest=/media/daniele/Seagate6TB2/vecchio disco

LEGACY_SURFACE_USB_TOPOLOGY:
hub=SABRENT_HB-BUP7_powered_USB_hub
hub_power=36W
host_connection=single_Surface_Pro_USB_port
kernel_chipset=Realtek_RTS5411/0bda:0411
path=Surface_Pro_USB_port->SABRENT_HB-BUP7->Samsung_T7_root+Seagate_4TB_source+Seagate_6TB_backup
port1=Samsung_PSSD_T7_Shield_root_Linux
port2=Seagate_ST4000LM024_4TB_BitLocker_source
port3=Seagate_ST6000DM003_6TB_backup_destination

LEGACY_SURFACE_SYNTHETIC_VIEW:
node=Surface;role=host;storage=root_on_T7_USB
node=T7_root;device=/dev/sda;criticality=critical;risk=host_freeze_if_USB_hub_or_disk_stalls
node=4TB_BitLocker_source;device=/dev/sdb2;criticality=important;mode=readonly_required
node=6TB_backup_destination;device=/dev/sdc1;criticality=critical;mount=/media/daniele/Seagate6TB2
node=SABRENT_HB-BUP7;criticality=critical;role=shared_USB_path_for_root_source_backup

LEGACY_SURFACE_PROJECT_STORAGE_RELATIONS:
project=mint-cloud-backup;source=/;destination=Backblaze_B2_restic;state=/var/lib/mint-cloud-backup;cache=/var/cache/mint-cloud-backup/restic
project=backup_docs;source=/home/daniele;destination=/media/daniele/Seagate6TB2/home-backups;service=home-incremental-backup.service
project=surface-recovery-hardening;source=/dev/sdb2 BitLocker readonly;destination=/media/daniele/Seagate6TB2/vecchio disco;guard=transfer-usb-io-watchdog.service
project=mint-freeze-forensics;observes=root_disk+swap+USB_IO+proc_io;state=/home/daniele/.local/state/mint-freeze-forensics
project=mint-update-tracker;db=/home/ubuntu/sync_root/db/software_audit.db;storage=root_disk_USB
project=windowtabnotes;db=/home/daniele/.local/share/windowtabnotes/windowtabnotes.sqlite3;storage=root_disk_USB

CONSTRAINTS:
constraint=legacy_Surface_root_on_USB_SSD
constraint=legacy_Surface_root_on_USB_hub
constraint=legacy_Surface_source_and_destination_share_USB_hub
constraint=legacy_Surface_large_parallel_IO_can_affect_root_source_destination
constraint=BitLocker_source_readonly_required
constraint=avoid_rsync_delete
constraint=verify_mounts_not_autofs_wrapper
constraint=do_not_auto_resume_after_storage_error
constraint=large_artifacts_outside_MegaVault

OPEN:
open=current_Windows_drive_letters_mounts_BitLocker_backup_paths_UNKNOWN
open=exact_Surface_generation_UNKNOWN
open=current_BitLocker_source_mount_state_UNKNOWN_not_checked_for_write
