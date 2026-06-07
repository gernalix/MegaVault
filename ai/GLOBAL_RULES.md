# MegaVault Global Rules

## Resolution Order
1. Open `ai/MEGAVAULT_PROTOCOL.md`.
2. Open `ai/global/HOST_PROFILE.md`.
3. Open the current repo's `dev/project.metadata.json`.
4. Follow `ai_doc` and open the matching MegaVault AI project file.
5. Use HOST_PROFILE as hardware/system constraint authority.
6. Use the AI doc as the primary project operational source for Codex work.
7. Use Human docs for user-facing explanation only; they are not operational authority.
8. Use `dev/legacy/` only for historical context, missing detail recovery, or audit trails.
9. If architecture, build, tests, safety rules, release rules, data rules, or roadmap change, update the AI doc in the same change.
10. If UX, functionality, user workflows, troubleshooting, or changelog change, update Human docs from the AI doc.
11. Conflict rule: protocol + HOST_PROFILE + metadata + AI doc win over Human docs and legacy docs. If metadata and AI doc conflict, stop and repair metadata/AI doc before continuing.

## Global Docs
- HOST_PROFILE_AI: [global/HOST_PROFILE.md](global/HOST_PROFILE.md)
- HOST_PROFILE_HUMAN: [../human/global/HOST_PROFILE.md](../human/global/HOST_PROFILE.md)
- HOST_PROFILE_REQUIRED_FOR: performance, monitoring, automation, service, system tuning, Android tooling, backup, storage, Linux Mint, freeze investigations.

## Write Policy
- Do not delete legacy docs casually.
- Do not modify application code or databases for documentation-only tasks.
- Prefer `UNKNOWN`, `TODO`, or `OPEN QUESTION` over invented facts.
- Keep one AI file per project under `ai/projects/<slug>.md`.
- Keep Human docs readable under `human/projects/<slug>/`.

## Next-Prompt Rule
For every future Codex prompt inside an indexed repo: `ai/MEGAVAULT_PROTOCOL.md` -> `ai/global/HOST_PROFILE.md` -> `dev/project.metadata.json` -> `ai_doc` -> task files -> legacy only if the AI doc lacks required history.

LAST_UPDATED: 2026-06-07T19:10:00+02:00 by #847261
