#!/usr/bin/env python3
"""Emit a secret-free JSON snapshot of installed systemd timers."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path


PROPERTIES = (
    "Id,LoadState,ActiveState,SubState,UnitFileState,FragmentPath,Triggers,"
    "LastTriggerUSec,NextElapseUSecRealtime"
)
SERVICE_PROPERTIES = "Id,LoadState,ActiveState,SubState,Result,ExecMainStatus,FragmentPath"


def run_systemctl(scope: str, *args: str) -> str:
    command = ["systemctl"]
    if scope == "user":
        command.append("--user")
    command.extend(args)
    result = subprocess.run(command, text=True, capture_output=True, timeout=30, check=False)
    if result.returncode:
        raise RuntimeError(result.stderr.strip().splitlines()[-1] or "systemctl failed")
    return result.stdout


def properties(scope: str, unit: str, names: str) -> dict[str, str]:
    output = run_systemctl(scope, "show", unit, f"--property={names}", "--no-pager")
    return dict(line.split("=", 1) for line in output.splitlines() if "=" in line)


def file_evidence(path_text: str) -> dict[str, object]:
    path = Path(path_text)
    try:
        data = path.read_bytes()
    except (OSError, ValueError):
        return {"path": path_text, "sha256": None, "line_start": None, "line_end": None}
    return {
        "path": str(path),
        "sha256": hashlib.sha256(data).hexdigest(),
        "line_start": 1,
        "line_end": len(data.splitlines()) or 1,
    }


def snapshot_scope(scope: str) -> list[dict[str, object]]:
    output = run_systemctl(scope, "list-unit-files", "--type=timer", "--no-legend", "--no-pager")
    units = sorted({
        line.split()[0] for line in output.splitlines()
        if line.strip() and line.split()[0].endswith(".timer") and not line.split()[0].endswith("@.timer")
    })
    rows: list[dict[str, object]] = []
    for timer in units:
        timer_props = properties(scope, timer, PROPERTIES)
        triggers = [item for item in timer_props.get("Triggers", "").split() if item.endswith(".service")]
        service = triggers[0] if len(triggers) == 1 else timer.removesuffix(".timer") + ".service"
        service_props = properties(scope, service, SERVICE_PROPERTIES)
        timer_source = file_evidence(timer_props.get("FragmentPath", ""))
        service_source = file_evidence(service_props.get("FragmentPath", ""))
        rows.append({
            "scope": scope,
            "timer_unit": timer,
            "service_unit": service,
            "enabled_state": timer_props.get("UnitFileState") or "unknown",
            "active_state": timer_props.get("ActiveState") or "unknown",
            "sub_state": timer_props.get("SubState") or "unknown",
            "last_trigger": timer_props.get("LastTriggerUSec") or None,
            "next_trigger": timer_props.get("NextElapseUSecRealtime") or None,
            "service_active_state": service_props.get("ActiveState") or "unknown",
            "service_result": service_props.get("Result") or "unknown",
            "service_exec_status": service_props.get("ExecMainStatus") or None,
            "timer_source": timer_source,
            "service_source": service_source,
        })
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scope", choices=("system", "user", "all"), default="system")
    args = parser.parse_args()
    scopes = ("system", "user") if args.scope == "all" else (args.scope,)
    rows = [row for scope in scopes for row in snapshot_scope(scope)]
    print(json.dumps({"schema": 1, "timers": rows}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
