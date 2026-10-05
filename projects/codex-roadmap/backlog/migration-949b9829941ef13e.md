# C2 Master Goal can be false-active and stall indefinitely. After the watchdog set the persisted native Goal active at 20

<!-- migration-949b9829941ef13e -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:75b78aa9c8ab4877a60b3b4e1cefb8b4`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### C2 Master Goal can be false-active and stall indefinitely. After the watchdog set the persisted native Goal active at 20

C2 Master Goal can be false-active and stall indefinitely. After the watchdog set the persisted native Goal active at 2026-09-30 11:39:37 CEST, the canonical Codex rollout for thread 01a0e719-60ff-7b91-82db-1d7c55787c67 still had mtime 02:48:22 CEST and the latest persisted turn was completed at 2026-09-29 18:33 CEST; no new turn was appended. c2_master_watchdog currently treats goal_status=active as healthy without a freshness/owner-progress check. The earlier explicit thread/resume approach is known to fail because a managed daemon owns the thread, so do not restore a competing app-server. Add owner-aware Goal liveness/progress detection and a deterministic wake/rehydration path for an active-but-unprogressing native Goal, preserving single-owner semantics.

status: pending

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "51",
      "reason": "semantic correction of source routing; original identity preserved",
      "related_projects": [
        "51"
      ]
    },
    "source": {
      "work_item_id": "wi:75b78aa9c8ab4877a60b3b4e1cefb8b4",
      "parent_id": null,
      "kind": "task",
      "title": "C2 Master Goal can be false-active and stall indefinitely. After the watchdog set the persisted native Goal active at 20",
      "objective": "C2 Master Goal can be false-active and stall indefinitely. After the watchdog set the persisted native Goal active at 2026-09-30 11:39:37 CEST, the canonical Codex rollout for thread 01a0e719-60ff-7b91-82db-1d7c55787c67 still had mtime 02:48:22 CEST and the latest persisted turn was completed at 2026-09-29 18:33 CEST; no new turn was appended. c2_master_watchdog currently treats goal_status=active as healthy without a freshness/owner-progress check. The earlier explicit thread/resume approach is known to fail because a managed daemon owns the thread, so do not restore a competing app-server. Add owner-aware Goal liveness/progress detection and a deterministic wake/rehydration path for an active-but-unprogressing native Goal, preserving single-owner semantics.",
      "acceptance_json": "[]",
      "status": "pending",
      "executor_policy": "auto",
      "sort_order": null,
      "current_action": null,
      "next_action": null,
      "blocker": null,
      "project_id": null,
      "project_name": null,
      "repo": null,
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-30T12:21:51Z",
      "updated_at": "2026-09-30T12:21:51Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:75b78aa9c8ab4877a60b3b4e1cefb8b4",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2296,
        "work_item_id": "wi:75b78aa9c8ab4877a60b3b4e1cefb8b4",
        "evidence_kind": "issue_inbox",
        "label": "issue:ef4cf90133e546c597c9ef5f094c2417",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"C2 Master Goal can be false-active and stall indefinitely. After the watchdog set the persisted native Goal active at 2026-09-30 11:39:37 CEST, the canonical Codex rollout for thread 01a0e719-60ff-7b91-82db-1d7c55787c67 still had mtime 02:48:22 CEST and the latest persisted turn was completed at 2026-09-29 18:33 CEST; no new turn was appended. c2_master_watchdog currently treats goal_status=active as healthy without a freshness/owner-progress check. The earlier explicit thread/resume approach is known to fail because a managed daemon owns the thread, so do not restore a competing app-server. Add owner-aware Goal liveness/progress detection and a deterministic wake/rehydration path for an active-but-unprogressing native Goal, preserving single-owner semantics.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:ef4cf90133e546c597c9ef5f094c2417\", \"observed_at_ms\": 1790761373270, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T12:21:51Z"
      },
      {
        "evidence_id": 2359,
        "work_item_id": "wi:75b78aa9c8ab4877a60b3b4e1cefb8b4",
        "evidence_kind": "issue_inbox",
        "label": "issue:532b7b05080041fab986929b6f20654c",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"C2 Master Goal false liveness: live readback shows goal_status=active, thread_status=notLoaded, latest turn=completed, no Master Goal process/worker, while 76 pending auto work items lack execution specs. The watchdog returns working solely because goal_status is active. A bounded paused->active experiment with AppServerRPC produced no new turn (213 turns before and after), proving thread/goal/set active does not wake planning. Replace the active flag as liveness evidence with an actual active turn/process; wake planning by explicitly starting one bounded planner turn on material state change, and keep it event-driven so unchanged state consumes no model calls.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:532b7b05080041fab986929b6f20654c\", \"observed_at_ms\": 1790763825982, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T13:05:38Z"
      },
      {
        "evidence_id": 2450,
        "work_item_id": "wi:75b78aa9c8ab4877a60b3b4e1cefb8b4",
        "evidence_kind": "issue_inbox",
        "label": "issue:5d4bb58164a549a3bb90f93b26bba546",
        "uri": "https://chatgpt.com/g/g-p-6ab69fbdbaf88191a39a75ff5c9e3d70-c2/c/6abcd235-20f0-83eb-861e-d8a0e79d25c1",
        "value_json": "{\"chat_url\": \"https://chatgpt.com/g/g-p-6ab69fbdbaf88191a39a75ff5c9e3d70-c2/c/6abcd235-20f0-83eb-861e-d8a0e79d25c1\", \"code_location\": null, \"description\": \"Candidate mechanical command: one-shot fail-closed Master Goal recovery. In the 2026-09-30 chat recovery repeatedly required manual inspection and sequencing: detect runs marked running with expired leases and inactive systemd units, terminalize/reconcile stale runs, handle ghost terminalization (run 103001), canonical readback/fencing, resume a notLoaded/interrupted Master Goal thread, then verify active-and-progressing before returning to normal workers. Encapsulate as a deterministic dry-run-capable command rather than repeating multi-step manual recovery.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:5d4bb58164a549a3bb90f93b26bba546\", \"observed_at_ms\": 1790784486222, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T16:45:28Z"
      },
      {
        "evidence_id": 2457,
        "work_item_id": "wi:75b78aa9c8ab4877a60b3b4e1cefb8b4",
        "evidence_kind": "issue_inbox",
        "label": "issue:75435317c7a046f4ac92b4980ce1faf0",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Mechanical human round-trip observed in the acceleration chat: the watchdog surfaced `Master Goal bloccato... Chiedimi di diagnosticare il Master Goal C2`, forcing the user to send back a diagnostic request before read-only inspection could start. The watchdog/supervisor should automatically run deterministic diagnosis and whitelisted safe recovery when criteria are met; only actions outside the authorized recovery envelope should require a user prompt. A dedicated diagnose/recover Master Goal command can back this path.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:75435317c7a046f4ac92b4980ce1faf0\", \"observed_at_ms\": 1790785122305, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T16:45:28Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:532b7b05080041fab986929b6f20654c",
        "work_item_id": "wi:75b78aa9c8ab4877a60b3b4e1cefb8b4",
        "role": "matched",
        "created_at": "2026-09-30T10:23:45Z"
      },
      {
        "issue_id": "issue:ef4cf90133e546c597c9ef5f094c2417",
        "work_item_id": "wi:75b78aa9c8ab4877a60b3b4e1cefb8b4",
        "role": "decision",
        "created_at": "2026-09-30T09:42:53Z"
      },
      {
        "issue_id": "issue:532b7b05080041fab986929b6f20654c",
        "work_item_id": "wi:75b78aa9c8ab4877a60b3b4e1cefb8b4",
        "role": "decision",
        "created_at": "2026-09-30T10:23:45Z"
      },
      {
        "issue_id": "issue:5d4bb58164a549a3bb90f93b26bba546",
        "work_item_id": "wi:75b78aa9c8ab4877a60b3b4e1cefb8b4",
        "role": "decision",
        "created_at": "2026-09-30T16:45:28Z"
      },
      {
        "issue_id": "issue:75435317c7a046f4ac92b4980ce1faf0",
        "work_item_id": "wi:75b78aa9c8ab4877a60b3b4e1cefb8b4",
        "role": "decision",
        "created_at": "2026-09-30T16:45:28Z"
      }
    ]
  }
]
```
