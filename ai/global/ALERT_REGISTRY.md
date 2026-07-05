# ALERT_REGISTRY
VERSION=1
STATUS=ACTIVE
MODE=codex_first
FORMAT=ultracompressed
SOURCE=HOST_PROFILE+project_ai_docs+local_scripts_grep_2026-06-08+kuma_sqlite_readonly_2026-06-10+prompt_458217_kuma_hardening
PROTOCOL=../MEGAVAULT_PROTOCOL.md
HOST_PROFILE=HOST_PROFILE.md
HUMAN=../../human/global/ALERT_REGISTRY.md

RULES:
rule=never_print_tokens
rule=never_commit_Kuma_push_URLs
rule=Telegram_helper_shared=/home/daniele/codex-workspace/scripts/amici_fb/telegram_notify.py
rule=Kuma_is_alerting_history_visualization_not_remediation
unknown=live_delivery_status_for_each_Telegram_source

KUMA:
kuma=Oracle_VM_Uptime_Kuma
admin_url=http://127.0.0.1:3001 after SSH tunnel -L 3001:127.0.0.1:3002
public_push_proxy=http://150.230.148.128:3001/api/push/<token>;dashboard_root_public_403
notification=Telegram id=1 documented
db=/opt/uptime-kuma/data/kuma.db
live_db_query=verified_2026-06-12;integrity=ok;db=/opt/uptime-kuma/data/kuma.db;container=uptime-kuma running;app_http_ok;docker_image_healthcheck_disabled_due_preexisting_runc_exec_failure
notification_mapping=monitor_ids 1,2,3,4,5,6,7,9,10,11,13,14,15,16,17 -> Telegram id=1;group id=12 no direct notification

KUMA_MONITORS_ACTIVE:
alert=cloud_backup;monitor_id=3;owner=mint-cloud-backup;owner_project=mint-cloud-backup;source=mint-cloud-backup-kuma-push.service;source_service=mint-cloud-backup-kuma-push.service;severity=critical;actionability=codex_investigate;false_positive_risk=medium
alert=mint-home-backup;monitor_id=4;owner=backup_docs;owner_project=backup_docs;source=home-backup-kuma-push.service;source_service=home-backup-kuma-push.service;severity=critical;actionability=codex_investigate;false_positive_risk=medium
alert=amici_fb;monitor_id=5;owner=amici-fb;owner_project=amici-fb;source=amici_fb.service;source_service=amici_fb.service;severity=warning;actionability=codex_investigate;false_positive_risk=medium
alert=disk-usage-monitor;monitor_id=6;owner=disk-usage-monitor;owner_project=disk-usage-monitor;source=disk-usage-monitor.service;source_service=disk-usage-monitor.service;heartbeat_msg=OK_T7_free_SG4_free_SG6_free;severity=warning;actionability=codex_investigate;false_positive_risk=medium
alert=parcel-tracker;monitor_id=7;owner=parcel-tracker;owner_project=parcel-tracker;source=parcel-tracker.service;source_service=parcel-tracker.service;severity=info;actionability=human_action;false_positive_risk=medium
alert=mint-home-backup-retention;monitor_id=9;owner=backup_docs;owner_project=backup_docs;source=home-backup-retention-kuma-push.service;source_service=home-backup-retention-kuma-push.service;severity=warning;actionability=codex_investigate;false_positive_risk=medium
alert=software_audit_mint;monitor_id=11;owner=mint-update-tracker;owner_project=mint-update-tracker;source=mint-update-tracker.service;source_service=mint-update-tracker.service;severity=warning;actionability=codex_investigate;false_positive_risk=low
alert=Freeze_Gaps;monitor_id=13;owner=mint-freeze-forensics;owner_project=mint-freeze-forensics;source=KUMA_PUSH_FREEZE_GAPS;source_service=mint-freeze-forensics.service;severity=critical;actionability=codex_investigate;false_positive_risk=medium
alert=PSI_Memory;monitor_id=14;owner=mint-freeze-forensics;owner_project=mint-freeze-forensics;source=KUMA_PUSH_PSI_MEMORY;source_service=mint-freeze-forensics.service;severity=warning;actionability=codex_investigate;false_positive_risk=medium
alert=PSI_IO;monitor_id=15;owner=mint-freeze-forensics;owner_project=mint-freeze-forensics;source=KUMA_PUSH_PSI_IO;source_service=mint-freeze-forensics.service;severity=warning;actionability=codex_investigate;false_positive_risk=medium
alert=Guardian_Alerts;monitor_id=16;owner=mint-freeze-forensics;owner_project=mint-freeze-forensics;source=KUMA_PUSH_GUARDIAN_ALERTS;source_service=mint-resource-guardian.service;severity=warning;actionability=human_action;false_positive_risk=medium
alert=Forensics_Alive;monitor_id=17;owner=mint-freeze-forensics;owner_project=mint-freeze-forensics;source=KUMA_PUSH_FORENSICS_ALIVE;source_service=mint-freeze-forensics.service;severity=warning;actionability=codex_investigate;false_positive_risk=low

KUMA_GROUPS:
group=Mint Freeze Analysis;monitor_id=12;status_page_id=1;status_page_slug=mint-freeze-analysis;children=13,14,15,16,17;owner_project=mint-freeze-forensics;notification=none_direct;latest_2026-06-10=down_due_child

KUMA_MONITORS_DISABLED:
alert=mint_heartbeat;monitor_id=1;owner_project=UNKNOWN;source_service=UNKNOWN;state=disabled_obsolete;severity=info;actionability=informational;false_positive_risk=high
alert=rsync-transfer;monitor_id=2;owner=surface-recovery-hardening;owner_project=surface-recovery-hardening;source_service=rsync-uptime-kuma-push.service;state=disabled_obsolete_no_live_runner;severity=info;actionability=informational;false_positive_risk=high
alert=codex-token-watcher;monitor_id=10;owner=codex-token-watcher;owner_project=codex-token-watcher;source_service=codex-usage-monitor.service;state=disabled_obsolete;severity=info;actionability=informational;false_positive_risk=high

TELEGRAM_SOURCES:
alert=amici_fb;owner=amici-fb;owner_project=amici-fb;source_service=amici_fb.service;helper=telegram_notify.py;env=TELEGRAM_BOT_TOKEN+TELEGRAM_CHAT_ID;events=snapshot,diff,error;severity=warning;actionability=human_action;false_positive_risk=medium
alert=parcel_tracker_update;owner=parcel-tracker;owner_project=parcel-tracker;source_service=parcel-tracker.service;helper=amici_fb/telegram_notify.py;events=shipment_update,test;severity=info;actionability=human_action;false_positive_risk=medium
alert=codex_usage_weekly_change;owner=codex-token-watcher;owner_project=codex-token-watcher;source_service=codex-usage-monitor.service;helper=amici_fb/telegram_notify.py;events=weekly_change,error,recovery,quota_drop;runtime_status=legacy_Mint_local;severity=info;actionability=codex_investigate;false_positive_risk=high
alert=transfer_usb_io_watchdog;owner=surface-recovery-hardening;owner_project=surface-recovery-hardening;source_service=transfer-usb-io-watchdog.service;helper=amici_fb/telegram_notify.py;env=/home/daniele/.config/environment.d/telegram.conf;events=critical_storage_event;severity=critical;actionability=human_action;false_positive_risk=low
alert=memory_pressure_guardian;owner=surface-recovery-hardening;owner_project=surface-recovery-hardening;source_service=legacy_script;helper=amici_fb/telegram_notify.py;events=memory_pressure;status=legacy_script;severity=warning;actionability=human_action;false_positive_risk=medium
alert=mint-freeze-forensics_guardian;owner=mint-freeze-forensics;owner_project=mint-freeze-forensics;source_service=mint-resource-guardian.service;transport=Kuma;events=guardian_alert_count;severity=warning;actionability=human_action;false_positive_risk=medium
alert=disk_usage_canonical;owner=disk-usage-monitor;owner_project=disk-usage-monitor;source_service=disk-usage-monitor.service;source_timer=disk-usage-monitor.timer;transport=Telegram+Kuma documented in /home/daniele/disk_usage_monitor;events=connection_change_or_low_space_with_cooldown,delta_used_change_ge_1GiB;scope=T7_sistema,Seagate_4TB,Seagate_6TB_only;severity=warning;actionability=codex_investigate;false_positive_risk=medium;healthy_service_idle=inactive_dead_if_last_success_and_timer_waiting;delta_state=delta_notification_state
alert=disk_usage_ok_digest;owner=disk-usage-monitor;owner_project=disk-usage-monitor;source_service=disk-usage-monitor.service;transport=Telegram_local;events=daily_clean_3_disk_ok_digest;severity=info;actionability=informational;false_positive_risk=low

PROJECT_RELATIONS:
project=mint-freeze-forensics;alerts=Freeze_Gaps,PSI_Memory,PSI_IO,Guardian_Alerts,Forensics_Alive
project=mint-cloud-backup;alerts=cloud_backup
project=backup_docs;alerts=mint-home-backup,mint-home-backup-retention
project=amici-fb;alerts=amici_fb,Telegram_snapshot
project=parcel-tracker;alerts=parcel-tracker,Telegram_update
project=mint-update-tracker;alerts=software_audit_mint
project=surface-recovery-hardening;alerts=rsync-transfer_disabled,transfer_usb_io_watchdog_Telegram
project=codex-token-watcher;alerts=codex-token-watcher_disabled,Telegram_optional

OPEN:
open=Telegram_delivery_not_tested_2026-06-10_docs_only
