# Bound semantic watcher goal-watchdog log tail read

<!-- migration-35bc4797ca821400 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:338f1a75febd49aa856aef9364301517`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Bound semantic watcher goal-watchdog log tail read

C2 semantic watcher reads the entire c2-roadmap-goal-watchdog.log every 15-second pass just to retain the last 35 lines. systemd currently reports about 223 MB memory peak per semantic-watcher pass. This is avoidable monitoring overhead and can become a self-inflicted resource bottleneck. Use a bounded tail/reverse read instead of Path.read_text().splitlines().

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
      "work_item_id": "wi:338f1a75febd49aa856aef9364301517",
      "parent_id": null,
      "kind": "task",
      "title": "Bound semantic watcher goal-watchdog log tail read",
      "objective": "C2 semantic watcher reads the entire c2-roadmap-goal-watchdog.log every 15-second pass just to retain the last 35 lines. systemd currently reports about 223 MB memory peak per semantic-watcher pass. This is avoidable monitoring overhead and can become a self-inflicted resource bottleneck. Use a bounded tail/reverse read instead of Path.read_text().splitlines().",
      "acceptance_json": "[]",
      "status": "pending",
      "executor_policy": "auto",
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
      "created_at": "2026-09-29T20:05:40Z",
      "updated_at": "2026-09-29T22:21:33Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:338f1a75febd49aa856aef9364301517",
        "tag": "source:issue-inbox"
      },
      {
        "work_item_id": "wi:338f1a75febd49aa856aef9364301517",
        "tag": "priority:p0"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 1849,
        "work_item_id": "wi:338f1a75febd49aa856aef9364301517",
        "evidence_kind": "issue_inbox",
        "label": "issue:8d2e4130cea244969bedacab4b8d6c96",
        "uri": "codex://threads/01a0e719-60ff-7b91-82db-1d7c55787c67",
        "value_json": "{\"chat_url\": \"codex://threads/01a0e719-60ff-7b91-82db-1d7c55787c67\", \"code_location\": \"/home/daniele/.local/share/c2-roadmap-semantic-watcher/watcher.py:process_snapshot\", \"description\": \"C2 semantic watcher reads the entire c2-roadmap-goal-watchdog.log every 15-second pass just to retain the last 35 lines. systemd currently reports about 223 MB memory peak per semantic-watcher pass. This is avoidable monitoring overhead and can become a self-inflicted resource bottleneck. Use a bounded tail/reverse read instead of Path.read_text().splitlines().\", \"executor\": null, \"executor_ref\": \"c2-roadmap-semantic-watcher\", \"issue_id\": \"issue:8d2e4130cea244969bedacab4b8d6c96\", \"observed_at_ms\": 1790636901685, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"gernalix/codex-roadmap\"}",
        "created_at": "2026-09-29T20:05:40Z"
      },
      {
        "evidence_id": 1896,
        "work_item_id": "wi:338f1a75febd49aa856aef9364301517",
        "evidence_kind": "classification",
        "label": "User explicitly requested P0 for the C2 batch on 2026-09-30; this item is currently runnable and belongs to gernalix/cod",
        "uri": null,
        "value_json": "\"User explicitly requested P0 for the C2 batch on 2026-09-30; this item is currently runnable and belongs to gernalix/codex-roadmap.\"",
        "created_at": "2026-09-29T22:21:33Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:8d2e4130cea244969bedacab4b8d6c96",
        "work_item_id": "wi:338f1a75febd49aa856aef9364301517",
        "role": "decision",
        "created_at": "2026-09-28T23:08:21Z"
      }
    ]
  }
]
```
