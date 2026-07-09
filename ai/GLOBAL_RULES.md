# GLOBAL_RULES
VERSION=2
STATUS=ACTIVE_ROUTING_SUMMARY
MODE=codex_first
FORMAT=ultracompressed
AUTHORITY=ai/MEGAVAULT_PROTOCOL.md
UPDATED=2026-07-09T00:00:00+02:00

READ_ORDER:
order=ai/MEGAVAULT_PROTOCOL.md>ai/global/HOST_PROFILE.md>dev/project.metadata.json>project/docs/ai>task_files>legacy_if_required
conflict=protocol+HOST_PROFILE+metadata+AI_doc>Human_docs+legacy
metadata_ai_conflict=stop+repair_before_implementation

HOST_SYSTEM_CURRENT:
os=Fedora_Linux_44_Workstation
host=fedora
user=daniele
home=/home/daniele
megavault=/home/daniele/MegaVault
shell=bash
package_manager=dnf
local_rule=Fedora_paths_and_commands_only

GLOBAL_DOCS:
host_ai=global/HOST_PROFILE.md
host_human=../human/global/HOST_PROFILE.md
service_ai=global/SERVICE_REGISTRY.md
data_ai=global/DATA_REGISTRY.md
network_ai=global/NETWORK_TOPOLOGY.md
storage_ai=global/STORAGE_TOPOLOGY.md
alert_ai=global/ALERT_REGISTRY.md
incident_ai=global/INCIDENT_REGISTRY.md
software_ai=global/SOFTWARE_INVENTORY.md
project_index_ai=PROJECT_INDEX.md+global/PROJECT_INDEX_EXTENDED.md
timeline_db=../codex_global_timeline.sqlite
timeline_report=../codex_global_timeline.md
timeline_ai=../codex_global_timeline_ai.md

WRITE_POLICY:
ai_format=ultracompressed_key_value
human_format=derived_readable
facts=verify_or_UNKNOWN
project_docs=project_repo/docs
megavault_scope=global_only
legacy=use_only_when_current_AI_docs_lack_required_context
secrets=never_store
timeline=run_build_codex_global_timeline.py_before_final

CODEX_FEDORA:
paths=/home/daniele/...
shell=bash
packages=dnf
services=systemctl+systemctl_--user
storage=findmnt+lsblk+df
android=flatpak+adb+sdkmanager+java+project_Gradle_wrapper
non_Fedora_local_assumptions=forbidden
