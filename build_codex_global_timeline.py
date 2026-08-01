#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "codex_global_timeline.sqlite"
REPORT_PATH = BASE_DIR / "codex_global_timeline.md"
AI_REPORT_PATH = BASE_DIR / "codex_global_timeline_ai.md"

VALID_CATEGORIES = {
    "feature",
    "bugfix",
    "performance",
    "release",
    "infra",
    "docs",
    "qa",
    "migration",
    "automation",
    "security",
    "backup",
    "testing",
}
VALID_IMPORTANCE = {"P0", "P1", "P2", "P3"}
VALID_STATUSES = {"PASS", "WARN", "FAIL", "OPEN", "PARTIAL", "UNKNOWN"}

SOURCE_EXTENSIONS = {".md", ".txt", ".json", ".jsonl", ".csv", ".log", ".yml", ".yaml"}
SKIP_DIRS = {
    ".git",
    ".gradle",
    ".idea",
    ".venv",
    "__pycache__",
    "node_modules",
    "build",
    "dist",
    ".dart_tool",
    ".mypy_cache",
    ".pytest_cache",
    ".cache",
    "cache",
    "caches",
    "tmp",
    "temp",
}
SKIP_FILENAMES = {
    "codex_global_timeline.md",
    "codex_global_timeline_ai.md",
    "codex_global_timeline.sqlite",
    "codex_global_timeline.sqlite-shm",
    "codex_global_timeline.sqlite-wal",
}
MAX_SAMPLE_CHARS = 900_000
MAX_SUMMARY_CHARS = 180
MAX_REPORT_SUMMARY_CHARS = 150
DEFAULT_GIT_MAX_COMMITS = 2500
SCHEMA_COLUMNS = (
    "id", "event_date", "discovered_at", "project", "category", "importance",
    "label_short", "event_type", "summary", "source_path", "source_kind",
    "branch", "commit_hash", "artifact_path", "apk_name", "version_name",
    "version_code", "status", "confidence", "notes",
)

SECRET_PATTERNS = [
    re.compile(r"(?i)\bBearer\s+[A-Za-z0-9._~+/=-]{12,}"),
    re.compile(r"(?i)\b(api[_-]?key|token|secret|password|passwd|authorization|chat_id)\s*[:=]\s*['\"]?[^'\"\s,;]{4,}"),
    re.compile(r"AIza[0-9A-Za-z_-]{20,}"),
    re.compile(r"\b\d{6,12}:[A-Za-z0-9_-]{25,}\b"),
    re.compile(r"https://api\.telegram\.org/bot[^\s)\"']+"),
]

PROJECT_LABELS = {
    "multitimetracker": "MTT",
    "multi-time-tracker": "MTT",
    "mtt": "MTT",
    "supercontacts": "SC",
    "soldi": "Soldi",
    "luoghi": "Luoghi",
    "sostanze": "Sostanze",
    "amici-fb": "Amici FB",
    "oracle-backup-service": "Oracle Backup",
    "oracle-uptime-kuma": "Kuma",
    "windows-flight-recorder": "WFR",
    "windows-winget-daily-update": "Winget",
    "megavault": "MegaVault",
    "megavault-2": "MegaVault",
    "mega-vault": "MegaVault",
}


@dataclass(frozen=True)
class Event:
    id: str
    event_date: str
    discovered_at: str
    project: str
    category: str
    importance: str
    label_short: str
    event_type: str
    summary: str
    source_path: str
    source_kind: str
    branch: str
    commit_hash: str
    artifact_path: str
    apk_name: str
    version_name: str
    version_code: str
    status: str
    confidence: float
    notes: str


def stable_timestamp(event_date: str) -> str:
    """Return a content-derived UTC timestamp; never consult the wall clock."""
    return f"{event_date}T00:00:00+00:00"


def ascii_clean(text: str) -> str:
    text = unicodedata.normalize("NFKD", str(text))
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[\x00-\x08\x0b-\x1f\x7f]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def redact(text: str) -> str:
    text = ascii_clean(text)
    for pattern in SECRET_PATTERNS:
        text = pattern.sub(lambda match: redact_match(match), text)
    return text


def redact_match(match: re.Match[str]) -> str:
    value = match.group(0)
    lower = value.lower()
    if lower.startswith("bearer "):
        return "Bearer REDACTED"
    if value.startswith("AIza"):
        return "AIza...REDACTED"
    if "api.telegram.org/bot" in lower:
        return "TELEGRAM_BOT_URL_REDACTED"
    if ":" in value and re.match(r"^\d{6,12}:", value):
        return "TELEGRAM_TOKEN_REDACTED"
    key = value.split("=", 1)[0].split(":", 1)[0]
    return f"{key}=REDACTED"


def truncate(text: str, limit: int) -> str:
    text = redact(text)
    if len(text) <= limit:
        return text
    return text[: max(0, limit - 3)].rstrip() + "..."


def slugify(text: str) -> str:
    text = ascii_clean(text).lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    if len(text) > 80:
        text = text[:80].rstrip("-")
    return text or "unknown"


def display_project(project: str) -> str:
    project = slugify(project)
    return PROJECT_LABELS.get(project, project)


def short_label(raw: str) -> str:
    raw = redact(raw)
    raw = re.sub(r"[|:;,\[\](){}<>]+", " ", raw)
    raw = re.sub(r"\s+", " ", raw).strip(" -_")
    if not raw:
        raw = "Event"
    words = raw.split()
    if len(words) <= 4:
        return " ".join(words)
    filtered = [w for w in words if w.lower() not in {"the", "a", "an", "and", "or", "di", "del", "della", "final", "report"}]
    words = filtered or words
    return " ".join(words[:4])


def read_sample(path: Path) -> str:
    try:
        with path.open("r", encoding="utf-8", errors="replace") as handle:
            return handle.read(MAX_SAMPLE_CHARS)
    except OSError:
        return ""


def extract_date(path: Path, content: str) -> tuple[str, float]:
    haystacks = [path.name, str(path), content[:120_000]]
    for text in haystacks:
        match = re.search(r"\b(20\d{2})[-_/](\d{2})[-_/](\d{2})\b", text)
        if match and valid_date(match.group(1), match.group(2), match.group(3)):
            return f"{match.group(1)}-{match.group(2)}-{match.group(3)}", 0.92
        match = re.search(r"\b(20\d{2})(\d{2})(\d{2})\b", text)
        if match and valid_date(match.group(1), match.group(2), match.group(3)):
            return f"{match.group(1)}-{match.group(2)}-{match.group(3)}", 0.88
    # Git metadata is stable across checkouts; filesystem mtimes are not.
    git_date = run_git(path.parent, ["log", "-1", "--format=%cs", "--", str(path)])
    candidate = git_date.strip()
    if re.fullmatch(r"20\d{2}-\d{2}-\d{2}", candidate):
        return candidate, 0.72
    return "1970-01-01", 0.20


def valid_date(year: str, month: str, day: str) -> bool:
    try:
        datetime(int(year), int(month), int(day))
    except ValueError:
        return False
    return True


def extract_summary(path: Path, content: str) -> str:
    if path.suffix.lower() == ".jsonl":
        jsonl_summary = extract_jsonl_summary(content)
        if jsonl_summary:
            return truncate(jsonl_summary, MAX_SUMMARY_CHARS)

    for line in content.splitlines()[:250]:
        stripped = redact(line).strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            title = stripped.lstrip("#").strip(" -")
            if title:
                return truncate(title, MAX_SUMMARY_CHARS)

    key_pattern = re.compile(r"(?i)^(summary|result|scope|root_cause|cause|status|purpose|feature|fix|release|test|manual_status)\s*[:=]\s*(.+)$")
    for line in content.splitlines()[:350]:
        stripped = redact(line).strip().lstrip("-* ")
        match = key_pattern.match(stripped)
        if match:
            return truncate(match.group(2), MAX_SUMMARY_CHARS)
        if stripped.startswith("- ") and len(stripped) > 20:
            return truncate(stripped.lstrip("- "), MAX_SUMMARY_CHARS)

    stem = path.stem.replace("_", " ").replace("-", " ")
    return truncate(stem, MAX_SUMMARY_CHARS)


def extract_jsonl_summary(content: str) -> str:
    candidates: list[str] = []
    for line in content.splitlines()[:300]:
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        collect_json_strings(obj, candidates)
        if len(candidates) >= 8:
            break
    for value in candidates:
        cleaned = redact(value)
        if 35 <= len(cleaned) <= 600 and not cleaned.startswith("{"):
            return cleaned
    return ""


def collect_json_strings(value: object, out: list[str]) -> None:
    if len(out) >= 12:
        return
    if isinstance(value, dict):
        priority = ["cwd", "objective", "message", "text", "content", "summary", "title"]
        for key in priority:
            if key in value:
                collect_json_strings(value[key], out)
        for key, child in value.items():
            if key not in priority:
                collect_json_strings(child, out)
    elif isinstance(value, list):
        for child in value[:8]:
            collect_json_strings(child, out)
    elif isinstance(value, str):
        if value.strip():
            out.append(value.strip())


def infer_project(path: Path, content: str, root: Path) -> str:
    lower_parts = [part.lower() for part in path.parts]
    for marker in ("projects", "project"):
        if marker in lower_parts:
            idx = lower_parts.index(marker)
            if idx + 1 < len(path.parts):
                candidate = path.parts[idx + 1]
                if path.suffix.lower() == ".md" and idx + 1 == len(path.parts) - 1:
                    candidate = path.stem
                return slugify(candidate)

    cwd_match = re.search(r"C:\\Users\\seste\\Documents\\([^\\\"'\r\n;,)|]+)", content)
    if cwd_match:
        return slugify(cwd_match.group(1))

    text = f"{path} {content[:50_000]}".lower()
    keyword_projects = [
        ("multitimetracker", "multitimetracker"),
        ("multi time tracker", "multitimetracker"),
        ("supercontacts", "supercontacts"),
        ("soldi", "soldi"),
        ("luoghi", "luoghi"),
        ("sostanze", "sostanze"),
        ("oracle-backup", "oracle-backup-service"),
        ("uptime kuma", "oracle-uptime-kuma"),
        ("veeam", "windows"),
        ("tasker", "tasker"),
        ("whatsapp", "pixel-8a"),
        ("windows flight recorder", "windows-flight-recorder"),
        ("winget", "windows-winget-daily-update"),
    ]
    for needle, project in keyword_projects:
        if needle in text:
            return project

    try:
        rel = path.relative_to(root)
        if rel.parts:
            first = rel.parts[0]
            if first.lower() in {"ai", "human", "dev"}:
                return "megavault"
            return slugify(first)
    except ValueError:
        pass
    return slugify(root.name)


def infer_status(content: str) -> str:
    text = content[:120_000].lower()
    if re.search(r"\b(pass|passed|success|successful|exit0|exit=0|rc=0|ok true)\b", text):
        if re.search(r"\b(warn|warning|partial|blocked|degraded)\b", text):
            return "WARN"
        return "PASS"
    if re.search(r"\b(fail|failed|failure|error|critical|blocked)\b", text):
        return "FAIL"
    if re.search(r"\b(warn|warning|partial|degraded)\b", text):
        return "WARN"
    if re.search(r"\b(open|todo|unknown|pending)\b", text):
        return "OPEN"
    return "UNKNOWN"


def infer_category(path: Path, content: str, summary: str) -> str:
    text = f"{path} {summary} {content[:80_000]}".lower()
    category_keywords = [
        ("security", ["secret", "token", "credential", "password", "firewall", "permission", "private key", "api key"]),
        ("backup", ["backup", "veeam", "restic", "rsync", "snapshot", "quota", "t7", "seagate"]),
        ("release", ["release", ".apk", "version", "versioncode", "versionname", "apk"]),
        ("bugfix", ["bug", "fix", "fixed", "root_cause", "cause=", "regression", "failure", "crash"]),
        ("performance", ["performance", "cpu", "memory", "io_pressure", "latency", "jank", "disk usage", "throughput"]),
        ("migration", ["migration", "migrate", "merge", "move_policy", "content_aware"]),
        ("automation", ["automation", "task scheduler", "scheduledtask", "timer", "service", "monitor", "healthcheck"]),
        ("testing", ["test", "unit", "instrument", "adb", "emulator", "qa", "pass/warn/fail"]),
        ("infra", ["windows", "git", "path", "oracle", "docker", "nginx", "ssh", "host", "vm", "kuma", "sqlite"]),
        ("docs", ["protocol", "docs", "document", "changelog", "index", "report", "megavault", "timeline"]),
        ("feature", ["feature", "added", "implemented", "created", "new "]),
    ]
    for category, needles in category_keywords:
        if any(needle in text for needle in needles):
            if category in VALID_CATEGORIES:
                return category
    return "docs"


def infer_importance(path: Path, content: str, category: str, status: str, summary: str) -> str:
    text = f"{path} {summary} {content[:80_000]}".lower()
    if any(token in text for token in ["protocol", "milestone", "final_permanent", "p0", "global codex timeline", "version=13"]):
        return "P0"
    if category in {"release", "security", "backup"}:
        return "P1"
    if category in {"bugfix", "infra", "migration", "automation"}:
        return "P1" if status in {"PASS", "FAIL", "WARN"} else "P2"
    if "archive" in text or "legacy" in text:
        return "P3"
    if category in {"docs", "qa", "testing", "performance", "feature"}:
        return "P2"
    return "P2"


def infer_event_type(path: Path, content: str, category: str, summary: str) -> str:
    text = f"{path.name} {summary} {content[:50_000]}".lower()
    if ".apk" in text or category == "release":
        return "release"
    if "changelog" in text:
        return "changelog"
    if "protocol" in text:
        return "protocol_update"
    if "report" in text:
        return "report"
    if category in {"qa", "testing"}:
        return "qa"
    if category == "migration":
        return "migration"
    if category == "backup":
        return "backup"
    return "doc_event"


def extract_apk(text: str, path: Path) -> str:
    match = re.search(r"(?i)\b([A-Za-z0-9_. -]{1,60}\.apk)\b", f"{path.name} {text[:100_000]}")
    if not match:
        return ""
    return short_label(match.group(1))


def extract_version(text: str, path: Path) -> tuple[str, str]:
    combined = f"{path.name} {text[:100_000]}"
    name_patterns = [
        r"(?i)\bversion_name\s*[:=]\s*['\"]?([A-Za-z0-9_.-]+)",
        r"(?i)\bversionName\s*[:=]\s*['\"]?([A-Za-z0-9_.-]+)",
        r"(?i)\bv(\d{1,5})\b",
    ]
    code_patterns = [
        r"(?i)\bversion_code\s*[:=]\s*(\d{1,8})",
        r"(?i)\bversionCode\s*[:=]\s*(\d{1,8})",
    ]
    version_name = ""
    version_code = ""
    for pattern in name_patterns:
        match = re.search(pattern, combined)
        if match:
            value = match.group(1)
            version_name = value if value.startswith("v") else f"v{value}" if value.isdigit() else value
            break
    for pattern in code_patterns:
        match = re.search(pattern, combined)
        if match:
            version_code = match.group(1)
            break
    return redact(version_name), redact(version_code)


def extract_commit(text: str) -> str:
    match = re.search(r"\b([a-f0-9]{7,40})\b", text.lower())
    return match.group(1) if match else ""


def extract_branch(text: str) -> str:
    match = re.search(r"(?i)\bbranch\s*[:=]\s*([A-Za-z0-9_./-]+)", text[:80_000])
    return redact(match.group(1)) if match else ""


def extract_artifact_path(text: str) -> str:
    match = re.search(r"(?i)\b([A-Z]:\\[^|<>\"'\n\r]{5,220}|/[^|<>\"'\n\r]{5,220})", text[:120_000])
    if not match:
        return ""
    value = match.group(1).strip()
    if len(value) > 220:
        value = value[:217] + "..."
    return redact(value)


def build_label(project: str, summary: str, content: str, path: Path, apk_name: str, version_name: str) -> str:
    text = f"{path} {summary} {content[:80_000]}".lower()
    alias = display_project(project)
    if apk_name:
        return short_label(f"{alias} {apk_name}" if alias.lower() not in apk_name.lower() else apk_name)
    if version_name and alias:
        return short_label(f"{alias} {version_name}")
    if "global codex timeline" in text or "codex_global_timeline" in text:
        return "Codex Timeline"
    if "veeam" in text and "t7" in text:
        return "Veeam T7"
    if "git" in text and "path" in text:
        return "Git PATH"
    if "tasker" in text and "pixel" in text:
        return "Tasker Pixel"
    if "telegram" in text and "apk" in text:
        return "Telegram APK"
    if "saf" in text and project == "luoghi":
        return "Luoghi SAF"
    if "address" in text and project == "supercontacts":
        return "SC Address"
    if "android" in text and ("test" in text or "qa" in text):
        return "Android Tests"
    clean_summary = re.sub(r"(?i)^prompt\s+\d+\s*[-:]*\s*", "", summary)
    clean_summary = re.sub(r"(?i)\b(final|report|prompt)\b", " ", clean_summary)
    return short_label(f"{alias} {clean_summary}" if alias else clean_summary)


def make_event_id(event_date: str, project: str, label: str, event_type: str, category: str, status: str, summary: str, commit_hash: str, apk_name: str, version_name: str) -> str:
    summary_key = slugify(re.sub(r"(?i)\bprompt[_ -]?\d+\b", "prompt", summary))[:140]
    parts = [event_date, slugify(project), label.lower(), event_type, category, status, summary_key, commit_hash[:12], apk_name.lower(), version_name.lower()]
    digest = hashlib.sha256("|".join(parts).encode("utf-8")).hexdigest()[:20]
    return f"evt_{digest}"


def source_kind(path: Path) -> str:
    suffix = path.suffix.lower().lstrip(".")
    lower = str(path).lower()
    if ".codex" in lower and suffix == "jsonl":
        return "codex_log"
    if suffix == "md":
        return "markdown"
    if suffix in {"json", "jsonl"}:
        return suffix
    if suffix == "csv":
        return "csv"
    if suffix == "log":
        return "log"
    return suffix or "file"


def event_from_file(path: Path, root: Path, discovered_at: str = "") -> Event | None:
    if path.name in SKIP_FILENAMES or path.suffix.lower() not in SOURCE_EXTENSIONS:
        return None
    content = read_sample(path)
    if not content.strip():
        return None
    summary = extract_summary(path, content)
    event_date, date_conf = extract_date(path, content)
    discovered_at = stable_timestamp(event_date)
    project = infer_project(path, content, root)
    status = infer_status(content)
    category = infer_category(path, content, summary)
    importance = infer_importance(path, content, category, status, summary)
    event_type = infer_event_type(path, content, category, summary)
    apk_name = extract_apk(content, path)
    version_name, version_code = extract_version(content, path)
    label = build_label(project, summary, content, path, apk_name, version_name)
    commit_hash = extract_commit(content)
    branch = extract_branch(content)
    artifact_path = extract_artifact_path(content)
    confidence = round(min(0.98, 0.45 + date_conf * 0.25 + (0.15 if summary else 0) + (0.1 if status != "UNKNOWN" else 0)), 2)
    event_id = make_event_id(event_date, project, label, event_type, category, status, summary, commit_hash, apk_name, version_name)
    notes = f"root={redact(str(root))};mtime_date_confidence={date_conf:.2f}"
    return Event(
        id=event_id,
        event_date=event_date,
        discovered_at=discovered_at,
        project=slugify(project),
        category=category,
        importance=importance,
        label_short=label,
        event_type=event_type,
        summary=summary,
        source_path=redact(str(path)),
        source_kind=source_kind(path),
        branch=branch,
        commit_hash=commit_hash,
        artifact_path=artifact_path,
        apk_name=apk_name,
        version_name=version_name,
        version_code=version_code,
        status=status,
        confidence=confidence,
        notes=notes,
    )


def discover_source_roots(primary_root: Path, extra_roots: list[Path]) -> list[Path]:
    """Use only explicit roots; live Codex sessions are intentionally absent."""
    return dedupe_paths([primary_root, *extra_roots])


def dedupe_paths(paths: list[Path]) -> list[Path]:
    seen: set[str] = set()
    result: list[Path] = []
    for path in paths:
        try:
            resolved = str(path.resolve()).lower()
        except OSError:
            continue
        if resolved in seen or not path.exists():
            continue
        seen.add(resolved)
        result.append(path)
    return result


def git_root(path: Path) -> Path | None:
    output = run_git(path, ["rev-parse", "--show-toplevel"]).strip()
    return Path(output).resolve() if output else None


def is_safe_source_path(relative: Path) -> bool:
    parts = {part.lower() for part in relative.parts}
    if parts & {name.lower() for name in SKIP_DIRS}:
        return False
    if parts & {"private", "secrets", ".codex", "sessions"}:
        return False
    if relative.name in SKIP_FILENAMES:
        return False
    return relative.suffix.lower() in SOURCE_EXTENSIONS


def iter_source_files(root: Path) -> list[Path]:
    """Return tracked and untracked/non-ignored files from a Git repo/worktree."""
    repo = git_root(root)
    if repo is None:
        raise RuntimeError(f"source root is not a Git repository or worktree: {root}")
    raw = run_git(repo, ["ls-files", "-co", "--exclude-standard", "-z"])
    files: list[Path] = []
    for item in raw.split("\0"):
        if not item:
            continue
        relative = Path(item)
        path = repo / relative
        if not is_safe_source_path(relative) or not path.is_file():
            continue
        try:
            if path.stat().st_size <= 0:
                continue
        except OSError:
            continue
        files.append(path)
    return sorted(files, key=lambda item: item.as_posix())


def discover_git_repos(source_roots: list[Path]) -> list[Path]:
    """Resolve both normal repositories and linked worktrees via Git itself."""
    return dedupe_paths([repo for root in source_roots if (repo := git_root(root)) is not None])


def find_git() -> str:
    preferred = Path(r"C:\Program Files\Git\cmd\git.exe")
    if preferred.exists():
        return str(preferred)
    found = shutil.which("git")
    return found or "git"


def run_git(repo: Path, args: list[str], timeout: int = 30) -> str:
    git = find_git()
    try:
        completed = subprocess.run(
            [git, "-C", str(repo), *args],
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
        )
    except (OSError, subprocess.TimeoutExpired):
        return ""
    if completed.returncode != 0:
        return ""
    return completed.stdout


def events_from_git(repo: Path, discovered_at: str, max_commits: int) -> list[Event]:
    branch = run_git(repo, ["rev-parse", "--abbrev-ref", "HEAD"]).strip()
    log = run_git(repo, ["log", f"--max-count={max_commits}", "--date=short", "--pretty=format:%H%x1f%ad%x1f%s%x1f%D"], timeout=90)
    events: list[Event] = []
    for line in log.splitlines():
        parts = line.split("\x1f")
        if len(parts) < 3:
            continue
        commit_hash, event_date, subject = parts[:3]
        discovered_at = stable_timestamp(event_date)
        refs = parts[3] if len(parts) > 3 else ""
        project = slugify(repo.name)
        summary = truncate(subject, MAX_SUMMARY_CHARS)
        category = infer_category(repo, "", summary)
        status = "PASS"
        importance = infer_importance(repo, "", category, status, summary)
        apk_name = extract_apk(subject, repo)
        version_name, version_code = extract_version(subject, repo)
        label = build_label(project, summary, subject, repo, apk_name, version_name)
        event_id = make_event_id(event_date, project, label, "git_commit", category, status, summary, commit_hash, apk_name, version_name)
        events.append(
            Event(
                id=event_id,
                event_date=event_date,
                discovered_at=discovered_at,
                project=project,
                category=category,
                importance=importance,
                label_short=label,
                event_type="git_commit",
                summary=summary,
                source_path=redact(str(repo)),
                source_kind="git_log",
                branch=redact(branch),
                commit_hash=commit_hash,
                artifact_path="",
                apk_name=apk_name,
                version_name=version_name,
                version_code=version_code,
                status=status,
                confidence=0.96,
                notes=truncate(f"refs={refs}", 180),
            )
        )
    return events


def connect_db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS timeline_events (
            id TEXT PRIMARY KEY,
            event_date TEXT NOT NULL,
            discovered_at TEXT NOT NULL,
            project TEXT NOT NULL,
            category TEXT NOT NULL,
            importance TEXT NOT NULL,
            label_short TEXT NOT NULL,
            event_type TEXT NOT NULL,
            summary TEXT NOT NULL,
            source_path TEXT NOT NULL,
            source_kind TEXT NOT NULL,
            branch TEXT,
            commit_hash TEXT,
            artifact_path TEXT,
            apk_name TEXT,
            version_name TEXT,
            version_code TEXT,
            status TEXT NOT NULL,
            confidence REAL NOT NULL,
            notes TEXT
        )
        """
    )
    conn.execute("CREATE INDEX IF NOT EXISTS idx_timeline_event_date ON timeline_events(event_date)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_timeline_project ON timeline_events(project)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_timeline_category ON timeline_events(category)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_timeline_importance ON timeline_events(importance)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_timeline_status ON timeline_events(status)")
    return conn


def checkpoint_existing_db(path: Path) -> None:
    """Materialize any valid WAL, then leave no transient SQLite sidecars."""
    if path.exists():
        conn = sqlite3.connect(path)
        try:
            conn.execute("PRAGMA wal_checkpoint(TRUNCATE)")
        finally:
            conn.close()
    for suffix in ("-wal", "-shm"):
        sidecar = Path(f"{path}{suffix}")
        if sidecar.exists():
            sidecar.unlink()


def load_existing_events(path: Path) -> list[Event]:
    if not path.exists():
        return []
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    try:
        table = conn.execute(
            "SELECT 1 FROM sqlite_master WHERE type='table' AND name='timeline_events'"
        ).fetchone()
        if table is None:
            return []
        return [Event(**{column: row[column] for column in SCHEMA_COLUMNS}) for row in conn.execute("SELECT * FROM timeline_events")]
    finally:
        conn.close()


def create_schema(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE timeline_events (
            id TEXT PRIMARY KEY,
            event_date TEXT NOT NULL,
            discovered_at TEXT NOT NULL,
            project TEXT NOT NULL,
            category TEXT NOT NULL,
            importance TEXT NOT NULL,
            label_short TEXT NOT NULL,
            event_type TEXT NOT NULL,
            summary TEXT NOT NULL,
            source_path TEXT NOT NULL,
            source_kind TEXT NOT NULL,
            branch TEXT,
            commit_hash TEXT,
            artifact_path TEXT,
            apk_name TEXT,
            version_name TEXT,
            version_code TEXT,
            status TEXT NOT NULL,
            confidence REAL NOT NULL,
            notes TEXT
        )
        """
    )
    conn.execute("CREATE INDEX idx_timeline_event_date ON timeline_events(event_date)")
    conn.execute("CREATE INDEX idx_timeline_project ON timeline_events(project)")
    conn.execute("CREATE INDEX idx_timeline_category ON timeline_events(category)")
    conn.execute("CREATE INDEX idx_timeline_importance ON timeline_events(importance)")
    conn.execute("CREATE INDEX idx_timeline_status ON timeline_events(status)")


def write_deterministic_db(path: Path, events: list[Event]) -> bool:
    """Rebuild canonically, replacing the target only when its bytes change."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    os.close(fd)
    temporary = Path(temporary_name)
    try:
        conn = sqlite3.connect(temporary)
        try:
            conn.execute("PRAGMA page_size=4096")
            conn.execute("PRAGMA auto_vacuum=NONE")
            conn.execute("PRAGMA journal_mode=DELETE")
            conn.execute("PRAGMA synchronous=FULL")
            create_schema(conn)
            placeholders = ",".join("?" for _ in SCHEMA_COLUMNS)
            columns = ",".join(SCHEMA_COLUMNS)
            rows = [tuple(getattr(event, column) for column in SCHEMA_COLUMNS) for event in sorted(events, key=lambda item: item.id)]
            conn.executemany(f"INSERT INTO timeline_events ({columns}) VALUES ({placeholders})", rows)
            conn.commit()
            conn.execute("VACUUM")
        finally:
            conn.close()
        if path.exists() and path.read_bytes() == temporary.read_bytes():
            return False
        os.replace(temporary, path)
        return True
    finally:
        if temporary.exists():
            temporary.unlink()


def merge_append_only(existing: list[Event], discovered: list[Event]) -> list[Event]:
    """Preserve all historical rows and add only new, non-equivalent events."""
    by_id = {event.id: event for event in existing}
    equivalence = {event_equivalence_key(event) for event in existing}
    for event in sorted(discovered, key=lambda item: item.id):
        if event.id in by_id or event_equivalence_key(event) in equivalence:
            continue
        by_id[event.id] = event
        equivalence.add(event_equivalence_key(event))
    return list(by_id.values())


def upsert_events(conn: sqlite3.Connection, events: list[Event]) -> None:
    sql = """
        INSERT INTO timeline_events (
            id,event_date,discovered_at,project,category,importance,label_short,event_type,
            summary,source_path,source_kind,branch,commit_hash,artifact_path,apk_name,
            version_name,version_code,status,confidence,notes
        ) VALUES (
            :id,:event_date,:discovered_at,:project,:category,:importance,:label_short,:event_type,
            :summary,:source_path,:source_kind,:branch,:commit_hash,:artifact_path,:apk_name,
            :version_name,:version_code,:status,:confidence,:notes
        )
        ON CONFLICT(id) DO UPDATE SET
            event_date=excluded.event_date,
            discovered_at=timeline_events.discovered_at,
            project=excluded.project,
            category=excluded.category,
            importance=excluded.importance,
            label_short=excluded.label_short,
            event_type=excluded.event_type,
            summary=excluded.summary,
            source_path=excluded.source_path,
            source_kind=excluded.source_kind,
            branch=excluded.branch,
            commit_hash=excluded.commit_hash,
            artifact_path=excluded.artifact_path,
            apk_name=excluded.apk_name,
            version_name=excluded.version_name,
            version_code=excluded.version_code,
            status=excluded.status,
            confidence=excluded.confidence,
            notes=excluded.notes
    """
    conn.executemany(sql, [event.__dict__ for event in events])
    sync_current_event_set(conn, [event.id for event in events])
    delete_equivalent_duplicates(conn)
    conn.commit()


def sync_current_event_set(conn: sqlite3.Connection, event_ids: list[str]) -> None:
    conn.execute("CREATE TEMP TABLE IF NOT EXISTS current_timeline_event_ids (id TEXT PRIMARY KEY)")
    conn.execute("DELETE FROM current_timeline_event_ids")
    conn.executemany("INSERT OR IGNORE INTO current_timeline_event_ids(id) VALUES (?)", [(event_id,) for event_id in event_ids])
    conn.execute(
        """
        DELETE FROM timeline_events
        WHERE id NOT IN (SELECT id FROM current_timeline_event_ids)
        """
    )
    conn.execute("DROP TABLE current_timeline_event_ids")


def event_equivalence_key(event: Event) -> tuple[str, str, str, str, str, str]:
    return (
        event.event_date,
        event.project,
        event.label_short.lower(),
        event.event_type,
        slugify(event.summary),
        event.status,
    )


def source_score(kind: str) -> int:
    return {
        "git_log": 60,
        "markdown": 50,
        "json": 40,
        "jsonl": 35,
        "codex_log": 30,
        "csv": 20,
        "log": 10,
    }.get(kind, 0)


def dedupe_events(events: list[Event]) -> list[Event]:
    grouped: dict[tuple[str, str, str, str, str, str], Event] = {}
    for event in events:
        key = event_equivalence_key(event)
        current = grouped.get(key)
        if current is None:
            grouped[key] = event
            continue
        current_rank = (current.confidence, source_score(current.source_kind), -len(current.source_path), current.id)
        event_rank = (event.confidence, source_score(event.source_kind), -len(event.source_path), event.id)
        if event_rank > current_rank:
            grouped[key] = event
    return list(grouped.values())


def delete_equivalent_duplicates(conn: sqlite3.Connection) -> None:
    rows = conn.execute(
        """
        SELECT id,event_date,project,label_short,event_type,summary,status,confidence,source_kind,source_path
        FROM timeline_events
        """
    ).fetchall()
    grouped: dict[tuple[str, str, str, str, str, str], list[sqlite3.Row]] = defaultdict(list)
    for row in rows:
        key = (
            row["event_date"],
            row["project"],
            row["label_short"].lower(),
            row["event_type"],
            slugify(row["summary"]),
            row["status"],
        )
        grouped[key].append(row)
    delete_ids: list[str] = []
    for duplicates in grouped.values():
        if len(duplicates) <= 1:
            continue
        keep = sorted(
            duplicates,
            key=lambda row: (row["confidence"], source_score(row["source_kind"]), -len(row["source_path"]), row["id"]),
            reverse=True,
        )[0]["id"]
        delete_ids.extend(row["id"] for row in duplicates if row["id"] != keep)
    if delete_ids:
        conn.executemany("DELETE FROM timeline_events WHERE id=?", [(item,) for item in delete_ids])


def fetch_events(conn: sqlite3.Connection) -> list[sqlite3.Row]:
    rows = conn.execute(
        """
        SELECT * FROM timeline_events
        ORDER BY event_date DESC, project COLLATE NOCASE, importance, label_short COLLATE NOCASE, id
        """
    ).fetchall()
    return rows


def table_escape(value: object, limit: int = 0) -> str:
    text = redact("" if value is None else str(value))
    text = text.replace("|", "/")
    if limit:
        text = truncate(text, limit)
    return text


def write_if_changed(path: Path, content: str) -> bool:
    encoded = content.encode("utf-8")
    if path.exists() and path.read_bytes() == encoded:
        return False
    path.write_bytes(encoded)
    return True


def write_reports(conn: sqlite3.Connection, source_roots: list[Path]) -> None:
    events = fetch_events(conn)
    generated_at = stable_timestamp(max((row["event_date"] for row in events), default="1970-01-01"))
    by_project = Counter(row["project"] for row in events)
    by_category = Counter(row["category"] for row in events)
    by_importance = Counter(row["importance"] for row in events)
    by_status = Counter(row["status"] for row in events)
    p0_events = [row for row in events if row["importance"] == "P0"]
    recent_events = events[:20]

    lines: list[str] = []
    lines.append("# Global Codex Timeline")
    lines.append("")
    lines.append(f"Generated: {generated_at}")
    lines.append(f"SQLite canonical source: `{table_escape(DB_PATH)}`")
    lines.append(f"Total events: {len(events)}")
    lines.append("")
    lines.append("## Source Roots")
    for root in source_roots:
        lines.append(f"- `{table_escape(root)}`")
    lines.append("")
    lines.append("## Statistics")
    lines.extend(counter_lines("Events by project", by_project))
    lines.extend(counter_lines("Events by category", by_category))
    lines.extend(counter_lines("Events by importance", by_importance))
    lines.extend(counter_lines("Events by status", by_status))
    lines.append("")
    lines.append("## Recent Events")
    lines.extend(event_table(recent_events))
    lines.append("")
    lines.append("## P0 Milestones")
    lines.extend(event_table(p0_events))
    lines.append("")
    lines.append("## Projects")
    for project, count in sorted(by_project.items(), key=lambda item: (-item[1], item[0])):
        latest = next((row for row in events if row["project"] == project), None)
        latest_date = latest["event_date"] if latest else ""
        latest_label = latest["label_short"] if latest else ""
        lines.append(f"- `{project}`: {count} events; latest={latest_date}; label={table_escape(latest_label)}")
    lines.append("")
    lines.append("## Complete Timeline")
    lines.extend(event_table(events))
    write_if_changed(REPORT_PATH, "\n".join(lines) + "\n")

    ai_lines = [
        "# Global Codex Timeline AI",
        f"generated_at={generated_at}",
        f"total_events={len(events)}",
        "format=event_date|project|label_short|category|status|importance",
    ]
    for row in events:
        ai_lines.append(
            "|".join(
                [
                    table_escape(row["event_date"]),
                    table_escape(row["project"]),
                    table_escape(row["label_short"]),
                    table_escape(row["category"]),
                    table_escape(row["status"]),
                    table_escape(row["importance"]),
                ]
            )
        )
    write_if_changed(AI_REPORT_PATH, "\n".join(ai_lines) + "\n")


def counter_lines(title: str, counter: Counter[str]) -> list[str]:
    lines = [f"### {title}", "", "| Value | Events |", "|---|---:|"]
    for key, value in sorted(counter.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"| {table_escape(key)} | {value} |")
    lines.append("")
    return lines


def event_table(rows: list[sqlite3.Row]) -> list[str]:
    lines = ["| Date | Project | Label | Category | Status | Importance | Type | Source | Summary |", "|---|---|---|---|---|---|---|---|---|"]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    table_escape(row["event_date"]),
                    table_escape(row["project"]),
                    table_escape(row["label_short"]),
                    table_escape(row["category"]),
                    table_escape(row["status"]),
                    table_escape(row["importance"]),
                    table_escape(row["event_type"]),
                    table_escape(row["source_kind"]),
                    table_escape(row["summary"], MAX_REPORT_SUMMARY_CHARS),
                ]
            )
            + " |"
        )
    return lines


def count_secret_hits(paths: list[Path]) -> int:
    hits = 0
    for path in paths:
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for pattern in SECRET_PATTERNS:
            hits += len(pattern.findall(text))
    return hits


def validate(conn: sqlite3.Connection) -> dict[str, object]:
    integrity = conn.execute("PRAGMA integrity_check").fetchone()[0]
    total = conn.execute("SELECT COUNT(*) FROM timeline_events").fetchone()[0]
    duplicate_ids = conn.execute(
        "SELECT COUNT(*) FROM (SELECT id FROM timeline_events GROUP BY id HAVING COUNT(*) > 1)"
    ).fetchone()[0]
    duplicate_equiv = conn.execute(
        """
        SELECT COUNT(*) FROM (
            SELECT event_date,project,label_short,event_type,summary,status,COUNT(*) c
            FROM timeline_events
            GROUP BY event_date,project,label_short,event_type,summary,status
            HAVING c > 1
        )
        """
    ).fetchone()[0]
    invalid_labels = conn.execute(
        """
        SELECT COUNT(*) FROM timeline_events
        WHERE length(trim(label_short)) = 0
           OR (length(trim(label_short)) - length(replace(trim(label_short), ' ', '')) + 1) > 4
        """
    ).fetchone()[0]
    invalid_categories = conn.execute(
        f"SELECT COUNT(*) FROM timeline_events WHERE category NOT IN ({','.join('?' for _ in VALID_CATEGORIES)})",
        sorted(VALID_CATEGORIES),
    ).fetchone()[0]
    invalid_importance = conn.execute(
        f"SELECT COUNT(*) FROM timeline_events WHERE importance NOT IN ({','.join('?' for _ in VALID_IMPORTANCE)})",
        sorted(VALID_IMPORTANCE),
    ).fetchone()[0]
    generated_secret_hits = count_secret_hits([REPORT_PATH, AI_REPORT_PATH])
    return {
        "sqlite_integrity": integrity,
        "total_events": total,
        "duplicate_ids": duplicate_ids,
        "duplicate_equivalent_events": duplicate_equiv,
        "invalid_labels": invalid_labels,
        "invalid_categories": invalid_categories,
        "invalid_importance": invalid_importance,
        "generated_secret_hits": generated_secret_hits,
    }


def print_counts(conn: sqlite3.Connection, title: str, column: str) -> None:
    print(title)
    for value, count in conn.execute(f"SELECT {column}, COUNT(*) FROM timeline_events GROUP BY {column} ORDER BY COUNT(*) DESC, {column}"):
        print(f"  {value}: {count}")


def print_recent(conn: sqlite3.Connection) -> None:
    print("recent_20")
    for row in conn.execute(
        """
        SELECT event_date,project,label_short,category,status,importance
        FROM timeline_events
        ORDER BY event_date DESC, project, label_short
        LIMIT 20
        """
    ):
        print("|".join(str(value) for value in row))


def print_milestones(conn: sqlite3.Connection) -> None:
    print("milestones_p0")
    for row in conn.execute(
        """
        SELECT event_date,project,label_short,category,status,summary
        FROM timeline_events
        WHERE importance='P0'
        ORDER BY event_date DESC, project, label_short
        """
    ):
        print("|".join(table_escape(value, 120) for value in row))


def build(args: argparse.Namespace) -> int:
    global DB_PATH, REPORT_PATH, AI_REPORT_PATH
    primary_root = Path(args.primary_root).resolve()
    output_dir = Path(args.output_dir).resolve()
    DB_PATH = output_dir / "codex_global_timeline.sqlite"
    REPORT_PATH = output_dir / "codex_global_timeline.md"
    AI_REPORT_PATH = output_dir / "codex_global_timeline_ai.md"
    source_roots = discover_source_roots(primary_root, [Path(item) for item in args.source_root])
    events_by_id: dict[str, Event] = {}
    file_count = 0
    for root in source_roots:
        for path in iter_source_files(root):
            file_count += 1
            event = event_from_file(path, root)
            if event is not None:
                events_by_id[event.id] = event

    git_events = 0
    if not args.no_git:
        primary_repo = git_root(primary_root)
        for repo in discover_git_repos(source_roots):
            # Importing this repository's HEAD would make every generator commit
            # recursively change its own canonical output.
            if primary_repo is not None and repo == primary_repo:
                continue
            for event in events_from_git(repo, "", args.max_git_commits):
                git_events += 1
                events_by_id[event.id] = event

    deduped_events = dedupe_events(list(events_by_id.values()))
    checkpoint_existing_db(DB_PATH)
    existing_events = load_existing_events(DB_PATH)
    complete_events = merge_append_only(existing_events, deduped_events)
    database_changed = write_deterministic_db(DB_PATH, complete_events)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    write_reports(conn, source_roots)
    validation = validate(conn)

    print("Global Codex Timeline build")
    print(f"source_roots={len(source_roots)}")
    print(f"source_files_scanned={file_count}")
    print(f"events_discovered_this_run={len(events_by_id)}")
    print(f"events_after_equivalence_dedupe={len(deduped_events)}")
    print(f"events_preserved_from_history={len(existing_events)}")
    print(f"database_changed={'yes' if database_changed else 'no'}")
    print(f"git_events_discovered={git_events}")
    for key, value in validation.items():
        print(f"{key}={value}")
    print(f"sqlite={DB_PATH}")
    print(f"report={REPORT_PATH}")
    print(f"ai_report={AI_REPORT_PATH}")
    print_counts(conn, "events_by_project", "project")
    print_counts(conn, "events_by_category", "category")
    print_counts(conn, "events_by_importance", "importance")
    print_recent(conn)
    print_milestones(conn)
    conn.close()

    failed = [
        validation["sqlite_integrity"] != "ok",
        validation["duplicate_ids"] != 0,
        validation["duplicate_equivalent_events"] != 0,
        validation["invalid_labels"] != 0,
        validation["invalid_categories"] != 0,
        validation["invalid_importance"] != 0,
        validation["generated_secret_hits"] != 0,
    ]
    return 1 if any(failed) else 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the mandatory Global Codex Timeline.")
    parser.add_argument("--primary-root", default=str(BASE_DIR), help="Primary Git repository or worktree root.")
    parser.add_argument("--source-root", action="append", default=[], help="Extra source root to scan recursively.")
    parser.add_argument("--output-dir", default=str(BASE_DIR), help="Directory for the three canonical outputs.")
    parser.add_argument("--no-git", action="store_true", help="Skip local git log import.")
    parser.add_argument("--max-git-commits", type=int, default=DEFAULT_GIT_MAX_COMMITS, help="Max commits imported per local repository.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    return build(args)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
