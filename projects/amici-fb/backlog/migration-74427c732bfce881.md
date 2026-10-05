# Adopt Project Capsule v1 in amici-fb

<!-- migration-74427c732bfce881 -->

Migrated project backlog. Project: **amici-fb**; project_id: 1.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 1.

Provenance: `wi:621af0a298134a7f8819f2e9341bebee`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Adopt Project Capsule v1 in amici-fb

Parent wi:d6185f8fb88d466f907814bf6125890e. MegaVault project_id=1, repository_id=R0001. Add a truthful repository-local Project Capsule v1 based on codex-roadmap/docs/project-capsule after standard PR #2666 merges. Verify project identity and runtime facts from MegaVault; use isolated worktree and repository integration. Preserve active work and data.

Acceptance:

- Root project-capsule.yaml conforms to C2 Project Capsule v1 schema and links essential local documentation without copying global MegaVault/C2 state.
- FAST validation passes against the canonical MegaVault identity, declared paths and freshness after integration.
- FULL safe project verification and appropriate targeted tests pass; risky deployment/device/data operations are documented and gated.
- Integrated repository head and PR/receipt are read back; no terminal PASS from a branch alone.

status: blocked

current_action: BLOCKED

next_action: Restore Actions account gate, rerun checks, then guarded integrate.

blocker: amici_fb PR #1 remains open; required CI job failed under GitHub billing/spending limit.

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "1",
      "reason": "canonical MegaVault project_id",
      "related_projects": [
        "1"
      ]
    },
    "source": {
      "work_item_id": "wi:621af0a298134a7f8819f2e9341bebee",
      "parent_id": "wi:d6185f8fb88d466f907814bf6125890e",
      "kind": "task",
      "title": "Adopt Project Capsule v1 in amici-fb",
      "objective": "Parent wi:d6185f8fb88d466f907814bf6125890e. MegaVault project_id=1, repository_id=R0001. Add a truthful repository-local Project Capsule v1 based on codex-roadmap/docs/project-capsule after standard PR #2666 merges. Verify project identity and runtime facts from MegaVault; use isolated worktree and repository integration. Preserve active work and data.",
      "acceptance_json": "[\"Root project-capsule.yaml conforms to C2 Project Capsule v1 schema and links essential local documentation without copying global MegaVault/C2 state.\", \"FAST validation passes against the canonical MegaVault identity, declared paths and freshness after integration.\", \"FULL safe project verification and appropriate targeted tests pass; risky deployment/device/data operations are documented and gated.\", \"Integrated repository head and PR/receipt are read back; no terminal PASS from a branch alone.\"]",
      "status": "blocked",
      "executor_policy": "auto",
      "sort_order": null,
      "current_action": "BLOCKED",
      "next_action": "Restore Actions account gate, rerun checks, then guarded integrate.",
      "blocker": "amici_fb PR #1 remains open; required CI job failed under GitHub billing/spending limit.",
      "project_id": "1",
      "project_name": "amici-fb",
      "repo": "https://github.com/gernalix/amici_fb",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-27T19:27:47Z",
      "updated_at": "2026-09-27T22:23:04.779359Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:621af0a298134a7f8819f2e9341bebee",
        "tag": "project-capsule"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [
      {
        "receipt_id": "work-item:wi:621af0a298134a7f8819f2e9341bebee:8148713729394128c65c341ce99a81cd",
        "work_item_id": "wi:621af0a298134a7f8819f2e9341bebee",
        "run_id": null,
        "prompt_id": null,
        "outcome": "BLOCKED",
        "summary": null,
        "completed_json": "[]",
        "remaining_json": "[\"Root project-capsule.yaml conforms to C2 Project Capsule v1 schema and links essential local documentation without copying global MegaVault/C2 state.\", \"FAST validation passes against the canonical MegaVault identity, declared paths and freshness after integration.\", \"FULL safe project verification and appropriate targeted tests pass; risky deployment/device/data operations are documented and gated.\", \"Integrated repository head and PR/receipt are read back; no terminal PASS from a branch alone.\"]",
        "evidence_json": "[\"Submitted branch head 1dfabfcf80939b8440248cf71031276460775ab1 with root project-capsule.yaml and AGENTS.md in isolated single-writer task worktree.\", \"Project Capsule FAST and FULL checks pass in the registered task worktree, including MegaVault identity/workdir validation, schema/path/freshness checks and the complete unittest suite.\", \"PR #1 CI run 36348913387 failed before starting tests; GitHub annotation states the job was not started because recent account payments failed or the spending limit needs to be increased.\", \"C2 issue capture issue:f045de168ccc43779cd68e950317340f was submitted as Issue #2790.\"]",
        "blocker": "GitHub Actions billing or spending-limit state prevents required CI from starting, so the PR cannot pass the required CI gate or be integrated.",
        "next_action": "After GitHub billing or spending-limit state is resolved, rerun PR #1 checks, wait for single-writer integration, read back merged head, rerun FAST/FULL on the integrated head, then submit a strict PASS receipt.",
        "strict_contract": 1,
        "payload_sha256": "8148713729394128c65c341ce99a81cd52fbdd7141bf516b0fc20cef0d5bbd2f",
        "captured_at": 1790541788.3627489
      }
    ],
    "work_item_evidence": [
      {
        "evidence_id": 937,
        "work_item_id": "wi:621af0a298134a7f8819f2e9341bebee",
        "evidence_kind": "executor_result",
        "label": "Submitted branch head 1dfabfcf80939b8440248cf71031276460775ab1 with root project-capsule.yaml and AGENTS.md in isolated ",
        "uri": null,
        "value_json": "\"Submitted branch head 1dfabfcf80939b8440248cf71031276460775ab1 with root project-capsule.yaml and AGENTS.md in isolated single-writer task worktree.\"",
        "created_at": "2026-09-27T20:43:08Z"
      },
      {
        "evidence_id": 938,
        "work_item_id": "wi:621af0a298134a7f8819f2e9341bebee",
        "evidence_kind": "executor_result",
        "label": "Project Capsule FAST and FULL checks pass in the registered task worktree, including MegaVault identity/workdir validati",
        "uri": null,
        "value_json": "\"Project Capsule FAST and FULL checks pass in the registered task worktree, including MegaVault identity/workdir validation, schema/path/freshness checks and the complete unittest suite.\"",
        "created_at": "2026-09-27T20:43:08Z"
      },
      {
        "evidence_id": 939,
        "work_item_id": "wi:621af0a298134a7f8819f2e9341bebee",
        "evidence_kind": "executor_result",
        "label": "PR #1 CI run 36348913387 failed before starting tests; GitHub annotation states the job was not started because recent a",
        "uri": null,
        "value_json": "\"PR #1 CI run 36348913387 failed before starting tests; GitHub annotation states the job was not started because recent account payments failed or the spending limit needs to be increased.\"",
        "created_at": "2026-09-27T20:43:08Z"
      },
      {
        "evidence_id": 940,
        "work_item_id": "wi:621af0a298134a7f8819f2e9341bebee",
        "evidence_kind": "executor_result",
        "label": "C2 issue capture issue:f045de168ccc43779cd68e950317340f was submitted as Issue #2790.",
        "uri": null,
        "value_json": "\"C2 issue capture issue:f045de168ccc43779cd68e950317340f was submitted as Issue #2790.\"",
        "created_at": "2026-09-27T20:43:08Z"
      },
      {
        "evidence_id": 1058,
        "work_item_id": "wi:621af0a298134a7f8819f2e9341bebee",
        "evidence_kind": "issue_inbox",
        "label": "issue:f045de168ccc43779cd68e950317340f",
        "uri": "codex://threads/01a0e494-b045-7ce3-ad31-4f5b627f3471",
        "value_json": "{\"chat_url\": \"codex://threads/01a0e494-b045-7ce3-ad31-4f5b627f3471\", \"code_location\": \"PR #1 CI run 36348913387\", \"description\": \"GitHub Actions CI for amici-fb PR #1 cannot start because the account reports recent payments failed or spending limit needs increase; PR check is failure before test execution, so serialized integration cannot proceed until GitHub billing is resolved.\", \"executor\": \"codex\", \"executor_ref\": \"01a0e494-b045-7ce3-ad31-4f5b627f3471\", \"issue_id\": \"issue:f045de168ccc43779cd68e950317340f\", \"observed_at_ms\": 1790541756600, \"origin_run_id\": null, \"origin_work_item_id\": \"wi:621af0a298134a7f8819f2e9341bebee\", \"repo\": \"gernalix/amici_fb\"}",
        "created_at": "2026-09-27T21:12:21Z"
      },
      {
        "evidence_id": 1213,
        "work_item_id": "wi:621af0a298134a7f8819f2e9341bebee",
        "evidence_kind": "blocked_reconcile",
        "label": "amici_fb PR #1 remains open; required CI job failed under GitHub billing/spending limit.",
        "uri": null,
        "value_json": "\"amici_fb PR #1 remains open; required CI job failed under GitHub billing/spending limit.\"",
        "created_at": "2026-09-27T22:23:04.779359Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:f045de168ccc43779cd68e950317340f",
        "work_item_id": "wi:621af0a298134a7f8819f2e9341bebee",
        "role": "matched",
        "created_at": "2026-09-27T20:42:36Z"
      },
      {
        "issue_id": "issue:f045de168ccc43779cd68e950317340f",
        "work_item_id": "wi:621af0a298134a7f8819f2e9341bebee",
        "role": "decision",
        "created_at": "2026-09-27T20:42:36Z"
      }
    ]
  }
]
```
