# Creare e validare il repository pubblico e-Boks scraper

<!-- migration-cd617360cdbf2bde -->

Migrated project backlog. Project: **eboks-scraper**; project_id: None.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: eboks.

Provenance: `prompt:218695`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Creare e validare il repository pubblico e-Boks scraper

status: pending

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "eboks",
      "reason": "semantic correction of source routing; original identity preserved",
      "related_projects": [
        "eboks"
      ]
    },
    "source": {
      "work_item_id": "prompt:218695",
      "parent_id": null,
      "kind": "task",
      "title": "Creare e validare il repository pubblico e-Boks scraper",
      "objective": null,
      "acceptance_json": null,
      "status": "pending",
      "executor_policy": "codex",
      "sort_order": 6,
      "current_action": null,
      "next_action": null,
      "blocker": null,
      "project_id": "23",
      "project_name": "MegaVault / e-Boks bootstrap",
      "repo": "/home/daniele/MegaVault",
      "prompt_id": "218695",
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "prompt",
      "source_ref": "218695",
      "created_at": "2026-09-21T17:52:46Z",
      "updated_at": "2026-09-26T16:25:56Z"
    },
    "prompt_metadata": [
      {
        "prompt_id": "218695",
        "slug": "eboks-scraper-bootstrap-public-repo-live-adapter",
        "chat_guidance": "Nuova chat Codex; task bootstrap bounded su repo nuovo + Chrome e-Boks reale",
        "prompt_type": "Bootstrap",
        "model": "GPT-5.6 Terra",
        "reasoning": "medium",
        "megavault_mode": "FAST",
        "campaign_id": null,
        "explanation": "Dopo 582946 va prima verificato se il download e-Boks ottenuto è già sufficiente. Solo se serve ancora uno scraper, si riusa il repository pubblico eboks-scraper già esistente ma vuoto; altrimenti questo task va cancellato.",
        "current_path": "prompts/eboks-scraper-bootstrap-public-repo-live-adapter.md",
        "materialization_sha256": "f3b960ecf7d86df2e4cc4b8bc9b3d03f57abb22dc50325524c43888f6684ae46",
        "created_at": "2026-09-21T17:52:46Z",
        "updated_at": "2026-09-26T16:25:56Z"
      }
    ],
    "prompt_materializations": [
      {
        "prompt_id": "218695",
        "body": "PROMPT_ID=218695 | PROJECT=MegaVault / e-Boks bootstrap | project_id=23 | MegaVault=FAST\n\n# Goal\nCrea e pubblica il repository pubblico `gernalix/eboks-scraper` dal seed già implementato, registralo canonicamente in MegaVault e calibra/verifica SOLO l'adapter UI reale di e-Boks sulla sessione Chrome autenticata di Fedora.\n\n# Starting point\n- seed carrier: `gernalix/codex-roadmap`, branch `seed/eboks-scraper-20260921`, file `seeds/eboks-scraper.zip.b64`, commit `13c104cf038d0f30dbe9366161c643e3a5869139`; NON mergiare questo branch in roadmap main.\n- Il seed passa già 5 unit test Python + syntax check JS.\n- Architettura già implementata: MV3 extension -> normale UI e-Boks “Save local copy” -> watcher Python localhost -> PDF/ZIP -> SHA-256 dedupe -> SQLite/FTS5 -> pdftotext, OCR opzionale -> systemd user service.\n- Nessuna API privata e-Boks, cookie/session extraction, automazione MitID, CAPTCHA/rate-limit bypass.\n- target checkout: `~/projects/eboks-scraper`; target remote pubblico: `gernalix/eboks-scraper`.\n- La sessione e-Boks autenticata in Chrome è un prerequisito runtime da usare, non da automatizzare.\n\n# Execution\n1. Prima di altro lavoro esegui `python3 ~/projects/codex-roadmap/tools/roadmap_start.py --repo ~/projects/codex-roadmap --prompt-id 218695`. Rispetta il worktree_path restituito per MegaVault; il nuovo repo e-Boks va creato separatamente in `~/projects/eboks-scraper`.\n2. Fai un solo fetch mirato del branch seed e decodifica il file esatto nel target checkout. Non esplorare o riscrivere il progetto già implementato.\n3. Crea il repository GitHub PUBBLICO `gernalix/eboks-scraper` con il tooling GitHub già autenticato locale, inizializza/pusha `main`. Registra il nuovo progetto in MegaVault con il meccanismo canonico esistente; NON inventare un project_id.\n4. Esegui una volta i test del seed. Installa/avvia il backend con `scripts/install.sh`; dipendenze Python/Fedora globali soltanto, MAI venv.\n5. Carica l'estensione unpacked nel Chrome reale. Prima `dryRun=true`. Ispeziona SOLO il DOM necessario a `extension/adapter.js`; se confidence/selettori non bastano, modifica SOLO adapter/selettori e test direttamente pertinenti. Non fare reverse engineering di endpoint privati.\n6. Smoke reale bounded su 1-3 messaggi max: UI ufficiale Save local copy -> download -> watcher -> archive -> estrazione testo -> SQLite. Verifica anche che re-ingest dello stesso file sia idempotente via SHA-256.\n7. Se compare login scaduto, CAPTCHA, 429/throttling o altro anti-bot, STOP fail-closed: nessun bypass e nessun retry identico.\n8. Commit/push SOLO i fix necessari al nuovo repo. Verifica repo pubblico e CI. Dopo conferma del target remoto, elimina il branch temporaneo `seed/eboks-scraper-20260921` da codex-roadmap senza toccare main.\n\n# Acceptance\n- `gernalix/eboks-scraper` esiste ed è pubblico, con seed + eventuali fix adapter validati;\n- nuovo progetto registrato canonicamente in MegaVault;\n- unit test/syntax check PASS e backend locale healthy;\n- smoke reale archivia almeno 1 documento e-Boks con testo estratto in SQLite; se impossibile, BLOCKED solo per un prerequisito esterno concreto e non aggirabile in sicurezza;\n- dry-run/fail-closed e divieti API privata/login automation/anti-bot bypass restano intatti;\n- branch seed temporaneo rimosso dopo bootstrap riuscito.\n\n# Non-goal\nExport completo della inbox, refactor/cleanup/modernizzazioni, dashboard aggiuntive, audit repo/browser generali.\n\n# Stop\nAl PASS finalizza subito via roadmap_result/roadmap_finish e STOP. Output finale max 8 righe: PROMPT_ID, RESULT, REPO_URL, PROJECT_ID, TESTS, LIVE_SMOKE, CI, BLOCKER se presente.\n",
        "sha256": "f3b960ecf7d86df2e4cc4b8bc9b3d03f57abb22dc50325524c43888f6684ae46",
        "created_at": "2026-09-24T08:49:53Z",
        "actor": "chatgpt"
      }
    ],
    "analyses": [],
    "executions": [],
    "status_history": [
      {
        "history_id": 556,
        "prompt_id": "218695",
        "old_status": null,
        "new_status": "pending",
        "changed_at": "2026-09-21T17:52:46Z",
        "actor": "chatgpt",
        "note": "registered"
      }
    ],
    "work_item_tags": [
      {
        "work_item_id": "prompt:218695",
        "tag": "conditional:only-if-eboks-native-export-incomplete"
      },
      {
        "work_item_id": "prompt:218695",
        "tag": "manual-prerequisite:confirm-eboks-scraper-needed"
      }
    ],
    "work_item_dependencies": [
      {
        "work_item_id": "prompt:218695",
        "depends_on_work_item_id": "prompt:582946",
        "required": 1,
        "note": "Il bootstrap/processing e-Boks deve attendere che l'export iniziale completo sia terminato."
      }
    ],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [],
    "work_item_runs": [],
    "issue_work_item_links": []
  }
]
```
