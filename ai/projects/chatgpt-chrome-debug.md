PROJECT: chatgpt-chrome-debug
SLUG: chatgpt-chrome-debug
PATH: /home/daniele/codex-workspace/chatgpt-chrome-debug
REMOTE: none
BRANCH: master

STACK:
- node
- shell

ARCH:
- source: legacy docs in dev/legacy; central doc is authoritative after 2026-06-01T07:23:54+02:00
- legacy_archived: 7
- dirty_docs_skipped: 0

DB:
- diagnostics/profiles/diff_chrome_clean_gpu_on_1778449697/first_party_sets.db
- diagnostics/profiles/diff_chrome_clean_gpu_off_1778449357/first_party_sets.db
- diagnostics/profiles/smoke_runtime/first_party_sets.db
- diagnostics/profiles/diff_chrome_extensions_allowed_isolated_1778449709/first_party_sets.db
- diagnostics/profiles/diff_chrome_clean_gpu_on_1778449350/first_party_sets.db
- diagnostics/profiles/diff_chrome_many_tabs_1778449717/first_party_sets.db
- diagnostics/profiles/smoke_headless/first_party_sets.db
- diagnostics/profiles/diff_chrome_clean_gpu_off_1778449704/first_party_sets.db
- diagnostics/profiles/diff_chrome_extensions_allowed_isolated_1778449365/first_party_sets.db
- diagnostics/profiles/diff_chrome_memory_stress_1778449733/first_party_sets.db

BUILD:
- npm scripts
- shell scripts

TEST:
- not detected

VERSIONING:
- git_branch: master
- git_remote: none
- preexisting_status_count: 7

RULES:
- Open dev/project.metadata.json first.
- This AI doc is primary. Human docs derive from it.
- Legacy docs are historical only.
- Do not modify app code/db/build for docs-only migration.

ACTIVE_WORK:
- ?? .codexmeta
- ?? .codexmeta.bak.20260528_191731
- ?? .codexmeta.bak.20260528_191758
- ?? .codexmeta.bak.20260528_191912
- ?? .codexmeta.bak.20260528_193715
- ?? .codexmeta.bak.20260528_193944
- ?? .codexmeta.bak.20260528_194118

KNOWN_BUGS:
- not indexed; inspect legacy if needed

ROADMAP:
- not indexed; inspect legacy if needed

LEGACY_DOCS:
- KNOWN_PATTERNS.md -> dev/legacy/KNOWN_PATTERNS.md
- QUICK_FIXES.md -> dev/legacy/QUICK_FIXES.md
- README.md -> dev/legacy/README.md
- ROOT_CAUSE_ANALYSIS.md -> dev/legacy/ROOT_CAUSE_ANALYSIS.md
- diagnostics/environment/snapshot_20260510_223934/chrome_version.txt -> dev/legacy/diagnostics/environment/snapshot_20260510_223934/chrome_version.txt
- diagnostics/environment/snapshot_20260510_224516/chrome_version.txt -> dev/legacy/diagnostics/environment/snapshot_20260510_224516/chrome_version.txt
- diagnostics/environment/snapshot_20260510_224657/chrome_version.txt -> dev/legacy/diagnostics/environment/snapshot_20260510_224657/chrome_version.txt

SKIPPED_DOCS:
- none

LAST_VERIFIED: 2026-06-01T07:23:54+02:00
