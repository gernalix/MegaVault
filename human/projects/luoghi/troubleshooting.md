# Luoghi Troubleshooting

## Build

Run:

```bash
cd /home/daniele/AndroidStudioProjects/Luoghi
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

## Template Source

`Luoghi` must trace back to `/home/daniele/codex-workspace/android-app-template`. `Soldi` is not a template source.
