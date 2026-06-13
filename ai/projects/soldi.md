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
relationship=Soldi_is_real_app;historical_template_source_once_only;not_live_template

PURPOSE:
domain=personal finance,expenses,transactions
stage=real app at clean Android starter stage; may be developed normally
implemented_features=Android launcher activity,Compose Hello Android screen,debug build
non_features=no finance model,no persistence,no business logic
template_note=template was extracted once from original clean Soldi; future Soldi work must not feed template automatically

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
template_boundary=do not use Soldi as generator source; use /home/daniele/codex-workspace/android-app-template

FLOW:
launch=Launcher -> MainActivity -> SoldiTheme -> Scaffold -> Greeting("Android")
build=Gradle wrapper -> Android plugin -> debug APK
generation=initial reset from android-app-template completed 2026-06-13; future new apps must not use Soldi as source

INV:
git=repo initialized at /home/daniele/AndroidStudioProjects/Soldi on branch main
identity=namespace/applicationId/package/test assertion must stay com.gernalix.soldi
app_name=res string must stay Soldi until product rename requested
template=Soldi is not a template; do not copy future Soldi changes into android-app-template unless explicit migration requested
new_apps=generate from android-app-template only,never from Soldi
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
item=do not regenerate/overwrite Soldi for app creation|why=Soldi is real app|test=template generator refuses Soldi destination
item=do not use Soldi as template source|why=template is independent frozen snapshot|test=new app source path is android-app-template
item=do not change package casually|why=application identity|test=rg com.gernalix.soldi app dev

BUG:
known=none after generated debug build

RISK:
risk=app is still starter UI|trigger=assuming finance features exist|mitigation=mark non_features|test=read MainActivity.kt
risk=template confusion|trigger=using Soldi to generate new apps|mitigation=document Soldi real-app boundary|test=README+AI docs contain guardrail
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
