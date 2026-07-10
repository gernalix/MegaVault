# ALERT_REGISTRY
VERSION=4
STATUS=ACTIVE
MODE=codex_first
FORMAT=ultracompressed
SOURCE=Fedora_systemd_live_2026-07-09+HOST_PROFILE+activity_593184
PROTOCOL=../MEGAVAULT_PROTOCOL.md
HOST_PROFILE=HOST_PROFILE.md
HUMAN=../../human/global/ALERT_REGISTRY.md

CURRENT_FEDORA:
host=fedora
project_alert_services_verified=fedora-system-monitor-events+collectors
project_alert_timers_verified=fedora-system-monitor-fast+hourly+daily+weekly
Kuma_push_sources_verified=fedora-system-monitor
Telegram_sources_verified=none
alert_migration=not_revalidated

FEDORA_SYSTEM_MONITOR_KUMA:
source=fedora-system-monitor;credentials=/etc/fedora-system-monitor/uptime-kuma.toml;mode=root:root_0600;transport=HTTP_existing_infrastructure;runtime_cookie_dependency=none
monitor=Fedora_Host;id=39;heartbeat=180s;mapping=CPU+memory+swap+temperature+kernel+OOM
monitor=Fedora_Storage;id=40;heartbeat=480s;mapping=filesystem+SMART+IO+mount+devices
monitor=Fedora_Network;id=41;heartbeat=180s;mapping=Internet+gateway+WiFi+VPN+NetworkManager
monitor=Fedora_Services;id=42;heartbeat=180s;mapping=failed_units+restart+restart_loop
monitor=Fedora_Software;id=43;heartbeat=5400s;mapping=updates+transactions+inventory
delivery_audit_1.0.1=atomic_alert_transition+endpoint_flock+post_delivery_reconciliation;slow_DOWN_recovery_order=DOWN_then_UP_PASS;real_current_health_heartbeat=delivered;false_transition_final_gate=none
anti_spam=persistent_dedup+duration_gate+hysteresis+cooldown+aggregation+single_recovery
verification=all_five_real_UP_delivered+Software_controlled_DOWN_HTTP_200+recovery_UP_HTTP_200
security=push_URLs_not_in_repo_or_logs;HTTP_transport_risk_documented

SYSTEM_SIGNALING_CURRENT:
service=abrtd.service;state=active/running;scope=local_crash_reporting
service=abrt-journal-core.service;state=active/running;scope=coredump_events
service=abrt-oops.service;state=active/running;scope=kernel_oops
service=smartd.service;state=active/running;scope=storage_health
service=systemd-oomd.service;state=active/running;scope=memory_pressure

RULES:
rule=never_print_or_commit_tokens+chat_ids+push_URLs
rule=alerts_are_signals_not_remediation_authority
rule=verify_sender+timer+delivery+destination_before_marking_active
rule=do_not_assume_pre_migration_alert_sources_exist

OPEN:
open=other_project_alerting_and_remote_monitoring_not_revalidated_from_Fedora
open=migrate_existing_Kuma_endpoint_to_HTTPS
