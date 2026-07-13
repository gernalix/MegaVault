# PROJECT_INDEX_EXTENDED
VERSION=8
STATUS=ACTIVE
MODE=codex_first
FORMAT=ultracompressed
SOURCE=PROJECT_INDEX+Fedora_live_revalidation_2026-07-13+activity_593184+activity_471852+activity_846271+activity_583921+activity_684219
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
project=WindowTabNotes;repo_local=removed;/home/daniele/projects/WindowTabNotes=absent;remote=https://github.com/gernalix/WindowTabNotes;branch=fedora-current-session-window-detection-927514;commit=40421981911c6d92111e9062eb20c506003d4d97;service=removed;data_backup=/home/daniele/WindowTabNotes-backup-351806
project=fedora-system-monitor;repo=/home/daniele/MegaVault/projects/fedora-system-monitor;remote=https://github.com/gernalix/fedora-system-monitor.git;branch=codex/471852-fedora-system-monitor;version=1.1.0;runtime=/usr/local/libexec/fedora-system-monitor;config=/etc/fedora-system-monitor;data=/var/lib/fedora-system-monitor;services=events+lifecycle+collector_templates+optional_prometheus_disabled;timers=fast+hourly+daily+weekly;path=software;features=dashboard+timeline+trends+service_history+prometheus_optional;status=installed+enabled+tested;activity=471852
project=fedora-t7-backup;repo=/home/daniele/MegaVault/projects/fedora-t7-backup;remote=https://github.com/gernalix/fedora-t7-backup.git;branch=codex/684219-t7-connect-backup;commit=1495f135a81e9457e1efcb12a5db6689983b3c79;runtime=/usr/local/libexec/t7-restic-lifecycle;repository=/mnt/T7_BACKUP/restic-fedora;services=backup_lifecycle+disconnect_reminder;trigger=udev_disk_add_by_serial;timer=one_shot_30m_reminder;status=installed+trigger+single_job+backup+maintenance+unmount+notifications+restore+failsafe_tested;activity=684219

NO_RUNTIME_RELATION_VERIFIED:
scope=all_other_indexed_projects
reason=services+timers+DBs+dashboards+monitors_not_revalidated_after_Fedora_migration

OPEN:
open=rebuild_cross_project_relations_incrementally_when_each_project_is_migrated_or_touched
