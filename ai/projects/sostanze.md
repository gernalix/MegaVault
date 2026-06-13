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
last_prompt=294816

PURPOSE:
domain=farmaci,integratori,scorte,prescrizioni,interazioni,assunzioni
stage=MVP implemented from existing Android project
implemented_features=Home Events-style intake grid,Room persistence,stock coverage,prescription refill dates,interaction blocks,undo last intake,notification scheduling hooks,ImportExport SAF live SQLite,TCL smoke
non_features=no CSV export UI yet,no full interaction-specific-target editor,no medical advice defaults

STACK:
platform=Android
lang=Kotlin
ui=Jetpack Compose Material3
build=Gradle wrapper
db=Room SQLite
agp=9.2.1
kotlin=2.2.10
compose_bom=2026.02.01
compileSdk=36.1
minSdk=29
package=com.gernalix.sostanze

MAP:
entry=app/src/main/java/com/gernalix/sostanze/MainActivity.kt
ui=app/src/main/java/com/gernalix/sostanze/ui/SostanzeApp.kt
vm=app/src/main/java/com/gernalix/sostanze/ui/SostanzeViewModel.kt
db=app/src/main/java/com/gernalix/sostanze/data/Entities.kt,app/src/main/java/com/gernalix/sostanze/data/SostanzeDao.kt,app/src/main/java/com/gernalix/sostanze/data/SostanzeDatabase.kt
repo=app/src/main/java/com/gernalix/sostanze/data/SostanzeRepository.kt
domain=app/src/main/java/com/gernalix/sostanze/domain/SostanzeEngine.kt
notifications=app/src/main/java/com/gernalix/sostanze/notifications/SostanzeNotificationScheduler.kt
theme=app/src/main/java/com/gernalix/sostanze/ui/theme/
manifest=app/src/main/AndroidManifest.xml
strings=app/src/main/res/values/strings.xml
build=app/build.gradle.kts,settings.gradle.kts,gradle/libs.versions.toml
metadata=dev/project.metadata.json
tests=app/src/test/java/com/gernalix/sostanze/domain/SostanzeEngineTest.kt,app/src/androidTest/java/com/gernalix/sostanze/ExampleInstrumentedTest.kt

ARCH:
current=single Activity Compose app with ViewModel+capsule APIs+Room+pure domain engine
state=SostanzeViewModel combines Room flows with minute ticker into SostanzeUiState
ui=Home/Scorte/Prescrizioni/Interazioni tabs; Home reuses MultiTimeTracker Events compact button-grid workflow
domain=SostanzeEngine owns scheduling,stock,refill,interaction,countdown,notification-plan math
boundary=no medical hardcoding; app applies user-entered rules only
reuse_source=/home/daniele/codex-workspace/projects/MultiTimeTracker Events/QuickEvents
import_export=ImportExport capsule owns SAF tree URI,SQLite validation,live overwrite,import replacement; repository must not know SAF/URI/SostanzeDataPorter

FLOW:
launch=Launcher -> MainActivity -> SostanzeTheme -> SostanzeApp
home=Room substances/intakes/rules -> dose states -> Events-style action buttons grouped by Da prendere oggi,Prossima dose piu tardi,Bloccate da interazione,Presi oggi,PRN
intake=tap dose button -> intake_events insert -> stock decrement -> stock_adjustments insert
undo=overflow Undo ultimo tap -> latest intake delete -> stock restore -> stock_adjustments note
stock=Scorte row tap -> +/- dialog -> stock_adjustments + substances.stock_current
prescriptions=quantity/refill months -> next refill date=date+N months
interactions=user rule avoid_before/avoid_after -> ALL_PRESENT_AND_FUTURE or specific targets -> blocked section + countdown + notification plan
build=Gradle wrapper -> Android plugin -> debug APK
seed=empty DB seeds Pregabalin 3/die,Vitamina D 1/die,Psyllium 1/die all-future 2h rule,Ibuprofene PRN

REUSE:
source=MultiTimeTracker Events implementation
reused=two-column LazyVerticalGrid,search/filter control shape,section headers,compact action cards,overflow menu,long-tap edit pattern,collapsible recent/taken section,bounded recent snapshot principle,stable sorting
adapted=QuickEventTemplateButton -> DoseActionButton; QuickEventEntryRow -> stock/prescription cards; QuickEventsCapsuleViewModel snapshot flow -> SostanzeViewModel state flow
rewritten=storage because prompt requires Room while MTT Events uses SnapshotSqlite custom SQLite; domain rules because medication stock/interactions differ from generic quick events

INV:
git=repo initialized at /home/daniele/AndroidStudioProjects/Sostanze on branch main
identity=namespace/applicationId/package/test assertion must stay com.gernalix.sostanze
app_name=res string must stay Sostanze until product rename requested
domain=no hardcoded medical advice or interaction semantics beyond user-entered rules
reuse=Home should remain visually/workflow-close to MultiTimeTracker Events
device_test=prompt 739284 uses TCL 6102H serial 192.168.1.200:45699; Pixel not used
ignore=.gitignore excludes build outputs,.gradle,.kotlin,local.properties,APK artifacts,IDE transient files

BUILD:
cmd=cd /home/daniele/AndroidStudioProjects/Sostanze && ./gradlew --no-daemon --console=plain testDebugUnitTest assembleDebug
result=PASS 2026-06-13 prompt 294816
version=4
apk=/home/daniele/AndroidStudioProjects/Sostanze/output/4.apk
apk_sha256=e596fc4dc85ccf55abfea5e923bf9689d9652c2b280d1aed4a231400925c6f66
warning=stripDebugDebugSymbols cannot strip libandroidx.graphics.path.so; packaged as-is
env=ANDROID_HOME=/home/daniele/Android/Sdk

TEST:
unit=./gradlew --no-daemon --console=plain testDebugUnitTest PASS; SostanzeEngineTest+CapsuleArchitectureTest 12 tests 0 failures
unit_cases=1/die,3/die,next_interval,stock_decrement,adjustment_plus_minus,days_covered,refill_months,psyllium_block,ALL_PRESENT_AND_FUTURE future target,countdown,interaction_notification_plan,UTC_Z_export_dates,capsule_guardrail
compile=:app:compileDebugKotlin PASS
smoke=assembleDebug PASS 2026-06-13
tcl_device=192.168.1.200:45699 model 6102H; install PASS; am start PASS; UI dump shows Sostanze v4 and Export active: sostanze.db
live_saf=/sdcard/Download/SostanzeSafLive persisted tree URI verified; folder final content only sostanze.db hash 38ab726e size 143360
overwrite_evidence=baseline e3dcadd2 -> macro 2eb35ee6 -> undo 891591c7 -> intake 4b87702a -> stock 4411523b; mtime changed and folder stayed single-file
import_valid=autoexport import restored state to intake_events=2 stock_adjustments=10 Pregabalin.stock_current=30.0 integrity_check=ok hash 8f68760d
import_invalid=bad SQLite rejected with missing-schema UI error; SAF hash stayed 8f68760d
pixel=not used per operator instruction
instrumented=starter ExampleInstrumentedTest still present; not run in prompt 739284

DATA:
storage=Room SQLite app DB
db_name=sostanze.db
tables=substances,intake_events,stock_adjustments,prescriptions,interaction_rules,interaction_targets,notification_state,settings,macros,macro_items
foreign_keys=yes on intake_events,stock_adjustments,prescriptions,interaction_rules,interaction_targets
backup=Android allowBackup true; explicit app export not implemented
export=SAF live SQLite fixed filename sostanze.db implemented; CSV still future
migration=Room schema version 3; schema export currently disabled

DNB:
item=do not commit local.properties/build outputs/APKs|why=machine-specific/generated|test=git status --ignored
item=do not change package casually|why=application identity|test=rg com.gernalix.sostanze app dev
item=do not add medical advice defaults|why=user owns interaction rules|test=review seed/docs/code
item=do not port MultiTimeTracker SnapshotSqlite blindly|why=Room required|test=Room annotations present
item=do not test prompt 739284 on Pixel unless user changes instruction|why=operator said use TCL|test=adb -s 192.168.1.200:45699

BUG:
known=Material3 TabRow deprecation warning; non-blocking
known=notification alarm delivery not end-to-end waited in device smoke

RISK:
risk=seed demo data appears on empty DB|trigger=first install|mitigation=replace with onboarding later|test=seedIfEmpty
risk=notification exactness varies by device policy|trigger=AlarmManager under idle/vendor restrictions|mitigation=future WorkManager/exact-alarm decision|test=notification delivery smoke
risk=Room schema export disabled|trigger=future migrations|mitigation=enable schema directory before v2|test=DB version bump checklist
risk=remote is private GitHub repo|trigger=cloning from unauthenticated host|mitigation=use authenticated SSH/GitHub access|test=git ls-remote origin refs/heads/main

ROAD:
now=prompt 294816 ImportExport live SAF validated
next=full CRUD for prescriptions/interactions,specific interaction target UI,CSV export action,notification delivery smoke
later=onboarding,Room schema export/migrations,accessibility/localization polish

LINK:
repo=/home/daniele/AndroidStudioProjects/Sostanze
metadata=/home/daniele/AndroidStudioProjects/Sostanze/dev/project.metadata.json
local_ai=/home/daniele/AndroidStudioProjects/Sostanze/dev/ai/INDEX.md
template_ai=/home/daniele/codex-workspace/MegaVault/ai/projects/android-app-template.md
human_overview=/home/daniele/codex-workspace/MegaVault/human/projects/sostanze/overview.md
human_roadmap=/home/daniele/codex-workspace/MegaVault/human/projects/sostanze/roadmap.md
human_changelog=/home/daniele/codex-workspace/MegaVault/human/projects/sostanze/changelog.md
human_troubleshooting=/home/daniele/codex-workspace/MegaVault/human/projects/sostanze/troubleshooting.md

OPEN:
export_ui=implemented via DocumentsUI picker
notification_alarm_delivery=not fully device-wait tested
specific_interaction_target_editor=not implemented
remote_origin=git@github.com:gernalix/Sostanze.git
