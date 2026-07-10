# PROJECT_INDEX_EXTENDED
VERSION=4
STATUS=ACTIVE
MODE=codex_first
FORMAT=ultracompressed
SOURCE=PROJECT_INDEX+Fedora_live_revalidation_2026-07-09+task_714283+activity_593184
PROTOCOL=../MEGAVAULT_PROTOCOL.md
HOST_PROFILE=HOST_PROFILE.md
HUMAN=../../human/global/PROJECT_INDEX_EXTENDED.md

CURRENT_FEDORA:
host=fedora
home=/home/daniele
megavault=/home/daniele/MegaVault
project_runtime_migration=not_revalidated

RULES:
rule=PROJECT_INDEX.md_is_canonical_project_catalog
rule=this_file_maps_only_relations_verified_on_current_Fedora
rule=UNKNOWN_when_runtime_relation_not_verified
rule=project_paths+services+DBs+alerts_require_live_Fedora_evidence

RELATIONS_CURRENT:
project=MegaVault;repo=/home/daniele/MegaVault;db=/home/daniele/MegaVault/codex_global_timeline.sqlite;builder=/home/daniele/MegaVault/build_codex_global_timeline.py;service=none;timer=none
project=codex-session-logger;repo=/home/daniele/projects/codex-session-logger;remote=https://github.com/gernalix/codex-session-logger.git;branch=main;runtime=/home/daniele/.local/bin/codex-live;data=/home/daniele/.local/state/codex-session-logger/sessions;service=none;timer=none;status=installed+tested
project=WindowTabNotes;repo_local=removed;/home/daniele/projects/WindowTabNotes=absent;remote=https://github.com/gernalix/WindowTabNotes;branch=fedora-current-session-window-detection-927514;commit=40421981911c6d92111e9062eb20c506003d4d97;service=removed;data_backup=/home/daniele/WindowTabNotes-backup-351806
project=fedora-system-monitor;repo=/home/daniele/MegaVault/projects/fedora-system-monitor;remote=https://github.com/gernalix/fedora-system-monitor.git;branch=codex/593184-fedora-system-monitor;runtime=/usr/local/libexec/fedora-system-monitor;config=/etc/fedora-system-monitor;data=/var/lib/fedora-system-monitor;services=events+lifecycle+collector_templates;timers=fast+hourly+daily+weekly;path=software;status=installed+enabled+tested;activity=593184

NO_RUNTIME_RELATION_VERIFIED:
scope=all_other_indexed_projects
reason=services+timers+DBs+dashboards+monitors_not_revalidated_after_Fedora_migration

OPEN:
open=rebuild_cross_project_relations_incrementally_when_each_project_is_migrated_or_touched
