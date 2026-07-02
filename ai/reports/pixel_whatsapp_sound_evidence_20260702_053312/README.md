# Pixel WhatsApp Sound Evidence - Redacted Summary

Date: 2026-07-02 CEST

This folder was used locally for raw ADB/UI/logcat evidence while diagnosing the WhatsApp notification sound issue. Raw files were intentionally not committed because several captures used `--noredact` or logcat and may contain personal notification metadata, contact identifiers, or message text.

Committed summary evidence:

- `individual_chat_defaults_4` was not the cause:
  - Android channel name: `Message notifications`.
  - `mImportance=4`.
  - `mSound=content://settings/system/notification_sound`.
  - `mVibrationEnabled=true`.
  - `mBypassDnd=false`.
  - Android UI showed `Default` selected and `Sound: Default notification sound`.
- WhatsApp in-app notification settings were audible:
  - conversation tones enabled.
  - message notification tone: `Default (Eureka)`.
  - group notification tone: `Default (Eureka)`.
  - high priority notifications enabled.
- Device-level audio gates were not the cause:
  - DND/Zen off: `zen_mode=0`.
  - ringer mode normal.
  - notification stream non-muted and non-zero.
  - notification/ring route on speaker, not an active Bluetooth audio route.
- Pre-fix root-cause channel:
  - `silent_notifications_6` / `Silent notifications`.
  - selected in UI as `Silent / No sound or vibration`.
  - `mImportance=2`.
  - `mSound=null`.
  - `mVibrationEnabled=false`.
- Notification grouping behavior:
  - WhatsApp posted a group summary on `silent_notifications_6`.
  - WhatsApp posted the child message on `individual_chat_defaults_4`.
  - `groupAlertBehavior=1` meant the summary path was the relevant alerting path for the grouped notification.
  - Result: the visible per-message channel looked audible, but the alerting summary channel was silent.
- Fix:
  - Android Settings > Apps > WhatsApp > Notifications > Silent notifications.
  - Changed from `Silent` to `Default`.
- Post-fix channel state:
  - `silent_notifications_6`.
  - `mImportance=3`.
  - `mSound=content://settings/system/notification_sound`.
  - `mBypassDnd=false`.
  - `mUserLockedFields=24`.
  - UI showed `Default` selected and `Sound: Default notification sound`.
- Validation:
  - Pixel locked/screen off.
  - User sent a WhatsApp message from another account/device.
  - User confirmed the Pixel emitted the notification sound.
  - Logcat showed WhatsApp push/background handling and SystemUI notification ringtone playback:
    - WhatsApp allowed via `PUSH_MESSAGING`.
    - `RingtonePlayer` played `content://settings/system/notification_sound`.
    - audio focus requested with `USAGE_NOTIFICATION`.
    - ringtone playback started.

No destructive actions were performed:

- WhatsApp was not uninstalled.
- WhatsApp data/cache were not cleared.
- WhatsApp was not logged out.
- Google Play Services was not reset or changed.
