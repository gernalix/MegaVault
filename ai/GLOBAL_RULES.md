# MegaVault Global Rules

## Resolution Order
1. Open the current repo's `dev/project.metadata.json`.
2. Follow `ai_doc` and open the matching MegaVault AI project file.
3. Use the AI doc as the primary operational source for Codex work.
4. Use Human docs for user-facing explanation only; they are not operational authority.
5. Use `dev/legacy/` only for historical context, missing detail recovery, or audit trails.
6. If architecture, build, tests, safety rules, release rules, data rules, or roadmap change, update the AI doc in the same change.
7. If UX, functionality, user workflows, troubleshooting, or changelog change, update Human docs from the AI doc.
8. Conflict rule: metadata + AI doc win over Human docs and legacy docs. If metadata and AI doc conflict, stop and repair metadata/AI doc before continuing.

## Write Policy
- Do not delete legacy docs casually.
- Do not modify application code or databases for documentation-only tasks.
- Prefer `UNKNOWN`, `TODO`, or `OPEN QUESTION` over invented facts.
- Keep one AI file per project under `ai/projects/<slug>.md`.
- Keep Human docs readable under `human/projects/<slug>/`.

## Next-Prompt Rule
For every future Codex prompt inside an indexed repo: `dev/project.metadata.json` -> `ai_doc` -> task files -> legacy only if the AI doc lacks required history.

LAST_UPDATED: 2026-06-01T13:20:29+02:00 by #842915
