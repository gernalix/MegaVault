# C2 prompt routing: repo canonico e-Boks resta MegaVault dopo la verifica del nuovo repo

<!-- migration-199b2c7f2b65b03f -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:0fa0c1ccfc3d4d269d28225ee81161bc`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### C2 prompt routing: repo canonico e-Boks resta MegaVault dopo la verifica del nuovo repo

Permettere una correzione fenced e auditabile del repo/project routing di un prompt pending senza riscrivere testo, modello o lifecycle; prompt 218695 indica ancora /home/daniele/MegaVault mentre il repo pubblico eboks-scraper esiste.

Acceptance:

- La mutation rifiuta prompt running/terminal, active run, repo inesistente o routing ambiguo.
- Il cambio del solo routing è registrato con evidenza e preserva prompt materialization/hash e dipendenze.
- 218695 può essere corretto solo dopo la decisione condizionale successiva al MitID; nessun export o login viene avviato.

status: waiting

current_action: Audit 2026-09-26: work_items.repo di prompt 218695 è /home/daniele/MegaVault; gernalix/eboks-scraper main è vuoto con seed branch 13c104cf; il writer non espone update repo per prompt.

next_action: Aggiungere mutation minima per routing prompt pending, poi applicarla soltanto quando 582946 dimostra che lo scraper serve ancora.

blocker: MitID export outcome is pending; a fenced prompt repo-routing mutation is unavailable until the conditional scraper need is established.

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "51",
      "reason": "canonical repository identity",
      "related_projects": [
        "51"
      ]
    },
    "source": {
      "work_item_id": "wi:0fa0c1ccfc3d4d269d28225ee81161bc",
      "parent_id": null,
      "kind": "task",
      "title": "C2 prompt routing: repo canonico e-Boks resta MegaVault dopo la verifica del nuovo repo",
      "objective": "Permettere una correzione fenced e auditabile del repo/project routing di un prompt pending senza riscrivere testo, modello o lifecycle; prompt 218695 indica ancora /home/daniele/MegaVault mentre il repo pubblico eboks-scraper esiste.",
      "acceptance_json": "[\"La mutation rifiuta prompt running/terminal, active run, repo inesistente o routing ambiguo.\", \"Il cambio del solo routing è registrato con evidenza e preserva prompt materialization/hash e dipendenze.\", \"218695 può essere corretto solo dopo la decisione condizionale successiva al MitID; nessun export o login viene avviato.\"]",
      "status": "waiting",
      "executor_policy": "auto",
      "sort_order": 70,
      "current_action": "Audit 2026-09-26: work_items.repo di prompt 218695 è /home/daniele/MegaVault; gernalix/eboks-scraper main è vuoto con seed branch 13c104cf; il writer non espone update repo per prompt.",
      "next_action": "Aggiungere mutation minima per routing prompt pending, poi applicarla soltanto quando 582946 dimostra che lo scraper serve ancora.",
      "blocker": "MitID export outcome is pending; a fenced prompt repo-routing mutation is unavailable until the conditional scraper need is established.",
      "project_id": null,
      "project_name": null,
      "repo": "gernalix/codex-roadmap",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 0,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-26T17:24:26Z",
      "updated_at": "2026-09-26T17:25:32Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:0fa0c1ccfc3d4d269d28225ee81161bc",
        "tag": "c2:audit-followup"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 389,
        "work_item_id": "wi:0fa0c1ccfc3d4d269d28225ee81161bc",
        "evidence_kind": "classification",
        "label": "codex-roadmap main e2338999 prompt 218695 repo is /home/daniele/MegaVault, while public eboks-scraper main exists empty ",
        "uri": null,
        "value_json": "\"codex-roadmap main e2338999 prompt 218695 repo is /home/daniele/MegaVault, while public eboks-scraper main exists empty with seed 13c104cf; writer has no pending-prompt repo update operation.\"",
        "created_at": "2026-09-26T17:25:32Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": []
  }
]
```
