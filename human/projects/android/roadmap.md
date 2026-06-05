# android Roadmap

## Now
- Keep `adb-wifi-autoconnect.service` active/enabled.
- Use terminal pairing for new devices: `adb pair HOST:PORT CODE`, then `adb connect HOST:PORT`.

## Next
- Add an optional CLI command to edit device profiles without manual JSON edits.
- Add a clear status warning when a known device advertises for several scans but remains unconnectable.

## Later
- Consider pruning old endpoint history from `state.json` while preserving recent diagnostics.
