# NETWORK_TOPOLOGY
VERSION=3
STATUS=ACTIVE
MODE=codex_first
FORMAT=ultracompressed
SOURCE=HOST_PROFILE+ip_live_2026-07-09+adb_live_2026-07-09
PROTOCOL=../MEGAVAULT_PROTOCOL.md
HOST_PROFILE=HOST_PROFILE.md
HUMAN=../../human/global/NETWORK_TOPOLOGY.md

LOCAL_FEDORA:
host=fedora
machine=Lenovo_ThinkPad_P14s_Gen_5_AMD
os=Fedora_Linux_44_Workstation
loopback=127.0.0.1
wifi_interface=wlp2s0
wifi_state=UP
lan_ipv4=192.168.1.231/24
default_gateway=192.168.1.1
ethernet_interface=enp1s0f0
ethernet_state=DOWN
tailscale=not_installed_or_not_in_PATH

ANDROID_NETWORK:
adb=/home/daniele/Android/Sdk/platform-tools/adb
adb_daemon=started_2026-07-09
connected_devices=none
verify=adb_devices_-l
constraint=mDNS_or_cached_IP_is_not_device_proof

CONSTRAINTS:
constraint=network_facts_drift_fast;verify_before_use
constraint=do_not_expose_tokens+credentials+private_keys
constraint=remote_nodes_require_separate_live_verification

OPEN:
open=current_external_IP_UNKNOWN
open=Android_device_addresses_UNKNOWN_until_connected
