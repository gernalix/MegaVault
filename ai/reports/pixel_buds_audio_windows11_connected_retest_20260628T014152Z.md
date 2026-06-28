# Pixel Buds Pro 2 Windows 11 connected retest

META:
created_utc=2026-06-28T01:41:52Z
host=DANIELE_PC
user=seste
pc=ThinkPad P14s Gen 5 AMD
os=Windows 11 Pro build 26200
protocol=MEGAVAULT_PROTOCOL.md VERSION=3
branch=codex/pixel-buds-windows-audio
report_path=C:\Users\seste\Documents\MegaVault\ai\reports\pixel_buds_audio_windows11_connected_retest_20260628T014152Z.md
log_dir=C:\Users\seste\Documents\windows\logs\pixel-buds-repair\20260628T014152Z
previous_report_1=C:\Users\seste\Documents\MegaVault\ai\reports\pixel_buds_audio_windows11_20260628T005406Z.md
previous_report_2=C:\Users\seste\Documents\MegaVault\ai\reports\pixel_buds_audio_windows11_followup_20260628T0106Z.md
previous_report_3=C:\Users\seste\Documents\MegaVault\ai\reports\pixel_buds_audio_windows11_third_attempt_20260628T012830Z.md

TITLE:
bug=Pixel Buds Pro 2 connected/default in Windows; verify real audio path.
attempt=connected_retest
status=PARTIAL_FIXED_ROUTING_VERIFIED_BUDS_AUDIO_RECONNECT_AND_BOTH_EARS_PENDING

CONTEXT:
why_previous_inconclusive=Buds were in case during earlier diagnostics; phantom/unplugged endpoint could be expected when not physically active.
current_physical_state_from_user=Buds fuori dal case/connesse.
current_active_state_from_user=Buds indossate o comunque attive.
windows_ui_from_user=Settings > System > Sound > Output shows Headphones / 2- D's Pixel Buds Pro 2 / Default device.
rule=Do not remove pairing/device stack or create automation unless real audio test justifies it.

PRIVILEGES:
whoami=seste\daniele
windows_principal_admin=False
net_session_command=net session
net_session_exit_code=2
net_session_output=System error 5 has occurred. Access is denied.
current_process=pwsh.exe via Codex Desktop MSIX command runner.
interpretation=Codex command runner not elevated; continue read-only diagnostics and audio test.

DIAG_CURRENT:
category_pre_audio=A_candidate_endpoint_active_default
coreaudio_buds_render=Headphones / Pixel Buds render endpoint state=1 Active.
coreaudio_buds_endpoint_id={0.0.0.00000000}.{29D565D0-6EDF-47D6-ABB2-93AB893BC12D}
pnp_buds_playback=Headphones (2- D's Pixel Buds Pro 2) Status=OK Problem=CM_PROB_NONE.
pnp_buds_capture=Headset (D's Pixel Buds Pro 2) Status=OK Problem=CM_PROB_NONE.
pnp_buds_bluetooth=D's Pixel Buds Pro 2 Status=OK Problem=CM_PROB_NONE.
pnp_buds_media=D's Pixel Buds Pro 2 Status=OK Problem=CM_PROB_NONE.
default_console=Headphones Pixel Buds state=1 Active.
default_multimedia=Headphones Pixel Buds state=1 Active.
default_communications=Headphones Pixel Buds state=1 Active.
other_active_playback=Speakers Realtek; 2 - SyncMaster AMD HDMI.
prior_phantom_status=Resolved when Buds are out of case/active.

SERVICES:
ApxSvc=Stopped Manual.
AudioEndpointBuilder=Running Automatic.
AudioSrv=Running Automatic.
bthserv=Running Manual.
DeviceAssociationService=Running Manual.
BTAGService=Running Manual.
BthAvctpSvc=Running Manual.
BluetoothUserService_11f663=Stopped Manual.

TASKS:
PixelBudsAudioRouteAtLogon=Disabled.
PixelBudsAudioRouteOnPnp=Disabled.
decision=Leave disabled until real audio test passes and reconnect persistence is known.

COMMANDS_EXECUTED:
cmd=Get-Content MegaVault protocol and three prior reports.
cmd=whoami; whoami /groups; whoami /priv; net session; Get-Process -Id $PID; WindowsPrincipal.IsInRole.
cmd=Get-CimInstance Win32_Process filtered Codex/OpenAI/PowerShell.
cmd=C:\Users\seste\Documents\windows\maintenance\Set-PixelBudsAudio.ps1 -StatusOnly.
cmd=Get-PnpDevice -Class AudioEndpoint.
cmd=Get-PnpDevice filtered Pixel/Buds/Google/Headphones/Headset/APX/BTHENUM/MMDEVAPI.
cmd=Registry read HKLM MMDevices Audio Render/Capture state/name.
cmd=Get-Service AudioSrv,AudioEndpointBuilder,bthserv,DeviceAssociationService,BTAGService,BthAvctpSvc,ApxSvc,BluetoothUserService_*.
cmd=Get-ScheduledTask PixelBudsAudioRouteAtLogon,PixelBudsAudioRouteOnPnp.

FAILED_COMMANDS:
failure=net session
exit_code=2
message=System error 5 has occurred. Access is denied.
interpretation=Runner non-admin; not relevant to read-only endpoint/default/audio test.

TEST_AUDIO:
summary=Multiple tests were run after confirming the Buds were out of the case and the Pixel Buds playback endpoint was Active/default.
initial_windows_wav_test=System.Media.SoundPlayer played C:\Windows\Media\Windows Notify Calendar.wav through default endpoint; user response: "non ho sentito niente".
initial_tone_test=A generated 880 Hz WAV was played via SoundPlayer; endpoint meter max stayed 0.0000 on Buds/Speakers/SyncMaster; user response still no sound.
vlc_test=A generated WAV was played via VLC; endpoint meters stayed 0.0000 on all render endpoints; VLC exited normally.
windows_settings_test_56=Native Settings > Sound > Headphones (2- D's Pixel Buds Pro 2) > Test at 56 percent; user response: "nessuno".
volume_max_test_setup=Per user request, active render endpoint volumes were temporarily set to 100 percent for Pixel Buds, Realtek Speakers, and SyncMaster HDMI.
windows_settings_test_100_before_fix=Native Windows Settings Buds Test at 100 percent before Dolby change; user response: "nessuno"; meters stayed 0.0000.
speaker_control_100=Native Windows Settings Speakers Test at 100 percent produced METER_MAX_SPEAKERS=0.9901 and Buds/SyncMaster remained 0.0000. This proves the Windows Settings test and meter capture were valid.
apxsvc_start_test=Started ApxSvc once through an explicit UAC elevated helper; log showed IsAdmin=True and Start-Service ApxSvc result=success.
windows_settings_test_after_apxsvc=Native Windows Settings Buds Test after ApxSvc start still produced no audible response from user and meters stayed 0.0000. ApxSvc alone was not sufficient.
dolby_change=Settings > Sound > Headphones (2- D's Pixel Buds Pro 2) > Audio enhancements changed from "Dolby Effect Pack BTH" to "Off".
windows_settings_test_after_dolby_off=Native Windows Settings Buds Test after disabling Dolby Effect Pack BTH produced METER_MAX_BUDS=0.9283, Speakers/SyncMaster 0.0000.
user_response_after_dolby_off="buds, ma credo solo la la sinistra, anche se non ne sono del tutto sicuro".
result=Routing to Buds is now verified at least once with real user-audible output and endpoint meter activity. Full both-ear/stereo and reconnect persistence are not yet verified.
volume_restore=After 100 percent tests, volumes were restored to Buds=56, Speakers=96, SyncMaster=100.
left_right_followup=A synthetic left/right WAV played through SoundPlayer after the fix produced no useful meter activity; SoundPlayer is unreliable for this Bluetooth/APX path and is not considered a valid regression test.
channel_balance_check=CoreAudio exposed the Pixel Buds render endpoint with channelCount=1, masterVolume=56, mute=False, and a single channel volume=56. There is no Windows L/R balance slider available on this endpoint to correct a right-ear-only/left-ear-only condition.

ROOT_CAUSE_UPDATED:
previous_attempt_issue=Earlier phantom/unplugged evidence was caused or confounded by the Buds being in the case/inactive. The automation created in earlier attempts could not fix a sleeping or phantom endpoint and was correctly left disabled.
effective_root_cause=With Buds awake, paired, active, and default, the audio path was still blackholed until the Bluetooth Dolby enhancement was disabled. The most probable root cause is the "Dolby Effect Pack BTH" APO/enhancement path breaking output for the Pixel Buds Pro 2 APX/LE Audio render endpoint.
secondary_factor=ApxSvc was stopped before the test and could be started elevated, but starting it alone did not restore audio. In final service snapshot ApxSvc was stopped again while the Buds endpoint remained Active/default, so ApxSvc is likely on-demand or secondary rather than the durable fix.
not_root_cause=Default endpoint selection was not the root cause during this retest; Console, Multimedia, and Communications defaults already pointed at the Pixel Buds render endpoint.
not_root_cause=Phantom/unplugged endpoint was not present during the valid connected retest; PnP status was OK / CM_PROB_NONE for Bluetooth, AudioEndpoint, and MEDIA devices.
open_question=User heard Buds after the Dolby fix but suspected possibly only the left bud. Windows exposes this endpoint as a single-channel APX/LE Audio endpoint, so there is no per-ear Windows balance setting to repair locally.

CHANGES_APPLIED:
system_changes=Disabled Audio enhancements for Headphones (2- D's Pixel Buds Pro 2) in Windows Settings, changing "Dolby Effect Pack BTH" to "Off".
system_changes=Started ApxSvc once through UAC elevated helper C:\Users\seste\Documents\windows\maintenance\Start-ApxAudioProxyElevated.ps1 for diagnostics. Final snapshot later showed ApxSvc stopped again; no persistent service start-mode change was made.
system_changes=Temporarily set active playback endpoint volumes to 100 percent for a controlled loud test, then restored original levels.
driver_changes=None.
device_removal=None.
script_or_task_created=None.
task_state_changed=None.
task_state=PixelBudsAudioRouteAtLogon remains Disabled.
task_state=PixelBudsAudioRouteOnPnp remains Disabled.
pairing_removed=None. Pairing/device stack was preserved because the endpoint became Active/default and then produced audio after the Dolby enhancement was disabled.
volume_final=Pixel Buds restored to 56 percent; Realtek Speakers restored to 96 percent; SyncMaster remains 100 percent.

FINAL_DIAG:
timestamp_utc=2026-06-28T04:27:47Z.
final_status_script=C:\Users\seste\Documents\windows\logs\pixel-buds-repair\20260628T014152Z\final-status-set-pixelbuds-audio.txt
final_pnp_buds_bluetooth=OK / CM_PROB_NONE.
final_pnp_buds_headset=OK / CM_PROB_NONE.
final_pnp_buds_headphones=OK / CM_PROB_NONE.
final_pnp_buds_media=OK / CM_PROB_NONE.
final_render_endpoint=Headphones state=1 Active id={0.0.0.00000000}.{29D565D0-6EDF-47D6-ABB2-93AB893BC12D}.
final_default_console=Headphones state=1 Active.
final_default_multimedia=Headphones state=1 Active.
final_default_communications=Headphones state=1 Active.
final_services=AudioEndpointBuilder Running; AudioSrv Running; bthserv Running; DeviceAssociationService Running; BTAGService Running; BthAvctpSvc Running; ApxSvc Stopped Manual.
final_tasks=PixelBudsAudioRouteAtLogon Disabled; PixelBudsAudioRouteOnPnp Disabled.

ROLLBACK:
dolby_change=Settings > System > Sound > Headphones (2- D's Pixel Buds Pro 2) > Audio enhancements can be changed back from Off to "Dolby Effect Pack BTH" if needed, but that is expected to reintroduce the silent-output bug.
apxsvc=No persistent service configuration was changed. If ApxSvc is running and needs to be stopped for testing, use elevated PowerShell: Stop-Service ApxSvc.
volumes=Volumes were restored after max-volume tests.
tasks=The two older routing tasks remain disabled; re-enable only if a future validated reason exists.
reports=Git revert report commit if needed.
logs=Delete C:\Users\seste\Documents\windows\logs\pixel-buds-repair\20260628T014152Z if no longer useful.

TODO:
todo=Run reconnect persistence test: put both Buds in case until Windows disconnects, take them out, wait for reconnect, verify Headphones endpoint Active/default and run the native Windows Settings Test again.
todo=Verify both-ear playback physically: both Buds charged, out of case, in ears, not simultaneously captured by phone/another device. User heard Buds after the fix but was unsure whether only the left bud played.
todo=If only one Bud continues to play, verify Pixel Buds firmware/state on Pixel phone and test the Buds on another source. Because Windows exposes this endpoint as one channel, there is no local Windows L/R balance fix currently visible.
todo=If silence returns while endpoint remains Active/default and enhancements remain Off, inspect Bluetooth LE Audio/APX toggles and Lenovo Vantage/Windows Update optional Bluetooth/audio drivers before considering a full remove/re-pair.
todo=Do not re-enable routing automation until real audio and reconnect persistence are both proven.

OUTCOME:
fixed=PARTIAL. Real audio through Pixel Buds was achieved after disabling Dolby Effect Pack BTH; routing bug is materially fixed for the tested connected session.
blocked=False.
next=Reconnect persistence and both-ear confirmation still required.
