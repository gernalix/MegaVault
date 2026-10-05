# Adopt Project Capsule v1 in salute

<!-- migration-1d7ccab218563f69 -->

Migrated project backlog. Project: **salute**; project_id: 84.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 84.

Provenance: `wi:916f47260cbd4be9aaadd2702f98364c`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Adopt Project Capsule v1 in salute

Parent wi:d6185f8fb88d466f907814bf6125890e. MegaVault project_id=84, repository_id=R0084. Add a truthful repository-local Project Capsule v1 based on codex-roadmap/docs/project-capsule after standard PR #2666 merges. Verify project identity and runtime facts from MegaVault; use isolated worktree and repository integration. Preserve active work and data.

Acceptance:

- Root project-capsule.yaml conforms to C2 Project Capsule v1 schema and links essential local documentation without copying global MegaVault/C2 state.
- FAST validation passes against the canonical MegaVault identity, declared paths and freshness after integration.
- FULL safe project verification and appropriate targeted tests pass; risky deployment/device/data operations are documented and gated.
- Integrated repository head and PR/receipt are read back; no terminal PASS from a branch alone.

status: blocked

current_action: BLOCKED

next_action: Restore Actions gate, rerun validate, then guarded integrate.

blocker: salute PR #2 remains open; required validate job failed before source integration.

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "84",
      "reason": "canonical MegaVault project_id",
      "related_projects": [
        "84"
      ]
    },
    "source": {
      "work_item_id": "wi:916f47260cbd4be9aaadd2702f98364c",
      "parent_id": "wi:d6185f8fb88d466f907814bf6125890e",
      "kind": "task",
      "title": "Adopt Project Capsule v1 in salute",
      "objective": "Parent wi:d6185f8fb88d466f907814bf6125890e. MegaVault project_id=84, repository_id=R0084. Add a truthful repository-local Project Capsule v1 based on codex-roadmap/docs/project-capsule after standard PR #2666 merges. Verify project identity and runtime facts from MegaVault; use isolated worktree and repository integration. Preserve active work and data.",
      "acceptance_json": "[\"Root project-capsule.yaml conforms to C2 Project Capsule v1 schema and links essential local documentation without copying global MegaVault/C2 state.\", \"FAST validation passes against the canonical MegaVault identity, declared paths and freshness after integration.\", \"FULL safe project verification and appropriate targeted tests pass; risky deployment/device/data operations are documented and gated.\", \"Integrated repository head and PR/receipt are read back; no terminal PASS from a branch alone.\"]",
      "status": "blocked",
      "executor_policy": "auto",
      "sort_order": null,
      "current_action": "BLOCKED",
      "next_action": "Restore Actions gate, rerun validate, then guarded integrate.",
      "blocker": "salute PR #2 remains open; required validate job failed before source integration.",
      "project_id": "84",
      "project_name": "salute",
      "repo": "https://github.com/gernalix/salute",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-27T19:27:47Z",
      "updated_at": "2026-09-27T22:23:04.779668Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:916f47260cbd4be9aaadd2702f98364c",
        "tag": "project-capsule"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [
      {
        "receipt_id": "work-item:wi:916f47260cbd4be9aaadd2702f98364c:72f4d709e107d2a456e3685b0daf4e78",
        "work_item_id": "wi:916f47260cbd4be9aaadd2702f98364c",
        "run_id": null,
        "prompt_id": null,
        "outcome": "BLOCKED",
        "summary": null,
        "completed_json": "[\"Root project-capsule.yaml conforms to C2 Project Capsule v1 schema and links essential local documentation without copying global MegaVault/C2 state.\", \"FULL safe project verification and appropriate targeted tests pass; risky deployment/device/data operations are documented and gated.\"]",
        "remaining_json": "[\"FAST validation passes against the canonical MegaVault identity, declared paths and freshness after integration.\", \"Integrated repository head and PR/receipt are read back; no terminal PASS from a branch alone.\"]",
        "evidence_json": "[\"Submitted branch head 5253b78dfa2a9ad7afaeabab89cba2e3e7d1956d contains only root project-capsule.yaml and AGENTS.md.\", \"Project Capsule FAST passed against MegaVault project_id=84, R0084 and /home/daniele/projects/salute; schema, declared paths, freshness and change mappings passed.\", \"Project Capsule FULL passed, including the complete synthetic unittest suite; no health database, MinSP export or Workflowy operation was run.\", \"PR #2 CI run 36349472739 failed before the validate job started; GitHub states recent account payments failed or the spending limit needs to be increased.\", \"The same shared GitHub Actions billing blocker was captured in C2 issue #2790; health database authority mismatch separately captured as C2 issue #2803.\"]",
        "blocker": "GitHub Actions account billing or spending-limit state prevents required PR CI from starting, so the PR cannot pass the CI gate or be integrated.",
        "next_action": "After GitHub billing or spending-limit state is resolved, rerun PR #2 checks, wait for single-writer integration, then rerun FAST on the integrated head and read back the merged head before submitting a strict PASS receipt.",
        "strict_contract": 1,
        "payload_sha256": "72f4d709e107d2a456e3685b0daf4e78fc341d9ccac8a2a6ee7f00e5eef5fb9f",
        "captured_at": 1790542269.4661722
      }
    ],
    "work_item_evidence": [
      {
        "evidence_id": 957,
        "work_item_id": "wi:916f47260cbd4be9aaadd2702f98364c",
        "evidence_kind": "executor_result",
        "label": "Submitted branch head 5253b78dfa2a9ad7afaeabab89cba2e3e7d1956d contains only root project-capsule.yaml and AGENTS.md.",
        "uri": null,
        "value_json": "\"Submitted branch head 5253b78dfa2a9ad7afaeabab89cba2e3e7d1956d contains only root project-capsule.yaml and AGENTS.md.\"",
        "created_at": "2026-09-27T20:51:09Z"
      },
      {
        "evidence_id": 958,
        "work_item_id": "wi:916f47260cbd4be9aaadd2702f98364c",
        "evidence_kind": "executor_result",
        "label": "Project Capsule FAST passed against MegaVault project_id=84, R0084 and /home/daniele/projects/salute; schema, declared p",
        "uri": null,
        "value_json": "\"Project Capsule FAST passed against MegaVault project_id=84, R0084 and /home/daniele/projects/salute; schema, declared paths, freshness and change mappings passed.\"",
        "created_at": "2026-09-27T20:51:09Z"
      },
      {
        "evidence_id": 959,
        "work_item_id": "wi:916f47260cbd4be9aaadd2702f98364c",
        "evidence_kind": "executor_result",
        "label": "Project Capsule FULL passed, including the complete synthetic unittest suite; no health database, MinSP export or Workfl",
        "uri": null,
        "value_json": "\"Project Capsule FULL passed, including the complete synthetic unittest suite; no health database, MinSP export or Workflowy operation was run.\"",
        "created_at": "2026-09-27T20:51:09Z"
      },
      {
        "evidence_id": 960,
        "work_item_id": "wi:916f47260cbd4be9aaadd2702f98364c",
        "evidence_kind": "executor_result",
        "label": "PR #2 CI run 36349472739 failed before the validate job started; GitHub states recent account payments failed or the spe",
        "uri": null,
        "value_json": "\"PR #2 CI run 36349472739 failed before the validate job started; GitHub states recent account payments failed or the spending limit needs to be increased.\"",
        "created_at": "2026-09-27T20:51:09Z"
      },
      {
        "evidence_id": 961,
        "work_item_id": "wi:916f47260cbd4be9aaadd2702f98364c",
        "evidence_kind": "executor_result",
        "label": "The same shared GitHub Actions billing blocker was captured in C2 issue #2790; health database authority mismatch separa",
        "uri": null,
        "value_json": "\"The same shared GitHub Actions billing blocker was captured in C2 issue #2790; health database authority mismatch separately captured as C2 issue #2803.\"",
        "created_at": "2026-09-27T20:51:09Z"
      },
      {
        "evidence_id": 1214,
        "work_item_id": "wi:916f47260cbd4be9aaadd2702f98364c",
        "evidence_kind": "blocked_reconcile",
        "label": "salute PR #2 remains open; required validate job failed before source integration.",
        "uri": null,
        "value_json": "\"salute PR #2 remains open; required validate job failed before source integration.\"",
        "created_at": "2026-09-27T22:23:04.779668Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": []
  }
]
```
