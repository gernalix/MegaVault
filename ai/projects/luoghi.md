# luoghi

META:
slug=luoghi
name=Luoghi
status=active
type=Android app
repo=/home/daniele/AndroidStudioProjects/Luoghi
remote=git@github.com:gernalix/Luoghi.git
branch=main
metadata=/home/daniele/AndroidStudioProjects/Luoghi/dev/project.metadata.json
human_overview=/home/daniele/codex-workspace/MegaVault/human/projects/luoghi/overview.md
human_roadmap=/home/daniele/codex-workspace/MegaVault/human/projects/luoghi/roadmap.md
human_changelog=/home/daniele/codex-workspace/MegaVault/human/projects/luoghi/changelog.md
human_troubleshooting=/home/daniele/codex-workspace/MegaVault/human/projects/luoghi/troubleshooting.md
template_source=/home/daniele/codex-workspace/android-app-template
source_policy=generated_from_android-app-template_only;not_from_Soldi

PURPOSE:
domain=TBD
stage=clean Android Studio starter generated from official frozen template
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
package=com.gernalix.luoghi

MAP:
entry=app/src/main/java/com/gernalix/luoghi/MainActivity.kt
theme=app/src/main/java/com/gernalix/luoghi/ui/theme/
manifest=app/src/main/AndroidManifest.xml
strings=app/src/main/res/values/strings.xml
build=app/build.gradle.kts,settings.gradle.kts,gradle/libs.versions.toml
metadata=dev/project.metadata.json
tests=app/src/test/java/com/gernalix/luoghi/ExampleUnitTest.kt,app/src/androidTest/java/com/gernalix/luoghi/ExampleInstrumentedTest.kt

ARCH:
current=single Activity Compose starter
state=no domain architecture selected
boundary=do not infer app domain from name until operator defines scope
template_boundary=Luoghi generated from android-app-template; never from Soldi

FLOW:
launch=Launcher -> MainActivity -> LuoghiTheme -> Scaffold -> Greeting("Android")
build=Gradle wrapper -> Android plugin -> debug APK
generation=android-app-template generator rewrote package,namespace,applicationId,app_name,theme,root project name

INV:
git=repo initialized at /home/daniele/AndroidStudioProjects/Luoghi on branch main
identity=namespace/applicationId/package/test assertion must stay com.gernalix.luoghi
app_name=res string must stay Luoghi until product rename requested
template=do not edit Luoghi to repair template bugs; fix android-app-template first
source=android-app-template only; Soldi is forbidden as generator source
ignore=.gitignore excludes build outputs,.gradle,.kotlin,local.properties,APK artifacts,IDE transient files

BUILD:
cmd=cd /home/daniele/AndroidStudioProjects/Luoghi && ./gradlew assembleDebug
result=PASS 2026-06-13
apk=/home/daniele/AndroidStudioProjects/Luoghi/app/build/outputs/apk/debug/app-debug.apk
apk_sha256=19523bd19c958af093f2580323dd405b550f9d81f20728dc46e78c129c3c1653
warning=stripDebugDebugSymbols cannot strip libandroidx.graphics.path.so; packaged as-is
env=ANDROID_HOME=/home/daniele/Android/Sdk

TEST:
smoke=./gradlew assembleDebug PASS 2026-06-13
unit=starter ExampleUnitTest only
instrumented=starter ExampleInstrumentedTest asserts com.gernalix.luoghi; not run on device
device_strategy=ADB device state may drift; verify with adb devices -l before connected tests

DATA:
storage=TBD
db=none
backup=none_app_data_yet
migration=none

DNB:
item=do not commit local.properties/build outputs/APKs|why=machine-specific/generated|test=git status --ignored
item=do not use Soldi as source|why=Soldi is real app not template|test=template_source path is android-app-template
item=do not change package casually|why=application identity|test=rg com.gernalix.luoghi app dev

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
repo=/home/daniele/AndroidStudioProjects/Luoghi
metadata=/home/daniele/AndroidStudioProjects/Luoghi/dev/project.metadata.json
template_ai=/home/daniele/codex-workspace/MegaVault/ai/projects/android-app-template.md
soldi_ai=/home/daniele/codex-workspace/MegaVault/ai/projects/soldi.md
human_overview=/home/daniele/codex-workspace/MegaVault/human/projects/luoghi/overview.md
human_roadmap=/home/daniele/codex-workspace/MegaVault/human/projects/luoghi/roadmap.md
human_changelog=/home/daniele/codex-workspace/MegaVault/human/projects/luoghi/changelog.md
human_troubleshooting=/home/daniele/codex-workspace/MegaVault/human/projects/luoghi/troubleshooting.md

OPEN:
domain=TBD
architecture=TBD
persistence=TBD
remote_origin=git@github.com:gernalix/Luoghi.git
