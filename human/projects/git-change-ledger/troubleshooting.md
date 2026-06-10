# git-change-ledger Troubleshooting

## `doctor` reports missing symlink

Run:

```bash
ln -sfn /home/daniele/codex-workspace/git-change-ledger/git-change-ledger.sh /home/daniele/.local/bin/git-change-ledger
```

## Scan Takes Too Long

Use a limit or shorter timeout:

```bash
git-change-ledger scan --limit 10 --timeout 10
```

## DB Missing

Run a real scan or doctor:

```bash
git-change-ledger doctor
git-change-ledger scan --limit 5
```

The database must be:

```text
/home/daniele/sync_root/db/git_change_ledger.sqlite3
```

## Full Diff Needed For One Repo

Use the explicit command only when needed:

```bash
git-change-ledger diff /home/daniele/codex-workspace/PROJECT HEAD~1..HEAD
```

Normal scans do not store that output.

