from __future__ import annotations

import subprocess
import unittest

import adb_device_gate as gate


class FakeAdb:
    def __init__(self, responses):
        self.responses = {tuple(key): list(value) for key, value in responses.items()}
        self.calls = []

    def __call__(self, args):
        key = tuple(args)
        self.calls.append(key)
        values = self.responses.get(key)
        if not values:
            return subprocess.CompletedProcess(args, 0, "", "")
        if len(values) == 1:
            return values[0]
        return values.pop(0)


def proc(stdout="", code=0, stderr=""):
    return subprocess.CompletedProcess([], code, stdout, stderr)


def pixel_responses(serial="P"):
    return {
        ("-s", serial, "shell", "getprop", "ro.product.manufacturer"): [proc("Google\n")],
        ("-s", serial, "shell", "getprop", "ro.product.model"): [proc("Pixel 8a\n")],
        ("-s", serial, "shell", "getprop", "ro.product.device"): [proc("akita\n")],
    }


class GateTests(unittest.TestCase):
    def test_selects_pixel_by_verified_getprop_not_device_order(self):
        responses = {
            ("devices", "-l"): [
                proc(
                    "List of devices attached\n"
                    "T device model:TCL_6102H\n"
                    "P device model:Pixel_8a\n"
                )
            ],
            ("-s", "T", "shell", "getprop", "ro.product.manufacturer"): [proc("TCL\n")],
            ("-s", "T", "shell", "getprop", "ro.product.model"): [proc("6102H\n")],
            ("-s", "T", "shell", "getprop", "ro.product.device"): [proc("tcl\n")],
            **pixel_responses("P"),
        }
        adb = FakeAdb(responses)
        result = gate.gate(gate.TARGETS["pixel"], runner=adb)
        self.assertEqual("ok", result["status"])
        self.assertEqual("P", result["serial"])
        self.assertTrue(result["identity_verified"])

    def test_wrong_requested_serial_blocks_before_package_check(self):
        responses = {
            ("devices", "-l"): [
                proc("List of devices attached\nT device model:TCL_6102H\n")
            ],
            ("-s", "T", "shell", "getprop", "ro.product.manufacturer"): [proc("TCL\n")],
            ("-s", "T", "shell", "getprop", "ro.product.model"): [proc("6102H\n")],
            ("-s", "T", "shell", "getprop", "ro.product.device"): [proc("tcl\n")],
        }
        adb = FakeAdb(responses)
        result = gate.gate(
            gate.TARGETS["pixel"],
            serial="T",
            required_packages=["de.hafas.android.rejseplanen"],
            runner=adb,
        )
        self.assertEqual("blocked", result["status"])
        self.assertEqual("target_identity_mismatch", result["reason"])
        self.assertFalse(any("packages" in call for call in adb.calls))

    def test_required_package_is_checked_only_after_identity_passes(self):
        responses = {
            ("devices", "-l"): [
                proc("List of devices attached\nP device model:Pixel_8a\n")
            ],
            **pixel_responses("P"),
            ("-s", "P", "shell", "pm", "list", "users"): [
                proc("Users:\n\tUserInfo{0:Owner:13} running\n")
            ],
            (
                "-s",
                "P",
                "shell",
                "pm",
                "list",
                "packages",
                "--user",
                "0",
                "de.hafas.android.rejseplanen",
            ): [proc("package:de.hafas.android.rejseplanen\n")],
        }
        result = gate.gate(
            gate.TARGETS["pixel"],
            required_packages=["de.hafas.android.rejseplanen"],
            runner=FakeAdb(responses),
        )
        self.assertEqual("ok", result["status"])
        self.assertEqual(
            [0],
            result["packages"]["de.hafas.android.rejseplanen"]["users"],
        )

    def test_missing_package_is_not_confused_with_wrong_device(self):
        responses = {
            ("devices", "-l"): [
                proc("List of devices attached\nP device model:Pixel_8a\n")
            ],
            **pixel_responses("P"),
            ("-s", "P", "shell", "pm", "list", "users"): [
                proc(
                    "Users:\n"
                    "\tUserInfo{0:Owner:13} running\n"
                    "\tUserInfo{10:Work:30}\n"
                )
            ],
            (
                "-s",
                "P",
                "shell",
                "pm",
                "list",
                "packages",
                "--user",
                "0",
                "x.y",
            ): [proc("")],
            (
                "-s",
                "P",
                "shell",
                "pm",
                "list",
                "packages",
                "--user",
                "10",
                "x.y",
            ): [proc("")],
        }
        result = gate.gate(
            gate.TARGETS["pixel"],
            required_packages=["x.y"],
            runner=FakeAdb(responses),
        )
        self.assertEqual("blocked", result["status"])
        self.assertEqual("required_package_missing", result["reason"])
        self.assertTrue(result["identity_verified"])

    def test_two_matching_pixels_are_ambiguous_without_serial(self):
        responses = {
            ("devices", "-l"): [
                proc(
                    "List of devices attached\n"
                    "P1 device model:Pixel_8a\n"
                    "P2 device model:Pixel_8a\n"
                )
            ],
            **pixel_responses("P1"),
            **pixel_responses("P2"),
        }
        result = gate.gate(gate.TARGETS["pixel"], runner=FakeAdb(responses))
        self.assertEqual("blocked", result["status"])
        self.assertEqual("target_identity_ambiguous", result["reason"])


if __name__ == "__main__":
    unittest.main()
