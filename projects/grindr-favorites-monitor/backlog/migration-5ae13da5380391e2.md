# Migrare i media Grindr nel layout canonico per profilo

<!-- migration-5ae13da5380391e2 -->

Migrated project backlog. Project: **grindr-favorites-monitor**; project_id: 104.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 104.

Provenance: `wi:4faad2c6bc8c4875a931355791f33963`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Migrare i media Grindr nel layout canonico per profilo

Adottare il layout profile-media canonico per tutti i media, includendo migrazione una tantum idempotente dell’archivio esistente, nomi basati su hash, path relativi nel DB, metadata ricostruibili e conservazione dei media non più correnti. Verificare integrità e conteggi prima e dopo senza rimuovere gli originali prima del PASS.

status: pending

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "104",
      "reason": "canonical repository identity",
      "related_projects": [
        "104"
      ]
    },
    "source": {
      "work_item_id": "wi:4faad2c6bc8c4875a931355791f33963",
      "parent_id": null,
      "kind": "task",
      "title": "Migrare i media Grindr nel layout canonico per profilo",
      "objective": "Adottare il layout profile-media canonico per tutti i media, includendo migrazione una tantum idempotente dell’archivio esistente, nomi basati su hash, path relativi nel DB, metadata ricostruibili e conservazione dei media non più correnti. Verificare integrità e conteggi prima e dopo senza rimuovere gli originali prima del PASS.",
      "acceptance_json": "[]",
      "status": "pending",
      "executor_policy": "auto",
      "sort_order": null,
      "current_action": null,
      "next_action": null,
      "blocker": null,
      "project_id": null,
      "project_name": null,
      "repo": "gernalix/grindr-favorites-monitor",
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
        "work_item_id": "wi:4faad2c6bc8c4875a931355791f33963",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2203,
        "work_item_id": "wi:4faad2c6bc8c4875a931355791f33963",
        "evidence_kind": "issue_inbox",
        "label": "issue:14e134140b484269aaf68307c776a27b",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Grindr favorites monitor — adottare il nuovo layout canonico di profile-media per TUTTI i media, non solo quelli futuri, includendo una migrazione una tantum dell'archivio esistente.\\n\\nCriteri da applicare:\\n- root: /home/daniele/.local/state/grindr-favorites-monitor/profile-media/\\n- una directory per profile_id: profile-media/<profile_id>/\\n- dentro ogni profilo: metadata.json, media/, e thumbs/ solo se/finché servono thumbnail derivate\\n- nomi media stabili basati sul content hash, non su ordine, display name, timestamp o URL CDN\\n- hash completo conservato nei metadati/DB; filename stabile derivato dall'hash\\n- metadata.json come indice leggibile/ricostruibile dei media, non seconda fonte canonica concorrente al DB\\n- registrare path relativi nel DB, non path assoluti\\n- se un media sparisce dal profilo, non cancellarlo automaticamente: conservarlo nello storico e marcarlo non-current con first_seen_at/last_seen_at\\n- se ricompare contenuto identico, riusare lo stesso file\\n- thumbs/ è derivata e rigenerabile, quindi non canonica\\n- migrazione una tantum: individuare TUTTI i media già scaricati, attribuirli al relativo profile_id, calcolare/normalizzare hash e nome file, spostarli nel nuovo layout, generare/aggiornare metadata.json e riferimenti DB senza perdita né duplicazioni\\n- la migrazione deve essere idempotente e verificare integrità/conteggi prima e dopo, senza cancellare gli originali finché la verifica finale non passa.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:14e134140b484269aaf68307c776a27b\", \"observed_at_ms\": 1790742801373, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"grindr-favorites-monitor\"}",
        "created_at": "2026-09-30T10:36:29Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:14e134140b484269aaf68307c776a27b",
        "work_item_id": "wi:4faad2c6bc8c4875a931355791f33963",
        "role": "decision",
        "created_at": "2026-09-30T04:33:21Z"
      }
    ]
  }
]
```
