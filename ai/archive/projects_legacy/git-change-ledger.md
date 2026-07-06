META:
name=git-change-ledger
slug=git-change-ledger
path=/home/daniele/codex-workspace/git-change-ledger
remote=git@github.com:gernalix/git-change-ledger.git
branch=main
verified_commit=edbc8857e3ca5abee55539f40abcba728f75f5e7
verified_at=2026-06-10T19:44:00+02:00
protocol=MEGAVAULT_PROTOCOL.md:v8
PURPOSE:
purpose=Local lightweight Git state ledger for repos under `/home/daniele/codex-workspace`, stored in one SQLite DB without full diffs.
STACK:
lang=Bash
db=SQLite WAL
tools=git,sqlite3,find,timeout,flock,sha256sum,stat
platform=Linux Mint workstation
MAP:
entry=git-change-ledger.sh
core=scan/status/repo-list/dirty/recent/report/doctor/diff command handlers
db=/home/daniele/sync_root/db/git_change_ledger.sqlite3
systemd_template=systemd/user/git-change-ledger.service,systemd/user/git-change-ledger.timer disabled_by_default
docs=README.md,dev/project.metadata.json,MegaVault ai/human project docs
avoid=other_project_code,automatic_fetch,daemon_loop,Kuma_monitor,full_diff_storage
ARCH:
discovery=find `$GCL_ROOT` for `.git` dirs with prune list for heavy paths
scan=per_repo timeout git metadata/status/log/diff_stat only
cache=skip heavy work when branch+HEAD+working_tree_fingerprint unchanged
storage=SQLite tables scan_runs,repos,repo_scans,changed_files,recent_commits,schema_meta
report=dirty repos,unpushed commits,large changed files,secret-like changed paths,repos without remote,MegaVault docs candidates
FLOW:
normal=git-change-ledger scan -> discover repos -> lock -> collect git metadata -> upsert DB -> report summary
dry_run=scan --dry-run -> discover+inspect -> print summary -> no DB writes
status=status/repo-list/dirty/recent/report read SQLite only
explicit_diff=diff REPO [REF] prints full diff to stdout only; never part of normal scan
INV:
data=DB path fixed `/home/daniele/sync_root/db/git_change_ledger.sqlite3`
data=normal scan stores no full diffs or file contents
perf=no daemon,no loop,no fetch,per-repo timeout,configurable repo limit,cache skip
security=secret detection is path/stat-name heuristic only; no sensitive file content reads
ops=global symlink `/home/daniele/.local/bin/git-change-ledger`
ops=systemd timer template exists but is not installed/enabled by this patch
BUILD:
cmd=bash -n git-change-ledger.sh
requirements=bash,git,sqlite3,find,timeout,flock,sha256sum,stat
install=chmod +x git-change-ledger.sh; ln -sfn repo script to /home/daniele/.local/bin/git-change-ledger
TEST:
syntax=bash -n git-change-ledger.sh
doctor=git-change-ledger doctor
dry_run=git-change-ledger scan --dry-run
scan=git-change-ledger scan --limit N
status=git-change-ledger status
dirty=git-change-ledger dirty
db_verify=test -f /home/daniele/sync_root/db/git_change_ledger.sqlite3; sqlite3 schema/table checks
result_2026-06-10=bash_n PASS; doctor PASS; dry_run_limit5 PASS; full_scan PASS scan_id=3 repos=27 skipped_cache=26 dirty=15 elapsed=38.45s maxrss=13068KB; status/dirty/repo-list/recent/report PASS; diff_git_markers=0
DATA:
DB=/home/daniele/sync_root/db/git_change_ledger.sqlite3
Schema=scan_runs,repos,repo_scans,changed_files,recent_commits,schema_meta
DBSize_2026-06-10=148K after scan_id=3
Backup=external sync_root policy only; script does not copy DB
Restore=rerun scan from live repos
Import=none
Export=sqlite queries/report output
Migration=additive schema via CREATE TABLE IF NOT EXISTS
Retention=none yet; scan rows append, recent_commits current per repo
DNB:
dnb=do not modify code in scanned repos
dnb=do not run git fetch automatically
dnb=do not store full diffs by default
dnb=do not create Kuma monitor in this patch
dnb=do not enable timer unless operator explicitly asks
dnb=do not scan outside `/home/daniele/codex-workspace` unless GCL_ROOT override is intentional
BUG:
issue=none known at creation
RISK:
risk=large number of dirty files can make status/path rows large; mitigation=timeout,limit,cache,stat byte cap
risk=SQLite DB grows over time; mitigation=future retention/vacuum command if needed
risk=worktrees with `.git` file are not discovered; mitigation=documented limit
risk=path-based secret hints can false-positive/false-negative; mitigation=no content reads, report as potential only
ROAD:
now=create local CLI,DB,docs,global symlink,manual scans
next=add retention/vacuum command if DB growth becomes material
later=optional disabled user timer install if operator requests scheduled scans
LINK:
meta=../../../git-change-ledger/dev/project.metadata.json
human=../../human/projects/git-change-ledger/overview.md
repo=../../../git-change-ledger
legacy=none
OPEN:
open=none
