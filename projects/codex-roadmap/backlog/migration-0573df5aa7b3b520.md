# C3 Inbox triage run 53a24e1207d34fee80a99d609f0da233 is canonically running for wi:08a9c0472c904fe39c16bc25cbe28992 with worker_ref c3-run:53a24e1207d34fee80a99d609f0da233, but no matching c3-control run metadata file exists and the persist

<!-- migration-0573df5aa7b3b520 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Merged duplicate/complementary observations and subtasks; every original requirement retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `issue:f48781c70dcf4687acb9034db8f6da41`, `issue:f89fa6a228eb4bba8905217fbc86d66b`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### issue:f48781c70dcf4687acb9034db8f6da41

C3 Inbox triage run 53a24e1207d34fee80a99d609f0da233 is canonically running for wi:08a9c0472c904fe39c16bc25cbe28992 with worker_ref c3-run:53a24e1207d34fee80a99d609f0da233, but no matching c3-control run metadata file exists and the persisted stable chat alias still names completed wi:dd4e09dfc4c64e47a65f260c7e1bb01d. This can leave the active bounded triage without a traceable/reusable chat binding.

state: pending

### issue:f89fa6a228eb4bba8905217fbc86d66b

C3 Inbox triage run 53a24e1207d34fee80a99d609f0da233 remains running after its lease expired at 2026-10-01T15:29:00Z. It has no per-run chat metadata; c3-runtime repeats launch for the same stale run while Inbox remains at 43 pending. This prevents recovery/dispatch of a fresh bounded triage batch.

state: pending

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "51",
      "reason": "explicit C3/C2 repository subject",
      "related_projects": [
        "51"
      ]
    },
    "source": {
      "issue_id": "issue:f48781c70dcf4687acb9034db8f6da41",
      "description": "C3 Inbox triage run 53a24e1207d34fee80a99d609f0da233 is canonically running for wi:08a9c0472c904fe39c16bc25cbe28992 with worker_ref c3-run:53a24e1207d34fee80a99d609f0da233, but no matching c3-control run metadata file exists and the persisted stable chat alias still names completed wi:dd4e09dfc4c64e47a65f260c7e1bb01d. This can leave the active bounded triage without a traceable/reusable chat binding.",
      "repo": null,
      "code_location": null,
      "executor": null,
      "executor_ref": "01a0f7fd-fd04-73f3-8ab3-437d30ed9ebc",
      "chat_url": "codex://threads/01a0f7fd-fd04-73f3-8ab3-437d30ed9ebc",
      "origin_work_item_id": null,
      "origin_run_id": null,
      "observed_at_ms": 1790869504172,
      "state": "pending",
      "matched_work_item_id": null,
      "promoted_work_item_id": null,
      "disposition_reason": null,
      "triaged_by": null,
      "triaged_at_ms": null,
      "created_at": "2026-10-01T15:45:04Z"
    },
    "issue_work_item_links": []
  },
  {
    "routing": {
      "project": "51",
      "reason": "explicit C3/C2 repository subject",
      "related_projects": [
        "51"
      ]
    },
    "source": {
      "issue_id": "issue:f89fa6a228eb4bba8905217fbc86d66b",
      "description": "C3 Inbox triage run 53a24e1207d34fee80a99d609f0da233 remains running after its lease expired at 2026-10-01T15:29:00Z. It has no per-run chat metadata; c3-runtime repeats launch for the same stale run while Inbox remains at 43 pending. This prevents recovery/dispatch of a fresh bounded triage batch.",
      "repo": null,
      "code_location": null,
      "executor": null,
      "executor_ref": "01a0f7fd-fd04-73f3-8ab3-437d30ed9ebc",
      "chat_url": "codex://threads/01a0f7fd-fd04-73f3-8ab3-437d30ed9ebc",
      "origin_work_item_id": null,
      "origin_run_id": null,
      "observed_at_ms": 1790869504895,
      "state": "pending",
      "matched_work_item_id": null,
      "promoted_work_item_id": null,
      "disposition_reason": null,
      "triaged_by": null,
      "triaged_at_ms": null,
      "created_at": "2026-10-01T15:45:04Z"
    },
    "issue_work_item_links": []
  }
]
```
