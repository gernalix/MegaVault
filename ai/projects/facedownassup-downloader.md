META:
name=facedownassup-downloader
slug=facedownassup-downloader
path=/home/daniele/codex-workspace/facedownassup-downloader
remote=git@github.com:gernalix/facedownassup-downloader.git
branch=main
prompt=518407
verified_at=2026-06-13T13:24:00+02:00
protocol=MEGAVAULT_PROTOCOL.md:VERSION=8
PURPOSE:
purpose=Local authorized downloader for facedownassup.com member gallery pages using existing legitimate Firefox login via yt-dlp cookies by default.
scope=personal_access_only,no_DRM_bypass,no_paywall_bypass,no_credential_attack,no_exploit,no_aggressive_rate
STACK:
lang=Bash,Python_inline_parser
tools=yt-dlp,Firefox cookies via --cookies-from-browser firefox,optional Chrome DevTools diagnostics,JDownloader existing jar,ffmpeg/ffprobe,gh,git
platform=Linux Mint/XFCE host
MAP:
entry=fda_downloader.sh
config=env:FDA_*,FDA_COOKIE_BROWSER,FDA_FIREFOX_PROFILE,VERSION,dev/project.metadata.json
docs=README.md,MegaVault/human/projects/facedownassup-downloader/*
state=state/download-archive.txt,state/segments-*.txt,logs/run-*.log,private/crawl-*
output=downloads/<extractor>/<id> - <title>.<ext>
avoid=downloads,logs,state,private,cookies,*.dump,*.part,*.ytdl
ARCH:
script=fda_downloader.sh modes:doctor,refresh-test,browser-check,test,download,list,crawl
download=yt-dlp --cookies-from-browser firefox by default; FDA_COOKIE_BROWSER=chrome supported; FDA_FIREFOX_PROFILE overrides detected Firefox profile; Referer/Origin/User-Agent + no-cache + archive + local verbose logs
refresh=refresh-test checks browser playback status when possible, extracts fresh page/manifest immediately before download, reports segments, validates complete files with ffprobe, and handles partials
browser_check=Firefox default runs redacted yt-dlp probe and documents that real Firefox Network capture is not automated; Chrome path remains explicit DevTools diagnostic launched only with FDA_BROWSER_CHECK_LAUNCH=1
jdownloader_check=existing /home/daniele/Downloads/JDownloader.jar process tested via clipboard/ClickAndLoad-style local port; no install performed; no cookie export performed
crawl=bounded same-origin gallery discovery from authorized HTML dumps; signed media URLs not persisted in reports
FLOW:
refresh-test=browser_playback_check->fresh_preflight_write_pages_private->fresh_gallery_download->segment_report->ffprobe_or_partial_classification
browser-check=ensure_existing_or_explicit_chrome_devtools->open_authorized_url->Network.responseReceived/loadingFinished->redacted_media_report->temporary_ytdlp_probe->comparison->FINAL_REPORT
test=doctor->yt-dlp_cookie_extract_from_selected_browser->generic_gallery_page->html5_m3u8->hlsnative
list=read_urls->download_url_each->sleep_between_videos->archive_dedupe
crawl=start_page->write_pages_tmp->parse_gallery_links->state/crawl-found-*.txt
INV:
security=never_print_cookies_tokens_passwords_signed_urls_in_reports
auth=only_use_operator_browser_session_for_content_already_authorized; Firefox is default cookie source
access=no_DRM/paywall/rate_limit/credential/protection_bypass
browser_diag=Chrome_remote_debugging_launch_only_when_FDA_BROWSER_CHECK_LAUNCH=1
data=raw_logs_local_only_chmod600; logs_may_contain_expiring_signed_URLs
ops=do_not_commit downloads/logs/state/private/cookies/dumps
version=VERSION and fda_downloader.sh SCRIPT_VERSION must move together
cookie_source=default Firefox; overrides FDA_COOKIE_BROWSER=firefox/chrome and FDA_FIREFOX_PROFILE
partials=complete_only_when_missing_count=0_and_ffprobe_passes; incomplete_outputs_move_to_downloads/_partials_or_delete_with_--no-partials
BUILD:
cmd=bash -n fda_downloader.sh
deps=yt-dlp,python3,Firefox_profile,optional_Chrome_profile,ffmpeg
install=none; optional FDA_UPDATE_YTDLP=1 ./fda_downloader.sh doctor
TEST:
syntax=bash -n fda_downloader.sh PASS 2026-06-13 after v0.4.0
doctor=./fda_downloader.sh doctor PASS 2026-06-13; cookie_browser=firefox; firefox_profile=/home/daniele/.config/mozilla/firefox/50b1zmic.default-release; cookie_read_probe=OK; no cookie values printed
real_download_672941=FDA_REFRESH_ATTEMPTS=1 FDA_SLEEP_REQUESTS=0 FDA_ABORT_ON_UNAVAILABLE=1 ./fda_downloader.sh --no-partials refresh-test URL; cookie_source=firefox; total_fragments=264; missing_count=1; missing_ranges=72; partial_deleted=yes; result=failed_external_HLS_404
browser_check_672941=FDA_BROWSER_CHECK_YTDLP_MODE=fragments ./fda_downloader.sh browser-check URL; report=state/browser-check-20260613-130553.txt; firefox_network=unavailable_by_design; ytdlp_http_statuses=404,404; ytdlp_fragment_errors=404/72,72; FINAL_REPORT=UNKNOWN
jdownloader_518407=JDownloader already running from /home/daniele/Downloads/JDownloader.jar pidfile=/home/daniele/Downloads/JDownloader.pid; Firefox profile checked=/home/daniele/.config/mozilla/firefox/50b1zmic.default-release; no JDownloader Firefox extension found; JDownloader log says Firefox settings folder not found; gallery URL accepted as clipboard job length 52 at 2026-06-13T13:20:28; no download/linkgrabber item produced; download list stayed empty; local HTTP API/CNL probes timed out or returned empty reply
browser_check_metadata=FDA_BROWSER_CHECK_SECONDS=1 FDA_BROWSER_CHECK_YTDLP_MODE=metadata ./fda_downloader.sh browser-check URL PASS; DevTools unavailable by design; chrome_verdict=UNKNOWN; ytdlp_rc=0; FINAL_REPORT=UNKNOWN; report=state/browser-check-20260610-164245.txt
diagnostic=yt-dlp with Chrome cookies+Referer+Origin+UA removed initial 403 and produced local MP4 diagnostic outside repo
script_test=started extraction/download; stopped by timeout after repeated HLS fragment 404; partial removed
refresh_test=FDA_REFRESH_ATTEMPTS=1 FDA_ABORT_ON_UNAVAILABLE=1 --no-partials refresh-test URL; result=expected_external_404; total_fragments=264; missing_count=1; missing_ranges=72; partial_deleted=yes
DATA:
db=none
paths=downloads,downloads/_partials,logs,state,private,state/browser-check-*.txt
backup=git remote private GitHub; generated media excluded
retention=operator_managed; raw logs sensitive
DNB:
dnb=do_not_add_cookie_export_or_store_browser_cookies_in_repo
dnb=do_not_add_DRM_or_auth_bypass_logic
dnb=do_not_report_full_signed_m3u8/mp4_URLs
dnb=do_not_log_cookie_token_or_complete_signed_URL_from_DevTools
dnb=do_not_force_HLS_when_Chrome_and_yt-dlp_both_receive_404; classify_server_playlist_or_content_problem
dnb=do_not_make_crawl_unbounded_or_cross-domain
dnb=do_not_reuse_old_m3u8_direct_URLs; always pass gallery/page URL to yt-dlp
BUG:
issue=HLS manifest accessible with headers but many segment requests return 404
cause=likely_signed_or_temporary_segment_URLs_or_playlist_references_unavailable_segments; v0.2.0 strict test failed at fragment 72 after fresh manifest
workaround=rerun refresh-test with fresh page/manifest; if still 404 document external stream limit
status=open_external_stream_limit
issue=Prompt 672941 Firefox cookie source did not solve gallery id=173 completion
cause=Firefox cookie read and manifest extraction succeeded, but fragment 72 returned 404 from HLS media host after fresh manifest
workaround=manual Firefox playback verification if needed; do not force or bypass protections
status=external_HLS_404
issue=Prompt 518407 JDownloader could not verify a successful authenticated download for gallery id=173
cause=JDownloader was installed/running but not integrated with the authenticated Firefox profile; clipboard URL was crawled/accepted but yielded no downloadable item, and no download reached the HLS fragment stage
workaround=manual JDownloader browser-extension/login setup would be required for a stronger JDownloader-specific test; do not export cookies or bypass protections
status=not_viable_as_configured
issue=browser-check may return UNKNOWN for Firefox real-session playback because Firefox Network capture is not automated by this wrapper
cause=do_not_remote_control_or_clone_logged_in_Firefox_profile_without_an_explicit_supported_protocol
workaround=use existing Firefox session for manual playback verification or switch to FDA_COOKIE_BROWSER=chrome for explicit Chrome DevTools diagnostics; keep reports redacted
status=by_design
RISK:
risk=signed_URL_leak; trigger=raw verbose log sharing; mitigation=chmod600+redacted summaries+gitignore logs; test=rg redaction in summaries
risk=incomplete_MP4; trigger=HLS fragment 404 skip; mitigation=segment_report+ffprobe+_partials_or_--no-partials; test=strict refresh-test deleted partial
risk=account/session misuse; trigger=wrong URL/account; mitigation=same-origin default+authorized-only docs
ROAD:
now=use refresh-test for HLS 404/scaduti and keep raw signed URL material local-only
next=only manual real-browser playback can add evidence; JDownloader as currently configured does not change the external-HLS-404 conclusion
later=UNKNOWN
LINK:
meta=../../../facedownassup-downloader/dev/project.metadata.json
human=../../human/projects/facedownassup-downloader/overview.md
repo=../../../facedownassup-downloader
readme=../../../facedownassup-downloader/README.md
OPEN:
open=Chrome UI playback automated status depends on explicit DevTools session and authenticated profile
open=If browser-check reports MATCH_404_SERVER_PLAYLIST_OR_CONTENT then gallery id=173 should be documented as server playlist/content failure and not forced
