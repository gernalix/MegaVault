#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import subprocess
from pathlib import Path

DEFAULT_REPO = Path.home() / "MegaVault"
DEFAULT_UNIT_DIR = Path.home() / ".config" / "systemd" / "user"


def run(args: list[str]) -> None:
    subprocess.run(args, check=True)


def write_unit(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(content, encoding="utf-8")
    os.replace(tmp, path)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Install the local MegaVault PROMPT_ID fallback worker as a user systemd timer."
    )
    parser.add_argument("--repo", type=Path, default=DEFAULT_REPO)
    parser.add_argument("--interval-seconds", type=int, default=15)
    args = parser.parse_args(argv)

    repo = args.repo.expanduser().resolve()
    worker = repo / "tools" / "prompt_id_local_worker.py"
    if not worker.is_file():
        raise SystemExit(f"worker_missing:{worker}")
    interval = max(10, int(args.interval_seconds))

    service = DEFAULT_UNIT_DIR / "megavault-prompt-id-worker.service"
    timer = DEFAULT_UNIT_DIR / "megavault-prompt-id-worker.timer"

    write_unit(
        service,
        f"""[Unit]
Description=MegaVault PROMPT_ID local fallback worker
After=network-online.target
Wants=network-online.target

[Service]
Type=oneshot
ExecStart=/usr/bin/python3 {worker}
WorkingDirectory={repo}
""",
    )
    write_unit(
        timer,
        f"""[Unit]
Description=Run MegaVault PROMPT_ID fallback worker

[Timer]
OnBootSec=15s
OnUnitActiveSec={interval}s
AccuracySec=1s
Persistent=true
Unit=megavault-prompt-id-worker.service

[Install]
WantedBy=timers.target
""",
    )

    run(["systemctl", "--user", "daemon-reload"])
    run(["systemctl", "--user", "enable", "--now", "megavault-prompt-id-worker.timer"])
    run(["systemctl", "--user", "start", "megavault-prompt-id-worker.service"])
    print(f"service={service}")
    print(f"timer={timer}")
    print("status=installed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
