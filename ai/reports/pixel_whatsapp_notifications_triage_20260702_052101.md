# Pixel WhatsApp notifications triage

Date: 2026-07-02 05:20 CEST
Device: Pixel 8a
Android: 17
Package: com.whatsapp
WhatsApp version: 2.26.25.80 (versionCode 262508000)
Evidence folder: ai/reports/pixel_whatsapp_notifications_evidence_20260702_051407

## Initial symptom

Pixel stopped receiving/showing WhatsApp notifications even though Android and WhatsApp UI settings appeared correct. Constraints followed: no uninstall, no WhatsApp data/cache clear, no logout, no destructive reset.

## Commands used

Preparation:

```powershell
adb devices
adb shell getprop ro.product.model
adb shell getprop ro.build.version.release
adb shell pm list packages | grep -i whatsapp
adb shell dumpsys package com.whatsapp | grep -i version
```

Notification state:

```powershell
adb shell cmd notification get_app_importance com.whatsapp
adb shell dumpsys package com.whatsapp | grep POST_NOTIFICATIONS
adb shell dumpsys notification --noredact | grep -i -A40 -B20 whatsapp
adb shell settings get global zen_mode
adb shell settings get global low_power
adb shell settings list secure | grep -iE 'focus|bedtime|zen|night|wellbeing'
adb shell settings list global | grep -iE 'focus|bedtime|zen|night|wellbeing'
```

Battery/background:

```powershell
adb shell cmd appops get com.whatsapp
adb shell cmd appops get com.whatsapp RUN_ANY_IN_BACKGROUND
adb shell cmd appops get com.whatsapp RUN_IN_BACKGROUND
adb shell cmd appops get com.whatsapp POST_NOTIFICATION
adb shell cmd appops get com.whatsapp WAKE_LOCK
adb shell dumpsys deviceidle whitelist
adb shell dumpsys usagestats | grep -i whatsapp
adb shell dumpsys jobscheduler | grep -i whatsapp
adb shell am get-standby-bucket com.whatsapp
adb shell dumpsys deviceidle
```

Network/FCM/validation:

```powershell
adb shell cmd appops get com.google.android.gms
adb shell am get-standby-bucket com.google.android.gms
adb shell dumpsys package com.google.android.gms | grep -i versionName
adb shell cmd netpolicy get restrict-background
adb shell cmd netpolicy list restrict-background-whitelist
adb shell cmd netpolicy list restrict-background-blacklist
adb logcat -c
adb shell input keyevent 223
adb logcat -v time | grep -iE "whatsapp|notification|fcm|gms|firebase|push|doze|deviceidle|appops"
```

Fix:

```powershell
adb shell cmd netpolicy remove restrict-background-blacklist 10363
adb shell cmd netpolicy list restrict-background-blacklist
adb shell am get-standby-bucket com.whatsapp
```

## Evidence collected

- ADB saw the physical Pixel: `adb-52131JEKB01070-Ne8QqZ._adb-tls-connect._tcp device`.
- Model/version: Pixel 8a, Android 17.
- WhatsApp package: `com.whatsapp`.
- WhatsApp version: `versionName=2.26.25.80`, `versionCode=262508000`.
- `cmd notification get_app_importance` is not supported on this Android build and returned `Unknown command: get_app_importance`; fallback was `dumpsys notification`.
- `POST_NOTIFICATIONS` is granted: `granted=true`.
- WhatsApp app notification importance is `DEFAULT`, user-set.
- Main WhatsApp message channels are not blocked:
  - `Message notifications`: `mImportance=4`.
  - `Group notifications`: `mImportance=4`.
  - `Chats` channel group: `mBlocked=false`.
- DND/Zen is currently off: `zen_mode=0` / `ZEN_MODE_OFF`.
- Battery saver is off: `low_power=0`.
- WhatsApp standby bucket is `10` (Active), not Rare/Restricted.
- Relevant WhatsApp appops are not blocking background execution/notifications:
  - `RUN_ANY_IN_BACKGROUND`: default allow.
  - `RUN_IN_BACKGROUND`: default allow.
  - `POST_NOTIFICATION`: default allow.
  - `WAKE_LOCK`: allow.
- WhatsApp package is not stopped/suspended/hidden/quarantined: `stopped=false`, `suspended=false`, `hidden=false`.
- Google Play Services appears healthy for push delivery checks available through ADB:
  - GMS standby bucket: `5`.
  - GMS `POST_NOTIFICATION` and `WAKE_LOCK`: allow.
  - GMS is in device idle whitelist.
- Important finding: `cmd netpolicy list restrict-background-blacklist` contained WhatsApp UID `10363` before the fix.
- `cmd netpolicy get restrict-background` reported global Data Saver/restrict background as disabled, but the per-UID blacklist entry is still the Android representation of app-level background data restriction and is a plausible cause on metered/cellular networks or policy transitions.
- Notification listeners are enabled for multiple apps, including notification saver / launcher / wearable services. No assistant was active. This is not the primary suspected root cause, but it is worth remembering if user-visible behavior differs from Android's notification state.

## Root cause most likely

Most likely root cause: WhatsApp's UID (`10363`) was in Android's `restrict-background-blacklist`, meaning background network access for WhatsApp had been restricted at the OS network policy layer.

This fits the symptom pattern where messages may arrive only when WhatsApp is opened, or delivery is unreliable while locked/backgrounded, especially on mobile data or networks treated as metered. The usual notification settings were not the root cause: permission, app importance, message channels, DND, battery saver, standby bucket, and key appops all looked OK.

## Fix applied

Applied one non-destructive, reversible fix:

```powershell
adb shell cmd netpolicy remove restrict-background-blacklist 10363
```

Verification after fix:

- WhatsApp UID `10363` no longer appears in `restrict-background-blacklist`.
- Global restrict background remains disabled.
- WhatsApp standby bucket remains `10` (Active).
- No WhatsApp data/cache was cleared.
- WhatsApp was not uninstalled or force-logged-out.
- No Google Play Services reset was performed.
- No Doze whitelist was added, because diagnostics did not justify it.

Reverse command, if ever needed:

```powershell
adb shell cmd netpolicy add restrict-background-blacklist 10363
```

## Validation

A post-fix 120-second logcat capture was run with the Pixel locked/screen off (`KEYCODE_SLEEP=223`). The filtered logcat captured device lock/Doze/GMS activity but did not capture a conclusive new WhatsApp/FCM delivery line. A later `cmd notification list` did not show an active WhatsApp notification at that exact inspection point.

Therefore validation is partially complete:

- Confirmed: the suspected OS-level policy restriction was removed.
- Confirmed: notification permissions/channels/background appops remain healthy.
- Not conclusively confirmed from ADB alone: a new locked-screen WhatsApp message produced banner/sound/vibration after the fix.

Recommended immediate validation step: with the phone locked and screen off, send a fresh WhatsApp message from another account/device while on both Wi-Fi and mobile data. Expected result after the fix: WhatsApp receives the message without opening the app, and Android posts it on the message channel.

## Risks and residuals

- The fix may increase WhatsApp background data usage, because it restores background network access for WhatsApp.
- If notifications still do not appear after this fix, next suspects are:
  - per-chat mute/archive settings inside WhatsApp;
  - lockscreen notification visibility/notification history behavior;
  - notification listener/wearable/saver apps altering user-visible notification handling;
  - network-specific issue (VPN, Private DNS, adblock, metered Wi-Fi, captive portal);
  - a WhatsApp-side registration/session/push token issue.
- The raw evidence files include `--noredact` outputs and may contain notification metadata. The report intentionally avoids copying personal names, message text, phone numbers, or notification contents.

## Next steps if the problem returns

1. Re-run:

```powershell
adb shell cmd netpolicy list restrict-background-blacklist
adb shell am get-standby-bucket com.whatsapp
adb shell dumpsys package com.whatsapp | grep POST_NOTIFICATIONS
adb shell dumpsys notification --noredact | grep -i -A40 -B20 whatsapp
```

2. If UID `10363` reappears in the blacklist, remove it again and inspect which Settings/app automation may be toggling background data.
3. Test on mobile data with Wi-Fi off, then on Wi-Fi with mobile data off.
4. Check WhatsApp Settings > Notifications and the specific chat(s) for mute/archive/custom notification overrides.
5. Temporarily disable notification saver/wearable mirroring apps only if Android posts WhatsApp notifications but the user does not see/hear them.
6. Consider temporary Doze whitelist only if a future logcat shows FCM delivery delayed until device unlock/open app.

## Validation addendum: user-confirmed WhatsApp test

A second validation was run after the user confirmed they were ready to send a WhatsApp message from another account/device.

Test window:

- Start: 2026-07-02 05:22:19 CEST.
- End: 2026-07-02 05:24:49 CEST.
- Device was put to sleep via `adb shell input keyevent 223` before the message was sent.
- Evidence files:
  - `30_logcat_validation_user_sent_message_filtered.txt`
  - `30_validation_user_sent_message_state.txt`

Result:

- Logcat shows Google Play Services / FCM handling at approximately 05:22:34.
- Android allowed WhatsApp to start foreground push handling from background via `PUSH_MESSAGING` with `com.google.android.c2dm.intent.RECEIVE`.
- WhatsApp process was unfrozen and `com.whatsapp/.messaging.service.GcmFGService` started.
- Android posted active WhatsApp notifications at approximately 05:22:35.
- `adb shell cmd notification list` showed active WhatsApp records after the test:
  - individual message notification: `com.whatsapp`, id `1`, non-null tag, UID `10363`.
  - group summary notification: `com.whatsapp`, id `1`, null tag, UID `10363`.
- The individual message notification used channel `individual_chat_defaults_4` with importance `4`.
- Notification record status was not intercepted and not hidden (`mIntercept=false`, `mHidden=false`).

Conclusion update:

The post-fix test confirms that, after removing WhatsApp UID `10363` from `restrict-background-blacklist`, the Pixel receives WhatsApp push while locked/screen-off and Android posts the WhatsApp notification without opening the app. This supports the netpolicy background-data restriction as the real root cause.

User-visible sound/vibration/banner still depends on the exact chat/channel sound settings and current device volume/vibration state, but Android delivery and notification posting are now confirmed.
