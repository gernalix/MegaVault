META:
name=Oracle Uptime Kuma
slug=oracle-uptime-kuma
path=/opt/uptime-kuma on ubuntu@150.230.148.128
repo=runtime
branch=runtime
prompt=847261,428691,731845
created=2026-06-07
updated=2026-06-10 prompt_731845
protocol=MEGAVAULT_PROTOCOL.md:v8
verify_source=ssh_readonly_2026-06-10T14:03+02

PURPOSE:
purpose=Uptime Kuma instance on Oracle VM for Mint/Oracle black-box history, alerting, and visualization.
mode=black_box_history_alerting_visualization
not=remediation_engine;not=source_of_truth_for_job_semantics
truth_rule=Kuma DOWN is signal; service-local state/logs/DB decide real failure.

STACK:
ssh=ssh -i /home/daniele/codex-workspace/projects/vm_oracle/ssh-key-2026-02-01.key ubuntu@150.230.148.128
host=ubuntu@150.230.148.128
hostname=instance-20260201-1126
url=http://150.230.148.128:3001
docker_systemd=docker.service active/running since 2026-06-01T12:42:10Z
compose_bin=/usr/bin/docker compose version v5.1.4
compose_file=/opt/uptime-kuma/docker-compose.yml
compose_service=uptime-kuma
container=uptime-kuma
container_id_prefix=15c942e18d85
image=louislam/uptime-kuma:2.3.2
restart_policy=unless-stopped
container_state=running;healthy;started=2026-06-07T05:30:34Z
port=0.0.0.0:3001->[container]:3001;[::]:3001->[container]:3001
systemd_unit_absent=uptime-kuma.service not present; manage with docker compose/container, not systemctl uptime-kuma.
server_timezone_setting=Africa/Bangui

MAP:
entry=/opt/uptime-kuma/docker-compose.yml
config_dir=/opt/uptime-kuma
data_dir=/opt/uptime-kuma/data
db=/opt/uptime-kuma/data/kuma.db
db_wal=/opt/uptime-kuma/data/kuma.db-wal
db_shm=/opt/uptime-kuma/data/kuma.db-shm
backup_dir=/opt/uptime-kuma/backups
app_error_log=/opt/uptime-kuma/data/error.log
docker_json_log=/var/lib/docker/containers/15c942e18d85828376f88ed186df1ca3922f9f7a8cb78d8468129e7c066005d9/15c942e18d85828376f88ed186df1ca3922f9f7a8cb78d8468129e7c066005d9-json.log
runtime_logs=docker logs uptime-kuma;app_error_log
scripts=none inside MegaVault; local pushers live in monitored project repos/scripts.
avoid=printing push tokens,printing Telegram token/chat id,browser-only invisible edits,automatic remediation

RUNTIME_INVENTORY:
compose_yaml=service uptime-kuma;image louislam/uptime-kuma:2.3.2;container_name uptime-kuma;port 3001:3001;volume /opt/uptime-kuma/data:/app/data;restart unless-stopped;logging json-file max-size=10m max-file=3
db_integrity_2026-06-10=ok
db_size_2026-06-10=8806400
wal_size_2026-06-10=5677392
shm_size_2026-06-10=32768
backup_files=uptime-kuma-data-20260508T113626Z.tar.gz,uptime-kuma-data-20260510T232040Z.tar.gz,uptime-kuma-data-20260510T233041Z.tar.gz,kuma-pre-482917-20260606T181225Z.db,kuma-pre-847261-freeze-analysis.db
disk_2026-06-10=/dev/sda1 45G used=42G avail=3.2G use=93%;treat_as_capacity_risk_before_large_backup_or_log_growth
recent_error_log=SQLITE_CONSTRAINT duplicate stat_minutely/stat_daily rows for monitor_ids 6,16,17 observed 2026-06-10;do_not_fix_without_separate_runtime_task
container_env_safe=UPTIME_KUMA_IS_CONTAINER=1;UPTIME_KUMA_ENABLE_EMBEDDED_MARIADB=1;NODE_VERSION=22.22.2;no tokens observed in safe env listing

MONITOR_INVENTORY:
status_codes=0_down,1_up,2_pending
table_source=sqlite_readonly_2026-06-10 select id,name,type,active,parent,interval,timeout,retry_interval,maxretries,upside_down from monitor
monitor=1;name=mint heartbeat;type=push;active=0;class=obsolete_disabled;interval=60;timeout=48;retry=60;maxretries=4;tags=482917-reviewed,push-monitor,obsolete-disabled;notification=1;replacement=service_specific_pushers+Forensics_Alive;latest=down 2026-06-06T18:15:20
monitor=2;name=rsync-transfer;type=push;active=0;class=obsolete_disabled_no_live_runner;interval=178;timeout=48;retry=178;maxretries=0;tags=482917-reviewed,push-monitor,obsolete-disabled;notification=1;replacement=none_until_verified_transfer;source=rsync-uptime-kuma-push.service disabled_obsolete;latest=down 2026-06-06T18:15:32
monitor=3;name=cloud backup;type=push;active=1;class=canonical;owner_project=mint-cloud-backup;source_service=mint-cloud-backup-kuma-push.service;env=/etc/mint-cloud-backup/uptime-kuma.env;interval=180;timeout=60;retry=120;maxretries=2;tags=482917-reviewed,push-monitor;notification=1;latest=up 2026-06-10T12:00:05
monitor=4;name=mint-home-backup;type=push;active=1;class=canonical;owner_project=backup_docs;source_service=home-backup-kuma-push.service;script=/home/daniele/home_backup_kuma_push.sh;env=/home/daniele/.config/home-backup/kuma.env;interval=900;timeout=60;retry=900;maxretries=1;tags=482917-reviewed,push-monitor;notification=1;latest=up 2026-06-10T12:00:09
monitor=5;name=amici_fb;type=push;active=1;class=canonical;owner_project=amici-fb;source_service=amici_fb.service;env=/home/daniele/codex-workspace/scripts/amici_fb/.env;interval=86400;timeout=48;retry=86400;maxretries=2;tags=482917-reviewed,push-monitor;notification=1;latest=up 2026-06-10T11:40:29
monitor=6;name=disk-usage-monitor;type=push;active=1;class=canonical_noisy_fixed;owner_project=disk-usage-monitor;source_service=disk-usage-monitor.service;env=/home/daniele/disk_usage_monitor/.env + /home/daniele/.config/environment.d/telegram.conf;interval=420;timeout=60;retry=300;maxretries=2;tags=482917-reviewed,push-monitor;notification=1;latest=up 2026-06-10T00:02:08
monitor=7;name=parcel-tracker;type=push;active=1;class=canonical;owner_project=parcel-tracker;source_service=parcel-tracker.service;script=/home/daniele/codex-workspace/parcel-tracker/parcel_tracker.py;interval=2400;timeout=60;retry=1800;maxretries=2;tags=482917-reviewed,push-monitor;notification=1;latest=up 2026-06-10T11:58:38
monitor=9;name=mint-home-backup-retention;type=push;active=1;class=canonical_noisy_fixed;owner_project=backup_docs;source_service=home-backup-retention-kuma-push.service;script=/home/daniele/home_backup_kuma_push.sh;env=/home/daniele/.config/home-backup/kuma-retention.env;interval=180;timeout=60;retry=120;maxretries=2;tags=482917-reviewed,push-monitor;notification=1;latest=up 2026-06-10T12:00:11
monitor=10;name=codex-token-watcher;type=push;active=0;class=obsolete_disabled;owner_project=codex-token-watcher;source_service=codex-usage-monitor.service;interval=60;timeout=48;retry=60;maxretries=3;tags=482917-reviewed,push-monitor,obsolete-disabled;notification=1;replacement=none;latest=down 2026-06-06T18:15:18
monitor=11;name=software audit mint;type=push;active=1;class=canonical_noisy_fixed;owner_project=mint-update-tracker;source_service=mint-update-tracker.service;env=/home/daniele/.config/mint-update-tracker/kuma.env;interval=120;timeout=60;retry=120;maxretries=2;tags=482917-reviewed,push-monitor;notification=1;latest=up 2026-06-10T12:00:37
monitor=12;name=Mint Freeze Analysis;type=group;active=1;class=status_group;parent=none;interval=60;timeout=45;retry=60;maxretries=1;children=13,14,15,16,17;notification=none;latest=down 2026-06-10T12:01:07 due child status
monitor=13;name=Freeze Gaps;type=push;active=1;class=canonical_freeze;owner_project=mint-freeze-forensics;source_service=mint-freeze-forensics.service;env=/home/daniele/.config/mint-freeze-forensics/kuma.env key=KUMA_PUSH_FREEZE_GAPS;parent=12;interval=60;timeout=45;retry=60;maxretries=1;tags=mint-freeze-analysis;notification=1;latest=down 2026-06-10T12:01:47
monitor=14;name=PSI Memory;type=push;active=1;class=canonical_freeze;owner_project=mint-freeze-forensics;source_service=mint-freeze-forensics.service;env=/home/daniele/.config/mint-freeze-forensics/kuma.env key=KUMA_PUSH_PSI_MEMORY;parent=12;interval=60;timeout=45;retry=60;maxretries=1;tags=mint-freeze-analysis;notification=1;latest=pending 2026-06-10T12:01:36
monitor=15;name=PSI IO;type=push;active=1;class=canonical_freeze;owner_project=mint-freeze-forensics;source_service=mint-freeze-forensics.service;env=/home/daniele/.config/mint-freeze-forensics/kuma.env key=KUMA_PUSH_PSI_IO;parent=12;interval=60;timeout=45;retry=60;maxretries=1;tags=mint-freeze-analysis;notification=1;latest=pending 2026-06-10T12:01:36
monitor=16;name=Guardian Alerts;type=push;active=1;class=canonical_freeze;owner_project=mint-freeze-forensics;source_service=mint-resource-guardian.service;env=/home/daniele/.config/mint-freeze-forensics/kuma.env key=KUMA_PUSH_GUARDIAN_ALERTS;parent=12;interval=60;timeout=45;retry=60;maxretries=1;tags=mint-freeze-analysis;notification=1;latest=up 2026-06-10T12:00:53
monitor=17;name=Forensics Alive;type=push;active=1;class=canonical_freeze_alive;owner_project=mint-freeze-forensics;source_service=mint-freeze-forensics.service;env=/home/daniele/.config/mint-freeze-forensics/kuma.env key=KUMA_PUSH_FORENSICS_ALIVE;parent=12;interval=60;timeout=45;retry=60;maxretries=2;tags=mint-freeze-analysis;notification=1;latest=up 2026-06-10T12:01:46
http_monitors_live=none as of 2026-06-10
heartbeat_monitor_term=Kuma push monitors are heartbeat-style monitors in this deployment; no separate non-push heartbeat type exists in live DB.

NOTIFICATION_INVENTORY:
notification=1;name=Notifica Telegram (1);type=telegram;active=1;default=1;has_chat_id=yes;has_bot_token=yes;values_not_printed
mapping=monitor_ids 1,2,3,4,5,6,7,9,10,11,13,14,15,16,17 -> notification 1
mapping_absent=monitor_id 12 group has no direct notification
policy=keep Telegram on active critical/warning monitors unless user explicitly requests retune; reduce noise by fixing pusher semantics/timing first
noisy_fixed_482917=cloud backup,disk-usage-monitor,parcel-tracker,mint-home-backup-retention,software audit mint
known_noise_current=freeze group children 13-15/16/17 can flap if pusher cadence misses 60s/45s window; verify mint-freeze-forensics local state before retuning
disabled_dismissed=mint heartbeat,rsync-transfer,codex-token-watcher

ARCH:
kuma=Docker compose runtime on Oracle VM, not Mint host service.
data=SQLite under /opt/uptime-kuma/data plus docker logs; push tokens live in DB/env files and must not enter MegaVault.
notification=single Telegram notification id 1 reused by canonical monitors.
status_page=Mint Freeze Analysis status page id=1 slug=mint-freeze-analysis title="Mint Freeze Analysis" auto_refresh_interval=60 published=1
status_page_group=monitor_group rows id 1-5 map monitors 13-17 to group_id=1 weights 1013-1017 send_url=0
tags=1:482917-reviewed,2:push-monitor,3:obsolete-disabled,4:mint-freeze-analysis
user=1 active username=saldrenafil

FLOW:
push_flow=local service/timer -> local pusher reads env -> GET http://150.230.148.128:3001/api/push/<token>?status=...&msg=... -> Kuma heartbeat row -> optional Telegram id 1
config_flow=backup DB -> mutate via UI/API/SQLite -> restart container only when direct DB edit requires runtime reload -> verify monitor table+heartbeat+UI/status page
noise_flow=classify from heartbeat/local state -> repair pusher or widen timing -> preserve real failures -> document in ALERT_REGISTRY/report
registry_flow=any monitor/service/env/timing change -> update ai/global/SERVICE_REGISTRY.md + ai/global/ALERT_REGISTRY.md + this doc + human changelog

INV:
arch=Kuma external to Mint; local services only push.
data=DB path /opt/uptime-kuma/data/kuma.db; WAL/SHM present; backup before any write.
ux=UI available at http://150.230.148.128:3001 but docs must record every manual setting change.
backup=/opt/uptime-kuma/backups
security=never print push_token,full /api/push URL,Telegram token,Telegram chat id,notification config JSON raw.
ops=no destructive monitor/DB change without current DB backup.
version=image louislam/uptime-kuma:2.3.2;schema must be rechecked after image upgrade.

BUILD:
cmd=not built locally
env=Oracle VM Docker Compose
requirements=ssh key /home/daniele/codex-workspace/projects/vm_oracle/ssh-key-2026-02-01.key;sudo on VM;sqlite3 on VM

TEST:
runtime=ssh VM 'sudo docker ps --filter name=uptime-kuma; sudo docker inspect uptime-kuma --format "{{.State.Status}} {{.State.Health.Status}}"'
db=sudo sqlite3 -readonly /opt/uptime-kuma/data/kuma.db 'PRAGMA integrity_check;'
monitor_inventory=sudo sqlite3 -readonly -header -column /opt/uptime-kuma/data/kuma.db 'select id,name,type,active,parent,"interval",timeout,retry_interval,maxretries from monitor order by id;'
push=run source pusher or curl redacted URL; expect HTTP 200 and new heartbeat row timestamp for that monitor
notification=prefer UI test for notification id 1; if DB-only, verify monitor_notification binding and do not expose config token/chat id

DATA:
DB=SQLite
Path=/opt/uptime-kuma/data/kuma.db
WAL=/opt/uptime-kuma/data/kuma.db-wal
SHM=/opt/uptime-kuma/data/kuma.db-shm
SchemaTables=api_key,docker_host,domain_expiry,group,heartbeat,incident,maintenance,monitor,monitor_group,monitor_notification,monitor_tag,notification,notification_sent_history,setting,status_page,tag,user,stat_*
BackupDir=/opt/uptime-kuma/backups
BackupCmd=sudo mkdir -p /opt/uptime-kuma/backups && sudo cp -a /opt/uptime-kuma/data/kuma.db /opt/uptime-kuma/backups/kuma-pre-<prompt>-$(date -u +%Y%m%dT%H%M%SZ).db
BackupVerify=sudo ls -lh /opt/uptime-kuma/backups/kuma-pre-<prompt>-*.db && sudo sqlite3 -readonly <backup_path> 'PRAGMA integrity_check;'
RestoreCmd=stop container -> copy bad DB aside -> cp backup to /opt/uptime-kuma/data/kuma.db -> chown root:root if needed -> docker compose up -d -> integrity+monitor query+UI check
SQLiteSafeInspect=PRAGMA integrity_check; .tables; PRAGMA table_info(monitor); PRAGMA table_info(notification); select monitor inventory without push_token/url secrets
SQLiteForbidden=delete from monitor/heartbeat/notification; update push_token without backup; select push_token/config raw in logs; vacuum/prune large DB during quota pressure without explicit task
HistoricalSQLFound=prompt_482917 reports remote SQLite query after restart but not exact SQL; human troubleshooting used select id,name,type,active,parent from monitor order by id; prompt_731845 exact readonly queries documented here.

RUNBOOK:
preflight=git clean MegaVault; read this doc + SERVICE_REGISTRY + ALERT_REGISTRY; SSH to VM; confirm docker.service active, container healthy, DB integrity ok, root disk has headroom; create DB backup before writes.
add_push_monitor=1 choose stable name lower/kebab matching service; 2 verify no same-name row; 3 backup DB; 4 generate 32-char token outside shell history; 5 insert monitor type push user_id=1 interval/timeout/retry/maxretries; 6 insert monitor_notification monitor_id,new notification_id=1; 7 add tag push-monitor and optional 482917-reviewed; 8 store full URL only in service env; 9 run pusher; 10 verify heartbeat timestamp; 11 update registries/docs/report.
add_http_monitor=1 backup DB; 2 prefer UI because URL may contain credentials; 3 if SQL, insert type=http with url,method GET,accepted_statuscodes_json='["200-299"]',user_id=1,interval/timeout/retry/maxretries; 4 bind notification only if alerting desired; 5 run readonly monitor query; 6 verify first heartbeat; 7 document endpoint without secrets.
add_heartbeat_monitor=use add_push_monitor; in this deployment heartbeat means Kuma push monitor.
disable_monitor=1 backup DB; 2 update monitor set active=0 where id=<id>; 3 add obsolete-disabled tag if permanent; 4 do not delete heartbeat/history; 5 verify active=0; 6 move ALERT_REGISTRY entry to disabled section.
mark_obsolete=disable_monitor plus reason in ALERT_REGISTRY state=disabled_obsolete_<reason>; keep source service disabled/static unless user asks runtime repair.
rename_monitor=1 backup DB; 2 update monitor set name='<new>' where id=<id>; 3 update ALERT_REGISTRY alert name and project docs; 4 verify pusher token unchanged and heartbeat still lands on same id.
modify_intervals=1 prove current flapping/noise from heartbeat history+local state; 2 backup DB; 3 update monitor set interval=<sec>,timeout=<sec>,retry_interval=<sec>,maxretries=<n> where id=<id>; 4 restart container if UI/runtime cache stale; 5 verify heartbeat and Telegram noise.
replace_push_token=prefer Kuma UI; if SQLite required, backup DB, generate token, update only monitor.push_token for id, immediately update one env file, run pusher, verify HTTP 200; never print token or commit env.
replace_push_endpoint=usually env-only on local service; if Kuma host/port changes update env files and docs; if token changes use replace_push_token.
replace_telegram_config=prefer UI notification id 1 edit/test; if SQLite required, backup DB and update notification.config without printing JSON; verify notification id 1 remains active/default and test delivery manually.
verify_monitor=readonly query monitor config, latest heartbeat, source systemd unit, source state/log; for push monitors run pusher once if safe; HTTP 200 from push plus fresh heartbeat is success.
verify_notification=check monitor_notification binding to id 1, notification active/default/type telegram, then use Kuma UI notification test or safe manual alert; do not read/print bot token/chat id.
reduce_noise=do not disable real failures; fix pusher idempotence/flock/nonfatal curl first; widen interval/timeout/retry only after measuring cadence; split roles if one pusher reports unrelated jobs; preserve Telegram for critical alerts.
recover_broken_monitor=check active flag, latest heartbeat, source unit/timer, env file presence/perms, script exists, local state truth; only then retune or replace token; for disabled obsolete monitors do not revive without owner_project docs.
restore_from_backup=stop container with docker compose down; copy current data dir metadata and DB aside; restore selected DB; docker compose up -d; wait healthy; integrity_check; monitor count; verify critical pushers.

SQLITE_OPERATIONS:
pre_write=ssh VM; sudo sqlite3 -readonly DB 'PRAGMA integrity_check;'; BackupCmd; BackupVerify; inspect .schema for touched table.
post_write=sudo docker compose -f /opt/uptime-kuma/docker-compose.yml restart uptime-kuma if DB edit not visible; verify docker healthy; readonly query changed rows; run pusher/heartbeat.
safe_query_monitor=select id,name,type,active,parent,"interval",timeout,retry_interval,maxretries,upside_down from monitor order by id;
safe_query_notifications=select id,name,active,is_default,json_extract(config,'$.type') as notification_type,json_extract(config,'$.telegramChatID') is not null as has_chat_id,json_extract(config,'$.telegramBotToken') is not null as has_bot_token from notification order by id;
safe_query_bindings=select monitor_id,notification_id from monitor_notification order by monitor_id,notification_id;
safe_query_latest=select m.id,m.name,h.status,h.time,h.ping,h.duration from monitor m left join heartbeat h on h.id=(select h2.id from heartbeat h2 where h2.monitor_id=m.id order by h2.time desc limit 1) order by m.id;
safe_query_tags=select t.name,mt.monitor_id,m.name from monitor_tag mt join tag t on t.id=mt.tag_id join monitor m on m.id=mt.monitor_id order by mt.monitor_id,t.name;
write_add_push=insert into monitor (name,type,user_id,interval,timeout,retry_interval,maxretries,push_token,created_date) values ('<name>','push',1,<interval>,<timeout>,<retry>,<maxretries>,'<32_char_token>',DATETIME('now')); then select id by name; then bind notification/tag.
write_add_http=insert into monitor (name,type,user_id,url,method,interval,timeout,retry_interval,maxretries,created_date) values ('<name>','http',1,'<url>','GET',<interval>,<timeout>,<retry>,<maxretries>,DATETIME('now')); then bind notification/tag if alerting required.
write_disable=update monitor set active=0 where id=<id>;
write_interval=update monitor set interval=<sec>,timeout=<sec>,retry_interval=<sec>,maxretries=<n> where id=<id>;
write_rename=update monitor set name='<new_name>' where id=<id>;
write_bind_notification=insert into monitor_notification (monitor_id,notification_id) values (<id>,1);
write_tag=insert into monitor_tag (monitor_id,tag_id,value) values (<id>,2,'');
write_status_page_child=insert into monitor_group (monitor_id,group_id,weight,send_url) values (<monitor_id>,1,<1000+monitor_id>,0);

MEGAVAULT_INTEGRATION:
SERVICE_REGISTRY_UPDATE=when source service/timer/script/env changes, new pusher is added, service is disabled/obsolete, or owner_project changes.
ALERT_REGISTRY_UPDATE=when monitor id/name/type/active/severity/source_service/notification/noise policy changes.
REPORT_CREATE=when runtime Kuma/SQLite/UI setting is changed, monitor added/disabled/renamed, token rotated, noise policy changed, or restore performed.
NAMING=monitor name should match owner service slug; push env var should include project prefix; report ai/reports/prompt_<id>_kuma_<action>.md.
LINKS=owner project AI doc must mention monitor id and env path; ALERT_REGISTRY maps monitor->owner_project/source_service; SERVICE_REGISTRY maps source_service->purpose/criticality.

DNB:
dnb=do not use Kuma for reboot/restart/kill remediation.
dnb=do not commit push URLs/tokens or Telegram config.
dnb=do not delete monitor/history rows for obsolete monitors unless user explicitly requests purge after backup.
dnb=do not trust systemctl success alone for oneshot pushers; verify local state and Kuma heartbeat.
dnb=do not revive rsync-transfer/codex-token-watcher/mint heartbeat monitors without owner-specific docs and live source proof.
dnb=do not run destructive Oracle cleanup/restic retention from Kuma docs.

BUG:
issue=direct DB edit can require container restart for UI/runtime refresh;workaround=restart uptime-kuma container after backup+write if query says changed but UI stale.
issue=stat_minutely/stat_daily SQLITE_CONSTRAINT lines in error.log on 2026-06-10;status=observed_not_fixed;risk=log noise/stat aggregation issue.
issue=freeze monitor group was down/pending during 2026-06-10 audit despite service running;status=documented;next=diagnose mint-freeze-forensics pusher cadence only in runtime task.

RISK:
risk=Oracle root disk 93% used can affect Docker healthchecks/log writes;mitigation=check df before backup/restore and do not grow logs blindly.
risk=push token leak via shell history/log/docs;mitigation=redact outputs and use env files mode 600.
risk=direct SQLite writes across Kuma upgrade schema drift;mitigation=PRAGMA table_info before write.
risk=Kuma false red from pusher cadence/local mount boot timing;mitigation=verify service-local state before alert retune.

OPERATIONAL_MEMORY:
decision=Kuma is observability only; no remediation actions originate from Kuma.
decision=Telegram notification id 1 is shared default channel for all current non-group monitors.
decision=Obsolete monitors stay disabled with history retained, not deleted.
decision=Service-specific pushers replaced generic mint heartbeat.
decision=Mint Freeze Analysis group id 12/status page slug mint-freeze-analysis owns monitors 13-17.
deprecated=mint heartbeat id1;reason=generic noisy heartbeat replaced by service-specific monitors.
deprecated=rsync-transfer id2;reason=no verified live transfer runner when disabled; do not reactivate until transfer source/dest/process are verified.
deprecated=codex-token-watcher id10;reason=legacy/Cloudflare/login state not reliable; current VM Codex watcher docs say Kuma not configured.
historical_error=wrong push URL reused between backup/retention caused red retention; use dedicated env per monitor.
historical_error=log freshness alone caused rsync false down; verify exact rsync pid/mount safety.
historical_error=curl rc 7/28 killed pusher under set -e; wrap push as nonfatal unless pusher is sole service.
historical_error=DB_BUSY and intentional ABORTED_SAFE were once treated as hard DOWN; map documented wait/guard states to warning/up only with persisted reason.

ROAD:
now=docs operational; runtime unchanged.
next=separate runtime task should diagnose 2026-06-10 Freeze Gaps/PSI pending/down if user asks.
later=replace direct DB edits with authenticated Kuma API only after API auth is verified and documented.

LINK:
meta=../../../projects/vm_oracle/oracle-uptime-kuma/dev/project.metadata.json
human=../../human/projects/oracle-uptime-kuma/overview.md
runtime=ssh ubuntu@150.230.148.128 /opt/uptime-kuma
report_482917=../reports/prompt_482917_kuma_noise_reduction.md
report_428691=../reports/prompt_428691_kuma_docs_normalization.md
report_731845=../reports/prompt_731845_kuma_operational_audit.md
registries=../global/SERVICE_REGISTRY.md,../global/ALERT_REGISTRY.md,../global/DATA_REGISTRY.md

OPEN:
open=Kuma UI/API auth workflow still undocumented; DB/UI paths are verified.
open=Telegram delivery test not executed in prompt_731845 to avoid runtime notification.
open=No HTTP monitors currently exist; HTTP runbook is schema-derived and must be smoke-tested when first used.
