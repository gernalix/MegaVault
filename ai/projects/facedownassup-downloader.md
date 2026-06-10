META:
name=facedownassup-downloader
slug=facedownassup-downloader
path=/home/daniele/codex-workspace/facedownassup-downloader
remote=git@github.com:gernalix/facedownassup-downloader.git
branch=main
prompt=615902
verified_at=2026-06-10T17:35:00+02:00
protocol=MEGAVAULT_PROTOCOL.md:VERSION=8
PURPOSE:
purpose=Local authorized downloader for facedownassup.com member gallery pages using existing legitimate Chrome login via yt-dlp cookies.
scope=personal_access_only,no_DRM_bypass,no_paywall_bypass,no_credential_attack,no_exploit,no_aggressive_rate
STACK:
lang=Bash,Python_inline_parser
tools=yt-dlp 2026.06.09.230517,Chrome 149.0.7827.102,ffmpeg/ffprobe 6.1.1,gh,git
platform=Linux Mint/XFCE host
MAP:
entry=fda_downloader.sh
config=env:FDA_*,VERSION,dev/project.metadata.json
docs=README.md,MegaVault/human/projects/facedownassup-downloader/*
state=state/download-archive.txt,state/segments-*.txt,logs/run-*.log,private/crawl-*
output=downloads/<extractor>/<id> - <title>.<ext>
avoid=downloads,logs,state,private,cookies,*.dump,*.part,*.ytdl
ARCH:
script=fda_downloader.sh modes:doctor,refresh-test,browser-check,test,download,list,crawl
download=yt-dlp --cookies-from-browser chrome + Referer/Origin/User-Agent + no-cache + archive + local verbose logs
refresh=refresh-test checks Chrome playback status when possible, extracts fresh page/manifest immediately before download, reports segments, validates complete files with ffprobe, and handles partials
browser_check=explicit DevTools diagnostic; launches Chrome only with FDA_BROWSER_CHECK_LAUNCH=1; captures redacted .m3u8/.ts/.m4s Network status and compares with temporary yt-dlp probe
crawl=bounded same-origin gallery discovery from authorized HTML dumps; signed media URLs not persisted in reports
FLOW:
refresh-test=chrome_playback_check->fresh_preflight_write_pages_private->fresh_gallery_download->segment_report->ffprobe_or_partial_classification
browser-check=ensure_existing_or_explicit_chrome_devtools->open_authorized_url->Network.responseReceived/loadingFinished->redacted_media_report->temporary_ytdlp_probe->comparison->FINAL_REPORT
test=doctor->yt-dlp_cookie_extract->generic_gallery_page->html5_m3u8->hlsnative
list=read_urls->download_url_each->sleep_between_videos->archive_dedupe
crawl=start_page->write_pages_tmp->parse_gallery_links->state/crawl-found-*.txt
INV:
security=never_print_cookies_tokens_passwords_signed_urls_in_reports
auth=only_use_operator_Chrome_session_for_content_already_authorized
access=no_DRM/paywall/rate_limit/credential/protection_bypass
browser_diag=Chrome_remote_debugging_launch_only_when_FDA_BROWSER_CHECK_LAUNCH=1
data=raw_logs_local_only_chmod600; logs_may_contain_expiring_signed_URLs
ops=do_not_commit downloads/logs/state/private/cookies/dumps
version=VERSION and fda_downloader.sh SCRIPT_VERSION must move together
partials=complete_only_when_missing_count=0_and_ffprobe_passes; incomplete_outputs_move_to_downloads/_partials_or_delete_with_--no-partials
BUILD:
cmd=bash -n fda_downloader.sh
deps=yt-dlp,python3,Chrome_profile,ffmpeg
install=none; optional FDA_UPDATE_YTDLP=1 ./fda_downloader.sh doctor
TEST:
syntax=bash -n fda_downloader.sh PASS 2026-06-10 after v0.3.0
doctor=./fda_downloader.sh doctor PASS 2026-06-10; yt-dlp=2026.06.09.230517; Chrome=149.0.7827.102
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
issue=browser-check may return UNKNOWN if no explicit DevTools session is available or Chrome profile is not authenticated
cause=remote_debugging_intentionally_not_auto_started_without_FDA_BROWSER_CHECK_LAUNCH
workaround=start explicit debug session or rerun with FDA_BROWSER_CHECK_LAUNCH=1 using an authorized Chrome profile; keep reports redacted
status=by_design
RISK:
risk=signed_URL_leak; trigger=raw verbose log sharing; mitigation=chmod600+redacted summaries+gitignore logs; test=rg redaction in summaries
risk=incomplete_MP4; trigger=HLS fragment 404 skip; mitigation=segment_report+ffprobe+_partials_or_--no-partials; test=strict refresh-test deleted partial
risk=account/session misuse; trigger=wrong URL/account; mitigation=same-origin default+authorized-only docs
ROAD:
now=use refresh-test for HLS 404/scaduti and keep raw signed URL material local-only
next=use browser-check for real Chrome Network proof before deciding whether HLS 404 is external/server-side
later=UNKNOWN
LINK:
meta=../../../facedownassup-downloader/dev/project.metadata.json
human=../../human/projects/facedownassup-downloader/overview.md
repo=../../../facedownassup-downloader
readme=../../../facedownassup-downloader/README.md
OPEN:
open=Chrome UI playback automated status depends on explicit DevTools session and authenticated profile
open=If browser-check reports MATCH_404_SERVER_PLAYLIST_OR_CONTENT then gallery id=173 should be documented as server playlist/content failure and not forced
