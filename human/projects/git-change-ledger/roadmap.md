# git-change-ledger Roadmap

## Now

- Local manual CLI.
- SQLite DB under `/home/daniele/sync_root/db/git_change_ledger.sqlite3`.
- Global command symlink in `/home/daniele/.local/bin/git-change-ledger`.
- Report for dirty repos, unpushed commits, large changed files, secret-like paths, missing remotes, and MegaVault doc candidates.

## Next

- Add a retention/vacuum command if the append-only scan history grows too much.
- Add JSON or CSV export only if another local tool needs it.

## Later

- Install and enable the provided user timer only after explicit operator request.

