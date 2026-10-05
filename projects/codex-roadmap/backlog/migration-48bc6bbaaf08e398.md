# Make C2/C3 stream recovery resumable from durable state

<!-- migration-48bc6bbaaf08e398 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:ab385383b9284e28937bd7067470ba51`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Make C2/C3 stream recovery resumable from durable state

When ChatGPT stream recovery times out, preserve canonical worker/thread/run state, completed side effects, pending readback, and a deterministic resume action so a lost stream does not leave an almost-complete task ambiguous.

Acceptance:

- Recovery timeout returns a durable, resumable checkpoint.
- Resume/reconcile can continue from the checkpoint without repeating completed side effects.

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
      "work_item_id": "wi:ab385383b9284e28937bd7067470ba51",
      "parent_id": null,
      "kind": "task",
      "title": "Make C2/C3 stream recovery resumable from durable state",
      "objective": "When ChatGPT stream recovery times out, preserve canonical worker/thread/run state, completed side effects, pending readback, and a deterministic resume action so a lost stream does not leave an almost-complete task ambiguous.",
      "acceptance_json": "[\"Recovery timeout returns a durable, resumable checkpoint.\", \"Resume/reconcile can continue from the checkpoint without repeating completed side effects.\"]",
      "status": "pending",
      "executor_policy": "auto",
      "sort_order": null,
      "current_action": null,
      "next_action": null,
      "blocker": null,
      "project_id": null,
      "project_name": null,
      "repo": "codex-roadmap",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-30T16:35:23Z",
      "updated_at": "2026-09-30T16:35:23Z"
    },
    "work_item_tags": [],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2445,
        "work_item_id": "wi:ab385383b9284e28937bd7067470ba51",
        "evidence_kind": "issue_inbox",
        "label": "issue:dc76dc038e184b399b21d84906bffc1d",
        "uri": "https://chatgpt.com/g/g-p-6ab69fbdbaf88191a39a75ff5c9e3d70-c2/c/6abcd235-20f0-83eb-861e-d8a0e79d25c1",
        "value_json": "{\"chat_url\": \"https://chatgpt.com/g/g-p-6ab69fbdbaf88191a39a75ff5c9e3d70-c2/c/6abcd235-20f0-83eb-861e-d8a0e79d25c1\", \"code_location\": null, \"description\": \"Coordinator stream-resume fragility observed at the end of the 2026-09-30 C3 acceleration chat: immediately after executor rerouting and Symphony production-routing work, the controller ended with ChatGPT stream recovery polling timed out before final canonical readback. Long C2/C3 operations should checkpoint current phase, completed side effects, pending readback and Next action before/after risky integration or deployment, and expose a deterministic resume-last/reconcile-last-operation path so a lost chat stream cannot leave nearly-complete work ambiguous.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:dc76dc038e184b399b21d84906bffc1d\", \"observed_at_ms\": 1790784617326, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T16:35:23Z"
      },
      {
        "evidence_id": 2446,
        "work_item_id": "wi:ab385383b9284e28937bd7067470ba51",
        "evidence_kind": "issue_inbox",
        "label": "issue:0abebe741738438184d14d44fc14bac6",
        "uri": "https://chatgpt.com/g/g-p-6ab69fbdbaf88191a39a75ff5c9e3d70-c2/c/6abcd235-20f0-83eb-861e-d8a0e79d25c1",
        "value_json": "{\"chat_url\": \"https://chatgpt.com/g/g-p-6ab69fbdbaf88191a39a75ff5c9e3d70-c2/c/6abcd235-20f0-83eb-861e-d8a0e79d25c1\", \"code_location\": null, \"description\": \"ChatGPT/C2 supervision stream-recovery failure observed at the end of the acceleration chat: after implementing executor rerouting and Symphony routing, the UI reported `ChatGPT stream recovery polling timed out`. This can strand an otherwise-progressing long task and force manual continuation. The supervisor should persist last canonical worker/thread/run state, retry recovery with bounded backoff, and on timeout return a deterministic resumable checkpoint instead of an opaque Retry state.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:0abebe741738438184d14d44fc14bac6\", \"observed_at_ms\": 1790784996281, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T16:35:23Z"
      },
      {
        "evidence_id": 2494,
        "work_item_id": "wi:ab385383b9284e28937bd7067470ba51",
        "evidence_kind": "issue_inbox",
        "label": "issue:738e710819744e5e9f93a8c09e28a54f",
        "uri": "https://chatgpt.com/g/g-p-6ab69fbdbaf88191a39a75ff5c9e3d70-c2/c/6abcd235-20f0-83eb-861e-d8a0e79d25c1",
        "value_json": "{\"chat_url\": \"https://chatgpt.com/g/g-p-6ab69fbdbaf88191a39a75ff5c9e3d70-c2/c/6abcd235-20f0-83eb-861e-d8a0e79d25c1\", \"code_location\": null, \"description\": \"C2/C3 monitor durability issue observed in the acceleration chat: state.json/live.log persistence was intermittently blocked and the monitor was judged insufficiently versioned/reproducible. A supervisor that cannot durably persist state makes post-crash/reboot recovery expensive. Persist monitor state atomically outside fragile shell paths, version the monitor config/code, and expose last durable checkpoint/readback.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:738e710819744e5e9f93a8c09e28a54f\", \"observed_at_ms\": 1790784619766, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-10-01T12:32:14Z"
      },
      {
        "evidence_id": 2498,
        "work_item_id": "wi:ab385383b9284e28937bd7067470ba51",
        "evidence_kind": "issue_inbox",
        "label": "issue:8f7f31f3aaf246a1aebac997bd5753d4",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Long-running C2/C3 orchestration required repeated manual `continua` nudges in the acceleration chat even though the task was already authorized for autonomous completion. This is avoidable human-in-the-loop latency. Once an execution goal is accepted, the coordinator/supervisor should keep progressing until quiescence, a real external blocker, or acceptance criteria, and automatically resume from the last durable checkpoint after recoverable interruptions instead of waiting for another chat message.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:8f7f31f3aaf246a1aebac997bd5753d4\", \"observed_at_ms\": 1790785122052, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-10-01T12:32:14Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:dc76dc038e184b399b21d84906bffc1d",
        "work_item_id": "wi:ab385383b9284e28937bd7067470ba51",
        "role": "decision",
        "created_at": "2026-09-30T16:35:23Z"
      },
      {
        "issue_id": "issue:0abebe741738438184d14d44fc14bac6",
        "work_item_id": "wi:ab385383b9284e28937bd7067470ba51",
        "role": "decision",
        "created_at": "2026-09-30T16:35:23Z"
      },
      {
        "issue_id": "issue:738e710819744e5e9f93a8c09e28a54f",
        "work_item_id": "wi:ab385383b9284e28937bd7067470ba51",
        "role": "decision",
        "created_at": "2026-10-01T12:32:14Z"
      },
      {
        "issue_id": "issue:738e710819744e5e9f93a8c09e28a54f",
        "work_item_id": "wi:ab385383b9284e28937bd7067470ba51",
        "role": "matched",
        "created_at": "2026-10-01T12:32:14Z"
      },
      {
        "issue_id": "issue:8f7f31f3aaf246a1aebac997bd5753d4",
        "work_item_id": "wi:ab385383b9284e28937bd7067470ba51",
        "role": "decision",
        "created_at": "2026-10-01T12:32:14Z"
      },
      {
        "issue_id": "issue:8f7f31f3aaf246a1aebac997bd5753d4",
        "work_item_id": "wi:ab385383b9284e28937bd7067470ba51",
        "role": "matched",
        "created_at": "2026-10-01T12:32:14Z"
      }
    ]
  }
]
```
