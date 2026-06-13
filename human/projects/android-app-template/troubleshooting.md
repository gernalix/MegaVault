# Android App Template Troubleshooting

## Generator

The generator refuses existing non-empty destinations. Move or back up the target first.

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
