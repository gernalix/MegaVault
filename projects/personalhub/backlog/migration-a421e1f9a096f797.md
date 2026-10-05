# Identità canoniche stabili per le entità PersonalHub

<!-- migration-a421e1f9a096f797 -->

Migrated project backlog. Project: **personalhub**; project_id: 49.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 49.

Provenance: `wi:6e571be01bf14bf1abd45fc3a9295006`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Identità canoniche stabili per le entità PersonalHub

Rendere gli oggetti PersonalHub indirizzabili con ID canonici stabili tra PersonalHub, PersonalHub-data e repository esterni. Applicare la classificazione delle tabelle, migrazione additiva con mappa verificabile, dual-write compatibile, migrazione dei riferimenti e cutover reversibile come specificato nella cattura.

status: pending

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "49",
      "reason": "canonical repository identity",
      "related_projects": [
        "49"
      ]
    },
    "source": {
      "work_item_id": "wi:6e571be01bf14bf1abd45fc3a9295006",
      "parent_id": null,
      "kind": "task",
      "title": "Identità canoniche stabili per le entità PersonalHub",
      "objective": "Rendere gli oggetti PersonalHub indirizzabili con ID canonici stabili tra PersonalHub, PersonalHub-data e repository esterni. Applicare la classificazione delle tabelle, migrazione additiva con mappa verificabile, dual-write compatibile, migrazione dei riferimenti e cutover reversibile come specificato nella cattura.",
      "acceptance_json": "[]",
      "status": "pending",
      "executor_policy": "auto",
      "sort_order": null,
      "current_action": null,
      "next_action": null,
      "blocker": null,
      "project_id": null,
      "project_name": null,
      "repo": "gernalix/PersonalHub",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-30T10:36:29Z",
      "updated_at": "2026-09-30T10:36:29Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:6e571be01bf14bf1abd45fc3a9295006",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2198,
        "work_item_id": "wi:6e571be01bf14bf1abd45fc3a9295006",
        "evidence_kind": "issue_inbox",
        "label": "issue:93176b8791fc48178f436e1de8497539",
        "uri": "personal-hub-chat",
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"PH canonical identity design\\nGoal: make every PH object that can be referenced outside its local table/module addressable through one stable canonical ID shared by PersonalHub, PersonalHub-data and external repos.\\n\\nVerified baseline (PersonalHub-data schema v23 / app v63):\\n- contacts: INTEGER local PK + UNIQUE public_id; current data has 95/95 non-null and distinct public_id values, but schema still permits NULL.\\n- places: uuid TEXT PRIMARY KEY; already compliant.\\n- hub_entity_bindings contains canonical_id but is not exhaustive, so it cannot be the master identity registry.\\n- substances: INTEGER PK + UNIQUE canonical_name; canonical_name is a business key, not immutable identity.\\n- finance_transactions/products have UNIQUE uuid but local INTEGER PK; finance_products currently permits default empty uuid.\\n- finance_chains/titles/tags rely on INTEGER IDs and names.\\n- finance_transactions.personId and finance_recurrences.personId use INTEGER references instead of canonical People identity.\\n- Timer / Since When primary objects still largely use INTEGER IDs.\\n\\n1. CANONICAL ID CONTRACT\\n- Canonical identity type: TEXT, NOT NULL, UNIQUE, immutable.\\n- Generated once at object creation; never derived from name, phone, canonical_name, timestamp, rowid, repo path or local INTEGER PK.\\n- Never reused after deletion. Tombstones retain the ID.\\n- Existing stable IDs are preserved exactly; no cosmetic rewrites.\\n- Consumers treat IDs as opaque strings. New IDs use a common globally unique generator (UUID v4 is sufficient).\\n- Local INTEGER PKs may remain inside SQLite/Room for performance, but must never be the identity crossing module/repo boundaries.\\n- Cross-domain PH references (e.g. Soldi -> People) must use canonical IDs too.\\n- Wire contract: {entity_kind, canonical_id}. Established columns such as contacts.public_id or places.uuid may remain physically named as-is, but adapters/schema metadata declare them as canonical_id.\\n- Pure junction/cache/sync/UI-state rows are exempt unless they become externally addressable.\\n- Merge: one survivor canonical ID; losing IDs become permanent aliases to the survivor.\\n- Split: newly separated entities get new IDs; the original ID stays with the explicitly selected continuation.\\n- Restore/import preserves canonical IDs; collision with a different entity is a hard integrity error, never auto-renumber.\\n- History/change payloads carry entity_kind + canonical_id in addition to local row keys.\\n- Automated invariants: not-null, uniqueness, immutability, export/import stability, no alias cycles, no cross-boundary local INTEGER identity leakage.\\n2. EXTERNAL IDENTITY REGISTRY\\nCreate an exhaustive canonical registry separate from hub_entity_bindings.\\n\\nhub_entities\\n- canonical_id TEXT PRIMARY KEY\\n- entity_kind TEXT NOT NULL\\n- owning_module TEXT NOT NULL\\n- local_table TEXT NOT NULL\\n- local_key TEXT NOT NULL\\n- lifecycle TEXT NOT NULL (ACTIVE/TOMBSTONED/MERGED)\\n- created_at INTEGER NOT NULL\\n- updated_at INTEGER NOT NULL\\n- UNIQUE(owning_module, local_table, local_key)\\nEvery canonical-addressable object must be present here. hub_entity_bindings remains the UI/tag/context binding layer and references canonical identity; its own id is not entity identity.\\n\\nhub_external_identities\\n- id TEXT PRIMARY KEY\\n- canonical_id TEXT NOT NULL REFERENCES hub_entities(canonical_id)\\n- entity_kind TEXT NOT NULL\\n- system TEXT NOT NULL\\n- source_scope TEXT NOT NULL\\n- external_id TEXT NOT NULL\\n- external_id_normalized TEXT NULL\\n- link_method TEXT NOT NULL\\n- first_seen_at / last_seen_at / verified_at INTEGER NULL\\n- lifecycle TEXT NOT NULL (ACTIVE/RETIRED)\\n- metadata_json TEXT NULL\\n- created_at / updated_at INTEGER NOT NULL\\n- UNIQUE(system, source_scope, external_id)\\nRules: one external tuple resolves to at most one canonical entity; one entity may have many external identities; do not store auth secrets; normalize only where provider-specific rules are authoritative; ambiguous matching may propose a link but must not silently merge entities.\\n\\nhub_entity_aliases\\n- alias_canonical_id TEXT PRIMARY KEY\\n- canonical_id TEXT NOT NULL REFERENCES hub_entities(canonical_id)\\n- reason TEXT NULL\\n- created_at INTEGER NOT NULL\\nUse for canonical merges and legacy redirects. Resolution must be deterministic and cycle-free.\\n\\nExample: Grindr profile_id 743178098 remains the provider-native ID and maps via hub_external_identities to the PH People canonical ID. External repos should store both their native ID and the PH canonical ID when linked.\\n3. MIGRATION PLAN FOR NON-CONFORMING MODULES\\n\\nPeople\\n- contacts.public_id becomes NOT NULL, UNIQUE and immutable; it is the canonical person ID.\\n- Preserve every existing public_id. Investigate/classify the qa-overlay-* row before propagating it.\\n- Register every contact in hub_entities; hub_entity_bindings coverage must not gate registration.\\n- Migrate all cross-module person references to canonical People ID.\\n- finance_transactions.personId and finance_recurrences.personId -> person_canonical_id TEXT, validated against People canonical identity.\\n- contact_fields, initiatives, messaging links, photos and tag joins remain subordinate/local unless another repo needs to address those child rows directly.\\n- saved_searches.public_id: enforce canonical invariants only if saved searches are shared/exported; otherwise classify as local config.\\n\\nPlaces\\n- places.uuid is canonical already. Preserve all values and register all places.\\n- Existing references to places.uuid remain valid.\\n- place_events.event_uuid is the stable event ID; enforce non-null/unique.\\n- Legacy place_tags/place_tag_cross_ref should converge on unified hub_tags rather than gain a parallel identity system.\\n- aliases/links/geofence/cache rows remain subordinate/internal.\\n\\nSubstances\\n- Add public_id/canonical_id TEXT NOT NULL UNIQUE to substances; backfill each current row once with a generated UUID and persist the mapping.\\n- canonical_name stays a mutable normalized business key, not identity.\\n- Register all substances in hub_entities.\\n- Exports/APIs stop exposing substance_id as ecosystem identity.\\n- Intake events, prescriptions, interaction rules and macros get stable public/event IDs only if addressable outside the module; macro_items, interaction_targets and junction rows remain local.\\n\\nSoldi\\n- finance_accounts.id is already stable TEXT: formally declare it canonical and register accounts.\\n- finance_transactions.uuid and finance_products.uuid are canonical; enforce NOT NULL, UNIQUE, non-empty and immutable. Remove products default empty uuid and generate on insert.\\n- Add canonical/public IDs to finance_chains, finance_titles and finance_tags; names remain business keys.\\n- finance_transfers, finance_macros, finance_recurrences, finance_attachments and finance_owned_items already use stable TEXT IDs/uuid: validate non-empty/immutability and register when externally addressable.\\n- finance_stores correctly keys by places.uuid.\\n- Migrate all personId fields to People canonical ID; keep placeId canonical.\\n- Junction tables retain composite local keys.\\nTimer / Quick Events\\n- Add canonical/public IDs to sessions, quick_event_templates, quick_event_macros and quick_event_entries; keep INTEGER IDs as local compatibility keys.\\n- saved_searches.public_id already exists: enforce canonical invariants if it is exported/shared.\\n- Template fields, field values and junction rows remain subordinate unless external targeting is required.\\n- Legacy integer tags converge on hub_tags; do not create a competing tag identity system.\\n- All future exported Timer references use canonical IDs.\\n\\nSince When\\n- Add canonical/public ID to since_when_counters and register all counters.\\n- source_entity_id must store the source entity canonical ID paired with source_entity_type/entity_kind; migrate legacy local IDs through an explicit map.\\n- since_when_migration_state remains internal.\\n\\nWordPulse\\n- Treat wordpulse_sessions.id as canonical only after validating generator, non-empty uniqueness and immutability; register sessions only if cross-module/repo addressable.\\n- word_entries remain high-volume subordinate rows unless a concrete external-reference requirement appears; do not add UUIDs merely for cosmetic uniformity.\\n\\nHub / Tags / Contexts / Alerts\\n- Existing stable TEXT IDs for hub_tags, hub_contexts, hub_resources, alert_rules and similar durable Hub objects remain canonical where semantically appropriate.\\n- Populate hub_entities exhaustively.\\n- hub_entity_bindings references canonical IDs and remains a binding/index layer; never use hub_entity_bindings.id as the identity of the underlying object.\\n- Clarify hub_context_members naming/semantics: distinguish canonical entity ID from binding ID and migrate to canonical reference if it currently stores binding IDs.\\n- Tag assignments may still target bindings where binding semantics are required, provided every binding resolves to exactly one canonical entity.\\n\\nHistory / audit / system\\n- Stable event UUIDs remain event identities; enforce uniqueness where missing if events are externally addressable.\\n- backup_metadata, sync_*, hub_sync_*, snapshots, caches, settings, notification_state, derived/integrity/global stats and UI prefs are explicitly exempt.\\n\\nPhased rollout\\n0. Publish contract and table classification; freeze new cross-repo references based on local INTEGER IDs.\\n1. Add hub_entities, hub_external_identities, hub_entity_aliases and additive canonical columns/constraints.\\n2. One-time backfill: preserve all existing stable IDs; generate IDs only where absent. Emit a machine-readable old_local_id -> canonical_id migration map for each affected table.\\n3. Dual-write canonical + legacy local references where compatibility with old app versions requires it.\\n4. Migrate PersonalHub-data export/import, history payloads and all cross-repo integrations to entity_kind + canonical_id. Populate external mappings without heuristic merges.\\n5. Migrate internal cross-domain references such as Soldi -> People and Since When -> source entities.\\n6. Validate and cut over; retire legacy external use of local IDs only after all consumers pass.\\n\\nAcceptance criteria\\n- Every canonical-addressable object has exactly one immutable canonical ID.\\n- hub_entities coverage is 100% for canonical-addressable live/tombstoned objects.\\n- Every external identity maps to zero or one canonical entity; ambiguity is prevented by constraints.\\n- People, Places, Substances, Soldi, Timer, Since When, WordPulse where applicable, Hub/Tags/Contexts and Alerts are explicitly classified compliant or migrated.\\n- No cross-repo payload uses a local INTEGER PK as identity.\\n- No PH cross-domain reference depends on another domain's local INTEGER PK.\\n- Existing People public_id and Places uuid values remain unchanged.\\n- Export/import round-trip preserves canonical IDs and alias resolution.\\n- Tests cover nulls, duplicates, immutability, alias cycles, orphan external identities, collision handling and migration-map completeness.\\n- Migration remains additive/reversible until final cutover and does not destructively rewrite existing PersonalHub-data history.\\n\", \"executor\": null, \"executor_ref\": \"personal-hub-chat\", \"issue_id\": \"issue:93176b8791fc48178f436e1de8497539\", \"observed_at_ms\": 1790740525787, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"PersonalHub\"}",
        "created_at": "2026-09-30T10:36:29Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:93176b8791fc48178f436e1de8497539",
        "work_item_id": "wi:6e571be01bf14bf1abd45fc3a9295006",
        "role": "decision",
        "created_at": "2026-09-30T03:55:25Z"
      }
    ]
  }
]
```
