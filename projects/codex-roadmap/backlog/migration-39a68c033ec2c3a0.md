# Triage C2 issue inbox

<!-- migration-39a68c033ec2c3a0 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Merged duplicate/complementary observations and subtasks; every original requirement retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:e328b70d05f042d8b7ff763d440def70`, `wi:c30d552797d44b7b864a782bfb84caf4`, `wi:8c81a0c4a2bd422995ae76252889402f`, `wi:6574bc4f782f4925913d64cc7c0988e4`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Triage C2 issue inbox

Process every pending issue_inbox row. Use the canonical snapshot to identify related roadmap/repository work. Submit c2_promote_issue or c2_discard_issue through tools/c2_control.py with the current supervisor ID and fencing token. For active matches, promote into the existing work item with evidence. For completed matches, promote a regression successor; never discard as fixed. For irrelevant or obsolete issues, discard with a concrete reason. Read pending rows again before completion and finish only when none remain.

Acceptance:

- No pending issue_inbox rows remain at completion

status: failed

current_action: The prior C2 issue-inbox triage executor is no longer active

next_action: Create a fresh triage work item/run for the remaining pending issue_inbox rows

blocker: The prior ChatGPT triage run failed before clearing the pending inbox

### Triage C2 issue inbox

Process every pending issue_inbox row. Use the canonical snapshot to identify related roadmap/repository work. Submit c2_promote_issue or c2_discard_issue through tools/c2_control.py with the current supervisor ID and fencing token. For active matches, promote into the existing work item with evidence. For completed matches, promote a regression successor; never discard as fixed. For irrelevant or obsolete issues, discard with a concrete reason. Read pending rows again before completion and finish only when none remain.

Acceptance:

- No pending issue_inbox rows remain at completion

status: failed

current_action: Triage worker failed before delivery because the current ChatGPT composer was not found by the Playwright selector set; supervisor triaged the pending Inbox separately.

next_action: Fix wi:8ad34449ed6144b8be70b016afa77124 before relying on browser triage delivery; future Inbox triage may use a fresh canonical worker.

blocker: ChatGPT browser executor composer selector is incompatible with the current UI surface.

### Triage C2 issue inbox

Process every row from v_issue_inbox_pending_ordered in its displayed order. Use the canonical snapshot to identify related roadmap/repository work. Submit c2_promote_issue or c2_discard_issue through tools/c2_control.py with the current supervisor ID and fencing token. For every row, create human-facing copy before disposition. human_title must be plain Italian, concrete, normally 20-90 characters (hard max 120), contain no unnecessary IDs or implementation jargon, and never end in ellipsis. ai_title must remain technically precise (hard max 220). human_summary must explain in 1-3 short Italian sentences what changes and why it matters (hard max 600). If the source is too ambiguous to translate safely, never guess: use copy_status=needs_clarification, human_title='Chiarire: <area comprensibile>', and a human_summary stating exactly what is missing. Submit c2_set_human_copy for the issue; when promoting, pass the same human_title, ai_title, human_summary and copy_status so the roadmap item inherits the copy. For active matches, promote into the existing work item with evidence. For completed matches, promote a regression successor; never discard as fixed. For each promotion, record any known priority or dependency consequence without reprioritizing the whole queue. After the full Inbox drain, reconcile relative priority and dependencies in both directions, duplicates, obsolete work, and incomplete items against the resulting queue once; encode verified changes explicitly before finishing. For irrelevant or obsolete issues, discard with a concrete reason. Read pending rows again before completion and finish only when none remain.

Acceptance:

- No pending issue_inbox rows remain at completion
- Post-drain roadmap reconciliation is recorded before completion

status: failed

current_action: DRAIN_INBOX_NATIVE

next_action: Run the non-GUI fenced Inbox drain executor until v_issue_inbox_pending_ordered is empty.

### Triage C2 issue inbox

Process every row from v_issue_inbox_pending_ordered in its displayed order. Use the canonical snapshot to identify related roadmap/repository work. Submit c2_promote_issue or c2_discard_issue through tools/c2_control.py with the current supervisor ID and fencing token. For every row, create human-facing copy before disposition. human_title must be plain Italian, concrete, normally 20-90 characters (hard max 120), contain no unnecessary IDs or implementation jargon, and never end in ellipsis. ai_title must remain technically precise (hard max 220). human_summary must explain in 1-3 short Italian sentences what changes and why it matters (hard max 600). If the source is too ambiguous to translate safely, never guess: use copy_status=needs_clarification, human_title='Chiarire: <area comprensibile>', and a human_summary stating exactly what is missing. Submit c2_set_human_copy for the issue; when promoting, pass the same human_title, ai_title, human_summary and copy_status so the roadmap item inherits the copy. For active matches, promote into the existing work item with evidence. For completed matches, promote a regression successor; never discard as fixed. For each promotion, record any known priority or dependency consequence without reprioritizing the whole queue. After the full Inbox drain, reconcile relative priority and dependencies in both directions, duplicates, obsolete work, and incomplete items against the resulting queue once; encode verified changes explicitly before finishing. For irrelevant or obsolete issues, discard with a concrete reason. Read pending rows again before completion and finish only when none remain.

Acceptance:

- No pending issue_inbox rows remain at completion
- Post-drain roadmap reconciliation is recorded before completion

status: failed

next_action: Read v_issue_inbox_pending_ordered; apply one fenced disposition per row in order.

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
      "work_item_id": "wi:e328b70d05f042d8b7ff763d440def70",
      "parent_id": null,
      "kind": "task",
      "title": "Triage C2 issue inbox",
      "objective": "Process every pending issue_inbox row. Use the canonical snapshot to identify related roadmap/repository work. Submit c2_promote_issue or c2_discard_issue through tools/c2_control.py with the current supervisor ID and fencing token. For active matches, promote into the existing work item with evidence. For completed matches, promote a regression successor; never discard as fixed. For irrelevant or obsolete issues, discard with a concrete reason. Read pending rows again before completion and finish only when none remain.",
      "acceptance_json": "[\"No pending issue_inbox rows remain at completion\"]",
      "status": "failed",
      "executor_policy": "auto",
      "sort_order": null,
      "current_action": "The prior C2 issue-inbox triage executor is no longer active",
      "next_action": "Create a fresh triage work item/run for the remaining pending issue_inbox rows",
      "blocker": "The prior ChatGPT triage run failed before clearing the pending inbox",
      "project_id": null,
      "project_name": null,
      "repo": null,
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-26T22:29:50Z",
      "updated_at": "2026-09-27T00:43:30Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:e328b70d05f042d8b7ff763d440def70",
        "tag": "c2:issue-triage"
      },
      {
        "work_item_id": "wi:e328b70d05f042d8b7ff763d440def70",
        "tag": "priority:p0"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [
      {
        "receipt_id": "run:44feb2e758ac4f30b9ee3b183fcbdb13",
        "work_item_id": "wi:e328b70d05f042d8b7ff763d440def70",
        "run_id": "44feb2e758ac4f30b9ee3b183fcbdb13",
        "prompt_id": null,
        "outcome": "FAIL",
        "summary": "The prior C2 issue-inbox triage executor is no longer active",
        "completed_json": "[]",
        "remaining_json": "[\"Pending issue_inbox rows still require triage\"]",
        "evidence_json": "[\"Canonical run 44feb2e758ac4f30b9ee3b183fcbdb13 is already state=failed and no matching worker process exists\"]",
        "blocker": "The prior ChatGPT triage run failed before clearing the pending inbox",
        "next_action": "Create a fresh triage work item/run for the remaining pending issue_inbox rows",
        "strict_contract": 1,
        "payload_sha256": "426740e2af66533feb01889786d74aa766094280517897887af1ed8826a78763",
        "captured_at": 1790486735.6221695
      }
    ],
    "work_item_evidence": [
      {
        "evidence_id": 506,
        "work_item_id": "wi:e328b70d05f042d8b7ff763d440def70",
        "evidence_kind": "classification",
        "label": "Existing failed browser delivery run is terminal; current manual ChatGPT session is directly executing the canonical sem",
        "uri": null,
        "value_json": "\"Existing failed browser delivery run is terminal; current manual ChatGPT session is directly executing the canonical semantic triage work item, so browser recovery is no longer required.\"",
        "created_at": "2026-09-27T00:43:30Z"
      },
      {
        "evidence_id": 545,
        "work_item_id": "wi:e328b70d05f042d8b7ff763d440def70",
        "evidence_kind": "executor_result",
        "label": "Canonical run 44feb2e758ac4f30b9ee3b183fcbdb13 is already state=failed and no matching worker process exists",
        "uri": null,
        "value_json": "\"Canonical run 44feb2e758ac4f30b9ee3b183fcbdb13 is already state=failed and no matching worker process exists\"",
        "created_at": "2026-09-27T05:25:35Z"
      }
    ],
    "work_item_runs": [
      {
        "run_id": "44feb2e758ac4f30b9ee3b183fcbdb13",
        "work_item_id": "wi:e328b70d05f042d8b7ff763d440def70",
        "event_key": "c2-schedule-2c1102f30d6a8b5c3091a9c54cbf1fb2",
        "attempt": 1,
        "executor": "chatgpt",
        "state": "failed",
        "lease_until": 0.0,
        "worker_ref": null,
        "checkpoint_commit": null,
        "metadata_json": "{\"activity\": \"semantic\", \"command_json\": null, \"executor\": \"chatgpt\", \"goal_mode\": 0, \"max_attempts\": 3, \"model\": null, \"pre_migration_retirement\": {\"checkpoint_commit\": null, \"classification\": \"historical-only\", \"lease_until\": 1790462759.1056669, \"previous_state\": \"failed\", \"worker_ref\": \"c2-run:44feb2e758ac4f30b9ee3b183fcbdb13\"}, \"project_url\": \"https://chatgpt.com/g/g-p-6ab69fbdbaf88191a39a75ff5c9e3d70/project\", \"prompt_id\": null, \"reasoning\": null, \"repo\": null, \"resources_json\": \"[\\\"c2:issue-triage\\\"]\", \"work_item_id\": \"wi:e328b70d05f042d8b7ff763d440def70\", \"worktree\": null}",
        "created_at": 1790462601.4020302
      }
    ],
    "issue_work_item_links": []
  },
  {
    "routing": {
      "project": "51",
      "reason": "semantic correction of source routing; original identity preserved",
      "related_projects": [
        "51"
      ]
    },
    "source": {
      "work_item_id": "wi:c30d552797d44b7b864a782bfb84caf4",
      "parent_id": null,
      "kind": "task",
      "title": "Triage C2 issue inbox",
      "objective": "Process every pending issue_inbox row. Use the canonical snapshot to identify related roadmap/repository work. Submit c2_promote_issue or c2_discard_issue through tools/c2_control.py with the current supervisor ID and fencing token. For active matches, promote into the existing work item with evidence. For completed matches, promote a regression successor; never discard as fixed. For irrelevant or obsolete issues, discard with a concrete reason. Read pending rows again before completion and finish only when none remain.",
      "acceptance_json": "[\"No pending issue_inbox rows remain at completion\"]",
      "status": "failed",
      "executor_policy": "auto",
      "sort_order": null,
      "current_action": "Triage worker failed before delivery because the current ChatGPT composer was not found by the Playwright selector set; supervisor triaged the pending Inbox separately.",
      "next_action": "Fix wi:8ad34449ed6144b8be70b016afa77124 before relying on browser triage delivery; future Inbox triage may use a fresh canonical worker.",
      "blocker": "ChatGPT browser executor composer selector is incompatible with the current UI surface.",
      "project_id": null,
      "project_name": null,
      "repo": null,
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-27T07:43:20Z",
      "updated_at": "2026-09-27T07:43:20Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:c30d552797d44b7b864a782bfb84caf4",
        "tag": "c2:issue-triage"
      },
      {
        "work_item_id": "wi:c30d552797d44b7b864a782bfb84caf4",
        "tag": "priority:p0"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [
      {
        "receipt_id": "run:9ec355c5963741e49b3e06a0f97728bc",
        "work_item_id": "wi:c30d552797d44b7b864a782bfb84caf4",
        "run_id": "9ec355c5963741e49b3e06a0f97728bc",
        "prompt_id": null,
        "outcome": "FAIL",
        "summary": "Triage worker failed before delivery because the current ChatGPT composer was not found by the Playwright selector set; supervisor triaged the pending Inbox separately.",
        "completed_json": "[\"Pending Inbox rows were dispositioned canonically by the supervisor.\"]",
        "remaining_json": "[]",
        "evidence_json": "[\"Run 9ec355c5963741e49b3e06a0f97728bc had no durable successful ChatGPT delivery and the selector failure is captured/matched to wi:8ad34449ed6144b8be70b016afa77124.\", \"Canonical issue_inbox pending count is now zero.\"]",
        "blocker": "ChatGPT browser executor composer selector is incompatible with the current UI surface.",
        "next_action": "Fix wi:8ad34449ed6144b8be70b016afa77124 before relying on browser triage delivery; future Inbox triage may use a fresh canonical worker.",
        "strict_contract": 1,
        "payload_sha256": "5639e476ddca96f7f9d43c5710500830125753eb06534266c3ec019f298e2274",
        "captured_at": 1790498647.6846433
      }
    ],
    "work_item_evidence": [
      {
        "evidence_id": 601,
        "work_item_id": "wi:c30d552797d44b7b864a782bfb84caf4",
        "evidence_kind": "executor_result",
        "label": "Run 9ec355c5963741e49b3e06a0f97728bc had no durable successful ChatGPT delivery and the selector failure is captured/mat",
        "uri": null,
        "value_json": "\"Run 9ec355c5963741e49b3e06a0f97728bc had no durable successful ChatGPT delivery and the selector failure is captured/matched to wi:8ad34449ed6144b8be70b016afa77124.\"",
        "created_at": "2026-09-27T08:44:07Z"
      },
      {
        "evidence_id": 602,
        "work_item_id": "wi:c30d552797d44b7b864a782bfb84caf4",
        "evidence_kind": "executor_result",
        "label": "Canonical issue_inbox pending count is now zero.",
        "uri": null,
        "value_json": "\"Canonical issue_inbox pending count is now zero.\"",
        "created_at": "2026-09-27T08:44:07Z"
      }
    ],
    "work_item_runs": [
      {
        "run_id": "9ec355c5963741e49b3e06a0f97728bc",
        "work_item_id": "wi:c30d552797d44b7b864a782bfb84caf4",
        "event_key": "c2-schedule-69e382bf80e34f46847ccaa5ab2ba8e6",
        "attempt": 1,
        "executor": "chatgpt",
        "state": "failed",
        "lease_until": 0.0,
        "worker_ref": null,
        "checkpoint_commit": null,
        "metadata_json": "{\"activity\": \"semantic\", \"command_json\": null, \"executor\": \"chatgpt\", \"goal_mode\": 0, \"max_attempts\": 3, \"model\": null, \"pre_migration_retirement\": {\"checkpoint_commit\": null, \"classification\": \"historical-only\", \"lease_until\": 1790496170.4449153, \"previous_state\": \"failed\", \"worker_ref\": \"c2-run:9ec355c5963741e49b3e06a0f97728bc\"}, \"project_url\": \"https://chatgpt.com/g/g-p-6ab69fbdbaf88191a39a75ff5c9e3d70/project\", \"prompt_id\": null, \"reasoning\": null, \"repo\": null, \"resources_json\": \"[\\\"c2:issue-triage\\\"]\", \"work_item_id\": \"wi:c30d552797d44b7b864a782bfb84caf4\", \"worktree\": null}",
        "created_at": 1790495092.4335933
      }
    ],
    "issue_work_item_links": []
  },
  {
    "routing": {
      "project": "51",
      "reason": "semantic correction of source routing; original identity preserved",
      "related_projects": [
        "51"
      ]
    },
    "source": {
      "work_item_id": "wi:8c81a0c4a2bd422995ae76252889402f",
      "parent_id": null,
      "kind": "task",
      "title": "Triage C2 issue inbox",
      "objective": "Process every row from v_issue_inbox_pending_ordered in its displayed order. Use the canonical snapshot to identify related roadmap/repository work. Submit c2_promote_issue or c2_discard_issue through tools/c2_control.py with the current supervisor ID and fencing token. For every row, create human-facing copy before disposition. human_title must be plain Italian, concrete, normally 20-90 characters (hard max 120), contain no unnecessary IDs or implementation jargon, and never end in ellipsis. ai_title must remain technically precise (hard max 220). human_summary must explain in 1-3 short Italian sentences what changes and why it matters (hard max 600). If the source is too ambiguous to translate safely, never guess: use copy_status=needs_clarification, human_title='Chiarire: <area comprensibile>', and a human_summary stating exactly what is missing. Submit c2_set_human_copy for the issue; when promoting, pass the same human_title, ai_title, human_summary and copy_status so the roadmap item inherits the copy. For active matches, promote into the existing work item with evidence. For completed matches, promote a regression successor; never discard as fixed. For each promotion, record any known priority or dependency consequence without reprioritizing the whole queue. After the full Inbox drain, reconcile relative priority and dependencies in both directions, duplicates, obsolete work, and incomplete items against the resulting queue once; encode verified changes explicitly before finishing. For irrelevant or obsolete issues, discard with a concrete reason. Read pending rows again before completion and finish only when none remain.",
      "acceptance_json": "[\"No pending issue_inbox rows remain at completion\", \"Post-drain roadmap reconciliation is recorded before completion\"]",
      "status": "failed",
      "executor_policy": "auto",
      "sort_order": null,
      "current_action": "DRAIN_INBOX_NATIVE",
      "next_action": "Run the non-GUI fenced Inbox drain executor until v_issue_inbox_pending_ordered is empty.",
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
      "created_at": "2026-09-28T10:46:18Z",
      "updated_at": "2026-09-29T00:10:29Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:8c81a0c4a2bd422995ae76252889402f",
        "tag": "c2:issue-triage"
      },
      {
        "work_item_id": "wi:8c81a0c4a2bd422995ae76252889402f",
        "tag": "priority:p0"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 1659,
        "work_item_id": "wi:8c81a0c4a2bd422995ae76252889402f",
        "evidence_kind": "classification",
        "label": "Existing ChatGPT triage run repeatedly suspended because disable-chat-supervisor kill-switch is intentionally active; no",
        "uri": null,
        "value_json": "\"Existing ChatGPT triage run repeatedly suspended because disable-chat-supervisor kill-switch is intentionally active; no Inbox disposition was produced.\"",
        "created_at": "2026-09-29T00:10:29Z"
      }
    ],
    "work_item_runs": [
      {
        "run_id": "83fe3e8cecc44f6db621276bb9bac000",
        "work_item_id": "wi:8c81a0c4a2bd422995ae76252889402f",
        "event_key": "c2-schedule-d0f0aae967335a3c6281ee2dade4b538",
        "attempt": 1,
        "executor": "chatgpt",
        "state": "failed",
        "lease_until": 0.0,
        "worker_ref": null,
        "checkpoint_commit": null,
        "metadata_json": "{\"activity\": \"semantic\", \"command_json\": null, \"executor\": \"chatgpt\", \"goal_mode\": 0, \"max_attempts\": 3, \"model\": null, \"pre_migration_retirement\": {\"checkpoint_commit\": null, \"classification\": \"historical-only\", \"lease_until\": 1790640008.7984533, \"previous_state\": \"failed\", \"worker_ref\": \"c2-run:83fe3e8cecc44f6db621276bb9bac000\"}, \"project_url\": \"https://chatgpt.com/g/g-p-6ab69fbdbaf88191a39a75ff5c9e3d70/project\", \"prompt_id\": null, \"reasoning\": null, \"repo\": null, \"resources_json\": \"[\\\"c2:issue-triage\\\"]\", \"work_item_id\": \"wi:8c81a0c4a2bd422995ae76252889402f\", \"worktree\": null}",
        "created_at": 1790592467.5236194
      },
      {
        "run_id": "b3eb915b122547af9af1cafb037c253b",
        "work_item_id": "wi:8c81a0c4a2bd422995ae76252889402f",
        "event_key": "c2-schedule-4d12f0d256c094f3cc78dcd6a28d64cc",
        "attempt": 2,
        "executor": "rdc",
        "state": "failed",
        "lease_until": 0.0,
        "worker_ref": null,
        "checkpoint_commit": null,
        "metadata_json": "{\"activity\": \"native\", \"command_json\": \"[\\\"/home/daniele/.local/bin/c2-inbox-drain-native\\\"]\", \"executor\": \"rdc\", \"goal_mode\": 0, \"max_attempts\": 3, \"model\": null, \"pre_migration_retirement\": {\"checkpoint_commit\": null, \"classification\": \"historical-only\", \"lease_until\": 1790644663.6189673, \"previous_state\": \"failed\", \"worker_ref\": \"c2-run:b3eb915b122547af9af1cafb037c253b\"}, \"project_url\": null, \"prompt_id\": null, \"reasoning\": null, \"repo\": null, \"resources_json\": \"[\\\"c2:issue-triage\\\"]\", \"work_item_id\": \"wi:8c81a0c4a2bd422995ae76252889402f\", \"worktree\": null}",
        "created_at": 1790640694.5187123
      }
    ],
    "issue_work_item_links": []
  },
  {
    "routing": {
      "project": "51",
      "reason": "semantic correction of source routing; original identity preserved",
      "related_projects": [
        "51"
      ]
    },
    "source": {
      "work_item_id": "wi:6574bc4f782f4925913d64cc7c0988e4",
      "parent_id": null,
      "kind": "task",
      "title": "Triage C2 issue inbox",
      "objective": "Process every row from v_issue_inbox_pending_ordered in its displayed order. Use the canonical snapshot to identify related roadmap/repository work. Submit c2_promote_issue or c2_discard_issue through tools/c2_control.py with the current supervisor ID and fencing token. For every row, create human-facing copy before disposition. human_title must be plain Italian, concrete, normally 20-90 characters (hard max 120), contain no unnecessary IDs or implementation jargon, and never end in ellipsis. ai_title must remain technically precise (hard max 220). human_summary must explain in 1-3 short Italian sentences what changes and why it matters (hard max 600). If the source is too ambiguous to translate safely, never guess: use copy_status=needs_clarification, human_title='Chiarire: <area comprensibile>', and a human_summary stating exactly what is missing. Submit c2_set_human_copy for the issue; when promoting, pass the same human_title, ai_title, human_summary and copy_status so the roadmap item inherits the copy. For active matches, promote into the existing work item with evidence. For completed matches, promote a regression successor; never discard as fixed. For each promotion, record any known priority or dependency consequence without reprioritizing the whole queue. After the full Inbox drain, reconcile relative priority and dependencies in both directions, duplicates, obsolete work, and incomplete items against the resulting queue once; encode verified changes explicitly before finishing. For irrelevant or obsolete issues, discard with a concrete reason. Read pending rows again before completion and finish only when none remain.",
      "acceptance_json": "[\"No pending issue_inbox rows remain at completion\", \"Post-drain roadmap reconciliation is recorded before completion\"]",
      "status": "failed",
      "executor_policy": "auto",
      "sort_order": null,
      "current_action": null,
      "next_action": "Read v_issue_inbox_pending_ordered; apply one fenced disposition per row in order.",
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
      "created_at": "2026-09-29T00:30:37Z",
      "updated_at": "2026-09-29T00:30:37Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:6574bc4f782f4925913d64cc7c0988e4",
        "tag": "c2:issue-triage"
      },
      {
        "work_item_id": "wi:6574bc4f782f4925913d64cc7c0988e4",
        "tag": "priority:p0"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [],
    "work_item_runs": [
      {
        "run_id": "374a7ccb2145446591d35e1d27ee2cdd",
        "work_item_id": "wi:6574bc4f782f4925913d64cc7c0988e4",
        "event_key": "c2-schedule-a3e430ca410753cc5889f2861400ca72",
        "attempt": 1,
        "executor": "rdc",
        "state": "failed",
        "lease_until": 0.0,
        "worker_ref": null,
        "checkpoint_commit": null,
        "metadata_json": "{\"activity\": \"native\", \"command_json\": \"[\\\"/home/daniele/.local/bin/c2-inbox-drain-native\\\"]\", \"executor\": \"rdc\", \"goal_mode\": 0, \"max_attempts\": 3, \"model\": null, \"pre_migration_retirement\": {\"checkpoint_commit\": null, \"classification\": \"historical-only\", \"lease_until\": 1790646702.5078495, \"previous_state\": \"failed\", \"worker_ref\": \"c2-run:374a7ccb2145446591d35e1d27ee2cdd\"}, \"project_url\": null, \"prompt_id\": null, \"reasoning\": null, \"repo\": null, \"resources_json\": \"[\\\"c2:issue-triage\\\"]\", \"work_item_id\": \"wi:6574bc4f782f4925913d64cc7c0988e4\", \"worktree\": null}",
        "created_at": 1790642736.3340795
      }
    ],
    "issue_work_item_links": []
  }
]
```
