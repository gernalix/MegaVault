# grindr-web-exporter

META:
slug=grindr-web-exporter
prompt=739418
root=/home/daniele/codex-workspace/grindr-web-exporter
metadata=../../grindr-web-exporter/dev/project.metadata.json
status=MVP

PURPOSE:
purpose=local resumable Grindr Web chat exporter using Firefox session data and Playwright DOM scraping
privacy=local_only; no cookie/token printing; no upload services; debug artifacts local_sensitive

STACK:
lang=Python>=3.10
browser=Playwright Firefox persistent context
db=SQLite WAL
cli=grindr-export setup-check|scan-chats|export-one|export-all|resume|export-html|export-json|status

MAP:
cli=src/grindr_exporter/cli.py
browser=src/grindr_exporter/browser.py
dom=src/grindr_exporter/dom.py
db=src/grindr_exporter/db.py
media=src/grindr_exporter/media.py
exports=src/grindr_exporter/exporters.py
docs=README.md,docs/DATABASE.md

ARCH:
flow=Firefox_profile_copy->Playwright_page->DOM_extract->normalized_SQLite->JSON/HTML
resume=export_runs+progress_checkpoints+message_dedupe_hash
dedupe=chat_stable_key+direction+text+timestamp+relative_position+reply+type SHA256
missing_rule=latest visible scan flags absent prior chats/profiles as missing and blocked_or_deleted_inferred without deletion
media=http_https direct fetch via browser context; unsupported/protected marked failed/protected

FLOW:
setup=grindr-export setup-check
scan=grindr-export scan-chats
mvp=grindr-export export-one
all=grindr-export export-all
resume=grindr-export resume
exports=grindr-export export-json && grindr-export export-html

INV:
arch=src package CLI modules, no service
data=/home/ubuntu/sync_root/db/grindr_export.sqlite3 default on this host; exports/,media/,debug/,state/ gitignored
ux=stdout progress redacts chat names unless --show-sensitive
backup=UNKNOWN
migration=schema_meta schema_version=1
version=package 0.1.0; code first line # v1
i18n=timestamp parser handles English/Italian Today/Yesterday labels partially
security=browser cookies never printed; debug HTML/screenshots local sensitive; protected media not bypassed
perf=incremental duplicate threshold stops long known histories

BUILD:
cmd=python3 -m venv .venv && . .venv/bin/activate && python -m pip install -e '.[test]' && python -m playwright install firefox

TEST:
static=PYTHONPATH=src python -m py_compile src/grindr_exporter/*.py tests/*.py PASS 2026-06-18
unit=PYTHONPATH=src python -m pytest -q PASS 3 2026-06-18
real=setup-check reached https://web.grindr.com/chat but source_grindr_cookie_count=0 and visible_chat_candidates=0; no export-one real chat possible until authenticated session exists

DATA:
db=/home/ubuntu/sync_root/db/grindr_export.sqlite3
paths=exports/,media/,debug/,state/,logs/ gitignored
backup=UNKNOWN
restore=rerun from DB plus profile copy; no destructive cleanup
import=none
export=JSON+HTML
migration=manual future schema migrations
retention=operator-managed

DNB:
dnb=do not commit DB/media/debug/profile/cookies
dnb=do not print message text or identifiers unless explicitly requested
dnb=do not bypass protected albums or anti-screenshot protections
dnb=do not delete existing chat/profile/message rows when absent from latest scan

BUG:
bug=Grindr DOM is not contractual; selectors are heuristic and require real-page validation after login
bug=Firefox default profile currently has 0 Grindr cookies on 2026-06-18

RISK:
risk=debug artifacts contain sensitive local HTML/screenshots
risk=media URLs may be signed/short-lived and fail despite visibility
risk=direction/delivered/read inference depends on DOM labels/classes

ROAD:
next=run grindr-export --profile-mode persistent-copy --pause-for-login setup-check
next=run export-one on authenticated visible chat and refine selectors from local debug artifacts
next=add sanitized DOM fixtures

LINK:
readme=../../grindr-web-exporter/README.md
dbdoc=../../grindr-web-exporter/docs/DATABASE.md
metadata=../../grindr-web-exporter/dev/project.metadata.json

OPEN:
open=authenticated real chat export not validated because no Grindr cookies/session were present in Firefox profile
open=remote Git push not performed; repo has no origin and exporter is local/sensitive until operator approves publication
