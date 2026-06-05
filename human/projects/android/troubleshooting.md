# android Troubleshooting

## TCL Advertised But Not Connected
- Check authoritative state: `adb devices -l`.
- Check advertisements: `adb mdns services` and `avahi-browse -rtp _adb-tls-connect._tcp`.
- If first-time setup is needed, open TCL Wireless debugging -> Pair device with pairing code, then run `adb pair HOST:PORT CODE`.
- Connect after pairing: `adb connect HOST:PORT`.

## Pairing Popup Steals Focus
- Default is disabled in v0.3.0: `auto pairing UI: disabled`.
- Do not set `ADB_WIFI_AUTOCONNECT_AUTO_PAIR_UI=1` unless focus-stealing popups are acceptable.
- Close stale dialogs with `pkill -f 'adb-wifi-autoconnect pair-ui-zenity|zenity --forms'`.

## mDNS Looks Green But ADB Fails
- Treat mDNS as advertisement only.
- `Connection refused`, `No route to host`, or protocol errors can occur with stale Android wireless-debugging ports.
- Verify the phone remains on Wi-Fi, Wireless debugging stays enabled, and the current connect port is still shown by Avahi/ADB mDNS.
