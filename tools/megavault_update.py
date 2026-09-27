#!/usr/bin/env python3
"""Fail-closed fast-forward updater for the canonical MegaVault checkout."""

from __future__ import annotations

import fcntl
import json
import os
import sqlite3
import subprocess
import sys
from pathlib import Path

CANONICAL_REPO = Path("/home/daniele/MegaVault")
CANONICAL_BRANCH = "master"
LOCK_PATH = Path.home() / ".local" / "state" / "megavault" / "canonical-update.lock"
OPERATION_MARKERS = (
    "MERGE_HEAD",
    "CHERRY_PICK_HEAD",
    "REVERT_HEAD",
    "rebase-merge",
    "rebase-apply",
    "sequencer",
)


class UpdateBlocked(RuntimeError):
    pass


def git(repo: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if check and result.returncode:
        detail = (result.stderr or result.stdout).strip().replace("\n", " ")[:300]
        raise UpdateBlocked(f"git_{args[0]}_failed:{detail}")
    return result


def operation_in_progress(repo: Path) -> str | None:
    for marker in OPERATION_MARKERS:
        location = git(repo, "rev-parse", "--git-path", marker).stdout.strip()
        if location and Path(location).exists():
            return marker
    if git(repo, "ls-files", "-u").stdout:
        return "unmerged-index"
    return None


def validate(repo: Path) -> None:
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    result = subprocess.run(
        [sys.executable, str(repo / "megavault.py"), "validate"],
        cwd=repo,
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode:
        detail = (result.stderr or result.stdout).strip().replace("\n", " ")[:300]
        raise UpdateBlocked(f"validation_failed:{detail}")
    with sqlite3.connect(f"file:{repo / 'megavault.sqlite'}?mode=ro", uri=True) as conn:
        if conn.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
            raise UpdateBlocked("sqlite_integrity_failed")
        if conn.execute("PRAGMA foreign_key_check").fetchall():
            raise UpdateBlocked("sqlite_foreign_keys_failed")


def update(repo: Path, *, expected_repo: Path = CANONICAL_REPO) -> dict[str, str]:
    repo = repo.resolve()
    if repo != expected_repo.resolve():
        raise UpdateBlocked(f"noncanonical_checkout:{repo}")
    if git(repo, "rev-parse", "--is-inside-work-tree").stdout.strip() != "true":
        raise UpdateBlocked("not_git_worktree")
    operation = operation_in_progress(repo)
    if operation:
        raise UpdateBlocked(f"git_operation_in_progress:{operation}")
    branch = git(repo, "branch", "--show-current").stdout.strip()
    if branch != CANONICAL_BRANCH:
        raise UpdateBlocked(f"wrong_branch:{branch or 'detached'}")
    if git(repo, "status", "--porcelain").stdout.strip():
        raise UpdateBlocked("dirty_worktree")

    before = git(repo, "rev-parse", "HEAD").stdout.strip()
    git(
        repo,
        "fetch",
        "--no-tags",
        "origin",
        f"+refs/heads/{CANONICAL_BRANCH}:refs/remotes/origin/{CANONICAL_BRANCH}",
    )
    counts = git(repo, "rev-list", "--left-right", "--count", f"HEAD...origin/{CANONICAL_BRANCH}").stdout.split()
    if len(counts) != 2:
        raise UpdateBlocked("relation_check_failed")
    ahead, behind = map(int, counts)
    if ahead:
        raise UpdateBlocked(f"local_ahead_or_diverged:ahead={ahead}:behind={behind}")
    if behind:
        git(repo, "merge", "--ff-only", f"origin/{CANONICAL_BRANCH}")
    validate(repo)
    if git(repo, "status", "--porcelain").stdout.strip():
        raise UpdateBlocked("post_update_dirty")
    after = git(repo, "rev-parse", "HEAD").stdout.strip()
    remote = git(repo, "rev-parse", f"origin/{CANONICAL_BRANCH}").stdout.strip()
    if after != remote:
        raise UpdateBlocked("post_update_not_synchronized")
    return {"status": "PASS", "before": before, "after": after, "changed": str(before != after).lower()}


def main() -> int:
    LOCK_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOCK_PATH.open("a+", encoding="utf-8") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        try:
            result = update(CANONICAL_REPO)
        except UpdateBlocked as exc:
            print(json.dumps({"status": "BLOCKED", "reason": str(exc)}, sort_keys=True))
            return 2
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
