# Delegare export Grindr end-to-end a ChatGPT Desktop

<!-- migration-fd847d09a5bc6a00 -->

Migrated project backlog. Project: **grindr-export**; project_id: 106.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 106.

Provenance: `prompt:556372`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Delegare export Grindr end-to-end a ChatGPT Desktop

status: pending

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "106",
      "reason": "canonical repository identity",
      "related_projects": [
        "106"
      ]
    },
    "source": {
      "work_item_id": "prompt:556372",
      "parent_id": null,
      "kind": "task",
      "title": "Delegare export Grindr end-to-end a ChatGPT Desktop",
      "objective": null,
      "acceptance_json": null,
      "status": "pending",
      "executor_policy": "codex",
      "sort_order": 4,
      "current_action": null,
      "next_action": null,
      "blocker": null,
      "project_id": null,
      "project_name": "grindr-export",
      "repo": "gernalix/grindr-export",
      "prompt_id": "556372",
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "prompt",
      "source_ref": "556372",
      "created_at": "2026-09-22T03:43:34Z",
      "updated_at": "2026-09-26T16:25:56Z"
    },
    "prompt_metadata": [
      {
        "prompt_id": "556372",
        "slug": "grindr-export-chatgpt-desktop-end-to-end-v1",
        "chat_guidance": "Nuova chat Codex in ChatGPT Desktop; parte solo dopo la finalizzazione di 354882 per non contendere la stessa sessione Grindr/Chrome.",
        "prompt_type": "Bootstrap",
        "model": "GPT-5.6 Terra",
        "reasoning": "medium",
        "megavault_mode": "FAST",
        "campaign_id": null,
        "explanation": "Fa gestire a ChatGPT Desktop tutto il lavoro: prepara il repo sul PC, lo registra in MegaVault, controlla Grindr nel browser, esporta la conversazione aperta e verifica che l’archivio sia completo. Non devi lanciare comandi a mano, salvo un eventuale login realmente necessario.",
        "current_path": "prompts/grindr-export-chatgpt-desktop-end-to-end-v1.md",
        "materialization_sha256": "155f9d100d8fa3cd1d107dee0d489cd6fbb2f08c6071cd7b4ead546924da8cbf",
        "created_at": "2026-09-22T03:43:34Z",
        "updated_at": "2026-09-26T16:25:56Z"
      }
    ],
    "prompt_materializations": [
      {
        "prompt_id": "556372",
        "body": "PROMPT_ID=556372 | MegaVault=FAST\nWORKDIR=/home/daniele/projects/grindr-export\n\n# Goal\nPrendi in carico in ChatGPT Desktop l'intero workflow di `gernalix/grindr-export` senza chiedermi di eseguire comandi manualmente: prepara il checkout locale canonico, registra il nuovo repo in MegaVault, valida codice/test, usa la sessione Grindr Web reale già autenticata quando disponibile, acquisisci la conversazione attualmente aperta/selezionata, genera l'archivio offline e verifica end-to-end gli output.\n\n# Starting point autoritativo\n- remoto già pronto: `https://github.com/gernalix/grindr-export`, branch `main`;\n- main contiene `grindr_dom_archive.py`, `GRINDR_EXPORT_MINIPROMPT.md`, `README.md`, `.gitignore` e 3 test stdlib;\n- commit d'integrazione noto: `6b77ac5d215b872353f28c2756bf501e110ee432`;\n- il transcript storico allegato NON deve entrare in Git;\n- export utente sotto `/home/daniele/Documents/ChatGPT/Pixel 8a/grindr_archive/`;\n- Python globale; venv/virtualenv/poetry/uv vietati;\n- `grindr-export` non è ancora registrato nel `megavault.sqlite` canonico;\n- PROMPT_ID=354882 lavora sul diverso repo `grindr-web-exporter` e condivide la stessa risorsa browser/Grindr: questo task parte solo dopo la sua finalizzazione, come imposto dalla dependency della roadmap. Non riaprire o correggere 354882.\n\n# Esecuzione\n1. Prima azione: `python3 ~/projects/codex-roadmap/tools/roadmap_start.py --repo ~/projects/codex-roadmap --prompt-id 556372`. Procedi solo se conferma `running`.\n2. Porta il repo locale a `/home/daniele/projects/grindr-export` dal remoto canonico. Se già presente, riusalo: niente secondo clone. Verifica che `main` corrisponda al remoto senza distruggere modifiche locali.\n3. Registra il repository in MegaVault usando il CLI canonico del checkout `/home/daniele/projects/MegaVault`. Usa `register-github-repo` con owner `gernalix`, nome `grindr-export`, remote URL, default branch `main` e worktree canonico. Leggi poi il project_id assegnato dal DB/CLI e verifica che repo/path siano risolvibili. Non inventare project_id e non creare registri paralleli.\n4. Esegui i test mirati già presenti:\n   `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v`.\n   Se falliscono per un bug reale del repo, correggi il minimo necessario nello stesso task; se serve modificare Git, usa il flusso single-writer/repo-task previsto dal protocollo. Niente refactor/cleanup fuori scope.\n5. Controlla la sessione Chrome reale. Riusa una tab `web.grindr.com` già autenticata se esiste. Non chiudere il Chrome predefinito, non cancellare cookie/profili e non avviare loop di login.\n6. Se esiste evidenza positiva di logout/login richiesto, chiedi UN SOLO handoff per il login nella stessa finestra e, appena autenticato, continua automaticamente. Assenza di un selettore o DOM inatteso non equivale a logout: diagnostica il DOM invece di chiedere un altro login.\n7. Usa `GRINDR_EXPORT_MINIPROMPT.md` come specifica di acquisizione, ma esegui tu direttamente i passi: sulla conversazione Grindr attualmente aperta/selezionata raggiungi il marker/inizio disponibile, acquisisci `[data-testid=\"chat-container\"]` con snapshot incrementali fino al fondo e salva `raw/dom_snapshots.json`. Non chiedermi di copiare/incollare prompt o lanciare script.\n8. Per media usa solo normali asset browser/pageAssets. Non bypassare album privati, view-once, protezioni o URL firmati; registra come non esportabile ciò che non è normalmente acquisibile. Non salvare cookie, auth header, token, session secret o query string firmate.\n9. Esegui direttamente:\n   `python3 /home/daniele/projects/grindr-export/grindr_dom_archive.py \"<ARCHIVE_DIR>\"`\n   sull'archive appena acquisito.\n10. Valida davvero:\n   - `raw/acquisition_summary.json`;\n   - `archive.sqlite` con `PRAGMA integrity_check` e `PRAGMA foreign_key_check`;\n   - coerenza conteggio messaggi JSON/CSV/SQLite;\n   - `index.html` apribile offline e ricerca funzionante;\n   - nessuna dipendenza remota attiva nel viewer;\n   - nessun export/chat/media personale tracciato in Git.\n11. Se il workflow reale smentisce una premessa (DOM Grindr cambiato, path diverso, helper non più valido), fai discovery solo mirata, correggi il minimo e riprendi il goal. Non creare follow-up per failure locali correggibili.\n12. Se hai modificato il repo, completa il flusso single-writer e attendi l'integrazione canonica verificata. Se non hai modificato codice, lascia il checkout pulito e sincronizzato.\n13. Dopo acceptance PASS, finalizza:\n   `python3 ~/projects/codex-roadmap/tools/roadmap_result.py --repo ~/projects/codex-roadmap --prompt-id 556372 --result PASS --confirm-executed`\n   e STOP.\n\n# Acceptance\nPASS solo se:\n- checkout canonico `/home/daniele/projects/grindr-export` esiste ed è coerente col remoto;\n- repo registrato nel MegaVault canonico con project_id reale e path risolvibile;\n- test del repo PASS;\n- una conversazione reale attualmente selezionata viene acquisita end-to-end senza loop di login;\n- normalizzazione produce `messages.json`, `messages.csv`, `archive.sqlite`, `index.html`, `README.md` e `raw/acquisition_summary.json`;\n- tutti i check di integrità passano; `PASS WITH WARNINGS` è ammesso solo per media/album non esportabili normalmente;\n- nessuna credenziale, token, transcript o media personale finisce in Git/log/report;\n- nessun passaggio terminale viene scaricato sull'utente salvo login/permesso realmente indispensabile.\n\n# Non-goal\nEsportare automaticamente tutte le chat senza un target selezionato, bypassare protezioni Grindr, riscrivere `grindr-web-exporter`, audit generale di Chrome/MegaVault/roadmap, nuovi daemon/monitor/dashboard.\n\n# Output finale\nMassimo 9 righe: RESULT, PROJECT_ID, REPO_STATE, TESTS, AUTH/LOGIN_HANDOFFS, ARCHIVE_DIR, MESSAGE_COUNTS, MEDIA_WARNINGS, BLOCKER.",
        "sha256": "155f9d100d8fa3cd1d107dee0d489cd6fbb2f08c6071cd7b4ead546924da8cbf",
        "created_at": "2026-09-24T08:49:53Z",
        "actor": "chatgpt"
      }
    ],
    "analyses": [],
    "executions": [],
    "status_history": [
      {
        "history_id": 710,
        "prompt_id": "556372",
        "old_status": null,
        "new_status": "pending",
        "changed_at": "2026-09-22T03:43:34Z",
        "actor": "chatgpt",
        "note": "registered"
      }
    ],
    "work_item_tags": [
      {
        "work_item_id": "prompt:556372",
        "tag": "grindr"
      },
      {
        "work_item_id": "prompt:556372",
        "tag": "export"
      },
      {
        "work_item_id": "prompt:556372",
        "tag": "browser"
      }
    ],
    "work_item_dependencies": [
      {
        "work_item_id": "prompt:556372",
        "depends_on_work_item_id": "prompt:181259",
        "required": 1,
        "note": "Condivide la sessione browser/Grindr: eseguire solo dopo la finalizzazione del task già running 354882."
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
