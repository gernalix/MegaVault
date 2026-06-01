META:
name=codex-html-live
slug=codex-html-live
path=/home/daniele/codex-workspace/codex-html-live
remote=none
branch=master
verified_commit=1e8ecaa
verified_at=2026-06-01T13:59:53+02:00
protocol=MEGAVAULT_PROTOCOL.md:v2
PURPOSE:
purpose=Live HTML archive for Codex JSONL sessions: watches session files and renders browser-readable chat archives without relying on tmux
STACK:
lang=Python
fw=UNKNOWN
db=UNKNOWN
platform=UNKNOWN
tools=systemd
MAP:
entry=UNKNOWN
ui=UNKNOWN
core=codex_html_live.py,dev/project.metadata.json
db=UNKNOWN
tests=tests/test_codex_html_live.py
scripts=UNKNOWN
build=UNKNOWN
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
core=codex_html_live.py:RenderedSession,iso_from_mtime,safe_name,ensure_output_dir,atomic_write,text_from_content
test=tests/test_codex_html_live.py:CodexHtmlLiveTests
FLOW:
flow=tests/test_codex_html_live.py:4:from pathlib import Path
flow=tests/test_codex_html_live.py:8:SPEC = importlib.util.spec_from_file_location("codex_html_live", ROOT / "codex_html_live.py")
flow=tests/test_codex_html_live.py:9:codex_html_live = importlib.util.module_from_spec(SPEC)
INV:
arch=codex_html_live.py:RenderedSession,iso_from_mtime,safe_name,ensure_output_dir,atomic_write; tests/test_codex_html_live.py:CodexHtmlLiveTests
data=codex_html_live.py:145:session.html_path = OUTPUT_DIR / f"{safe_name(session.session_id)}.html"; codex_html_live.py:331:target = cached_session.html_path if cached_session else OUTPUT_DIR / f"{safe_name(path.stem)}.html"
ux=codex_html_live.py:44:def safe_name(value: str) -> str:; codex_html_live.py:94:role_class = safe_name(role.lower())
backup=UNKNOWN
migration=UNKNOWN
version=dev/project.metadata.json:9:"metadata_version": 1,
i18n=UNKNOWN
security=UNKNOWN
perf=codex_html_live.py:199:@media (max-width: 720px) { .top { display: block; } th:nth-child(3), td:nth-child(3) { display: none; } .wrap { padding: 14px; } }; codex_html_live.py:331:target = cached_session.html_path if cached_session else O...
BUILD:
files=UNKNOWN
cmd=UNKNOWN
TEST:
files=tests/test_codex_html_live.py
cmd=UNKNOWN
DATA:
db=DB=UNKNOWN
paths=UNKNOWN
backup=UNKNOWN
restore=codex_html_live.py:11:from dataclasses import dataclass, field; tests/test_codex_html_live.py:4:from pathlib import Path
import=codex_html_live.py:11:from dataclasses import dataclass, field; tests/test_codex_html_live.py:4:from pathlib import Path
export=tests/test_codex_html_live.py:21:source = sessions / "session.jsonl"; dev/project.metadata.json:9:"metadata_version": 1,
migration=UNKNOWN
retention=UNKNOWN
DNB:
dnb=codex_html_live.py:199:@media (max-width: 720px) { .top { display: block; } th:nth-child(3), td:nth-child(3) { display: none; } .wrap { padding: 14px; } }
dnb=preserve=dev/project.metadata.json,dev/legacy,AI/Human links; docs-only tasks must not touch app code/DB
BUG:
issue=UNKNOWN
RISK:
risk=codex_html_live.py:199:@media (max-width: 720px) { .top { display: block; } th:nth-child(3), td:nth-child(3) { display: none; } .wrap { padding: 14px; } }
ROAD:
now=UNKNOWN
next=UNKNOWN
later=UNKNOWN
LINK:
meta=../../../codex-html-live/dev/project.metadata.json
human=../../human/projects/codex-html-live/overview.md
legacy=../../../codex-html-live/dev/legacy
repo=../../../codex-html-live
OPEN:
open=none
