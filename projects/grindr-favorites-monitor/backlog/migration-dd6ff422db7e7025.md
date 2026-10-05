# Rendere immediato il profile_id dalle foto Grindr scaricate

<!-- migration-dd6ff422db7e7025 -->

Migrated project backlog. Project: **grindr-favorites-monitor**; project_id: 104.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 104.

Provenance: `wi:cc78ff4dcaf942f998d821fb48826d23`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Rendere immediato il profile_id dalle foto Grindr scaricate

In grindr-favorites-monitor rendere ogni foto profilo scaricata autoidentificante rispetto al profile_id con attrito minimo: naming deterministico che includa chiaramente il profile_id, metadata EXIF/XMP come fallback quando sicuro, mapping univoco e stabile, e backfill/rinomina sicura delle foto esistenti senza perdere associazioni o deduplica.

status: waiting

next_action: Prepare exact bounded implementation and dispatch through C2.

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "104",
      "reason": "canonical repository identity",
      "related_projects": [
        "104"
      ]
    },
    "source": {
      "work_item_id": "wi:cc78ff4dcaf942f998d821fb48826d23",
      "parent_id": null,
      "kind": "task",
      "title": "Rendere immediato il profile_id dalle foto Grindr scaricate",
      "objective": "In grindr-favorites-monitor rendere ogni foto profilo scaricata autoidentificante rispetto al profile_id con attrito minimo: naming deterministico che includa chiaramente il profile_id, metadata EXIF/XMP come fallback quando sicuro, mapping univoco e stabile, e backfill/rinomina sicura delle foto esistenti senza perdere associazioni o deduplica.",
      "acceptance_json": "[]",
      "status": "waiting",
      "executor_policy": "codex",
      "sort_order": 120,
      "current_action": null,
      "next_action": "Prepare exact bounded implementation and dispatch through C2.",
      "blocker": null,
      "project_id": null,
      "project_name": null,
      "repo": "gernalix/grindr-favorites-monitor",
      "prompt_id": "625582",
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-27T08:41:47Z",
      "updated_at": "2026-09-27T22:23:04.384167Z"
    },
    "prompt_metadata": [
      {
        "prompt_id": "625582",
        "slug": "rendere-immediato-il-profile-id-dalle-foto-grind-625582",
        "chat_guidance": null,
        "prompt_type": "Prompt",
        "model": "GPT-5.6 Terra",
        "reasoning": "medium",
        "megavault_mode": "FAST",
        "campaign_id": null,
        "explanation": "",
        "current_path": "prompts/rendere-immediato-il-profile-id-dalle-foto-grind-625582.md",
        "materialization_sha256": "0535eb5cd81f389e4dc450fbd22e9d5625e69917576ab5824e7ee1388b3b1085",
        "created_at": "2026-09-27T10:33:05Z",
        "updated_at": "2026-09-27T22:23:05Z"
      }
    ],
    "prompt_materializations": [
      {
        "prompt_id": "625582",
        "body": "PROMPT_ID=625582\n\nImplementa SOLO il work item C2 assegnato sulla UX foto/profile_id di grindr-favorites-monitor.\n\nRequisiti:\n- ogni foto profilo scaricata deve avere naming stabile/deterministico che includa chiaramente il profile_id ed eventuali metadati già necessari ai flussi esistenti;\n- il profile_id deve essere ricavabile direttamente dal filename/titolo del viewer con attrito minimo; EXIF/XMP solo come fallback sicuro, senza introdurre dipendenze fragili;\n- aggiungi una piccola azione/script Nautilus che, partendo da una foto scaricata, estragga il profile_id dal filename e apra direttamente il profilo corrispondente nel Datasette configurato;\n- mapping foto→profile_id univoco e stabile; backfill/rinomina delle foto esistenti solo se conservativo, idempotente e senza perdita/dedup break;\n- riusa convenzioni e primitive esistenti; niente UI/DB paralleli o refactor estranei.\n\nVerifica con test mirati del naming/parser/backfill e dello script/azione; preserva compatibilità runtime. Commit+push del checkpoint verificato. Usa il percorso repo single-writer già assegnato; non modificare roadmap.sqlite direttamente.\n\nAlla fine integra tramite il percorso canonico del repo e terminalizza PROMPT_ID con roadmap_finish.py. Se emerge un problema incidentale, cattura solo la descrizione con c2_issue_capture.py e continua.\n",
        "sha256": "0535eb5cd81f389e4dc450fbd22e9d5625e69917576ab5824e7ee1388b3b1085",
        "created_at": "2026-09-27T10:33:05Z",
        "actor": "c2-intake"
      }
    ],
    "analyses": [],
    "executions": [
      {
        "execution_id": 460,
        "prompt_id": "625582",
        "cycle_key": "a691cec3dc8e379c00f88068",
        "materialization_sha256": "83c3721b13c10dd9ac205f559c6d77707319524a427687d0f2b8a7f1bea0a7ce",
        "started_at": "2026-09-27T10:44:26Z",
        "ended_at": "2026-09-27T10:44:29Z",
        "outcome": "UNKNOWN",
        "duration_seconds": 3.139,
        "model": "codex-auto-review",
        "reasoning": "low",
        "codex_project": "/home/daniele/.local/share/codex-github-autosync/worktrees/gernalix_grindr-favorites-monitor/625582",
        "chat_title": null,
        "branch": null,
        "commit_before": null,
        "commit_after": null,
        "tool_call_count": 0,
        "input_tokens": 14004,
        "cached_input_tokens": 11008,
        "uncached_input_tokens": 2996,
        "output_tokens": 120,
        "reasoning_output_tokens": 51,
        "total_tokens": 14124,
        "source": "codex-usage",
        "recorded_at": "2026-09-27T10:46:05Z"
      },
      {
        "execution_id": 463,
        "prompt_id": "625582",
        "cycle_key": "6679e00f43e7bb994e5c7f3a",
        "materialization_sha256": "0535eb5cd81f389e4dc450fbd22e9d5625e69917576ab5824e7ee1388b3b1085",
        "started_at": "2026-09-27T10:43:32Z",
        "ended_at": "2026-09-27T10:45:14Z",
        "outcome": "UNKNOWN",
        "duration_seconds": 101.686,
        "model": "gpt-5.6-terra",
        "reasoning": "medium",
        "codex_project": "/home/daniele/.local/share/codex-github-autosync/worktrees/gernalix_grindr-favorites-monitor/625582",
        "chat_title": null,
        "branch": null,
        "commit_before": null,
        "commit_after": null,
        "tool_call_count": 9,
        "input_tokens": 31944,
        "cached_input_tokens": 31488,
        "uncached_input_tokens": 456,
        "output_tokens": 422,
        "reasoning_output_tokens": 253,
        "total_tokens": 32366,
        "source": "codex-usage",
        "recorded_at": "2026-09-27T10:46:54Z"
      },
      {
        "execution_id": 467,
        "prompt_id": "625582",
        "cycle_key": "11b7fc03fdc08131f4e65d54",
        "materialization_sha256": "8707ba5e9797ab8e1305546235bc7fd46578343ebaada1828093df74a6a39317",
        "started_at": "2026-09-27T10:43:26Z",
        "ended_at": "2026-09-27T10:49:13Z",
        "outcome": "BLOCKED",
        "duration_seconds": 346.956,
        "model": "gpt-5.6-terra",
        "reasoning": "medium",
        "codex_project": "/home/daniele/.local/share/codex-github-autosync/worktrees/gernalix_grindr-favorites-monitor/625582",
        "chat_title": null,
        "branch": null,
        "commit_before": null,
        "commit_after": null,
        "tool_call_count": 21,
        "input_tokens": 67246,
        "cached_input_tokens": 66304,
        "uncached_input_tokens": 942,
        "output_tokens": 270,
        "reasoning_output_tokens": 162,
        "total_tokens": 67516,
        "source": "codex-usage",
        "recorded_at": "2026-09-27T10:51:01Z"
      },
      {
        "execution_id": 471,
        "prompt_id": "625582",
        "cycle_key": "cd3ac7743fe4b4e61e87f07b",
        "materialization_sha256": "d2aaa71dcff6d10db851420e12bcddf83417941adc03b33162eb46dd1f9d6e05",
        "started_at": "2026-09-27T10:45:01Z",
        "ended_at": "2026-09-27T10:45:04Z",
        "outcome": "UNKNOWN",
        "duration_seconds": 3.351,
        "model": "codex-auto-review",
        "reasoning": "low",
        "codex_project": "/home/daniele/.local/share/codex-github-autosync/worktrees/gernalix_grindr-favorites-monitor/625582",
        "chat_title": null,
        "branch": null,
        "commit_before": null,
        "commit_after": null,
        "tool_call_count": 0,
        "input_tokens": 15105,
        "cached_input_tokens": 13056,
        "uncached_input_tokens": 2049,
        "output_tokens": 98,
        "reasoning_output_tokens": 35,
        "total_tokens": 15203,
        "source": "codex-usage",
        "recorded_at": "2026-09-27T10:59:08Z"
      },
      {
        "execution_id": 497,
        "prompt_id": "625582",
        "cycle_key": "9369690d29ca365fb7f179b5",
        "materialization_sha256": "94db15e5ea5e3775addfb8b32ff650e5da9a1637e675a3bfb2edf81d6c645377",
        "started_at": "2026-09-28T03:06:58Z",
        "ended_at": "2026-09-28T03:08:12Z",
        "outcome": "BLOCKED",
        "duration_seconds": 74.653,
        "model": "gpt-5.6-terra",
        "reasoning": "medium",
        "codex_project": "/home/daniele/.local/share/codex-github-autosync/worktrees/gernalix_grindr-favorites-monitor/625582",
        "chat_title": null,
        "branch": null,
        "commit_before": null,
        "commit_after": null,
        "tool_call_count": 3,
        "input_tokens": 73181,
        "cached_input_tokens": 72448,
        "uncached_input_tokens": 733,
        "output_tokens": 99,
        "reasoning_output_tokens": 46,
        "total_tokens": 73280,
        "source": "codex-usage",
        "recorded_at": "2026-09-28T03:09:53Z"
      },
      {
        "execution_id": 518,
        "prompt_id": "625582",
        "cycle_key": "b27b92e996d238f9bc8390f6",
        "materialization_sha256": "9cb09b1ba82ca5cf7c3dc8ef4d23dbea761a95c72d752daa155fc309048777d0",
        "started_at": "2026-09-29T09:32:06Z",
        "ended_at": "2026-09-29T09:32:14Z",
        "outcome": "UNKNOWN",
        "duration_seconds": 7.908,
        "model": "codex-auto-review",
        "reasoning": "low",
        "codex_project": "/home/daniele/.local/share/c2-supervisor/worktrees/roadmap-batch-reconciliation-20260928",
        "chat_title": null,
        "branch": null,
        "commit_before": null,
        "commit_after": null,
        "tool_call_count": 0,
        "input_tokens": 31753,
        "cached_input_tokens": 28416,
        "uncached_input_tokens": 3337,
        "output_tokens": 74,
        "reasoning_output_tokens": 24,
        "total_tokens": 31827,
        "source": "codex-usage",
        "recorded_at": "2026-09-29T09:33:46Z"
      },
      {
        "execution_id": 519,
        "prompt_id": "625582",
        "cycle_key": "9d964ba994213183c6339127",
        "materialization_sha256": "81b029b301f7a35cd884f7bb8ab1baa26e96221357707e7eca5cae9b262a8b5d",
        "started_at": "2026-09-29T09:34:02Z",
        "ended_at": "2026-09-29T09:34:08Z",
        "outcome": "UNKNOWN",
        "duration_seconds": 6.198,
        "model": "codex-auto-review",
        "reasoning": "low",
        "codex_project": "/home/daniele/.local/share/c2-supervisor/worktrees/roadmap-batch-reconciliation-20260928",
        "chat_title": null,
        "branch": null,
        "commit_before": null,
        "commit_after": null,
        "tool_call_count": 0,
        "input_tokens": 30335,
        "cached_input_tokens": 7936,
        "uncached_input_tokens": 22399,
        "output_tokens": 111,
        "reasoning_output_tokens": 59,
        "total_tokens": 30446,
        "source": "codex-usage",
        "recorded_at": "2026-09-29T09:36:04Z"
      },
      {
        "execution_id": 520,
        "prompt_id": "625582",
        "cycle_key": "8745ecab1f418b35a7695ce6",
        "materialization_sha256": "8a2b1ccf387c7e81b213a9e0884d9ae229e88e0d158386170a288becdd1fb4e9",
        "started_at": "2026-09-29T09:35:00Z",
        "ended_at": "2026-09-29T09:35:07Z",
        "outcome": "UNKNOWN",
        "duration_seconds": 7.099,
        "model": "codex-auto-review",
        "reasoning": "low",
        "codex_project": "/home/daniele/.local/share/c2-supervisor/worktrees/roadmap-batch-reconciliation-20260928",
        "chat_title": null,
        "branch": null,
        "commit_before": null,
        "commit_after": null,
        "tool_call_count": 0,
        "input_tokens": 29127,
        "cached_input_tokens": 7936,
        "uncached_input_tokens": 21191,
        "output_tokens": 124,
        "reasoning_output_tokens": 106,
        "total_tokens": 29251,
        "source": "codex-usage",
        "recorded_at": "2026-09-29T09:38:41Z"
      },
      {
        "execution_id": 521,
        "prompt_id": "625582",
        "cycle_key": "ce6c7b133730809e71ab8c8b",
        "materialization_sha256": "16acad2f205387f50187a17e0fb415afd378b166e5d877273b92ad24b17f4313",
        "started_at": "2026-09-29T09:36:53Z",
        "ended_at": "2026-09-29T09:36:59Z",
        "outcome": "UNKNOWN",
        "duration_seconds": 5.605,
        "model": "codex-auto-review",
        "reasoning": "low",
        "codex_project": "/home/daniele/.local/share/c2-supervisor/worktrees/roadmap-batch-reconciliation-20260928",
        "chat_title": null,
        "branch": null,
        "commit_before": null,
        "commit_after": null,
        "tool_call_count": 0,
        "input_tokens": 29368,
        "cached_input_tokens": 7936,
        "uncached_input_tokens": 21432,
        "output_tokens": 87,
        "reasoning_output_tokens": 69,
        "total_tokens": 29455,
        "source": "codex-usage",
        "recorded_at": "2026-09-29T09:39:54Z"
      },
      {
        "execution_id": 522,
        "prompt_id": "625582",
        "cycle_key": "caeeb3a1ced876cd25bfb84a",
        "materialization_sha256": "5f66e204e8066d323f48145ae5b47ad8c6235d225903177e8277c3ea2b4024d6",
        "started_at": "2026-09-29T09:39:31Z",
        "ended_at": "2026-09-29T09:39:37Z",
        "outcome": "UNKNOWN",
        "duration_seconds": 6.108,
        "model": "codex-auto-review",
        "reasoning": "low",
        "codex_project": "/home/daniele/.local/share/c2-supervisor/worktrees/roadmap-batch-reconciliation-20260928",
        "chat_title": null,
        "branch": null,
        "commit_before": null,
        "commit_after": null,
        "tool_call_count": 0,
        "input_tokens": 29568,
        "cached_input_tokens": 4864,
        "uncached_input_tokens": 24704,
        "output_tokens": 175,
        "reasoning_output_tokens": 116,
        "total_tokens": 29743,
        "source": "codex-usage",
        "recorded_at": "2026-09-29T09:42:42Z"
      }
    ],
    "status_history": [
      {
        "history_id": 1048,
        "prompt_id": "625582",
        "old_status": null,
        "new_status": "pending",
        "changed_at": "2026-09-27T10:33:05Z",
        "actor": "c2-intake",
        "note": "work item materialized for Codex"
      },
      {
        "history_id": 1055,
        "prompt_id": "625582",
        "old_status": "pending",
        "new_status": "running",
        "changed_at": "2026-09-27T10:34:23Z",
        "actor": "codex",
        "note": "launch-claim:roadmap_start"
      },
      {
        "history_id": 1058,
        "prompt_id": "625582",
        "old_status": "running",
        "new_status": "blocked",
        "changed_at": "2026-09-27T10:49:13Z",
        "actor": "codex",
        "note": "terminal:roadmap_result:BLOCKED"
      },
      {
        "history_id": 1083,
        "prompt_id": "625582",
        "old_status": "blocked",
        "new_status": "waiting",
        "changed_at": "2026-09-27T22:23:04.384167Z",
        "actor": "c2-blocked-reconcile",
        "note": "Prepare exact bounded implementation and dispatch through C2."
      }
    ],
    "work_item_tags": [
      {
        "work_item_id": "wi:cc78ff4dcaf942f998d821fb48826d23",
        "tag": "grindr:favorites-monitor"
      },
      {
        "work_item_id": "wi:cc78ff4dcaf942f998d821fb48826d23",
        "tag": "ux:media"
      },
      {
        "work_item_id": "wi:cc78ff4dcaf942f998d821fb48826d23",
        "tag": "source:issue-inbox"
      },
      {
        "work_item_id": "wi:cc78ff4dcaf942f998d821fb48826d23",
        "tag": "regression"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [
      {
        "from_work_item_id": "wi:cc78ff4dcaf942f998d821fb48826d23",
        "to_work_item_id": "wi:20eed8f493a645edb9c6692cb4ed32fd",
        "relation_type": "regression_of",
        "created_at": "2026-09-27T08:41:47Z",
        "actor": "c2-issue-triage",
        "note": "issue:f567f7d97ff64f6f92366f4734750fdd"
      }
    ],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 598,
        "work_item_id": "wi:cc78ff4dcaf942f998d821fb48826d23",
        "evidence_kind": "issue_inbox",
        "label": "issue:f567f7d97ff64f6f92366f4734750fdd",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Grindr scraper UX: da qualunque foto profilo scaricata e aperta dalla cartella Downloads deve essere possibile risalire al relativo profile_id con il minor numero di clic possibile. Soluzione preferita: naming deterministico che includa chiaramente il profile_id nel nome file (idealmente visibile direttamente nel titolo del viewer, quindi 0 clic); aggiungere anche profile_id nei metadati EXIF/XMP come fallback. Evitare lookup manuali nel DB o UI separate. Ogni immagine deve mappare in modo univoco e stabile a un solo profile_id; considerare anche backfill/rinomina delle foto già scaricate se sicuro.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:f567f7d97ff64f6f92366f4734750fdd\", \"observed_at_ms\": 1790496049990, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"grindr-favorites-monitor\"}",
        "created_at": "2026-09-27T08:41:47Z"
      },
      {
        "evidence_id": 623,
        "work_item_id": "wi:cc78ff4dcaf942f998d821fb48826d23",
        "evidence_kind": "issue_inbox",
        "label": "issue:0b87c681f6534929a130f18cb5e4c6cd",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Grindr scraper / Datasette UX: aggiungere uno script/azione Nautilus che, da una foto scaricata, estragga il profile_id dal filename e apra direttamente in Datasette il profilo corrispondente; modificare inoltre il repo dello scraper affinché i filename/titoli delle foto siano sempre standardizzati e includano il profile_id, oltre agli eventuali altri metadati necessari agli altri flussi, mantenendo una convenzione di naming stabile e coerente.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:0b87c681f6534929a130f18cb5e4c6cd\", \"observed_at_ms\": 1790504397356, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"grindr-favorites-monitor\"}",
        "created_at": "2026-09-27T10:27:49Z"
      },
      {
        "evidence_id": 1185,
        "work_item_id": "wi:cc78ff4dcaf942f998d821fb48826d23",
        "evidence_kind": "blocked_reconcile",
        "label": "No current blocker or terminal receipt is recorded; prior download task is completed and scoped photo-ID work remains va",
        "uri": null,
        "value_json": "\"No current blocker or terminal receipt is recorded; prior download task is completed and scoped photo-ID work remains valid.\"",
        "created_at": "2026-09-27T22:23:04.384167Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:0b87c681f6534929a130f18cb5e4c6cd",
        "work_item_id": "wi:cc78ff4dcaf942f998d821fb48826d23",
        "role": "matched",
        "created_at": "2026-09-27T10:19:57Z"
      },
      {
        "issue_id": "issue:f567f7d97ff64f6f92366f4734750fdd",
        "work_item_id": "wi:cc78ff4dcaf942f998d821fb48826d23",
        "role": "decision",
        "created_at": "2026-09-27T08:00:49Z"
      },
      {
        "issue_id": "issue:0b87c681f6534929a130f18cb5e4c6cd",
        "work_item_id": "wi:cc78ff4dcaf942f998d821fb48826d23",
        "role": "decision",
        "created_at": "2026-09-27T10:19:57Z"
      }
    ]
  }
]
```
