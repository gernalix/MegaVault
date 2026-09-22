#!/usr/bin/env python3
"""Explicit MegaVault composition root."""

from __future__ import annotations

import sys

from ai.megavault_core import (
    ROOT,
    DB,
    PROTOCOL,
    SCHEMA_VERSION,
    CANONICAL_TAG_RE,
    DEFAULT_CANONICAL_TAGS,
    DEFAULT_TAG_ALIASES,
    ROOT_ALLOWLIST,
    ALLOWED_TRACKED_MARKDOWN,
    TRACKED_FORBIDDEN_PREFIXES,
    TRACKED_FORBIDDEN_FILES,
    REQUIRED_PROTOCOL_FAMILIES,
    SECRET_PATTERNS,
    TagConflictError,
    TagNotFoundError,
    connect,
    PROMPT_ID_MIN,
    PROMPT_ID_SPACE,
    PROMPT_ID_STATUSES,
    ensure_prompt_id_schema,
    allocate_prompt_id,
    bind_prompt_id_request,
    backfill_prompt_ids,
    parse_prompt_id_file,
    extract_prompt_ids,
    prompt_ids_from_git_history,
    prompt_ids_from_prompt_dir,
    prompt_ids_from_text_tree,
    create_prompt_id_backup,
    backfill_prompt_ids_from_sources,
    prompt_content_sha256,
    materialize_prompt_id,
    mark_prompt_id_used,
    cancel_prompt_id,
    smoke_prompt_id,
    table_columns,
    table_exists,
    ensure_column,
    incident_id_is_integer,
    normalize_tag_name,
    normalize_canonical_tag_name,
    resolve_tag,
    create_tag,
    resolve_or_create_tag,
    ensure_default_incident_taxonomy,
    add_tag_alias,
    link_incident_tag,
    search_incidents_by_tags,
    split_legacy_tag_tokens,
    create_incident,
    execute_statements,
    create_incident_tables,
    migrate_incident_schema,
    backfill_legacy_incident_tags,
    normalize_remote_url,
    git_value,
    repository_runtime_parts,
    infer_repository_kind,
    refresh_repository_index_rows,
    normalized_sql,
    ensure_view,
    ensure_codex_project_index_view,
    ensure_codex_retrieval_views,
    PROJECT_CONTEXT_COMPONENTS,
    PROJECT_CONTEXT_OPERATIONS,
    ensure_project_context_schema,
    migrate_project_index_schema,
    git_tracked,
    protocol_semantic_errors,
    secret_scan_errors,
    schema_errors,
    validate,
    print_errors,
    project,
    CODEX_PROJECT_FIELDS,
    project_index_row,
    project_list_command,
    print_project_retrieval_rows,
    CODEX_WORK_QUEUE_FIELDS,
    CODEX_STATUS_LIST_FIELDS,
    project_view_command,
    project_show_command,
    CODEX_PROJECT_CONTEXT_FIELDS,
    codex_project_context_command,
    project_path_command,
    normalize_github_remote,
    repo_slug,
    next_repository_id,
    find_registered_github_repo,
    local_repository_metadata,
    local_repository_matches,
    register_local_repo_command,
    register_github_repo_command,
    migrate_database,
    print_incident_rows,
    tag_list_command,
    tag_resolve_command,
    tag_create_command,
    tag_command,
    tag_alias_command,
    incident_tag_command,
    incident_search_command,
    incident_command,
    incident_create_command,
)
from ai.megavault_core import main as _core_main
from ai.operational_indexes import dispatch as _dispatch_operational
from ai.operational_indexes import migrate_operational_indexes
from ai.workflow_events import dispatch as _dispatch_workflow_events


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    operational = _dispatch_operational(args)
    if operational is not None:
        return operational
    workflow_events = _dispatch_workflow_events(args)
    if workflow_events is not None:
        return workflow_events
    if args and args[0] == "migrate":
        result = _core_main(args)
        if result != 0:
            return result
        return migrate_operational_indexes()
    return _core_main(args)


if __name__ == "__main__":
    raise SystemExit(main())
