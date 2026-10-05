# Aggiungere fast-path C2 per adottare modifiche esterne

<!-- migration-3c032b29a01731b2 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:53a52adb1bf24689a76e384a95ca9919`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Aggiungere fast-path C2 per adottare modifiche esterne

C2: introdurre un fast-path canonico per adottare e integrare modifiche prodotte fuori dalla C2, separato dal lifecycle C2-native. Prevedere un helper idempotente tipo  che: verifica commit/branch e policy no-direct-main; deduplica per SHA; associa o crea solo il minimo record C2 necessario con provenance=external; non richiede executor_started, PROMPT_ID, claim manuali o mutation start/result; serializza soltanto l'integrazione tramite single-writer senza bloccare la registrazione perché un altro work item dello stesso repo è running; pusha/crea/integra PR quando necessario; per commit già mergiati registra solo provenance/evidence; registra commit, PR e merge SHA e chiude il work item solo se ne copre interamente lo scope. Output compatto canonico RESULT/COMMIT/MERGE_SHA/PR/C2. Inoltre, una volta che il work item è terminale, steer/messaggi Codex già accodati devono essere annullati o respinti salvo esplicita riapertura/nuovo work item, per evitare commit/PR fuori lifecycle.

status: blocked

current_action: BLOCKED by invalid auto-preparation contract; supervisor stopped the unintended run.

next_action: Fix and test the Track A preparer to fail closed on missing acceptance, then reconcile this prepared artifact explicitly before any retry.

blocker: Auto-preparation admitted an incomplete work-item contract with empty acceptance criteria; execution was stopped before acceptance could be verified.

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "51",
      "reason": "canonical MegaVault project_id",
      "related_projects": [
        "51"
      ]
    },
    "source": {
      "work_item_id": "wi:53a52adb1bf24689a76e384a95ca9919",
      "parent_id": null,
      "kind": "task",
      "title": "Aggiungere fast-path C2 per adottare modifiche esterne",
      "objective": "C2: introdurre un fast-path canonico per adottare e integrare modifiche prodotte fuori dalla C2, separato dal lifecycle C2-native. Prevedere un helper idempotente tipo  che: verifica commit/branch e policy no-direct-main; deduplica per SHA; associa o crea solo il minimo record C2 necessario con provenance=external; non richiede executor_started, PROMPT_ID, claim manuali o mutation start/result; serializza soltanto l'integrazione tramite single-writer senza bloccare la registrazione perché un altro work item dello stesso repo è running; pusha/crea/integra PR quando necessario; per commit già mergiati registra solo provenance/evidence; registra commit, PR e merge SHA e chiude il work item solo se ne copre interamente lo scope. Output compatto canonico RESULT/COMMIT/MERGE_SHA/PR/C2. Inoltre, una volta che il work item è terminale, steer/messaggi Codex già accodati devono essere annullati o respinti salvo esplicita riapertura/nuovo work item, per evitare commit/PR fuori lifecycle.",
      "acceptance_json": "[]",
      "status": "blocked",
      "executor_policy": "codex",
      "sort_order": null,
      "current_action": "BLOCKED by invalid auto-preparation contract; supervisor stopped the unintended run.",
      "next_action": "Fix and test the Track A preparer to fail closed on missing acceptance, then reconcile this prepared artifact explicitly before any retry.",
      "blocker": "Auto-preparation admitted an incomplete work-item contract with empty acceptance criteria; execution was stopped before acceptance could be verified.",
      "project_id": "51",
      "project_name": "codex-roadmap",
      "repo": "gernalix/codex-roadmap",
      "prompt_id": "314611",
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-27T07:33:41Z",
      "updated_at": "2026-10-02T10:31:41Z"
    },
    "prompt_metadata": [
      {
        "prompt_id": "314611",
        "slug": "aggiungere-fast-path-c2-per-adottare-modifiche-e-314611",
        "chat_guidance": null,
        "prompt_type": "Prompt",
        "model": "gpt-5.6-sol",
        "reasoning": "medium",
        "megavault_mode": null,
        "campaign_id": null,
        "explanation": "",
        "current_path": "prompts/aggiungere-fast-path-c2-per-adottare-modifiche-e-314611.md",
        "materialization_sha256": "dcd8e645ebd8f568ad9ee0d09b10c78763f5341a695da361bbfdc79969388f92",
        "created_at": "2026-10-02T10:28:20Z",
        "updated_at": "2026-10-02T10:28:20Z"
      }
    ],
    "prompt_materializations": [
      {
        "prompt_id": "314611",
        "body": "PROMPT_ID=314611\n\n# Aggiungere fast-path C2 per adottare modifiche esterne\n\n## Objective\nC2: introdurre un fast-path canonico per adottare e integrare modifiche prodotte fuori dalla C2, separato dal lifecycle C2-native. Prevedere un helper idempotente tipo  che: verifica commit/branch e policy no-direct-main; deduplica per SHA; associa o crea solo il minimo record C2 necessario con provenance=external; non richiede executor_started, PROMPT_ID, claim manuali o mutation start/result; serializza soltanto l'integrazione tramite single-writer senza bloccare la registrazione perché un altro work item dello stesso repo è running; pusha/crea/integra PR quando necessario; per commit già mergiati registra solo provenance/evidence; registra commit, PR e merge SHA e chiude il work item solo se ne copre interamente lo scope. Output compatto canonico RESULT/COMMIT/MERGE_SHA/PR/C2. Inoltre, una volta che il work item è terminale, steer/messaggi Codex già accodati devono essere annullati o respinti salvo esplicita riapertura/nuovo work item, per evitare commit/PR fuori lifecycle.\n",
        "sha256": "dcd8e645ebd8f568ad9ee0d09b10c78763f5341a695da361bbfdc79969388f92",
        "created_at": "2026-10-02T10:28:20Z",
        "actor": "c2-intake"
      }
    ],
    "analyses": [],
    "executions": [],
    "status_history": [
      {
        "history_id": 1131,
        "prompt_id": "314611",
        "old_status": null,
        "new_status": "pending",
        "changed_at": "2026-10-02T10:28:20Z",
        "actor": "c2-intake",
        "note": "work item materialized for Codex"
      },
      {
        "history_id": 1132,
        "prompt_id": "314611",
        "old_status": "pending",
        "new_status": "running",
        "changed_at": "2026-10-02T10:28:39Z",
        "actor": "c2-scheduler",
        "note": null
      },
      {
        "history_id": 1133,
        "prompt_id": "314611",
        "old_status": "running",
        "new_status": "blocked",
        "changed_at": "2026-10-02T10:31:41Z",
        "actor": "c2-executor-result",
        "note": "executor_result:run:f77c639f283c4abd9f85838e1c2d29e9"
      }
    ],
    "work_item_tags": [
      {
        "work_item_id": "wi:53a52adb1bf24689a76e384a95ca9919",
        "tag": "source:issue-inbox"
      },
      {
        "work_item_id": "wi:53a52adb1bf24689a76e384a95ca9919",
        "tag": "priority:p0"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [
      {
        "receipt_id": "run:f77c639f283c4abd9f85838e1c2d29e9",
        "work_item_id": "wi:53a52adb1bf24689a76e384a95ca9919",
        "run_id": "f77c639f283c4abd9f85838e1c2d29e9",
        "prompt_id": "314611",
        "outcome": "BLOCKED",
        "summary": "BLOCKED by invalid auto-preparation contract; supervisor stopped the unintended run.",
        "completed_json": "[]",
        "remaining_json": "[\"Do not execute the auto-prepared prompt until the work item has a non-empty canonical acceptance contract and the Track A preparation gate is fixed.\"]",
        "evidence_json": "[\"Supervisor observed work item wi:53a52adb1bf24689a76e384a95ca9919 with acceptance_json=[] after auto-preparation.\", \"Runtime immediately scheduled run f77c639f283c4abd9f85838e1c2d29e9 after the spec was materialized.\", \"The run unit was physically stopped before any task result was accepted; Symphony reports no active agent.\"]",
        "blocker": "Auto-preparation admitted an incomplete work-item contract with empty acceptance criteria; execution was stopped before acceptance could be verified.",
        "next_action": "Fix and test the Track A preparer to fail closed on missing acceptance, then reconcile this prepared artifact explicitly before any retry.",
        "strict_contract": 1,
        "payload_sha256": "d1022dfcba6dd56c2dad3f7d834a3d70beef0ab42f99d684e856701144e0d3f0",
        "captured_at": 1790937101.656792
      }
    ],
    "work_item_evidence": [
      {
        "evidence_id": 591,
        "work_item_id": "wi:53a52adb1bf24689a76e384a95ca9919",
        "evidence_kind": "issue_inbox",
        "label": "issue:7f2185567bf043d9a09e28b9427df6ff",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": \"tools/repo-task + C2 executor/scheduler integration\", \"description\": \"C2: introdurre un fast-path canonico per adottare e integrare modifiche prodotte fuori dalla C2, separato dal lifecycle C2-native. Prevedere un helper idempotente tipo  che: verifica commit/branch e policy no-direct-main; deduplica per SHA; associa o crea solo il minimo record C2 necessario con provenance=external; non richiede executor_started, PROMPT_ID, claim manuali o mutation start/result; serializza soltanto l'integrazione tramite single-writer senza bloccare la registrazione perché un altro work item dello stesso repo è running; pusha/crea/integra PR quando necessario; per commit già mergiati registra solo provenance/evidence; registra commit, PR e merge SHA e chiude il work item solo se ne copre interamente lo scope. Output compatto canonico RESULT/COMMIT/MERGE_SHA/PR/C2. Inoltre, una volta che il work item è terminale, steer/messaggi Codex già accodati devono essere annullati o respinti salvo esplicita riapertura/nuovo work item, per evitare commit/PR fuori lifecycle.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:7f2185567bf043d9a09e28b9427df6ff\", \"observed_at_ms\": 1790494342912, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"codex-roadmap\"}",
        "created_at": "2026-09-27T07:33:41Z"
      },
      {
        "evidence_id": 1888,
        "work_item_id": "wi:53a52adb1bf24689a76e384a95ca9919",
        "evidence_kind": "classification",
        "label": "User explicitly requested P0 for the C2 batch on 2026-09-30; this item is currently runnable and belongs to gernalix/cod",
        "uri": null,
        "value_json": "\"User explicitly requested P0 for the C2 batch on 2026-09-30; this item is currently runnable and belongs to gernalix/codex-roadmap.\"",
        "created_at": "2026-09-29T22:21:33Z"
      },
      {
        "evidence_id": 2582,
        "work_item_id": "wi:53a52adb1bf24689a76e384a95ca9919",
        "evidence_kind": "classification",
        "label": "MegaVault canonical repository R0051",
        "uri": null,
        "value_json": "\"MegaVault canonical repository R0051\"",
        "created_at": "2026-10-02T10:28:20Z"
      },
      {
        "evidence_id": 2583,
        "work_item_id": "wi:53a52adb1bf24689a76e384a95ca9919",
        "evidence_kind": "classification",
        "label": "canonical successful execution profile for gernalix/codex-roadmap",
        "uri": null,
        "value_json": "\"canonical successful execution profile for gernalix/codex-roadmap\"",
        "created_at": "2026-10-02T10:28:20Z"
      },
      {
        "evidence_id": 2584,
        "work_item_id": "wi:53a52adb1bf24689a76e384a95ca9919",
        "evidence_kind": "executor_result",
        "label": "Supervisor observed work item wi:53a52adb1bf24689a76e384a95ca9919 with acceptance_json=[] after auto-preparation.",
        "uri": null,
        "value_json": "\"Supervisor observed work item wi:53a52adb1bf24689a76e384a95ca9919 with acceptance_json=[] after auto-preparation.\"",
        "created_at": "2026-10-02T10:31:41Z"
      },
      {
        "evidence_id": 2585,
        "work_item_id": "wi:53a52adb1bf24689a76e384a95ca9919",
        "evidence_kind": "executor_result",
        "label": "Runtime immediately scheduled run f77c639f283c4abd9f85838e1c2d29e9 after the spec was materialized.",
        "uri": null,
        "value_json": "\"Runtime immediately scheduled run f77c639f283c4abd9f85838e1c2d29e9 after the spec was materialized.\"",
        "created_at": "2026-10-02T10:31:41Z"
      },
      {
        "evidence_id": 2586,
        "work_item_id": "wi:53a52adb1bf24689a76e384a95ca9919",
        "evidence_kind": "executor_result",
        "label": "The run unit was physically stopped before any task result was accepted; Symphony reports no active agent.",
        "uri": null,
        "value_json": "\"The run unit was physically stopped before any task result was accepted; Symphony reports no active agent.\"",
        "created_at": "2026-10-02T10:31:41Z"
      }
    ],
    "work_item_runs": [
      {
        "run_id": "f77c639f283c4abd9f85838e1c2d29e9",
        "work_item_id": "wi:53a52adb1bf24689a76e384a95ca9919",
        "event_key": "c2-schedule-f58cf724c09a14c6124fa594e85bd432",
        "attempt": 1,
        "executor": "symphony",
        "state": "failed",
        "lease_until": 1790937039.7597995,
        "worker_ref": "c3-run:f77c639f283c4abd9f85838e1c2d29e9",
        "checkpoint_commit": null,
        "metadata_json": "{\"activity\": \"coding\", \"command_json\": null, \"executor\": \"symphony\", \"goal_mode\": 0, \"max_attempts\": 3, \"model\": \"gpt-5.6-sol\", \"model_id\": \"gpt-5.6-sol\", \"project_url\": null, \"prompt_id\": \"314611\", \"reasoning\": \"medium\", \"reasoning_effort\": \"medium\", \"repo\": \"gernalix/codex-roadmap\", \"resources_json\": \"[]\", \"symphony_route\": {\"mode\": \"production\", \"source_repos\": [\"gernalix/codex-roadmap\"], \"tracker_repo\": \"gernalix/c3-symphony\"}, \"work_item_id\": \"wi:53a52adb1bf24689a76e384a95ca9919\", \"worktree\": \"/home/daniele/.local/share/codex-github-autosync/worktrees/gernalix_codex-roadmap/314611\"}",
        "created_at": 1790936919.7457118
      }
    ],
    "issue_work_item_links": [
      {
        "issue_id": "issue:7f2185567bf043d9a09e28b9427df6ff",
        "work_item_id": "wi:53a52adb1bf24689a76e384a95ca9919",
        "role": "decision",
        "created_at": "2026-09-27T07:32:22Z"
      }
    ]
  }
]
```
