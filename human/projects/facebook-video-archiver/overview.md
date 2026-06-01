# facebook-video-archiver Overview

facebook-video-archiver is documented in the MegaVault because local project docs were consolidated and archived under `dev/legacy`. Verified purpose from the source corpus: Start here for Codex/operator work on `facebook-video-archiver`.

## Why It Exists
- dev/legacy/README.md: Conservative local archiver for Facebook videos/posts that you own or are explicitly authorized to download. The default page is:
- dev/legacy/dev/INDEX.md: Start here for Codex/operator work on `facebook-video-archiver`.
- dev/legacy/dev/ARCHITECTURE.md: `facebook_video_archiver.sh` is the operator entrypoint. It wraps `yt-dlp` and delegates persistent manual-login browser work to `facebook_session_browser.py`.
- dev/legacy/dev/AGENT_RULES.md: - Keep `VERSION` as the single source of truth.
- dev/legacy/dev/TEST_PLAN.md: bash -n facebook_video_archiver.sh
- dev/legacy/dev/CHANGELOG.md: - Added `--discover-deep` with progressive scrolling, checkpoint/resume, and no-new-URL stop condition.
- dev/legacy/dev/OPERATIONS.md: cd ~/codex-workspace/facebook-video-archiver

## Current State
- Repository: `/home/daniele/codex-workspace/facebook-video-archiver`
- Branch at enrichment: `work/v4-deep-discovery`
- Latest local commit at enrichment: `ab0e526`
- Stack signals: Python, Shell, UNKNOWN, UNKNOWN
- Documentation quality: enriched from legacy docs and repository structure

## How To Use This Documentation
Start with the AI doc for operational work, then read these Human pages for explanation. Legacy docs are historical context, not the primary operating source after this enrichment.

## Links
- AI doc: [AI doc](../../../ai/projects/facebook-video-archiver.md)
- Metadata: [dev/project.metadata.json](../../../../facebook-video-archiver/dev/project.metadata.json)
- Legacy docs: [dev/legacy](../../../../facebook-video-archiver/dev/legacy)
- Repository: [repo path](../../../../facebook-video-archiver)
