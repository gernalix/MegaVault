#!/usr/bin/env python3
"""Deterministic semantic lint for the canonical MegaVault protocol."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PROTOCOL = ROOT / "ai" / "MEGAVAULT_PROTOCOL.md"
SEMANTIC_MAP = ROOT / "ai" / "V17_PROTOCOL_SEMANTIC_MAP.json"
KEY_RE = re.compile(r"[A-Z][A-Z0-9_]*")


def parse_protocol(raw: str) -> tuple[dict[str, str], list[str]]:
    pairs: dict[str, str] = {}
    errors: list[str] = []
    keys: list[str] = []
    for number, line in enumerate(raw.splitlines(), 1):
        if not line:
            errors.append(f"line_{number}:blank_line")
            continue
        if line.startswith("#") or "=" not in line:
            errors.append(f"line_{number}:not_key_value")
            continue
        key, value = line.split("=", 1)
        keys.append(key)
        if not KEY_RE.fullmatch(key):
            errors.append(f"line_{number}:naming_inconsistency:{key}")
        if not value:
            errors.append(f"line_{number}:missing_value:{key}")
        pairs[key] = value
    for key, count in Counter(keys).items():
        if count > 1:
            errors.append(f"duplicate_key:{key}:{count}")
    return pairs, errors


def metrics(raw: str) -> dict[str, int | str]:
    encoded = raw.encode("utf-8")
    return {
        "lines": len(raw.splitlines()),
        "words": len(raw.split()),
        "bytes": len(encoded),
        "estimated_tokens": (len(encoded) + 3) // 4,
        "token_estimator": "ceil_utf8_bytes_div_4",
    }


def git_output(*args: str, binary: bool = False) -> str | bytes:
    return subprocess.run(
        ["git", *args], cwd=ROOT, check=True, capture_output=True, text=not binary
    ).stdout


def lint() -> dict[str, object]:
    raw = PROTOCOL.read_text(encoding="utf-8")
    pairs, errors = parse_protocol(raw)
    manifest = json.loads(SEMANTIC_MAP.read_text(encoding="utf-8"))

    required = {
        "VERSION": "17",
        "FORMAT": "ultracompressed_key_value",
        "LANG": "key_value",
        "LINE_RULE": "1_line=1_fact",
        "EXECUTION_INSIGHTS": "mandatory",
        "OPTIMIZATION_OPPORTUNITIES": "mandatory_final_report_section",
        "PROTOCOL_LINT": "mandatory",
        "GLOBAL_GIT_MODEL": "trunk_based_single_developer",
        "GIT_POLICY_SCOPE": "all_projects,all_repositories,past_present_future",
        "OPERATIVE_BRANCH_COUNT": "1",
        "DEFAULT_WORK_BRANCH": "canonical_branch",
        "DIRECT_CANONICAL_WORK": "default",
        "NEW_BRANCH_DEFAULT": "forbidden",
        "NEW_BRANCH_PER_TASK": "forbidden",
        "BRANCH_CHAINING": "forbidden",
        "TEMP_BRANCH_FINALIZATION": "integrate_into_canonical+delete",
        "CANONICAL_SYNC_REQUIRED": "yes",
    }
    for key, expected in required.items():
        if pairs.get(key) != expected:
            errors.append(f"required_field:{key}:expected={expected}:actual={pairs.get(key)}")

    if pairs.get("AI_SOURCE") == "authoritative" and pairs.get("HUMAN_SOURCE") == "authoritative":
        errors.append("contradiction:ai_and_human_both_authoritative")
    if pairs.get("GLOBAL_GIT_MODEL") == "trunk_based_single_developer" and pairs.get("OPERATIVE_BRANCH_COUNT") != "1":
        errors.append("contradiction:single_trunk_without_one_operative_branch")
    if pairs.get("NEW_BRANCH_DEFAULT") == "forbidden" and pairs.get("TEMP_BRANCH") != "exception":
        errors.append("contradiction:temporary_branch_not_exception")
    if pairs.get("TEMP_BRANCH") == "exception" and not pairs.get("TEMP_BRANCH_ALLOWED_IF"):
        errors.append("unreachable_rule:temporary_branch_missing_conditions")
    if pairs.get("GLOBAL_TIMELINE") == "mandatory_all_codex_tasks" and pairs.get("TIMELINE_FINAL_GATE") != "run_before_final_response":
        errors.append("unreachable_rule:timeline_mandate_without_final_gate")
    if any(re.fullmatch(r"P\d+", key) for key in pairs):
        errors.append("naming_inconsistency:opaque_P_key")

    referenced_files = {
        pairs.get("CANONICAL_GENERAL"),
        pairs.get("CANONICAL_ANDROID"),
        pairs.get("CANONICAL_HOST"),
        pairs.get("CANONICAL_SERVICE"),
        pairs.get("CANONICAL_DATA"),
        pairs.get("CANONICAL_NETWORK"),
        pairs.get("CANONICAL_STORAGE"),
        pairs.get("CANONICAL_ALERT"),
        pairs.get("CANONICAL_INCIDENT"),
        pairs.get("HOST_PROFILE_PATH"),
        pairs.get("ANDROID_PROTOCOL"),
        pairs.get("PROTOCOL_SEMANTIC_MAP"),
        pairs.get("PROTOCOL_LINT_TOOL"),
        pairs.get("TIMELINE_SCRIPT"),
    }
    for value in sorted(item for item in referenced_files if item):
        path_text = value.split(";", 1)[0]
        target = ROOT / path_text
        if not target.exists():
            errors.append(f"unreachable_rule:missing_reference:{path_text}")

    baseline_ref = manifest["baseline_ref"]
    baseline_path = manifest["baseline_path"]
    try:
        baseline_raw = git_output("show", f"{baseline_ref}:{baseline_path}")
        baseline_blob = git_output("rev-parse", f"{baseline_ref}:{baseline_path}").strip()
    except subprocess.CalledProcessError as exc:
        errors.append(f"semantic_coverage:baseline_unavailable:{exc.returncode}")
        baseline_raw = ""
        baseline_blob = ""
    baseline_sha256 = hashlib.sha256(baseline_raw.encode("utf-8")).hexdigest()
    if baseline_blob != manifest["baseline_git_blob"]:
        errors.append("semantic_coverage:baseline_git_blob_mismatch")
    if baseline_sha256 != manifest["baseline_sha256"]:
        errors.append("semantic_coverage:baseline_sha256_mismatch")
    if manifest["baseline_metrics"] != metrics(baseline_raw):
        errors.append("semantic_coverage:baseline_metrics_mismatch")

    baseline_pairs, baseline_errors = parse_protocol(baseline_raw)
    if any(item.startswith("duplicate_key") for item in baseline_errors):
        errors.append("semantic_coverage:baseline_duplicate_keys")
    transformations = manifest["transformations"]
    covered: list[str] = []
    for key, value in baseline_pairs.items():
        if pairs.get(key) == value:
            covered.append(key)
            continue
        item = transformations.get(key)
        if not item:
            errors.append(f"semantic_coverage:missing:{key}")
            continue
        replacements = item.get("replacement_keys", [])
        if not replacements or any(replacement not in pairs for replacement in replacements):
            errors.append(f"semantic_coverage:bad_replacement:{key}")
            continue
        if not item.get("reason"):
            errors.append(f"semantic_coverage:missing_reason:{key}")
            continue
        covered.append(key)
    for key in transformations:
        if key not in baseline_pairs:
            errors.append(f"semantic_coverage:unknown_baseline_key:{key}")

    before = metrics(baseline_raw)
    after = metrics(raw)
    for field in ("lines", "words", "bytes", "estimated_tokens"):
        if int(after[field]) >= int(before[field]):
            errors.append(f"compression:{field}:not_reduced")

    expected_insight_fields = "root_cause,impact,estimated_future_savings,one_time_fix,priority,confidence,status"
    if pairs.get("INSIGHT_ITEM_FIELDS") != expected_insight_fields:
        errors.append("missing_required_fields:insight_item_fields")
    if pairs.get("OPTIMIZATION_ITEM_FIELDS") != expected_insight_fields:
        errors.append("missing_required_fields:optimization_item_fields")
    required_scopes = {"token", "time", "reasoning", "IO", "scans", "documentation", "metadata", "indexing", "caching", "tooling", "automation", "prompt", "architecture"}
    if set(pairs.get("OPTIMIZATION_SCOPE", "").split(",")) != required_scopes:
        errors.append("missing_required_fields:optimization_scope")

    return {
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "semantic_coverage": {
            "covered": len(set(covered)),
            "required": len(baseline_pairs),
            "percent": round(100 * len(set(covered)) / len(baseline_pairs), 2) if baseline_pairs else 0,
        },
        "metrics": {"before": before, "after": after},
        "checks": list(pairs.get("PROTOCOL_LINT_CHECKS", "").split(",")),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = lint()
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(f"protocol_lint={result['status']}")
        print(f"semantic_coverage={result['semantic_coverage']['covered']}/{result['semantic_coverage']['required']}")
        print(f"metrics={json.dumps(result['metrics'], sort_keys=True)}")
        for error in result["errors"]:
            print(f"error={error}")
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
