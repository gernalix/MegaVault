# Adopt Project Capsule v1 in datasette5

<!-- migration-8ee178bbeadf81bf -->

Migrated project backlog. Project: **datasette5**; project_id: 10.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 10.

Provenance: `wi:abf635b09b6f4defbcdd1d25392028c3`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Adopt Project Capsule v1 in datasette5

Parent wi:d6185f8fb88d466f907814bf6125890e. MegaVault project_id=10, repository_id=R0010. Add a truthful repository-local Project Capsule v1 based on codex-roadmap/docs/project-capsule after standard PR #2666 merges. Verify project identity and runtime facts from MegaVault; use isolated worktree and repository integration. Preserve active work and data.

Acceptance:

- Root project-capsule.yaml conforms to C2 Project Capsule v1 schema and links essential local documentation without copying global MegaVault/C2 state.
- FAST validation passes against the canonical MegaVault identity, declared paths and freshness after integration.
- FULL safe project verification and appropriate targeted tests pass; risky deployment/device/data operations are documented and gated.
- Integrated repository head and PR/receipt are read back; no terminal PASS from a branch alone.

status: blocked

current_action: Capsule is authored and locally validated, but required PR CI did not start its job steps, so guarded integration cannot proceed.

next_action: Restore runner/account CI and rerun required test before integration.

blocker: datasette5 PR #2 remains open; required GitHub Actions test failed before any steps with unavailable logs.

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "10",
      "reason": "canonical MegaVault project_id",
      "related_projects": [
        "10"
      ]
    },
    "source": {
      "work_item_id": "wi:abf635b09b6f4defbcdd1d25392028c3",
      "parent_id": "wi:d6185f8fb88d466f907814bf6125890e",
      "kind": "task",
      "title": "Adopt Project Capsule v1 in datasette5",
      "objective": "Parent wi:d6185f8fb88d466f907814bf6125890e. MegaVault project_id=10, repository_id=R0010. Add a truthful repository-local Project Capsule v1 based on codex-roadmap/docs/project-capsule after standard PR #2666 merges. Verify project identity and runtime facts from MegaVault; use isolated worktree and repository integration. Preserve active work and data.",
      "acceptance_json": "[\"Root project-capsule.yaml conforms to C2 Project Capsule v1 schema and links essential local documentation without copying global MegaVault/C2 state.\", \"FAST validation passes against the canonical MegaVault identity, declared paths and freshness after integration.\", \"FULL safe project verification and appropriate targeted tests pass; risky deployment/device/data operations are documented and gated.\", \"Integrated repository head and PR/receipt are read back; no terminal PASS from a branch alone.\"]",
      "status": "blocked",
      "executor_policy": "auto",
      "sort_order": null,
      "current_action": "Capsule is authored and locally validated, but required PR CI did not start its job steps, so guarded integration cannot proceed.",
      "next_action": "Restore runner/account CI and rerun required test before integration.",
      "blocker": "datasette5 PR #2 remains open; required GitHub Actions test failed before any steps with unavailable logs.",
      "project_id": "10",
      "project_name": "datasette5",
      "repo": "https://github.com/gernalix/datasette5",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-27T19:27:47Z",
      "updated_at": "2026-09-27T22:23:04.972538Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:abf635b09b6f4defbcdd1d25392028c3",
        "tag": "project-capsule"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [
      {
        "receipt_id": "work-item:wi:abf635b09b6f4defbcdd1d25392028c3:774f7b41404622b17acbb5e726357feb",
        "work_item_id": "wi:abf635b09b6f4defbcdd1d25392028c3",
        "run_id": null,
        "prompt_id": null,
        "outcome": "BLOCKED",
        "summary": "Capsule is authored and locally validated, but required PR CI did not start its job steps, so guarded integration cannot proceed.",
        "completed_json": "[\"Added the repository-root Project Capsule v1 manifest with MegaVault identity 10/R0010, source-backed paths and commands, host-local data boundaries, and freshness at the reviewed main commit.\", \"FAST validator passed against MegaVault identity and the changed manifest.\", \"FULL validator passed its safe targeted file-browser verification hook; the targeted file-browser suite passed 3 tests.\", \"Opened PR #2 through repo_single_writer; branch head is f482c524942b43e4f356c8878b91bd81295eb26a on base 51e3106a35a98816593994510919239b644af462.\"]",
        "remaining_json": "[\"Resolve the GitHub Actions test-job initialization failure or obtain actionable authorized runner evidence, then rerun required PR checks.\", \"After checks pass, let the canonical single-writer integrator merge; verify the exact integrated main head and rerun FAST/FULL targeted validation on that head before terminal PASS.\"]",
        "evidence_json": "[\"PR https://github.com/gernalix/datasette5/pull/2 remains OPEN with head f482c524942b43e4f356c8878b91bd81295eb26a and base 51e3106a35a98816593994510919239b644af462.\", \"Required CI run 36353187571 / job 108715667329 concluded FAILURE at 2026-09-27T21:50:35Z; job JSON contains steps=[] and no log is available (`gh run view --log-failed` returned `log not found: 108715667329`). PR mergeStateStatus is UNSTABLE.\", \"GitGuardian Security Checks passed.\", \"Local FAST and FULL capsule validation passed; safe file-browser unittest passed 3/3.\", \"The full local unittest suite could not complete in the current checkout environment: external canonical schema fixture is absent and installed pydantic/pydantic-core versions conflict; issue capture #3061 was queued separately.\"]",
        "blocker": "Required GitHub Actions CI job failed before any steps ran and the runner log is unavailable, leaving PR #2 unmergeable under required checks. No code-level CI failure evidence is available.",
        "next_action": "Ask the authorized CI owner to resolve the job-initialization failure or provide actionable runner evidence, rerun PR #2 checks, then resume guarded integration and post-integration validation.",
        "strict_contract": 1,
        "payload_sha256": "774f7b41404622b17acbb5e726357feb55bbc56808d202d4c04affa023067aaa",
        "captured_at": 1790546007.0803232
      }
    ],
    "work_item_evidence": [
      {
        "evidence_id": 1142,
        "work_item_id": "wi:abf635b09b6f4defbcdd1d25392028c3",
        "evidence_kind": "issue_inbox",
        "label": "issue:997b758be33649eca16e06b3239e1db9",
        "uri": "codex://threads/01a0e46f-c785-7153-af83-ad925b812c28",
        "value_json": "{\"chat_url\": \"codex://threads/01a0e46f-c785-7153-af83-ad925b812c28\", \"code_location\": null, \"description\": \"datasette5 full unittest suite is blocked in this checkout: test_personalhub_labels requires a canonical Room schema file that is absent, and importing test_personalhub_projection/test_personalhub_replica fails because installed pydantic and pydantic-core versions are incompatible; test_runtime deployment coverage also imports the failing module. This prevents full suite validation without the external schema and a compatible Datasette environment.\", \"executor\": null, \"executor_ref\": \"01a0e46f-c785-7153-af83-ad925b812c28\", \"issue_id\": \"issue:997b758be33649eca16e06b3239e1db9\", \"observed_at_ms\": 1790545792404, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-27T21:51:59Z"
      },
      {
        "evidence_id": 1144,
        "work_item_id": "wi:abf635b09b6f4defbcdd1d25392028c3",
        "evidence_kind": "executor_result",
        "label": "PR https://github.com/gernalix/datasette5/pull/2 remains OPEN with head f482c524942b43e4f356c8878b91bd81295eb26a and bas",
        "uri": null,
        "value_json": "\"PR https://github.com/gernalix/datasette5/pull/2 remains OPEN with head f482c524942b43e4f356c8878b91bd81295eb26a and base 51e3106a35a98816593994510919239b644af462.\"",
        "created_at": "2026-09-27T21:53:27Z"
      },
      {
        "evidence_id": 1145,
        "work_item_id": "wi:abf635b09b6f4defbcdd1d25392028c3",
        "evidence_kind": "executor_result",
        "label": "Required CI run 36353187571 / job 108715667329 concluded FAILURE at 2026-09-27T21:50:35Z; job JSON contains steps=[] and",
        "uri": null,
        "value_json": "\"Required CI run 36353187571 / job 108715667329 concluded FAILURE at 2026-09-27T21:50:35Z; job JSON contains steps=[] and no log is available (`gh run view --log-failed` returned `log not found: 108715667329`). PR mergeStateStatus is UNSTABLE.\"",
        "created_at": "2026-09-27T21:53:27Z"
      },
      {
        "evidence_id": 1146,
        "work_item_id": "wi:abf635b09b6f4defbcdd1d25392028c3",
        "evidence_kind": "executor_result",
        "label": "GitGuardian Security Checks passed.",
        "uri": null,
        "value_json": "\"GitGuardian Security Checks passed.\"",
        "created_at": "2026-09-27T21:53:27Z"
      },
      {
        "evidence_id": 1147,
        "work_item_id": "wi:abf635b09b6f4defbcdd1d25392028c3",
        "evidence_kind": "executor_result",
        "label": "Local FAST and FULL capsule validation passed; safe file-browser unittest passed 3/3.",
        "uri": null,
        "value_json": "\"Local FAST and FULL capsule validation passed; safe file-browser unittest passed 3/3.\"",
        "created_at": "2026-09-27T21:53:27Z"
      },
      {
        "evidence_id": 1148,
        "work_item_id": "wi:abf635b09b6f4defbcdd1d25392028c3",
        "evidence_kind": "executor_result",
        "label": "The full local unittest suite could not complete in the current checkout environment: external canonical schema fixture ",
        "uri": null,
        "value_json": "\"The full local unittest suite could not complete in the current checkout environment: external canonical schema fixture is absent and installed pydantic/pydantic-core versions conflict; issue capture #3061 was queued separately.\"",
        "created_at": "2026-09-27T21:53:27Z"
      },
      {
        "evidence_id": 1223,
        "work_item_id": "wi:abf635b09b6f4defbcdd1d25392028c3",
        "evidence_kind": "blocked_reconcile",
        "label": "datasette5 PR #2 remains open; required GitHub Actions test failed before any steps with unavailable logs.",
        "uri": null,
        "value_json": "\"datasette5 PR #2 remains open; required GitHub Actions test failed before any steps with unavailable logs.\"",
        "created_at": "2026-09-27T22:23:04.972538Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:997b758be33649eca16e06b3239e1db9",
        "work_item_id": "wi:abf635b09b6f4defbcdd1d25392028c3",
        "role": "matched",
        "created_at": "2026-09-27T21:49:52Z"
      },
      {
        "issue_id": "issue:997b758be33649eca16e06b3239e1db9",
        "work_item_id": "wi:abf635b09b6f4defbcdd1d25392028c3",
        "role": "decision",
        "created_at": "2026-09-27T21:49:52Z"
      }
    ]
  }
]
```
