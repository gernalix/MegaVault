# NETWORK_TOPOLOGY
VERSION=4
STATUS=ACTIVE
MODE=codex_first
FORMAT=ultracompressed
SOURCE=HOST_PROFILE+ip_live_2026-07-10+adb_live_2026-07-10+activity_638214
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
adb_daemon=daniele_user_server+127.0.0.1:5037+LIBADBMDNS
adb_keeper=adb-device-keeper.service;enabled+active;docs=ADB_DEVICE_KEEPER.md
connected_devices=Pixel_8a+TCL_6102H
pixel=Google_Pixel_8a+Android_17+ADB_WiFi_2.0+dynamic_mDNS
tcl=TCL_6102H+Android_12+legacy_ADB_WiFi+verified_endpoint_cache_fallback
endpoint_snapshot_2026-07-10=Pixel_192.168.1.37:37355+TCL_192.168.1.200:32921;dynamic_not_authoritative
verify=adb_devices_-l
constraint=mDNS_or_cached_IP_is_not_device_proof

CONSTRAINTS:
constraint=network_facts_drift_fast;verify_before_use
constraint=do_not_expose_tokens+credentials+private_keys
constraint=remote_nodes_require_separate_live_verification
constraint=ADB_connect_candidates_require_allowlist_identity_verification

OPEN:
open=current_external_IP_UNKNOWN
open=Android_device_addresses_and_ports_drift+verify_live
