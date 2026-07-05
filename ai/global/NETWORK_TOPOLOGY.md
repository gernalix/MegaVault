# NETWORK_TOPOLOGY
VERSION=1
STATUS=LEGACY_SURFACE_SNAPSHOT_CURRENT_WINDOWS_UNKNOWN
MODE=codex_first
FORMAT=ultracompressed
SOURCE=ip_live_2026-06-08+HOST_PROFILE+dashboard_status+prompt_458217_kuma_hardening;current_windows_not_scanned_prompt_483920
PROTOCOL=../MEGAVAULT_PROTOCOL.md
HOST_PROFILE=HOST_PROFILE.md
HUMAN=../../human/global/NETWORK_TOPOLOGY.md

CURRENT_LOCAL_HOST:
host=ThinkPad_P14s_Gen_5_AMD
os=Windows_11_Pro
hostname=UNKNOWN
primary_lan=UNKNOWN
primary_ip=UNKNOWN
default_gateway=UNKNOWN
wifi_essid=UNKNOWN
tailscale=UNKNOWN
loopback=127.0.0.1/8_assumed_standard
constraint=do_not_assume_legacy_Surface_IP_Tailscale_or_phone_IPs_for_current_host

LEGACY_SURFACE_LOCAL_HOST:
host=daniele-Surface-Pro
primary_lan=wlp1s0
primary_ip=192.168.1.97/24
default_gateway=192.168.1.1
wifi_essid=Alaska_5G
wifi_frequency=5.22GHz
wifi_bitrate=468Mb/s
wifi_power_management=off
tailscale=tailscale0 100.68.141.10/32 fd7a:115c:a1e0::b434:8d0a/128
loopback=127.0.0.1/8

LEGACY_SURFACE_LOCAL_ENDPOINTS:
endpoint=system-service-dashboard;url=http://127.0.0.1:8788;service=system-service-dashboard.service;state=ok
endpoint=mint-cloud-backup-dashboard;url=http://127.0.0.1:8765;service=mint-cloud-backup-dashboard.service;state=ok
endpoint=windowtabnotes;url=UNKNOWN;service=windowtabnotes.service;state=active

REMOTE_NODES:
node=oracle_vm
host=ubuntu@150.230.148.128
roles=uptime_kuma,oracle_backup,remote_monitoring
kuma_admin=ssh_tunnel http://127.0.0.1:3001 -> VM 127.0.0.1:3002
kuma_public_push=http://150.230.148.128:3001/api/push/<token>
kuma_container=uptime-kuma
kuma_db=/opt/uptime-kuma/data/kuma.db
ssh_key=/home/daniele/codex-workspace/projects/vm_oracle/ssh-key-2026-02-01.key
live_ssh_status=UNKNOWN_timeout_2026-06-08

SYNTHETIC_VIEW:
node=ThinkPad_P14s_Gen_5_AMD;role=current_primary_workstation;lan=UNKNOWN;tailscale=UNKNOWN
node=Surface;role=local_workstation;lan=192.168.1.97;tailscale=100.68.141.10
node=Oracle_VM;role=Kuma+backup;addr=150.230.148.128;kuma_admin=ssh_tunnel_to_127.0.0.1:3002;kuma_public=push_only_proxy_3001
node=Kuma;role=alert_history_visualization;remediation=no
node=Pixel_8a;role=ADB_Wi-Fi;addr=192.168.1.37;current=verify_live_before_use
node=TCL_6102H;role=ADB_Wi-Fi;addr=192.168.1.200;current=verify_live_before_use

ANDROID_NETWORK:
device=Pixel_8a;ip_current=UNKNOWN;ip_legacy_Surface=192.168.1.37;role=ADB_Wi-Fi;current=UNKNOWN_on_Windows
device=TCL_6102H;ip_current=UNKNOWN;ip_legacy_Surface=192.168.1.200;role=ADB_Wi-Fi;current=UNKNOWN_on_Windows
constraint=verify_with_adb_devices_l_not_mdns_only

LEGACY_MINT_KUMA_PUSH_PATHS:
path=local_Mint_service->HTTP_push->oracle_vm:3001/api/push via Nginx push-only proxy
monitor=cloud_backup;id=3;source=mint-cloud-backup-kuma-push.service
monitor=mint-home-backup;id=4;source=home-backup-kuma-push.service
monitor=amici_fb;id=5;source=amici_fb.service
monitor=disk-usage-monitor;id=6;source=disk-usage-monitor.service
monitor=parcel-tracker;id=7;source=parcel-tracker.service
monitor=mint-home-backup-retention;id=9;source=home-backup-retention-kuma-push.service
monitor=software_audit_mint;id=11;source=mint-update-tracker.service
monitor=Freeze_Gaps;id=13;source=mint-freeze-forensics.service
monitor=PSI_Memory;id=14;source=mint-freeze-forensics.service
monitor=PSI_IO;id=15;source=mint-freeze-forensics.service
monitor=Guardian_Alerts;id=16;source=mint-freeze-forensics.service
monitor=Forensics_Alive;id=17;source=mint-freeze-forensics.service

LEGACY_DISABLED_REMOTE_MONITORS:
monitor=mint_heartbeat;id=1;state=disabled_obsolete
monitor=rsync-transfer;id=2;state=disabled_obsolete
monitor=codex-token-watcher;id=10;state=disabled_obsolete

CONSTRAINTS:
constraint=Kuma_DOWN_is_signal_not_truth
constraint=local_state_files_authoritative_for_job_semantics
constraint=do_not_print_Kuma_push_URLs
constraint=do_not_assume_Oracle_reachable_without_live_ssh_or_http_check

OPEN:
open=current_Windows_hostname_LAN_IP_Tailscale_phone_IPs_UNKNOWN
open=Oracle_Kuma_monitor_table_not_live_verified_due_ssh_timeout
open=router_model_UNKNOWN
