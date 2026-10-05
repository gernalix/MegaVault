# Pause nonterminal C2 Master Goal after each deterministic watchdog wake

<!-- migration-8adacbb6bd775830 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:6d603f31e51b449788e2cd3d607d56b1`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Pause nonterminal C2 Master Goal after each deterministic watchdog wake

Native C2 Master Goal auto-continuation bypasses deterministic watchdog suppression: c2-master-goal-start sets thread/goal status active before waiting for its turn, but does not pause the Goal after a non-terminal turn finishes. Evidence after deterministic watchdog deployment: watchdog state remained waiting_external with should_wake_goal=false and unchanged last_wake_at, c2-master-goal.service was inactive, yet new Master Goal assistant turns continued to appear. Impact: repeated model-driven polling/token burn persists even though the watcher no longer wakes the Goal. Fix the controller so each deterministic wake yields one bounded turn and leaves a still-active/nonterminal Goal paused until the control-plane fingerprint changes.

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
      "work_item_id": "wi:6d603f31e51b449788e2cd3d607d56b1",
      "parent_id": null,
      "kind": "task",
      "title": "Pause nonterminal C2 Master Goal after each deterministic watchdog wake",
      "objective": "Native C2 Master Goal auto-continuation bypasses deterministic watchdog suppression: c2-master-goal-start sets thread/goal status active before waiting for its turn, but does not pause the Goal after a non-terminal turn finishes. Evidence after deterministic watchdog deployment: watchdog state remained waiting_external with should_wake_goal=false and unchanged last_wake_at, c2-master-goal.service was inactive, yet new Master Goal assistant turns continued to appear. Impact: repeated model-driven polling/token burn persists even though the watcher no longer wakes the Goal. Fix the controller so each deterministic wake yields one bounded turn and leaves a still-active/nonterminal Goal paused until the control-plane fingerprint changes.",
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
      "created_at": "2026-09-30T06:02:15Z",
      "updated_at": "2026-09-30T06:02:15Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:6d603f31e51b449788e2cd3d607d56b1",
        "tag": "priority:p1"
      },
      {
        "work_item_id": "wi:6d603f31e51b449788e2cd3d607d56b1",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2026,
        "work_item_id": "wi:6d603f31e51b449788e2cd3d607d56b1",
        "evidence_kind": "issue_inbox",
        "label": "issue:51f795b24f234d038882a583b9aeaf87",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Native C2 Master Goal auto-continuation bypasses deterministic watchdog suppression: c2-master-goal-start sets thread/goal status active before waiting for its turn, but does not pause the Goal after a non-terminal turn finishes. Evidence after deterministic watchdog deployment: watchdog state remained waiting_external with should_wake_goal=false and unchanged last_wake_at, c2-master-goal.service was inactive, yet new Master Goal assistant turns continued to appear. Impact: repeated model-driven polling/token burn persists even though the watcher no longer wakes the Goal. Fix the controller so each deterministic wake yields one bounded turn and leaves a still-active/nonterminal Goal paused until the control-plane fingerprint changes.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:51f795b24f234d038882a583b9aeaf87\", \"observed_at_ms\": 1790677394777, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"https://github.com/gernalix/codex-roadmap\"}",
        "created_at": "2026-09-30T06:02:15Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:51f795b24f234d038882a583b9aeaf87",
        "work_item_id": "wi:6d603f31e51b449788e2cd3d607d56b1",
        "role": "decision",
        "created_at": "2026-09-29T10:23:14Z"
      }
    ]
  }
]
```
