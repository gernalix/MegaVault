# Chrome watch bridge: terminare il retry infinito quando il debugger è detached

<!-- migration-80b1ad554971cd56 -->

Migrated project backlog. Project: **chatgpt-rdc-supervisor**; project_id: 105.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 105.

Provenance: `wi:4a9d8d63fcdb4f06849698e2a440dae3`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Chrome watch bridge: terminare il retry infinito quando il debugger è detached

Roadmap live watcher can enter an infinite RuntimeError('Debugger unattached') loop after Chrome detaches the CDP debugger because the bridge keeps stale _attached=True state. Add automatic reattach/retry on this error and a regression test so monitoring self-recovers instead of silently dying.

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
      "work_item_id": "wi:4a9d8d63fcdb4f06849698e2a440dae3",
      "parent_id": null,
      "kind": "task",
      "title": "Chrome watch bridge: terminare il retry infinito quando il debugger è detached",
      "objective": "Roadmap live watcher can enter an infinite RuntimeError('Debugger unattached') loop after Chrome detaches the CDP debugger because the bridge keeps stale _attached=True state. Add automatic reattach/retry on this error and a regression test so monitoring self-recovers instead of silently dying.",
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
      "created_at": "2026-09-27T21:06:30Z",
      "updated_at": "2026-09-28T06:45:03Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:4a9d8d63fcdb4f06849698e2a440dae3",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 1029,
        "work_item_id": "wi:4a9d8d63fcdb4f06849698e2a440dae3",
        "evidence_kind": "issue_inbox",
        "label": "issue:bf266591858e4f1e98d607e82e1c7b6b",
        "uri": "https://chatgpt.com/c/6ab92890-6c94-83ed-83b8-86a8b7563734",
        "value_json": "{\"chat_url\": \"https://chatgpt.com/c/6ab92890-6c94-83ed-83b8-86a8b7563734\", \"code_location\": \"/home/daniele/.local/share/chatgpt-rdc-supervisor/bin/chrome_watch_bridge.py\", \"description\": \"Roadmap live watcher can enter an infinite RuntimeError('Debugger unattached') loop after Chrome detaches the CDP debugger because the bridge keeps stale _attached=True state. Add automatic reattach/retry on this error and a regression test so monitoring self-recovers instead of silently dying.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:bf266591858e4f1e98d607e82e1c7b6b\", \"observed_at_ms\": 1790530567361, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"/home/daniele/projects/codex-roadmap\"}",
        "created_at": "2026-09-27T21:06:30Z"
      },
      {
        "evidence_id": 1451,
        "work_item_id": "wi:4a9d8d63fcdb4f06849698e2a440dae3",
        "evidence_kind": "classification",
        "label": "User explicitly directed that C2 will soon be largely replaced by Symphony; this C2-only enhancement is non-essential to",
        "uri": null,
        "value_json": "\"User explicitly directed that C2 will soon be largely replaced by Symphony; this C2-only enhancement is non-essential to current roadmap execution and should not compete for slots before the migration decision.\"",
        "created_at": "2026-09-28T06:45:03Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:bf266591858e4f1e98d607e82e1c7b6b",
        "work_item_id": "wi:4a9d8d63fcdb4f06849698e2a440dae3",
        "role": "decision",
        "created_at": "2026-09-27T17:36:07Z"
      }
    ]
  }
]
```
