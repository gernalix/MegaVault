# soldi

META:
slug=soldi
name=Soldi
type=AndroidApp
status=preimpl
package=com.gernalix.soldi
platform=Android
lang=Kotlin
ui=Compose
db=SQLite(Room)
minSdk=29
philosophy=financial_quantified_self

VISION:
track_money+products+prices+places+wealth
not_classic_accounting
local_first
offline_first
sqlite_first
receipt_centric
product_centric
tag_based

CORE:
single_source_of_truth=sqlite
continuous_auto_export=required
full_import_export_parity=required
all_entities_searchable=yes
all_lists_sortable=yes
all_lists_filterable=yes
all_ids_stable=yes
timestamps=UTC_Z

FORBIDDEN:
mandatory_category_tree
forced_month_sections
cloud_dependency
hidden_data

DATA:

ACCOUNT:
id,name,currency,balance

TRANSACTION:
id,date,amount,account_id,title,description,notes,receipt_id,place_id,chain_id,balance_before,balance_after,impact_percent,photo_uri,created_at,updated_at

TAG:
id,name,is_archived

TRANSACTION_TAG:
transaction_id,tag_id

CHAIN:
id,name,aliases,is_archived

PLACE:
id,chain_id,name,address,lat,lon,radius,is_archived

RECEIPT:
id,chain_id,place_id,date,total,currency,source(manual|ocr|digital),verification_status

PRODUCT:
id,canonical_name,default_tags,is_archived

PRODUCT_ALIAS:
id,raw_name,product_id

RECEIPT_ITEM:
id,receipt_id,transaction_id,product_id,raw_name,quantity,unit,total_price,unit_price,cost_per_kg

TRANSACTION_LINK:
id,transaction_a_id,transaction_b_id,type,amount,note

LIFE_EVENT:
id,name,date,note

TRANSACTION_EVENT:
transaction_id,event_id

WEALTH_SNAPSHOT:
derived_not_stored

TAGS:
categories_replaced_by_tags=yes
unlimited_tags=yes
multi_tag=yes
tag_archive=yes
archived_not_suggested=yes
history_preserved=yes

WEALTH:
wealth=sum(all_accounts_converted_to_base_currency)
impact_percent=transaction_amount/wealth_at_transaction_time
balance_before_required=yes
balance_after_required=yes
rebuild_any_historical_date=yes
full_recalculation_allowed=yes

MULTI_CURRENCY:
multiple_account_currencies=yes
base_currency=user_defined
historical_fx_rates=planned
fallback=current_fx_allowed
wealth_always_computable=yes

LOCATION:
transaction_has_place=yes
transaction_has_chain=yes
gps_autodetect=yes
gps_suggest=yes
friendly_names=yes
example=Netto_vicino_casa

CHAINS:
Lidl
Netto
Rema1000
Føtex
Bilka
Apotek
other

RECEIPT_SYSTEM:
receipt_id_required_for_grouped_purchases
all_products_share_receipt_id
view_products=yes
view_receipts=yes
receipt_total_reconstructable=yes
bank_reconciliation=yes

BANK_RECONCILIATION:
group_by_receipt_id
compare(bank_total,receipt_total)
difference_visible
verification_status

PRODUCT_TRACKING:
product_level_transactions=yes
canonical_products=yes
aliases=yes
product_learning=yes
auto_tag_suggestions=yes
auto_product_mapping=yes

PRICE_MEMORY:
store(product,chain,place,date,price,cost_per_kg)
show_best_price=yes
show_historical_prices=yes
show_difference_percent=yes
show_cheapest_chain=yes

COST_PER_KG:
manual_entry=yes
receipt_import=yes
comparison_enabled=yes

OCR:
paper_receipts=yes
digital_receipts=yes
confirmation_screen_required=yes

OCR_FLOW:
receipt
->ocr
->parser
->product_match
->price_memory
->suggestions
->confirm
->save

DIGITAL_RECEIPTS:
preferred_over_paper=yes
structured_parsers=yes
chain_specific_parsers=yes

TRANSACTION_LINKS:
refund
reimbursement
correction
transfer
related

LINK_NAV:
bidirectional=yes
single_tap_jump=yes

MEDIA:
transaction_photo_optional=yes
product_photo_planned=yes

LINKS:
clickable_urls=yes

LISTS:
sort=date,amount,impact_percent,place,chain,account,tag,title
group=none,day,week,month,tag,place,chain,receipt

MONTH_UI:
forced=no

ANALYTICS:

PLACE_ANALYTICS:
ranking_by_spend
ranking_by_wealth_impact
map_view

CHAIN_ANALYTICS:
ranking_by_spend
price_comparison

PRODUCT_ANALYTICS:
best_price
avg_price
price_history
price_trend

WEALTH_ANALYTICS:
wealth_timeline
wealth_high
wealth_low
wealth_by_period

RECEIPT_ANALYTICS:
verification
missing_items
difference_tracking

MAP:
pins=places
metric=amount|impact_percent

PRICE_DECISION_ASSIST:
when_product_typed
show_best_price
show_chain
show_place
show_cost_per_kg
show_difference_percent

ENTRY_FLOW:
fast_entry
minimal_taps
autocomplete_everywhere
archived_hidden_by_default

SEARCH:
transactions
products
receipts
places
chains
tags
links

ARCHIVE:
tags
places
chains
products

LIFE_EVENTS:
attach_events_to_timeline
example=job_start,move,recovery,large_purchase
overlay_on_wealth_graph=yes

FUTURE:
impulse_spending_detection
spending_anomalies
work_hours_equivalent
salary_equivalent
behavior_patterns
advanced_learning

INV:
sqlite_is_truth
all_data_exportable
all_data_importable
no_category_tree
tags_primary_taxonomy
receipt_id_stable
entity_ids_stable
wealth_reconstructable
receipt_reconstructable
bank_comparable
product_history_preserved

SUCCESS:
build_pass
tests_pass
no_todo
no_placeholder
all_features_present
import_export_verified
ocr_pipeline_working
wealth_reconstruction_working
receipt_reconstruction_working

