META:
name=codex-html-live
slug=codex-html-live
path=/home/daniele/codex-workspace/codex-html-live
remote=none
branch=master
verified_commit=1e8ecaa
verified_at=2026-06-01T13:39:31+02:00
PURPOSE:
- Live HTML archive for Codex JSONL sessions: watches session files and renders browser-readable chat archives without relying on tmux.
STACK:
lang=Python;fw=UNKNOWN;db=UNKNOWN;platform=UNKNOWN;tools=systemd
MAP:
entry=UNKNOWN
core=codex_html_live.py,dev/project.metadata.json
ui=UNKNOWN
db=UNKNOWN
tests=tests/test_codex_html_live.py
scripts=UNKNOWN
build=UNKNOWN
ci=UNKNOWN
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
- codex_html_live.py=>RenderedSession,iso_from_mtime,safe_name,ensure_output_dir,atomic_write,text_from_content,short_
- codex_html_live.py:2:import argparse
- codex_html_live.py:3:import gc
- codex_html_live.py:4:import html
- codex_html_live.py:5:import json
- codex_html_live.py:6:import os
- codex_html_live.py:7:import re
FLOW:
- codex_html_live.py:2:import argparse
- codex_html_live.py:3:import gc
- codex_html_live.py:4:import html
- codex_html_live.py:5:import json
- codex_html_live.py:6:import os
- codex_html_live.py:7:import re
- codex_html_live.py:8:import subprocess
- codex_html_live.py:9:import sys
- tests/test_codex_html_live.py:1:import importlib.util
- tests/test_codex_html_live.py:2:import tempfile
- tests/test_codex_html_live.py:3:import unittest
- tests/test_codex_html_live.py:4:from pathlib import Path
INV:
arch=codex_html_live.py:44:def safe_name(value: str) -> str:
arch=codex_html_live.py:94:role_class = safe_name(role.lower())
arch=codex_html_live.py:109:html_path=OUTPUT_DIR / f"{safe_name(fallback_id)}.html",
arch=codex_html_live.py:145:session.html_path = OUTPUT_DIR / f"{safe_name(session.session_id)}.html"
arch=codex_html_live.py:199:@media (max-width: 720px) { .top { display: block; } th:nth-child(3), td:nth-child(3) { d
arch=codex_html_live.py:331:target = cached_session.html_path if cached_session else OUTPUT_DIR / f"{safe_name(path.s
data=codex_html_live.py:2:import argparse
data=codex_html_live.py:3:import gc
data=codex_html_live.py:4:import html
data=codex_html_live.py:5:import json
safety=codex_html_live.py:199:@media (max-width: 720px) { .top { display: block; } th:nth-child(3), td:nth-child(3) { d
safety=codex_html_live.py:348:removed = set(previous) - set(observed)
safety=codex_html_live.py:349:for path in removed:
safety=codex_html_live.py:352:if removed or ((set(previous) != set(rendered_state) or changed or not (OUTPUT_DIR / "ind
safety=codex_html_live.py:44:def safe_name(value: str) -> str:
safety=codex_html_live.py:94:role_class = safe_name(role.lower())
safety=codex_html_live.py:109:html_path=OUTPUT_DIR / f"{safe_name(fallback_id)}.html",
ux=UNKNOWN
version=dev/project.metadata.json:9:"metadata_version": 1,
i18n=UNKNOWN
BUILD:
- UNKNOWN
TEST:
- tests/test_codex_html_live.py:3:import unittest
- tests/test_codex_html_live.py:10:assert SPEC.loader is not None
- tests/test_codex_html_live.py:14:class CodexHtmlLiveTests(unittest.TestCase):
- tests/test_codex_html_live.py:15:def test_changed_session_is_rate_limited(self) -> None:
- tests/test_codex_html_live.py:40:self.assertTrue(changed)
- tests/test_codex_html_live.py:42:self.assertTrue(html_path.exists())
- tests/test_codex_html_live.py:57:self.assertFalse(changed)
- tests/test_codex_html_live.py:58:self.assertEqual(first_mtime, html_path.stat().st_mtime_ns)
- tests/test_codex_html_live.py:67:self.assertTrue(changed)
- tests/test_codex_html_live.py:68:self.assertGreater(html_path.stat().st_mtime_ns, first_mtime)
DATA:
db=codex_html_live.py:2:import argparse
db=codex_html_live.py:3:import gc
db=codex_html_live.py:4:import html
db=codex_html_live.py:5:import json
backup=UNKNOWN
import=codex_html_live.py:2:import argparse
import=codex_html_live.py:3:import gc
import=codex_html_live.py:4:import html
export=UNKNOWN
migration=UNKNOWN
retention=UNKNOWN
DNB:
- codex_html_live.py:199:@media (max-width: 720px) { .top { display: block; } th:nth-child(3), td:nth-child(3) { displ
- codex_html_live.py:348:removed = set(previous) - set(observed)
- codex_html_live.py:349:for path in removed:
- codex_html_live.py:352:if removed or ((set(previous) != set(rendered_state) or changed or not (OUTPUT_DIR / "index.h
- codex_html_live.py:44:def safe_name(value: str) -> str:
- codex_html_live.py:94:role_class = safe_name(role.lower())
- codex_html_live.py:109:html_path=OUTPUT_DIR / f"{safe_name(fallback_id)}.html",
- codex_html_live.py:145:session.html_path = OUTPUT_DIR / f"{safe_name(session.session_id)}.html"
- codex_html_live.py:331:target = cached_session.html_path if cached_session else OUTPUT_DIR / f"{safe_name(path.stem)
- dev/project.metadata.json:9:"metadata_version": 1,
BUG:
- codex_html_live.py:56:if path.exists() and path.read_text(encoding="utf-8", errors="replace") == content:
- codex_html_live.py:58:except OSError:
- codex_html_live.py:118:with path.open("r", encoding="utf-8", errors="replace") as handle:
- codex_html_live.py:132:except json.JSONDecodeError as exc:
- codex_html_live.py:133:return message_row("tool", "", f"JSON parse error: {exc}\n{raw[:1000]}")
- codex_html_live.py:322:except FileNotFoundError:
- codex_html_live.py:380:except Exception as exc:
- codex_html_live.py:381:print(f"codex-html-live error: {exc}", file=sys.stderr, flush=True)
RISK:
- codex_html_live.py:199:@media (max-width: 720px) { .top { display: block; } th:nth-child(3), td:nth-child(3) { displ
- codex_html_live.py:348:removed = set(previous) - set(observed)
- codex_html_live.py:349:for path in removed:
- codex_html_live.py:352:if removed or ((set(previous) != set(rendered_state) or changed or not (OUTPUT_DIR / "index.h
ROAD:
now=codex_html_live.py:315:next_cache: dict[Path, RenderedSession] = {}
next=codex_html_live.py:328:next_cache[path] = cache[path]
later=codex_html_live.py:336:next_cache[path] = cached_session
LINK:
meta=../../../codex-html-live/dev/project.metadata.json
human=../../human/projects/codex-html-live/overview.md
legacy=../../../codex-html-live/dev/legacy
repo=../../../codex-html-live
OPEN:
- none
