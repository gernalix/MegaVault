# Sostanze Troubleshooting

## Build

Run:

```bash
cd /home/daniele/AndroidStudioProjects/Sostanze
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

## Template Drift

If the starter base needs repair, update `/home/daniele/codex-workspace/android-app-template` first, then regenerate or port the fix deliberately.
