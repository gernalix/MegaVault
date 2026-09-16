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
| android-app-template | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| fedora-system-monitor | private | PUBLIC_AFTER_AUDIT | P1 | Generic system tooling if host-specific details/secrets are absent. |
| fedora-t7-backup | private | PUBLIC_AFTER_AUDIT | P1 | Generic backup logic if no private paths/identifiers/credentials leak. |
| app_lifecycle_monitor | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| codex-session-logger | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| wayland-workspace-switcher | deleted | RETIRE | — | GitHub remote retired after verified offline archive; local clone preserved due path guard. |
| git-change-ledger | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| codex_weekly_limit_monitor | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| whatsapp-watcher | private | PUBLIC_AFTER_AUDIT | P1 | Extension code can be public if no session/account material exists. |
| chatgpt_tab_watcher_v1 | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| WindowTabNotes | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| android_build_telegram_watch_v1 | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| yt_dlp_downloader | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| patch_watcher_v1 | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| logseq_updates | private | PUBLIC_AFTER_AUDIT | P2 | Generic update helper if no graph/user data are tracked. |
| file-mtt-automate | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| typing_tracker | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| script_manager | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| script-edit-tabelle | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| gestore_db | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| HabitTracker | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| HabitTracker2 | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| real_timer_plugin | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| codex-roadmap | public | PUBLIC_AFTER_AUDIT | P0 | Intentionally public workflow repo; audit for accidental secrets/private references. |
| gernalix.github.io | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| my-notes | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| my-notes2 | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| salute | public | PRIVATE | P0 | Potentially sensitive personal-domain repository; no compelling CI/publication benefit established. |
| MegaVault | private | PRIVATE | P0 | Operational knowledge base, SQLite inventory and infrastructure metadata. |
| vm_oracle | private | PRIVATE | P0 | Live infrastructure configuration/operations. |
| codex-usage | private | PRIVATE | P0 | Session/prompt/usage archive can contain private interaction and local metadata. |
| oracle-backup-service | private | PRIVATE | P0 | Backup/infrastructure topology and operational configuration. |
| owntracks | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| amici_fb | private | PRIVATE | P0 | Social/contact-oriented data risk. |
| telegram_insert_bot | private | PRIVATE | P0 | Bot/chat credentials and personal integration risk. |
| discord-exporter | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| datasette_sesso | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| meth-repo | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| datasette5 | private | PRIVATE | P1 | Operational/data-serving repository; likely contains deployment/data context. |
| surface-recovery-hardening | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| mint-freeze-forensics | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| logseq | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| logseq2 | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| logseq3 | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| logseq4 | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| logseq5 | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| logseq6 | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| L16 | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| L17 | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| dash_python2 | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| dash3 | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| scriptone | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| scriptone4 | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| porno_downloader | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| facedownassup-downloader | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| livinggaul-x-downloader | private | PRIVATE | P2 | Personal-use downloader; no compelling public-CI benefit. |
| strano-anello | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |
| Soldi | private | RETIRE | — | Standalone app superseded by PersonalHub module. |
| wordpulse | deleted | RETIRE | — | Retired after verified offline archive and live confirmation that no Pixel package remained; GitHub remote and canonical local clone deleted. |
| Sostanze | private | RETIRE | — | Standalone app superseded by PersonalHub module. |
| Luoghi | private | RETIRE | — | Standalone app superseded by PersonalHub module. |
| luoghi-app | deleted | RETIRE | — | Retired after verified offline archive; GitHub remote and canonical local clone deleted. |

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
