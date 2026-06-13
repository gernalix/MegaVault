# Android App Template Troubleshooting

## Generator

The generator refuses existing non-empty destinations. Move or back up the target first.

The generator also refuses `/home/daniele/AndroidStudioProjects/Soldi`; `Soldi` is a real app and must not be regenerated while creating new apps.

## Validation

After generation, run:

```bash
cd DESTINATION
./gradlew assembleDebug
```

Then check for stale identifiers:

```bash
rg 'AndroidAppTemplate|com\.gernalix\.androidapptemplate|danielegalati|com\.danielegalati' DESTINATION
```

## SDK

The current host uses `/home/daniele/Android/Sdk` through `ANDROID_HOME` and `ANDROID_SDK_ROOT`; generated apps intentionally do not commit `local.properties`.
