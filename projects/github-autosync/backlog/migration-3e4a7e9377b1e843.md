# Sanare tutti i repo/worktree sporchi e prevenire ricorrenza

<!-- migration-3e4a7e9377b1e843 -->

Migrated project backlog. Project: **github-autosync**; project_id: 92.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 49, 51, 92.

Provenance: `wi:d08356a155404433bbea2f6700287927`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Sanare tutti i repo/worktree sporchi e prevenire ricorrenza

Sanare TUTTI i repository e worktree sporchi rilevabili nell’ambiente C2/PersonalHub e negli altri repo gestiti, senza perdere lavoro valido: classificare ogni dirty state (modifiche intenzionali/non committate, artefatti generati, merge/rebase/stash residui, file untracked, branch/worktree operativi), portare ogni repo a uno stato coerente e pushato quando appropriato, e verificare che non restino dirty worktree che possano bloccare autosync, scheduler, executor o recovery. Inoltre implementare, se tecnicamente sensato, un fix sistemico che prevenga la ricorrenza: rilevazione/preflight automatica del dirty state, cleanup sicuro degli artefatti generati, isolamento corretto dei worktree/executor, checkpoint commit+push e recovery/fail-closed invece di accumulare modifiche locali. Il risultato deve coprire tutti i repo/worktree interessati, non solo quelli già noti.

status: blocked

current_action: Operational C2 worktree sanitation and recurrence guards are integrated; remaining historical dirty worktrees require their owning repository/task dispositions.

next_action: When an owning repository task integrates or an owner provides explicit retirement evidence, recheck only its preserved worktree, checkpoint unique changes, then clean it safely; repeat for the remaining named owners and only then reconsider d083 completion and dad7 branch convergence.

blocker: Remaining dirty trees contain unique historical code, task data, or owner-specific staged/untracked changes; no safe global cleanup or branch deletion is justified until those owners integrate or explicitly retire their work. No current installed C2 canonical/runtime dirt blocks execution.

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "92",
      "reason": "semantic correction of source routing; original identity preserved",
      "related_projects": [
        "92",
        "49",
        "51"
      ]
    },
    "source": {
      "work_item_id": "wi:d08356a155404433bbea2f6700287927",
      "parent_id": null,
      "kind": "task",
      "title": "Sanare tutti i repo/worktree sporchi e prevenire ricorrenza",
      "objective": "Sanare TUTTI i repository e worktree sporchi rilevabili nell’ambiente C2/PersonalHub e negli altri repo gestiti, senza perdere lavoro valido: classificare ogni dirty state (modifiche intenzionali/non committate, artefatti generati, merge/rebase/stash residui, file untracked, branch/worktree operativi), portare ogni repo a uno stato coerente e pushato quando appropriato, e verificare che non restino dirty worktree che possano bloccare autosync, scheduler, executor o recovery. Inoltre implementare, se tecnicamente sensato, un fix sistemico che prevenga la ricorrenza: rilevazione/preflight automatica del dirty state, cleanup sicuro degli artefatti generati, isolamento corretto dei worktree/executor, checkpoint commit+push e recovery/fail-closed invece di accumulare modifiche locali. Il risultato deve coprire tutti i repo/worktree interessati, non solo quelli già noti.",
      "acceptance_json": "[]",
      "status": "blocked",
      "executor_policy": "auto",
      "sort_order": null,
      "current_action": "Operational C2 worktree sanitation and recurrence guards are integrated; remaining historical dirty worktrees require their owning repository/task dispositions.",
      "next_action": "When an owning repository task integrates or an owner provides explicit retirement evidence, recheck only its preserved worktree, checkpoint unique changes, then clean it safely; repeat for the remaining named owners and only then reconsider d083 completion and dad7 branch convergence.",
      "blocker": "Remaining dirty trees contain unique historical code, task data, or owner-specific staged/untracked changes; no safe global cleanup or branch deletion is justified until those owners integrate or explicitly retire their work. No current installed C2 canonical/runtime dirt blocks execution.",
      "project_id": null,
      "project_name": null,
      "repo": null,
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-27T00:50:41Z",
      "updated_at": "2026-09-27T00:50:41Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:d08356a155404433bbea2f6700287927",
        "tag": "c2"
      },
      {
        "work_item_id": "wi:d08356a155404433bbea2f6700287927",
        "tag": "git"
      },
      {
        "work_item_id": "wi:d08356a155404433bbea2f6700287927",
        "tag": "maintenance"
      },
      {
        "work_item_id": "wi:d08356a155404433bbea2f6700287927",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [
      {
        "work_item_id": "wi:dad7a0b2953041a597762b7190bd074c",
        "depends_on_work_item_id": "wi:d08356a155404433bbea2f6700287927",
        "required": 1,
        "note": "c2-intake"
      }
    ],
    "work_item_relations": [
      {
        "from_work_item_id": "wi:daad704307a448e09f7b32b903939a52",
        "to_work_item_id": "wi:d08356a155404433bbea2f6700287927",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T06:37:59Z",
        "actor": "c2-root-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "wi:9b5fe27af4814065918a72c1d5b85fc4",
        "to_work_item_id": "wi:d08356a155404433bbea2f6700287927",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T06:37:59Z",
        "actor": "c2-root-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "wi:91bda0f2a16f43049ab1f15c4d8005b7",
        "to_work_item_id": "wi:d08356a155404433bbea2f6700287927",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T06:39:48Z",
        "actor": "c2-root-audit",
        "note": "DUPLICATE_MERGE"
      }
    ],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [
      {
        "receipt_id": "work-item:wi:d08356a155404433bbea2f6700287927:d9b156e1ae982e9ee70595c6746309b7",
        "work_item_id": "wi:d08356a155404433bbea2f6700287927",
        "run_id": null,
        "prompt_id": null,
        "outcome": "BLOCKED",
        "summary": "Operational C2 worktree sanitation and recurrence guards are integrated; remaining historical dirty worktrees require their owning repository/task dispositions.",
        "completed_json": "[\"C2 canonical and installed runtime worktrees are clean, current, and pass the startup guard.\", \"Protected-ref pack-refs diagnostics and opt-in byte-equivalent runtime recovery were integrated in C2 PR #3911 with focused tests passing.\", \"MegaVault-registered dirty worktrees were classified by repository and source owner; overlapping C2 ADB-history trees were reduced to one future task identity without deleting either.\"]",
        "remaining_json": "[\"Preserved historical dirty worktrees with unique or owner-specific changes need safe owner-level integration, publication, or explicit retirement before they can be cleaned.\", \"Global branch convergence wi:dad7a0b2953041a597762b7190bd074c requires this item completed and per-branch ancestry or patch-equivalence review after active integrations.\"]",
        "evidence_json": "[\"ROADMAP-BATCH-RECONCILIATION-20260928.md batch-01 residual dirty ownership, 15:50 UTC whole-batch reconciliation, and 16:47 UTC owner refinement; checkpoint branch ac9c1163 pushed.\", \"C2 PR #3911 merged; focused tests 18 PASS and pull tests 21 PASS; canonical and installed runtime guards healthy.\", \"19 preserved registered dirty worktrees at the bounded inventory; eight isolated C2 trees and two unowned canonical trees reread without reset or stash.\"]",
        "blocker": "Remaining dirty trees contain unique historical code, task data, or owner-specific staged/untracked changes; no safe global cleanup or branch deletion is justified until those owners integrate or explicitly retire their work. No current installed C2 canonical/runtime dirt blocks execution.",
        "next_action": "When an owning repository task integrates or an owner provides explicit retirement evidence, recheck only its preserved worktree, checkpoint unique changes, then clean it safely; repeat for the remaining named owners and only then reconsider d083 completion and dad7 branch convergence.",
        "strict_contract": 1,
        "payload_sha256": "d9b156e1ae982e9ee70595c6746309b7611ae66895d0a791e64214d63ad6c48f",
        "captured_at": 1790614767.143547
      }
    ],
    "work_item_evidence": [
      {
        "evidence_id": 513,
        "work_item_id": "wi:d08356a155404433bbea2f6700287927",
        "evidence_kind": "issue_inbox",
        "label": "issue:9a7fe44aaef2445098aab976fb00f53e",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Sanare TUTTI i repository e worktree sporchi rilevabili nell’ambiente C2/PersonalHub e negli altri repo gestiti, senza perdere lavoro valido: classificare ogni dirty state (modifiche intenzionali/non committate, artefatti generati, merge/rebase/stash residui, file untracked, branch/worktree operativi), portare ogni repo a uno stato coerente e pushato quando appropriato, e verificare che non restino dirty worktree che possano bloccare autosync, scheduler, executor o recovery. Inoltre implementare, se tecnicamente sensato, un fix sistemico che prevenga la ricorrenza: rilevazione/preflight automatica del dirty state, cleanup sicuro degli artefatti generati, isolamento corretto dei worktree/executor, checkpoint commit+push e recovery/fail-closed invece di accumulare modifiche locali. Il risultato deve coprire tutti i repo/worktree interessati, non solo quelli già noti.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:9a7fe44aaef2445098aab976fb00f53e\", \"observed_at_ms\": 1790463317821, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-27T00:50:41Z"
      },
      {
        "evidence_id": 624,
        "work_item_id": "wi:d08356a155404433bbea2f6700287927",
        "evidence_kind": "issue_inbox",
        "label": "issue:1ae99de21cff4d33a87aac4ea6ada7bf",
        "uri": "codex://threads/01a0e173-23e2-76d0-b9d5-d520ad172f0c",
        "value_json": "{\"chat_url\": \"codex://threads/01a0e173-23e2-76d0-b9d5-d520ad172f0c\", \"code_location\": \"tools/c2_runtime.py\", \"description\": \"C2 runtime launch is currently blocked: c2-runtime.service fails before launching acknowledged run ca41243058a34906a088c21c271dba56 / PROMPT_ID=853479 because tools/c2_worktree_guard.py reports the runtime worktree ~/.local/share/c2-supervisor/worktree unhealthy with issues [dirty_worktree, runtime_code_drift]. Timer/watchdog remain active, but the worker unit is never created. Restore/realign the runtime worktree safely while preserving the durable recovery pointer outside disposable runtime state, then resume the same run identity without rescheduling.\", \"executor\": \"codex\", \"executor_ref\": \"01a0e173-23e2-76d0-b9d5-d520ad172f0c\", \"issue_id\": \"issue:1ae99de21cff4d33a87aac4ea6ada7bf\", \"observed_at_ms\": 1790504481658, \"origin_run_id\": null, \"origin_work_item_id\": \"prompt:660629\", \"repo\": \"gernalix/codex-roadmap\"}",
        "created_at": "2026-09-27T10:27:50Z"
      },
      {
        "evidence_id": 1315,
        "work_item_id": "wi:d08356a155404433bbea2f6700287927",
        "evidence_kind": "issue_inbox",
        "label": "issue:0258b6d8994743bd81ad12257f5003cc",
        "uri": "codex://threads/01a0e425-7cbe-7270-b9b4-6d074a91c1b6",
        "value_json": "{\"chat_url\": \"codex://threads/01a0e425-7cbe-7270-b9b4-6d074a91c1b6\", \"code_location\": null, \"description\": \"PersonalHub single-writer managed worktree for queued PR #57 had 40 uncommitted cross-scope files, causing guarded integration to stall; preserving them required a separate pushed branch and manual worktree reset before queue processing. Need a fail-fast guard and durable recovery protocol that identifies dirty queued worktrees before integration without risking changes.\", \"executor\": null, \"executor_ref\": \"01a0e425-7cbe-7270-b9b4-6d074a91c1b6\", \"issue_id\": \"issue:0258b6d8994743bd81ad12257f5003cc\", \"observed_at_ms\": 1790552828649, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-27T23:50:51Z"
      },
      {
        "evidence_id": 1641,
        "work_item_id": "wi:d08356a155404433bbea2f6700287927",
        "evidence_kind": "executor_result",
        "label": "ROADMAP-BATCH-RECONCILIATION-20260928.md batch-01 residual dirty ownership, 15:50 UTC whole-batch reconciliation, and 16",
        "uri": null,
        "value_json": "\"ROADMAP-BATCH-RECONCILIATION-20260928.md batch-01 residual dirty ownership, 15:50 UTC whole-batch reconciliation, and 16:47 UTC owner refinement; checkpoint branch ac9c1163 pushed.\"",
        "created_at": "2026-09-28T16:59:27Z"
      },
      {
        "evidence_id": 1642,
        "work_item_id": "wi:d08356a155404433bbea2f6700287927",
        "evidence_kind": "executor_result",
        "label": "C2 PR #3911 merged; focused tests 18 PASS and pull tests 21 PASS; canonical and installed runtime guards healthy.",
        "uri": null,
        "value_json": "\"C2 PR #3911 merged; focused tests 18 PASS and pull tests 21 PASS; canonical and installed runtime guards healthy.\"",
        "created_at": "2026-09-28T16:59:27Z"
      },
      {
        "evidence_id": 1643,
        "work_item_id": "wi:d08356a155404433bbea2f6700287927",
        "evidence_kind": "executor_result",
        "label": "19 preserved registered dirty worktrees at the bounded inventory; eight isolated C2 trees and two unowned canonical tree",
        "uri": null,
        "value_json": "\"19 preserved registered dirty worktrees at the bounded inventory; eight isolated C2 trees and two unowned canonical trees reread without reset or stash.\"",
        "created_at": "2026-09-28T16:59:27Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:1ae99de21cff4d33a87aac4ea6ada7bf",
        "work_item_id": "wi:d08356a155404433bbea2f6700287927",
        "role": "matched",
        "created_at": "2026-09-27T10:21:21Z"
      },
      {
        "issue_id": "issue:0258b6d8994743bd81ad12257f5003cc",
        "work_item_id": "wi:d08356a155404433bbea2f6700287927",
        "role": "matched",
        "created_at": "2026-09-27T23:47:08Z"
      },
      {
        "issue_id": "issue:9a7fe44aaef2445098aab976fb00f53e",
        "work_item_id": "wi:d08356a155404433bbea2f6700287927",
        "role": "decision",
        "created_at": "2026-09-26T22:55:17Z"
      },
      {
        "issue_id": "issue:1ae99de21cff4d33a87aac4ea6ada7bf",
        "work_item_id": "wi:d08356a155404433bbea2f6700287927",
        "role": "decision",
        "created_at": "2026-09-27T10:21:21Z"
      },
      {
        "issue_id": "issue:0258b6d8994743bd81ad12257f5003cc",
        "work_item_id": "wi:d08356a155404433bbea2f6700287927",
        "role": "decision",
        "created_at": "2026-09-27T23:47:08Z"
      }
    ]
  }
]
```
