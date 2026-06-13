# soldi

META:
slug=soldi
name=Soldi
status=active
type=Android app
repo=/home/daniele/AndroidStudioProjects/Soldi
remote=git@github.com:gernalix/Soldi.git
branch=main
metadata=/home/daniele/AndroidStudioProjects/Soldi/dev/project.metadata.json
human_overview=/home/daniele/codex-workspace/MegaVault/human/projects/soldi/overview.md
human_roadmap=/home/daniele/codex-workspace/MegaVault/human/projects/soldi/roadmap.md
human_changelog=/home/daniele/codex-workspace/MegaVault/human/projects/soldi/changelog.md
human_troubleshooting=/home/daniele/codex-workspace/MegaVault/human/projects/soldi/troubleshooting.md
template_source=/home/daniele/codex-workspace/android-app-template
backup_original=/home/daniele/AndroidStudioProjects/_backups/Soldi-original-dir-20260613-040309
backup_verified_copy=/home/daniele/AndroidStudioProjects/_backups/Soldi-pre-template-20260613-040309

PURPOSE:
domain=personal finance,expenses,transactions
stage=clean Android Studio starter generated from reusable local template
implemented_features=Android launcher activity,Compose Hello Android screen,debug build
non_features=no finance model,no persistence,no business logic

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
package=com.gernalix.soldi

MAP:
entry=app/src/main/java/com/gernalix/soldi/MainActivity.kt
theme=app/src/main/java/com/gernalix/soldi/ui/theme/
manifest=app/src/main/AndroidManifest.xml
strings=app/src/main/res/values/strings.xml
build=app/build.gradle.kts,settings.gradle.kts,gradle/libs.versions.toml
metadata=dev/project.metadata.json
tests=app/src/test/java/com/gernalix/soldi/ExampleUnitTest.kt,app/src/androidTest/java/com/gernalix/soldi/ExampleInstrumentedTest.kt

ARCH:
current=single Activity Compose starter
state=no domain architecture selected
boundary=do not add finance behavior unless explicitly requested

FLOW:
launch=Launcher -> MainActivity -> SoldiTheme -> Scaffold -> Greeting("Android")
build=Gradle wrapper -> Android plugin -> debug APK
generation=android-app-template generator rewrote package,namespace,applicationId,app_name,theme,root project name

INV:
git=repo initialized at /home/daniele/AndroidStudioProjects/Soldi on branch main
identity=namespace/applicationId/package/test assertion must stay com.gernalix.soldi
app_name=res string must stay Soldi until product rename requested
template=do not edit generated app to repair template bugs; fix template then regenerate if possible
ignore=.gitignore excludes build outputs,.gradle,.kotlin,local.properties,APK artifacts,IDE transient files

BUILD:
cmd=cd /home/daniele/AndroidStudioProjects/Soldi && ./gradlew assembleDebug
result=PASS 2026-06-13
apk=/home/daniele/AndroidStudioProjects/Soldi/app/build/outputs/apk/debug/app-debug.apk
apk_sha256=3e203d071d494c455764d5483f622de3695c5fb269fabd08fd6a24045a9db515
warning=stripDebugDebugSymbols cannot strip libandroidx.graphics.path.so; packaged as-is
env=ANDROID_HOME=/home/daniele/Android/Sdk

TEST:
smoke=./gradlew assembleDebug PASS 2026-06-13
unit=starter ExampleUnitTest only
instrumented=starter ExampleInstrumentedTest asserts com.gernalix.soldi; not run on device
device_strategy=ADB device state may drift; verify with adb devices -l before connected tests

DATA:
storage=TBD
db=none
backup=none_app_data_yet
migration=none

DNB:
item=do not commit local.properties/build outputs/APKs|why=machine-specific/generated|test=git status --ignored
item=do not overwrite original 2026-06-05 source without backup|why=used as golden template source|test=backup dirs exist under AndroidStudioProjects/_backups
item=do not change package casually|why=application identity|test=rg com.gernalix.soldi app dev

BUG:
known=none after generated debug build

RISK:
risk=app is still starter UI|trigger=assuming finance features exist|mitigation=mark non_features|test=read MainActivity.kt
risk=template drift|trigger=manual fixes in only one generated app|mitigation=fix android-app-template first|test=compare generator/template docs
risk=remote is private GitHub repo|trigger=cloning from unauthenticated host|mitigation=use authenticated SSH/GitHub access|test=git ls-remote origin refs/heads/main

ROAD:
now=define MVP scope and data model
next=choose persistence,probably Room/SQLite
later=add finance screens,validation,backup/export if needed

LINK:
repo=/home/daniele/AndroidStudioProjects/Soldi
metadata=/home/daniele/AndroidStudioProjects/Soldi/dev/project.metadata.json
template_ai=/home/daniele/codex-workspace/MegaVault/ai/projects/android-app-template.md
human_overview=/home/daniele/codex-workspace/MegaVault/human/projects/soldi/overview.md
human_roadmap=/home/daniele/codex-workspace/MegaVault/human/projects/soldi/roadmap.md
human_changelog=/home/daniele/codex-workspace/MegaVault/human/projects/soldi/changelog.md
human_troubleshooting=/home/daniele/codex-workspace/MegaVault/human/projects/soldi/troubleshooting.md

OPEN:
architecture=TBD
persistence=TBD
remote_origin=git@github.com:gernalix/Soldi.git
