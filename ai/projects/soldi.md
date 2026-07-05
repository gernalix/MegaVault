# soldi

META:
slug=soldi
name=Soldi
type=AndroidApp
status=active_capsule_v2
repo=/home/daniele/AndroidStudioProjects/Soldi
remote=git@github.com:gernalix/Soldi.git
branch=codex/prompt-739204-soldi-capsule
package=com.gernalix.soldi
platform=Android
lang=Kotlin
ui=Compose
db=SQLite(Room)
minSdk=29
version=2
apk=/home/daniele/AndroidStudioProjects/Soldi/app/build/outputs/apk/debug/2.apk
metadata=/home/daniele/AndroidStudioProjects/Soldi/dev/project.metadata.json
human_overview=/home/daniele/codex-workspace/MegaVault/human/projects/soldi/overview.md
human_roadmap=/home/daniele/codex-workspace/MegaVault/human/projects/soldi/roadmap.md
human_changelog=/home/daniele/codex-workspace/MegaVault/human/projects/soldi/changelog.md
human_troubleshooting=/home/daniele/codex-workspace/MegaVault/human/projects/soldi/troubleshooting.md

PURPOSE:
vision=track_money+products+prices+places+wealth;not_classic_accounting;financial_quantified_self
mode=local_first+offline_first+sqlite_first
taxonomy=tags_primary;no_category_tree
flow=receipt_centric+product_centric+transaction_centric
capsule=single app repo + Room DB + SAF SQLite vault + MegaVault docs

STACK:
android=AGP_9.2.1,Kotlin_2.2.10,Compose_BOM_2026.02.01,Room_2.8.4,KSP_2.2.10-2.0.2
versioning=version.txt integer source; app asset soldi-version.txt; versionCode/versionName derived as 2
i18n=res/values + res/values-it
build=./gradlew testDebugUnitTest assembleDebug assembleDebugAndroidTest
adb_tcl=QCGADUVOSSEYFES4 mDNS visible; pairing required before connected tests

MAP:
entry=app/src/main/java/com/gernalix/soldi/MainActivity.kt
db=app/src/main/java/com/gernalix/soldi/data/SoldiDatabase.kt
entities=app/src/main/java/com/gernalix/soldi/data/SoldiEntities.kt
dao=app/src/main/java/com/gernalix/soldi/data/SoldiDao.kt
repo=app/src/main/java/com/gernalix/soldi/data/SoldiRepository.kt
export=app/src/main/java/com/gernalix/soldi/data/SoldiExporter.kt
domain=app/src/main/java/com/gernalix/soldi/domain/*
tests=app/src/test/java/com/gernalix/soldi/SoldiCoreTest.kt;app/src/androidTest/java/com/gernalix/soldi/SoldiPersistenceInstrumentedTest.kt

DATA:
truth=internal Room SQLite /data/data/com.gernalix.soldi/databases/soldi.db
tables=settings,accounts,tags,transaction_tags,chains,places,receipts,products,product_aliases,transactions,receipt_items,transaction_links,life_events,transaction_events,price_memory
stable_ids=string ids with semantic seeds for defaults and UUID ids for user-created rows
timestamps=UTC_Z ISO_INSTANT in persisted date/created_at/updated_at fields
wealth_snapshot=derived_not_stored
base_currency=settings.base_currency default DKK
fallback_fx=settings.fallback_fx_EUR;historical_fx_status documents planned historical rates without breaking computability
archive=tags/chains/places/products keep rows and hide archived from active suggestion queries

EXPORT_IMPORT:
baseline=adapted from MultiTimeTracker SQLite vault contract
files=soldi.db,soldi.db.bak,soldi.db.tmp
autoexport=SAF folder selected by user; every repository mutation triggers throttled SQLite export when configured
manual_export=button exports current DB to configured SAF vault
manual_import=OpenDocument imports SQLite candidate after PRAGMA integrity_check and schema validation
atomicity=tmp copy -> validate -> bak -> promote -> validate; rollback from previous copy on failed promotion
parity=import/export is SQLite database copy, not reduced JSON/CSV projection

FEATURES:
transactions=fast entry,title,amount,account,tags,chain,place,notes,balance_before,balance_after,impact_percent,UTC_Z
accounts=default Cash DKK account; multi-currency-ready account model
tags=unlimited multi-tag relation and archive preservation
chains=default Lidl,Netto,Rema1000,Fotex,Bilka,Apotek,other plus aliases
places=friendly named places with chain/address/lat/lon/radius fields
receipts=OCR/manual text parser -> confirmation screen -> receipt + grouped bank transaction + receipt items
products=canonical products,aliases,price_memory from receipt lines
links=refund,reimbursement,correction,transfer,related supported by free type field and bidirectional one-tap jump
life_events=table and UI state included in analytics model; transaction_event relation present
analytics=place spend,chain spend,product best/avg price,receipt reconciliation,wealth current/high/low,map pins list
search_sort_filter=transactions query+sort; all feature lists shown with archive status and active queries in repository
month_ui=not forced

INV:
sqlite_is_truth=yes
all_data_exportable=yes
all_data_importable=yes
no_category_tree=yes
no_forced_month_sections=yes
no_cloud_dependency=yes
no_hidden_data=yes
receipt_id_stable=yes
entity_ids_stable=yes
wealth_reconstructable=yes
receipt_reconstructable=yes
bank_comparable=yes
product_history_preserved=yes
version_visible_home_footer=yes

TEST:
unit=PASS ./gradlew testDebugUnitTest; covers export policy, OCR parser, wealth reconstruction, receipt reconstruction, bidirectional link navigation
build=PASS ./gradlew assembleDebug; APK 2.apk sha256 8055e504cd865de7b2490cb9777ec47bc08d30c199118185b0efc731fd368ef4
android_test_build=PASS ./gradlew assembleDebugAndroidTest; includes SQLite export/import roundtrip test
tcl_status=BLOCKED until wireless debugging pairing code is provided; mdns pairing 192.168.1.200:36185 and connect 192.168.1.200:39737 observed 2026-06-18; adb connect failed before pairing
pixel_status=ignored for final validation per user instruction

DNB:
item=do not use Soldi as Android template source|why=Soldi is real app capsule|source=dev/project.metadata.json
item=do not add mandatory category tree|why=tags replace categories|test=Room schema has tags not categories
item=do not add cloud dependency|why=local/offline/sqlite first|test=only SAF user-selected export
item=do not store wealth snapshots as source truth|why=wealth is reconstructable from accounts/fx|test=WEALTH_SNAPSHOT derived_not_stored
item=do not bypass SQLite export parity|why=SQLite is truth|test=soldi.db vault copy

ROAD:
now=pair TCL and run connectedAndroidTest import/export roundtrip on TCL only
next=expand OCR with chain-specific digital parsers and add historical FX table/migrations
later=advanced behavior analytics,product photos,impulse/anomaly detection

OPEN:
tcl_pairing=needs live wireless debugging pairing code from device
historical_fx=planned structure documented; current fallback FX active
gps_autodetect=fields/UI present; runtime GPS permission/autodetect not wired yet
