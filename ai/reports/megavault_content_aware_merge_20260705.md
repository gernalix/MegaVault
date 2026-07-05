# MegaVault Content-Aware Merge Report 2026-07-05

## Sources

- Local MegaVault: `C:\Users\seste\Documents\MegaVault-surface`
- GitHub repository: `https://github.com/gernalix/MegaVault`
- Source branch: `codex/prompt-729604-supercontacts-capsule-audit`
- Created branch: `codex/merge-surface-with-supercontacts-content-aware`
- Working directory: `C:\Users\seste\Documents\megavault_content_aware_merge_20260705`
- User constraint update: final branch must contain only `.md` files outside `.git`.

## Criteria Used

Applied in the requested order: structural sections, operational rules, invariants, workflows, documented risks, tests/build/recovery/backup/incidents/versioning/automation/integration facts, completeness, MegaVault coherence, then size/hash/timestamp only as diagnostics.

Timestamp was not used for choosing content. File size was used only as a warning signal. Version header was not used as an automatic decision criterion.

## Inventory

- Initial unique non-`.git` paths across both sources: 304
- Unique Markdown paths compared after the `.md`-only constraint: 283
- Local Markdown files: 258
- GitHub Markdown files before report: 283
- Byte-identical Markdown files: 147
- Semantically identical after line-ending normalization: 95
- Same path with real content differences: 16
- Present only locally: 0
- Present only in GitHub branch: 25
- Unique non-Markdown paths excluded/removed by constraint: 6
- Same basename in different paths: 19 basename groups, mostly standard `overview.md`, `changelog.md`, `features.md`, `roadmap.md`, `troubleshooting.md` project docs.
- Probable duplicate content groups before merge: 242 normalized-hash groups; these were source-pair duplicates or line-ending variants, not copied as sidecars.

## Decisions Summary

- Files chosen from local MegaVault: 1 (0 local-only + 1 content conflicts)
- Files chosen from GitHub branch: 126 (25 GitHub-only + 6 content conflicts + 95 semantically identical files kept from branch)
- Files merged conservatively: 11
- Files kept in double version: 0
- Residual undecided conflicts: 0

## Local-Only Markdown Imported

- none

## GitHub-Only Markdown Kept

- `ai/projects/os-observer.md`
- `ai/projects/system-watchdog.md`
- `ai/projects/windows-flight-recorder.md`
- `ai/projects/windows-winget-daily-update.md`
- `ai/reports/pixel_buds_audio_windows11_20260628T005406Z.md`
- `human/projects/os-observer/changelog.md`
- `human/projects/os-observer/features.md`
- `human/projects/os-observer/overview.md`
- `human/projects/os-observer/roadmap.md`
- `human/projects/os-observer/troubleshooting.md`
- `human/projects/system-watchdog/changelog.md`
- `human/projects/system-watchdog/features.md`
- `human/projects/system-watchdog/overview.md`
- `human/projects/system-watchdog/roadmap.md`
- `human/projects/system-watchdog/troubleshooting.md`
- `human/projects/windows-flight-recorder/changelog.md`
- `human/projects/windows-flight-recorder/features.md`
- `human/projects/windows-flight-recorder/overview.md`
- `human/projects/windows-flight-recorder/roadmap.md`
- `human/projects/windows-flight-recorder/troubleshooting.md`
- `human/projects/windows-winget-daily-update/changelog.md`
- `human/projects/windows-winget-daily-update/features.md`
- `human/projects/windows-winget-daily-update/overview.md`
- `human/projects/windows-winget-daily-update/roadmap.md`
- `human/projects/windows-winget-daily-update/troubleshooting.md`

## Content Conflicts Chosen From Local

- `ai/MEGAVAULT_PROTOCOL.md`

## Content Conflicts Chosen From GitHub

- `ai/projects/amici-fb.md`
- `human/projects/amici-fb/changelog.md`
- `human/projects/amici-fb/features.md`
- `human/projects/amici-fb/overview.md`
- `human/projects/amici-fb/roadmap.md`
- `human/projects/amici-fb/troubleshooting.md`

Reason: the GitHub `amici-fb` files contain the Windows migration, scheduler validation, profile chooser fix, and explicit secret/runtime-state boundaries. The local versions were older Linux/systemd-oriented and included sensitive session/cookie excerpts as source-code facts, so they were not carried forward.

## Files Merged Conservatively

- `ai/PROJECT_INDEX.md`
- `ai/PROJECT_INVENTORY.md`
- `ai/projects/multitimetracker.md`
- `human/PROJECTS.md`
- `human/projects/multitimetracker/architecture-audit.md`
- `human/projects/multitimetracker/changelog.md`
- `human/projects/multitimetracker/features.md`
- `human/projects/multitimetracker/overview.md`
- `human/projects/multitimetracker/roadmap.md`
- `human/projects/multitimetracker/troubleshooting.md`
- `human/system/custom-services-status.md`

Merge rationale:

- `ai/PROJECT_INDEX.md`, `ai/PROJECT_INVENTORY.md`, `human/PROJECTS.md`: union of local and GitHub project rows, with missing internal Markdown links converted to `absent` text and synthesized rows for Markdown project docs present in the branch.
- `human/system/custom-services-status.md`: local later anti-freeze removal/Kuma state retained, GitHub detailed service snapshot appended.
- `multitimetracker` AI and human docs: local v527-v534 persistence/capsule/device history retained, GitHub master v535 Play Store readiness and wrong-branch recovery facts appended.

## Main Decision Notes

- `ai/MEGAVAULT_PROTOCOL.md`: local version chosen even though smaller because it is a denser evolved protocol with newer mandatory rules: host profile, Android protocol routing, incident registry, remote clean/push, sync state, final-report requirements and destructive-action/secret constraints. One path was corrected to `ai/ANDROID_PROTOCOL.md` to match the md-only branch.
- `ai/GLOBAL_RULES.md`, `human/INDEX.md`, global registries and most Linux Mint/Oracle project docs: local chosen because it adds new operational rules, registries, incidents, backup/recovery and validation facts absent from the branch.
- `SuperContacts`: local chosen for v28-v30 SAF root/photo/tag/home-card improvements, while the GitHub branch stopped earlier at v27/capsule audit.
- `Soldi`: local chosen because it documents the real local-first finance app, Room schema, SAF export/import and v2 validation; GitHub still described the starter project.
- `oracle-backup-service`: local chosen for fallback-quota recovery and MegaVault protocol conformity facts.
- Non-Markdown files: removed or excluded because the user updated the target constraint to `.md` only. The branch therefore intentionally contains no JSON, CSV, TXT, service, or moved-from-live files.

## Validations Performed

- Final branch file-type check: 0 non-`.md` files outside `.git`.
- Markdown readability: 283 Markdown files before this report, all UTF-8 readable, no NUL bytes.
- Internal Markdown links: 0 broken links resolving inside the MegaVault branch.
- External/outside relative references: 185 retained as references to project repos, metadata, or runtime locations outside this md-only branch.
- JSON/YAML validation: not applicable after md-only pruning; no JSON/YAML files remain in the branch.
- Large-file check before report: 283 Markdown files, total 1,039,582 bytes, no file over 1 MiB.
- Secret scan: exact token/key patterns found no real tokens. Broad keyword hits were placeholders (`<token>`), environment-variable names, warnings, or descriptive secret-handling rules.
- No database/archive/log binaries were added; the previous non-md snapshot/log/service files from GitHub were removed.
- Executed `git status` and `git diff --stat` before commit.

## Residual Risks

- Relative links that resolve outside the MegaVault repository were not live-verified; they are retained as operational references to project repos or runtime paths.
- Some synthesized index rows have `metadata unknown`/`repo unknown` when the Markdown project docs existed but neither source index had reliable row metadata.
- The MultiTimeTracker merge is intentionally conservative and retains source-specific historical facts; future editorial cleanup can compress it, but no operational fact was intentionally dropped.

## Git Commands Executed

```text
git clone https://github.com/gernalix/MegaVault.git C:\Users\seste\Documents\megavault_content_aware_merge_20260705
git checkout codex/prompt-729604-supercontacts-capsule-audit
git checkout -b codex/merge-surface-with-supercontacts-content-aware
git rm -- <all tracked non-md files>
git status --short
git diff --stat
git add -A
git commit -m "merge: content-aware merge surface MegaVault with supercontacts branch"
git commit --amend --no-edit
git push -u origin codex/merge-surface-with-supercontacts-content-aware
```

## Final Commit

- Final commit hash: see final response / `git rev-parse HEAD` after final amend. A tracked report cannot contain its own final Git SHA because writing that SHA changes the commit. Pre-note content commit: `79b7930e2abd603c668d08397a1ce0caca773b93`.
