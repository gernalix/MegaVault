META:
name=linux-mint-service-dashboard
slug=linux-mint-service-dashboard
path=/home/daniele/codex-workspace/linux-mint-service-dashboard
remote=none
branch=prompt-816-local-dashboard
verified_commit=487ca7e
verified_at=2026-06-01T13:59:53+02:00
protocol=MEGAVAULT_PROTOCOL.md:v2
PURPOSE:
purpose=Dashboard locale read-only per i servizi operativi importanti di questo host Linux Mint/XFCE
STACK:
lang=JS/TS,Python
fw=Playwright
db=SQLite
platform=UNKNOWN
tools=Uptime Kuma,restic,systemd
MAP:
entry=app/server.py
ui=app/static/app.js,app/static/index.html,app/static/styles.css
core=app/__init__.py,app/collectors.py,dev/project.metadata.json,launchers/linux-mint-service-dashboard.desktop,systemd/system-service-dashboard.service
db=UNKNOWN
tests=tests/playwright-smoke.js,tests/test_dashboard.py
scripts=UNKNOWN
build=UNKNOWN
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
entry=app/server.py:DashboardHandler,parse_args,main
core=app/collectors.py:CommandResult,now_local,iso_now,display_now,version,redact_text,collect_freeze_forensics,freeze_forensics_service_from_payload
ui=app/static/app.js:escapeHtml,statusClass,scalar,renderOverview,statCard,renderTabs,renderFreezePanel
test=tests/playwright-smoke.js:URL,VIEWPORTS,browser,errors,page,tabs
test=tests/test_dashboard.py:DashboardTests
FLOW:
flow=entry->app/server.py=>app/__init__.py
flow=app/server.py:10:from http import HTTPStatus
flow=launchers/linux-mint-service-dashboard.desktop:9:StartupNotify=false
flow=systemd/system-service-dashboard.service:9:ExecStart=/usr/bin/python3 /home/daniele/codex-workspace/linux-mint-service-dashboard/app/server.py --host 127.0.0.1 --port 8788
flow_freeze=collect_all->collect_freeze_forensics->mint-freeze-forensics dashboard-json->renderFreezePanel
flow_rsync=collect_rsync_transfer->unit_show(rsync-transfer.service user)->mount_info filters root/autofs wrappers->stale throughput hidden when no live rsync
INV:
arch=app/server.py:DashboardHandler,parse_args,main; app/collectors.py:CommandResult,now_local,iso_now,display_now,version; app/static/app.js:escapeHtml,statusClass,scalar,renderOverview,statCard; tests/playwright-smoke.js:URL,VIEWPORTS,brows...
data=app/server.py:80:self.send_json({"status": "ok", "version": version(), "refresh_display": display_now(), "read_only": True}); dev/project.metadata.json:9:"metadata_version": 1,
ux=app/server.py:26:server_version = f"LinuxMintServiceDashboard/{version()}"; app/server.py:116:parser = argparse.ArgumentParser(description="Linux Mint local read-only service dashboard"); freeze tab plain-language state/24h/7d/explanation/safe command-copy buttons
backup=UNKNOWN
migration=UNKNOWN
version=app/server.py:18:from app.collectors import collect_all, display_now, redact_text, version; app/server.py:26:server_version = f"LinuxMintServiceDashboard/{version()}"
i18n=UNKNOWN
security=tests/test_dashboard.py:27:self.assertNotIn("super-token", cleaned); tests/test_dashboard.py:29:self.assertNotIn("bucket/key", cleaned)
perf=app/collectors.py:44:r"error|failed|fail|warning|warn|critical|blocked|stalled|corrupt|I/O|input/output|timeout|degraded|"; app/collectors.py:45:r"storage|lock|TRUE_PRE_EMERGENCY|PRE_EMERGENCY|abort|skipped",
BUILD:
files=UNKNOWN
cmd=UNKNOWN
TEST:
files=tests/playwright-smoke.js,tests/test_dashboard.py
cmd=UNKNOWN
DATA:
db=DB=SQLite
paths=UNKNOWN
backup=UNKNOWN
restore=app/server.py:10:from http import HTTPStatus; app/server.py:11:from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import=app/server.py:10:from http import HTTPStatus; app/server.py:11:from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
export=app/static/app.js:36:const compact = JSON.stringify(value);; app/static/app.js:218:const data = await response.json();
migration=UNKNOWN
retention=UNKNOWN
DNB:
dnb=app/server.py:58:"trace": redact_text(traceback.format_exc(limit=3)),
dnb=app/collectors.py:24:SECRET_PATTERNS = [
dnb=app/collectors.py:26:re.compile(r"((?:token|secret|password|passwd|api[_-]?key|key|restic_password|b2_account_key|aws_secret_access_key|kuma_push_url)\s*[=:]\s*)[^\s\"']+", re.I),
dnb=app/collectors.py:44:r"error|failed|fail|warning|warn|critical|blocked|stalled|corrupt|I/O|input/output|timeout|degraded|"
dnb=app/collectors.py:45:r"storage|lock|TRUE_PRE_EMERGENCY|PRE_EMERGENCY|abort|skipped",
dnb=app/collectors.py:77:for pattern in SECRET_PATTERNS:
dnb=preserve=dev/project.metadata.json,dev/legacy,AI/Human links; docs-only tasks must not touch app code/DB
dnb=freeze tab reads mint-freeze-forensics dashboard-json; must not duplicate freeze scoring or execute kill/restart/remediation
dnb=rsync tab must not report root mount or systemd-1 autofs wrapper as real source/destination; must not display stale progress speed as current throughput
BUG:
issue=app/collectors.py:44:r"error|failed|fail|warning|warn|critical|blocked|stalled|corrupt|I/O|input/output|timeout|degraded|"
issue=tests/test_dashboard.py:104:last_error: Exception | None = None
issue=tests/test_dashboard.py:112:last_error = exc
issue=tests/test_dashboard.py:114:raise AssertionError(f"server did not answer: {last_error}")
issue=2026-06-10 rsync tab showed service=rsync-transfer.service while unit was absent and reused stale throughput; fix=created static manual unit and filtered mount_info root/autofs plus stale throughput
RISK:
risk=app/server.py:58:"trace": redact_text(traceback.format_exc(limit=3)),
risk=app/collectors.py:24:SECRET_PATTERNS = [
risk=app/collectors.py:26:re.compile(r"((?:token|secret|password|passwd|api[_-]?key|key|restic_password|b2_account_key|aws_secret_access_key|kuma_push_url)\s*[=:]\s*)[^\s\"']+", re.I),
risk=app/collectors.py:44:r"error|failed|fail|warning|warn|critical|blocked|stalled|corrupt|I/O|input/output|timeout|degraded|"
risk=app/collectors.py:45:r"storage|lock|TRUE_PRE_EMERGENCY|PRE_EMERGENCY|abort|skipped",
risk=app/collectors.py:77:for pattern in SECRET_PATTERNS:
ops=dashboard service system-service-dashboard.service user ExecStart=/usr/bin/python3 /home/daniele/codex-workspace/linux-mint-service-dashboard/app/server.py --host 127.0.0.1 --port 8788
ops_rsync=dashboard rsync tab service field now resolves loaded/static rsync-transfer.service; unit=/home/daniele/.config/systemd/user/rsync-transfer.service; runner=/home/daniele/.local/bin/rsync-transfer-runner; manual_start=/home/daniele/.local/bin/rsync-transfer-start
test_2026-06-10=python3 -m unittest tests/test_dashboard.py OK; API rsync service loaded/static inactive/dead, source mounted false root/autofs ignored, destination /dev/sdc1 ext4, throughput stale
ROAD:
now=Freeze / Rallentamenti tab integrated with mint-freeze-forensics
next=review wording after >=3 real freeze events
later=UNKNOWN
LINK:
meta=../../../linux-mint-service-dashboard/dev/project.metadata.json
human=../../human/projects/linux-mint-service-dashboard/overview.md
report_custom_services=../../human/system/custom-services-status.md
legacy=../../../linux-mint-service-dashboard/dev/legacy
repo=../../../linux-mint-service-dashboard
OPEN:
open=none
