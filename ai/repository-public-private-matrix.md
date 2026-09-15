# Repository public/private matrix

Updated: 2026-09-16
Status: **baseline recommendation; secret/history audit not yet executed**

Purpose: decide which repositories may safely become public so repeatable GitHub Actions can use free standard hosted runners, while keeping personal data, operational infrastructure and account/session material private.

## Decision codes

- `PUBLIC_AFTER_AUDIT`: good candidate for public visibility **only after** the publication-safety audit passes for the complete Git history and current tracked tree.
- `PRIVATE`: keep private by default. Public visibility has little benefit or the repository's purpose/data/operational context creates avoidable exposure.
- `RETIRE`: obsolete standalone repository scheduled for deletion; exclude from publication work.

The audit may downgrade any `PUBLIC_AFTER_AUDIT` repository to `PRIVATE`. A `PRIVATE` repository should be promoted only with concrete evidence that it contains reusable code only and no sensitive/operational material.

## Matrix

| Repository | Current visibility | Baseline recommendation | Audit priority | Rationale |
| --- | --- | --- | --- | --- |
| PersonalHub | private | PUBLIC_AFTER_AUDIT | P0 | Main active software project; large CI benefit if clean. |
| codex-usage-monitor | private | PUBLIC_AFTER_AUDIT | P0 | Reusable Python tooling; high CI benefit. |
| github-autosync | private | PUBLIC_AFTER_AUDIT | P0 | Reusable automation; deterministic tests. |
| workflowy-import | private | PUBLIC_AFTER_AUDIT | P0 | Code can be public if exports, DBs, URLs and credentials are absent. |
| MultiTimeTracker | private | PUBLIC_AFTER_AUDIT | P1 | Active Android software; substantial CI benefit. |
| SuperContacts | private | PUBLIC_AFTER_AUDIT | P1 | App code can be public only if no real contact data/export fixtures are tracked. |
| android-app-template | private | PUBLIC_AFTER_AUDIT | P1 | Generic template; strong public-code candidate. |
| fedora-system-monitor | private | PUBLIC_AFTER_AUDIT | P1 | Generic system tooling if host-specific details/secrets are absent. |
| fedora-t7-backup | private | PUBLIC_AFTER_AUDIT | P1 | Generic backup logic if no private paths/identifiers/credentials leak. |
| app_lifecycle_monitor | private | PUBLIC_AFTER_AUDIT | P1 | Small reusable monitor. |
| codex-session-logger | private | PUBLIC_AFTER_AUDIT | P1 | Code may be reusable; session content itself must remain excluded. |
| wayland-workspace-switcher | private | PUBLIC_AFTER_AUDIT | P1 | Generic desktop utility. |
| git-change-ledger | private | PUBLIC_AFTER_AUDIT | P1 | Generic Git utility. |
| codex_weekly_limit_monitor | private | PUBLIC_AFTER_AUDIT | P1 | Generic monitor if account/session artifacts are excluded. |
| whatsapp-watcher | private | PUBLIC_AFTER_AUDIT | P1 | Extension code can be public if no session/account material exists. |
| chatgpt_tab_watcher_v1 | private | PUBLIC_AFTER_AUDIT | P1 | Browser automation code can be public if profiles/cookies/session data are absent. |
| WindowTabNotes | private | PUBLIC_AFTER_AUDIT | P1 | Generic browser/desktop utility candidate. |
| android_build_telegram_watch_v1 | private | PUBLIC_AFTER_AUDIT | P1 | Generic automation only if Telegram credentials/chat identifiers are not embedded. |
| yt_dlp_downloader | private | PUBLIC_AFTER_AUDIT | P1 | Generic downloader if no personal URLs/cookies/history are tracked. |
| patch_watcher_v1 | private | PUBLIC_AFTER_AUDIT | P2 | Small generic watcher. |
| logseq_updates | private | PUBLIC_AFTER_AUDIT | P2 | Generic update helper if no graph/user data are tracked. |
| file-mtt-automate | private | PUBLIC_AFTER_AUDIT | P2 | Generic automation if paths/data fixtures are sanitized. |
| typing_tracker | private | PUBLIC_AFTER_AUDIT | P2 | Generic utility if recorded user data are absent. |
| script_manager | private | PUBLIC_AFTER_AUDIT | P2 | Generic tooling candidate after purpose/content check. |
| script-edit-tabelle | private | PUBLIC_AFTER_AUDIT | P2 | Generic script candidate if no real DB/data samples are tracked. |
| gestore_db | private | PUBLIC_AFTER_AUDIT | P2 | Generic DB tooling only if real databases/credentials are absent. |
| HabitTracker | public | PUBLIC_AFTER_AUDIT | P0 | Already public; audit confirms no historical exposure. |
| HabitTracker2 | public | PUBLIC_AFTER_AUDIT | P0 | Already public; audit confirms no historical exposure. |
| real_timer_plugin | public | PUBLIC_AFTER_AUDIT | P0 | Already public reusable code; audit history. |
| codex-roadmap | public | PUBLIC_AFTER_AUDIT | P0 | Intentionally public workflow repo; audit for accidental secrets/private references. |
| gernalix.github.io | public | PUBLIC_AFTER_AUDIT | P0 | Must be public for normal Pages use; audit tracked/history content. |
| my-notes | public | PRIVATE | P0 | Name/purpose may imply personal content; keep/private unless audit proves it is code-only and intentionally public. |
| my-notes2 | public | PRIVATE | P0 | Same risk as `my-notes`; currently public so audit is urgent. |
| salute | public | PRIVATE | P0 | Potentially sensitive personal-domain repository; no compelling CI/publication benefit established. |
| MegaVault | private | PRIVATE | P0 | Operational knowledge base, SQLite inventory and infrastructure metadata. |
| vm_oracle | private | PRIVATE | P0 | Live infrastructure configuration/operations. |
| codex-usage | private | PRIVATE | P0 | Session/prompt/usage archive can contain private interaction and local metadata. |
| oracle-backup-service | private | PRIVATE | P0 | Backup/infrastructure topology and operational configuration. |
| owntracks | private | PRIVATE | P0 | Location-oriented project/data risk. |
| amici_fb | private | PRIVATE | P0 | Social/contact-oriented data risk. |
| telegram_insert_bot | private | PRIVATE | P0 | Bot/chat credentials and personal integration risk. |
| discord-exporter | private | PRIVATE | P0 | Account/export/session data risk outweighs free-CI benefit. |
| datasette_sesso | private | PRIVATE | P0 | Potentially sensitive personal dataset/application. |
| meth-repo | private | PRIVATE | P0 | Sensitive personal-domain repository; no public-CI need established. |
| datasette5 | private | PRIVATE | P1 | Operational/data-serving repository; likely contains deployment/data context. |
| surface-recovery-hardening | private | PRIVATE | P1 | Host recovery/security configuration can reveal system-specific details. |
| mint-freeze-forensics | private | PRIVATE | P1 | Machine-forensics evidence/log context should stay private. |
| logseq | private | PRIVATE | P1 | Treat Logseq graph/content repositories as personal data by default. |
| logseq2 | private | PRIVATE | P1 | Treat Logseq graph/content repositories as personal data by default. |
| logseq3 | private | PRIVATE | P1 | Treat Logseq graph/content repositories as personal data by default. |
| logseq4 | private | PRIVATE | P1 | Treat Logseq graph/content repositories as personal data by default. |
| logseq5 | private | PRIVATE | P1 | Treat Logseq graph/content repositories as personal data by default. |
| logseq6 | private | PRIVATE | P1 | Treat Logseq graph/content repositories as personal data by default. |
| L16 | private | PRIVATE | P2 | Legacy/unknown-purpose repository; no reason to expose merely for CI. |
| L17 | private | PRIVATE | P2 | Legacy/unknown-purpose repository; no reason to expose merely for CI. |
| dash_python2 | private | PRIVATE | P2 | Legacy/low-priority repository; public-CI benefit not established. |
| dash3 | private | PRIVATE | P2 | Legacy/low-priority repository; public-CI benefit not established. |
| scriptone | private | PRIVATE | P2 | Purpose/content not sufficiently generic to justify exposure without a separate need. |
| scriptone4 | private | PRIVATE | P2 | Purpose/content not sufficiently generic to justify exposure without a separate need. |
| porno_downloader | private | PRIVATE | P2 | Personal-use downloader; no compelling public-CI benefit. |
| facedownassup-downloader | private | PRIVATE | P2 | Personal-use downloader; no compelling public-CI benefit. |
| livinggaul-x-downloader | private | PRIVATE | P2 | Personal-use downloader; no compelling public-CI benefit. |
| strano-anello | private | PRIVATE | P2 | Unknown/private-purpose repository; keep private absent a concrete publication need. |
| Soldi | private | RETIRE | — | Standalone app superseded by PersonalHub module. |
| wordpulse | private | RETIRE | — | Standalone app superseded by PersonalHub module. |
| Sostanze | private | RETIRE | — | Standalone app superseded by PersonalHub module. |
| Luoghi | private | RETIRE | — | Standalone app superseded by PersonalHub module. |
| luoghi-app | private | RETIRE | — | Standalone app superseded by PersonalHub module. |

## Audit outcome fields

The Codex audit should extend this matrix with these columns rather than creating a second competing inventory:

- `audit_status`: `PASS`, `PASS_WITH_REMEDIATION`, `PRIVATE_BY_POLICY`, `RETIRED`, `BLOCKED`
- `secret_findings`: counts by severity only; **never secret values**
- `sensitive_artifacts`: concise categories/path references, no private payloads
- `history_clean`: yes/no/unknown
- `required_remediation`: concise action before any visibility change
- `final_recommendation`: `PUBLIC`, `PRIVATE`, `RETIRE`
- `confidence`: high/medium/low

## Safety rule

No repository visibility may be changed merely because this baseline says `PUBLIC_AFTER_AUDIT`. Publication is a separate explicit action after the audit result is reviewed. If a currently public repository has a live credential or sensitive personal artifact, report it as P0 remediation; do not print the value into logs, reports, Telegram, roadmap or chat.