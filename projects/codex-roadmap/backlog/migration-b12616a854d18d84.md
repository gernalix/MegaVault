# Conservare e confrontare lo storico dei test ADB

<!-- migration-b12616a854d18d84 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 49, 51.

Provenance: `wi:a299a4c1a72049b88f594587dc786768`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Conservare e confrontare lo storico dei test ADB

Aggiungere a C2 un registro strutturato e rapidamente interrogabile dei test Android/ADB, con risultati, contesto di build/device e metriche numeriche storiche; integrare PersonalHub Macrobenchmark per conservare e confrontare nel tempo i tempi di avvio di app e moduli.

Acceptance:

- Ogni run registrata conserva timestamp, progetto/repo, commit/build, device, tipo test, outcome e riferimenti all'evidenza grezza.
- Le metriche numeriche sono normalizzate e interrogabili come serie storica per progetto, device, scenario e metrica.
- PersonalHub Macrobenchmark può importare i tempi di cold startup per modulo senza parsing manuale.
- Esistono query/CLI concise per latest, history e confronto con il run precedente.
- Schema e ingestione sono idempotenti e coperti da test; nessun DB live viene modificato fuori dal writer C2.

status: blocked

current_action: Codex preparation requested from explicit structured input.

next_action: Resolve the exact execution metadata/worktree and existing task identity before dispatch.

blocker: Historical ADB metrics task has no explicit blocker, accepted execution spec, or current executor receipt; resolution cannot be inferred.

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "51",
      "reason": "canonical MegaVault project_id",
      "related_projects": [
        "51",
        "49"
      ]
    },
    "source": {
      "work_item_id": "wi:a299a4c1a72049b88f594587dc786768",
      "parent_id": null,
      "kind": "task",
      "title": "Conservare e confrontare lo storico dei test ADB",
      "objective": "Aggiungere a C2 un registro strutturato e rapidamente interrogabile dei test Android/ADB, con risultati, contesto di build/device e metriche numeriche storiche; integrare PersonalHub Macrobenchmark per conservare e confrontare nel tempo i tempi di avvio di app e moduli.",
      "acceptance_json": "[\"Ogni run registrata conserva timestamp, progetto/repo, commit/build, device, tipo test, outcome e riferimenti all'evidenza grezza.\", \"Le metriche numeriche sono normalizzate e interrogabili come serie storica per progetto, device, scenario e metrica.\", \"PersonalHub Macrobenchmark può importare i tempi di cold startup per modulo senza parsing manuale.\", \"Esistono query/CLI concise per latest, history e confronto con il run precedente.\", \"Schema e ingestione sono idempotenti e coperti da test; nessun DB live viene modificato fuori dal writer C2.\"]",
      "status": "blocked",
      "executor_policy": "codex",
      "sort_order": 60,
      "current_action": "Codex preparation requested from explicit structured input.",
      "next_action": "Resolve the exact execution metadata/worktree and existing task identity before dispatch.",
      "blocker": "Historical ADB metrics task has no explicit blocker, accepted execution spec, or current executor receipt; resolution cannot be inferred.",
      "project_id": "51",
      "project_name": "codex-roadmap",
      "repo": "https://github.com/gernalix/codex-roadmap",
      "prompt_id": "875575",
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-25T17:41:05Z",
      "updated_at": "2026-09-27T22:23:04.087741Z"
    },
    "prompt_metadata": [
      {
        "prompt_id": "875575",
        "slug": "conservare-e-confrontare-lo-storico-dei-test-adb-875575",
        "chat_guidance": null,
        "prompt_type": "Prompt",
        "model": "GPT-5.6 Sol",
        "reasoning": "medium",
        "megavault_mode": null,
        "campaign_id": null,
        "explanation": "",
        "current_path": "falliti/conservare-e-confrontare-lo-storico-dei-test-adb-875575.md",
        "materialization_sha256": "6fd07e96570eee7d1a5c6c23e9c44bc0dc37a387c2719130fcd41594d36340f0",
        "created_at": "2026-09-26T22:40:17Z",
        "updated_at": "2026-09-26T22:45:05Z"
      }
    ],
    "prompt_materializations": [
      {
        "prompt_id": "875575",
        "body": "PROMPT_ID=875575\n\n# Goal\nAggiungere a C2 un registro strutturato e rapidamente interrogabile dei test Android/ADB, con risultati, contesto di build/device e metriche numeriche storiche; integrare PersonalHub Macrobenchmark per conservare e confrontare nel tempo i tempi di avvio di app e moduli.\n\n# Canonical starting point\n- C2 work item: wi:a299a4c1a72049b88f594587dc786768\n- Repository: https://github.com/gernalix/codex-roadmap\n- The work item scope and acceptance below are authoritative. Inspect only files needed to satisfy them.\n- Use the assigned isolated worktree and the repository single-writer/integration path. Do not edit canonical branches directly.\n- Do not broaden scope into unrelated cleanup, refactors or audits.\n- Existing verified evidence:\n  - codex-roadmap main a5873827 c2_scheduler.configure_auto requires structured execution.worktree and materialized prompt/exact metadata for Codex; this intake has no work_item_execution_specs row.\n  - codex-roadmap main a5873827 lacks structured ADB test metrics/ingest/query; PersonalHub main c9a574cf contains PersonalHubShortcutBenchmarks.kt.\n\n# First bounded action\nImplement C2 metric schema and ingest/query first; coordinate PH benchmark adapter with PH owner.\n\n# Acceptance\n- Ogni run registrata conserva timestamp, progetto/repo, commit/build, device, tipo test, outcome e riferimenti all'evidenza grezza.\n- Le metriche numeriche sono normalizzate e interrogabili come serie storica per progetto, device, scenario e metrica.\n- PersonalHub Macrobenchmark può importare i tempi di cold startup per modulo senza parsing manuale.\n- Esistono query/CLI concise per latest, history e confronto con il run precedente.\n- Schema e ingestione sono idempotenti e coperti da test; nessun DB live viene modificato fuori dal writer C2.\n\n# Execution rules\n- Fix only failures necessary for this goal; preserve unrelated local/runtime state.\n- Use targeted tests first and widen only if evidence requires it.\n- On incidental C2 bugs/bottlenecks, capture only the description to the C2 Inbox and continue.\n- Stop immediately when acceptance is verified; do not wait on CI/merge in a model turn.\n",
        "sha256": "6fd07e96570eee7d1a5c6c23e9c44bc0dc37a387c2719130fcd41594d36340f0",
        "created_at": "2026-09-26T22:40:17Z",
        "actor": "c2-intake"
      }
    ],
    "analyses": [],
    "executions": [
      {
        "execution_id": 405,
        "prompt_id": "875575",
        "cycle_key": "9b40c7111933213218f84817",
        "materialization_sha256": "60fd99fd5501cd2f5fe65625906d2a773eee5b17833cd8cc4c58fc05be6af153",
        "started_at": "2026-09-26T22:45:54Z",
        "ended_at": "2026-09-26T22:45:58Z",
        "outcome": "UNKNOWN",
        "duration_seconds": 3.783,
        "model": "codex-auto-review",
        "reasoning": "low",
        "codex_project": "/home/daniele/.local/share/c2-supervisor/worktrees/codex-roadmap/875575",
        "chat_title": null,
        "branch": null,
        "commit_before": null,
        "commit_after": null,
        "tool_call_count": 0,
        "input_tokens": 22142,
        "cached_input_tokens": 4864,
        "uncached_input_tokens": 17278,
        "output_tokens": 153,
        "reasoning_output_tokens": 98,
        "total_tokens": 22295,
        "source": "codex-usage",
        "recorded_at": "2026-09-26T22:46:46Z"
      },
      {
        "execution_id": 406,
        "prompt_id": "875575",
        "cycle_key": "0b12e716b9ced67d5e00c396",
        "materialization_sha256": "669610993da8de37349af23471e48fe0484c16bffcd7241af6a70eccdb3537a2",
        "started_at": "2026-09-26T22:49:45Z",
        "ended_at": "2026-09-26T22:49:48Z",
        "outcome": "UNKNOWN",
        "duration_seconds": 2.715,
        "model": "codex-auto-review",
        "reasoning": "low",
        "codex_project": "/home/daniele/.local/share/c2-supervisor/worktrees/codex-roadmap/875575",
        "chat_title": null,
        "branch": null,
        "commit_before": null,
        "commit_after": null,
        "tool_call_count": 0,
        "input_tokens": 31183,
        "cached_input_tokens": 28416,
        "uncached_input_tokens": 2767,
        "output_tokens": 80,
        "reasoning_output_tokens": 21,
        "total_tokens": 31263,
        "source": "codex-usage",
        "recorded_at": "2026-09-26T22:52:00Z"
      }
    ],
    "status_history": [
      {
        "history_id": 986,
        "prompt_id": "875575",
        "old_status": null,
        "new_status": "pending",
        "changed_at": "2026-09-26T22:40:17Z",
        "actor": "c2-intake",
        "note": "work item materialized for Codex"
      },
      {
        "history_id": 990,
        "prompt_id": "875575",
        "old_status": "pending",
        "new_status": "running",
        "changed_at": "2026-09-26T22:43:21Z",
        "actor": "c2-scheduler",
        "note": null
      },
      {
        "history_id": 991,
        "prompt_id": "875575",
        "old_status": "running",
        "new_status": "blocked",
        "changed_at": "2026-09-26T22:45:05Z",
        "actor": "codex",
        "note": "repo-task isolation could not be established after launch claim"
      }
    ],
    "work_item_tags": [
      {
        "work_item_id": "wi:a299a4c1a72049b88f594587dc786768",
        "tag": "c2"
      },
      {
        "work_item_id": "wi:a299a4c1a72049b88f594587dc786768",
        "tag": "android"
      },
      {
        "work_item_id": "wi:a299a4c1a72049b88f594587dc786768",
        "tag": "adb"
      },
      {
        "work_item_id": "wi:a299a4c1a72049b88f594587dc786768",
        "tag": "test-evidence"
      },
      {
        "work_item_id": "wi:a299a4c1a72049b88f594587dc786768",
        "tag": "performance-history"
      },
      {
        "work_item_id": "wi:a299a4c1a72049b88f594587dc786768",
        "tag": "priority:p0"
      }
    ],
    "work_item_dependencies": [
      {
        "work_item_id": "wi:a299a4c1a72049b88f594587dc786768",
        "depends_on_work_item_id": "prompt:175908",
        "required": 1,
        "note": "c2-intake"
      }
    ],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 368,
        "work_item_id": "wi:a299a4c1a72049b88f594587dc786768",
        "evidence_kind": "classification",
        "label": "codex-roadmap main a5873827 lacks structured ADB test metrics/ingest/query; PersonalHub main c9a574cf contains PersonalH",
        "uri": null,
        "value_json": "\"codex-roadmap main a5873827 lacks structured ADB test metrics/ingest/query; PersonalHub main c9a574cf contains PersonalHubShortcutBenchmarks.kt.\"",
        "created_at": "2026-09-26T17:12:41Z"
      },
      {
        "evidence_id": 381,
        "work_item_id": "wi:a299a4c1a72049b88f594587dc786768",
        "evidence_kind": "classification",
        "label": "codex-roadmap main a5873827 c2_scheduler.configure_auto requires structured execution.worktree and materialized prompt/e",
        "uri": null,
        "value_json": "\"codex-roadmap main a5873827 c2_scheduler.configure_auto requires structured execution.worktree and materialized prompt/exact metadata for Codex; this intake has no work_item_execution_specs row.\"",
        "created_at": "2026-09-26T17:18:38Z"
      },
      {
        "evidence_id": 428,
        "work_item_id": "wi:a299a4c1a72049b88f594587dc786768",
        "evidence_kind": "classification",
        "label": "The 2026-09-26 C2 root audit already verified this intake against the relevant repository and recorded that its only exe",
        "uri": null,
        "value_json": "\"The 2026-09-26 C2 root audit already verified this intake against the relevant repository and recorded that its only execution blocker is the missing canonical Codex prompt/exact metadata/isolated worktree context.\"",
        "created_at": "2026-09-26T22:40:00Z"
      },
      {
        "evidence_id": 429,
        "work_item_id": "wi:a299a4c1a72049b88f594587dc786768",
        "evidence_kind": "classification",
        "label": "codex-roadmap main a5873827 lacks structured ADB test metrics/ingest/query; PersonalHub main c9a574cf contains PersonalH",
        "uri": null,
        "value_json": "\"codex-roadmap main a5873827 lacks structured ADB test metrics/ingest/query; PersonalHub main c9a574cf contains PersonalHubShortcutBenchmarks.kt.\"",
        "created_at": "2026-09-26T22:40:00Z"
      },
      {
        "evidence_id": 1183,
        "work_item_id": "wi:a299a4c1a72049b88f594587dc786768",
        "evidence_kind": "blocked_reconcile",
        "label": "Historical ADB metrics task has no explicit blocker, accepted execution spec, or current executor receipt; resolution ca",
        "uri": null,
        "value_json": "\"Historical ADB metrics task has no explicit blocker, accepted execution spec, or current executor receipt; resolution cannot be inferred.\"",
        "created_at": "2026-09-27T22:23:04.087741Z"
      }
    ],
    "work_item_runs": [
      {
        "run_id": "2929627471944cc58ee1f1ddf703dcae",
        "work_item_id": "wi:a299a4c1a72049b88f594587dc786768",
        "event_key": "c2-schedule-2c1102f30d6a8b5c3091a9c54cbf1fb2",
        "attempt": 1,
        "executor": "codex",
        "state": "failed",
        "lease_until": 0.0,
        "worker_ref": null,
        "checkpoint_commit": null,
        "metadata_json": "{\"activity\": \"coding\", \"command_json\": null, \"executor\": \"codex\", \"goal_mode\": 0, \"max_attempts\": 3, \"model\": \"GPT-5.6 Sol\", \"pre_migration_retirement\": {\"checkpoint_commit\": null, \"classification\": \"historical-only\", \"lease_until\": 1790462758.7021556, \"previous_state\": \"failed\", \"worker_ref\": \"c2-run:2929627471944cc58ee1f1ddf703dcae\"}, \"project_url\": null, \"prompt_id\": \"875575\", \"reasoning\": \"medium\", \"repo\": \"https://github.com/gernalix/codex-roadmap\", \"resources_json\": \"[\\\"c2-test-evidence\\\"]\", \"work_item_id\": \"wi:a299a4c1a72049b88f594587dc786768\", \"worktree\": \"/home/daniele/.local/share/c2-supervisor/worktrees/codex-roadmap/875575\"}",
        "created_at": 1790462601.4020302
      }
    ],
    "issue_work_item_links": []
  }
]
```
