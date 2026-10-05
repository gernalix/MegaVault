# Ripristinare la schermata completa di creazione Since When

<!-- migration-a3edc42d21dff92c -->

Migrated project backlog. Project: **personalhub**; project_id: 49.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Merged duplicate/complementary observations and subtasks; every original requirement retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 49.

Provenance: `wi:8740f8fd8e744642b01a3abc7055172e`, `wi:4ff68fd6a78a4953ad997a856996884f`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Ripristinare la schermata completa di creazione Since When

Ripristinare la schermata di creazione Since When disponibile quando la funzione apparteneva a Timer, mantenendo la tile autonoma in Home e il sistema tag indipendente. Eliminare ogni dipendenza residua da Timer e ripristinare almeno la selezione dell’ora.

Acceptance:

- La tile autonoma Since When in PersonalHub resta il punto di ingresso e la creazione/modifica non dipende da UI o lifecycle di Timer.
- La schermata di creazione/modifica ripristina i controlli del precedente editor Since When già supportati dal modello dati: titolo, descrizione, data+ora di inizio, fine opzionale con data+ora, colore, unità di visualizzazione e tag Since When.
- La selezione dell’ora viene persistita esattamente: creare o modificare un contatore con ora non a mezzanotte e riaprirlo restituisce lo stesso timestamp locale.
- Fine opzionale, colore, unità e tag fanno round-trip nei campi canonici esistenti senza introdurre dipendenze da Timer; i tag restano nello scope Since When indipendente.
- I contatori esistenti e la provenance source_entity_* restano leggibili/modificabili senza perdita di dati e la migrazione legacy continua a funzionare.
- Test mirati PASS e verifica UI reale del flusso create → save → reopen/edit → readback PASS; integrazione Git canonica completata prima del PASS del batch.

status: running

current_action: Pre-dispatch Symphony claim released: Retry same real batch after fixing canonical repository casing; prior worker failed before tracker/binding publication.

### PersonalHub — Ripristino creazione Since When

Ripristinare nell’app PersonalHub autonoma la schermata completa di creazione/modifica Since When già disponibile nel precedente editor Timer, usando il modello Since When canonico esistente e senza reintrodurre dipendenze da Timer.

Acceptance:

- La tile autonoma Since When in PersonalHub resta il punto di ingresso e la creazione/modifica non dipende da UI o lifecycle di Timer.
- La schermata di creazione/modifica ripristina i controlli del precedente editor Since When già supportati dal modello dati: titolo, descrizione, data+ora di inizio, fine opzionale con data+ora, colore, unità di visualizzazione e tag Since When.
- La selezione dell’ora viene persistita esattamente: creare o modificare un contatore con ora non a mezzanotte e riaprirlo restituisce lo stesso timestamp locale.
- Fine opzionale, colore, unità e tag fanno round-trip nei campi canonici esistenti senza introdurre dipendenze da Timer; i tag restano nello scope Since When indipendente.
- I contatori esistenti e la provenance source_entity_* restano leggibili/modificabili senza perdita di dati e la migrazione legacy continua a funzionare.
- Test mirati PASS e verifica UI reale del flusso create → save → reopen/edit → readback PASS; integrazione Git canonica completata prima del PASS del batch.

status: pending

current_action: Execute the existing Since When regression child through normal C3 lifecycle.

next_action: Prepare and execute the existing child work item; integrate and verify UI before batch PASS.

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "49",
      "reason": "canonical MegaVault project_id",
      "related_projects": [
        "49"
      ]
    },
    "source": {
      "work_item_id": "wi:8740f8fd8e744642b01a3abc7055172e",
      "parent_id": "wi:4ff68fd6a78a4953ad997a856996884f",
      "kind": "task",
      "title": "Ripristinare la schermata completa di creazione Since When",
      "objective": "Ripristinare la schermata di creazione Since When disponibile quando la funzione apparteneva a Timer, mantenendo la tile autonoma in Home e il sistema tag indipendente. Eliminare ogni dipendenza residua da Timer e ripristinare almeno la selezione dell’ora.",
      "acceptance_json": "[\"La tile autonoma Since When in PersonalHub resta il punto di ingresso e la creazione/modifica non dipende da UI o lifecycle di Timer.\", \"La schermata di creazione/modifica ripristina i controlli del precedente editor Since When già supportati dal modello dati: titolo, descrizione, data+ora di inizio, fine opzionale con data+ora, colore, unità di visualizzazione e tag Since When.\", \"La selezione dell’ora viene persistita esattamente: creare o modificare un contatore con ora non a mezzanotte e riaprirlo restituisce lo stesso timestamp locale.\", \"Fine opzionale, colore, unità e tag fanno round-trip nei campi canonici esistenti senza introdurre dipendenze da Timer; i tag restano nello scope Since When indipendente.\", \"I contatori esistenti e la provenance source_entity_* restano leggibili/modificabili senza perdita di dati e la migrazione legacy continua a funzionare.\", \"Test mirati PASS e verifica UI reale del flusso create → save → reopen/edit → readback PASS; integrazione Git canonica completata prima del PASS del batch.\"]",
      "status": "running",
      "executor_policy": "codex",
      "sort_order": -15000,
      "current_action": "Pre-dispatch Symphony claim released: Retry same real batch after fixing canonical repository casing; prior worker failed before tracker/binding publication.",
      "next_action": null,
      "blocker": null,
      "project_id": "49",
      "project_name": "PersonalHub",
      "repo": "gernalix/PersonalHub",
      "prompt_id": "281063",
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-30T10:16:35Z",
      "updated_at": "2026-10-02T23:34:32Z"
    },
    "prompt_metadata": [
      {
        "prompt_id": "281063",
        "slug": "ripristinare-la-schermata-completa-di-creazione--281063",
        "chat_guidance": null,
        "prompt_type": "Prompt",
        "model": "gpt-5.6-sol",
        "reasoning": "medium",
        "megavault_mode": null,
        "campaign_id": null,
        "explanation": "",
        "current_path": "prompts/ripristinare-la-schermata-completa-di-creazione--281063.md",
        "materialization_sha256": "1791b9acb7d4af1e76c762dbadcdb6c525a198b2867816e73613ef6f3865ef5b",
        "created_at": "2026-10-02T23:23:07Z",
        "updated_at": "2026-10-02T23:23:07Z"
      }
    ],
    "prompt_materializations": [
      {
        "prompt_id": "281063",
        "body": "PROMPT_ID=281063\n\n# Ripristinare la schermata completa di creazione Since When\n\n## Objective\nRipristinare la schermata di creazione Since When disponibile quando la funzione apparteneva a Timer, mantenendo la tile autonoma in Home e il sistema tag indipendente. Eliminare ogni dipendenza residua da Timer e ripristinare almeno la selezione dell’ora.\n\n## Acceptance criteria\n- La tile autonoma Since When in PersonalHub resta il punto di ingresso e la creazione/modifica non dipende da UI o lifecycle di Timer.\n- La schermata di creazione/modifica ripristina i controlli del precedente editor Since When già supportati dal modello dati: titolo, descrizione, data+ora di inizio, fine opzionale con data+ora, colore, unità di visualizzazione e tag Since When.\n- La selezione dell’ora viene persistita esattamente: creare o modificare un contatore con ora non a mezzanotte e riaprirlo restituisce lo stesso timestamp locale.\n- Fine opzionale, colore, unità e tag fanno round-trip nei campi canonici esistenti senza introdurre dipendenze da Timer; i tag restano nello scope Since When indipendente.\n- I contatori esistenti e la provenance source_entity_* restano leggibili/modificabili senza perdita di dati e la migrazione legacy continua a funzionare.\n- Test mirati PASS e verifica UI reale del flusso create → save → reopen/edit → readback PASS; integrazione Git canonica completata prima del PASS del batch.\n\n## Next action\nRestore the complete standalone Since When editor, test persistence/UI, integrate through canonical Git lifecycle.\n",
        "sha256": "1791b9acb7d4af1e76c762dbadcdb6c525a198b2867816e73613ef6f3865ef5b",
        "created_at": "2026-10-02T23:23:07Z",
        "actor": "c2-intake"
      }
    ],
    "analyses": [],
    "executions": [],
    "status_history": [
      {
        "history_id": 1140,
        "prompt_id": "281063",
        "old_status": null,
        "new_status": "pending",
        "changed_at": "2026-10-02T23:23:07Z",
        "actor": "c2-intake",
        "note": "work item materialized for Codex"
      },
      {
        "history_id": 1143,
        "prompt_id": "281063",
        "old_status": "pending",
        "new_status": "running",
        "changed_at": "2026-10-02T23:29:22Z",
        "actor": "c2-scheduler",
        "note": null
      },
      {
        "history_id": 1144,
        "prompt_id": "281063",
        "old_status": "pending",
        "new_status": "running",
        "changed_at": "2026-10-02T23:34:32Z",
        "actor": "c2-scheduler",
        "note": null
      }
    ],
    "work_item_tags": [
      {
        "work_item_id": "wi:8740f8fd8e744642b01a3abc7055172e",
        "tag": "source:issue-inbox"
      },
      {
        "work_item_id": "wi:8740f8fd8e744642b01a3abc7055172e",
        "tag": "regression"
      },
      {
        "work_item_id": "wi:8740f8fd8e744642b01a3abc7055172e",
        "tag": "batch-child"
      },
      {
        "work_item_id": "wi:8740f8fd8e744642b01a3abc7055172e",
        "tag": "canary:real-execution"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [
      {
        "from_work_item_id": "wi:8740f8fd8e744642b01a3abc7055172e",
        "to_work_item_id": "prompt:822595",
        "relation_type": "regression_of",
        "created_at": "2026-09-30T10:16:35Z",
        "actor": "c2-issue-triage",
        "note": "issue:38f706a9aa2741199ef79efa505d7ff3"
      }
    ],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2151,
        "work_item_id": "wi:8740f8fd8e744642b01a3abc7055172e",
        "evidence_kind": "issue_inbox",
        "label": "issue:38f706a9aa2741199ef79efa505d7ff3",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Ripristinare la stessa schermata di creazione di \\\"Since when\\\" usata quando il modulo era ancora parte di Timer, mantenendo però la tile autonoma nella Home e il sistema di tag indipendente. Non deve rimanere alcuna dipendenza residua da Timer. La nuova schermata è troppo limitata, fino al punto di non consentire nemmeno la selezione dell'ora.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:38f706a9aa2741199ef79efa505d7ff3\", \"observed_at_ms\": 1790711499565, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T10:16:35Z"
      },
      {
        "evidence_id": 2589,
        "work_item_id": "wi:8740f8fd8e744642b01a3abc7055172e",
        "evidence_kind": "classification",
        "label": "Original promoted issue issue:38f706a9aa2741199ef79efa505d7ff3 requests restoring the previous Since When creation scree",
        "uri": null,
        "value_json": "\"Original promoted issue issue:38f706a9aa2741199ef79efa505d7ff3 requests restoring the previous Since When creation screen while keeping the standalone Home tile and independent tags.\"",
        "created_at": "2026-10-02T23:20:01Z"
      },
      {
        "evidence_id": 2590,
        "work_item_id": "wi:8740f8fd8e744642b01a3abc7055172e",
        "evidence_kind": "classification",
        "label": "Current SinceWhenScreen CounterEditorDialog exposes title/description and DatePicker only; canonical SinceWhenCounterEnt",
        "uri": null,
        "value_json": "\"Current SinceWhenScreen CounterEditorDialog exposes title/description and DatePicker only; canonical SinceWhenCounterEntity already stores end_timestamp, color_argb, display_units_json and legacy_tag_ids_json, while the previous SinceWhenLifePeriodEditorDialog provides date+time, optional end, color, units and tags.\"",
        "created_at": "2026-10-02T23:20:01Z"
      },
      {
        "evidence_id": 2591,
        "work_item_id": "wi:8740f8fd8e744642b01a3abc7055172e",
        "evidence_kind": "reparent",
        "label": "<root>->wi:4ff68fd6a78a4953ad997a856996884f",
        "uri": null,
        "value_json": "{\"actor\": \"chatgpt-c3-real-batch-pilot\", \"evidence\": \"User explicitly requested switching C3 operation to a first real non-meta batch; this existing Since When regression is the sole implementation child of the canonical PersonalHub batch.\", \"from_parent_id\": null, \"to_parent_id\": \"wi:4ff68fd6a78a4953ad997a856996884f\"}",
        "created_at": "2026-10-02T23:20:01Z"
      }
    ],
    "work_item_runs": [
      {
        "run_id": "73fc69fd43e94fce94b87dc85b1f0ff8",
        "work_item_id": "wi:8740f8fd8e744642b01a3abc7055172e",
        "event_key": "c2-schedule-3e1256c60f110740fa2c2ba1c508b051",
        "attempt": 1,
        "executor": "symphony",
        "state": "failed",
        "lease_until": 1790983882.4472086,
        "worker_ref": "c3-run:73fc69fd43e94fce94b87dc85b1f0ff8",
        "checkpoint_commit": null,
        "metadata_json": "{\"activity\": \"coding\", \"command_json\": null, \"executor\": \"symphony\", \"goal_mode\": 0, \"max_attempts\": 3, \"model\": \"gpt-5.6-sol\", \"model_id\": \"gpt-5.6-sol\", \"project_url\": null, \"prompt_id\": \"281063\", \"reasoning\": \"medium\", \"reasoning_effort\": \"medium\", \"repo\": \"gernalix/personalhub\", \"resources_json\": \"[]\", \"symphony_route\": {\"mode\": \"production\", \"source_repos\": [\"gernalix/codex-roadmap\", \"gernalix/personalhub\"], \"tracker_repo\": \"gernalix/c3-symphony\"}, \"work_item_id\": \"wi:8740f8fd8e744642b01a3abc7055172e\", \"worktree\": \"/home/daniele/.local/share/codex-github-autosync/worktrees/gernalix_PersonalHub/281063\"}",
        "created_at": 1790983762.4355757
      },
      {
        "run_id": "04d159166ae24da0bc776b108ba871db",
        "work_item_id": "wi:8740f8fd8e744642b01a3abc7055172e",
        "event_key": "c2-schedule-40c5a224f52889fb29ecdf15b22ae997",
        "attempt": 2,
        "executor": "symphony",
        "state": "running",
        "lease_until": 1790984192.4379976,
        "worker_ref": "c3-run:04d159166ae24da0bc776b108ba871db",
        "checkpoint_commit": null,
        "metadata_json": "{\"activity\": \"coding\", \"command_json\": null, \"executor\": \"symphony\", \"goal_mode\": 0, \"max_attempts\": 3, \"model\": \"gpt-5.6-sol\", \"model_id\": \"gpt-5.6-sol\", \"project_url\": null, \"prompt_id\": \"281063\", \"reasoning\": \"medium\", \"reasoning_effort\": \"medium\", \"repo\": \"gernalix/PersonalHub\", \"resources_json\": \"[]\", \"symphony_route\": {\"mode\": \"production\", \"source_repos\": [\"gernalix/PersonalHub\", \"gernalix/codex-roadmap\"], \"tracker_repo\": \"gernalix/c3-symphony\"}, \"work_item_id\": \"wi:8740f8fd8e744642b01a3abc7055172e\", \"worktree\": \"/home/daniele/.local/share/codex-github-autosync/worktrees/gernalix_PersonalHub/281063\"}",
        "created_at": 1790984072.4281003
      }
    ],
    "issue_work_item_links": [
      {
        "issue_id": "issue:38f706a9aa2741199ef79efa505d7ff3",
        "work_item_id": "wi:8740f8fd8e744642b01a3abc7055172e",
        "role": "decision",
        "created_at": "2026-09-29T19:51:39Z"
      }
    ]
  },
  {
    "routing": {
      "project": "49",
      "reason": "canonical MegaVault project_id",
      "related_projects": [
        "49"
      ]
    },
    "source": {
      "work_item_id": "wi:4ff68fd6a78a4953ad997a856996884f",
      "parent_id": null,
      "kind": "goal",
      "title": "PersonalHub — Ripristino creazione Since When",
      "objective": "Ripristinare nell’app PersonalHub autonoma la schermata completa di creazione/modifica Since When già disponibile nel precedente editor Timer, usando il modello Since When canonico esistente e senza reintrodurre dipendenze da Timer.",
      "acceptance_json": "[\"La tile autonoma Since When in PersonalHub resta il punto di ingresso e la creazione/modifica non dipende da UI o lifecycle di Timer.\", \"La schermata di creazione/modifica ripristina i controlli del precedente editor Since When già supportati dal modello dati: titolo, descrizione, data+ora di inizio, fine opzionale con data+ora, colore, unità di visualizzazione e tag Since When.\", \"La selezione dell’ora viene persistita esattamente: creare o modificare un contatore con ora non a mezzanotte e riaprirlo restituisce lo stesso timestamp locale.\", \"Fine opzionale, colore, unità e tag fanno round-trip nei campi canonici esistenti senza introdurre dipendenze da Timer; i tag restano nello scope Since When indipendente.\", \"I contatori esistenti e la provenance source_entity_* restano leggibili/modificabili senza perdita di dati e la migrazione legacy continua a funzionare.\", \"Test mirati PASS e verifica UI reale del flusso create → save → reopen/edit → readback PASS; integrazione Git canonica completata prima del PASS del batch.\"]",
      "status": "pending",
      "executor_policy": "human",
      "sort_order": -15000,
      "current_action": "Execute the existing Since When regression child through normal C3 lifecycle.",
      "next_action": "Prepare and execute the existing child work item; integrate and verify UI before batch PASS.",
      "blocker": null,
      "project_id": "49",
      "project_name": "PersonalHub",
      "repo": "gernalix/PersonalHub",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-10-02T23:20:01Z",
      "updated_at": "2026-10-02T23:20:01Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:4ff68fd6a78a4953ad997a856996884f",
        "tag": "batch"
      },
      {
        "work_item_id": "wi:4ff68fd6a78a4953ad997a856996884f",
        "tag": "canary:real-execution"
      },
      {
        "work_item_id": "wi:4ff68fd6a78a4953ad997a856996884f",
        "tag": "personalhub"
      },
      {
        "work_item_id": "wi:4ff68fd6a78a4953ad997a856996884f",
        "tag": "since-when"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [],
    "work_item_runs": [],
    "issue_work_item_links": []
  }
]
```
