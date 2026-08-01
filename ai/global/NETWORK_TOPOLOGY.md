# NETWORK_TOPOLOGY
VERSION=9
STATUS=ACTIVE
MODE=codex_first
FORMAT=ultracompressed
SOURCE=HOST_PROFILE+ip_live_2026-07-10+adb_live_2026-07-10+activity_638214+activity_593184+activity_593804+activity_471853+activity_826417+activity_731904+activity_641827+activity_731842
PROTOCOL=../MEGAVAULT_PROTOCOL.md
HOST_PROFILE=HOST_PROFILE.md
HUMAN=../../human/global/NETWORK_TOPOLOGY.md

LOCAL_FEDORA:
host=fedora
machine=Lenovo_ThinkPad_P14s_Gen_5_AMD
os=Fedora_Linux_44_Workstation
loopback=127.0.0.1

MONITORING_EGRESS:
source=fedora-system-monitor;destination=150.230.148.128:3001;protocol=HTTP;purpose=Uptime_Kuma_push_only;categories=system+storage+network+services+software;credentials=root_only;payload=no_sensitive_data;firewall_change=none;delivery_verified=2026-07-14;admin_readback=remote_SQLite_ok
source=fedora-system-monitor-prometheus;destination=127.0.0.1:9109;protocol=HTTP;purpose=optional_local_metrics;default_state=disabled;external_exposure=none;verified=2026-07-13
source=prometheus;destination=127.0.0.1:9090;protocol=HTTP;purpose=local_UI+official_query_API+self_metrics;external_exposure=none;firewall_change=none;verified=2026-07-14;activity=826417
source=prometheus-node-exporter;destination=127.0.0.1:9100;protocol=HTTP;purpose=local_Fedora_host_metrics;external_exposure=none;firewall_change=none;verified=2026-07-14;activity=826417
relation=Prometheus_scrapes_127.0.0.1:9090+9100+9109;Uptime_Kuma_egress_independent+unchanged;SSH_tunnel_future_compatible_not_configured
risk=HTTP_does_not_protect_push_endpoint_or_status_from_on_path_observers;HTTPS_migration_recommended
wifi_interface=wlp2s0
wifi_state=UP
wifi_power_policy=NetworkManager_global_wifi.powersave_2+iw_power_save_off;driver=ath11k_pci;PCI_runtime_control=on;verified=2026-07-23;activity=641827
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

ORACLE_VM_SSH:
host=150.230.148.128;alias=oracle-vm;user=ubuntu;remote_hostname=instance-20260201-1126;remote_os=Ubuntu_22.04.5_oracle_kernel_6.8.0-1058-oracle;ssh_env=/home/daniele/.config/codex/secrets/oracle.env;ssh_key_path=/home/daniele/.config/codex/secrets/oracle_vm_rsa;ssh_command=load_oracle.env+fail_closed_then_ssh_-i_$ORACLE_KEY_FILE_-p_$ORACLE_PORT_-o_BatchMode=yes_-o_IdentitiesOnly=yes_$ORACLE_USER@$ORACLE_HOST;public_key_fingerprint=SHA256:cmihWRlHSLgX1YGGRx7zukWWql3Am4rCqCx/Hp27uXU;host_key=ED25519_SHA256:jeMdcW+n3CdSv33xHSLgLx8tO4L4Pk3h6ziTgre0wUE;verified=2026-08-01;activity=593804+731904+731842+816429
rule=private_key_never_in_docs_prompts_logs_git;secret_material_stored_only_under_/home/daniele/.config/codex/secrets

ORACLE_VM_SSH:
host=150.230.148.128;alias=oracle-vm;user=ubuntu;remote_hostname=instance-20260201-1126;remote_os=Ubuntu_22.04_oracle_kernel_6.8.0-1054-oracle;ssh_env=/home/daniele/.config/codex/secrets/oracle.env;ssh_key_path=/home/daniele/.config/codex/secrets/oracle_vm_rsa;ssh_command=load_oracle.env+fail_closed_then_ssh_-i_$ORACLE_KEY_FILE_-p_$ORACLE_PORT_-o_BatchMode=yes_-o_IdentitiesOnly=yes_$ORACLE_USER@$ORACLE_HOST;public_key_fingerprint=SHA256:cmihWRlHSLgX1YGGRx7zukWWql3Am4rCqCx/Hp27uXU;host_key=ED25519_SHA256:jeMdcW+n3CdSv33xHSLgLx8tO4L4Pk3h6ziTgre0wUE;verified=2026-08-01;activity=593804+731904+816429
rule=private_key_never_in_docs_prompts_logs_git;secret_material_stored_only_under_/home/daniele/.config/codex/secrets

OPEN:
open=current_external_IP_UNKNOWN
open=Android_device_addresses_and_ports_drift+verify_live
