# facedownassup-downloader

Local helper for downloading member gallery videos that are already accessible with the operator's Chrome login.

It wraps `yt-dlp` with Chrome cookies, browser-like `Referer`, `Origin`, and `User-Agent` headers, local verbose logs, a download archive, ordered output folders, refresh-test mode, single-URL test mode, list mode, and bounded same-origin crawl mode.

Refresh-test regenerates the authorized page and HLS manifest immediately before download, reports missing HLS fragment ranges, validates completed outputs with `ffprobe` when available, and moves or deletes incomplete files instead of mixing them with completed downloads.

Safety boundary: no DRM bypass, no paywall bypass, no credential attacks, no brute force, no exploit attempts, no aggressive crawling, and no full signed media URLs in reports.

Links: [AI doc](../../../ai/projects/facedownassup-downloader.md), [metadata](../../../../facedownassup-downloader/dev/project.metadata.json), [repo](../../../../facedownassup-downloader), [README](../../../../facedownassup-downloader/README.md).
