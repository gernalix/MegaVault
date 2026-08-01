# git-change-ledger

`git-change-ledger` is a local command that records the Git state of projects under `/home/daniele/codex-workspace` into one SQLite database:

```text
/home/daniele/sync_root/db/git_change_ledger.sqlite3
```

It is designed for low overhead: no daemon, no continuous loop, no automatic fetch, no full diff storage, per-repo timeout, cache skip, and a configurable repo limit.

## Main Commands

```bash
git-change-ledger scan
git-change-ledger status
git-change-ledger repo-list
git-change-ledger dirty
git-change-ledger recent
git-change-ledger report
git-change-ledger doctor
```

The report highlights dirty repos, local commits not pushed, large changed files, secret-like changed paths, repos without remotes, and repos whose MegaVault docs may need updates.

## Safety Notes

- The scan does not change other repositories.
- The scan does not fetch from remotes.
- The scan stores `git diff --stat`, not full patches.
- A disabled-by-default systemd user timer template exists in the repo but was not installed or enabled.

## Links

- AI doc: ../../../ai/projects/git-change-ledger.md (`../../../ai/projects/git-change-ledger.md`; status=UNKNOWN)
- Metadata: ../../../../git-change-ledger/dev/project.metadata.json (`../../../../git-change-ledger/dev/project.metadata.json`; status=UNKNOWN)
- Repo: ../../../../git-change-ledger (`../../../../git-change-ledger`; status=UNKNOWN)
- Legacy docs: none
