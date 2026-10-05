# C3 hardened artifact attestation and verification

<!-- migration-d6f0650b75c63a5a -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:a6ea0904c28a4eb4917f606fe09aa7ac`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### C3 hardened artifact attestation and verification

Replace the fixed escript build-output SHA256 contract in tools/c3_symphony_install.py with a durable host attestation binding the exact source commit, upstream and hardened lock hashes, manifest edits, production audit result, toolchain identity, and actual installed artifact hash. Make the backend verify the artifact against that attestation. Preserve the already-audited 25cdc28... artifact as valid historical gate evidence.

Acceptance:

- The installer records a durable host attestation binding the exact source commit, upstream and hardened lock hashes, manifest edits, production audit result, toolchain identity, and actual installed artifact hash.
- The backend verifies the installed artifact against its host attestation instead of requiring a fixed build-output escript SHA256.
- The already-audited 25cdc28... artifact remains valid historical gate evidence.

status: pending

next_action: Locate the C3 Symphony installer and backend validation paths, then define the attestation format and verification flow.

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
      "work_item_id": "wi:a6ea0904c28a4eb4917f606fe09aa7ac",
      "parent_id": null,
      "kind": "task",
      "title": "C3 hardened artifact attestation and verification",
      "objective": "Replace the fixed escript build-output SHA256 contract in tools/c3_symphony_install.py with a durable host attestation binding the exact source commit, upstream and hardened lock hashes, manifest edits, production audit result, toolchain identity, and actual installed artifact hash. Make the backend verify the artifact against that attestation. Preserve the already-audited 25cdc28... artifact as valid historical gate evidence.",
      "acceptance_json": "[\"The installer records a durable host attestation binding the exact source commit, upstream and hardened lock hashes, manifest edits, production audit result, toolchain identity, and actual installed artifact hash.\", \"The backend verifies the installed artifact against its host attestation instead of requiring a fixed build-output escript SHA256.\", \"The already-audited 25cdc28... artifact remains valid historical gate evidence.\"]",
      "status": "pending",
      "executor_policy": "auto",
      "sort_order": null,
      "current_action": null,
      "next_action": "Locate the C3 Symphony installer and backend validation paths, then define the attestation format and verification flow.",
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
      "created_at": "2026-09-30T14:43:18Z",
      "updated_at": "2026-09-30T14:43:18Z"
    },
    "work_item_tags": [],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2414,
        "work_item_id": "wi:a6ea0904c28a4eb4917f606fe09aa7ac",
        "evidence_kind": "issue_inbox",
        "label": "issue:d6d74401e96a40d6b1fbfda91bbfd896",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"C3 hardened artifact reproducibility gap: tools/c3_symphony_install.py requires one fixed escript SHA256, but rebuilding the exact pinned source + hardened lock + Elixir 1.19.5/OTP 28 produced a different escript hash while mix hex.audit/build succeeded. The escript ZIP embeds build metadata/path/timestamps, so whole-file SHA is not a stable reproducibility proof. Replace the static build-output hash contract with a durable host attestation binding exact source commit, upstream/hardened lock hashes, manifest edits, production audit result, toolchain identity and the actual installed artifact hash; backend verifies artifact against that attestation. Preserve the already-audited 25cdc28... artifact as valid historical gate evidence.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:d6d74401e96a40d6b1fbfda91bbfd896\", \"observed_at_ms\": 1790778922422, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T14:43:18Z"
      },
      {
        "evidence_id": 2500,
        "work_item_id": "wi:a6ea0904c28a4eb4917f606fe09aa7ac",
        "evidence_kind": "issue_inbox",
        "label": "issue:0bdef37e0b174a9aa6bb63ae44ae991f",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"C3/Symphony production handoff bug observed on run 0631347889c542d7b58294a5d73ee3a9: tracker issue gernalix/c3-symphony#2 closed PASS with committed task head 865e2353b8f491c93371647522be9d7c258f9253, then Symphony terminal cleanup deleted workspace GH-2 before c3_symphony_route.import_workspace_commit could fetch that commit into canonical worktree task/633902. Subsequent C2 recovery loops fail with symphony_workspace_import_missing and repeatedly relaunch the same stale run while Symphony itself has zero running/retrying/blocked agents. Production route must preserve/export the terminal commit before workspace cleanup, or otherwise make terminal artifact transfer durable/idempotent so C2 finalization cannot lose a successful task commit.\\n\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:0bdef37e0b174a9aa6bb63ae44ae991f\", \"observed_at_ms\": 1790787949105, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-10-01T12:32:14Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:d6d74401e96a40d6b1fbfda91bbfd896",
        "work_item_id": "wi:a6ea0904c28a4eb4917f606fe09aa7ac",
        "role": "decision",
        "created_at": "2026-09-30T14:43:18Z"
      },
      {
        "issue_id": "issue:0bdef37e0b174a9aa6bb63ae44ae991f",
        "work_item_id": "wi:a6ea0904c28a4eb4917f606fe09aa7ac",
        "role": "decision",
        "created_at": "2026-10-01T12:32:14Z"
      },
      {
        "issue_id": "issue:0bdef37e0b174a9aa6bb63ae44ae991f",
        "work_item_id": "wi:a6ea0904c28a4eb4917f606fe09aa7ac",
        "role": "matched",
        "created_at": "2026-10-01T12:32:14Z"
      }
    ]
  }
]
```
