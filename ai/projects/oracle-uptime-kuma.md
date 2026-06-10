META:
name=Oracle Uptime Kuma
slug=oracle-uptime-kuma
path=/opt/uptime-kuma on ubuntu@150.230.148.128
repo=runtime
branch=runtime
prompt=847261
created=2026-06-07
protocol=MEGAVAULT_PROTOCOL.md:v8
updated=2026-06-10 prompt_428691
PURPOSE:
purpose=Uptime Kuma instance on Oracle VM used for Mint/backup/service telemetry
mode=black_box_history_alerting_visualization
not=remediation_engine
STACK:
host=Oracle VM instance-20260201-1126
url=http://150.230.148.128:3001
container=uptime-kuma
image=louislam/uptime-kuma:2.3.2
db=/opt/uptime-kuma/data/kuma.db
MAP:
entry=/opt/uptime-kuma/docker-compose.yml
ui=http://150.230.148.128:3001
core=/opt/uptime-kuma/data/kuma.db
db=SQLite
tests=docker ps; sqlite3 monitor query; push HTTP 200
scripts=UNKNOWN
avoid=browser automation,token logging,automatic remediation
identify_runtime=ssh -i /home/daniele/codex-workspace/projects/vm_oracle/ssh-key-2026-02-01.key ubuntu@150.230.148.128 'hostname; sudo docker ps --filter name=uptime-kuma; sudo ls -l /opt/uptime-kuma/docker-compose.yml /opt/uptime-kuma/data/kuma.db'
ARCH:
kuma=Oracle VM Docker container
storage=SQLite DB + WAL under /opt/uptime-kuma/data
notifications=Telegram notification id=1
integration=Mint services push HTTP /api/push/<token>
status_page_mint_freeze=slug mint-freeze-analysis; title Mint Freeze Analysis; monitors 13-17; auto_refresh_interval=60
FLOW:
mint_push=local pusher -> http://150.230.148.128:3001/api/push/<token>
config_change=backup DB -> sqlite update -> docker restart uptime-kuma -> verify healthy
alerts=Kuma notification only; no reboot/restart/kill actions
new_monitor=check_existing_name/id -> backup DB -> prefer Kuma UI/API if available -> else inspect SQLite schema+clone/update pattern from existing push monitor -> restart container if DB edited -> verify monitor visible -> verify HTTP 200 push -> update SERVICE_REGISTRY+ALERT_REGISTRY+project docs
obsolete_monitor=backup DB -> set active=0 or mark obsolete/tag/rename; keep rows/history unless user explicitly asks purge -> verify disabled state -> update ALERT_REGISTRY disabled section
noise_reduction=prove false-positive class from heartbeat history/local state -> widen interval/timeout/retries or make pusher nonfatal/locked -> keep Telegram on real critical alerts -> document rationale and verification
INV:
arch=Kuma external to Mint host
data=/opt/uptime-kuma/data/kuma.db
ux=dashboard only; not required for Codex changes
backup=/opt/uptime-kuma/backups
version=image louislam/uptime-kuma:2.3.2
security=push tokens secret; document IDs not URLs
perf=container healthy after restart
ops=no destructive Kuma change without current DB backup
BUILD:
cmd=not built locally
env=Oracle VM Docker
requirements=ssh key /home/daniele/codex-workspace/projects/vm_oracle/ssh-key-2026-02-01.key
TEST:
container=sudo docker ps --filter name=uptime-kuma
db=sudo sqlite3 /opt/uptime-kuma/data/kuma.db 'select id,name from monitor'
push=Mint sample status HTTP 200
DATA:
DB=SQLite
Schema=monitor,monitor_notification,tag,monitor_tag,status_page,monitor_group
Backup=/opt/uptime-kuma/backups/kuma-pre-847261-freeze-analysis.db
Retention=managed by Kuma
Paths=/opt/uptime-kuma/data/kuma.db,/opt/uptime-kuma/docker-compose.yml
MintFreezeDashboard=http://150.230.148.128:3001/status/mint-freeze-analysis
BackupCmd=sudo mkdir -p /opt/uptime-kuma/backups && sudo cp -a /opt/uptime-kuma/data/kuma.db /opt/uptime-kuma/backups/kuma-pre-<prompt>-$(date -u +%Y%m%dT%H%M%SZ).db
InspectCmd=sudo sqlite3 -readonly /opt/uptime-kuma/data/kuma.db '.tables' && sudo sqlite3 -readonly -header -column /opt/uptime-kuma/data/kuma.db 'select id,name,type,active,interval,timeout,retry_interval,maxretries from monitor order by id;'
SqliteRule=if direct SQLite write needed: backup first, inspect .schema for touched tables, run explicit SQL, record SQL+rowcount/result in ai/report, restart container, verify with readonly query
PushVerify=curl -fsS --get --data-urlencode status=up --data-urlencode msg='manual verification <service>' '<redacted_KUMA_PUSH_URL>'
LocalPushPattern=store KUMA_PUSH_URL in service env file outside git; pusher uses bounded curl connect/max-time; curl failure nonfatal unless pusher itself is the monitored service
SystemdPattern=service oneshot or long-running pusher + timer interval shorter than Kuma interval; verify systemctl timer, pusher state JSON/log, and Kuma HTTP 200
DNB:
dnb=do not use Kuma for reboot/restart/kill remediation
dnb=do not commit push URLs/tokens
dnb=backup DB before direct sqlite changes
dnb=do not create duplicate monitors; update by name
dnb=do not delete monitor/history rows for obsolete monitors unless user explicitly requests purge after backup
dnb=do not silently change Kuma in browser/UI without documenting exact setting and verification
BUG:
issue=direct DB edit requires container restart for UI/runtime refresh
RISK:
risk=DB schema can change with Kuma upgrades; inspect schema before writes
risk=push monitor down state can be alert noise if local pusher stopped intentionally
risk=token leak via logs/docs; never print full /api/push URL
OPS:
codex_autonomy=when user requests Kuma setting change, Codex may change Kuma via SSH/UI/API/SQLite after fresh backup and live identification; no separate approval needed unless destructive/purge/cost/quota impact
preflight=git clean MegaVault; read HOST_PROFILE+SERVICE_REGISTRY+ALERT_REGISTRY+this doc; verify Oracle reachability; identify container/config/DB from live filesystem
backup_required=copy DB to /opt/uptime-kuma/backups before SQLite/UI setting changes that affect monitors/notifications/status pages
direct_sqlite=allowed only when UI/API unavailable or task explicitly accepts DB edit; use sqlite3 on VM, never copy DB into MegaVault; document queries/results
add_push_monitor=prefer reuse/update existing disabled monitor if same service semantics; otherwise create one monitor with stable name, Telegram notification id=1 if alerting required, interval/retry based on real pusher cadence, tag push-monitor
connect_local_service=add env-only push URL, add pusher command/timer, make push idempotent and bounded, write local push state when project already has state dir, avoid making external Kuma failure crash core service
verify_push=run local pusher or curl with token redacted; expect HTTP 200; then query/read Kuma monitor status/history; verify local timer/service state
disable_monitor=set inactive/active=0 or disable in UI, add obsolete-disabled tag/rename note, leave history intact, update ALERT_REGISTRY KUMA_MONITORS_DISABLED
reduce_noise=do not silence real failures; classify cause, widen timing windows, split roles, add initial heartbeat, lock duplicate pushers, map intentional waits to warning/up only when documented
registry_update=every new/changed service pusher goes in ai/global/SERVICE_REGISTRY.md; every new/disabled/retuned monitor goes in ai/global/ALERT_REGISTRY.md with owner_project, source_service, severity, false_positive_risk
ROAD:
now=Mint Freeze Analysis group + status page active
next=review graphs after 24-72h
later=replace direct DB edit with authenticated API if available
LINK:
meta=../../../projects/vm_oracle/oracle-uptime-kuma/dev/project.metadata.json
human=../../human/projects/oracle-uptime-kuma/overview.md
runtime=ssh ubuntu@150.230.148.128 /opt/uptime-kuma
report_482917=../reports/prompt_482917_kuma_noise_reduction.md
report_428691=../reports/prompt_428691_kuma_docs_normalization.md
OPEN:
open=browser login not used in prompt #847261
open=API auth details not documented; direct DB path verified
