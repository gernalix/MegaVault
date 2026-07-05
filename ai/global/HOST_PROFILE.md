# HOST_PROFILE
VERSION=2
STATUS=MANDATORY_GLOBAL_CONTEXT
MODE=codex_first
FORMAT=ultracompressed
AUTHORITY=hardware_constraints
UPDATED=2026-06-07T19:30:00+02:00
PROMPT=418572

META:
host=daniele-Surface-Pro
user=daniele
role=primary Linux Mint workstation for Codex,Android,backup,monitoring,automation
source=live_commands+MegaVault_docs+installed_services+operator_physical_inventory
read_after=ai/MEGAVAULT_PROTOCOL.md
human=../../human/global/HOST_PROFILE.md
protocol=../MEGAVAULT_PROTOCOL.md
global_rules=../GLOBAL_RULES.md

OS:
distro=Linux Mint 22.3 Zena
base=Ubuntu noble
kernel=6.19.8-surface-3 #3 SMP PREEMPT_DYNAMIC 2026-05-09
arch=x86_64
desktop=XFCE
session=x11
host_model=Microsoft Corporation Surface Pro
firmware=239.871.768;date=2015-11-07
battery=BAT1 M1009169;status=Not_charging;capacity=48%

HARDWARE:
cpu=Intel Core i5-7300U @2.60GHz
cpu_topology=2c/4t;max=3.5GHz;min=400MHz;VT-x=yes
ram=8054644kB about 7.7GiB
swap=/swapfile 8G;used_at_2026-06-07=2.9G
gpu=Intel HD Graphics 620;driver=i915
constraints=low_core_count,limited_ram,old_surface_firmware,USB_root_disk,USB_hub_critical_path,thermal/battery_laptop_profile
unknown=exact_Surface_generation,DIMM_layout

STORAGE:
root=/dev/sda2 ext4 rw,noatime,errors=remount-ro,stripe=8191;size=915.3G;used=96.2G;avail=772.5G
efi=/dev/sda1 vfat mounted /boot/efi
root_disk=/dev/sda Samsung PSSD T7 Shield serial=S6YGNS0Y903440H usb 931.5G
internal_disk=/dev/nvme0n1 KBG30ZPZ256G TOSHIBA serial=285Y11F5YMAS nvme 238.5G;Windows/BitLocker partitions;not_root
external_source=/dev/sdb ST4000LM024-2AN17V serial=WFF0FEX8 usb 3.6T;partition /dev/sdb2 BitLocker;historical transfer source
external_backup=/dev/sdc ST6000DM003-2CY186 serial=ZCT3KG54 usb 5.5T;/dev/sdc1 ext4 label=Seagate6TB uuid=75e5363d-6736-4a7e-84be-5242f4735a27 mounted /media/daniele/Seagate6TB2 rw,noatime
backup_path=/media/daniele/Seagate6TB2/home-backups
transfer_dest=/media/daniele/Seagate6TB2/vecchio disco
storage_constraints=root_on_USB_SSD,root_on_USB_hub,large_USB_HDD_workloads,shared_USB_bandwidth,shared_USB_controller,BitLocker_source_readonly_required,avoid_rsync_delete,verify_mounts_not_autofs_wrapper,do_not_assume_independent_storage_paths

HUB_USB:
vendor=SABRENT
model=HB-BUP7
name=SABRENT USB Hub Active 3.2 x1
ports=7
power_supply=36W
powered=yes
individual_switches=yes
kernel_chipset=Realtek RTS5411/0bda:0411 hub observed by lsusb
topology=all_primary_external_storage_connected_through_this_hub
host_connection=single_USB_port_on_Surface_Pro
live_tree=Bus002 root_hub xhci_hcd 5000M -> Realtek hub Dev002 -> ports 1/2/3 mass_storage + port4 nested hub

TOPOLOGY:
path=Surface_Pro_USB_port -> SABRENT_HB-BUP7_powered_hub -> Samsung_PSSD_T7_Shield(root_Linux),Seagate_ST4000LM024_4TB_BitLocker_source,Seagate_ST6000DM003_6TB_backup_destination
port1=Samsung_PSSD_T7_Shield /dev/sda root Linux
port2=Seagate_ST4000LM024_4TB_BitLocker_source /dev/sdb
port3=Seagate_ST6000DM003_6TB_backup_destination /dev/sdc
constraints=single_usb_root_path=yes,shared_usb_bandwidth=yes,shared_usb_controller=yes,USB_hub_is_critical_infrastructure=yes,storage_performance_and_freeze_investigations_must_consider_hub_topology=yes,large_parallel_IO_can_affect_all_attached_storage=yes,do_not_assume_independent_storage_paths=yes

PHONES:
adb=/home/daniele/Android/Sdk/platform-tools/adb version=37.0.0-14910828
android_sdk=/home/daniele/Android/Sdk
sdkmanager=/home/daniele/Android/Sdk/cmdline-tools/latest/bin/sdkmanager
adb_service=adb-wifi-autoconnect.service user enabled+active
phone_pixel=Pixel 8a;host=192.168.1.37;tokens=Pixel_8a,akita,52131JEKB01070;current=not_connected_at_2026-06-07
phone_tcl=TCL 6102H;host=192.168.1.200;tokens=6102H,QCGADUVOSSEYFES4,Android-3.local;historical_models=6102H_EEA,TCL_6102H;current_adb_devices_empty_at_2026-06-07
adb_constraints=manual_pair_default,auto_pairing_UI_disabled,mdns_can_be_stale,do_not_adb_kill_server_without_explicit_approval,verify_with_adb_devices_l_not_avahi_only

VM_ORACLE:
host=ubuntu@150.230.148.128
instance=instance-20260201-1126
ssh_key=/home/daniele/codex-workspace/projects/vm_oracle/ssh-key-2026-02-01.key
kuma_admin=ssh_tunnel http://127.0.0.1:3001 -> VM 127.0.0.1:3002
kuma_public_push=http://150.230.148.128:3001/api/push/<token>
kuma_container=uptime-kuma
kuma_image=louislam/uptime-kuma:2.3.2
kuma_db=/opt/uptime-kuma/data/kuma.db
kuma_role=black_box_history_alerting_visualization;not_remediation;admin_not_public_since_2026-06-12
oracle_backup=/etc/oracle_backup/oracle_backup.env,/var/lib/oracle_backup,/var/log/oracle_backup
oracle_constraints=backup_DB_before_direct_Kuma_sqlite,do_not_commit_tokens,remote_quota_critical_2026-06-05 used=22.262GB assumed_limit=22GiB,do_not_no-lock_prune_without_explicit_approval

SERVICES:
user_active=adb-wifi-autoconnect,mint-freeze-forensics,mint-update-tracker,system-service-dashboard,transfer-vecchio-disco-adaptive-throttle,windowtabnotes,aw-server,aw-watcher-afk,aw-watcher-window,aw-watcher-media-player
user_timers=amici_fb,android-sdk-auto-update,home-backup-kuma-push,home-backup-retention-kuma-push,home-incremental-backup,mint-manual-updates,mint-resource-guardian,mint-update-tracker,mint-xfce-layout-guard,parcel-tracker
system_services=mint-cloud-backup-monitor,mint-cloud-backup-dashboard,transfer-usb-io-watchdog,disk-usage-monitor,local-zram-swap,logind-power-intent-watch
system_timers=mint-cloud-backup,mint-cloud-backup-kuma-push,disk-usage-monitor,dpkg-db-backup,mintupdate-automation-autoremove,mintupdate-automation-upgrade
service_constraints=distinguish_user_vs_system,verify_systemd_plus_state_files,avoid_parallel_units,do_not_revive_removed_antifreeze_units,document_persistent_service_changes

FREEZE_HISTORY:
project=mint-freeze-forensics
service=mint-freeze-forensics.service user enabled/running;sampler=5s;no_remediation
guardian=mint-resource-guardian.timer enabled;noninteractive_alert_under_systemd;no_auto_kill
legacy_removed=freeze-reboot-monitor,freeze-zram-swap,screen-watchdog,system-watchdog,os-observer-autofix,mint_freeze_diag,freeze_reboot_monitor
zram_swap_2026-06-10=local-zram-swap.service system enabled active_exited;unit=/etc/systemd/system/local-zram-swap.service;script=/usr/local/sbin/local-zram-swap;size=4GiB;algorithm=zstd_if_available_else_lz4;priority=100;disk_swap_fallback=/swapfile priority=-1;no_daemon,no_watchdog,no_reboot
kuma_group=Mint Freeze Analysis id=12
kuma_monitors=Freeze_Gaps id=13,PSI_Memory id=14,PSI_IO id=15,Guardian_Alerts id=16,Forensics_Alive id=17
known=freeze/gap attribution needs real corpus; heuristic until >=3 real freeze events
constraint=no automatic reboot/restart/kill remediation during freeze work

IO_BOTTLENECK_HISTORY:
home_backup_2026-06-06=rsync_exit=137 caused by runtime load guard ABORTED_SAFE load_x100 622>600;not OOM;not disk full;not kernel IO error
backup_threshold=normal_load_x100_max=600
transfer_history=multi_TB USB BitLocker->Seagate6TB2 rsync stressed shared SABRENT hub/USB controller;watch kernel USB/I/O/JBD2/EXT4
watchdog=transfer-usb-io-watchdog.service enabled;data_safety_guard_not_generic_antifreeze
constraint=do_not_auto_resume_after_storage_error;verify exact rsync process,mounts,/proc IO and HUB_USB topology before health claims

BACKUP_INFRA:
local_home=home-incremental-backup.timer;dest=/media/daniele/Seagate6TB2/home-backups;guarded load/I/O behavior;Kuma push split backup vs retention
cloud_root=mint-cloud-backup system timer/restic/Backblaze_B2;state=/var/lib/mint-cloud-backup;dashboard=127.0.0.1:8765;Kuma monitor id=3
oracle=oracle-backup-service restic+SQLite snapshots on VM;remote OCI quota critical;local emergency_repo must not be deleted while remote degraded
constraints=never_print_env_tokens,do_not_prune/unlock/check/forget casually,prove_no_live_backup_before_unlock,ABORTED_SAFE_not_successful_backup

MONITOR_INFRA:
kuma=Oracle VM Uptime Kuma;Telegram notification id=1;push monitors
active_push_after_482917=cloud_backup id=3,mint-home-backup id=4,amici_fb id=5,disk-usage-monitor id=6,parcel-tracker id=7,mint-home-backup-retention id=9,software_audit_mint id=11,freeze_monitors id=13-17
disabled_obsolete=mint_heartbeat id=1,rsync-transfer id=2,codex-token-watcher id=10
local_dashboard=system-service-dashboard.service;localhost Linux Mint read-only dashboard
monitor_constraints=Kuma_DOWN_is_signal_not_truth,local_state_files_authoritative_for_job_semantics,do_not_silence_real_failures

LOGIND_POWER_INTENT:
service=logind-power-intent-watch.service system enabled;unit=/etc/systemd/system/logind-power-intent-watch.service;script=/home/daniele/.local/bin/logind-power-intent-watch
purpose=attribute_future_org.freedesktop.login1.Manager_Reboot/PowerOff/Halt/Suspend/Hibernate_requests;source=dbus-monitor_system_bus+busctl_status_sender
log=/var/log/logind-power-intent-watch/events.jsonl;fields=timestamp,sender,member,pid,uid,comm,cmdline,unit,user_unit,cgroup,session,audit_session
constraints=observes_only_no_blocking,no_reboot,no_private_window_titles,no_periodic_spam;verify=systemctl status logind-power-intent-watch.service && sudo tail -n 5 /var/log/logind-power-intent-watch/events.jsonl

DEPLOYMENT_CONSTRAINTS:
mint=prefer_existing_user/systemd_units,document_runtime_changes,avoid_focus_stealing_UI,keep_scripts_local_paths_stable
android=builds/tests may need real device online;current ADB empty blocks connected tests;Pixel/TCL pairing can drift by port/IP
oracle=remote runtime must be verified over SSH;Kuma direct DB edits require backup+restart+verify
storage=large transfers/backups must be conservative due root+source+destination sharing one powered USB hub,USB root/storage path,and load guard history
economic=direct budget UNKNOWN;documented economic/quota constraint is OCI backup remote at assumed 22GiB limit,avoid paid/quota-changing/destructive actions without explicit operator approval

DNB:
dnb=do not ignore HOST_PROFILE for performance,monitoring,automation,service,system tuning,Android tooling,backup,storage,Linux Mint,freeze work
dnb=do not treat mDNS/Avahi as Android device proof
dnb=do not create duplicate services/docs/slugs
dnb=do not run destructive storage/backup/remediation commands without explicit user intent
dnb=do not use human docs as operational authority when AI doc/protocol/profile disagree

OPEN:
open=exact Surface generation not exposed by DMI
open=exact Android phone online state changes frequently; verify live with adb devices -l
open=Oracle VM hardware shape not documented in local sources used here
open=direct monthly budget UNKNOWN; only quota/cost-sensitive constraints documented
