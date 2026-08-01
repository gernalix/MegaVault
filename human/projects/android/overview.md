# android Overview

Host-local Android helper project for Linux Mint.

## Links
- AI doc: android.md (`../../../ai/projects/android.md`; status=UNKNOWN)
- Metadata: project.metadata.json (`../../../../projects/android/dev/project.metadata.json`; status=UNKNOWN)
- Legacy metadata: .codexmeta (`../../../../projects/android/.codexmeta`; status=UNKNOWN)
- Repository path: projects/android (`../../../../projects/android`; status=UNKNOWN)

## ADB Wi-Fi Auto-Connect
- Project path: `/home/daniele/codex-workspace/projects/android`
- Main script: `/home/daniele/codex-workspace/projects/android/adb-wifi-autoconnect.py`
- Installed command: `~/.local/bin/adb-wifi-autoconnect`
- User service: `~/.config/systemd/user/adb-wifi-autoconnect.service`
- Config: `~/.config/adb-wifi-autoconnect/config.json`
- State/logs: `~/.local/state/adb-wifi-autoconnect/`

The service keeps ADB wireless debugging reachable by polling `adb mdns services` and Avahi, then running `adb connect HOST:PORT` for advertised Android endpoints. It supports Pixel and TCL at the same time through device profiles and does not require switching profiles manually.

Pairing is manual by default so the service does not steal focus with input windows. Use `adb pair HOST:PORT CODE`, then `adb connect HOST:PORT`. The old popup behavior is available only if `ADB_WIFI_AUTOCONNECT_AUTO_PAIR_UI=1` is set in the user unit.

Known default profiles:

- Pixel 8a: historical host `192.168.1.37`, tokens `Pixel_8a`, `akita`, `52131JEKB01070`.
- TCL 6102H: historical host `192.168.1.200`, tokens `6102H`, `QCGADUVOSSEYFES4`, `Android-3.local`.

## Operations
- Status: `adb-wifi-autoconnect status`
- One scan: `adb-wifi-autoconnect scan-now`
- Restart: `systemctl --user restart adb-wifi-autoconnect.service`
- Journal: `journalctl --user -u adb-wifi-autoconnect.service --no-pager`
- Pair manually: `adb pair HOST:PORT CODE && adb connect HOST:PORT`

`adb devices -l` is the authoritative connected/offline check. mDNS/Avahi only proves that a phone advertises wireless debugging; it does not prove the port is connectable.
