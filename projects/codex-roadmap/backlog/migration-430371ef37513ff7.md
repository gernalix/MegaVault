# Allow C2 Inbox triage to continue while a user-deferred row remains pending

<!-- migration-430371ef37513ff7 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:53317b48f00d4b3084353e7470b8fb89`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Allow C2 Inbox triage to continue while a user-deferred row remains pending

C2 runtime deadlock: the canonical issue-triage work item wi:c01fa42e01da48be80bd048ad5e07653 is status=blocked solely because one user-deferred Inbox-only row must remain pending, but c2_runtime treats blocked triage as active rather than terminal/recreatable. With 66 pending Inbox rows, runtime returns issue_triage_active and ready=0, so actionable new Inbox rows cannot be triaged and roadmap execution stalls. User-deferred Inbox-only rows should not block recreation/continuation of triage for other actionable pending rows.

status: waiting

current_action: Parked during roadmap semantic reconciliation.

next_action: Reassess after Symphony acquisition/migration scope is decided; resume only if the capability remains necessary outside Symphony.

blocker: Deferred pending Symphony migration/replacement decision.

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
      "work_item_id": "wi:53317b48f00d4b3084353e7470b8fb89",
      "parent_id": null,
      "kind": "task",
      "title": "Allow C2 Inbox triage to continue while a user-deferred row remains pending",
      "objective": "C2 runtime deadlock: the canonical issue-triage work item wi:c01fa42e01da48be80bd048ad5e07653 is status=blocked solely because one user-deferred Inbox-only row must remain pending, but c2_runtime treats blocked triage as active rather than terminal/recreatable. With 66 pending Inbox rows, runtime returns issue_triage_active and ready=0, so actionable new Inbox rows cannot be triaged and roadmap execution stalls. User-deferred Inbox-only rows should not block recreation/continuation of triage for other actionable pending rows.",
      "acceptance_json": "[]",
      "status": "waiting",
      "executor_policy": "auto",
      "sort_order": 9000,
      "current_action": "Parked during roadmap semantic reconciliation.",
      "next_action": "Reassess after Symphony acquisition/migration scope is decided; resume only if the capability remains necessary outside Symphony.",
      "blocker": "Deferred pending Symphony migration/replacement decision.",
      "project_id": null,
      "project_name": null,
      "repo": "gernalix/codex-roadmap",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 0,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-27T21:04:02Z",
      "updated_at": "2026-09-28T06:45:04Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:53317b48f00d4b3084353e7470b8fb89",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 1006,
        "work_item_id": "wi:53317b48f00d4b3084353e7470b8fb89",
        "evidence_kind": "issue_inbox",
        "label": "issue:4b1346142440462dad8d92885e1f648a",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"C2 runtime deadlock: the canonical issue-triage work item wi:c01fa42e01da48be80bd048ad5e07653 is status=blocked solely because one user-deferred Inbox-only row must remain pending, but c2_runtime treats blocked triage as active rather than terminal/recreatable. With 66 pending Inbox rows, runtime returns issue_triage_active and ready=0, so actionable new Inbox rows cannot be triaged and roadmap execution stalls. User-deferred Inbox-only rows should not block recreation/continuation of triage for other actionable pending rows.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:4b1346142440462dad8d92885e1f648a\", \"observed_at_ms\": 1790537851516, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-27T21:04:02Z"
      },
      {
        "evidence_id": 1454,
        "work_item_id": "wi:53317b48f00d4b3084353e7470b8fb89",
        "evidence_kind": "classification",
        "label": "User explicitly directed that C2 will soon be largely replaced by Symphony; this C2-only enhancement is non-essential to",
        "uri": null,
        "value_json": "\"User explicitly directed that C2 will soon be largely replaced by Symphony; this C2-only enhancement is non-essential to current roadmap execution and should not compete for slots before the migration decision.\"",
        "created_at": "2026-09-28T06:45:04Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:4b1346142440462dad8d92885e1f648a",
        "work_item_id": "wi:53317b48f00d4b3084353e7470b8fb89",
        "role": "decision",
        "created_at": "2026-09-27T19:37:31Z"
      }
    ]
  }
]
```
