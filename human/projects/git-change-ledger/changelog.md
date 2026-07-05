# git-change-ledger Changelog

## 2026-06-10

- Created local project `/home/daniele/codex-workspace/git-change-ledger`.
- Added Bash CLI with SQLite schema and commands `scan`, `status`, `repo-list`, `dirty`, `recent`, `report`, `doctor`, and explicit `diff`.
- Added DB path `/home/daniele/sync_root/db/git_change_ledger.sqlite3`.
- Added global command symlink target `/home/daniele/.local/bin/git-change-ledger`.
- Added disabled-by-default user systemd service/timer templates.
- Created private GitHub remote `git@github.com:gernalix/git-change-ledger.git` and pushed `main`.
- Verified full scan on 27 repos: 26 cache hits, 15 dirty repos, 38.45s elapsed, 13 MB max RSS, DB 148K, no `diff --git` markers stored.
