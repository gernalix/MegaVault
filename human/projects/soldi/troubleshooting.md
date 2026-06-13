# Soldi Troubleshooting

## Build

Run:

```bash
cd /home/daniele/AndroidStudioProjects/Soldi
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

`Soldi` is not a template. Do not use it as a source for new apps.

If the starter base needs repair, update `/home/daniele/codex-workspace/android-app-template` first. Do not copy future `Soldi` app work back into the template unless a deliberate template migration is requested.
