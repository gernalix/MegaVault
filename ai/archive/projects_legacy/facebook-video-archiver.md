META:
name=facebook-video-archiver
slug=facebook-video-archiver
path=/home/daniele/codex-workspace/facebook-video-archiver
remote=none
branch=work/v4-deep-discovery
verified_commit=ab0e526
verified_at=2026-06-01T13:59:53+02:00
protocol=MEGAVAULT_PROTOCOL.md:v2
PURPOSE:
purpose=Start here for Codex/operator work on `facebook-video-archiver`
STACK:
lang=Python,Shell
fw=Playwright
db=UNKNOWN
platform=UNKNOWN
tools=Chrome,yt-dlp
MAP:
entry=UNKNOWN
ui=UNKNOWN
core=dev/project.metadata.json,facebook_archive_dashboard.py,facebook_session_browser.py,systemd/user/facebook-video-archiver.service,systemd/user/facebook-video-archiver.timer
db=UNKNOWN
tests=UNKNOWN
scripts=facebook_video_archiver.sh
build=UNKNOWN
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
core=facebook_archive_dashboard.py:human_bytes,count_files_and_bytes,read_urls,recent_log,tail_lines,process_status
core=facebook_session_browser.py:expand,load_env_file,safe_print,normalize_facebook_url,read_existing_urls,write_deduped_urls
script=facebook_video_archiver.sh:usage,log,die,load_env,require_archive_mount,rel_or_abs
FLOW:
flow=script->facebook_video_archiver.sh=>dev/project.metadata.json
flow=facebook_archive_dashboard.py:8:from pathlib import Path
flow=facebook_archive_dashboard.py:49:if line and not line.startswith("#"):
flow=facebook_archive_dashboard.py:70:return "stopped", ""
INV:
arch=facebook_archive_dashboard.py:human_bytes,count_files_and_bytes,read_urls,recent_log,tail_lines; facebook_session_browser.py:expand,load_env_file,safe_print,normalize_facebook_url,read_existing_urls; facebook_video_archiver.sh:usage,log,...
data=dev/project.metadata.json:9:"metadata_version": 1,; facebook_session_browser.py:43:def safe_print(message: str) -> None:
ux=facebook_archive_dashboard.py:184:raise SystemExit(main()); facebook_session_browser.py:43:def safe_print(message: str) -> None:
backup=UNKNOWN
migration=UNKNOWN
version=dev/project.metadata.json:9:"metadata_version": 1,; facebook_video_archiver.sh:6:VERSION_FILE="$SCRIPT_DIR/VERSION"
i18n=UNKNOWN
security=facebook_video_archiver.sh:139:[[ "$FB_COOKIES_FILE" = "$SCRIPT_DIR"* ]] && die "FB_COOKIES_FILE must stay outside this repository."; facebook_video_archiver.sh:245:log "Conceptual yt-dlp command: yt-dlp <safe-options> $cookie_arg $mode...
perf=facebook_session_browser.py:123:await page.goto(args.page_url, wait_until="domcontentloaded", timeout=60000); facebook_session_browser.py:147:await page.goto(args.page_url, wait_until="domcontentloaded", timeout=60000)
BUILD:
files=UNKNOWN
cmd=UNKNOWN
TEST:
files=UNKNOWN
cmd=UNKNOWN
DATA:
db=systemd/user/facebook-video-archiver.timer:10:WantedBy=timers.target
paths=UNKNOWN
backup=UNKNOWN
restore=facebook_archive_dashboard.py:8:from pathlib import Path; facebook_session_browser.py:12:from pathlib import Path
import=facebook_archive_dashboard.py:8:from pathlib import Path; facebook_session_browser.py:12:from pathlib import Path
export=facebook_video_archiver.sh:47:./facebook_video_archiver.sh --export-session-cookies; facebook_video_archiver.sh:265:log "Dry-run limit: yt-dlp could not extract this source directly. Use --discover-page, authorized direct URLs in urls.tx...
migration=UNKNOWN
retention=UNKNOWN
DNB:
dnb=facebook_archive_dashboard.py:124:if any(token in line.lower() for token in ("warning", "error", "failed", "unsupported", "unable")):
dnb=preserve=dev/project.metadata.json,dev/legacy,AI/Human links; docs-only tasks must not touch app code/DB
BUG:
issue=UNKNOWN
RISK:
risk=facebook_archive_dashboard.py:124:if any(token in line.lower() for token in ("warning", "error", "failed", "unsupported", "unable")):
ROAD:
now=UNKNOWN
next=UNKNOWN
later=UNKNOWN
LINK:
meta=../../../facebook-video-archiver/dev/project.metadata.json
human=../../human/projects/facebook-video-archiver/overview.md
legacy=../../../facebook-video-archiver/dev/legacy
repo=../../../facebook-video-archiver
OPEN:
open=tests=UNKNOWN_OR_ABSENT
