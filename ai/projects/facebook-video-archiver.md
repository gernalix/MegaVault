META:
name=facebook-video-archiver
slug=facebook-video-archiver
path=/home/daniele/codex-workspace/facebook-video-archiver
remote=none
branch=work/v4-deep-discovery
verified_commit=ab0e526
verified_at=2026-06-01T13:39:31+02:00
PURPOSE:
- Start here for Codex/operator work on `facebook-video-archiver`.
STACK:
lang=Python,Shell;fw=Playwright;db=UNKNOWN;platform=UNKNOWN;tools=Chrome,yt-dlp
MAP:
entry=UNKNOWN
core=dev/project.metadata.json
core=facebook_archive_dashboard.py
core=facebook_session_browser.py
core=systemd/user/facebook-video-archiver.service
core=systemd/user/facebook-video-archiver.timer
ui=UNKNOWN
db=UNKNOWN
tests=UNKNOWN
scripts=facebook_video_archiver.sh
build=UNKNOWN
ci=UNKNOWN
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
- facebook_archive_dashboard.py=>human_bytes,count_files_and_bytes,read_urls,recent_log,tail_lines,process_status,acti
- facebook_session_browser.py=>expand,load_env_file,safe_print,normalize_facebook_url,read_existing_urls,write_deduped
- facebook_archive_dashboard.py:3:import argparse
- facebook_archive_dashboard.py:4:import os
- facebook_archive_dashboard.py:5:import re
- facebook_archive_dashboard.py:6:import subprocess
- facebook_archive_dashboard.py:7:import time
- facebook_archive_dashboard.py:8:from pathlib import Path
FLOW:
- facebook_archive_dashboard.py:3:import argparse
- facebook_archive_dashboard.py:4:import os
- facebook_archive_dashboard.py:5:import re
- facebook_archive_dashboard.py:6:import subprocess
- facebook_archive_dashboard.py:7:import time
- facebook_archive_dashboard.py:8:from pathlib import Path
- facebook_archive_dashboard.py:49:if line and not line.startswith("#"):
- facebook_archive_dashboard.py:70:return "stopped", ""
- facebook_session_browser.py:3:import argparse
- facebook_session_browser.py:4:import asyncio
- facebook_session_browser.py:5:import http.cookiejar
- facebook_session_browser.py:6:import json
INV:
arch=dev/project.metadata.json:9:"metadata_version": 1,
arch=facebook_archive_dashboard.py:184:raise SystemExit(main())
arch=facebook_session_browser.py:43:def safe_print(message: str) -> None:
arch=facebook_session_browser.py:101:safe_print(f"ERROR: Playwright is not available in this environment: {exc}")
arch=facebook_session_browser.py:102:safe_print("Run: ./facebook_video_archiver.sh --setup")
arch=facebook_session_browser.py:103:raise SystemExit(2) from exc
data=facebook_archive_dashboard.py:3:import argparse
data=facebook_archive_dashboard.py:4:import os
data=facebook_archive_dashboard.py:5:import re
data=facebook_archive_dashboard.py:6:import subprocess
safety=facebook_archive_dashboard.py:124:if any(token in line.lower() for token in ("warning", "error", "failed", "unsu
safety=facebook_session_browser.py:5:import http.cookiejar
safety=facebook_session_browser.py:17:DEFAULT_COOKIE_EXPORT = "~/.config/facebook-video-archiver/facebook-cookies.txt"
safety=facebook_session_browser.py:133:cookies = await context.cookies("https://www.facebook.com")
safety=facebook_session_browser.py:134:cookie_names = {cookie.get("name", "") for cookie in cookies}
safety=facebook_session_browser.py:135:if "c_user" in cookie_names or "xs" in cookie_names:
safety=facebook_session_browser.py:205:safe_print("Nessun URL trovato. Possibili limiti: cookie/sessione scaduti, check
ux=facebook_session_browser.py:121:safe_print("Fai login manualmente su Facebook, completa eventuale 2FA/checkpoint
version=dev/project.metadata.json:9:"metadata_version": 1,
version=facebook_video_archiver.sh:6:VERSION_FILE="$SCRIPT_DIR/VERSION"
version=facebook_video_archiver.sh:7:VERSION="$(tr -d '[:space:]' < "$VERSION_FILE")"
version=facebook_video_archiver.sh:37:facebook-video-archiver $VERSION
i18n=strings/resources present; verify no hardcoded UI
BUILD:
- facebook_video_archiver.sh:2:#!/usr/bin/env bash
- facebook_video_archiver.sh:40:./facebook_video_archiver.sh --version
- facebook_video_archiver.sh:41:./facebook_video_archiver.sh --setup
- facebook_video_archiver.sh:42:./facebook_video_archiver.sh --check
- facebook_video_archiver.sh:43:./facebook_video_archiver.sh --login-browser
- facebook_video_archiver.sh:44:./facebook_video_archiver.sh --check-session
- facebook_video_archiver.sh:45:./facebook_video_archiver.sh --discover-browser
- facebook_video_archiver.sh:46:./facebook_video_archiver.sh --discover-deep
TEST:
- UNKNOWN
DATA:
db=facebook_archive_dashboard.py:3:import argparse
db=facebook_archive_dashboard.py:4:import os
db=facebook_archive_dashboard.py:5:import re
db=facebook_archive_dashboard.py:6:import subprocess
backup=UNKNOWN
import=facebook_archive_dashboard.py:3:import argparse
import=facebook_archive_dashboard.py:4:import os
import=facebook_archive_dashboard.py:5:import re
export=facebook_archive_dashboard.py:3:import argparse
export=facebook_archive_dashboard.py:4:import os
export=facebook_archive_dashboard.py:5:import re
migration=UNKNOWN
retention=facebook_session_browser.py:339:def cookie_expires(cookie: dict) -> int:
retention=facebook_session_browser.py:340:expires = cookie.get("expires", -1)
DNB:
- facebook_archive_dashboard.py:124:if any(token in line.lower() for token in ("warning", "error", "failed", "unsuppor
- facebook_session_browser.py:5:import http.cookiejar
- facebook_session_browser.py:17:DEFAULT_COOKIE_EXPORT = "~/.config/facebook-video-archiver/facebook-cookies.txt"
- facebook_session_browser.py:133:cookies = await context.cookies("https://www.facebook.com")
- facebook_session_browser.py:134:cookie_names = {cookie.get("name", "") for cookie in cookies}
- facebook_session_browser.py:135:if "c_user" in cookie_names or "xs" in cookie_names:
- facebook_session_browser.py:205:safe_print("Nessun URL trovato. Possibili limiti: cookie/sessione scaduti, checkpoin
- facebook_session_browser.py:339:def cookie_expires(cookie: dict) -> int:
- dev/project.metadata.json:9:"metadata_version": 1,
- facebook_session_browser.py:43:def safe_print(message: str) -> None:
BUG:
- facebook_archive_dashboard.py:38:except OSError:
- facebook_archive_dashboard.py:47:for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
- facebook_archive_dashboard.py:62:lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
- facebook_archive_dashboard.py:69:except subprocess.CalledProcessError:
- facebook_archive_dashboard.py:89:except OSError:
- facebook_archive_dashboard.py:96:except OSError:
- facebook_archive_dashboard.py:124:if any(token in line.lower() for token in ("warning", "error", "failed", "unsuppor
- facebook_archive_dashboard.py:162:"ultimi warning/errori:",
- facebook_session_browser.py:71:for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
- facebook_session_browser.py:93:except Exception:
RISK:
- facebook_archive_dashboard.py:124:if any(token in line.lower() for token in ("warning", "error", "failed", "unsuppor
- facebook_session_browser.py:5:import http.cookiejar
- facebook_session_browser.py:17:DEFAULT_COOKIE_EXPORT = "~/.config/facebook-video-archiver/facebook-cookies.txt"
- facebook_session_browser.py:133:cookies = await context.cookies("https://www.facebook.com")
- facebook_session_browser.py:134:cookie_names = {cookie.get("name", "") for cookie in cookies}
- facebook_session_browser.py:135:if "c_user" in cookie_names or "xs" in cookie_names:
- facebook_session_browser.py:205:safe_print("Nessun URL trovato. Possibili limiti: cookie/sessione scaduti, checkpoin
- facebook_session_browser.py:339:def cookie_expires(cookie: dict) -> int:
- facebook_session_browser.py:340:expires = cookie.get("expires", -1)
- facebook_video_archiver.sh:24:FB_COOKIES_FILE="${FB_COOKIES_FILE:-}"
ROAD:
now=facebook_archive_dashboard.py:38:except OSError:
next=facebook_archive_dashboard.py:47:for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
later=facebook_archive_dashboard.py:62:lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
LINK:
meta=../../../facebook-video-archiver/dev/project.metadata.json
human=../../human/projects/facebook-video-archiver/overview.md
legacy=../../../facebook-video-archiver/dev/legacy
repo=../../../facebook-video-archiver
OPEN:
- no tests detected by static scan
