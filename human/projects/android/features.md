# android Features

## ADB Wi-Fi Auto-Connect
- User-level systemd loop for wireless ADB discovery and reconnect.
- Multi-device profile support for Pixel 8a and TCL 6102H.
- Generic unknown-device support remains enabled for future Android devices.
- Per-device labels in state/logs: profile id, label, endpoint, service id, hostname, mDNS name.
- Manual-first pairing so input windows do not steal focus.
- Retry throttling per endpoint to avoid noisy connect loops.

## Device Status
- TCL 6102H connected on 2026-06-05 as `192.168.1.200:34719`, `product=6102H_EEA`, `model=6102H`, `device=Cruze_Lite_S`.
- Pixel is not currently connected; mDNS/pairing advertisements are not treated as a connected-device proof.
