# HOST_PROFILE
VERSION=3
STATUS=MANDATORY_GLOBAL_CONTEXT
MODE=codex_first
FORMAT=ultracompressed
AUTHORITY=hardware_constraints
UPDATED=2026-06-21T21:47:07+02:00
PROMPT=483920

META:
current_host=ThinkPad_P14s_Gen_5_AMD
legacy_host=daniele-Surface-Pro
user=UNKNOWN
role=current_primary_workstation_for_Codex_Desktop_Windows,Android_development_testing,GitHub_repositories,MegaVault_docs,possible_Codex_Desktop_Android_plugin
source=operator_prompt_483920;no_live_host_scan
read_after=ai/MEGAVAULT_PROTOCOL.md
human=../../human/global/HOST_PROFILE.md
protocol=../MEGAVAULT_PROTOCOL.md
global_rules=../GLOBAL_RULES.md
rule=current_host_wins_for_new_work;legacy_host_used_only_for_historical_projects_services_paths

CURRENT_HOST:
vendor=Lenovo
model=ThinkPad_P14s_Gen_5_AMD
listing_model=21ME003SXX
os=Windows_11_Pro
role=primary_current_host
codex_surface=Codex_Desktop_Windows
hostname_windows=UNKNOWN
windows_username=UNKNOWN
windows_build=UNKNOWN
timezone=UNKNOWN

CURRENT_HARDWARE:
cpu=AMD_Ryzen_7_PRO_8840HS
ram=32GB
internal_ssd=1TB
display=14in_WUXGA_1920x1200_IPS_400nits_Low_Power_100pct_sRGB
gpu=UNKNOWN
firmware=UNKNOWN
ssd_serial=UNKNOWN
bitlocker=UNKNOWN

CURRENT_WINDOWS_OPERATIONS:
shell_default=PowerShell
path_syntax=Windows_paths_C:\\...;quote_paths_with_spaces
repo_workspace=Windows_GitHub_repo_workspace_UNKNOWN
codex_desktop=yes_current_target
sandbox_permissions=verify_from_Codex_session_not_assume
line_endings=avoid_mass_line_ending_churn;restore_if_checkout_only
preferred_search=rg_if_available_else_PowerShell_Select-String
avoid=Linux_absolute_paths_for_current_host_unless_inside_WSL_or_remote

CURRENT_ANDROID:
role=Android_development_testing_possible_plugin_use
codex_android_plugin=possible;verify_live_before_use
android_sdk_windows_path=UNKNOWN
adb_windows_path=UNKNOWN
adb_devices=UNKNOWN
phone_ips=UNKNOWN
device_pairing=UNKNOWN
wsl_status=UNKNOWN
docker_status=UNKNOWN
constraint=do_not_assume_Linux_ADB_paths_systemd_service_or_old_phone_IPs_on_Windows
constraint=verify_live_Android_device_plugin_ADB_before_build_test_release_claims

CURRENT_STORAGE:
internal_ssd_capacity=1TB
windows_system_drive=UNKNOWN
repo_paths=UNKNOWN
backup_paths_windows=UNKNOWN
external_drives_current=UNKNOWN
usb_topology_current=UNKNOWN
constraint=do_not_apply_Surface_USB_root_hub_bottleneck_to_ThinkPad_without_live_verification
constraint=do_not_run_backup_storage_runtime_scripts_from_docs_task

CURRENT_NETWORK:
hostname=UNKNOWN
lan_ip=UNKNOWN
wifi=UNKNOWN
tailscale=UNKNOWN
phone_ips_current=UNKNOWN
oracle_vm=see_REMOTE_ORACLE;verify_before_runtime_changes
constraint=do_not_assume_Surface_LAN_IP_or_Tailscale_address_for_current_host

CURRENT_SERVICES:
windows_services=UNKNOWN
codex_desktop_state=UNKNOWN
android_plugin_state=UNKNOWN
github_auth_state=UNKNOWN
wsl=UNKNOWN
docker=UNKNOWN
backup_agents=UNKNOWN
constraint=do_not_translate_legacy_systemd_units_to_Windows_services_without_live_inventory

REMOTE_ORACLE:
host=ubuntu@150.230.148.128
instance=instance-20260201-1126
ssh_key_legacy_path=/home/daniele/codex-workspace/projects/vm_oracle/ssh-key-2026-02-01.key
kuma_admin=ssh_tunnel http://127.0.0.1:3001 -> VM 127.0.0.1:3002
kuma_public_push=http://150.230.148.128:3001/api/push/<token>
kuma_container=uptime-kuma
kuma_image=louislam/uptime-kuma:2.3.2
kuma_db=/opt/uptime-kuma/data/kuma.db
constraints=backup_DB_before_direct_Kuma_sqlite,do_not_commit_tokens,verify_Windows_ssh_key_path_before_use,do_not_assume_remote_reachable

LEGACY_SURFACE_PRO:
status=legacy_historical_context_not_current_primary_host
host=daniele-Surface-Pro
role_old=primary_Linux_Mint_workstation_for_Codex,Android,backup,monitoring,automation
source_old=live_commands+MegaVault_docs+installed_services+operator_physical_inventory
os_old=Linux_Mint_22.3_Zena;Ubuntu_noble;kernel=6.19.8-surface-3;desktop=XFCE;session=x11
hardware_old=Microsoft_Surface_Pro;Intel_Core_i5-7300U_2c4t;ram_about_7.7GiB;Intel_HD_620;firmware=239.871.768
constraints_old=low_core_count,limited_ram,old_surface_firmware,thermal_battery_laptop_profile

LEGACY_SURFACE_STORAGE:
root=/dev/sda2 ext4 on Samsung_PSSD_T7_Shield_USB serial=S6YGNS0Y903440H
efi=/dev/sda1 vfat /boot/efi
internal_disk=/dev/nvme0n1 KBG30ZPZ256G_TOSHIBA serial=285Y11F5YMAS Windows_BitLocker_partitions_not_root
external_source=/dev/sdb ST4000LM024-2AN17V serial=WFF0FEX8 BitLocker_source_historical_readonly_required
external_backup=/dev/sdc ST6000DM003-2CY186 serial=ZCT3KG54 ext4 label=Seagate6TB mounted=/media/daniele/Seagate6TB2
backup_path=/media/daniele/Seagate6TB2/home-backups
transfer_dest=/media/daniele/Seagate6TB2/vecchio disco
hub=SABRENT_HB-BUP7_powered_USB_hub;36W;single_Surface_USB_port;Realtek_RTS5411/0bda:0411
topology=Surface_Pro_USB_port->SABRENT_HB-BUP7->Samsung_T7_root+Seagate_4TB_source+Seagate_6TB_backup
legacy_constraints=root_on_USB_SSD,root_on_USB_hub,source_and_destination_share_USB_hub,large_parallel_IO_can_affect_all_attached_storage,avoid_rsync_delete,do_not_auto_resume_after_storage_error

LEGACY_SURFACE_ANDROID:
adb=/home/daniele/Android/Sdk/platform-tools/adb version=37.0.0-14910828
android_sdk=/home/daniele/Android/Sdk
sdkmanager=/home/daniele/Android/Sdk/cmdline-tools/latest/bin/sdkmanager
adb_service=adb-wifi-autoconnect.service user enabled+active_on_legacy_Mint
phone_pixel=Pixel_8a;host_old=192.168.1.37;tokens=Pixel_8a,akita,52131JEKB01070;current=not_connected_at_2026-06-07
phone_tcl=TCL_6102H;host_old=192.168.1.200;tokens=6102H,QCGADUVOSSEYFES4,Android-3.local;current_adb_devices_empty_at_2026-06-07
legacy_constraints=manual_pair_default,mdns_can_be_stale,do_not_adb_kill_server_without_explicit_approval,verify_with_adb_devices_l_not_avahi_only

LEGACY_SURFACE_SERVICES:
status=legacy_Mint_systemd_snapshot;do_not_assume_running_on_Windows
user_active=adb-wifi-autoconnect,mint-freeze-forensics,mint-update-tracker,system-service-dashboard,transfer-vecchio-disco-adaptive-throttle,windowtabnotes,aw-server,aw-watcher-afk,aw-watcher-window,aw-watcher-media-player
user_timers=amici_fb,android-sdk-auto-update,home-backup-kuma-push,home-backup-retention-kuma-push,home-incremental-backup,mint-manual-updates,mint-resource-guardian,mint-update-tracker,mint-xfce-layout-guard,parcel-tracker
system_services=mint-cloud-backup-monitor,mint-cloud-backup-dashboard,transfer-usb-io-watchdog,disk-usage-monitor,local-zram-swap,logind-power-intent-watch
system_timers=mint-cloud-backup,mint-cloud-backup-kuma-push,disk-usage-monitor,dpkg-db-backup,mintupdate-automation-autoremove,mintupdate-automation-upgrade
service_constraints=legacy_only,verify_systemd_plus_state_files_on_legacy_host_before_changes,do_not_revive_removed_antifreeze_units

LEGACY_FREEZE_IO_BACKUP:
freeze_forensics=mint-freeze-forensics.service user enabled/running_on_legacy;sampler=5s;no_remediation
zram_swap_2026-06-10=local-zram-swap.service system enabled active_exited;size=4GiB;priority=100
home_backup_2026-06-06=rsync_exit=137 caused_by_ABORDED_SAFE_load_guard_not_OOM_not_disk_full_not_kernel_IO_error
backup_local_home=home-incremental-backup.timer;dest=/media/daniele/Seagate6TB2/home-backups
cloud_root=mint-cloud-backup system timer/restic/Backblaze_B2;state=/var/lib/mint-cloud-backup;dashboard=127.0.0.1:8765
monitoring=Oracle_VM_Uptime_Kuma_push_monitors_legacy_Mint_ids_3_17
constraints=legacy_Mint_storage_freeze_rules_remain_relevant_only_when_touching_old_projects_services_backups

DEPLOYMENT_CONSTRAINTS:
current_windows=use_PowerShell_and_Windows_paths;verify_tool_locations_live;do_not_assume_WSL_Docker_BitLocker_Android_SDK_backup_paths
android=builds/tests may need real device/plugin online;verify current Windows ADB/plugin before claims
github=repo workspace under Windows UNKNOWN;verify remote/status before edits;avoid mass_line_ending_changes
oracle=remote runtime must be verified over SSH;Kuma direct DB edits require backup+restart+verify
legacy_mint=Surface_Linux_paths_systemd_units_USB_topology_are_historical_context_unless explicitly working_on_legacy_host
economic=direct budget UNKNOWN;documented economic/quota constraint is OCI backup remote at assumed 22GiB limit,avoid paid/quota-changing/destructive actions without explicit operator approval

DNB:
dnb=do not call the legacy_Mint_Surface host the current primary host
dnb=do not use /home/daniele paths,systemd units,ADB Linux paths,Surface USB topology as current Windows facts
dnb=do not invent hostname,firmware,SSD serial,Android SDK path,phone IPs,Windows services,WSL,Docker,BitLocker,backup paths
dnb=do not treat mDNS/Avahi or old phone IPs as Android device proof
dnb=do not create duplicate services/docs/slugs
dnb=do not run destructive storage/backup/remediation commands without explicit user intent
dnb=do not use human docs as operational authority when AI doc/protocol/profile disagree

OPEN:
open=Windows_hostname_UNKNOWN
open=Windows_username_UNKNOWN
open=Windows_build_UNKNOWN
open=firmware_UNKNOWN
open=SSD_serial_UNKNOWN
open=Windows_BitLocker_status_UNKNOWN
open=Windows_repo_workspace_paths_UNKNOWN
open=Android_SDK_path_Windows_UNKNOWN
open=ADB_path_Windows_UNKNOWN
open=current_phone_IPs_and_ADB_state_UNKNOWN
open=Windows_services_Codex_Desktop_Android_plugin_state_UNKNOWN
open=WSL_status_UNKNOWN
open=Docker_status_UNKNOWN
open=backup_paths_Windows_UNKNOWN
open=Oracle_VM_current_reachability_UNKNOWN
