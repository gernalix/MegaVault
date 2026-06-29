META:
name=Strano Anello
slug=strano-anello
path=/home/ubuntu/bots/strano_anello
remote=https://github.com/gernalix/strano-anello.git
branch=main
metadata=dev/project.metadata.json
verified_commit=311b1f94427761d36c9466c507811f515f4c61be
verified_at=2026-06-29T15:37:05Z
protocol=MEGAVAULT_PROTOCOL.md:v3
PURPOSE:
purpose=WordPress watcher for lostranoanello.wordpress.com posts/comments; persists current normalized post/comment state; notifies Telegram on inserts/edits/deletes.
STACK:
lang=Python 3.10
deps=requests,beautifulsoup4
db=SQLite
runtime=systemd oneshot+timer
platform=Oracle VM ubuntu@150.230.148.128
MAP:
entry=strano_anello.py
ui=none
core=strano_anello.py:fetch_all_posts,extract_comments_from_post_html,apply_snapshots,store_comment_diagnostic
db=/home/ubuntu/db/strano_anello.db
tests=tests/test_strano_db.py
scripts=tools/strano_db_maintenance.py
service=strano-anello.service,strano-anello.timer
avoid=data,logs,comments,posts,diff,.venv,*.db,*.sqlite*,backups
ARCH:
component=watcher fetches WordPress REST posts and per-post HTML comments.
component=state tables watcher_posts/watcher_comments keep current canonical entities.
component=events table watcher_events stores only content/status change notifications.
component=diagnostics watcher_comment_diagnostics stores latest useful diagnostic per candidate_hash only.
component=maintenance CLI analyzes size, growth, duplicates, anomalies, compact.
boundary=Markdown snapshots under data/ are generated runtime artifacts, not repo source.
FLOW:
run=systemd timer -> strano_anello.py --auto 1 -> fetch posts -> fetch comments -> apply snapshots -> write markdown -> commit DB -> health.json.
diagnostics=extract all candidates in memory; persist only rejected/warning/low-confidence; upsert by candidate_hash; prune by retention/max rows.
notify=Telegram only for non-baseline events and repeated failures/recovery.
maintenance=tools/strano_db_maintenance.py compact creates backup, filtered compact DB, integrity_check, replace.
INV:
data=watcher_posts.post_id unique; watcher_comments.comment_id unique; URL unique for posts/comments.
data=watcher_comment_diagnostics must stay bounded; no per-run clean accepted candidate rows.
data=diagnostics unique by candidate_hash; latest row updated on repeated anomaly.
data=do not delete watcher_posts, watcher_comments, watcher_events during compaction.
backup=backup before real DB mutation; 2026-06-29 backup zstd tested at /var/lib/oracle_backup/manual_db_backups/strano_anello.pre-maintenance-20260629T145430Z.db.zst.
migration=db_init idempotent; schema_version state=2.
perf=DB anomaly threshold 100MiB; diagnostics_rows threshold 200000.
version=repo branch main.
security=Telegram tokens/helper contents not documented; do not commit DB/logs/data.
BUILD:
cmd=python3 -m py_compile strano_anello.py tools/strano_db_maintenance.py tests/test_strano_db.py
env=venv at /home/ubuntu/bots/strano_anello/.venv
requirements=requirements-strano-anello.txt
TEST:
unit=.venv/bin/python -m unittest discover -s tests -v
smoke=sudo systemctl start strano-anello.service; check journal for Run ok
maintenance=.venv/bin/python tools/strano_db_maintenance.py anomalies --max-db-bytes 104857600 --max-wal-bytes 67108864 --max-diagnostic-rows 200000
DATA:
DB=SQLite
Path=/home/ubuntu/db/strano_anello.db
Schema=watcher_runs,watcher_state,watcher_posts,watcher_comments,watcher_events,watcher_comment_diagnostics,watcher_db_size_history,legacy sa_*
Before=2026-06-29 db=6576418816 wal=10683192 page_size=4096 page_count=1605571 freelist=0 journal=wal diagnostics_seq=14693332
After=2026-06-29 db=2351104 wal=0 shm=32768 page_size=4096 page_count=574 freelist=0 journal=wal diagnostics_rows=102
Largest_before=watcher_comment_diagnostics 6573776896 bytes; next watcher_comments 1179648 bytes.
Columns_before=diagnostics text bytes: permalink_url=1322641205, post_url=1137318944, candidate_hash=940373248, candidate_selector=514266620, date_raw=274261100, date_source=249656686, content_source=235093312, author_name=187302204.
Backup=/var/lib/oracle_backup/manual_db_backups/strano_anello.pre-maintenance-20260629T145430Z.db.zst
Restore=zstd -d backup.zst -o /home/ubuntu/db/strano_anello.restore.db; stop timer/service before replacing live DB.
Import=none
Export=markdown snapshots generated under data/posts,data/comments; not source.
Migration=db_init creates watcher_db_size_history and diagnostics indexes.
Retention=diagnostics useful-only, unique candidate_hash, max rows STRANO_DIAGNOSTIC_MAX_ROWS default 50000, retention days default 7.
DNB:
dnb=Do not reintroduce per-run INSERT of every clean comment candidate.
dnb=Do not commit data/, logs/, *.db, *.sqlite*, backups/.
dnb=Stop strano-anello.timer before live DB compaction/replacement.
dnb=Restart datasette after replacing DB to release old open SQLite inode.
dnb=Keep backup external and compact; MegaVault stores only summary.
BUG:
issue=DB grew to 6.2GiB despite text-only purpose.
cause=watcher_comment_diagnostics stored every comment candidate every 10 minutes; 1358 rows/run; 14693332 diagnostic rows; no retention/dedup.
resolved=2026-06-29 runtime useful-only diagnostics + candidate_hash upsert + retention + maintenance compact.
workaround=none; run anomalies monitor if size exceeds 100MiB.
RISK:
risk=Full PRAGMA integrity_check on bloated 6.2GiB source was too slow on VM I/O; compact path uses backup + source quick/optional check + final compact integrity_check.
risk=Datasette can hold deleted old DB inode after replacement; restart datasette to free disk.
risk=Backup zst is 161MiB under /var/lib/oracle_backup/manual_db_backups; track manually, not MegaVault.
ROAD:
now=Monitor next timer runs for diagnostics_rows stable near 102.
next=Add periodic anomaly command to backup/healthcheck if desired.
later=Consider removing legacy sa_* tables only after explicit data-ownership review.
LINK:
meta=https://github.com/gernalix/strano-anello/blob/main/dev/project.metadata.json
human=../../human/projects/strano-anello/overview.md
legacy=UNKNOWN
repo=https://github.com/gernalix/strano-anello
OPEN:
open=No GitHub CI configured.
open=Legacy sa_* tables preserved; relationship to current watcher retained for compatibility.
open=No automated scheduled maintenance unit yet; CLI exists.
