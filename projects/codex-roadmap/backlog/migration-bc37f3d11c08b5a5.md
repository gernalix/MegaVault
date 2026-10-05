# Distribuisci gli ultimi fix della prompt infrastructure

<!-- migration-bc37f3d11c08b5a5 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Merged duplicate/complementary observations and subtasks; every original requirement retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `prompt:302284`, `state:gate:008c5ecbb292e8c246fc`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Distribuisci gli ultimi fix della prompt infrastructure

status: blocked

current_action: Terminalize as BLOCKED: acceptance is not fully met because target-session prompt_costs cannot be regenerated from the archived raw source currently available; repo-integrator also reports an unrelated failed-check PR.

next_action: Wait for valid source evidence and a green guarded integration gate before resuming focused cost readback.

blocker: The successor goal-cycle raw/normalized archive evidence remains absent and adb-device-keeper PR #2 has failed required checks.

### Resolve blocker: Raw/normalized archive source available for the target session does not contain the successor goal cycles needed by `codex_task_costs.py`; a safe isolated analysis returns only the historical 624831 row. Repo-integrator also reports unrelated PR #2 checks-failed for `gernalix/adb-device-keeper`.

status: blocked

next_action: Resolve the source evidence gap for 302284, then reconcile this derived gate.

blocker: Derived gate for prompt302284 still lacks successor goal-cycle archive evidence; parent remains blocked.

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "51",
      "reason": "canonical repository identity",
      "related_projects": [
        "51"
      ]
    },
    "source": {
      "work_item_id": "prompt:302284",
      "parent_id": null,
      "kind": "task",
      "title": "Distribuisci gli ultimi fix della prompt infrastructure",
      "objective": null,
      "acceptance_json": null,
      "status": "blocked",
      "executor_policy": "codex",
      "sort_order": 9,
      "current_action": "Terminalize as BLOCKED: acceptance is not fully met because target-session prompt_costs cannot be regenerated from the archived raw source currently available; repo-integrator also reports an unrelated failed-check PR.",
      "next_action": "Wait for valid source evidence and a green guarded integration gate before resuming focused cost readback.",
      "blocker": "The successor goal-cycle raw/normalized archive evidence remains absent and adb-device-keeper PR #2 has failed required checks.",
      "project_id": null,
      "project_name": "Prompt infrastructure / Fedora runtime",
      "repo": "gernalix/codex-roadmap",
      "prompt_id": "302284",
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "prompt",
      "source_ref": "302284",
      "created_at": "2026-09-24T10:04:07Z",
      "updated_at": "2026-09-27T22:23:04.086459Z"
    },
    "prompt_metadata": [
      {
        "prompt_id": "302284",
        "slug": "prompt-infrastructure-final-runtime-activation-v1",
        "chat_guidance": "Nuova chat Codex breve; un solo pass Fedora sui runtime già implementati",
        "prompt_type": "Prompt",
        "model": "GPT-6 Luna",
        "reasoning": "low",
        "megavault_mode": "FAST",
        "campaign_id": null,
        "explanation": "Aggiorna in un solo passaggio i servizi locali della roadmap, Workflowy, telemetria Codex e switcher, verificando anche i nuovi colori e la correzione dei costi/attribuzioni.",
        "current_path": "falliti/prompt-infrastructure-final-runtime-activation-v1.md",
        "materialization_sha256": "9d53b0f01007f2340e4102573a0d59b4e039f196d5f7692d127922893e60f576",
        "created_at": "2026-09-24T10:04:07Z",
        "updated_at": "2026-09-25T10:24:29Z"
      }
    ],
    "prompt_materializations": [
      {
        "prompt_id": "302284",
        "body": "PROMPT_ID=302284\n\n# Goal\nDistribuisci sul Fedora reale in UN SOLO passaggio bounded gli ultimi fix già presenti sui main remoti della prompt infrastructure: lifecycle roadmap consolidato, Workflowy aggiornato, publisher Codex con attribuzione goal corretta e styling Workflowy/CCS. Nessun redesign e nessun audit generale.\n\n# Precondizione\n- Esegui solo dopo 222733 PASS: il heartbeat runaway di 788315 deve essere spento prima di toccare il runtime ChatGPTExporter/prompt infrastructure.\n\n# Baseline remote minime già verificate\n- codex-roadmap: contiene il lifecycle single-writer/PBF corrente e operations/task-state; usa il main corrente.\n- github-autosync >= b47f7bd16c94afb17214a49d49637dd20dfd858b.\n- workflowy-importer >= 38df310862c3256f57391c72f781e12a09ec8d2f.\n- codex-usage-monitor >= 547e92b0c0f60b02e515cb8293d5c6d84ea35f8b.\n- chrome-codex-switcher >= 00963e3f31939d936b614c36db1fde57a872e4c7.\n- Il vecchio 729874 è sostituito da questo task perché non deployava il nuovo codex-usage-monitor e non verificava le nuove projection/style Workflowy.\n- Non rileggere storico/MegaVault/roadmap oltre ai mismatch concreti: questo starting point è sufficiente.\n\n# Esecuzione\n1. Claim 302284.\n2. In un solo batch per repo, porta in fast-forward sicuro i checkout canonici di codex-roadmap, github-autosync, workflowy-importer, codex-usage-monitor e chrome-codex-switcher. Niente stash/reset/cleanup di dirty non correlato.\n3. Gate mirati soltanto:\n   - codex-roadmap: test PBF/lifecycle/single-writer direttamente pertinenti;\n   - github-autosync: test_repo_single_writer + test_github_autosync;\n   - workflowy-importer: tests.test_roadmap_bridge;\n   - codex-usage-monitor: tests.test_usage_publisher_regressions + tests.test_task_costs;\n   - chrome-codex-switcher: tests.test_late_bind_contract + py_compile host.\n   Se un leaf fallisce, correggi solo quel failure domain e rilancia il leaf; niente suite complete salvo impatto condiviso dimostrato.\n4. Deploy una volta usando gli entrypoint già versionati:\n   - codex-roadmap: install_live_status_systemd.py e runtime sync già esistente;\n   - github-autosync: install_systemd.py;\n   - workflowy-importer: deploy_runtime.py;\n   - codex-usage-monitor: deploy_runtime.py --skip-fetch;\n   - chrome-codex-switcher: ./install.sh; non creare una seconda estensione/profilo.\n5. Readback lifecycle:\n   - roadmap live-status/sync, github-autosync/repo-integrator/watchdog, workflowy bridge/sync e codex-usage publisher timer/service devono essere enabled/active o non-failed secondo il loro tipo;\n   - una sola esecuzione roadmap sync deve terminare 0;\n   - repo_integrator.py --json una sola volta: nessun writer concorrente o falsa finalizzazione.\n6. Readback Workflowy/CCS:\n   - esegui un solo sync Workflowy;\n   - verifica su un nodo Goal e uno Prompt che la projection contenga riga /goal solo per Goal e riga dedicata model/reasoning;\n   - l'estensione installata deve contenere ct-roadmap-model viola+bold+underline e ct-roadmap-goal ciano; se una normale tab Workflowy è già disponibile, fai un solo readback live del class assignment. Non aprire chrome-extension:// e non creare polling.\n7. Readback codex-usage:\n   - esegui una sola run publisher bounded;\n   - verifica la sessione 01a0ca04-1001-7650-8c7a-f8e74aecf3d4: i cicli del goal successore devono risultare attribuiti a 613102 quando roadmap_start ha dichiarato prompt_id=613102, e non restare duplicati sotto prompts/624831/cycles;\n   - esegui/rigenera task_costs e usa prompt_costs/delta per il costo per PROMPT_ID; non sommare ingenuamente total_tokens cumulativi di goal;\n   - una seconda publisher run è ammessa SOLO come fast-path noop_unchanged_sources, non come polling.\n8. Verifica che codex-usage resti telemetria passiva e Workflowy lifecycle read-only.\n9. Dopo PASS finalizza e STOP. Non attendere CI/merge in modello e non creare follow-up cosmetici.\n\n# Acceptance\nPASS solo se i cinque runtime corrispondono ai main minimi, test mirati PASS, lifecycle single-writer è sano, Workflowy mostra i nuovi metadata/style, il publisher ha corretto/backfillato l'attribuzione 613102/624831 e prompt_costs è la base del confronto costi.\n\n# Report\nMassimo 9 righe: RESULT, ROADMAP_AUTOSYNC, WORKFLOWY, CCS_STYLE, CODEX_USAGE_ATTRIBUTION, PROMPT_COSTS, SYSTEMD, COMMITS_IF_ANY, BLOCKER.",
        "sha256": "9d53b0f01007f2340e4102573a0d59b4e039f196d5f7692d127922893e60f576",
        "created_at": "2026-09-24T10:04:07Z",
        "actor": "chatgpt"
      }
    ],
    "analyses": [],
    "executions": [],
    "status_history": [
      {
        "history_id": 810,
        "prompt_id": "302284",
        "old_status": null,
        "new_status": "pending",
        "changed_at": "2026-09-24T10:04:07Z",
        "actor": "chatgpt",
        "note": "registered"
      },
      {
        "history_id": 821,
        "prompt_id": "302284",
        "old_status": "pending",
        "new_status": "running",
        "changed_at": "2026-09-24T11:28:50Z",
        "actor": "codex",
        "note": "launch-claim:roadmap_start"
      },
      {
        "history_id": 841,
        "prompt_id": "302284",
        "old_status": "running",
        "new_status": "blocked",
        "changed_at": "2026-09-25T10:24:29Z",
        "actor": "codex",
        "note": "terminal:roadmap_result:BLOCKED"
      }
    ],
    "work_item_tags": [],
    "work_item_dependencies": [
      {
        "work_item_id": "prompt:302284",
        "depends_on_work_item_id": "prompt:222733",
        "required": 1,
        "note": "Prima spegni il heartbeat runaway di ChatGPTExporter/Codex."
      },
      {
        "work_item_id": "prompt:641903",
        "depends_on_work_item_id": "prompt:302284",
        "required": 1,
        "note": "Run the final CCS live proof only after the current CCS/Workflowy runtime is deployed by 302284."
      },
      {
        "work_item_id": "prompt:896074",
        "depends_on_work_item_id": "prompt:302284",
        "required": 1,
        "note": "Eseguire solo dopo il deploy/readback dell'infrastruttura corrente."
      }
    ],
    "work_item_relations": [
      {
        "from_work_item_id": "prompt:729874",
        "to_work_item_id": "prompt:302284",
        "relation_type": "replacement",
        "created_at": "2026-09-24T10:04:07Z",
        "actor": "chatgpt",
        "note": "Sostituisce il vecchio deploy lifecycle con il pass aggiornato che include codex-usage attribution e Workflowy/CCS styling."
      },
      {
        "from_work_item_id": "state:step:11046c379b7d2a9a0a54",
        "to_work_item_id": "prompt:302284",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:06Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:032e1357d145bd5eeb06",
        "to_work_item_id": "prompt:302284",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:06Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:fb24db267874c3211207",
        "to_work_item_id": "prompt:302284",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:06Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:c7e52b231a4a102e011c",
        "to_work_item_id": "prompt:302284",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:06Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:79218ce9025062e854bd",
        "to_work_item_id": "prompt:302284",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:06Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:10bbb6a275529b86bf07",
        "to_work_item_id": "prompt:302284",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:51:16Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:6810f4deddeae23c390f",
        "to_work_item_id": "prompt:302284",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:51:16Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:phase:9a29a9cc7fcaffc446ea",
        "to_work_item_id": "prompt:302284",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:51:16Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:d8b40dc99d0d0789d6f8",
        "to_work_item_id": "prompt:302284",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:51:16Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      }
    ],
    "work_item_checkpoints": [
      {
        "checkpoint_id": 2,
        "work_item_id": "prompt:302284",
        "source_file": "302284.md",
        "source_commit": "52bea96d02f55fac91cea210cf2e370b5963cc4f",
        "source_sha256": "fd3dbd1a6231a0fcbe262e430d1498ca338227c8f2e3977ad207d8dc532d7f81",
        "objective": "Finish the bounded Fedora runtime activation for the prompt infrastructure: roadmap lifecycle, GitHub autosync/single-writer, Workflowy projection, Codex usage attribution/costs, and Chrome Codex Switcher styling/runtime.",
        "current_step": "Terminalize as BLOCKED: acceptance is not fully met because target-session prompt_costs cannot be regenerated from the archived raw source currently available; repo-integrator also reports an unrelated failed-check PR.",
        "next_action": null,
        "blocker": "pre-migration / retired: historical evidence only",
        "completed_json": "[\"Recovery of canonical state, collision check, focused codex-usage completion, regression coverage, targeted tests, and pushed checkpoint.\"]",
        "remaining_json": "[\"Target-session prompt_costs readback/backfill requires source evidence containing the successor goal cycles; repo-integrator has an unrelated failed-check PR. Acceptance is not met.\"]",
        "evidence_json": "[\"Codex-usage source commits `27cdcec` + `8a76578`; targeted cost tests 11/11 PASS; isolated archive analysis did not modify live costs; publisher state shows three 613102 cycles and no successor cycle under 624831; installed CSS class checks PASS; systemd readback PASS except repo-integrator service reports exit-code 2 for unrelated PR checks. 222733 terminal PASS was verified earlier via canonical dry-run.\"]",
        "captured_at": "2026-09-25T15:54:51Z"
      }
    ],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 30,
        "work_item_id": "prompt:302284",
        "evidence_kind": "completed",
        "label": "Recovery of canonical state, collision check, focused codex-usage completion, regression coverage, targeted tests, and pushed checkpoint.",
        "uri": "state://302284.md#completed-387e06fe9d600fd8",
        "value_json": "{\"text\": \"Recovery of canonical state, collision check, focused codex-usage completion, regression coverage, targeted tests, and pushed checkpoint.\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 31,
        "work_item_id": "prompt:302284",
        "evidence_kind": "evidence",
        "label": "Codex-usage source commits `27cdcec` + `8a76578`; targeted cost tests 11/11 PASS; isolated archive analysis did not modify live costs; publisher state shows three 613102 cycles and no successor cycle under 624831; installed CSS class checks PASS; systemd readback PASS except repo-integrator service reports exit-code 2 for unrelated PR checks. 222733 terminal PASS was verified earlier via canonical dry-run.",
        "uri": "state://302284.md#evidence-bf62f2e3da57dcf6",
        "value_json": "{\"text\": \"Codex-usage source commits `27cdcec` + `8a76578`; targeted cost tests 11/11 PASS; isolated archive analysis did not modify live costs; publisher state shows three 613102 cycles and no successor cycle under 624831; installed CSS class checks PASS; systemd readback PASS except repo-integrator service reports exit-code 2 for unrelated PR checks. 222733 terminal PASS was verified earlier via canonical dry-run.\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 1179,
        "work_item_id": "prompt:302284",
        "evidence_kind": "blocked_reconcile",
        "label": "The successor goal-cycle raw/normalized archive evidence remains absent and adb-device-keeper PR #2 has failed required ",
        "uri": null,
        "value_json": "\"The successor goal-cycle raw/normalized archive evidence remains absent and adb-device-keeper PR #2 has failed required checks.\"",
        "created_at": "2026-09-27T22:23:04.086459Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": []
  },
  {
    "routing": {
      "project": "51",
      "reason": "blocker subtask inherits explicitly identified parent project",
      "related_projects": [
        "51"
      ]
    },
    "source": {
      "work_item_id": "state:gate:008c5ecbb292e8c246fc",
      "parent_id": "prompt:302284",
      "kind": "gate",
      "title": "Resolve blocker: Raw/normalized archive source available for the target session does not contain the successor goal cycles needed by `codex_task_costs.py`; a safe isolated analysis returns only the historical 624831 row. Repo-integrator also reports unrelated PR #2 checks-failed for `gernalix/adb-device-keeper`.",
      "objective": null,
      "acceptance_json": null,
      "status": "blocked",
      "executor_policy": "auto",
      "sort_order": 1202,
      "current_action": null,
      "next_action": "Resolve the source evidence gap for 302284, then reconcile this derived gate.",
      "blocker": "Derived gate for prompt302284 still lacks successor goal-cycle archive evidence; parent remains blocked.",
      "project_id": null,
      "project_name": "Prompt infrastructure / Fedora runtime",
      "repo": "gernalix/codex-roadmap",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "task_state",
      "source_ref": "302284.md#blocker",
      "created_at": "2026-09-25T15:54:51Z",
      "updated_at": "2026-09-27T22:21:39.658316Z"
    },
    "work_item_tags": [],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 1174,
        "work_item_id": "state:gate:008c5ecbb292e8c246fc",
        "evidence_kind": "blocked_reconcile",
        "label": "Derived gate for prompt302284 still lacks successor goal-cycle archive evidence; parent remains blocked.",
        "uri": null,
        "value_json": "\"Derived gate for prompt302284 still lacks successor goal-cycle archive evidence; parent remains blocked.\"",
        "created_at": "2026-09-27T22:21:39.658316Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": []
  }
]
```
