# HOST_PROFILE
VERSION=3
STATUS=MANDATORY_GLOBAL_CONTEXT
MODE=codex_first
FORMAT=ultracompressed
AUTHORITY=hardware_constraints
UPDATED=2026-07-05T00:00:00+02:00
SOURCE=local_Windows_CIM+Get-Volume+Get-Disk+tool_versions+user_context

META:
host=DANIELE_PC
user=seste
primary_machine=Lenovo_ThinkPad_P14s_Gen_5_AMD
model=LENOVO_21ME003SFR
role=primary_Windows_11_Pro_workstation_for_Codex,Android,backup,monitoring,automation
path_root=C:\Users\seste\Documents
workspace_current=C:\Users\seste\Documents\megavault_content_aware_merge_20260705
read_after=ai/MEGAVAULT_PROTOCOL.md
human=../../human/global/HOST_PROFILE.md
protocol=../MEGAVAULT_PROTOCOL.md
centralization=host/system/storage/Android_tooling_constraints_authoritative_here;project_docs_keep_project_specific_evidence_only

OS:
os=Microsoft_Windows_11_Pro
version=10.0.26200
build=26200
arch=64-bit
shell=PowerShell/pwsh_on_Windows
pwsh=C:\Program Files\PowerShell\7\pwsh.exe version=7.6.3
git=C:\Program Files\Git\cmd\git.exe version=2.55.0.windows.2
github_desktop=UNKNOWN_not_required_when_git_cli_available

HARDWARE:
cpu=AMD_Ryzen_7_PRO_8840HS_w_Radeon_780M_Graphics
cpu_topology=8c/16t
ram=27.7GiB
bios=R2LET40W_1.21
gpu=Radeon_780M_integrated
constraints=laptop_power/thermal_profile,verify_elevation_for_admin_tasks,do_not_assume_Linux_systemd_or_paths_on_host

STORAGE_CURRENT:
disk0=KXG8AZNV1T02_LA_KIOXIA NVMe serial=8CE3_8E05_0310_B2D3 size=953.9GB online healthy
volume_C=Windows NTFS fixed size=951.5GB free=804.0GB
disk1=Seagate_Expansion USB serial=NAA37NFE size=3726.0GB online healthy
volume_D=Seagate_Expansion_Drive NTFS fixed size=3570.0GB free=32.3GB
volume_E=NTFS fixed size=155.9GB free=116.5GB
t7_current=not_connected_in_2026-07-05_scan
storage_rule=verify_Get-Disk+Get-Volume_before_backup_or_large_IO;drive_letters_can_change;do_not_reuse_Linux_mount_assumptions

ANDROID_WINDOWS:
android_studio=C:\Program Files\Android\Android Studio\bin\studio64.exe version=261.23567.138.0-AI
android_sdk=C:\Users\seste\AppData\Local\Android\Sdk
adb=C:\Users\seste\AppData\Local\Android\Sdk\platform-tools\adb.exe version=1.0.41/37.0.0-14910828
adb_os=Windows_10.0.26200
adb_rule=verify_with_adb_devices_-l;device_IPs_and_pairing_drift;do_not_assume_old_Mint_adb_service_exists

BACKUP_WINDOWS:
veeam_service=VeeamEndpointBackupSvc running automatic
veeam_config=not_exported_this_run;admin/service_permissions_may_apply
veeam_target=UNKNOWN_current;verify_Veeam_DB/logs_and_current_drive_letters_before_action
t7_backup_context=rotated/backup_media_possible;current_scan_no_T7;verify_physical_mount
backblaze_windows=not_detected_by_bzbui_or_default_dir_in_this_scan
backblaze_b2=legacy_or_remote_project_context_until_reverified
backup_rule=never_prune/delete/unlock/format_without_explicit_intent;diagnose_first;report_evidence_paths

REMOTE_ORACLE:
host=ubuntu@150.230.148.128
roles=uptime_kuma,oracle_backup,remote_monitoring
ssh_key_windows=UNKNOWN
ssh_key_legacy_linux=/home/daniele/codex-workspace/projects/vm_oracle/ssh-key-2026-02-01.key
kuma_db=/opt/uptime-kuma/data/kuma.db
remote_rule=remote_Linux_paths_valid_only_on_VM_or_legacy_docs;do_not_commit_tokens;backup_DB_before_direct_Kuma_SQLite

LEGACY_2026-06_SURFACE_MINT:
status=historical_not_primary
legacy_host=daniele-Surface-Pro
os=Linux_Mint_22.3_Zena kernel=6.19.8-surface-3 desktop=XFCE_X11
hardware=Microsoft_Surface_Pro Intel_i5-7300U 2c/4t 7.7GiB_RAM
legacy_root=/dev/sda2 ext4 on Samsung_PSSD_T7_Shield USB via SABRENT_HB-BUP7
legacy_backup=/media/daniele/Seagate6TB2/home-backups;cloud=mint-cloud-backup restic Backblaze_B2
legacy_android=/home/daniele/Android/Sdk;adb_service=adb-wifi-autoconnect.service
services=mint-freeze-forensics,mint-update-tracker,system-service-dashboard,transfer-vecchio-disco-adaptive-throttle,windowtabnotes
rule=all_Surface/Linux_Mint/systemd/ext4/restic_only/home_or_media_paths_here_are_legacy_or_remote;do_not_treat_as_current_Windows_host

DNB:
dnb=do_not_treat_Surface_or_Linux_Mint_as_primary_host
dnb=do_not_convert_remote_VM_Linux_paths_to_Windows_paths
dnb=do_not_treat_mDNS_as_Android_device_proof
dnb=do_not_run_destructive_storage/backup/remediation_commands_without_explicit_user_intent
dnb=do_not_use_human_docs_as_operational_authority_when_AI_doc/protocol/profile_disagree

OPEN:
open=exact_GitHub_Desktop_install_state_UNKNOWN
open=current_Veeam_job_target_UNKNOWN_without_DB/log_review
open=current_Backblaze_policy_UNKNOWN;local_client_not_detected
open=current_Oracle_SSH_key_Windows_path_UNKNOWN
