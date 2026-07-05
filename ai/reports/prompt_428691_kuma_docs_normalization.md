# Prompt 428691 Kuma Docs Normalization

META:
prompt=428691
date=2026-06-10
scope=docs_only;MegaVault;Oracle_Uptime_Kuma
protocol=MEGAVAULT_PROTOCOL.md:v8

RESULT:
canonical_project=ai/projects/oracle-uptime-kuma.md existed_before=yes
human_docs=human/projects/oracle-uptime-kuma existed_before=yes
runtime_changed=no
duplicates_created=no

DISCOVERY:
read=ai/MEGAVAULT_PROTOCOL.md,ai/GLOBAL_RULES.md,ai/global/HOST_PROFILE.md,ai/global/SERVICE_REGISTRY.md,ai/global/ALERT_REGISTRY.md,ai/projects/oracle-uptime-kuma.md,human/projects/oracle-uptime-kuma/*
searched=MegaVault rg Kuma/Uptime/push monitor/heartbeat/Oracle VM/Telegram/api push/monitor_id
historical_reports=ai/reports/prompt_482917_kuma_noise_reduction.md,human/system/uptime-kuma-482917.md

ADDED:
ai_doc=operational OPS for Codex Kuma changes: live identity, backup, add push monitor, disable obsolete monitor, reduce noise, connect local pusher, verify push, registry updates, SQLite rules
human_docs=readable overview/features/troubleshooting/changelog updates for Daniele
global_changelog=human/CHANGELOG.md entry

SAFETY:
rule=no destructive Kuma change without backup
rule=prefer tracked/documented changes over invisible UI edits
rule=if direct SQLite write is needed, backup first and document SQL/query result
token_policy=never print/commit full /api/push URLs
