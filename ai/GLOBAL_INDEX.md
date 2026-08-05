# GLOBAL_INDEX
VERSION=7
STATUS=BOOTSTRAP_ROUTER
FORMAT=ultracompact

READ:
all=MEGAVAULT_PROTOCOL.md
facts=../megavault.sqlite
validate=python3 ../megavault.py validate
project_lookup=python3 ../megavault.py project <alias-or-slug>
report_finish=python3 reporting.py --plain-file FINAL_REPORT_PLAIN.txt --technical-file FINAL_REPORT_TECHNICAL.txt --prompt-id PROMPT_ID

ROUTING:
project_id=resolve_only_from_sqlite:project_aliases->projects;integer_primary_key
repositories=sqlite:repositories
codex_project_index=sqlite:codex_project_index;one_row_per_project;deterministic_row_number
codex_work_queue=sqlite:codex_work_queue;LOCAL+REMOTE_ONLY_only;operational_fields
codex_status_views=sqlite:codex_remote_projects|codex_missing_projects|codex_archived_projects
project_cli=python3 ../megavault.py project-list|project-work-queue|project-remote|project-missing|project-archived|project-show PROJECT_ID|project-path PROJECT_ID|project-path --status PROJECT_ID
hosts=sqlite:hosts
services=sqlite:services
integrations=sqlite:integrations
secrets=sqlite:secret_refs;values_never_stored
incidents=sqlite:incidents+incident_events+tags+tag_aliases+incident_tags;and_search=multi_tag
timeline=sqlite:events
reporting=reporting.py->telegram_notify.send_task_reports;all_projects;plain_message+plain_attachment+technical_attachment
legacy=../legacy/README.md;non_authoritative;explicit_historical_request_only

RULE:
if_fact_missing=verify_live_or_mark_UNKNOWN
if_conflict=sqlite_current_fact_beats_deleted_markdown;Git_history_for_past_reports
report_finish_required=after_both_verified_reports_are_written;failure_must_be_reported_locally
