# Prompt 731845 Kuma Operational Audit

META:
prompt=731845
date=2026-06-10
scope=docs_only;Oracle_Uptime_Kuma;MegaVault
runtime_changed=no
db_changed=no
monitor_changed=no
protocol=MEGAVAULT_PROTOCOL.md:v8

GAPS_FOUND:
gap=AI doc described Kuma but lacked full live runtime inventory for docker.service, compose service, logs, WAL/SHM, backup list, disk risk.
gap=AI doc lacked complete live monitor table, tags, notification mapping, status page mapping, latest heartbeat evidence.
gap=global ALERT_REGISTRY and DATA_REGISTRY still said remote DB live query UNKNOWN from older SSH timeout.
gap=runbook covered push/disable/noise at high level but not HTTP monitor, token rotation, endpoint replacement, Telegram replacement, restore, safe/forbidden SQL.
gap=human docs explained project but did not expose enough operational status for Daniele to understand current active/obsolete monitors.

LIVE_VERIFICATION_2026_06_10:
host=ubuntu@150.230.148.128 hostname=instance-20260201-1126
docker=uptime-kuma container 15c942e18d85 image louislam/uptime-kuma:2.3.2 healthy
compose=/opt/uptime-kuma/docker-compose.yml service=uptime-kuma restart=unless-stopped port=3001
db=/opt/uptime-kuma/data/kuma.db integrity=ok size=8806400 wal=5677392 shm=32768
backups=/opt/uptime-kuma/backups includes kuma-pre-482917-20260606T181225Z.db,kuma-pre-847261-freeze-analysis.db
logs=/opt/uptime-kuma/data/error.log,docker_json_log
disk=/ 93% used on /dev/sda1
monitors=17 rows;active_push=3,4,5,6,7,9,11,13,14,15,16,17;disabled=1,2,10;group=12
notification=Telegram id=1 active/default bound to all non-group monitors
status_page=mint-freeze-analysis id=1 maps monitors 13-17

ADDED:
ai_doc=runtime inventory, monitor inventory, notification inventory, runbook for create/disable/rename/interval/token/endpoint/Telegram/verify/noise/recover/restore, SQLite safe/forbidden queries, MegaVault integration, Operational Memory
global_registries=updated ALERT_REGISTRY and DATA_REGISTRY from live VM verification
human_docs=overview/features/troubleshooting/roadmap/changelog updated from AI doc

NOT_RUNTIME_ACTIONS:
no=docker compose restart
no=sqlite write
no=monitor edit
no=notification test
no=token read/print

OPEN:
open=Kuma UI/API auth workflow not verified
open=Telegram delivery not tested to avoid runtime notification
open=HTTP monitor procedure is schema-derived because no HTTP monitor exists live
