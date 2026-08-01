# Sostanze Troubleshooting

## Build

Run:

```bash
cd /home/daniele/projects/Sostanze
./gradlew --no-daemon --console=plain testDebugUnitTest assembleDebug
```

If SDK discovery fails, verify:

```bash
echo "$ANDROID_HOME"
echo "$ANDROID_SDK_ROOT"
```

Expected local SDK path: `/home/daniele/Android/Sdk`.

## TCL Smoke

Use the TCL serial explicitly:

```bash
/home/daniele/Android/Sdk/platform-tools/adb -s 192.168.1.200:45699 install -r app/build/outputs/apk/debug/app-debug.apk
/home/daniele/Android/Sdk/platform-tools/adb -s 192.168.1.200:45699 shell am start -n com.gernalix.sostanze/.MainActivity
```

Prompts `#739284` and `#294816` used TCL 6102H, not Pixel.

## SAF ImportExport

- Export uses a dedicated Android SAF folder and the fixed filename `sostanze.db`.
- The folder should contain only `sostanze.db`; the exporter removes stale sibling files.
- Android production apps cannot receive SAF tree permission silently through adb. Use the app `Export` button and confirm the system DocumentsUI folder picker.
- Import uses the app `Import` button, validates the SQLite schema, and rejects incompatible files without changing current data.

## Known Warnings

- `stripDebugDebugSymbols` may report `libandroidx.graphics.path.so` cannot be stripped; the APK still packages it.
- Material3 `TabRow` deprecation warning is non-blocking.

## Generated Files

Do not commit `local.properties`, `.gradle/`, `.kotlin/`, `build/`, `app/build/`, or generated APK/AAB outputs outside the explicit `output/` release artifacts.

## Template Drift

If the starter base needs repair, update `/home/daniele/codex-workspace/android-app-template` first, then regenerate or port the fix deliberately.
