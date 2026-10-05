# Snapshot orari dei profili Grindr con chat recenti

<!-- migration-54bcd4167e9990f7 -->

Migrated project backlog. Project: **grindr-favorites-monitor**; project_id: 104.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 104.

Provenance: `wi:f0066b6c940b4d90b3981610312cb3b3`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Snapshot orari dei profili Grindr con chat recenti

Completare e integrare un servizio Fedora resiliente che ogni ora crea snapshot di tutti i profili attualmente nei Favorites Grindr con attività chat negli ultimi 7 giorni. Preferire la tab Grindr autenticata già aperta nel Chrome normale tramite RDC/Chrome bridge; usare il browser dedicato :9444 solo come fallback. Correggere profileStore.fetchOne(id,true) che può restituire undefined recuperando il profilo dalla cache/store e verificando profileId. Verificare run live end-to-end, target recenti, media, read-only/fail-closed, lock e timer systemd hourly enabled/active, test e integrazione repo-task single-writer. Conservare la documentazione dell’incidente 2026-09-29 in cui fu ignorata la tab Chrome autenticata.

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
      "work_item_id": "wi:f0066b6c940b4d90b3981610312cb3b3",
      "parent_id": null,
      "kind": "task",
      "title": "Snapshot orari dei profili Grindr con chat recenti",
      "objective": "Completare e integrare un servizio Fedora resiliente che ogni ora crea snapshot di tutti i profili attualmente nei Favorites Grindr con attività chat negli ultimi 7 giorni. Preferire la tab Grindr autenticata già aperta nel Chrome normale tramite RDC/Chrome bridge; usare il browser dedicato :9444 solo come fallback. Correggere profileStore.fetchOne(id,true) che può restituire undefined recuperando il profilo dalla cache/store e verificando profileId. Verificare run live end-to-end, target recenti, media, read-only/fail-closed, lock e timer systemd hourly enabled/active, test e integrazione repo-task single-writer. Conservare la documentazione dell’incidente 2026-09-29 in cui fu ignorata la tab Chrome autenticata.",
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
      "created_at": "2026-09-30T10:13:05Z",
      "updated_at": "2026-09-30T10:13:05Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:f0066b6c940b4d90b3981610312cb3b3",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2133,
        "work_item_id": "wi:f0066b6c940b4d90b3981610312cb3b3",
        "evidence_kind": "issue_inbox",
        "label": "issue:c4c7901ee6e54427a31ac75e2316ce0e",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Completa e integra il servizio Fedora resiliente che ogni ora crea snapshot di tutti i profili attualmente nei Favorites Grindr con attività chat negli ultimi 7 giorni. Preferire la tab Grindr autenticata già aperta nel Chrome normale tramite RDC/Chrome bridge; usare il browser dedicato :9444 solo come fallback. Correggere il bug corrente per cui profileStore.fetchOne(id,true) può restituire undefined: recuperare il profilo dalla cache/store dopo fetch, verificando rigorosamente profileId. Verificare run live end-to-end sui target recenti, media, read-only/fail-closed, lock, systemd timer hourly enabled/active, test e integrazione tramite repo-task single-writer. Conservare la documentazione dell'incidente 2026-09-29 in cui la tab autenticata del Chrome normale fu ignorata a favore del browser dedicato scaduto.\\n\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:c4c7901ee6e54427a31ac75e2316ce0e\", \"observed_at_ms\": 1790707217030, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"/home/daniele/projects/grindr-favorites-monitor\"}",
        "created_at": "2026-09-30T10:13:05Z"
      },
      {
        "evidence_id": 2405,
        "work_item_id": "wi:f0066b6c940b4d90b3981610312cb3b3",
        "evidence_kind": "issue_inbox",
        "label": "issue:d61d117cdaf74c20b0558b3f4cbb6642",
        "uri": "codex://threads/01a0f296-d084-7f52-b5ac-330501c88689",
        "value_json": "{\"chat_url\": \"codex://threads/01a0f296-d084-7f52-b5ac-330501c88689\", \"code_location\": null, \"description\": \"Candidato comando emerso dal thread Codex 01a0f296-d084-7f52-b5ac-330501c88689: incapsulare il workflow ricorrente \\\"profilo Grindr attualmente aperto → identifica profile_id dalla risposta autenticata/router → attribuisci account sorgente (es. tcl/pixel) → salva snapshot append-only → scarica/collega media → restituisci metadati, path e diff\\\". Oggi richiede più passaggi e discovery di entrypoint/schema/debug bridge; un comando unico parametrico ridurrebbe latenza ed errori e sarebbe riusabile dai monitor.\\n\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:d61d117cdaf74c20b0558b3f4cbb6642\", \"observed_at_ms\": 1790777588732, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T14:22:22Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:c4c7901ee6e54427a31ac75e2316ce0e",
        "work_item_id": "wi:f0066b6c940b4d90b3981610312cb3b3",
        "role": "decision",
        "created_at": "2026-09-29T18:40:17Z"
      },
      {
        "issue_id": "issue:d61d117cdaf74c20b0558b3f4cbb6642",
        "work_item_id": "wi:f0066b6c940b4d90b3981610312cb3b3",
        "role": "decision",
        "created_at": "2026-09-30T14:22:22Z"
      }
    ]
  }
]
```
