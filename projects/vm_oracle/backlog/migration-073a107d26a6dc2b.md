# Adopt Project Capsule v1 in vm_oracle

<!-- migration-073a107d26a6dc2b -->

Migrated project backlog. Project: **vm_oracle**; project_id: 43.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 43.

Provenance: `wi:1286360980cf462689f46cfcaf5d3e5d`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Adopt Project Capsule v1 in vm_oracle

Parent wi:d6185f8fb88d466f907814bf6125890e. MegaVault project_id=43, repository_id=R0043. Add a truthful repository-local Project Capsule v1 based on codex-roadmap/docs/project-capsule after standard PR #2666 merges. Verify project identity and runtime facts from MegaVault; use isolated worktree and repository integration. Preserve active work and data.

Acceptance:

- Root project-capsule.yaml conforms to C2 Project Capsule v1 schema and links essential local documentation without copying global MegaVault/C2 state.
- FAST validation passes against the canonical MegaVault identity, declared paths and freshness after integration.
- FULL safe project verification and appropriate targeted tests pass; risky deployment/device/data operations are documented and gated.
- Integrated repository head and PR/receipt are read back; no terminal PASS from a branch alone.

status: blocked

current_action: Capsule content and local validation are ready in PR #1; remote CI is blocked by GitHub Actions billing, so the PR and worktree are preserved without merging.

next_action: Restore account CI and integrate the exact tested PR after green checks.

blocker: vm_oracle PR #1 remains open; required GitHub Actions test is failed before source integration.

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "43",
      "reason": "canonical MegaVault project_id",
      "related_projects": [
        "43"
      ]
    },
    "source": {
      "work_item_id": "wi:1286360980cf462689f46cfcaf5d3e5d",
      "parent_id": "wi:d6185f8fb88d466f907814bf6125890e",
      "kind": "task",
      "title": "Adopt Project Capsule v1 in vm_oracle",
      "objective": "Parent wi:d6185f8fb88d466f907814bf6125890e. MegaVault project_id=43, repository_id=R0043. Add a truthful repository-local Project Capsule v1 based on codex-roadmap/docs/project-capsule after standard PR #2666 merges. Verify project identity and runtime facts from MegaVault; use isolated worktree and repository integration. Preserve active work and data.",
      "acceptance_json": "[\"Root project-capsule.yaml conforms to C2 Project Capsule v1 schema and links essential local documentation without copying global MegaVault/C2 state.\", \"FAST validation passes against the canonical MegaVault identity, declared paths and freshness after integration.\", \"FULL safe project verification and appropriate targeted tests pass; risky deployment/device/data operations are documented and gated.\", \"Integrated repository head and PR/receipt are read back; no terminal PASS from a branch alone.\"]",
      "status": "blocked",
      "executor_policy": "auto",
      "sort_order": null,
      "current_action": "Capsule content and local validation are ready in PR #1; remote CI is blocked by GitHub Actions billing, so the PR and worktree are preserved without merging.",
      "next_action": "Restore account CI and integrate the exact tested PR after green checks.",
      "blocker": "vm_oracle PR #1 remains open; required GitHub Actions test is failed before source integration.",
      "project_id": "43",
      "project_name": "vm_oracle",
      "repo": "https://github.com/gernalix/vm_oracle",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-27T19:27:47Z",
      "updated_at": "2026-09-27T22:23:04.778383Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:1286360980cf462689f46cfcaf5d3e5d",
        "tag": "project-capsule"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [
      {
        "receipt_id": "work-item:wi:1286360980cf462689f46cfcaf5d3e5d:ed8686e2527ed8de49fdc72d06716ed0",
        "work_item_id": "wi:1286360980cf462689f46cfcaf5d3e5d",
        "run_id": null,
        "prompt_id": null,
        "outcome": "BLOCKED",
        "summary": "Capsule content and local validation are ready in PR #1; remote CI is blocked by GitHub Actions billing, so the PR and worktree are preserved without merging.",
        "completed_json": "[\"Authored AGENTS.md and project-capsule.yaml in the isolated vm_oracle worktree; local FAST/FULL checks and targeted tests pass.\", \"Opened PR #1 and verified GitGuardian Security Checks pass; the repository integrator has not merged the PR.\"]",
        "remaining_json": "[\"Root project-capsule.yaml conforms to C2 Project Capsule v1 schema and links essential local documentation without copying global MegaVault/C2 state.\", \"FAST validation passes against the canonical MegaVault identity, declared paths and freshness after integration.\", \"FULL safe project verification and appropriate targeted tests pass; risky deployment/device/data operations are documented and gated.\", \"Integrated repository head and PR/receipt are read back; no terminal PASS from a branch alone.\"]",
        "evidence_json": "[\"PR https://github.com/gernalix/vm_oracle/pull/1 is OPEN on task/wi-1286360980cf462689f46cfcaf5d3e5d at head 9b82d8c1879593c7cb5ae9f82a4ca89a1c0b6700; repo-task status-any reports integration_state=queued.\", \"GitGuardian Security Checks pass. The CI test check failed before a runner started: runner_id=0, steps=[], and annotation says the job was not started because recent account payments failed or the spending limit needs increase.\", \"The same pre-runner GitHub Actions billing annotation appears on prior main run 35998407898 from 2026-09-24, before the capsule changes.\", \"Local Project Capsule FAST and FULL passed with MegaVault project_id=43, repository_id=R0043, canonical workdir, paths, commands, and freshness verified.\", \"Targeted test_configure_datasette_edge.py passed 2 tests and test_oracle_backup_alert_gate.py passed 3 tests; FULL safe unit-test and mocked SSH helper hooks both exited 0.\"]",
        "blocker": "GitHub Actions account billing or spending-limit state prevents the required CI job from starting, so PR #1 cannot meet the remote integration gate.",
        "next_action": "After GitHub Actions billing/spending-limit state is restored, rerun PR #1 CI and let repo-integrator merge; then fast-forward canonical main and rerun FAST before submitting PASS.",
        "strict_contract": 1,
        "payload_sha256": "ed8686e2527ed8de49fdc72d06716ed05434494397e0fc8269c5b9085c4e7eea",
        "captured_at": 1790540206.8866353
      }
    ],
    "work_item_evidence": [
      {
        "evidence_id": 881,
        "work_item_id": "wi:1286360980cf462689f46cfcaf5d3e5d",
        "evidence_kind": "executor_result",
        "label": "PR https://github.com/gernalix/vm_oracle/pull/1 is OPEN on task/wi-1286360980cf462689f46cfcaf5d3e5d at head 9b82d8c18795",
        "uri": null,
        "value_json": "\"PR https://github.com/gernalix/vm_oracle/pull/1 is OPEN on task/wi-1286360980cf462689f46cfcaf5d3e5d at head 9b82d8c1879593c7cb5ae9f82a4ca89a1c0b6700; repo-task status-any reports integration_state=queued.\"",
        "created_at": "2026-09-27T20:16:46Z"
      },
      {
        "evidence_id": 882,
        "work_item_id": "wi:1286360980cf462689f46cfcaf5d3e5d",
        "evidence_kind": "executor_result",
        "label": "GitGuardian Security Checks pass. The CI test check failed before a runner started: runner_id=0, steps=[], and annotatio",
        "uri": null,
        "value_json": "\"GitGuardian Security Checks pass. The CI test check failed before a runner started: runner_id=0, steps=[], and annotation says the job was not started because recent account payments failed or the spending limit needs increase.\"",
        "created_at": "2026-09-27T20:16:46Z"
      },
      {
        "evidence_id": 883,
        "work_item_id": "wi:1286360980cf462689f46cfcaf5d3e5d",
        "evidence_kind": "executor_result",
        "label": "The same pre-runner GitHub Actions billing annotation appears on prior main run 35998407898 from 2026-09-24, before the ",
        "uri": null,
        "value_json": "\"The same pre-runner GitHub Actions billing annotation appears on prior main run 35998407898 from 2026-09-24, before the capsule changes.\"",
        "created_at": "2026-09-27T20:16:46Z"
      },
      {
        "evidence_id": 884,
        "work_item_id": "wi:1286360980cf462689f46cfcaf5d3e5d",
        "evidence_kind": "executor_result",
        "label": "Local Project Capsule FAST and FULL passed with MegaVault project_id=43, repository_id=R0043, canonical workdir, paths, ",
        "uri": null,
        "value_json": "\"Local Project Capsule FAST and FULL passed with MegaVault project_id=43, repository_id=R0043, canonical workdir, paths, commands, and freshness verified.\"",
        "created_at": "2026-09-27T20:16:46Z"
      },
      {
        "evidence_id": 885,
        "work_item_id": "wi:1286360980cf462689f46cfcaf5d3e5d",
        "evidence_kind": "executor_result",
        "label": "Targeted test_configure_datasette_edge.py passed 2 tests and test_oracle_backup_alert_gate.py passed 3 tests; FULL safe ",
        "uri": null,
        "value_json": "\"Targeted test_configure_datasette_edge.py passed 2 tests and test_oracle_backup_alert_gate.py passed 3 tests; FULL safe unit-test and mocked SSH helper hooks both exited 0.\"",
        "created_at": "2026-09-27T20:16:46Z"
      },
      {
        "evidence_id": 1210,
        "work_item_id": "wi:1286360980cf462689f46cfcaf5d3e5d",
        "evidence_kind": "blocked_reconcile",
        "label": "vm_oracle PR #1 remains open; required GitHub Actions test is failed before source integration.",
        "uri": null,
        "value_json": "\"vm_oracle PR #1 remains open; required GitHub Actions test is failed before source integration.\"",
        "created_at": "2026-09-27T22:23:04.778383Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": []
  }
]
```
