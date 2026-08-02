#!/usr/bin/env python3
"""Minimal MegaVault validator and lookup tool."""

from __future__ import annotations

import argparse
import re
import sqlite3
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DB = ROOT / "megavault.sqlite"
PROTOCOL = ROOT / "ai" / "MEGAVAULT_PROTOCOL.md"
ROOT_ALLOWLIST = {
    ".git",
    ".gitignore",
    "ai",
    "legacy",
    "megavault.py",
    "megavault.sqlite",
    "tests",
}
TRACKED_FORBIDDEN_PREFIXES = (
    "human/",
    "docs/",
    "dev/",
    "backups/",
    "secrets/",
    "private/",
    "projects/",
    "ai/archive/",
    "ai/global/",
    "ai/projects/",
    "ai/reports/",
)
TRACKED_FORBIDDEN_FILES = {
    "codex_global_timeline.md",
    "codex_global_timeline_ai.md",
    "codex_global_timeline.sqlite",
    "build_codex_global_timeline.py",
    "protocol_lint.py",
}
REQUIRED_PROTOCOL_FAMILIES = {
    "capsulization": (
        "CAPSULIZATION=mandatory_all_projects",
        "CAPSULE_TARGET=100_percent",
        "NEW_CODE=capsule_only",
        "SHARED_LOGIC=capsule_only",
        "UI_DIRECT_DEPENDENCY=forbidden",
        "CROSS_MODULE_ACCESS=through_capsules_only",
        "LEGACY_REFACTOR=progressively_until_100_percent",
        "FINAL_GATE=verify_capsulization_before_final",
    ),
    "python_environment": (
        "PYTHON:",
        "env=global",
        "isolation=forbidden",
        "tools=venv|virtualenv|pipenv|poetry|uv",
        "override=user_explicit_request",
        "packages=reuse_global>install_global",
        "venv_without_override=protocol_violation",
    ),
    "single_trunk_git": (
        "model=trunk_based_single_developer;operative_branches=1",
        "direct_canonical_work=default",
        "per_task_branch=forbidden",
        "branch_chaining=forbidden",
        "commit_push_before_final=required_unless_user_explicitly_forbids",
        "final_branch_fields=repository,canonical_branch,current_branch,temp_branch_reason,integration_status,cleanup_status",
    ),
    "secret_policy": (
        "secret_values=never_store;reference_paths_only",
        "secrets=no_prompt_echo,no_command_echo,no_secret_values_in_logs_reports_repo_history",
        "secret_handling=read_only_when_task_requires;canonical_paths_from_database;reprompt_for_known_path_forbidden;rotation_manual_explicit_only",
    ),
    "project_id_authority": (
        "project_id_source=megavault.sqlite:projects+project_aliases_only;INTEGER_PRIMARY_KEY",
        "project_lifecycle=never_delete_project;archive_only;never_reuse_project_id;ids_unique_permanent_not_dense",
    ),
    "no_duplicate_truth": (
        "duplicate_truth=forbidden",
        "forbidden=reports_done,human_mirror,project_docs_in_MegaVault,generated_timeline_markdown,duplicate_registries",
        "project_docs=owner_repo_docs_code_tests;MegaVault_only_global_transversal_knowledge",
    ),
    "incident_policy": (
        "incidents=store_in_megavault.sqlite:incidents+incident_events;id=root_cause_stable_slug;forbid=symptom_spam_ids;status=OPEN|MITIGATED|RESOLVED|ACCEPTED",
    ),
    "final_reporting": (
        "final_fields=files_changed,tests,test_result,docs_or_MegaVault_updates,repo_status,commit,push,sync_state,branch_fields,execution_insights,blockers,optimization_opportunities,remaining_unresolved",
        "blockers=root_cause,impact,workaround,resolution,status;silent_workaround_retry_skip=forbidden",
        "optimization=root_cause,impact,estimated_future_savings,one_time_fix,priority,confidence,status;section=mandatory",
        "success_forbid=silent_failure,false_success,unverified_PASS",
    ),
    "android_policy": (
        "required_for=android_projects,android_builds,android_releases,android_tooling",
        "version=version.txt_integer_monotonic;derive_versionCode_versionName_apk_name;home_v_visible;skip_reuse_forbidden",
        "saf_sqlite=autoexport_all_app_data_on_db_change;atomic;validate_after_write;failure_visible;preserve_last_good;test_required",
        "i18n=en+it;no_hardcoded_user_visible_text;missing_translation_blocker",
    ),
}
SECRET_PATTERNS = (
    ("private_key", re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----")),
    ("github_token", re.compile(r"gh[pousr]_[A-Za-z0-9_]{36,}")),
    ("openai_key", re.compile(r"sk-[A-Za-z0-9]{20,}")),
    ("slack_token", re.compile(r"xox[baprs]-[A-Za-z0-9-]{20,}")),
    ("telegram_token", re.compile(r"\b[0-9]{8,10}:[A-Za-z0-9_-]{35,}\b")),
)


def connect() -> sqlite3.Connection:
    conn = sqlite3.connect(DB)
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def git_tracked() -> list[str]:
    git_dir = ROOT / ".git"
    if not git_dir.exists():
        return []
    import subprocess

    proc = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files"],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    return [line for line in proc.stdout.splitlines() if line]


def protocol_semantic_errors(raw: str | None = None) -> list[str]:
    errors: list[str] = []
    if raw is None:
        if not PROTOCOL.exists():
            return ["protocol_semantic_missing:file"]
        raw = PROTOCOL.read_text(encoding="utf-8")

    version_match = re.search(r"(?m)^VERSION=(\d+)$", raw)
    if not version_match or int(version_match.group(1)) < 19:
        errors.append("protocol_semantic_missing:version_at_least_19")

    for family, snippets in REQUIRED_PROTOCOL_FAMILIES.items():
        for snippet in snippets:
            if snippet not in raw:
                errors.append(f"protocol_semantic_missing:{family}:{snippet}")
    return errors


def secret_scan_errors(paths: list[str]) -> list[str]:
    errors: list[str] = []
    skip_suffixes = {".sqlite", ".pyc"}
    for path_text in paths:
        path = ROOT / path_text
        if path.suffix in skip_suffixes or not path.is_file():
            continue
        try:
            raw = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            raw = path.read_text(encoding="utf-8", errors="ignore")
        for name, pattern in SECRET_PATTERNS:
            if pattern.search(raw):
                errors.append(f"secret_scan:{name}:{path_text}")
    return errors


def validate() -> int:
    errors: list[str] = []
    if not DB.exists():
        errors.append("missing megavault.sqlite")
        print_errors(errors)
        return 1

    conn = connect()
    integrity = conn.execute("PRAGMA integrity_check").fetchone()[0]
    if integrity != "ok":
        errors.append(f"sqlite integrity_check failed: {integrity}")
    fk_errors = conn.execute("PRAGMA foreign_key_check").fetchall()
    if fk_errors:
        errors.append(f"foreign_key_check failed: {fk_errors!r}")

    ids = [row[0] for row in conn.execute("select project_id from projects")]
    if not ids or any(not isinstance(value, int) or value <= 0 for value in ids):
        errors.append("project_id must be positive integers")
    if len(ids) != len(set(ids)):
        errors.append("duplicate project_id")

    alias_dupes = conn.execute(
        "select alias, count(*) from project_aliases group by alias having count(*) > 1"
    ).fetchall()
    if alias_dupes:
        errors.append(f"duplicate aliases: {alias_dupes!r}")

    missing_permanent = conn.execute(
        """
        select p.project_id
        from projects p
        left join permanent_ids i
          on i.entity_type='project' and i.entity_id=p.project_id
        where i.entity_id is null
        """
    ).fetchall()
    if missing_permanent:
        errors.append(f"projects missing permanent_ids: {missing_permanent!r}")

    root_entries = {p.name for p in ROOT.iterdir()}
    unexpected = sorted(root_entries - ROOT_ALLOWLIST)
    if unexpected:
        errors.append(f"unexpected root entries: {unexpected}")

    tracked = git_tracked()
    for path in tracked:
        if path in TRACKED_FORBIDDEN_FILES or path.startswith(TRACKED_FORBIDDEN_PREFIXES):
            errors.append(f"competing tracked registry/artifact: {path}")
        if re.search(r"(^|/)(access\\.env|oracle-vm-rsa|.*secret.*|.*token.*)$", path, re.I):
            errors.append(f"tracked secret-like path: {path}")

    allowed_md = {"ai/MEGAVAULT_PROTOCOL.md", "ai/GLOBAL_INDEX.md", "legacy/README.md"}
    tracked_md = {path for path in tracked if path.endswith(".md")}
    extra_md = sorted(tracked_md - allowed_md)
    if extra_md:
        errors.append(f"extra tracked markdown: {extra_md}")

    errors.extend(protocol_semantic_errors())
    errors.extend(secret_scan_errors(tracked))

    print_errors(errors)
    if errors:
        return 1

    counts = {
        table: conn.execute(f"select count(*) from {table}").fetchone()[0]
        for table in (
            "projects",
            "project_aliases",
            "repositories",
            "hosts",
            "integrations",
            "services",
            "secret_refs",
            "data_assets",
            "incidents",
            "events",
        )
    }
    print("VALIDATE=PASS " + " ".join(f"{key}={value}" for key, value in counts.items()))
    return 0


def print_errors(errors: list[str]) -> None:
    for error in errors:
        print(f"VALIDATE=FAIL {error}", file=sys.stderr)


def project(alias: str) -> int:
    conn = connect()
    row = conn.execute(
        """
        select p.project_id, p.slug, p.name, p.status, p.archived
        from project_aliases a
        join projects p on p.project_id=a.project_id
        where a.alias=?
        """,
        (alias,),
    ).fetchone()
    if not row:
        print(f"PROJECT=NOT_FOUND alias={alias}", file=sys.stderr)
        return 1
    repo_rows = conn.execute(
        "select location, kind, branch, head, status from repositories where project_id=? order by canonical desc, repository_id",
        (row[0],),
    ).fetchall()
    print(f"project_id={row[0]}")
    print(f"slug={row[1]}")
    print(f"name={row[2]}")
    print(f"status={row[3]}")
    print(f"archived={row[4]}")
    for location, kind, branch, head, status in repo_rows:
        print(f"repo={location};kind={kind};branch={branch or ''};head={head or ''};status={status or ''}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("validate")
    project_parser = sub.add_parser("project")
    project_parser.add_argument("alias")
    args = parser.parse_args(argv)
    if args.cmd == "validate":
        return validate()
    if args.cmd == "project":
        return project(args.alias)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
