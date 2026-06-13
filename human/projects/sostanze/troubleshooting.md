# Sostanze Troubleshooting

## Build

Run:

```bash
cd /home/daniele/AndroidStudioProjects/Sostanze
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

Prompt `#739284` used TCL 6102H, not Pixel.

## Known Warnings

- `stripDebugDebugSymbols` may report `libandroidx.graphics.path.so` cannot be stripped; the APK still packages it.
- Material3 `TabRow` deprecation warning is non-blocking.

## Generated Files

Do not commit `local.properties`, `.gradle/`, `.kotlin/`, `build/`, `app/build/`, or APK/AAB outputs.

## Template Drift

If the starter base needs repair, update `/home/daniele/codex-workspace/android-app-template` first, then regenerate or port the fix deliberately.
