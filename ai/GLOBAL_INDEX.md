# GLOBAL_INDEX
VERSION=3
STATUS=BOOTSTRAP_ROUTER
FORMAT=ultracompact

READ:
all=MEGAVAULT_PROTOCOL.md
facts=../megavault.sqlite
validate=python3 ../megavault.py validate
project_lookup=python3 ../megavault.py project <alias-or-slug>

ROUTING:
project_id=resolve_only_from_sqlite:project_aliases->projects
repositories=sqlite:repositories
hosts=sqlite:hosts
services=sqlite:services
integrations=sqlite:integrations
secrets=sqlite:secret_refs;values_never_stored
incidents=sqlite:incidents+incident_events
timeline=sqlite:events
legacy=../legacy/README.md;non_authoritative;explicit_historical_request_only

RULE:
if_fact_missing=verify_live_or_mark_UNKNOWN
if_conflict=sqlite_current_fact_beats_deleted_markdown;Git_history_for_past_reports
