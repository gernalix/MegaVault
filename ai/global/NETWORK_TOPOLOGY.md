# NETWORK_TOPOLOGY
VERSION=2
STATUS=ACTIVE
MODE=codex_first
FORMAT=ultracompressed
DOC_CLASS=topology
LIFECYCLE=ACTIVE
AUTHORITY_LEVEL=L2
SOURCE_OF_TRUTH=yes
SOURCE=HOST_PROFILE_2026-07-05+legacy_Kuma_docs
PROTOCOL=../MEGAVAULT_PROTOCOL.md
HOST_PROFILE=HOST_PROFILE.md
HUMAN=../../human/global/NETWORK_TOPOLOGY.md

LOCAL_HOST:
host=DANIELE_PC
machine=Lenovo_ThinkPad_P14s_Gen_5_AMD
os=Windows_11_Pro
lan_ip=UNKNOWN_not_scanned
tailscale=UNKNOWN_not_scanned
loopback=127.0.0.1
rule=do_not_use_old_Surface_IP_as_current_host_without_live_ipconfig

REMOTE_NODES:
node=oracle_vm
host=ubuntu@150.230.148.128
roles=uptime_kuma,oracle_backup,remote_monitoring
kuma_admin=ssh_tunnel http://127.0.0.1:3001 -> VM 127.0.0.1:3002
kuma_public_push=http://150.230.148.128:3001/api/push/<token>
kuma_db=/opt/uptime-kuma/data/kuma.db
ssh_key_windows=UNKNOWN
ssh_key_legacy_linux=/home/daniele/codex-workspace/projects/vm_oracle/ssh-key-2026-02-01.key

ANDROID_NETWORK:
adb=C:\Users\seste\AppData\Local\Android\Sdk\platform-tools\adb.exe
device=Pixel_8a;role=ADB_Wi-Fi/USB;addr=UNKNOWN_current;verify=adb devices -l
device=TCL_6102H;role=ADB_Wi-Fi/USB;addr=UNKNOWN_current;verify=adb devices -l
constraint=mDNS/IP_cache_not_proof

LEGACY_2026-06_SURFACE_MINT:
status=historical_not_primary
legacy_host=daniele-Surface-Pro;lan=192.168.1.97;tailscale=100.68.141.10
wifi=Alaska_5G
kuma_push_sources=cloud_backup,mint-home-backup,amici_fb,disk-usage-monitor,parcel-tracker,software_audit_mint,freeze_monitors
disabled_monitors=mint_heartbeat,rsync-transfer,codex-token-watcher
rule=Surface_IPs,Mint_services,/home_paths are legacy unless reverified

CONSTRAINTS:
constraint=do_not_print_Kuma_push_URL_tokens
constraint=Kuma_DOWN_is_signal_not_truth
constraint=do_not_assume_Oracle_reachable_without_live_ssh_or_http_check
constraint=network_facts_drift_fast_verify_before_use

OPEN:
open=current_LAN_IP_UNKNOWN
open=current_Tailscale_state_UNKNOWN
open=current_Oracle_SSH_key_Windows_path_UNKNOWN
