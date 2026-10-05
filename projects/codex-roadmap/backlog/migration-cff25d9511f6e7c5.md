# C3 ensure_issue_triage recovery bug: tools/c2_issue_inbox.py treats c2:issue-triage work items with status blocked as active, so after a stale triage run is terminalized BLOCKED the writer returns existing wi:08a9... forever and cannot crea

<!-- migration-cff25d9511f6e7c5 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `issue:70f12d74db7847d9b320b990ef4f1169`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### issue:70f12d74db7847d9b320b990ef4f1169

C3 ensure_issue_triage recovery bug: tools/c2_issue_inbox.py treats c2:issue-triage work items with status blocked as active, so after a stale triage run is terminalized BLOCKED the writer returns existing wi:08a9... forever and cannot create the fresh bounded batch mandated by its next_action. Exclude blocked triage items from active selection or otherwise create a new batch after a terminal BLOCKED run.

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
      "issue_id": "issue:70f12d74db7847d9b320b990ef4f1169",
      "description": "C3 ensure_issue_triage recovery bug: tools/c2_issue_inbox.py treats c2:issue-triage work items with status blocked as active, so after a stale triage run is terminalized BLOCKED the writer returns existing wi:08a9... forever and cannot create the fresh bounded batch mandated by its next_action. Exclude blocked triage items from active selection or otherwise create a new batch after a terminal BLOCKED run.",
      "repo": null,
      "code_location": null,
      "executor": null,
      "executor_ref": "01a0f7fd-fd04-73f3-8ab3-437d30ed9ebc",
      "chat_url": "codex://threads/01a0f7fd-fd04-73f3-8ab3-437d30ed9ebc",
      "origin_work_item_id": null,
      "origin_run_id": null,
      "observed_at_ms": 1790869820212,
      "state": "pending",
      "matched_work_item_id": null,
      "promoted_work_item_id": null,
      "disposition_reason": null,
      "triaged_by": null,
      "triaged_at_ms": null,
      "created_at": "2026-10-01T15:50:20Z"
    },
    "issue_work_item_links": []
  }
]
```
