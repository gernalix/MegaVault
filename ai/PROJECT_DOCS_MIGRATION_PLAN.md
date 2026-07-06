VERSION=1
STATUS=PLAN_ONLY
MODE=ultracompressed
DOC_CLASS=guide
LIFECYCLE=REFERENCE
AUTHORITY_LEVEL=L6
SOURCE_OF_TRUTH=no
PURPOSE=migrate_project_specific_docs_out_of_MegaVault_without_automatic_file_moves
PROTOCOL=ai/MEGAVAULT_PROTOCOL.md
DATE=2026-07-05

RULE:
megavault_scope=global_aspecific_docs_only
project_ai_target=<project_repo>/docs/ai/
project_human_target=<project_repo>/docs/human/
incident_ai_target=<project_repo>/docs/ai/INCIDENT_REGISTRY.md
incident_human_target=<project_repo>/docs/human/INCIDENT_REGISTRY.md
human_source=derived_from_docs_ai+code+real_state
human_forbid=primary_operational_source
move_policy=no_automatic_moves;per_project_verify_repo+metadata+git_clean_first

LEGACY_PROJECT_DOCS:
legacy_ai_archive=ai/archive/projects_legacy/*.md;project_specific;not_active;read_default=no
legacy_ai_projects=amici-fb,android,android-app-template,aw-converter,chatgpt-chrome-debug,codex-html-live,codex-token-watcher,codex-wrapper,disk-usage-monitor,facebook-video-archiver,facedownassup-downloader,git-change-ledger,grindr-web-exporter,installa-app,linux-mint-service-dashboard,luoghi,maintenance-486,megavault-project-exporter,mint-cloud-backup,mint-freeze-forensics,mint-manual-updates,mint-update-tracker,multitimetracker,oracle-backup-service,oracle-uptime-kuma,os-observer,owntracks-watcher,parcel-tracker,remote-codex-phone,remote-opt-oracle-backup,soldi,sostanze,supercontacts,surface-recovery-hardening,system-watchdog,windows-flight-recorder,windows-winget-daily-update,windowtabnotes
legacy_human_projects=human/projects/*;project_specific;not_AI_authority;read_default=no
human_projects=amici-fb,android,android-app-template,aw-converter,chatgpt-chrome-debug,codex-html-live,codex-token-watcher,codex-wrapper,disk-usage-monitor,facebook-video-archiver,facedownassup-downloader,git-change-ledger,grindr-web-exporter,installa-app,linux-mint-service-dashboard,luoghi,maintenance-486,megavault-project-exporter,mint-cloud-backup,mint-freeze-forensics,mint-manual-updates,mint-update-tracker,multitimetracker,oracle-backup-service,oracle-uptime-kuma,os-observer,owntracks-watcher,parcel-tracker,remote-codex-phone,remote-opt-oracle-backup,soldi,sostanze,supercontacts,surface-recovery-hardening,system-watchdog,windows-flight-recorder,windows-winget-daily-update,windowtabnotes

MIGRATION_STEPS:
1=choose_one_project;verify_repo_path_from_ai/PROJECT_INDEX.md+metadata
2=git_clean_before_in_project_repo
3=create_or_update_docs/ai/ and docs/human/
4=copy_or_regenerate_AI_from_MegaVault_ai/archive/projects_legacy/<slug>.md;compress;verify_against_code_real_state
5=copy_or_regenerate_human_from_MegaVault_human/projects/<slug>/;derive_from_docs_ai+code+state
6=move_project_incidents_to_docs/ai/INCIDENT_REGISTRY.md+docs/human/INCIDENT_REGISTRY.md_if_project_specific
7=update_project_metadata_ai_doc/human_doc_to_local_docs_paths
8=update_MegaVault_project_indices_to_project_local_docs_targets
9=keep_MegaVault_project_specific_docs_archived_only_after_project_commit_pushed_and_indices_updated
10=git_clean_after_in_project_repo_and_MegaVault

INCIDENT_MIGRATION:
global_ai_current=ai/global/INCIDENT_REGISTRY.md
global_human_current=human/global/INCIDENT_REGISTRY.md
rule=keep_global_schema_and_cross_project_index_in_MegaVault
project_specific_entries=migrate_to_owner_project_docs_ai_and_docs_human_when_owner_repo_verified

BLOCKERS:
unknown_repo_path=disk-usage-monitor,windows-flight-recorder
metadata_missing_or_absent=some_rows;resolve_per_project_before_move
historical_reports=do_not_rewrite;leave_as_immutable_context
