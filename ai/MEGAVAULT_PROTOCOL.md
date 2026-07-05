VERSION=11
STATUS=FINAL_PERMANENT
MODE=codex_first
FORMAT=ultracompressed
AUDIENCE=codex
PURPOSE=global_doc_constitution
SCOPE=all_projects,all_tasks,all_docs
AUTHORITY=mandatory

# CORE
P1=ai_authoritative
P2=human_derived
P3=legacy_historical
P4=1_ai_doc_per_project
P5=max_info_density
P6=no_duplicate_truth
P7=no_invented_knowledge
P8=doc_debt=tech_debt
P9=code>docs
P10=metadata+ai_doc=>productive
P11=clean_git_required
P12=docs_before_final
P13=reuse_before_rewrite
P14=archive_default
P15=tooling_autonomy
P16=branch_documented
P17=large_artifacts_outside_vault
P18=unknown_explicit
P19=human_not_operational
P20=sync_state_required
P21=host_profile_required
P22=remote_clean_pushed_required
P23=incident_registry_required

# HOST_PROFILE
HOST_PROFILE=mandatory
HOST_PROFILE_PATH=ai/global/HOST_PROFILE.md
READ_ORDER=MEGAVAULT_PROTOCOL>HOST_PROFILE>project.metadata.json>ai_doc
HOST_PROFILE_REQUIRED_FOR=system,automation,monitoring,performance,backup,storage,linux
UNKNOWN_RULE=mark_UNKNOWN

# ANDROID
ANDROID_PROTOCOL=ai/ANDROID_PROTOCOL.md
ANDROID_AUTHORITY=mandatory
ANDROID_REQUIRED_FOR=android_projects,android_builds,android_releases,android_tooling
ANDROID_READ_ORDER=MEGAVAULT_PROTOCOL>HOST_PROFILE>ANDROID_PROTOCOL>metadata>ai_doc

# SOURCE_PRIORITY
SRC_ORDER=HOST_PROFILE>metadata>ai_doc>code>human>legacy
IF_CONFLICT=prefer_higher_priority
IF_STALE=update_from_code
INVENT_FACTS=forbidden

# ENTRY
ENTRY_ORDER=clean_check>protocol>host_profile>metadata>ai_doc>targeted_inspection>reuse>implementation
ENTRY_FORBID=repo_wide_scan,human_as_source,blind_copy

# GIT
CLEAN_REQUIRED=before+after
REMOTE_REQUIRED=yes
SYNC_REQUIRED=yes
PUSH_REQUIRED=yes
DIRTY_STATE=protocol_violation

# DOCS
AI_DOCS=dev/ai/*
HUMAN_DOCS=dev/human/*
AI_SOURCE=authoritative
HUMAN_SOURCE=derived
PROJECT_REQ=metadata,ai_doc,human_overview,human_roadmap,human_changelog,human_troubleshooting,links

# AI_DOC
AI_DOC_REQ=META,PURPOSE,STACK,MAP,ARCH,FLOW,INV,BUILD,TEST,DATA,DNB,BUG,RISK,ROAD,LINK,OPEN
LANG=key_value
LINE_RULE=1_line=1_fact

# UPDATE
UPDATE_AI_WHEN=arch,db,build,test,import_export,backup,versioning,release,ops,security,incident_registry
UPDATE_HUMAN_WHEN=ux,workflow,roadmap,changelog
DOC_CHECK_REQUIRED=yes

# REUSE
REUSE=preferred
REWRITE=last_resort

# TOOLING
TOOLING_AUTONOMY=yes
DEPENDENCY_AUTONOMY=yes
MISSING_DEPENDENCY=auto_install
BROKEN_DEPENDENCY=repair

# SECURITY
SECRET_COMMIT=forbidden
DESTRUCTIVE_ACTION=require_explicit_user_intent

# DB
SQLITE_DEFAULT=/home/ubuntu/sync_root/db/
DB_DOC_REQUIRED=yes

# INCIDENT_REGISTRY
INCIDENT_REGISTRY=mandatory_all_projects
INCIDENT_AI=dev/ai/INCIDENT_REGISTRY.md
INCIDENT_HUMAN=dev/human/INCIDENT_REGISTRY.md
INCIDENT_SQLITE_DEFAULT=/home/ubuntu/sync_root/db/incident_registry.sqlite
INCIDENT_SCHEMA=incidents+incident_events
INCIDENT_ID_RULE=root_cause_stable_slug
INCIDENT_FORBID=symptom_spam_ids
INCIDENT_UPDATE=automatic_healthcheck_monitor_fix
INCIDENT_BOOTSTRAP=required_new_project
INCIDENT_SIGNIFICANT_BUG=must_register

# VERSIONING
VERSIONING_DOC_REQUIRED=yes
VERSION_SKIP=forbidden
ANDROID_VERSIONING_SEE=ai/global/ANDROID_PROTOCOL.md

# FINAL_REPORT
FINAL_REPORT_REQ=files_changed,tests,test_result,docs,repo_status,commit,push,sync_state
FINAL_REPORT_FORBID=silent_failure,false_success

# VALIDATION
VALIDATE=metadata,ai_doc,human_docs,links,git_clean,remote_sync

# SUCCESS
SUCCESS=modify_project_from_metadata+ai_doc_without_repo_wide_scan
