# C2 supervisor: documentare e velocizzare il bootstrap manuale degli executor

<!-- migration-9ed52629a763e85f -->

Migrated project backlog. Project: **chatgpt-rdc-supervisor**; project_id: 105.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 105.

Provenance: `wi:c55c1af448494a38a8f1350946a45caa`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### C2 supervisor: documentare e velocizzare il bootstrap manuale degli executor

C2 manual supervisor bootstrap is too slow and under-documented. In this run, merely taking ownership of a monitoring task required trial-and-error discovery of valid c2_intake.py kind values, executor_policy values, project handling, then separate intake + executor_started + supervisor registration. The CLI help did not expose accepted enums, project=C2 failed, and the operator had to inspect source to proceed. Provide a single documented MegaVault/protocol entrypoint (ideally one helper command) for manual ChatGPT supervisor takeover/registration that validates inputs, exposes allowed values, creates/claims the work item, records executor_started, and registers the target chat without exploratory retries.

status: waiting

current_action: Parked during roadmap semantic reconciliation.

next_action: Reassess after Symphony acquisition/migration scope is decided; resume only if the capability remains necessary outside Symphony.

blocker: Deferred pending Symphony migration/replacement decision.

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "105",
      "reason": "semantic correction of source routing; original identity preserved",
      "related_projects": [
        "105"
      ]
    },
    "source": {
      "work_item_id": "wi:c55c1af448494a38a8f1350946a45caa",
      "parent_id": null,
      "kind": "task",
      "title": "C2 supervisor: documentare e velocizzare il bootstrap manuale degli executor",
      "objective": "C2 manual supervisor bootstrap is too slow and under-documented. In this run, merely taking ownership of a monitoring task required trial-and-error discovery of valid c2_intake.py kind values, executor_policy values, project handling, then separate intake + executor_started + supervisor registration. The CLI help did not expose accepted enums, project=C2 failed, and the operator had to inspect source to proceed. Provide a single documented MegaVault/protocol entrypoint (ideally one helper command) for manual ChatGPT supervisor takeover/registration that validates inputs, exposes allowed values, creates/claims the work item, records executor_started, and registers the target chat without exploratory retries.",
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
      "created_at": "2026-09-27T21:05:32Z",
      "updated_at": "2026-09-28T06:45:05Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:c55c1af448494a38a8f1350946a45caa",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 1022,
        "work_item_id": "wi:c55c1af448494a38a8f1350946a45caa",
        "evidence_kind": "issue_inbox",
        "label": "issue:ed6a0e1c7b524364889dea5091791102",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"C2 manual supervisor bootstrap is too slow and under-documented. In this run, merely taking ownership of a monitoring task required trial-and-error discovery of valid c2_intake.py kind values, executor_policy values, project handling, then separate intake + executor_started + supervisor registration. The CLI help did not expose accepted enums, project=C2 failed, and the operator had to inspect source to proceed. Provide a single documented MegaVault/protocol entrypoint (ideally one helper command) for manual ChatGPT supervisor takeover/registration that validates inputs, exposes allowed values, creates/claims the work item, records executor_started, and registers the target chat without exploratory retries.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:ed6a0e1c7b524364889dea5091791102\", \"observed_at_ms\": 1790518671187, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-27T21:05:32Z"
      },
      {
        "evidence_id": 1460,
        "work_item_id": "wi:c55c1af448494a38a8f1350946a45caa",
        "evidence_kind": "classification",
        "label": "User explicitly directed that C2 will soon be largely replaced by Symphony; this C2-only enhancement is non-essential to",
        "uri": null,
        "value_json": "\"User explicitly directed that C2 will soon be largely replaced by Symphony; this C2-only enhancement is non-essential to current roadmap execution and should not compete for slots before the migration decision.\"",
        "created_at": "2026-09-28T06:45:05Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:ed6a0e1c7b524364889dea5091791102",
        "work_item_id": "wi:c55c1af448494a38a8f1350946a45caa",
        "role": "decision",
        "created_at": "2026-09-27T14:17:51Z"
      }
    ]
  }
]
```
