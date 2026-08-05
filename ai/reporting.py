#!/usr/bin/env python3
"""Central completion gateway for Codex task reports.

Projects call this module by absolute path. Telegram transport remains owned by
``telegram_notify``; MegaVault only enforces the common reporting workflow.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def finish_task(
    plain_report: str,
    technical_report: str,
    *,
    prompt_id: str | int | None = None,
    title: str = "Codex Report",
    chat_id: str | int | None = None,
) -> dict[str, object]:
    """Deliver paired reports through the shared Telegram library."""
    from telegram_notify import send_task_reports

    return send_task_reports(
        plain_report,
        technical_report,
        title=title,
        prompt_id=prompt_id,
        chat_id=chat_id,
    )


def finish_task_files(
    plain_path: str | Path,
    technical_path: str | Path,
    *,
    prompt_id: str | int | None = None,
    title: str = "Codex Report",
    chat_id: str | int | None = None,
) -> dict[str, object]:
    """Read UTF-8 report files and deliver them."""
    plain = Path(plain_path).read_text(encoding="utf-8")
    technical = Path(technical_path).read_text(encoding="utf-8")
    return finish_task(
        plain,
        technical,
        prompt_id=prompt_id,
        title=title,
        chat_id=chat_id,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Invia il report semplice e quello tecnico tramite telegram_notify."
    )
    parser.add_argument("--plain-file", required=True, help="FINAL_REPORT_PLAIN.txt")
    parser.add_argument("--technical-file", required=True, help="FINAL_REPORT_TECHNICAL.txt")
    parser.add_argument("--prompt-id", default=None)
    parser.add_argument("--title", default="Codex Report")
    parser.add_argument("--chat-id", default=None)
    args = parser.parse_args(argv)

    try:
        result = finish_task_files(
            args.plain_file,
            args.technical_file,
            prompt_id=args.prompt_id,
            title=args.title,
            chat_id=args.chat_id,
        )
    except Exception as exc:
        print(
            f"TELEGRAM_NOTIFICATION=FAIL error={type(exc).__name__}: {exc}",
            file=sys.stderr,
        )
        return 1

    print("TELEGRAM_NOTIFICATION=PASS")
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
