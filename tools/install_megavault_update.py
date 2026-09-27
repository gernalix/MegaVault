#!/usr/bin/env python3
from __future__ import annotations

import os
import subprocess
from pathlib import Path

REPO = Path("/home/daniele/MegaVault")
UNIT_DIR = Path.home() / ".config" / "systemd" / "user"


def replace(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(text, encoding="utf-8")
    os.replace(temporary, path)


def main() -> int:
    updater = REPO / "tools" / "megavault_update.py"
    if not updater.is_file():
        raise SystemExit(f"updater_missing:{updater}")
    replace(
        UNIT_DIR / "megavault-canonical-update.service",
        f"""[Unit]
Description=Fail-closed canonical MegaVault update
After=network-online.target
Wants=network-online.target

[Service]
Type=oneshot
ExecStart=/usr/bin/python3 {updater}
WorkingDirectory={REPO}
ReadWritePaths={REPO} /home/daniele/.local/state/megavault
""",
    )
    replace(
        UNIT_DIR / "megavault-canonical-update.timer",
        """[Unit]
Description=Update canonical MegaVault automatically

[Timer]
OnBootSec=3m
OnUnitActiveSec=15m
RandomizedDelaySec=30s
Persistent=true
Unit=megavault-canonical-update.service

[Install]
WantedBy=timers.target
""",
    )
    subprocess.run(["systemctl", "--user", "daemon-reload"], check=True)
    subprocess.run(
        ["systemctl", "--user", "enable", "--now", "megavault-canonical-update.timer"],
        check=True,
    )
    print("status=installed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
