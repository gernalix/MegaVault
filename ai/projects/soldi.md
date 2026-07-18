# SOLDI
VERSION=1
STATUS=PREIMPL
FORMAT=ultracompressed

META:
slug=soldi;name=Soldi;type=AndroidApp;package=com.gernalix.soldi;platform=Android;lang=Kotlin;ui=Compose;db=SQLite(Room);minSdk=29
philosophy=financial_quantified_self

VISION:
scope=money+products+prices+places+wealth
mode=local_first+offline_first+sqlite_first+receipt_centric+product_centric+tag_based
not=classic_accounting

CORE:
truth=SQLite
sync=continuous_auto_export+full_import_export_parity
entities=searchable;lists=sortable+filterable;ids=stable;timestamps=UTC_Z
forbidden=mandatory_category_tree+forced_month_sections+cloud_dependency+hidden_data

DATA:
ACCOUNT=id,name,currency,balance
TRANSACTION=id,date,amount,account_id,title,description,notes,receipt_id,place_id,chain_id,balance_before,balance_after,impact_percent,photo_uri,created_at,updated_at
TAG=id,name,is_archived
TRANSACTION_TAG=transaction_id,tag_id
CHAIN=id,name,aliases,is_archived
PLACE=id,chain_id,name,address,lat,lon,radius,is_archived
RECEIPT=id,chain_id,place_id,date,total,currency,source(manual|ocr|digital),verification_status
PRODUCT=id,canonical_name,default_tags,is_archived
PRODUCT_ALIAS=id,raw_name,product_id
RECEIPT_ITEM=id,receipt_id,transaction_id,product_id,raw_name,quantity,unit,total_price,unit_price,cost_per_kg
TRANSACTION_LINK=id,transaction_a_id,transaction_b_id,type,amount,note
LIFE_EVENT=id,name,date,note
TRANSACTION_EVENT=transaction_id,event_id
WEALTH_SNAPSHOT=derived_not_stored

TAGS:
taxonomy=categories_replaced_by_unlimited_multi_tags
archive=yes;archived_suggestions=no;history=preserved

WEALTH:
formula=sum(all_accounts_converted_to_base_currency)
impact_percent=transaction_amount/wealth_at_transaction_time
required=balance_before+balance_after
rebuild=any_historical_date;full_recalculation=yes

CURRENCY:
accounts=multiple_currencies;base=user_defined;historical_fx=planned;fallback=current_fx_allowed;wealth_always_computable=yes

LOCATION:
transaction=place+chain;gps=autodetect+suggest;names=friendly;example=Netto_vicino_casa
chains=Lidl+Netto+Rema1000+Føtex+Bilka+Apotek+other

RECEIPTS:
group=receipt_id_required;all_products_share_receipt_id
views=products+receipts;total=reconstructable;bank_reconciliation=yes
bank_reconciliation=group_by_receipt_id;compare(bank_total,receipt_total);difference_visible;verification_status

PRODUCTS:
tracking=product_level_transactions+canonical_products+aliases+learning+auto_tag_suggestions+auto_mapping
price_memory=product+chain+place+date+price+cost_per_kg
price_views=best+historical+difference_percent+cheapest_chain
cost_per_kg=manual_entry+receipt_import+comparison

OCR:
inputs=paper+digital;confirmation_required=yes
flow=receipt>ocr>parser>product_match>price_memory>suggestions>confirm>save
digital=preferred+structured_parsers+chain_specific_parsers

LINKS:
transaction_types=refund+reimbursement+correction+transfer+related
navigation=bidirectional+single_tap
URLs=clickable
media=transaction_photo_optional+product_photo_planned

LISTS:
sort=date+amount+impact_percent+place+chain+account+tag+title
group=none+day+week+month+tag+place+chain+receipt
forced_month_ui=no

ANALYTICS:
place=spend_ranking+wealth_impact_ranking+map
chain=spend_ranking+price_comparison
product=best_price+avg_price+price_history+price_trend
wealth=timeline+high+low+period
receipt=verification+missing_items+difference_tracking
map=pins:places;metric=amount|impact_percent

UX:
price_assist=on_product_input>best_price+chain+place+cost_per_kg+difference_percent
entry=fast+minimal_taps+autocomplete+archived_hidden
search=transactions+products+receipts+places+chains+tags+links
archive=tags+places+chains+products

LIFE_EVENTS:
timeline=yes;examples=job_start+move+recovery+large_purchase;wealth_graph_overlay=yes

FUTURE:
features=impulse_spending_detection+spending_anomalies+work_hours_equivalent+salary_equivalent+behavior_patterns+advanced_learning

INV:
inv=SQLite_truth+all_data_exportable+importable+no_category_tree+tags_primary_taxonomy+stable_receipt/entity_IDs+reconstructable_wealth/receipts+bank_comparable+product_history_preserved

SUCCESS:
gate=build+tests+no_TODO+no_placeholder+all_features+verified_import/export+OCR+wealth_reconstruction+receipt_reconstruction
