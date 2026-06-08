# ALERT_REGISTRY
VERSION=1
STATUS=ACTIVE
MODE=codex_first
FORMAT=ultracompressed
SOURCE=HOST_PROFILE+project_ai_docs+local_scripts_grep_2026-06-08
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
url=http://150.230.148.128:3001
notification=Telegram id=1 documented
db=/opt/uptime-kuma/data/kuma.db
live_db_query=UNKNOWN_ssh_timeout_2026-06-08

KUMA_MONITORS_ACTIVE:
alert=cloud_backup;monitor_id=3;owner=mint-cloud-backup;source=mint-cloud-backup-kuma-push.service
alert=mint-home-backup;monitor_id=4;owner=backup_docs;source=home-backup-kuma-push.service
alert=amici_fb;monitor_id=5;owner=amici-fb;source=amici_fb.service
alert=disk-usage-monitor;monitor_id=6;owner=UNKNOWN;source=disk-usage-monitor.service
alert=parcel-tracker;monitor_id=7;owner=parcel-tracker;source=parcel-tracker.service
alert=mint-home-backup-retention;monitor_id=9;owner=backup_docs;source=home-backup-retention-kuma-push.service
alert=software_audit_mint;monitor_id=11;owner=mint-update-tracker;source=mint-update-tracker.service
alert=Freeze_Gaps;monitor_id=13;owner=mint-freeze-forensics;source=KUMA_PUSH_FREEZE_GAPS
alert=PSI_Memory;monitor_id=14;owner=mint-freeze-forensics;source=KUMA_PUSH_PSI_MEMORY
alert=PSI_IO;monitor_id=15;owner=mint-freeze-forensics;source=KUMA_PUSH_PSI_IO
alert=Guardian_Alerts;monitor_id=16;owner=mint-freeze-forensics;source=KUMA_PUSH_GUARDIAN_ALERTS
alert=Forensics_Alive;monitor_id=17;owner=mint-freeze-forensics;source=KUMA_PUSH_FORENSICS_ALIVE

KUMA_MONITORS_DISABLED:
alert=mint_heartbeat;monitor_id=1;state=disabled_obsolete
alert=rsync-transfer;monitor_id=2;owner=surface-recovery-hardening;state=disabled_obsolete_no_live_runner
alert=codex-token-watcher;monitor_id=10;owner=codex-token-watcher;state=disabled_obsolete

TELEGRAM_SOURCES:
alert=amici_fb;owner=amici-fb;helper=telegram_notify.py;env=TELEGRAM_BOT_TOKEN+TELEGRAM_CHAT_ID;events=snapshot,diff,error
alert=parcel_tracker_update;owner=parcel-tracker;helper=amici_fb/telegram_notify.py;events=shipment_update,test
alert=codex_usage_weekly_change;owner=codex-token-watcher;helper=amici_fb/telegram_notify.py;events=weekly_change,error,recovery,quota_drop;runtime_status=legacy_Mint_local
alert=transfer_usb_io_watchdog;owner=surface-recovery-hardening;helper=amici_fb/telegram_notify.py;env=/home/daniele/.config/environment.d/telegram.conf;events=critical_storage_event
alert=memory_pressure_guardian;owner=surface-recovery-hardening;helper=amici_fb/telegram_notify.py;events=memory_pressure;status=legacy_script
alert=mint-freeze-forensics_guardian;owner=mint-freeze-forensics;transport=Kuma;events=guardian_alert_count
alert=disk_usage_delta;owner=UNKNOWN;transport=Telegram+Kuma documented in /home/daniele/disk_usage_monitor;events=free_space_delta

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
open=Kuma_notification_bindings_not_live_verified_due_ssh_timeout
open=disk_usage_monitor_repo_owner_UNKNOWN
