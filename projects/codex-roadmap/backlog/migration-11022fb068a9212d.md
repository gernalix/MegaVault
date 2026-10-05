# Inject deterministic wake event into c2-master-goal-start and require fresh C2 read

<!-- migration-11022fb068a9212d -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:2349c8af8ff34ba094ca0917deb45e35`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Inject deterministic wake event into c2-master-goal-start and require fresh C2 read

Master Goal wake handoff ignores deterministic state transitions: the new deterministic watchdog correctly woke the Goal when the supervisor authority lease changed from valid to expired, but c2-master-goal-start still sent the same generic prompt. The Goal then replied using its stale last-verified state (264 Inbox items + live fence) and explicitly said no handoff/event was supplied, despite the runtime DB showing authority_lease_valid=false. Impact: watchdog autonomy can wake the Goal correctly but the Goal may fail to act on the event and remain blocked. Persist a repository-backed launcher that injects a compact deterministic wake payload and requires a fresh canonical read before deciding.

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
      "work_item_id": "wi:2349c8af8ff34ba094ca0917deb45e35",
      "parent_id": null,
      "kind": "task",
      "title": "Inject deterministic wake event into c2-master-goal-start and require fresh C2 read",
      "objective": "Master Goal wake handoff ignores deterministic state transitions: the new deterministic watchdog correctly woke the Goal when the supervisor authority lease changed from valid to expired, but c2-master-goal-start still sent the same generic prompt. The Goal then replied using its stale last-verified state (264 Inbox items + live fence) and explicitly said no handoff/event was supplied, despite the runtime DB showing authority_lease_valid=false. Impact: watchdog autonomy can wake the Goal correctly but the Goal may fail to act on the event and remain blocked. Persist a repository-backed launcher that injects a compact deterministic wake payload and requires a fresh canonical read before deciding.",
      "acceptance_json": "[]",
      "status": "pending",
      "executor_policy": "auto",
      "sort_order": null,
      "current_action": null,
      "next_action": null,
      "blocker": null,
      "project_id": null,
      "project_name": null,
      "repo": "https://github.com/gernalix/codex-roadmap",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-30T06:05:48Z",
      "updated_at": "2026-09-30T06:05:48Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:2349c8af8ff34ba094ca0917deb45e35",
        "tag": "priority:p1"
      },
      {
        "work_item_id": "wi:2349c8af8ff34ba094ca0917deb45e35",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2027,
        "work_item_id": "wi:2349c8af8ff34ba094ca0917deb45e35",
        "evidence_kind": "issue_inbox",
        "label": "issue:c55f89b7f8354e3daa638fc7c62d39d3",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Master Goal wake handoff ignores deterministic state transitions: the new deterministic watchdog correctly woke the Goal when the supervisor authority lease changed from valid to expired, but c2-master-goal-start still sent the same generic prompt. The Goal then replied using its stale last-verified state (264 Inbox items + live fence) and explicitly said no handoff/event was supplied, despite the runtime DB showing authority_lease_valid=false. Impact: watchdog autonomy can wake the Goal correctly but the Goal may fail to act on the event and remain blocked. Persist a repository-backed launcher that injects a compact deterministic wake payload and requires a fresh canonical read before deciding.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:c55f89b7f8354e3daa638fc7c62d39d3\", \"observed_at_ms\": 1790677542924, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"https://github.com/gernalix/codex-roadmap\"}",
        "created_at": "2026-09-30T06:05:48Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:c55f89b7f8354e3daa638fc7c62d39d3",
        "work_item_id": "wi:2349c8af8ff34ba094ca0917deb45e35",
        "role": "decision",
        "created_at": "2026-09-29T10:25:42Z"
      }
    ]
  }
]
```
