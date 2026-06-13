# sostanze

META:
slug=sostanze
name=Sostanze
status=active
type=Android app
repo=/home/daniele/AndroidStudioProjects/Sostanze
remote=git@github.com:gernalix/Sostanze.git
branch=main
metadata=/home/daniele/AndroidStudioProjects/Sostanze/dev/project.metadata.json
human_overview=/home/daniele/codex-workspace/MegaVault/human/projects/sostanze/overview.md
human_roadmap=/home/daniele/codex-workspace/MegaVault/human/projects/sostanze/roadmap.md
human_changelog=/home/daniele/codex-workspace/MegaVault/human/projects/sostanze/changelog.md
human_troubleshooting=/home/daniele/codex-workspace/MegaVault/human/projects/sostanze/troubleshooting.md
template_source=/home/daniele/codex-workspace/android-app-template

PURPOSE:
domain=TBD
stage=clean Android Studio starter generated from reusable local template
implemented_features=Android launcher activity,Compose Hello Android screen,debug build
non_features=no domain model,no persistence,no business logic

STACK:
platform=Android
lang=Kotlin
ui=Jetpack Compose Material3
build=Gradle wrapper
agp=9.2.1
kotlin=2.2.10
compose_bom=2026.02.01
compileSdk=36.1
minSdk=29
package=com.gernalix.sostanze

MAP:
entry=app/src/main/java/com/gernalix/sostanze/MainActivity.kt
theme=app/src/main/java/com/gernalix/sostanze/ui/theme/
manifest=app/src/main/AndroidManifest.xml
strings=app/src/main/res/values/strings.xml
build=app/build.gradle.kts,settings.gradle.kts,gradle/libs.versions.toml
metadata=dev/project.metadata.json
tests=app/src/test/java/com/gernalix/sostanze/ExampleUnitTest.kt,app/src/androidTest/java/com/gernalix/sostanze/ExampleInstrumentedTest.kt

ARCH:
current=single Activity Compose starter
state=no domain architecture selected
boundary=do not infer app domain from name until operator defines scope

FLOW:
launch=Launcher -> MainActivity -> SostanzeTheme -> Scaffold -> Greeting("Android")
build=Gradle wrapper -> Android plugin -> debug APK
generation=android-app-template generator rewrote package,namespace,applicationId,app_name,theme,root project name

INV:
git=repo initialized at /home/daniele/AndroidStudioProjects/Sostanze on branch main
identity=namespace/applicationId/package/test assertion must stay com.gernalix.sostanze
app_name=res string must stay Sostanze until product rename requested
template=do not edit generated app to repair template bugs; fix template then regenerate if possible
ignore=.gitignore excludes build outputs,.gradle,.kotlin,local.properties,APK artifacts,IDE transient files

BUILD:
cmd=cd /home/daniele/AndroidStudioProjects/Sostanze && ./gradlew assembleDebug
result=PASS 2026-06-13
apk=/home/daniele/AndroidStudioProjects/Sostanze/app/build/outputs/apk/debug/app-debug.apk
apk_sha256=2e93e61de9f5a41fb4c2db7d52747d25b37a9b665df42e39a1ef165ed9d1dd19
warning=stripDebugDebugSymbols cannot strip libandroidx.graphics.path.so; packaged as-is
env=ANDROID_HOME=/home/daniele/Android/Sdk

TEST:
smoke=./gradlew assembleDebug PASS 2026-06-13
unit=starter ExampleUnitTest only
instrumented=starter ExampleInstrumentedTest asserts com.gernalix.sostanze; not run on device
device_strategy=ADB device state may drift; verify with adb devices -l before connected tests

DATA:
storage=TBD
db=none
backup=none_app_data_yet
migration=none

DNB:
item=do not commit local.properties/build outputs/APKs|why=machine-specific/generated|test=git status --ignored
item=do not infer domain/data requirements from name|why=scope unknown|test=OPEN domain remains TBD
item=do not change package casually|why=application identity|test=rg com.gernalix.sostanze app dev

BUG:
known=none after generated debug build

RISK:
risk=app is still starter UI|trigger=assuming domain features exist|mitigation=mark non_features|test=read MainActivity.kt
risk=template drift|trigger=manual fixes in only one generated app|mitigation=fix android-app-template first|test=compare generator/template docs
risk=remote is private GitHub repo|trigger=cloning from unauthenticated host|mitigation=use authenticated SSH/GitHub access|test=git ls-remote origin refs/heads/main

ROAD:
now=define app domain and MVP scope
next=choose persistence if data is needed
later=add domain screens,validation,backup/export if needed

LINK:
repo=/home/daniele/AndroidStudioProjects/Sostanze
metadata=/home/daniele/AndroidStudioProjects/Sostanze/dev/project.metadata.json
template_ai=/home/daniele/codex-workspace/MegaVault/ai/projects/android-app-template.md
human_overview=/home/daniele/codex-workspace/MegaVault/human/projects/sostanze/overview.md
human_roadmap=/home/daniele/codex-workspace/MegaVault/human/projects/sostanze/roadmap.md
human_changelog=/home/daniele/codex-workspace/MegaVault/human/projects/sostanze/changelog.md
human_troubleshooting=/home/daniele/codex-workspace/MegaVault/human/projects/sostanze/troubleshooting.md

OPEN:
domain=TBD
architecture=TBD
persistence=TBD
remote_origin=git@github.com:gernalix/Sostanze.git
