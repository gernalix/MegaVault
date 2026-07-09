# PROJECT_INDEX_EXTENDED
VERSION=2
STATUS=ACTIVE
MODE=codex_first
FORMAT=ultracompressed
SOURCE=PROJECT_INDEX+Fedora_live_revalidation_2026-07-09
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

NO_RUNTIME_RELATION_VERIFIED:
scope=all_other_indexed_projects
reason=services+timers+DBs+dashboards+monitors_not_revalidated_after_Fedora_migration

OPEN:
open=rebuild_cross_project_relations_incrementally_when_each_project_is_migrated_or_touched
