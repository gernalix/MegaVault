#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class ExpectedIdentity:
    manufacturer: str
    model: str


TARGETS = {
    "pixel": ExpectedIdentity("Google", "Pixel 8a"),
    "pixel8a": ExpectedIdentity("Google", "Pixel 8a"),
    "tcl": ExpectedIdentity("TCL", "6102H"),
    "tcl6102h": ExpectedIdentity("TCL", "6102H"),
}

Runner = Callable[[list[str]], subprocess.CompletedProcess[str]]


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    adb = shutil.which("adb")
    if not adb:
        return subprocess.CompletedProcess(args, 127, "", "adb_not_found")
    try:
        return subprocess.run([adb, *args], text=True, capture_output=True, check=False, timeout=20)
    except subprocess.TimeoutExpired as exc:
        return subprocess.CompletedProcess(args, 124, exc.stdout or "", "adb_timeout")


def parse_devices(raw: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for line in raw.splitlines():
        if not line.strip() or line.startswith("List of devices attached"):
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        attrs: dict[str, str] = {}
        for item in parts[2:]:
            if ":" in item:
                key, value = item.split(":", 1)
                if key != "transport_id":
                    attrs[key] = value
        rows.append({
            "serial": parts[0],
            "state": parts[1],
            "model_hint": attrs.get("model", ""),
        })
    return rows


def adb_text(runner: Runner, serial: str, *args: str) -> tuple[bool, str]:
    result = runner(["-s", serial, *args])
    return result.returncode == 0, (result.stdout or "").strip()


def read_identity(runner: Runner, serial: str) -> tuple[bool, dict[str, str] | str]:
    values: dict[str, str] = {}
    for key, prop in (
        ("manufacturer", "ro.product.manufacturer"),
        ("model", "ro.product.model"),
        ("device", "ro.product.device"),
    ):
        ok, value = adb_text(runner, serial, "shell", "getprop", prop)
        if not ok:
            return False, f"getprop_failed:{prop}"
        values[key] = value
    return True, values


def identity_matches(actual: dict[str, str], expected: ExpectedIdentity) -> bool:
    manufacturer = normalize(actual.get("manufacturer", ""))
    model = normalize(actual.get("model", ""))
    expected_manufacturer = normalize(expected.manufacturer)
    expected_model = normalize(expected.model)

    if expected_manufacturer == "tcl":
        manufacturer_ok = manufacturer == "tcl" or manufacturer.startswith("tcl_")
    else:
        manufacturer_ok = manufacturer == expected_manufacturer

    if expected_model == "6102h":
        model_ok = model == "6102h" or model.endswith("_6102h") or "6102h" in model
    else:
        model_ok = model == expected_model
    return manufacturer_ok and model_ok


def parse_user_ids(raw: str) -> list[int]:
    return [int(match) for match in re.findall(r"UserInfo\{(\d+):", raw)]


def package_users(runner: Runner, serial: str, package: str) -> tuple[bool, list[int] | str]:
    ok, raw_users = adb_text(runner, serial, "shell", "pm", "list", "users")
    if not ok:
        return False, "pm_list_users_failed"
    users = parse_user_ids(raw_users) or [0]
    installed: list[int] = []
    for user_id in users:
        ok, raw = adb_text(
            runner,
            serial,
            "shell",
            "pm",
            "list",
            "packages",
            "--user",
            str(user_id),
            package,
        )
        if not ok:
            return False, f"pm_list_packages_failed:user={user_id}"
        if any(line.strip() == f"package:{package}" for line in raw.splitlines()):
            installed.append(user_id)
    return True, installed


def gate(
    expected: ExpectedIdentity,
    *,
    serial: str | None = None,
    required_packages: list[str] | None = None,
    runner: Runner = run,
) -> dict[str, object]:
    listed = runner(["devices", "-l"])
    if listed.returncode != 0:
        return {"status": "blocked", "reason": "adb_devices_failed", "detail": (listed.stderr or "").strip()}

    devices = parse_devices(listed.stdout)
    live_physical = [
        row
        for row in devices
        if row["state"] == "device" and not row["serial"].startswith("emulator-")
    ]

    if serial is not None:
        candidates = [row for row in live_physical if row["serial"] == serial]
        if not candidates:
            return {
                "status": "blocked",
                "reason": "requested_serial_not_live_physical_device",
                "serial": serial,
                "live_physical_serials": [row["serial"] for row in live_physical],
            }
    else:
        candidates = live_physical

    matches: list[dict[str, object]] = []
    examined: list[dict[str, object]] = []
    for row in candidates:
        ok, identity_or_reason = read_identity(runner, row["serial"])
        if not ok:
            examined.append({
                "serial": row["serial"],
                "identity_verified": False,
                "reason": identity_or_reason,
            })
            continue
        identity = identity_or_reason
        assert isinstance(identity, dict)
        matched = identity_matches(identity, expected)
        record = {
            "serial": row["serial"],
            "identity": identity,
            "identity_verified": matched,
        }
        examined.append(record)
        if matched:
            matches.append(record)

    if not matches:
        return {
            "status": "blocked",
            "reason": "target_identity_not_found" if serial is None else "target_identity_mismatch",
            "expected": {
                "manufacturer": expected.manufacturer,
                "model": expected.model,
            },
            "examined": examined,
        }
    if len(matches) > 1:
        return {
            "status": "blocked",
            "reason": "target_identity_ambiguous",
            "expected": {
                "manufacturer": expected.manufacturer,
                "model": expected.model,
            },
            "matches": matches,
        }

    target = matches[0]
    result: dict[str, object] = {
        "status": "ok",
        "identity_verified": True,
        "serial": target["serial"],
        "identity": target["identity"],
        "expected": {
            "manufacturer": expected.manufacturer,
            "model": expected.model,
        },
    }

    packages: dict[str, dict[str, object]] = {}
    for package in required_packages or []:
        ok, users_or_reason = package_users(runner, str(target["serial"]), package)
        if not ok:
            return {
                **result,
                "status": "blocked",
                "reason": str(users_or_reason),
                "packages": packages,
            }
        users = users_or_reason
        assert isinstance(users, list)
        packages[package] = {"installed": bool(users), "users": users}
        if not users:
            return {
                **result,
                "status": "blocked",
                "reason": "required_package_missing",
                "missing_package": package,
                "packages": packages,
            }

    if packages:
        result["packages"] = packages
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Fail-closed ADB identity gate. Verifies the physical device before "
            "package or device-specific conclusions."
        )
    )
    parser.add_argument("--target", choices=sorted(TARGETS), help="Known target identity")
    parser.add_argument(
        "--expect-manufacturer",
        help="Expected ro.product.manufacturer for a custom target",
    )
    parser.add_argument(
        "--expect-model",
        help="Expected ro.product.model for a custom target",
    )
    parser.add_argument(
        "--serial",
        help="Optional live ADB serial to verify; never trusted without getprop verification",
    )
    parser.add_argument(
        "--require-package",
        action="append",
        default=[],
        help=(
            "Package that must exist on at least one Android user/profile; "
            "repeatable"
        ),
    )
    args = parser.parse_args(argv)

    if args.target:
        if args.expect_manufacturer or args.expect_model:
            parser.error(
                "use --target or custom --expect-manufacturer/--expect-model, not both"
            )
        expected = TARGETS[args.target]
    else:
        if not args.expect_manufacturer or not args.expect_model:
            parser.error(
                "provide --target or both --expect-manufacturer and --expect-model"
            )
        expected = ExpectedIdentity(args.expect_manufacturer, args.expect_model)

    result = gate(
        expected,
        serial=args.serial,
        required_packages=args.require_package,
    )
    print(json.dumps(result, sort_keys=True))
    return 0 if result.get("status") == "ok" else 2


if __name__ == "__main__":
    raise SystemExit(main())
