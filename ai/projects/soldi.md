META
project=Soldi
type=Android app
path=/home/daniele/AndroidStudioProjects/Soldi
rule=Codex must read this file before every future modification.

PURPOSE
scope=personal finance / expenses / transactions app
stage=initial Android Studio project

STACK
platform=Android
build=Gradle wrapper
lang=Kotlin

MAP
root=/home/daniele/AndroidStudioProjects/Soldi
app=app/
gradle=gradlew,settings.gradle.kts,build.gradle.kts,gradle/libs.versions.toml

ARCH
state=not designed yet
constraint=no app functionality changes unless explicitly requested

FLOW
current=Android Studio starter app

INV
git=local repo initialized 2026-06-05
ignore=.gitignore excludes build outputs,.gradle,local.properties,IDE transient files,generated APKs

BUILD
cmd=./gradlew assembleDebug
result=PASS 2026-06-05
apk=app/build/outputs/apk/debug/app-debug.apk
note=strip warning for libandroidx.graphics.path.so; APK packaged as-is

TEST
debug_build=./gradlew assembleDebug

DATA
domain=finances,expenses,transactions
storage=TBD

DNB
do_not=change app behavior during setup-only work
do_not=commit local.properties or generated build outputs

BUG
known=none after initial debug build

RISK
risk=parent /home/daniele git repo exists; use Soldi local .git for project commits

ROAD
next=define MVP screens,data model,persistence,tests

LINK
human_overview=/home/daniele/codex-workspace/MegaVault/human/projects/soldi/overview.md
human_changelog=/home/daniele/codex-workspace/MegaVault/human/projects/soldi/changelog.md

OPEN
package_id=TBD
architecture=TBD
persistence=TBD
