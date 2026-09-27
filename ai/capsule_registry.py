#!/usr/bin/env python3
"""Project-capsule inventory, discovery, and deterministic verification."""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import os
import shutil
import sqlite3
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


EXCLUSION_REASONS = {
    "obsolete",
    "generated",
    "vendor",
    "mirror",
    "throwaway",
    "fully_absorbed",
}
CRITERION_STATES = {
    "pass",
    "fail",
    "unverified",
    "not_applicable",
    "not_evaluated",
}
ARTIFACT_CANDIDATES = {
    "manifest": ("project-capsule.yaml", "project-capsule.yml", "project-capsule.json"),
    "agents": ("AGENTS.md",),
    "architecture": ("architecture.md", "docs/architecture.md"),
    "operations": ("operations.md", "docs/operations.md"),
    "data_model": ("data-model.md", "docs/data-model.md"),
}


def _table_exists(conn: sqlite3.Connection, name: str) -> bool:
    return conn.execute(
        "select 1 from sqlite_master where type in ('table','view') and name=?", (name,)
    ).fetchone() is not None


def ensure_schema(conn: sqlite3.Connection) -> bool:
    """Create capsule metadata without duplicating project/repository identity."""
    existed = _table_exists(conn, "capsule_repository_policy")
    schema_sql = """
        CREATE TABLE IF NOT EXISTS capsule_repository_policy (
          repository_id TEXT PRIMARY KEY
            REFERENCES repositories(repository_id) ON UPDATE CASCADE ON DELETE CASCADE,
          coverage_state TEXT NOT NULL CHECK(coverage_state IN ('eligible','excluded')),
          exclusion_reason TEXT CHECK(exclusion_reason IN (
            'obsolete','generated','vendor','mirror','throwaway','fully_absorbed'
          )),
          source TEXT NOT NULL,
          updated_at_utc TEXT NOT NULL,
          CHECK(
            (coverage_state='eligible' AND exclusion_reason IS NULL) OR
            (coverage_state='excluded' AND exclusion_reason IS NOT NULL)
          )
        );

        CREATE TABLE IF NOT EXISTS capsule_registry (
          repository_id TEXT PRIMARY KEY
            REFERENCES repositories(repository_id) ON UPDATE CASCADE ON DELETE CASCADE,
          manifest_path TEXT,
          standard_ref TEXT,
          source_ref TEXT,
          source_sha256 TEXT,
          source_timestamp_utc TEXT,
          repository_head TEXT,
          discovery_state TEXT NOT NULL CHECK(discovery_state IN (
            'not_scanned','absent','present','invalid','unavailable'
          )),
          verification_state TEXT NOT NULL CHECK(verification_state IN (
            'pass','fail','unverified','not_applicable','not_evaluated'
          )),
          checked_mode TEXT CHECK(checked_mode IN ('FAST','FULL')),
          checked_at_utc TEXT
        );

        CREATE TABLE IF NOT EXISTS capsule_artifact_status (
          repository_id TEXT NOT NULL
            REFERENCES repositories(repository_id) ON UPDATE CASCADE ON DELETE CASCADE,
          artifact_key TEXT NOT NULL,
          artifact_path TEXT,
          presence_state TEXT NOT NULL CHECK(presence_state IN (
            'present','absent','unavailable'
          )),
          verification_state TEXT NOT NULL CHECK(verification_state IN (
            'pass','fail','unverified','not_applicable','not_evaluated'
          )),
          source_sha256 TEXT,
          source_timestamp_utc TEXT,
          checked_at_utc TEXT NOT NULL,
          PRIMARY KEY(repository_id, artifact_key)
        );

        CREATE TABLE IF NOT EXISTS capsule_criterion_status (
          repository_id TEXT NOT NULL
            REFERENCES repositories(repository_id) ON UPDATE CASCADE ON DELETE CASCADE,
          criterion_id TEXT NOT NULL,
          state TEXT NOT NULL CHECK(state IN (
            'pass','fail','unverified','not_applicable','not_evaluated'
          )),
          mode TEXT NOT NULL CHECK(mode IN ('FAST','FULL')),
          evidence_json TEXT NOT NULL CHECK(json_valid(evidence_json)),
          checked_at_utc TEXT NOT NULL,
          PRIMARY KEY(repository_id, criterion_id)
        );

        CREATE INDEX IF NOT EXISTS idx_capsule_policy_state
          ON capsule_repository_policy(coverage_state, exclusion_reason, repository_id);
        CREATE INDEX IF NOT EXISTS idx_capsule_criteria_state
          ON capsule_criterion_status(state, criterion_id, repository_id);
        """
    for statement in schema_sql.split(";"):
        if statement.strip():
            conn.execute(statement)
    conn.execute("DROP VIEW IF EXISTS capsule_inventory")
    conn.execute(
        """
        CREATE VIEW capsule_inventory AS
        SELECT
          p.project_id,
          p.slug AS project_slug,
          r.repository_id,
          r.repository_kind,
          r.canonical,
          r.worktree_path,
          r.remote_url,
          r.runtime_path,
          CASE
            WHEN policy.repository_id IS NOT NULL THEN policy.coverage_state
            WHEN p.archived=1 OR r.repository_kind='legacy' THEN 'excluded'
            WHEN r.canonical=0 THEN 'excluded'
            ELSE 'eligible'
          END AS coverage_state,
          CASE
            WHEN policy.repository_id IS NOT NULL THEN policy.exclusion_reason
            WHEN p.archived=1 THEN 'obsolete'
            WHEN r.canonical=0 AND EXISTS (
              SELECT 1 FROM repositories sibling
              WHERE sibling.project_id=r.project_id
                AND sibling.repository_id<>r.repository_id
                AND sibling.canonical=1
            ) THEN 'fully_absorbed'
            WHEN r.repository_kind='legacy' THEN 'obsolete'
            WHEN r.canonical=0 THEN 'mirror'
            ELSE NULL
          END AS exclusion_reason,
          CASE
            WHEN policy.repository_id IS NOT NULL THEN policy.source
            ELSE 'derived_from_canonical_registry'
          END AS policy_source,
          registry.discovery_state,
          registry.verification_state,
          registry.checked_mode,
          registry.checked_at_utc
        FROM repositories r
        JOIN projects p ON p.project_id=r.project_id
        LEFT JOIN capsule_repository_policy policy
          ON policy.repository_id=r.repository_id
        LEFT JOIN capsule_registry registry
          ON registry.repository_id=r.repository_id
        """
    )
    return not existed


def schema_errors(conn: sqlite3.Connection) -> list[str]:
    errors: list[str] = []
    required = {
        "capsule_repository_policy",
        "capsule_registry",
        "capsule_artifact_status",
        "capsule_criterion_status",
        "capsule_inventory",
    }
    missing = sorted(name for name in required if not _table_exists(conn, name))
    if missing:
        return [f"missing capsule tables/views: {missing!r}"]
    invalid = conn.execute(
        """
        select repository_id, coverage_state, exclusion_reason
        from capsule_inventory
        where coverage_state not in ('eligible','excluded')
           or (coverage_state='eligible' and exclusion_reason is not null)
           or (coverage_state='excluded' and exclusion_reason not in (
             'obsolete','generated','vendor','mirror','throwaway','fully_absorbed'
           ))
        order by repository_id
        """
    ).fetchall()
    if invalid:
        errors.append(f"capsule inventory invalid rows: {invalid!r}")
    repository_count = conn.execute("select count(*) from repositories").fetchone()[0]
    inventory_count = conn.execute("select count(*) from capsule_inventory").fetchone()[0]
    if repository_count != inventory_count:
        errors.append(
            f"capsule inventory row count mismatch: repositories={repository_count} inventory={inventory_count}"
        )
    return errors


def _utc_from_mtime(path: Path) -> str:
    return datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat()


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _git(repo: Path, *args: str) -> str | None:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.stdout.strip() if result.returncode == 0 else None


def _repo_path(row: sqlite3.Row | dict[str, Any]) -> Path | None:
    for key in ("worktree_path", "runtime_path"):
        value = row[key]
        if value and Path(value).is_absolute():
            return Path(value)
    return None


def _load_document(path: Path) -> dict[str, Any]:
    raw = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        value = json.loads(raw)
    else:
        try:
            import yaml  # type: ignore
        except ImportError as exc:
            raise ValueError("YAML manifest requires PyYAML; JSON remains supported") from exc
        value = yaml.safe_load(raw)
    if not isinstance(value, dict):
        raise ValueError("document root must be an object")
    return value


def _candidate_map(standard: dict[str, Any] | None) -> dict[str, tuple[str, ...]]:
    result = dict(ARTIFACT_CANDIDATES)
    if not standard:
        return result
    declared = standard.get("artifacts", {})
    if not isinstance(declared, dict):
        raise ValueError("standard.artifacts must be an object")
    for key, paths in declared.items():
        if isinstance(paths, str):
            paths = [paths]
        if not isinstance(paths, list) or not all(isinstance(item, str) for item in paths):
            raise ValueError(f"standard.artifacts.{key} must be a string or string list")
        result[str(key)] = tuple(paths)
    return result


def discover_artifacts(
    repo: Path, standard: dict[str, Any] | None = None
) -> dict[str, dict[str, Any]]:
    discovered: dict[str, dict[str, Any]] = {}
    for key, candidates in sorted(_candidate_map(standard).items()):
        selected: Path | None = None
        for relative in candidates:
            candidate = repo / relative
            try:
                candidate.resolve().relative_to(repo.resolve())
            except ValueError:
                continue
            if candidate.is_file():
                selected = candidate
                break
        if selected is None:
            discovered[key] = {
                "path": None,
                "presence_state": "absent",
                "verification_state": "not_evaluated",
            }
        else:
            discovered[key] = {
                "path": str(selected.relative_to(repo)),
                "presence_state": "present",
                "verification_state": "unverified",
                "source_sha256": _sha256(selected),
                "source_timestamp_utc": _utc_from_mtime(selected),
            }
    return discovered


def _normalize_argv(value: Any, label: str) -> list[str]:
    if not isinstance(value, list) or not value or not all(isinstance(item, str) and item for item in value):
        raise ValueError(f"{label}.argv must be a non-empty string list")
    return value


def validate_manifest(manifest: dict[str, Any], repo: Path) -> tuple[list[dict[str, Any]], list[str]]:
    criteria: list[dict[str, Any]] = []
    gaps: list[str] = []
    hooks = manifest.get("validation_hooks", [])
    if not isinstance(hooks, list):
        return [], ["manifest_schema_invalid:validation_hooks_must_be_list"]
    hook_ids: set[str] = set()
    declared_artifacts = manifest.get("artifacts", {})
    if not isinstance(declared_artifacts, dict):
        gaps.append("manifest_schema_invalid:artifacts_must_be_object")
    else:
        for key, relative in sorted(declared_artifacts.items()):
            criterion_id = f"declared_path:{key}"
            try:
                if not isinstance(relative, str) or not relative:
                    raise ValueError("artifact path must be a non-empty string")
                target = (repo / relative).resolve()
                target.relative_to(repo.resolve())
                if not target.exists():
                    raise ValueError("declared artifact path does not exist")
                criteria.append(
                    {"criterion_id": criterion_id, "state": "pass", "evidence": {"path": relative}}
                )
            except ValueError as exc:
                criteria.append(
                    {"criterion_id": criterion_id, "state": "fail", "evidence": {"error": str(exc)}}
                )
                gaps.append(f"declared_path_invalid:{key}")
    for index, hook in enumerate(hooks):
        criterion_id = f"declared_hook:{index}"
        evidence: dict[str, Any] = {}
        try:
            if not isinstance(hook, dict):
                raise ValueError("hook must be an object")
            hook_id = hook.get("id")
            if not isinstance(hook_id, str) or not hook_id or hook_id in hook_ids:
                raise ValueError("hook.id must be a unique non-empty string")
            hook_ids.add(hook_id)
            argv = _normalize_argv(hook.get("argv"), f"validation_hooks[{index}]")
            cwd = repo / str(hook.get("cwd", "."))
            cwd.resolve().relative_to(repo.resolve())
            if not cwd.is_dir():
                raise ValueError("hook.cwd does not exist")
            executable = argv[0]
            executable_ok = bool(shutil.which(executable))
            if "/" in executable:
                executable_ok = (cwd / executable).is_file()
            if not executable_ok:
                raise ValueError("hook executable is unavailable")
            if hook.get("safe") not in (True, False):
                raise ValueError("hook.safe must be boolean")
            evidence = {"hook_id": hook_id, "argv": argv, "cwd": str(cwd.relative_to(repo)), "safe": hook["safe"]}
            state = "pass"
        except (KeyError, TypeError, ValueError) as exc:
            evidence = {"error": str(exc)}
            state = "fail"
            gaps.append(f"declared_command_invalid:{index}")
        criteria.append({"criterion_id": criterion_id, "state": state, "evidence": evidence})
    mappings = manifest.get("change_verification", [])
    if not isinstance(mappings, list):
        gaps.append("manifest_schema_invalid:change_verification_must_be_list")
    return criteria, gaps


def _standard_criteria(
    standard: dict[str, Any] | None,
    artifacts: dict[str, dict[str, Any]],
    manifest: dict[str, Any] | None,
    mode: str,
) -> tuple[list[dict[str, Any]], list[str]]:
    """Evaluate declarative criteria; unknown checks remain explicit, never guessed."""
    if not standard:
        return [], []
    definitions = standard.get("criteria", [])
    if not isinstance(definitions, list):
        return [], ["standard_schema_invalid:criteria_must_be_list"]
    rows: list[dict[str, Any]] = []
    gaps: list[str] = []
    seen: set[str] = set()
    for index, definition in enumerate(definitions):
        if not isinstance(definition, dict):
            gaps.append(f"standard_criterion_invalid:{index}")
            continue
        criterion_id = definition.get("id")
        if not isinstance(criterion_id, str) or not criterion_id or criterion_id in seen:
            gaps.append(f"standard_criterion_invalid:{index}")
            continue
        seen.add(criterion_id)
        modes = definition.get("modes", ["FAST", "FULL"])
        if mode not in modes:
            rows.append({"criterion_id": criterion_id, "state": "not_evaluated", "evidence": {"mode": mode}})
            continue
        evidence: dict[str, Any] = {}
        if isinstance(definition.get("artifact"), str):
            artifact_key = definition["artifact"]
            artifact = artifacts.get(artifact_key)
            evidence = {"artifact": artifact_key}
            if artifact is None or artifact["presence_state"] == "absent":
                state = "fail"
            else:
                state = artifact["verification_state"]
        elif isinstance(definition.get("manifest_field"), str):
            parts = definition["manifest_field"].split(".")
            value: Any = manifest
            for part in parts:
                value = value.get(part) if isinstance(value, dict) else None
            evidence = {"manifest_field": definition["manifest_field"], "present": value is not None}
            state = "pass" if value is not None else "fail"
        else:
            state = "not_evaluated"
            evidence = {"reason": "unsupported_declarative_check"}
        if state in {"fail", "unverified", "not_evaluated"}:
            gaps.append(f"criterion_{state}:{criterion_id}")
        rows.append({"criterion_id": criterion_id, "state": state, "evidence": evidence})
    return rows, gaps


def _changed_file_verification(
    manifest: dict[str, Any], changed_files: list[str]
) -> tuple[list[dict[str, Any]], list[str]]:
    mappings = manifest.get("change_verification", [])
    if not isinstance(mappings, list):
        return [], ["change_verification_invalid"] if changed_files else []
    rows: list[dict[str, Any]] = []
    gaps: list[str] = []
    for changed in sorted(set(changed_files)):
        commands: list[Any] = []
        for mapping in mappings:
            if not isinstance(mapping, dict):
                continue
            patterns = mapping.get("paths", [])
            if isinstance(patterns, str):
                patterns = [patterns]
            if isinstance(patterns, list) and any(
                isinstance(pattern, str) and fnmatch.fnmatchcase(changed, pattern)
                for pattern in patterns
            ):
                declared = mapping.get("commands", [])
                if isinstance(declared, list):
                    commands.extend(declared)
        if commands:
            rows.append({"changed_file": changed, "commands": commands, "state": "pass"})
        else:
            rows.append({"changed_file": changed, "commands": [], "state": "fail"})
            gaps.append(f"change_verification_mapping_missing:{changed}")
    return rows, gaps


def _run_full_hooks(
    manifest: dict[str, Any], repo: Path, timeout: int
) -> tuple[list[dict[str, Any]], list[str]]:
    results: list[dict[str, Any]] = []
    gaps: list[str] = []
    for hook in manifest.get("validation_hooks", []):
        if not isinstance(hook, dict) or hook.get("safe") is not True:
            continue
        try:
            argv = _normalize_argv(hook.get("argv"), "validation_hook")
            cwd = (repo / str(hook.get("cwd", "."))).resolve()
            cwd.relative_to(repo.resolve())
            completed = subprocess.run(
                argv,
                cwd=cwd,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=timeout,
                check=False,
                env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
            )
            state = "pass" if completed.returncode == 0 else "fail"
            row = {
                "criterion_id": f"validation_hook:{hook.get('id', '')}",
                "state": state,
                "evidence": {"returncode": completed.returncode},
            }
            if state == "fail":
                gaps.append(f"validation_hook_failed:{hook.get('id', '')}")
        except (OSError, subprocess.TimeoutExpired, ValueError) as exc:
            row = {
                "criterion_id": f"validation_hook:{hook.get('id', '')}",
                "state": "fail",
                "evidence": {"error": type(exc).__name__},
            }
            gaps.append(f"validation_hook_failed:{hook.get('id', '')}")
        results.append(row)
    return results, gaps


def check_repository(
    row: sqlite3.Row,
    *,
    mode: str = "FAST",
    standard: dict[str, Any] | None = None,
    standard_ref: str | None = None,
    changed_files: list[str] | None = None,
    timeout: int = 300,
) -> dict[str, Any]:
    mode = mode.upper()
    if mode not in {"FAST", "FULL"}:
        raise ValueError("mode must be FAST or FULL")
    report: dict[str, Any] = {
        "project_id": row["project_id"],
        "project_slug": row["project_slug"],
        "repository_id": row["repository_id"],
        "coverage_state": row["coverage_state"],
        "exclusion_reason": row["exclusion_reason"],
        "mode": mode,
        "standard_ref": standard_ref,
        "artifacts": {},
        "criteria": [],
        "changed_file_verification": [],
        "freshness": {},
        "gaps": [],
    }
    if row["coverage_state"] == "excluded":
        report["criteria"].append(
            {"criterion_id": "coverage", "state": "not_applicable", "evidence": {"reason": row["exclusion_reason"]}}
        )
        return report
    repo = _repo_path(row)
    if repo is None or not repo.is_dir():
        report["criteria"].append(
            {"criterion_id": "repository_available", "state": "fail", "evidence": {}}
        )
        report["gaps"].append("repository_unavailable")
        return report
    report["freshness"] = {
        "repository_head": _git(repo, "rev-parse", "HEAD"),
        "repository_dirty": bool(_git(repo, "status", "--porcelain")),
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
    }
    artifacts = discover_artifacts(repo, standard)
    report["artifacts"] = artifacts
    for key, artifact in artifacts.items():
        if artifact["presence_state"] == "absent":
            report["gaps"].append(f"artifact_missing:{key}")
            report["criteria"].append(
                {"criterion_id": f"artifact:{key}", "state": "fail", "evidence": {"presence_state": "absent"}}
            )
        else:
            report["criteria"].append(
                {"criterion_id": f"artifact:{key}", "state": "unverified", "evidence": {"path": artifact["path"]}}
            )
    manifest_entry = artifacts.get("manifest", {})
    manifest: dict[str, Any] | None = None
    if manifest_entry.get("presence_state") == "present":
        manifest_path = repo / str(manifest_entry["path"])
        report["freshness"].update(
            {
                "capsule_source_ref": str(manifest_entry["path"]),
                "capsule_source_sha256": manifest_entry["source_sha256"],
                "capsule_source_timestamp_utc": manifest_entry["source_timestamp_utc"],
            }
        )
        try:
            manifest = _load_document(manifest_path)
            manifest_criteria, manifest_gaps = validate_manifest(manifest, repo)
            report["criteria"].extend(manifest_criteria)
            report["gaps"].extend(manifest_gaps)
            for criterion in report["criteria"]:
                if criterion["criterion_id"] == "artifact:manifest":
                    criterion["state"] = "pass" if not manifest_gaps else "fail"
                    manifest_entry["verification_state"] = criterion["state"]
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            report["gaps"].append("manifest_invalid")
            manifest_entry["verification_state"] = "fail"
            report["criteria"].append(
                {"criterion_id": "manifest_schema", "state": "fail", "evidence": {"error": str(exc)}}
            )
    if manifest is not None:
        mappings, mapping_gaps = _changed_file_verification(manifest, changed_files or [])
        report["changed_file_verification"] = mappings
        report["gaps"].extend(mapping_gaps)
        if changed_files and not manifest.get("change_verification"):
            report["gaps"].append("change_verification_mapping_missing")
        if mode == "FULL":
            full_criteria, full_gaps = _run_full_hooks(manifest, repo, timeout)
            report["criteria"].extend(full_criteria)
            report["gaps"].extend(full_gaps)
    elif changed_files:
        report["gaps"].append("change_verification_mapping_missing")
    standard_criteria, standard_gaps = _standard_criteria(
        standard, artifacts, manifest, mode
    )
    report["criteria"].extend(standard_criteria)
    report["gaps"].extend(standard_gaps)
    report["gaps"] = sorted(set(report["gaps"]))
    return report


def inventory_rows(conn: sqlite3.Connection, repository_id: str | None = None) -> list[sqlite3.Row]:
    conn.row_factory = sqlite3.Row
    sql = "select * from capsule_inventory"
    params: tuple[Any, ...] = ()
    if repository_id:
        sql += " where repository_id=?"
        params = (repository_id,)
    sql += " order by project_id, repository_id"
    return conn.execute(sql, params).fetchall()


def aggregate_report(
    conn: sqlite3.Connection,
    *,
    mode: str = "FAST",
    standard: dict[str, Any] | None = None,
    standard_ref: str | None = None,
    scan: bool = False,
) -> dict[str, Any]:
    rows = inventory_rows(conn)
    items: list[dict[str, Any]] = []
    gap_categories: set[str] = set()
    for row in rows:
        if scan and row["coverage_state"] == "eligible":
            item = check_repository(row, mode=mode, standard=standard, standard_ref=standard_ref)
            item["gap_categories"] = sorted({gap.split(":", 1)[0] for gap in item["gaps"]})
            gap_categories.update(item["gap_categories"])
        else:
            item = {
                "project_id": row["project_id"],
                "project_slug": row["project_slug"],
                "repository_id": row["repository_id"],
                "coverage_state": row["coverage_state"],
                "exclusion_reason": row["exclusion_reason"],
                "discovery_state": row["discovery_state"] or "not_scanned",
                "verification_state": row["verification_state"] or "not_evaluated",
                "mode": mode.upper(),
                "standard_ref": standard_ref,
                "artifacts": {},
                "criteria": [
                    {
                        "criterion_id": "coverage",
                        "state": "not_applicable",
                        "evidence": {"reason": row["exclusion_reason"]},
                    }
                ],
                "freshness": {},
                "gaps": [],
                "gap_categories": [],
            }
        items.append(item)
    eligible = sum(item["coverage_state"] == "eligible" for item in items)
    excluded = len(items) - eligible
    rollout = [
        {
            "project_id": item["project_id"],
            "repository_id": item["repository_id"],
            "project_slug": item["project_slug"],
            "gap_categories": item.get("gap_categories", []),
        }
        for item in items
        if item["coverage_state"] == "eligible" and item.get("gaps")
    ]
    return {
        "schema": "megavault.capsule-inventory.v1",
        "mode": mode.upper(),
        "standard_ref": standard_ref,
        "eligible_count": eligible,
        "excluded_count": excluded,
        "gap_categories": sorted(gap_categories),
        "repositories": items,
        "child_rollout_repositories": rollout,
    }


def record_reports(conn: sqlite3.Connection, reports: list[dict[str, Any]]) -> None:
    """Persist discovered status while keeping project/repository identity external."""
    for report in reports:
        repository_id = report["repository_id"]
        checked_at = report.get("freshness", {}).get("checked_at_utc") or datetime.now(
            timezone.utc
        ).isoformat()
        gaps = set(report.get("gaps", []))
        artifacts = report.get("artifacts", {})
        manifest = artifacts.get("manifest", {})
        if report["coverage_state"] == "excluded":
            discovery_state = "not_scanned"
            verification_state = "not_applicable"
        elif "repository_unavailable" in gaps:
            discovery_state = "unavailable"
            verification_state = "fail"
        elif manifest.get("presence_state") != "present":
            discovery_state = "absent"
            verification_state = "fail"
        elif "manifest_invalid" in gaps:
            discovery_state = "invalid"
            verification_state = "fail"
        else:
            discovery_state = "present"
            states = {item["state"] for item in report.get("criteria", [])}
            if "fail" in states:
                verification_state = "fail"
            elif "unverified" in states:
                verification_state = "unverified"
            elif states and states <= {"pass", "not_applicable"}:
                verification_state = "pass"
            else:
                verification_state = "not_evaluated"
        freshness = report.get("freshness", {})
        conn.execute(
            """
            INSERT INTO capsule_registry(
              repository_id, manifest_path, standard_ref, source_ref, source_sha256,
              source_timestamp_utc, repository_head, discovery_state,
              verification_state, checked_mode, checked_at_utc
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(repository_id) DO UPDATE SET
              manifest_path=excluded.manifest_path,
              standard_ref=excluded.standard_ref,
              source_ref=excluded.source_ref,
              source_sha256=excluded.source_sha256,
              source_timestamp_utc=excluded.source_timestamp_utc,
              repository_head=excluded.repository_head,
              discovery_state=excluded.discovery_state,
              verification_state=excluded.verification_state,
              checked_mode=excluded.checked_mode,
              checked_at_utc=excluded.checked_at_utc
            """,
            (
                repository_id,
                manifest.get("path"),
                report.get("standard_ref"),
                freshness.get("capsule_source_ref"),
                freshness.get("capsule_source_sha256"),
                freshness.get("capsule_source_timestamp_utc"),
                freshness.get("repository_head"),
                discovery_state,
                verification_state,
                report["mode"],
                checked_at,
            ),
        )
        conn.execute("delete from capsule_artifact_status where repository_id=?", (repository_id,))
        for key, artifact in sorted(artifacts.items()):
            conn.execute(
                """
                INSERT INTO capsule_artifact_status(
                  repository_id, artifact_key, artifact_path, presence_state,
                  verification_state, source_sha256, source_timestamp_utc, checked_at_utc
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    repository_id,
                    key,
                    artifact.get("path"),
                    artifact["presence_state"],
                    artifact["verification_state"],
                    artifact.get("source_sha256"),
                    artifact.get("source_timestamp_utc"),
                    checked_at,
                ),
            )
        conn.execute("delete from capsule_criterion_status where repository_id=?", (repository_id,))
        criteria_by_id = {
            criterion["criterion_id"]: criterion
            for criterion in report.get("criteria", [])
        }
        for criterion in criteria_by_id.values():
            conn.execute(
                """
                INSERT INTO capsule_criterion_status(
                  repository_id, criterion_id, state, mode, evidence_json, checked_at_utc
                ) VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    repository_id,
                    criterion["criterion_id"],
                    criterion["state"],
                    report["mode"],
                    json.dumps(criterion.get("evidence", {}), sort_keys=True),
                    checked_at,
                ),
            )


def _load_standard(path_text: str | None) -> tuple[dict[str, Any] | None, str | None]:
    if not path_text:
        return None, None
    path = Path(path_text).resolve()
    return _load_document(path), str(path)


def dispatch(argv: list[str], *, db_path: Path) -> int | None:
    if not argv or argv[0] not in {"capsule-inventory", "capsule-check"}:
        return None
    parser = argparse.ArgumentParser(prog=f"megavault.py {argv[0]}")
    parser.add_argument("--mode", choices=("FAST", "FULL"), default="FAST")
    parser.add_argument("--standard", help="JSON/YAML criteria and artifact definition")
    parser.add_argument("--output", help="write the JSON report to this path")
    parser.add_argument("--record", action="store_true", help="persist registry, artifact, and raw criterion states")
    if argv[0] == "capsule-inventory":
        parser.add_argument("--scan", action="store_true", help="discover and FAST/FULL-check eligible repositories")
    else:
        target = parser.add_mutually_exclusive_group(required=True)
        target.add_argument("--repository-id")
        target.add_argument("--project-id", type=int)
        parser.add_argument("--changed-file", action="append", default=[])
        parser.add_argument("--timeout", type=int, default=300)
    args = parser.parse_args(argv[1:])
    standard, standard_ref = _load_standard(args.standard)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        if argv[0] == "capsule-inventory":
            report = aggregate_report(
                conn,
                mode=args.mode,
                standard=standard,
                standard_ref=standard_ref,
                scan=args.scan,
            )
            if args.record:
                if not args.scan:
                    parser.error("--record requires --scan")
                record_reports(conn, report["repositories"])
                conn.commit()
        else:
            rows = inventory_rows(conn, args.repository_id)
            if args.project_id is not None:
                rows = [row for row in inventory_rows(conn) if row["project_id"] == args.project_id]
            if not rows:
                parser.error("no registered repository matched")
            reports = [
                check_repository(
                    row,
                    mode=args.mode,
                    standard=standard,
                    standard_ref=standard_ref,
                    changed_files=args.changed_file,
                    timeout=args.timeout,
                )
                for row in rows
            ]
            report = {
                "schema": "megavault.capsule-project-report.v1",
                "project_id": args.project_id if args.project_id is not None else reports[0]["project_id"],
                "reports": reports,
            }
            if args.record:
                record_reports(conn, reports)
                conn.commit()
        raw = json.dumps(report, sort_keys=True, indent=2) + "\n"
        if args.output:
            Path(args.output).write_text(raw, encoding="utf-8")
        else:
            print(raw, end="")
        return 0
    finally:
        conn.close()
