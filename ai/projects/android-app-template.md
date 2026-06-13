# android-app-template

META:
slug=android-app-template
name=Android App Template
status=active
type=Android reusable template
repo=/home/daniele/codex-workspace/android-app-template
remote=git@github.com:gernalix/android-app-template.git
branch=main
metadata=/home/daniele/codex-workspace/android-app-template/dev/project.metadata.json
human_overview=/home/daniele/codex-workspace/MegaVault/human/projects/android-app-template/overview.md
human_roadmap=/home/daniele/codex-workspace/MegaVault/human/projects/android-app-template/roadmap.md
human_changelog=/home/daniele/codex-workspace/MegaVault/human/projects/android-app-template/changelog.md
human_troubleshooting=/home/daniele/codex-workspace/MegaVault/human/projects/android-app-template/troubleshooting.md

PURPOSE:
goal=reusable clean Android Studio starter template generated from verified Soldi source
source=/home/daniele/AndroidStudioProjects/_backups/Soldi-original-dir-20260613-040309
implemented=template project plus create_android_app_from_template generator
generated_apps=Soldi,Sostanze

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
template_package=com.gernalix.androidapptemplate

MAP:
generator=create_android_app_from_template
entry=app/src/main/java/com/gernalix/androidapptemplate/MainActivity.kt
theme=app/src/main/java/com/gernalix/androidapptemplate/ui/theme/
manifest=app/src/main/AndroidManifest.xml
strings=app/src/main/res/values/strings.xml
build=app/build.gradle.kts,settings.gradle.kts,gradle/libs.versions.toml
metadata=dev/project.metadata.json

ARCH:
template=compilable Android project with neutral package/app name
generator=terminal-only Bash+rsync+Perl rewrite; no Android Studio required
copy_excludes=.git,.gradle,.kotlin,build,app/build,local.properties,README.md,dev

FLOW:
usage=/home/daniele/codex-workspace/android-app-template/create_android_app_from_template APP_NAME PACKAGE_NAME DESTINATION
rewrite=namespace,applicationId,Kotlin dirs,package declarations,imports,manifest theme,strings app_name,rootProject.name,instrumented package assertion
validation=run ./gradlew assembleDebug in generated destination

INV:
build_config_preserved=Gradle wrapper,AGP,Kotlin,Compose,libs.versions.toml,Android Studio stable config
clean_template=no source app package com.danielegalati.soldi remains
destination_rule=generator refuses existing non-empty destination
terminal_only=do not require Android Studio for generation/build

BUILD:
cmd=cd /home/daniele/codex-workspace/android-app-template && ./gradlew assembleDebug
result=PASS 2026-06-13
apk=/home/daniele/codex-workspace/android-app-template/app/build/outputs/apk/debug/app-debug.apk
apk_sha256=b1ac47ac9b3d9a2339766d9bff63937ad94e3fd03090531ed6daf13381110e95
warning=stripDebugDebugSymbols cannot strip libandroidx.graphics.path.so; packaged as-is
env=ANDROID_HOME=/home/daniele/Android/Sdk

TEST:
template_smoke=./gradlew assembleDebug PASS 2026-06-13
generator_smoke=generated Soldi and Sostanze; both assembleDebug PASS 2026-06-13
unit=starter ExampleUnitTest only
instrumented=starter ExampleInstrumentedTest not run on device

DATA:
storage=none
db=none
secrets=none

DNB:
item=do not add app-domain behavior to template|why=must remain reusable starter|test=MainActivity shows starter Greeting only
item=do not commit local.properties/build outputs|why=machine-specific/generated|test=git status --ignored
item=do not hand-edit generated apps for template bugs only|why=template drift|test=fix generator/template then regenerate

BUG:
known=none after template and generated app debug builds

RISK:
risk=package rewrite misses a text file|trigger=new file extension added|mitigation=extend generator find filter|test=rg old package in generated app
risk=destination overwrite|trigger=operator points to non-empty dir|mitigation=generator refuses non-empty destination|test=run with existing dir
risk=Android SDK env missing|trigger=no ANDROID_HOME/ANDROID_SDK_ROOT/local.properties|mitigation=set SDK env or create local.properties locally|test=./gradlew assembleDebug

ROAD:
now=use for fresh starter apps only
next=add generator self-test if template changes
later=optionally parameterize minSdk/package theme conventions

REUSE:
source=Soldi 2026-06-05 Android Studio starter app verified as no domain logic
reason=preserve Android Studio generated build/tooling stack exactly

LINK:
repo=/home/daniele/codex-workspace/android-app-template
metadata=/home/daniele/codex-workspace/android-app-template/dev/project.metadata.json
human_overview=/home/daniele/codex-workspace/MegaVault/human/projects/android-app-template/overview.md
human_roadmap=/home/daniele/codex-workspace/MegaVault/human/projects/android-app-template/roadmap.md
human_changelog=/home/daniele/codex-workspace/MegaVault/human/projects/android-app-template/changelog.md
human_troubleshooting=/home/daniele/codex-workspace/MegaVault/human/projects/android-app-template/troubleshooting.md

OPEN:
remote_origin=git@github.com:gernalix/android-app-template.git
