# Mint Update Tracker

## Overview

Mint Update Tracker is a read-only software audit service. It records package
installations, updates, downgrades and removals, then keeps periodic full
snapshots of the installed software inventory.

Each host uses its own local SQLite database:

```text
/home/ubuntu/sync_root/db/software_audit.db
```

The Mint desktop and the Oracle Ubuntu VM may use the same path, but they are
independent files on independent machines. The service does not use shared
SQLite, NFS, SMB or network database writes.

## Features

- Backfills historical events from apt, dpkg and Mint update logs.
- Reads snap and flatpak history when available.
- Captures full inventory snapshots for apt/dpkg, snap, flatpak, pip, pipx,
  npm global, AppImage, gem and cargo when those managers exist.
- Skips absent optional managers with warnings instead of failing.
- Stores host identity, hostname, OS name and OS version on each event.
- Uses SQLite WAL, foreign keys, indexes, unique event hashes and safe vacuum.
- Provides `status`, `verify`, `backfill`, `recent`, `export-csv` and `vacuum`.

## Mint Desktop Install

Use user-level systemd:

```bash
cd /home/daniele/codex-workspace/mint-update-tracker
mkdir -p ~/.config/systemd/user
cp systemd/user/mint-update-tracker*.service systemd/user/mint-update-tracker.timer ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable --now mint-update-tracker.service mint-update-tracker.timer
./mint_update_tracker.py verify
```

## Oracle Ubuntu Server Install

Use system-level systemd so the recorder works without a graphical session or
active user login:

```bash
cd /home/daniele/codex-workspace/mint-update-tracker
sudo cp systemd/system/software-audit*.service systemd/system/software-audit-backfill.timer /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now software-audit.service software-audit-backfill.timer
./mint_update_tracker.py verify
```

If the project is deployed at a different path on Oracle, adjust `WorkingDirectory`
and `ExecStart` in the system unit before enabling it.

## Roadmap

- Install and verify the user service on Mint.
- Deploy the same code on Oracle with the system service and its own local DB.
- Add export/import aggregation only as a separate future workflow.

## Changelog

- v2: adds full snapshots, multi-manager inventory, host/OS metadata, daemon
  heartbeat, watchdog-aware systemd units, `verify`, `backfill`, `vacuum`, and
  headless/server test coverage.
- v1: apt/dpkg/Mint update event tracker with periodic scan timer.

## Troubleshooting

- `verify` reports SQLite integrity, watchdog state, heartbeat and log coverage.
- Missing snap, flatpak, pipx or npm is normal on server hosts; check
  `logs/mint_update_tracker.log` for `optional_managers_absent`.
- If DB locks are temporary, rerun `verify`; the app uses busy timeout and
  bounded retry.
- If logs were rotated, run `./mint_update_tracker.py backfill`; imports are
  idempotent.
