# P0 MegaVault definitiva + database inventory + Datasette universale

<!-- migration-691ca490dd3830ff -->

Migrated project backlog. Project: **megavault**; project_id: 23.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Merged duplicate/complementary observations and subtasks; every original requirement retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 10, 23.

Provenance: `wi:68cd5b09eae24fe59352bd0750a559c1`, `wi:e20d87af9a6641c385b03b40aa72ab8a`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### P0 MegaVault definitiva + database inventory + Datasette universale

Consolidare MegaVault in una sola source of truth verificata; creare un database_inventory canonico e rigenerabile dal filesystem; rendere i DB selezionati Datasette-friendly nel codice sorgente; sincronizzare snapshot SQLite consistenti Fedora→Oracle ogni minuto; esporre solo i DB scelti su datasette.danielegalati.com con UX standard frictionless.

Acceptance:

- Una sola MegaVault canonica, pulita, sincronizzata e verificata; nessun consumer attivo punta a copie o path obsoleti.
- Bootstrap/protocollo executor minimo e automatico: nessun executor può legittimamente bypassare MegaVault perché dirty; gli update canonici hanno un percorso chiaro e non bloccante.
- Home-level MegaVault debris auditato e bonificato con recovery verificabile.
- database_inventory unico, automatico e riconciliato col filesystem reale; vecchi inventari duplicati ritirati o migrati.
- Selezione Datasette esplicita registrata in datasette_expose/sync_to_oracle; DB scelti resi Datasette-friendly nel codice sorgente con test/migrazioni adeguati.
- Sync Fedora→Oracle ogni minuto consistente, incrementale/change-aware, atomico e monitorabile; nessuna corruzione o WAL race.
- datasette.danielegalati.com mostra solo i DB scelti e la UX standard richiesta: date locali più raw epoch, boolean visuali, link, mappe quando applicabili, click-to-filter/date-day-filter, FK/backlink leggibili.
- Test mirati PASS, verifica runtime reale Oracle/Datasette e documentazione finale ultracompressa; nessun refactor estraneo.

status: waiting

current_action: Umbrella P0 da decomporre in fasi ordinate.

next_action: Freshly reconcile the whole Phase D batch on current MegaVault/Datasette5 state, execute one Datasette5 writer lane, then Phase E and e20d87 final gate.

blocker: Phase D Fedora-to-Oracle engine, Phase E Datasette UX, and sole final gate remain unverified.

### Gate finale — MegaVault + database inventory + Datasette end-to-end

Verificare sullo stato canonico e sui runtime reali che tutte le fasi A-E abbiano soddisfatto l'acceptance unica dell'umbrella P0; chiudere il root solo su PASS completo.

Acceptance:

- Una sola MegaVault canonica, pulita, sincronizzata e verificata; nessun consumer attivo punta a copie o path obsoleti.
- Bootstrap/protocollo executor minimo e automatico impedisce il bypass per dirty state e offre update canonici non bloccanti.
- Home-level MegaVault debris è bonificato con recovery verificabile.
- database_inventory unico e automatico è riconciliato col filesystem reale e i predecessori duplicati sono ritirati/migrati.
- Decisioni datasette_expose/sync_to_oracle sono esplicite e tutti i DB scelti sono Datasette-friendly nel codice sorgente con test/migrazioni.
- Sync Fedora→Oracle ogni minuto è consistente, change-aware, atomico e monitorabile senza WAL race.
- datasette.danielegalati.com espone solo i DB scelti e la UX standard richiesta funziona sul runtime reale.
- Test mirati, verifica runtime Oracle/Datasette e documentazione finale ultracompressa sono PASS; nessun lavoro estraneo resta necessario.

status: pending

current_action: Waiting on Phase E

next_action: Dopo Phase E, verificare tutti gli otto criteri end-to-end e chiudere l'umbrella solo su PASS.

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "23",
      "reason": "semantic correction of source routing; original identity preserved",
      "related_projects": [
        "23",
        "10"
      ]
    },
    "source": {
      "work_item_id": "wi:68cd5b09eae24fe59352bd0750a559c1",
      "parent_id": null,
      "kind": "goal",
      "title": "P0 MegaVault definitiva + database inventory + Datasette universale",
      "objective": "Consolidare MegaVault in una sola source of truth verificata; creare un database_inventory canonico e rigenerabile dal filesystem; rendere i DB selezionati Datasette-friendly nel codice sorgente; sincronizzare snapshot SQLite consistenti Fedora→Oracle ogni minuto; esporre solo i DB scelti su datasette.danielegalati.com con UX standard frictionless.",
      "acceptance_json": "[\"Una sola MegaVault canonica, pulita, sincronizzata e verificata; nessun consumer attivo punta a copie o path obsoleti.\", \"Bootstrap/protocollo executor minimo e automatico: nessun executor può legittimamente bypassare MegaVault perché dirty; gli update canonici hanno un percorso chiaro e non bloccante.\", \"Home-level MegaVault debris auditato e bonificato con recovery verificabile.\", \"database_inventory unico, automatico e riconciliato col filesystem reale; vecchi inventari duplicati ritirati o migrati.\", \"Selezione Datasette esplicita registrata in datasette_expose/sync_to_oracle; DB scelti resi Datasette-friendly nel codice sorgente con test/migrazioni adeguati.\", \"Sync Fedora→Oracle ogni minuto consistente, incrementale/change-aware, atomico e monitorabile; nessuna corruzione o WAL race.\", \"datasette.danielegalati.com mostra solo i DB scelti e la UX standard richiesta: date locali più raw epoch, boolean visuali, link, mappe quando applicabili, click-to-filter/date-day-filter, FK/backlink leggibili.\", \"Test mirati PASS, verifica runtime reale Oracle/Datasette e documentazione finale ultracompressa; nessun refactor estraneo.\"]",
      "status": "waiting",
      "executor_policy": "auto",
      "sort_order": -10000,
      "current_action": "Umbrella P0 da decomporre in fasi ordinate.",
      "next_action": "Freshly reconcile the whole Phase D batch on current MegaVault/Datasette5 state, execute one Datasette5 writer lane, then Phase E and e20d87 final gate.",
      "blocker": "Phase D Fedora-to-Oracle engine, Phase E Datasette UX, and sole final gate remain unverified.",
      "project_id": null,
      "project_name": null,
      "repo": null,
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-27T10:02:38Z",
      "updated_at": "2026-09-28T09:50:32Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:68cd5b09eae24fe59352bd0750a559c1",
        "tag": "priority:p0"
      },
      {
        "work_item_id": "wi:68cd5b09eae24fe59352bd0750a559c1",
        "tag": "priority:absolute"
      },
      {
        "work_item_id": "wi:68cd5b09eae24fe59352bd0750a559c1",
        "tag": "megavault"
      },
      {
        "work_item_id": "wi:68cd5b09eae24fe59352bd0750a559c1",
        "tag": "datasette"
      },
      {
        "work_item_id": "wi:68cd5b09eae24fe59352bd0750a559c1",
        "tag": "database-inventory"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [
      {
        "from_work_item_id": "wi:c24bc183ffdc4e648d77190f2bf5d651",
        "to_work_item_id": "wi:68cd5b09eae24fe59352bd0750a559c1",
        "relation_type": "superseded_by",
        "created_at": "2026-09-27T10:05:27Z",
        "actor": "c2-root-audit",
        "note": "SUPERSEDED"
      },
      {
        "from_work_item_id": "wi:05f8f72d99fa40b585db6e290292e57c",
        "to_work_item_id": "wi:68cd5b09eae24fe59352bd0750a559c1",
        "relation_type": "superseded_by",
        "created_at": "2026-09-27T10:05:27Z",
        "actor": "c2-root-audit",
        "note": "SUPERSEDED"
      },
      {
        "from_work_item_id": "wi:6d4b6f141ca74138ac035e864f8c3ef5",
        "to_work_item_id": "wi:68cd5b09eae24fe59352bd0750a559c1",
        "relation_type": "superseded_by",
        "created_at": "2026-09-27T10:05:27Z",
        "actor": "c2-root-audit",
        "note": "SUPERSEDED"
      }
    ],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 616,
        "work_item_id": "wi:68cd5b09eae24fe59352bd0750a559c1",
        "evidence_kind": "issue_inbox",
        "label": "issue:79cdfef8b7ca4c238fc53beb5c033106",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"[P0 ABSOLUTE PRIORITY — UMBRELLA] Bonifica definitiva MegaVault + database inventory canonico + Datasette universale. Questo task assorbe/supersede la sostanza di C2 #1980 se ancora pendente; decomporre internamente in fasi/work item ordinati, ma mantenere una sola acceptance end-to-end e non lasciare doppie fonti di verità.\\n\\nA) MEGAVAULT DEFINITIVA / ONE SOURCE OF TRUTH\\n- Riconciliare e fondere intelligentemente le due MegaVault oggi divergenti (/home/daniele/MegaVault e /home/daniele/projects/MegaVault): preservare ogni dato/storia utile, risolvere dirty state/branch/commit, scegliere UN solo checkout+megavault.sqlite canonico e rimuovere/archiviare in sicurezza i duplicati solo dopo verifica e backup coerente.\\n- Aggiornare TUTTI i protocolli, AGENTS.md, docs, script, servizi, C2/roadmap/PersonalHub e ogni altro consumer affinché puntino alla nuova MegaVault unica; nessun path/authority stale.\\n- Valutare architetturalmente se MegaVault debba fisicamente assorbire gli altri protocolli o diventare il loro indice/authority canonico. Obiettivo: “one source of truth” reale senza duplicare stato volatile o creare coupling inutile. Scegliere l’assetto più semplice/robusto e documentarlo in forma ultracompressa AI-friendly.\\n- Implementare i meccanismi pratici più forti e semplici per fare sì che qualunque executor/task/prompt: (1) legga il bootstrap MegaVault minimo pertinente, (2) rispetti i vincoli canonici, (3) aggiorni MegaVault quando produce fatti canonici. Preferire enforcement automatico (wrapper/helper/hook/guard/CI/protocol bootstrap) a istruzioni verbose.\\n- Eliminare definitivamente il pattern “MegaVault dirty => la ignoro”: usare/integrare github-autosync o meccanismo equivalente per mantenere il canonico pulito, sincronizzato locale/remoto e recuperabile, senza burocrazia che blocchi executor. Un dirty state non deve mai autorizzare il bypass della source of truth.\\n- Eliminare spietatamente ridondanze, documenti e strutture non necessarie: costo di bootstrap/consultazione minimo. Tutti i documenti AI-facing finali devono essere ultracompressi, non ridondanti, con link/indici invece di duplicazioni.\\n- Auditare e bonificare anche file/cartelle MegaVault-correlati sparsi direttamente sotto /home/daniele (inclusi quelli mostrati nello screenshot utente: copie/rapporti home_cleanup/home_consolidation/home_migration/home_structure_to_review, MegaVault, MegaVault-worktrees, megavault-safety/Megavault safety, eventuali backup/evidence analoghi). Classificare canonical/needed/obsolete; migrare ciò che serve e rimuovere il superfluo solo con recovery verificabile.\\n\\nB) DATABASE_INVENTORY CANONICO, GENERATO DAL FILESYSTEM\\n- Istituire UN solo database_inventory come source of truth, eliminando/sostituendo i predecessori/accenni sparsi oggi presenti in MegaVault/data_assets/project_components/docs.\\n- Deve essere rigenerabile/idempotente AUTOMATICAMENTE dal filesystem, non mantenuto a mano. Discovery: tutti i repository Git reali, deduplica worktree/clone per origin/common git dir, rilevamento SQLite per firma binaria (non solo estensione), runtime DB dichiarati fuori repo, mount pertinenti e mapping a project/repo/host; classificare canonical/derived/cache/browser/test/fixture/backup/historical/demo.\\n- Campi minimi obbligatori: project_id/project_slug, repo identity/path, host, db name, source_path, classification, status/last_seen, canonical yes/no, datasette_expose yes/no, sync_to_oracle yes/no; aggiungere solo campi realmente utili (es. oracle_path/sync mode/owner) senza overengineering.\\n- Il bootstrap deve riconciliare l’inventario attuale con il filesystem reale. Evidenza già osservata: ~/projects contiene 40 checkout top-level / 36 identità repo circa; MegaVault attuale manca almeno fedora-context-data, grindr-favorites-monitor, sqlite-to-obsidian, telegram-notification-history, whatsapp-exporter e ha path drift almeno per MegaVault e wayland-workspace-switcher. Non assumere che questi numeri restino invariati: rieseguire discovery al momento del task.\\n\\nC) SELEZIONE + DATASSETTE-FRIENDLINESS\\n- L’executor deve decidere quali DB vale la pena esporre personalmente in Datasette. Escludere per default cache/browser internals/test/backup/demo salvo ragione esplicita.\\n- Per ogni DB scelto, modificare il CODICE CHE LO GENERA/schema/migrazioni (non patch manuale dei file runtime) per renderlo quanto più Datasette-friendly possibile: PK/FK reali e complete, label semantiche, backlink utili, indici sensati, view human-readable, relazioni many-to-many esplicite, timestamp interpretabili, link e campi di navigazione. Non inventare relazioni semantiche non supportate dai dati.\\n- Conservare sempre i valori raw necessari per sorting/audit anche quando si aggiungono colonne di presentazione.\\n\\nD) MOTORE UNICO FEDORA -> ORACLE -> DATASETTE\\n- Creare un unico motore idempotente che ogni minuto sincronizzi SOLO i DB con sync_to_oracle=yes dalle sorgenti canoniche Fedora alle copie Oracle. Usare snapshot SQLite consistenti (backup API/VACUUM INTO o equivalente), change detection per evitare trasferimenti inutili, trasferimento sicuro e replace atomico; mai copiare ciecamente un DB live/WAL.\\n- Integrare nel Datasette esistente su https://datasette.danielegalati.com/ e nel repo datasette5/Oracle già operativo. Nascondere dall’interfaccia ordinaria tutti i DB oggi esposti e ormai obsoleti; esporre esclusivamente quelli selezionati dal nuovo inventory (oltre a eventuali endpoint tecnici indispensabili ma non navigabili, se necessari).\\n- Sicurezza/autenticazione esistenti devono restare private e funzionanti; niente nuove VPN o istanze parallele se non strettamente necessarie.\\n\\nE) UX DATASETTE STANDARD\\nPer i DB esposti implementare, preferibilmente in modo generico/riutilizzabile anziché per-DB:\\n- date human-readable d/m/yy hh:mm in ora locale, mantenendo SEMPRE anche la colonna epoch(ms)/raw originale per sorting/audit;\\n- boolean 1/0 resi visivamente con emoji/simbolo coerente senza perdere il raw se serve;\\n- link Markdown/URL renderizzati cliccabili secondo uno schema canonico prestabilito;\\n- map views quando esistono location/lat-lon utili;\\n- click su un valore di tabella => filtro automatico per quel valore; click su una data => filtro per tutte le entry di quel giorno;\\n- FK/backlink e label devono essere la via primaria di navigazione frictionless.\\n\\nACCEPTANCE END-TO-END\\n1. Una sola MegaVault canonica, pulita, sincronizzata e verificata; nessun consumer attivo punta a copie/path obsoleti.\\n2. Bootstrap/protocollo executor minimo e automatico: nessun executor può legittimamente bypassare MegaVault perché dirty; update canonici hanno percorso chiaro e non bloccante.\\n3. Home-level MegaVault debris auditato e bonificato con recovery verificabile.\\n4. database_inventory unico, automatico e riconciliato col filesystem reale; vecchi inventari duplicati ritirati/migrati.\\n5. Selezione Datasette esplicita registrata in datasette_expose/sync_to_oracle; DB scelti resi Datasette-friendly nel codice sorgente con test/migrazioni adeguati.\\n6. Sync ogni minuto Fedora->Oracle consistente, incrementale/change-aware, atomico e monitorabile; nessuna corruzione/WAL race.\\n7. datasette.danielegalati.com mostra solo i DB scelti per consultazione ordinaria e la UX standard richiesta (date locali+raw epoch, boolean visuali, link, mappe quando applicabili, click-to-filter/date-day-filter, FK/backlink leggibili).\\n8. Test mirati PASS + verifica runtime reale Oracle/Datasette + documentazione finale ultracompressa. Terminare appena questi criteri sono verificati, senza refactor estranei.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:79cdfef8b7ca4c238fc53beb5c033106\", \"observed_at_ms\": 1790502797197, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-27T10:05:26Z"
      },
      {
        "evidence_id": 1469,
        "work_item_id": "wi:68cd5b09eae24fe59352bd0750a559c1",
        "evidence_kind": "classification",
        "label": "MegaVault Phase A and B children are terminal; Phase C has remaining Datasette5 715479 and salute gates, so the umbrella",
        "uri": null,
        "value_json": "\"MegaVault Phase A and B children are terminal; Phase C has remaining Datasette5 715479 and salute gates, so the umbrella Phase A next action is stale.\"",
        "created_at": "2026-09-28T09:08:47Z"
      },
      {
        "evidence_id": 1574,
        "work_item_id": "wi:68cd5b09eae24fe59352bd0750a559c1",
        "evidence_kind": "classification",
        "label": "Phase C required children and canonical inventory decisions are complete; Phase D/E and one final gate remain.",
        "uri": null,
        "value_json": "\"Phase C required children and canonical inventory decisions are complete; Phase D/E and one final gate remain.\"",
        "created_at": "2026-09-28T09:50:32Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:79cdfef8b7ca4c238fc53beb5c033106",
        "work_item_id": "wi:68cd5b09eae24fe59352bd0750a559c1",
        "role": "matched",
        "created_at": "2026-09-27T09:53:17Z"
      },
      {
        "issue_id": "issue:79cdfef8b7ca4c238fc53beb5c033106",
        "work_item_id": "wi:68cd5b09eae24fe59352bd0750a559c1",
        "role": "decision",
        "created_at": "2026-09-27T09:53:17Z"
      }
    ]
  },
  {
    "routing": {
      "project": "23",
      "reason": "blocker subtask inherits explicitly identified parent project",
      "related_projects": [
        "23",
        "10"
      ]
    },
    "source": {
      "work_item_id": "wi:e20d87af9a6641c385b03b40aa72ab8a",
      "parent_id": "wi:68cd5b09eae24fe59352bd0750a559c1",
      "kind": "gate",
      "title": "Gate finale — MegaVault + database inventory + Datasette end-to-end",
      "objective": "Verificare sullo stato canonico e sui runtime reali che tutte le fasi A-E abbiano soddisfatto l'acceptance unica dell'umbrella P0; chiudere il root solo su PASS completo.",
      "acceptance_json": "[\"Una sola MegaVault canonica, pulita, sincronizzata e verificata; nessun consumer attivo punta a copie o path obsoleti.\", \"Bootstrap/protocollo executor minimo e automatico impedisce il bypass per dirty state e offre update canonici non bloccanti.\", \"Home-level MegaVault debris è bonificato con recovery verificabile.\", \"database_inventory unico e automatico è riconciliato col filesystem reale e i predecessori duplicati sono ritirati/migrati.\", \"Decisioni datasette_expose/sync_to_oracle sono esplicite e tutti i DB scelti sono Datasette-friendly nel codice sorgente con test/migrazioni.\", \"Sync Fedora→Oracle ogni minuto è consistente, change-aware, atomico e monitorabile senza WAL race.\", \"datasette.danielegalati.com espone solo i DB scelti e la UX standard richiesta funziona sul runtime reale.\", \"Test mirati, verifica runtime Oracle/Datasette e documentazione finale ultracompressa sono PASS; nessun lavoro estraneo resta necessario.\"]",
      "status": "pending",
      "executor_policy": "auto",
      "sort_order": -9940,
      "current_action": "Waiting on Phase E",
      "next_action": "Dopo Phase E, verificare tutti gli otto criteri end-to-end e chiudere l'umbrella solo su PASS.",
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
      "created_at": "2026-09-27T10:15:07Z",
      "updated_at": "2026-09-27T10:15:07Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:e20d87af9a6641c385b03b40aa72ab8a",
        "tag": "priority:p0"
      },
      {
        "work_item_id": "wi:e20d87af9a6641c385b03b40aa72ab8a",
        "tag": "priority:absolute"
      },
      {
        "work_item_id": "wi:e20d87af9a6641c385b03b40aa72ab8a",
        "tag": "acceptance-gate"
      },
      {
        "work_item_id": "wi:e20d87af9a6641c385b03b40aa72ab8a",
        "tag": "megavault"
      },
      {
        "work_item_id": "wi:e20d87af9a6641c385b03b40aa72ab8a",
        "tag": "datasette"
      }
    ],
    "work_item_dependencies": [
      {
        "work_item_id": "wi:e20d87af9a6641c385b03b40aa72ab8a",
        "depends_on_work_item_id": "wi:9116862e72024e89b0033b4c6eeb146c",
        "required": 1,
        "note": "c2-intake"
      }
    ],
    "work_item_relations": [
      {
        "from_work_item_id": "wi:879ae0332e364440ad013f090a63714d",
        "to_work_item_id": "wi:e20d87af9a6641c385b03b40aa72ab8a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:46:56Z",
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
