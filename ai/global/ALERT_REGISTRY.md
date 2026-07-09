# ALERT_REGISTRY
VERSION=2
STATUS=ACTIVE
MODE=codex_first
FORMAT=ultracompressed
SOURCE=Fedora_systemd_live_2026-07-09+HOST_PROFILE
PROTOCOL=../MEGAVAULT_PROTOCOL.md
HOST_PROFILE=HOST_PROFILE.md
HUMAN=../../human/global/ALERT_REGISTRY.md

CURRENT_FEDORA:
host=fedora
project_alert_services_verified=none
project_alert_timers_verified=none
Kuma_push_sources_verified=none
Telegram_sources_verified=none
alert_migration=not_revalidated

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
open=project_alerting_and_remote_monitoring_not_revalidated_from_Fedora
