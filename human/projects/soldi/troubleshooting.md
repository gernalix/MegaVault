# Soldi Troubleshooting

## Build

Run:

```bash
cd /home/daniele/projects/Soldi
./gradlew assembleDebug
```

If SDK discovery fails, verify:

```bash
echo "$ANDROID_HOME"
echo "$ANDROID_SDK_ROOT"
```

Expected local SDK path: `/home/daniele/Android/Sdk`.

## Generated Files

Do not commit `local.properties`, `.gradle/`, `.kotlin/`, `build/`, `app/build/`, or APK/AAB outputs.

## Export and Import

Soldi exports the authoritative SQLite database to the user-selected SAF folder as:

- `soldi.db`: current stable export
- `soldi.db.bak`: last validated emergency copy
- `soldi.db.tmp`: transient copy used during atomic promotion

If export fails, keep the last good `soldi.db` and check the in-app autoexport status.

## TCL Wireless Debugging

If the TCL appears offline or old ports fail:

```bash
/home/daniele/Android/Sdk/platform-tools/adb mdns services
```

Then open Wireless debugging on the TCL, choose pairing by code, and run:

```bash
/home/daniele/Android/Sdk/platform-tools/adb pair <ip>:<pairing-port>
/home/daniele/Android/Sdk/platform-tools/adb connect <ip>:<connect-port>
```

For 2026-06-18, mDNS showed pairing `192.168.1.200:36185` and connect `192.168.1.200:39737`, but `adb connect` failed before pairing.

## Template Drift

`Soldi` is not a template. Do not use it as a source for new apps.

If the starter base needs repair, update `/home/daniele/codex-workspace/android-app-template` first. Do not copy future `Soldi` app work back into the template unless a deliberate template migration is requested.
