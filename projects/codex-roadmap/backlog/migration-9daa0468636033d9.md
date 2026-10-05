# Impedire che override drain_first obsoleti blocchino la coda

<!-- migration-9daa0468636033d9 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:83ba579a17e44cd7a39103f73e040a7a`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Impedire che override drain_first obsoleti blocchino la coda

Impedire che un override repo-scoped drain_first resti attivo quando non esistono run attivi nello scope e sopprima la schedulazione di lavoro non correlato. Verificare auto-scadenza/associazione a run o batch e preservare priorità semantiche.

status: pending

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
      "work_item_id": "wi:83ba579a17e44cd7a39103f73e040a7a",
      "parent_id": null,
      "kind": "task",
      "title": "Impedire che override drain_first obsoleti blocchino la coda",
      "objective": "Impedire che un override repo-scoped drain_first resti attivo quando non esistono run attivi nello scope e sopprima la schedulazione di lavoro non correlato. Verificare auto-scadenza/associazione a run o batch e preservare priorità semantiche.",
      "acceptance_json": "[]",
      "status": "pending",
      "executor_policy": "human",
      "sort_order": null,
      "current_action": null,
      "next_action": null,
      "blocker": null,
      "project_id": null,
      "project_name": null,
      "repo": "gernalix/codex-roadmap",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-30T13:51:11Z",
      "updated_at": "2026-09-30T13:51:11Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:83ba579a17e44cd7a39103f73e040a7a",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2386,
        "work_item_id": "wi:83ba579a17e44cd7a39103f73e040a7a",
        "evidence_kind": "issue_inbox",
        "label": "issue:55995a9e10d64b368d4cc19b12ec1526",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"C2 execution override can become a permanent head-of-line blocker: a repo-scoped drain_first override for gernalix/codex-roadmap remained set although there were zero active runs in that repo, so a prepared P0 C3 security task stayed runnable-but-unscheduled until the override was manually cleared (#7341). Make drain_first self-expire/auto-clear once its selected scope has no active or draining executions, or attach it to the run/batch that created it so stale override state cannot suppress future unrelated work.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:55995a9e10d64b368d4cc19b12ec1526\", \"observed_at_ms\": 1790771000163, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T13:51:11Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:55995a9e10d64b368d4cc19b12ec1526",
        "work_item_id": "wi:83ba579a17e44cd7a39103f73e040a7a",
        "role": "decision",
        "created_at": "2026-09-30T12:23:20Z"
      }
    ]
  }
]
```
