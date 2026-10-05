# Operational task state — ADB Wi-Fi keeper latency

<!-- migration-b52c597d82a82231 -->

Migrated project backlog. Project: **adb-device-keeper**; project_id: 95.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Merged duplicate/complementary observations and subtasks; every original requirement retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 95.

Provenance: `task:CHATGPT-20260925-ADB-KEEPER-LATENCY`, `state:gate:9ad7b5812f954676d1c8`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Operational task state — ADB Wi-Fi keeper latency

status: waiting

current_action: The runtime fix is already deployed and verified. Source is pushed at task branch commit ff629562164d20449a41f4a9780490ce6dfa2c1e. The only source-integration blocker is GitHub Actions billing/spending-limit refusal; do not rerun identical CI until that account condition changes.

next_action: Do not rerun the blocked GitHub Actions job. First verify whether the billing/spending-limit prerequisite has changed; if unchanged, leave PR #2 safely pending and perform only non-destructive service health readback. When CI/integration becomes available, integrate ff62956 to main, then perform the single post-reboot acceptance check.

blocker: GitHub Actions billing/spending-limit prevents CI/integration of PR 2; await account-state change.

### Resolve blocker: GitHub Actions cannot start the deterministic job because of the account billing/spending-limit condition. This is external to the code change.

status: blocked

next_action: Restore GitHub Actions billing/runner gate, rerun required CI, then guarded integrate.

blocker: adb-device-keeper PR #2 remains open with required deterministic CI failed under account billing/spending-limit evidence.

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "95",
      "reason": "semantic correction of source routing; original identity preserved",
      "related_projects": [
        "95"
      ]
    },
    "source": {
      "work_item_id": "task:CHATGPT-20260925-ADB-KEEPER-LATENCY",
      "parent_id": null,
      "kind": "task",
      "title": "Operational task state — ADB Wi-Fi keeper latency",
      "objective": null,
      "acceptance_json": null,
      "status": "waiting",
      "executor_policy": "auto",
      "sort_order": null,
      "current_action": "The runtime fix is already deployed and verified. Source is pushed at task branch commit ff629562164d20449a41f4a9780490ce6dfa2c1e. The only source-integration blocker is GitHub Actions billing/spending-limit refusal; do not rerun identical CI until that account condition changes.",
      "next_action": "Do not rerun the blocked GitHub Actions job. First verify whether the billing/spending-limit prerequisite has changed; if unchanged, leave PR #2 safely pending and perform only non-destructive service health readback. When CI/integration becomes available, integrate ff62956 to main, then perform the single post-reboot acceptance check.",
      "blocker": "GitHub Actions billing/spending-limit prevents CI/integration of PR 2; await account-state change.",
      "project_id": null,
      "project_name": null,
      "repo": null,
      "prompt_id": null,
      "task_id": "CHATGPT-20260925-ADB-KEEPER-LATENCY",
      "required": 1,
      "actionable": 0,
      "source_kind": "task_state",
      "source_ref": "CHATGPT-20260925-ADB-KEEPER-LATENCY.md",
      "created_at": "2026-09-25T15:54:51Z",
      "updated_at": "2026-09-26T17:12:41Z"
    },
    "work_item_tags": [],
    "work_item_dependencies": [],
    "work_item_relations": [
      {
        "from_work_item_id": "state:step:63ae4d9a0f58b01e4079",
        "to_work_item_id": "task:CHATGPT-20260925-ADB-KEEPER-LATENCY",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:51:16Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:44dcfb45a24fb6986267",
        "to_work_item_id": "task:CHATGPT-20260925-ADB-KEEPER-LATENCY",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:51:16Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:phase:d782b96c5fa7dbd1b8db",
        "to_work_item_id": "task:CHATGPT-20260925-ADB-KEEPER-LATENCY",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:51:16Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:c7048f3f5721fc2d6c72",
        "to_work_item_id": "task:CHATGPT-20260925-ADB-KEEPER-LATENCY",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:51:16Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:9fe05c6a607b3a9aeafb",
        "to_work_item_id": "task:CHATGPT-20260925-ADB-KEEPER-LATENCY",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:51:16Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:28cbf219208a356b64aa",
        "to_work_item_id": "task:CHATGPT-20260925-ADB-KEEPER-LATENCY",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:51:16Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      }
    ],
    "work_item_checkpoints": [
      {
        "checkpoint_id": 16,
        "work_item_id": "task:CHATGPT-20260925-ADB-KEEPER-LATENCY",
        "source_file": "CHATGPT-20260925-ADB-KEEPER-LATENCY.md",
        "source_commit": "52bea96d02f55fac91cea210cf2e370b5963cc4f",
        "source_sha256": "f2cd8779984446461387c7c92dc41054d60f25c5fc7ac94170fbb7d73aee66be",
        "objective": "Restore reliable always-on Android wireless-debug reconnect behavior on Fedora and persist the verified latency fix safely to the canonical adb-device-keeper main branch.",
        "current_step": "The runtime fix is already deployed and verified. Source is pushed at task branch commit ff629562164d20449a41f4a9780490ce6dfa2c1e. The only source-integration blocker is GitHub Actions billing/spending-limit refusal; do not rerun identical CI until that account condition changes.",
        "next_action": null,
        "blocker": "pre-migration / retired: historical evidence only",
        "completed_json": "[\"Root cause narrowed to excessively slow polling/retry cadence rather than a dead service.\", \"Runtime polling intervals tightened.\", \"Two-device reconnect smoke verified.\", \"Fix committed and pushed to the isolated task branch.\"]",
        "remaining_json": "[\"Resolve/clear the external GitHub Actions billing/spending-limit prerequisite or use the repository's approved integration path if it can accept existing deterministic local evidence.\", \"Merge/integrate PR #2 to main without bypassing repository protections.\", \"Perform one normal Fedora reboot and verify adb-device-keeper returns enabled/active and reconnects both devices automatically.\"]",
        "evidence_json": "[\"Task commit ff629562164d20449a41f4a9780490ce6dfa2c1e.\", \"PR #2: [single-writer] CHATGPT-20260925-ADB-KEEPER-LATENCY.\", \"GitHub Actions run 36108598671: deterministic job conclusion=failure with zero steps; billing/spending-limit annotation.\", \"GitGuardian Security Checks: PASS.\", \"Remote task branch contains ff62956 and worktree is clean.\", \"Prior live reconnect test: Pixel 8a PASS ~15 s, TCL 6102H PASS ~15 s.\"]",
        "captured_at": "2026-09-25T15:54:51Z"
      }
    ],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 295,
        "work_item_id": "task:CHATGPT-20260925-ADB-KEEPER-LATENCY",
        "evidence_kind": "completed",
        "label": "Root cause narrowed to excessively slow polling/retry cadence rather than a dead service.",
        "uri": "state://CHATGPT-20260925-ADB-KEEPER-LATENCY.md#completed-59dce810982b75fc",
        "value_json": "{\"text\": \"Root cause narrowed to excessively slow polling/retry cadence rather than a dead service.\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 296,
        "work_item_id": "task:CHATGPT-20260925-ADB-KEEPER-LATENCY",
        "evidence_kind": "completed",
        "label": "Runtime polling intervals tightened.",
        "uri": "state://CHATGPT-20260925-ADB-KEEPER-LATENCY.md#completed-2a46aad9fc836359",
        "value_json": "{\"text\": \"Runtime polling intervals tightened.\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 297,
        "work_item_id": "task:CHATGPT-20260925-ADB-KEEPER-LATENCY",
        "evidence_kind": "completed",
        "label": "Two-device reconnect smoke verified.",
        "uri": "state://CHATGPT-20260925-ADB-KEEPER-LATENCY.md#completed-687f55f0b16fa461",
        "value_json": "{\"text\": \"Two-device reconnect smoke verified.\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 298,
        "work_item_id": "task:CHATGPT-20260925-ADB-KEEPER-LATENCY",
        "evidence_kind": "completed",
        "label": "Fix committed and pushed to the isolated task branch.",
        "uri": "state://CHATGPT-20260925-ADB-KEEPER-LATENCY.md#completed-3133cc571060e56f",
        "value_json": "{\"text\": \"Fix committed and pushed to the isolated task branch.\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 299,
        "work_item_id": "task:CHATGPT-20260925-ADB-KEEPER-LATENCY",
        "evidence_kind": "evidence",
        "label": "Task commit ff629562164d20449a41f4a9780490ce6dfa2c1e.",
        "uri": "state://CHATGPT-20260925-ADB-KEEPER-LATENCY.md#evidence-37fcf9d1aaca8ed0",
        "value_json": "{\"text\": \"Task commit ff629562164d20449a41f4a9780490ce6dfa2c1e.\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 300,
        "work_item_id": "task:CHATGPT-20260925-ADB-KEEPER-LATENCY",
        "evidence_kind": "evidence",
        "label": "PR #2: [single-writer] CHATGPT-20260925-ADB-KEEPER-LATENCY.",
        "uri": "state://CHATGPT-20260925-ADB-KEEPER-LATENCY.md#evidence-e60bcdbfd8703f6d",
        "value_json": "{\"text\": \"PR #2: [single-writer] CHATGPT-20260925-ADB-KEEPER-LATENCY.\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 301,
        "work_item_id": "task:CHATGPT-20260925-ADB-KEEPER-LATENCY",
        "evidence_kind": "evidence",
        "label": "GitHub Actions run 36108598671: deterministic job conclusion=failure with zero steps; billing/spending-limit annotation.",
        "uri": "state://CHATGPT-20260925-ADB-KEEPER-LATENCY.md#evidence-75ef0f1927a7fe1b",
        "value_json": "{\"text\": \"GitHub Actions run 36108598671: deterministic job conclusion=failure with zero steps; billing/spending-limit annotation.\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 302,
        "work_item_id": "task:CHATGPT-20260925-ADB-KEEPER-LATENCY",
        "evidence_kind": "evidence",
        "label": "GitGuardian Security Checks: PASS.",
        "uri": "state://CHATGPT-20260925-ADB-KEEPER-LATENCY.md#evidence-c065e3c313354b1e",
        "value_json": "{\"text\": \"GitGuardian Security Checks: PASS.\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 303,
        "work_item_id": "task:CHATGPT-20260925-ADB-KEEPER-LATENCY",
        "evidence_kind": "evidence",
        "label": "Remote task branch contains ff62956 and worktree is clean.",
        "uri": "state://CHATGPT-20260925-ADB-KEEPER-LATENCY.md#evidence-45237b6927b536d4",
        "value_json": "{\"text\": \"Remote task branch contains ff62956 and worktree is clean.\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 304,
        "work_item_id": "task:CHATGPT-20260925-ADB-KEEPER-LATENCY",
        "evidence_kind": "evidence",
        "label": "Prior live reconnect test: Pixel 8a PASS ~15 s, TCL 6102H PASS ~15 s.",
        "uri": "state://CHATGPT-20260925-ADB-KEEPER-LATENCY.md#evidence-f2e5ab9db8d4d469",
        "value_json": "{\"text\": \"Prior live reconnect test: Pixel 8a PASS ~15 s, TCL 6102H PASS ~15 s.\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 361,
        "work_item_id": "task:CHATGPT-20260925-ADB-KEEPER-LATENCY",
        "evidence_kind": "classification",
        "label": "adb-device-keeper PR 2 head ff629562 is open; GitHub Actions deterministic test cannot start due billing/spending-limit,",
        "uri": null,
        "value_json": "\"adb-device-keeper PR 2 head ff629562 is open; GitHub Actions deterministic test cannot start due billing/spending-limit, while local adb-device-keeper service is active.\"",
        "created_at": "2026-09-26T17:12:41Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [],
    "source_document": {
      "path": "/home/daniele/projects/codex-roadmap/operations/task-state/CHATGPT-20260925-ADB-KEEPER-LATENCY.md",
      "text": "# Operational task state — ADB Wi-Fi keeper latency\n\nTASK_ID: CHATGPT-20260925-ADB-KEEPER-LATENCY\nUpdated: 2026-09-25 Europe/Copenhagen\n\n## Objective\nRestore reliable always-on Android wireless-debug reconnect behavior on Fedora and persist the verified latency fix safely to the canonical adb-device-keeper main branch.\n\n## Constraints\n- Use Remote Desktop Commander for Fedora/runtime work.\n- Preserve existing Android pairing/authentication state.\n- Do not reset devices or ADB keys unless evidence requires it.\n- Reuse already verified runtime evidence; do not repeat destructive reconnect tests without need.\n- Treat Git/checkpoint state as canonical memory for continuation.\n\n## Plan / checklist\n- [x] Diagnose why the service appears not to reconnect promptly after an ADB Wi-Fi disconnect.\n- [x] Reduce normal health-check interval from 60 s to 15 s.\n- [x] Reduce missing-device retry interval from 25 s to 10 s.\n- [x] Verify forced disconnect/reconnect on Pixel 8a and TCL 6102H.\n- [x] Commit and push the fix on isolated task branch.\n- [ ] Integrate PR #2 into main once GitHub Actions can run or an approved equivalent gate is available.\n- [ ] Verify the service remains enabled/active and reconnect behavior survives one normal Fedora reboot.\n## Current step\nThe runtime fix is already deployed and verified. Source is pushed at task branch commit ff629562164d20449a41f4a9780490ce6dfa2c1e. The only source-integration blocker is GitHub Actions billing/spending-limit refusal; do not rerun identical CI until that account condition changes.\n\n## Verified facts\n- Repository: gernalix/adb-device-keeper.\n- Task branch: task/CHATGPT-20260925-ADB-KEEPER-LATENCY.\n- Pushed task commit: ff629562164d20449a41f4a9780490ce6dfa2c1e (Reduce ADB reconnect detection latency).\n- PR #2 targets main and is OPEN.\n- Real reconnect smoke previously passed on both physical devices: Pixel 8a approximately 15 s; TCL 6102H approximately 15 s.\n- Service was reported enabled + active with no abnormal restarts after the fix.\n- Current canonical checkout main is b5a2c22375d16d9d433ebfbf51909e6b6e6ec4db and does not yet contain ff62956.\n- GitHub Actions run 36108598671 failed before executing any steps; annotation states recent account payments failed or spending limit must be increased.\n- GitGuardian Security Checks pass.\n- Task worktree is clean and tracks origin/task/CHATGPT-20260925-ADB-KEEPER-LATENCY.\n\n## Decisions\n- Do not reinterpret the CI failure as a product/test failure; no CI steps actually ran.\n- Do not retry the same GitHub Actions job without a billing/spending-limit state change.\n- Keep the verified runtime fix deployed while source integration waits.\n- Reboot verification remains the final runtime acceptance gate after source persistence is settled or when a safe reboot is otherwise appropriate.\n\n## Completed\n- Root cause narrowed to excessively slow polling/retry cadence rather than a dead service.\n- Runtime polling intervals tightened.\n- Two-device reconnect smoke verified.\n- Fix committed and pushed to the isolated task branch.\n## Remaining\n- Resolve/clear the external GitHub Actions billing/spending-limit prerequisite or use the repository's approved integration path if it can accept existing deterministic local evidence.\n- Merge/integrate PR #2 to main without bypassing repository protections.\n- Perform one normal Fedora reboot and verify adb-device-keeper returns enabled/active and reconnects both devices automatically.\n\n## Blockers\n- GitHub Actions cannot start the deterministic job because of the account billing/spending-limit condition. This is external to the code change.\n\n## Evidence\n- Task commit ff629562164d20449a41f4a9780490ce6dfa2c1e.\n- PR #2: [single-writer] CHATGPT-20260925-ADB-KEEPER-LATENCY.\n- GitHub Actions run 36108598671: deterministic job conclusion=failure with zero steps; billing/spending-limit annotation.\n- GitGuardian Security Checks: PASS.\n- Remote task branch contains ff62956 and worktree is clean.\n- Prior live reconnect test: Pixel 8a PASS ~15 s, TCL 6102H PASS ~15 s.\n\n## Acceptance criteria\n- [x] Wireless ADB reconnect latency is reduced and verified on both physical devices.\n- [x] Source fix is committed and pushed on an isolated task branch.\n- [ ] Fix is integrated into canonical main through the repository's safe integration flow.\n- [ ] One post-reboot live readback confirms service enabled/active and automatic reconnect still works.\n\n## Next action\nDo not rerun the blocked GitHub Actions job. First verify whether the billing/spending-limit prerequisite has changed; if unchanged, leave PR #2 safely pending and perform only non-destructive service health readback. When CI/integration becomes available, integrate ff62956 to main, then perform the single post-reboot acceptance check.\n"
    }
  },
  {
    "routing": {
      "project": "95",
      "reason": "blocker subtask inherits explicitly identified parent project",
      "related_projects": [
        "95"
      ]
    },
    "source": {
      "work_item_id": "state:gate:9ad7b5812f954676d1c8",
      "parent_id": "task:CHATGPT-20260925-ADB-KEEPER-LATENCY",
      "kind": "gate",
      "title": "Resolve blocker: GitHub Actions cannot start the deterministic job because of the account billing/spending-limit condition. This is external to the code change.",
      "objective": null,
      "acceptance_json": null,
      "status": "blocked",
      "executor_policy": "auto",
      "sort_order": 1207,
      "current_action": null,
      "next_action": "Restore GitHub Actions billing/runner gate, rerun required CI, then guarded integrate.",
      "blocker": "adb-device-keeper PR #2 remains open with required deterministic CI failed under account billing/spending-limit evidence.",
      "project_id": null,
      "project_name": null,
      "repo": null,
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "task_state",
      "source_ref": "CHATGPT-20260925-ADB-KEEPER-LATENCY.md#blocker",
      "created_at": "2026-09-25T15:54:51Z",
      "updated_at": "2026-09-27T22:23:04.385164Z"
    },
    "work_item_tags": [],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 1187,
        "work_item_id": "state:gate:9ad7b5812f954676d1c8",
        "evidence_kind": "blocked_reconcile",
        "label": "adb-device-keeper PR #2 remains open with required deterministic CI failed under account billing/spending-limit evidence",
        "uri": null,
        "value_json": "\"adb-device-keeper PR #2 remains open with required deterministic CI failed under account billing/spending-limit evidence.\"",
        "created_at": "2026-09-27T22:23:04.385164Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": []
  }
]
```
