# Bonificare history Logseq e attivare updater

<!-- migration-1c7d7ee0c2eaf024 -->

Migrated project backlog. Project: **logseq-updates**; project_id: 76.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 76.

Provenance: `prompt:588376`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Bonificare history Logseq e attivare updater

status: pending

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "76",
      "reason": "canonical repository identity",
      "related_projects": [
        "76"
      ]
    },
    "source": {
      "work_item_id": "prompt:588376",
      "parent_id": null,
      "kind": "task",
      "title": "Bonificare history Logseq e attivare updater",
      "objective": null,
      "acceptance_json": null,
      "status": "pending",
      "executor_policy": "codex",
      "sort_order": 7,
      "current_action": null,
      "next_action": null,
      "blocker": null,
      "project_id": null,
      "project_name": "Fedora / logseq_updates",
      "repo": "gernalix/logseq_updates",
      "prompt_id": "588376",
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "prompt",
      "source_ref": "588376",
      "created_at": "2026-09-19T01:16:05Z",
      "updated_at": "2026-09-26T16:25:56Z"
    },
    "prompt_metadata": [
      {
        "prompt_id": "588376",
        "slug": "logseq-updates-pat-safety-closure-v3",
        "chat_guidance": "Stessa chat di 357862",
        "prompt_type": "Replacement",
        "model": "GPT-5.6 Sol",
        "reasoning": "medium",
        "megavault_mode": "STRICT",
        "campaign_id": null,
        "explanation": "Resta in Waiting per un solo motivo reale: il vecchio PAT GitHub deve essere revocato manualmente. Dopo la revoca, Codex può bonificare la history e attivare/verificare l’updater senza altri prerequisiti.",
        "current_path": "prompts/logseq-updates-pat-safety-closure-v3.md",
        "materialization_sha256": "2b2033c43a869c3f091f0ac5b6e226ba462c8d41d867d4cfcfc2ff03888cb081",
        "created_at": "2026-09-19T01:16:05Z",
        "updated_at": "2026-09-26T16:25:56Z"
      }
    ],
    "prompt_materializations": [
      {
        "prompt_id": "588376",
        "body": "PROMPT_ID=588376 | PARENT_PROMPT_ID=357862 | project=logseq_updates | MegaVault=STRICT\n\n# Goal\nDopo la revoca manuale del PAT storico, bonifica la history di gernalix/logseq_updates e attiva/verifica l'updater Fedora già implementato. Non ridisegnare la feature.\n\n# Starting point\n- repo: /home/daniele/projects/logseq_updates, solo main;\n- 30e22d50a6cbc9ba1440689d13a2c092044bc686 deve essere antenato; main può essere avanzato. Verificato remoto attuale: 8d0a752321e5b44e937df602aac81d32e3720598 con CI green e solo hardening CI sopra 30e22;\n- finding storico noto: github-pat nel commit 41ff0d119e3c...; non stampare valore/fingerprint;\n- helper: ~/projects/codex-roadmap/tools/ensure_git_filter_repo.py;\n- il login/revoca PAT è prerequisito umano, non tentarlo.\n\n# Esecuzione\n1. Verifica PAT inactive prima di predisporre rewrite. active/unknown => BLOCKED e stop.\n2. Su mirror fresco fai una sola scansione gitleaks all-refs redatta, riscrivi solo il secret target, verifica tree/tag preservati e gitleaks clean, quindi force-push solo main/tag necessari. Usa ensure_git_filter_repo e cleanup.\n3. Sostituisci checkout canonico solo se clean; nessuno stash/reset distruttivo.\n4. Aggiorna solo gli output MegaVault di publication audit già previsti dal workflow esistente, senza inglobare dirty work non correlato.\n5. Esegui unittest/py_compile, installa le due user unit già presenti, enable timer, un E2E --reinstall-latest e una seconda invocation no-op. Nessun browser/web search.\n\n# Acceptance\nPASS solo con PAT inactive, history clean, solo/default main, checkout riconciliato, test PASS, timer enabled+active, E2E install PASS e seconda invocation no-op. Stop dopo PASS.\n",
        "sha256": "2b2033c43a869c3f091f0ac5b6e226ba462c8d41d867d4cfcfc2ff03888cb081",
        "created_at": "2026-09-24T08:49:53Z",
        "actor": "chatgpt"
      }
    ],
    "analyses": [],
    "executions": [],
    "status_history": [
      {
        "history_id": 381,
        "prompt_id": "588376",
        "old_status": null,
        "new_status": "pending",
        "changed_at": "2026-09-19T01:16:05Z",
        "actor": "chatgpt",
        "note": "registered"
      }
    ],
    "work_item_tags": [
      {
        "work_item_id": "prompt:588376",
        "tag": "manual-prerequisite:revoke-pat"
      },
      {
        "work_item_id": "prompt:588376",
        "tag": "manual-prerequisite:revoke-old-github-pat"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [
      {
        "from_work_item_id": "prompt:357862",
        "to_work_item_id": "prompt:588376",
        "relation_type": "replacement",
        "created_at": "2026-09-19T01:16:05Z",
        "actor": "chatgpt",
        "note": "2026-09-19 roadmap refresh against current code"
      },
      {
        "from_work_item_id": "state:step:24f1ce6380d233ad4c3e",
        "to_work_item_id": "prompt:588376",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:06Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      }
    ],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [],
    "work_item_runs": [],
    "issue_work_item_links": []
  }
]
```
