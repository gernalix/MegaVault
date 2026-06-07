META:
name=Oracle Uptime Kuma
slug=oracle-uptime-kuma
path=/opt/uptime-kuma on ubuntu@150.230.148.128
repo=runtime
branch=runtime
prompt=847261
created=2026-06-07
protocol=MEGAVAULT_PROTOCOL.md:v4
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
ARCH:
kuma=Oracle VM Docker container
storage=SQLite DB + WAL under /opt/uptime-kuma/data
notifications=Telegram notification id=1
integration=Mint services push HTTP /api/push/<token>
FLOW:
mint_push=local pusher -> http://150.230.148.128:3001/api/push/<token>
config_change=backup DB -> sqlite update -> docker restart uptime-kuma -> verify healthy
alerts=Kuma notification only; no reboot/restart/kill actions
INV:
arch=Kuma external to Mint host
data=/opt/uptime-kuma/data/kuma.db
ux=dashboard only; not required for Codex changes
backup=/opt/uptime-kuma/backups
version=image louislam/uptime-kuma:2.3.2
security=push tokens secret; document IDs not URLs
perf=container healthy after restart
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
Schema=monitor,monitor_notification,tag,monitor_tag
Backup=/opt/uptime-kuma/backups/kuma-pre-847261-freeze-analysis.db
Retention=managed by Kuma
Paths=/opt/uptime-kuma/data/kuma.db,/opt/uptime-kuma/docker-compose.yml
DNB:
dnb=do not use Kuma for reboot/restart/kill remediation
dnb=do not commit push URLs/tokens
dnb=backup DB before direct sqlite changes
dnb=do not create duplicate monitors; update by name
BUG:
issue=direct DB edit requires container restart for UI/runtime refresh
RISK:
risk=DB schema can change with Kuma upgrades; inspect schema before writes
risk=push monitor down state can be alert noise if local pusher stopped intentionally
ROAD:
now=Mint Freeze Analysis group active
next=review graphs after 24-72h
later=replace direct DB edit with authenticated API if available
LINK:
meta=../../../projects/vm_oracle/oracle-uptime-kuma/dev/project.metadata.json
human=../../human/projects/oracle-uptime-kuma/overview.md
runtime=ssh ubuntu@150.230.148.128 /opt/uptime-kuma
OPEN:
open=browser login not used in prompt #847261
open=API auth details not documented; direct DB path verified
