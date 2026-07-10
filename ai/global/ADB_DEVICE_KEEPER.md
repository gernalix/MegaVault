# ADB_DEVICE_KEEPER
VERSION=1
STATUS=ACTIVE_VERIFIED
MODE=codex_first
FORMAT=ultracompressed
UPDATED=2026-07-10T06:34:00+02:00
SUMMARY=Servizio_systemd_utente_24x7_per_Pixel_8a_e_TCL_6102H_via_ADB_WiFi_allowlist
CATEGORY=automation
IMPORTANCE=P1
SOURCE_REF=activity_638214+Fedora_live_validation_2026-07-10
PROTOCOL=../MEGAVAULT_PROTOCOL.md
HOST_PROFILE=HOST_PROFILE.md
ANDROID_PROTOCOL=../ANDROID_PROTOCOL.md
SERVICE_REGISTRY=SERVICE_REGISTRY.md
NETWORK_TOPOLOGY=NETWORK_TOPOLOGY.md
HUMAN=../../human/global/ADB_DEVICE_KEEPER.md

META:
activity_id=638214
host=fedora
user=daniele
scope=user_service+local_LAN+ADB_WiFi
root_required=only_loginctl_enable_linger_via_logind_authorization
android_studio_dependency=none

DIAGNOSIS_INITIAL:
adb=/home/daniele/Android/Sdk/platform-tools/adb
adb_version=1.0.41/37.0.0-14910828
adb_server=daniele_owned+127.0.0.1:5037+shared_by_cli_and_Android_Studio
adb_server_backend=LIBADBMDNS
adb_server_mdns_enabled=true
adb_keys=/home/daniele/.android/adbkey+adbkey.pub;content_not_read_or_copied
adb_pairing_data=/home/daniele/.android/adb_known_hosts.pb;content_not_read_or_copied
android_studio_initial=Flatpak_running
devices_initial=Pixel_8a+TCL_6102H
pixel_mdns=advertised_consistently
tcl_mdns=not_advertised_during_samples_although_transport_connected
firewall=firewalld_active+FedoraWorkstation_zone+LAN_dynamic_TCP_UDP_allowed
mdns_runtime=avahi_active+ADB_UDP_5353_listener
environment=ANDROID_HOME+ANDROID_SDK_ROOT=/home/daniele/Android/Sdk
path=platform-tools_present

IDENTITY_ALLOWLIST:
device=Pixel_8a;manufacturer=Google;model=Pixel_8a;product_device=akita;serial=52131JEKB01070;mdns_prefix=adb-52131JEKB01070-
device=TCL_6102H;manufacturer=TCL;model=6102H;product_device=Cruze_Lite_S;serial=QCGADUVOSSEYFES4;mdns_prefix=adb-QCGADUVOSSEYFES4-
identifier_class=non_secret_but_config_and_state_mode_0600

ARCH:
choice=option_A_persistent_service_controlled_loop
reason=one_systemd_start+quiet_journal+immediate_state_memory+same_cost_as_periodic_oneshot_without_timer_churn
healthy_interval=60s
absent_interval=25s
endpoint_retry_backoff=25s_exponential_to_300s
concurrency=flock_per_cycle+manual_cycle_serialized
server_policy=start_server_without_kill_loop
native_autoconnect=ADB_MDNS_AUTO_CONNECT=0_when_keeper_starts_server
native_autoconnect_reason=ADB_default_filters_to_paired_devices_but_cannot_express_the_two_device_application_allowlist
discovery=only__adb-tls-connect._tcp+private_or_link_local_endpoint
connect_filter=exact_allowlisted_mdns_instance_prefix_or_previously_verified_endpoint_cache
post_connect_validation=manufacturer+model+product_device+serial
unknown_policy=ignore_unknown_mDNS;disconnect_candidate_immediately_on_identity_mismatch;never_pair
endpoint_policy=mDNS_primary+verified_last_endpoint_cache_fallback
logging=journal_transitions_only+deduplicated_significant_errors
android_studio_coexistence=shared_standard_ADB_server_on_5037

FILES:
script=/home/daniele/.local/bin/adb-device-keeper;mode=0700
config=/home/daniele/.config/adb-device-keeper/config;mode=0600
state=/home/daniele/.local/state/adb-device-keeper;mode=0700
unit=/home/daniele/.config/systemd/user/adb-device-keeper.service;mode=0600
enablement_symlink=/home/daniele/.config/systemd/user/default.target.wants/adb-device-keeper.service
timer=none
backup_initial=/home/daniele/.local/state/adb-device-keeper/backups/20260710T062520+0200
backup_script=/home/daniele/.local/state/adb-device-keeper/backups/20260710T063022+0200
backup_endpoint_test=/home/daniele/.local/state/adb-device-keeper/backups/20260710T063146+0200

SYSTEMD:
unit=adb-device-keeper.service
scope=user
enabled=yes
active=yes
restart=on-failure+30s
start_limit=3_per_600s
network_order=network-online.target
linger=yes
hardening=NoNewPrivileges+ProtectSystem+ProtectKernelTunables+ProtectKernelModules+ProtectControlGroups+ProtectClock+RestrictSUIDSGID+RestrictRealtime+LockPersonality+empty_capabilities
compatibility=home_and_devices_not_sandboxed_to_preserve_manual_ADB_USB_and_file_workflows

TEST:
test=syntax;result=PASS;detail=bash_-n
test=systemd_unit;result=PASS;detail=systemd-analyze_--user_verify
test=manual_cycle;result=PASS;detail=both_devices_verified+flock_with_daemon_active
test=Android_Studio_closed;result=PASS;detail=both_devices_visible+service_active
test=server_restart;result=PASS;detail=old_PID_28470_stopped+service_owned_PID_started+both_reconnected
test=server_policy;result=PASS;detail=LIBADBMDNS+mdns_enabled+ADB_MDNS_AUTO_CONNECT_0_in_server_environment
test=Pixel_absent;result=PASS;detail=host_transport_disconnected+TCL_remained+Pixel_reconnected_next_cycle
test=TCL_absent;result=PASS;detail=host_transport_disconnected+Pixel_remained+TCL_reconnected_next_cycle
test=endpoint_change;result=PASS_SIMULATED;detail=stale_Pixel_state_40000_replaced_by_mDNS_37355+configuration_unchanged
test=both_absent;result=PASS;detail=15s_active+ADB_list_empty+0.687ms_CPU+0_application_logs+both_reconnected_next_cycle
test=return_to_LAN;result=PASS;detail=real_host_transport_loss_and_reconnect_for_each_device
test=logout_new_session;result=PASS_STRUCTURAL;detail=Linger_yes+unit_enabled_in_default_target
test=Fedora_reboot;result=NOT_EXECUTED;detail=avoided_current_work_interruption+post_boot_check_documented
test=Android_Studio_coexistence;result=PASS;detail=same_ADB_PID_504069+both_devices_visible+Studio_closed_after_test
test=log_noise;result=PASS;detail=transition_only_logs+healthy_sleep
test=rollback;result=PASS_VERIFIED;detail=paths+enablement+linger_reversal_commands_checked_not_executed_to_preserve_final_state
test=shellcheck;result=NOT_RUN;detail=optional_tool_not_installed+bash_n_passed

OPERATIONS:
status=systemctl --user status adb-device-keeper.service
start=systemctl --user start adb-device-keeper.service
stop=systemctl --user stop adb-device-keeper.service
restart=systemctl --user restart adb-device-keeper.service
enable=systemctl --user enable --now adb-device-keeper.service
disable=systemctl --user disable --now adb-device-keeper.service
logs_recent=journalctl --user -u adb-device-keeper.service -n 100 --no-pager
logs_live=journalctl --user -u adb-device-keeper.service -f
devices=/home/daniele/Android/Sdk/platform-tools/adb devices -l
mdns=/home/daniele/Android/Sdk/platform-tools/adb mdns services
manual_reconnect=/home/daniele/.local/bin/adb-device-keeper --once
linger_status=loginctl show-user daniele -p Linger -p State

POST_BOOT_VERIFY:
command=systemctl --user is-enabled adb-device-keeper.service
command=systemctl --user is-active adb-device-keeper.service
command=loginctl show-user daniele -p Linger
command=/home/daniele/Android/Sdk/platform-tools/adb devices -l
command=journalctl --user -b -u adb-device-keeper.service --no-pager
expected=enabled+active+Linger_yes+reachable_allowlisted_devices_only

ROLLBACK:
step=systemctl --user disable --now adb-device-keeper.service
step=rm -f /home/daniele/.config/systemd/user/adb-device-keeper.service
step=rm -f /home/daniele/.config/systemd/user/default.target.wants/adb-device-keeper.service
step=rm -f /home/daniele/.local/bin/adb-device-keeper
step=rm -rf /home/daniele/.config/adb-device-keeper /home/daniele/.local/state/adb-device-keeper
step=systemctl --user daemon-reload
step=systemctl --user reset-failed adb-device-keeper.service
step=loginctl disable-linger daniele_only_if_no_other_user_service_requires_linger
step=git_-C_/home/daniele/MegaVault_revert_the_activity_638214_commit_for_documentation_rollback
preserve=/home/daniele/.android+ADB_keys+pairing_data+phone_authorizations
adb_server_after_rollback=leave_running_for_manual_tools;do_not_kill_unnecessarily

LIMITS:
limit=wireless_debugging_off+phone_off+suspended+different_LAN_prevents_connection_until_device_returns
limit=TCL_Android_12_did_not_publish_mDNS_in_observed_samples;verified_endpoint_cache_recovers_only_while_IP_and_port_remain_current
limit=if_TCL_IP_or_port_changes_without_mDNS_publication_host_cannot_discover_it;toggle_Wireless_debugging_on_phone_then_run_manual_cycle
limit=Pixel_Android_17_ADB_WiFi_2.0_supports_native_trusted_network_return_but_keeper_enforces_narrower_host_allowlist
limit=ADB_server_environment_policy_applies_when_keeper_starts_server;an_already_running_external_server_keeps_its_original_environment_until_controlled_restart
manual_phone_action=none_now
manual_phone_action_if_pairing_revoked=pair_manually_only_after_explicit_user_decision;service_never_pairs
manual_phone_action_if_TCL_stale=confirm_same_LAN+Wireless_debugging_enabled+toggle_it_if_service_not_advertised

LINKS:
link=https://developer.android.com/tools/adb
link=https://developer.android.com/tools/releases/platform-tools
link=https://android.googlesource.com/platform/packages/modules/adb/+/HEAD/docs/dev/adb_wifi.md

OPEN:
open=real_Fedora_reboot_validation_pending_safe_maintenance_window
open=real_phone_generated_IP_or_port_change_not_forced;stale_cache_detection_validated
