# PROMPT_582941_ACTIVITYWATCH_REBOOT_AFTER
VERSION=1
STATUS=SUCCESS
DATE_START=2026-06-10T19:44:54+02:00
HOST=daniele-Surface-Pro
USER=daniele
PRE_BOOT_ID=07710fe0-0202-491a-ba46-475a6aa63555
POST_BOOT_ID=2210d0fc-f801-4be8-b7f5-0a60b13d3329
UPTIME= 19:44:54 up 0 min,  1 user,  load average: 6.80, 1.74, 0.59
TRIGGER=activitywatch-postreboot-582941.service
NOTE=generated_after_XFCE_login_by_temporary_user_systemd_verifier

SUMMARY_PRE_TEST:
wait_units_rc=0
wait_api_rc=0

## loginctl_show_user

```text
UID=1000
GID=1000
Name=daniele
Timestamp=Wed 2026-06-10 19:44:20 CEST
TimestampMonotonic=6585648
RuntimePath=/run/user/1000
Service=user@1000.service
Slice=user-1000.slice
Display=c2
State=active
Sessions=c2
IdleHint=no
IdleSinceHint=0
IdleSinceHintMonotonic=0
Linger=yes

[exit=0]
```

## systemd_user_environment

```text
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
DISPLAY=:0.0
XAUTHORITY=/home/daniele/.Xauthority
XDG_SESSION_TYPE=x11

[exit=0]
```

## unit_state_before_kill

```text
MainPID=1182
NRestarts=0
Id=aw-server.service
ActiveState=active
SubState=running
FragmentPath=/home/daniele/.config/systemd/user/aw-server.service
UnitFileState=enabled

Id=activitywatch-graphical-session.target
ActiveState=active
SubState=active
FragmentPath=/home/daniele/.config/systemd/user/activitywatch-graphical-session.target
UnitFileState=static

MainPID=21198
NRestarts=0
Id=aw-watcher-afk.service
ActiveState=active
SubState=running
FragmentPath=/home/daniele/.config/systemd/user/aw-watcher-afk.service
UnitFileState=enabled

MainPID=21295
NRestarts=0
Id=aw-watcher-window.service
ActiveState=active
SubState=running
FragmentPath=/home/daniele/.config/systemd/user/aw-watcher-window.service
UnitFileState=enabled

MainPID=21301
NRestarts=0
Id=aw-watcher-media-player.service
ActiveState=active
SubState=running
FragmentPath=/home/daniele/.config/systemd/user/aw-watcher-media-player.service
UnitFileState=enabled

[exit=0]
```

## unit_status_before_kill

```text
● aw-server.service - ActivityWatch server
     Loaded: loaded (/home/daniele/.config/systemd/user/aw-server.service; enabled; preset: enabled)
     Active: active (running) since Wed 2026-06-10 19:44:24 CEST; 50s ago
       Docs: https://activitywatch.net/
   Main PID: 1182 (aw-server)
      Tasks: 1 (limit: 7912)
     Memory: 85.0M (peak: 85.7M)
        CPU: 1.173s
     CGroup: /user.slice/user-1000.slice/user@1000.service/app.slice/aw-server.service
             └─1182 /home/daniele/.local/bin/aw-server

Jun 10 19:44:24 daniele-Surface-Pro systemd[963]: Started aw-server.service - ActivityWatch server.
Jun 10 19:44:28 daniele-Surface-Pro aw-server[1182]: 2026-06-10 19:44:28 [INFO ]: Using storage method: peewee  (aw_server.main:33)
Jun 10 19:44:28 daniele-Surface-Pro aw-server[1182]: 2026-06-10 19:44:28 [INFO ]: Using custom_static: {'aw-watcher-media-player': '/usr/share/aw-watcher-media-player/visualization'}  (aw_server.main:39)
Jun 10 19:44:28 daniele-Surface-Pro aw-server[1182]: 2026-06-10 19:44:28 [INFO ]: Starting up...  (aw_server.main:41)
Jun 10 19:44:28 daniele-Surface-Pro aw-server[1182]: 2026-06-10 19:44:28 [INFO ]: Using database file: /home/daniele/.local/share/activitywatch/aw-server/peewee-sqlite.v2.db  (aw_datastore.storages.peewee:150)
Jun 10 19:44:28 daniele-Surface-Pro aw-server[1182]:  * Serving Flask app 'aw-server'
Jun 10 19:44:28 daniele-Surface-Pro aw-server[1182]:  * Debug mode: off
Jun 10 19:44:28 daniele-Surface-Pro aw-server[1182]: 2026-06-10 19:44:28 [INFO ]: WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
Jun 10 19:44:28 daniele-Surface-Pro aw-server[1182]:  * Running on http://localhost:5600  (werkzeug:187)
Jun 10 19:44:28 daniele-Surface-Pro aw-server[1182]: 2026-06-10 19:44:28 [INFO ]: Press CTRL+C to quit  (werkzeug:187)

● activitywatch-graphical-session.target - ActivityWatch graphical/session watchers
     Loaded: loaded (/home/daniele/.config/systemd/user/activitywatch-graphical-session.target; static)
     Active: active since Wed 2026-06-10 19:44:54 CEST; 20s ago
       Docs: https://activitywatch.net/

Jun 10 19:44:54 daniele-Surface-Pro systemd[963]: Reached target activitywatch-graphical-session.target - ActivityWatch graphical/session watchers.

● aw-watcher-afk.service - ActivityWatch AFK watcher
     Loaded: loaded (/home/daniele/.config/systemd/user/aw-watcher-afk.service; enabled; preset: enabled)
     Active: active (running) since Wed 2026-06-10 19:44:54 CEST; 20s ago
       Docs: https://activitywatch.net/
    Process: 21115 ExecCondition=/bin/sh -lc test "${XDG_SESSION_TYPE:-}" = x11 && test -n "${DISPLAY:-}" (code=exited, status=0/SUCCESS)
    Process: 21152 ExecStartPre=/bin/sh -lc for i in $(seq 1 30); do curl -fsS http://127.0.0.1:5600/api/0/info >/dev/null && exit 0; sleep 1; done; exit 1 (code=exited, status=0/SUCCESS)
   Main PID: 21198 (aw-watcher-afk)
      Tasks: 4 (limit: 7912)
     Memory: 44.1M (peak: 47.9M)
        CPU: 774ms
     CGroup: /user.slice/user-1000.slice/user@1000.service/app.slice/aw-watcher-afk.service
             └─21198 /home/daniele/.local/bin/aw-watcher-afk

Jun 10 19:44:54 daniele-Surface-Pro systemd[963]: Starting aw-watcher-afk.service - ActivityWatch AFK watcher...
Jun 10 19:44:54 daniele-Surface-Pro systemd[963]: Started aw-watcher-afk.service - ActivityWatch AFK watcher.
Jun 10 19:44:56 daniele-Surface-Pro aw-watcher-afk[21198]: 2026-06-10 19:44:56 [INFO ]: aw-watcher-afk started  (aw_watcher_afk.afk:62)
Jun 10 19:44:57 daniele-Surface-Pro aw-watcher-afk[21198]: 2026-06-10 19:44:57 [INFO ]: Connection to aw-server established by aw-watcher-afk  (aw_client.client:447)

● aw-watcher-window.service - ActivityWatch window watcher
     Loaded: loaded (/home/daniele/.config/systemd/user/aw-watcher-window.service; enabled; preset: enabled)
     Active: active (running) since Wed 2026-06-10 19:44:55 CEST; 19s ago
       Docs: https://activitywatch.net/
    Process: 21165 ExecCondition=/bin/sh -lc test "${XDG_SESSION_TYPE:-}" = x11 && test -n "${DISPLAY:-}" (code=exited, status=0/SUCCESS)
    Process: 21230 ExecStartPre=/bin/sh -lc for i in $(seq 1 30); do curl -fsS http://127.0.0.1:5600/api/0/info >/dev/null && exit 0; sleep 1; done; exit 1 (code=exited, status=0/SUCCESS)
   Main PID: 21295 (aw-watcher-wind)
      Tasks: 2 (limit: 7912)
     Memory: 41.3M (peak: 42.8M)
        CPU: 673ms
     CGroup: /user.slice/user-1000.slice/user@1000.service/app.slice/aw-watcher-window.service
             └─21295 /home/daniele/.local/bin/aw-watcher-window

Jun 10 19:44:54 daniele-Surface-Pro systemd[963]: Starting aw-watcher-window.service - ActivityWatch window watcher...
Jun 10 19:44:55 daniele-Surface-Pro systemd[963]: Started aw-watcher-window.service - ActivityWatch window watcher.
Jun 10 19:44:56 daniele-Surface-Pro aw-watcher-window[21295]: 2026-06-10 19:44:56 [INFO ]: aw-watcher-window started  (aw_watcher_window.main:70)
Jun 10 19:44:57 daniele-Surface-Pro aw-watcher-window[21295]: 2026-06-10 19:44:57 [INFO ]: Connection to aw-server established by aw-watcher-window  (aw_client.client:447)

● aw-watcher-media-player.service - ActivityWatch media player watcher
     Loaded: loaded (/home/daniele/.config/systemd/user/aw-watcher-media-player.service; enabled; preset: enabled)
     Active: active (running) since Wed 2026-06-10 19:44:55 CEST; 19s ago
       Docs: https://activitywatch.net/
    Process: 21173 ExecCondition=/bin/sh -lc test -n "${DBUS_SESSION_BUS_ADDRESS:-}" (code=exited, status=0/SUCCESS)
    Process: 21234 ExecStartPre=/bin/sh -lc for i in $(seq 1 30); do curl -fsS http://127.0.0.1:5600/api/0/info >/dev/null && exit 0; sleep 1; done; exit 1 (code=exited, status=0/SUCCESS)
   Main PID: 21301 (aw-watcher-medi)
      Tasks: 6 (limit: 7912)
     Memory: 2.7M (peak: 3.6M)
        CPU: 157ms
     CGroup: /user.slice/user-1000.slice/user@1000.service/app.slice/aw-watcher-media-player.service
             └─21301 /usr/bin/aw-watcher-media-player --config /home/daniele/.config/activitywatch/aw-watcher-media-player/aw-watcher-media-player.toml

Jun 10 19:44:54 daniele-Surface-Pro systemd[963]: Starting aw-watcher-media-player.service - ActivityWatch media player watcher...
Jun 10 19:44:55 daniele-Surface-Pro systemd[963]: Started aw-watcher-media-player.service - ActivityWatch media player watcher.

[exit=0]
```

## enabled_state

```text
enabled
static
enabled
enabled
enabled

[exit=0]
```

## failed_units_before_kill

```text
  UNIT LOAD ACTIVE SUB DESCRIPTION

0 loaded units listed.

[exit=0]
```

## api_info_before_kill

```text
{"hostname": "daniele-Surface-Pro", "version": "v0.13.2", "testing": false, "device_id": "bf9949f3-475c-40b4-aa59-f7e2fcea16df"}

[exit=0]
```

## buckets_before_kill

```text
aw-watcher-afk_daniele-Surface-Pro
aw-watcher-media-player_daniele-Surface-Pro
aw-watcher-window_daniele-Surface-Pro

[exit=0]
```

## processes_before_kill

```text
1182 /home/daniele/.local/bin/aw-server
21198 /home/daniele/.local/bin/aw-watcher-afk
21295 /home/daniele/.local/bin/aw-watcher-window
21301 /usr/bin/aw-watcher-media-player --config /home/daniele/.config/activitywatch/aw-watcher-media-player/aw-watcher-media-player.toml
PID=1182
0::/user.slice/user-1000.slice/user@1000.service/app.slice/aw-server.service
PID=21198
0::/user.slice/user-1000.slice/user@1000.service/app.slice/aw-watcher-afk.service
PID=21295
0::/user.slice/user-1000.slice/user@1000.service/app.slice/aw-watcher-window.service
PID=21301
0::/user.slice/user-1000.slice/user@1000.service/app.slice/aw-watcher-media-player.service

[exit=0]
```

## critical_logs_before_kill

```text

[exit=0]
```

AUTORESTART_SERVER:
pid_before=1182
pid_after=34701
pid_changed=yes
api_after_server_kill_rc=0

## unit_state_after_server_kill

```text
MainPID=34701
NRestarts=1
Id=aw-server.service
ActiveState=active
SubState=running
FragmentPath=/home/daniele/.config/systemd/user/aw-server.service
UnitFileState=enabled

Id=activitywatch-graphical-session.target
ActiveState=active
SubState=active
FragmentPath=/home/daniele/.config/systemd/user/activitywatch-graphical-session.target
UnitFileState=static

MainPID=21198
NRestarts=0
Id=aw-watcher-afk.service
ActiveState=active
SubState=running
FragmentPath=/home/daniele/.config/systemd/user/aw-watcher-afk.service
UnitFileState=enabled

MainPID=21295
NRestarts=0
Id=aw-watcher-window.service
ActiveState=active
SubState=running
FragmentPath=/home/daniele/.config/systemd/user/aw-watcher-window.service
UnitFileState=enabled

MainPID=21301
NRestarts=0
Id=aw-watcher-media-player.service
ActiveState=active
SubState=running
FragmentPath=/home/daniele/.config/systemd/user/aw-watcher-media-player.service
UnitFileState=enabled

[exit=0]
```

## api_info_after_server_kill

```text
{"hostname": "daniele-Surface-Pro", "version": "v0.13.2", "testing": false, "device_id": "bf9949f3-475c-40b4-aa59-f7e2fcea16df"}

[exit=0]
```

AUTORESTART_WATCHERS:
afk_pid_before=21198
afk_pid_after=37959
afk_pid_changed=yes
window_pid_before=21295
window_pid_after=37950
window_pid_changed=yes
media_pid_before=21301
media_pid_after=37963
media_pid_changed=yes
api_after_watcher_kill_rc=0

## unit_state_after_watcher_kill

```text
MainPID=34701
NRestarts=1
Id=aw-server.service
ActiveState=active
SubState=running
FragmentPath=/home/daniele/.config/systemd/user/aw-server.service
UnitFileState=enabled

Id=activitywatch-graphical-session.target
ActiveState=active
SubState=active
FragmentPath=/home/daniele/.config/systemd/user/activitywatch-graphical-session.target
UnitFileState=static

MainPID=37959
NRestarts=1
Id=aw-watcher-afk.service
ActiveState=active
SubState=running
FragmentPath=/home/daniele/.config/systemd/user/aw-watcher-afk.service
UnitFileState=enabled

MainPID=37950
NRestarts=1
Id=aw-watcher-window.service
ActiveState=active
SubState=running
FragmentPath=/home/daniele/.config/systemd/user/aw-watcher-window.service
UnitFileState=enabled

MainPID=37963
NRestarts=1
Id=aw-watcher-media-player.service
ActiveState=active
SubState=running
FragmentPath=/home/daniele/.config/systemd/user/aw-watcher-media-player.service
UnitFileState=enabled

[exit=0]
```

## unit_status_after_watcher_kill

```text
● aw-server.service - ActivityWatch server
     Loaded: loaded (/home/daniele/.config/systemd/user/aw-server.service; enabled; preset: enabled)
     Active: active (running) since Wed 2026-06-10 19:45:20 CEST; 19s ago
       Docs: https://activitywatch.net/
   Main PID: 34701 (aw-server)
      Tasks: 1 (limit: 7912)
     Memory: 79.4M (peak: 85.2M)
        CPU: 1.221s
     CGroup: /user.slice/user-1000.slice/user@1000.service/app.slice/aw-server.service
             └─34701 /home/daniele/.local/bin/aw-server

Jun 10 19:45:20 daniele-Surface-Pro systemd[963]: Started aw-server.service - ActivityWatch server.
Jun 10 19:45:22 daniele-Surface-Pro aw-server[34701]: 2026-06-10 19:45:22 [INFO ]: Using storage method: peewee  (aw_server.main:33)
Jun 10 19:45:22 daniele-Surface-Pro aw-server[34701]: 2026-06-10 19:45:22 [INFO ]: Using custom_static: {'aw-watcher-media-player': '/usr/share/aw-watcher-media-player/visualization'}  (aw_server.main:39)
Jun 10 19:45:22 daniele-Surface-Pro aw-server[34701]: 2026-06-10 19:45:22 [INFO ]: Starting up...  (aw_server.main:41)
Jun 10 19:45:22 daniele-Surface-Pro aw-server[34701]: 2026-06-10 19:45:22 [INFO ]: Using database file: /home/daniele/.local/share/activitywatch/aw-server/peewee-sqlite.v2.db  (aw_datastore.storages.peewee:150)
Jun 10 19:45:22 daniele-Surface-Pro aw-server[34701]:  * Serving Flask app 'aw-server'
Jun 10 19:45:22 daniele-Surface-Pro aw-server[34701]:  * Debug mode: off
Jun 10 19:45:22 daniele-Surface-Pro aw-server[34701]: 2026-06-10 19:45:22 [INFO ]: WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
Jun 10 19:45:22 daniele-Surface-Pro aw-server[34701]:  * Running on http://localhost:5600  (werkzeug:187)
Jun 10 19:45:22 daniele-Surface-Pro aw-server[34701]: 2026-06-10 19:45:22 [INFO ]: Press CTRL+C to quit  (werkzeug:187)

● activitywatch-graphical-session.target - ActivityWatch graphical/session watchers
     Loaded: loaded (/home/daniele/.config/systemd/user/activitywatch-graphical-session.target; static)
     Active: active since Wed 2026-06-10 19:44:54 CEST; 45s ago
       Docs: https://activitywatch.net/

Jun 10 19:44:54 daniele-Surface-Pro systemd[963]: Reached target activitywatch-graphical-session.target - ActivityWatch graphical/session watchers.

● aw-watcher-afk.service - ActivityWatch AFK watcher
     Loaded: loaded (/home/daniele/.config/systemd/user/aw-watcher-afk.service; enabled; preset: enabled)
     Active: active (running) since Wed 2026-06-10 19:45:33 CEST; 6s ago
       Docs: https://activitywatch.net/
    Process: 37857 ExecCondition=/bin/sh -lc test "${XDG_SESSION_TYPE:-}" = x11 && test -n "${DISPLAY:-}" (code=exited, status=0/SUCCESS)
    Process: 37908 ExecStartPre=/bin/sh -lc for i in $(seq 1 30); do curl -fsS http://127.0.0.1:5600/api/0/info >/dev/null && exit 0; sleep 1; done; exit 1 (code=exited, status=0/SUCCESS)
   Main PID: 37959 (aw-watcher-afk)
      Tasks: 4 (limit: 7912)
     Memory: 71.7M (peak: 71.9M)
        CPU: 869ms
     CGroup: /user.slice/user-1000.slice/user@1000.service/app.slice/aw-watcher-afk.service
             └─37959 /home/daniele/.local/bin/aw-watcher-afk

Jun 10 19:45:32 daniele-Surface-Pro systemd[963]: aw-watcher-afk.service: Scheduled restart job, restart counter is at 1.
Jun 10 19:45:32 daniele-Surface-Pro systemd[963]: Starting aw-watcher-afk.service - ActivityWatch AFK watcher...
Jun 10 19:45:33 daniele-Surface-Pro systemd[963]: Started aw-watcher-afk.service - ActivityWatch AFK watcher.
Jun 10 19:45:35 daniele-Surface-Pro aw-watcher-afk[37959]: 2026-06-10 19:45:35 [INFO ]: aw-watcher-afk started  (aw_watcher_afk.afk:62)
Jun 10 19:45:36 daniele-Surface-Pro aw-watcher-afk[37959]: 2026-06-10 19:45:36 [INFO ]: Connection to aw-server established by aw-watcher-afk  (aw_client.client:447)

● aw-watcher-window.service - ActivityWatch window watcher
     Loaded: loaded (/home/daniele/.config/systemd/user/aw-watcher-window.service; enabled; preset: enabled)
     Active: active (running) since Wed 2026-06-10 19:45:33 CEST; 6s ago
       Docs: https://activitywatch.net/
    Process: 37862 ExecCondition=/bin/sh -lc test "${XDG_SESSION_TYPE:-}" = x11 && test -n "${DISPLAY:-}" (code=exited, status=0/SUCCESS)
    Process: 37907 ExecStartPre=/bin/sh -lc for i in $(seq 1 30); do curl -fsS http://127.0.0.1:5600/api/0/info >/dev/null && exit 0; sleep 1; done; exit 1 (code=exited, status=0/SUCCESS)
   Main PID: 37950 (aw-watcher-wind)
      Tasks: 2 (limit: 7912)
     Memory: 67.5M (peak: 68.2M)
        CPU: 761ms
     CGroup: /user.slice/user-1000.slice/user@1000.service/app.slice/aw-watcher-window.service
             └─37950 /home/daniele/.local/bin/aw-watcher-window

Jun 10 19:45:32 daniele-Surface-Pro systemd[963]: aw-watcher-window.service: Scheduled restart job, restart counter is at 1.
Jun 10 19:45:32 daniele-Surface-Pro systemd[963]: Starting aw-watcher-window.service - ActivityWatch window watcher...
Jun 10 19:45:33 daniele-Surface-Pro systemd[963]: Started aw-watcher-window.service - ActivityWatch window watcher.
Jun 10 19:45:35 daniele-Surface-Pro aw-watcher-window[37950]: 2026-06-10 19:45:35 [INFO ]: aw-watcher-window started  (aw_watcher_window.main:70)
Jun 10 19:45:36 daniele-Surface-Pro aw-watcher-window[37950]: 2026-06-10 19:45:36 [INFO ]: Connection to aw-server established by aw-watcher-window  (aw_client.client:447)

● aw-watcher-media-player.service - ActivityWatch media player watcher
     Loaded: loaded (/home/daniele/.config/systemd/user/aw-watcher-media-player.service; enabled; preset: enabled)
     Active: active (running) since Wed 2026-06-10 19:45:33 CEST; 6s ago
       Docs: https://activitywatch.net/
    Process: 37877 ExecCondition=/bin/sh -lc test -n "${DBUS_SESSION_BUS_ADDRESS:-}" (code=exited, status=0/SUCCESS)
    Process: 37926 ExecStartPre=/bin/sh -lc for i in $(seq 1 30); do curl -fsS http://127.0.0.1:5600/api/0/info >/dev/null && exit 0; sleep 1; done; exit 1 (code=exited, status=0/SUCCESS)
   Main PID: 37963 (aw-watcher-medi)
      Tasks: 7 (limit: 7912)
     Memory: 6.6M (peak: 7.3M)
        CPU: 181ms
     CGroup: /user.slice/user-1000.slice/user@1000.service/app.slice/aw-watcher-media-player.service
             └─37963 /usr/bin/aw-watcher-media-player --config /home/daniele/.config/activitywatch/aw-watcher-media-player/aw-watcher-media-player.toml

Jun 10 19:45:32 daniele-Surface-Pro systemd[963]: aw-watcher-media-player.service: Scheduled restart job, restart counter is at 1.
Jun 10 19:45:32 daniele-Surface-Pro systemd[963]: Starting aw-watcher-media-player.service - ActivityWatch media player watcher...
Jun 10 19:45:33 daniele-Surface-Pro systemd[963]: Started aw-watcher-media-player.service - ActivityWatch media player watcher.

[exit=0]
```

## api_info_after_watcher_kill

```text
{"hostname": "daniele-Surface-Pro", "version": "v0.13.2", "testing": false, "device_id": "bf9949f3-475c-40b4-aa59-f7e2fcea16df"}

[exit=0]
```

## buckets_after_watcher_kill

```text
aw-watcher-afk_daniele-Surface-Pro
aw-watcher-media-player_daniele-Surface-Pro
aw-watcher-window_daniele-Surface-Pro

[exit=0]
```

## failed_units_final

```text
  UNIT LOAD ACTIVE SUB DESCRIPTION

0 loaded units listed.

[exit=0]
```

## critical_logs_final

```text
Jun 10 19:45:15 daniele-Surface-Pro systemd[963]: aw-server.service: Failed with result 'signal'.
Jun 10 19:45:17 daniele-Surface-Pro aw-watcher-window[21295]: 2026-06-10 19:45:17 [ERROR]: Unknown error, not retrying: {'id': None, 'timestamp': '2026-06-10T17:45:15.019000+00:00', 'duration': 1.047, 'data': {'app': 'Insync', 'title': 'Insync'}}  (aw_client.client:499)
Jun 10 19:45:17 daniele-Surface-Pro aw-watcher-window[21295]: Traceback (most recent call last):
Jun 10 19:45:17 daniele-Surface-Pro aw-watcher-window[21295]: ConnectionRefusedError: [Errno 111] Connection refused
Jun 10 19:45:17 daniele-Surface-Pro aw-watcher-window[21295]: During handling of the above exception, another exception occurred:
Jun 10 19:45:17 daniele-Surface-Pro aw-watcher-window[21295]: Traceback (most recent call last):
Jun 10 19:45:17 daniele-Surface-Pro aw-watcher-window[21295]: urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x76d5778637c0>: Failed to establish a new connection: [Errno 111] Connection refused
Jun 10 19:45:17 daniele-Surface-Pro aw-watcher-window[21295]: During handling of the above exception, another exception occurred:
Jun 10 19:45:17 daniele-Surface-Pro aw-watcher-window[21295]: Traceback (most recent call last):
Jun 10 19:45:17 daniele-Surface-Pro aw-watcher-window[21295]: urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='127.0.0.1', port=5600): Max retries exceeded with url: /api/0/buckets/aw-watcher-window_daniele-Surface-Pro/heartbeat?pulsetime=2.0 (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x76d5778637c0>: Failed to establish a new connection: [Errno 111] Connection refused'))
Jun 10 19:45:17 daniele-Surface-Pro aw-watcher-window[21295]: During handling of the above exception, another exception occurred:
Jun 10 19:45:17 daniele-Surface-Pro aw-watcher-window[21295]: Traceback (most recent call last):
Jun 10 19:45:17 daniele-Surface-Pro aw-watcher-window[21295]: requests.exceptions.ConnectionError: HTTPConnectionPool(host='127.0.0.1', port=5600): Max retries exceeded with url: /api/0/buckets/aw-watcher-window_daniele-Surface-Pro/heartbeat?pulsetime=2.0 (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x76d5778637c0>: Failed to establish a new connection: [Errno 111] Connection refused'))
Jun 10 19:45:21 daniele-Surface-Pro aw-watcher-window[21295]: 2026-06-10 19:45:21 [ERROR]: Unknown error, not retrying: {'id': None, 'timestamp': '2026-06-10T17:45:17.068000+00:00', 'duration': 3.042, 'data': {'app': 'Thunar', 'title': 'SuperContacts - Thunar'}}  (aw_client.client:499)
Jun 10 19:45:21 daniele-Surface-Pro aw-watcher-window[21295]: Traceback (most recent call last):
Jun 10 19:45:21 daniele-Surface-Pro aw-watcher-window[21295]: ConnectionRefusedError: [Errno 111] Connection refused
Jun 10 19:45:21 daniele-Surface-Pro aw-watcher-window[21295]: During handling of the above exception, another exception occurred:
Jun 10 19:45:21 daniele-Surface-Pro aw-watcher-window[21295]: Traceback (most recent call last):
Jun 10 19:45:21 daniele-Surface-Pro aw-watcher-window[21295]: urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x76d577872340>: Failed to establish a new connection: [Errno 111] Connection refused
Jun 10 19:45:21 daniele-Surface-Pro aw-watcher-window[21295]: During handling of the above exception, another exception occurred:
Jun 10 19:45:21 daniele-Surface-Pro aw-watcher-window[21295]: Traceback (most recent call last):
Jun 10 19:45:21 daniele-Surface-Pro aw-watcher-window[21295]: urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='127.0.0.1', port=5600): Max retries exceeded with url: /api/0/buckets/aw-watcher-window_daniele-Surface-Pro/heartbeat?pulsetime=2.0 (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x76d577872340>: Failed to establish a new connection: [Errno 111] Connection refused'))
Jun 10 19:45:21 daniele-Surface-Pro aw-watcher-window[21295]: During handling of the above exception, another exception occurred:
Jun 10 19:45:21 daniele-Surface-Pro aw-watcher-window[21295]: Traceback (most recent call last):
Jun 10 19:45:21 daniele-Surface-Pro aw-watcher-window[21295]: requests.exceptions.ConnectionError: HTTPConnectionPool(host='127.0.0.1', port=5600): Max retries exceeded with url: /api/0/buckets/aw-watcher-window_daniele-Surface-Pro/heartbeat?pulsetime=2.0 (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x76d577872340>: Failed to establish a new connection: [Errno 111] Connection refused'))
Jun 10 19:45:22 daniele-Surface-Pro aw-watcher-window[21295]: 2026-06-10 19:45:22 [ERROR]: Unknown error, not retrying: {'id': None, 'timestamp': '2026-06-10T17:45:21.625000+00:00', 'duration': 0.0, 'data': {'app': 'Thunar', 'title': 'codex-workspace - Thunar'}}  (aw_client.client:499)
Jun 10 19:45:22 daniele-Surface-Pro aw-watcher-window[21295]: Traceback (most recent call last):
Jun 10 19:45:22 daniele-Surface-Pro aw-watcher-window[21295]: ConnectionRefusedError: [Errno 111] Connection refused
Jun 10 19:45:22 daniele-Surface-Pro aw-watcher-window[21295]: During handling of the above exception, another exception occurred:
Jun 10 19:45:22 daniele-Surface-Pro aw-watcher-window[21295]: Traceback (most recent call last):
Jun 10 19:45:22 daniele-Surface-Pro aw-watcher-window[21295]: urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x76d577872d00>: Failed to establish a new connection: [Errno 111] Connection refused
Jun 10 19:45:22 daniele-Surface-Pro aw-watcher-window[21295]: During handling of the above exception, another exception occurred:
Jun 10 19:45:22 daniele-Surface-Pro aw-watcher-window[21295]: Traceback (most recent call last):
Jun 10 19:45:22 daniele-Surface-Pro aw-watcher-window[21295]: urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='127.0.0.1', port=5600): Max retries exceeded with url: /api/0/buckets/aw-watcher-window_daniele-Surface-Pro/heartbeat?pulsetime=2.0 (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x76d577872d00>: Failed to establish a new connection: [Errno 111] Connection refused'))
Jun 10 19:45:22 daniele-Surface-Pro aw-watcher-window[21295]: During handling of the above exception, another exception occurred:
Jun 10 19:45:22 daniele-Surface-Pro aw-watcher-window[21295]: Traceback (most recent call last):
Jun 10 19:45:22 daniele-Surface-Pro aw-watcher-window[21295]: requests.exceptions.ConnectionError: HTTPConnectionPool(host='127.0.0.1', port=5600): Max retries exceeded with url: /api/0/buckets/aw-watcher-window_daniele-Surface-Pro/heartbeat?pulsetime=2.0 (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x76d577872d00>: Failed to establish a new connection: [Errno 111] Connection refused'))
Jun 10 19:45:27 daniele-Surface-Pro systemd[963]: aw-watcher-afk.service: Failed with result 'signal'.
Jun 10 19:45:27 daniele-Surface-Pro systemd[963]: aw-watcher-window.service: Failed with result 'signal'.
Jun 10 19:45:27 daniele-Surface-Pro systemd[963]: aw-watcher-media-player.service: Failed with result 'signal'.

[exit=0]
```

FINAL_RESULT:
date_end=2026-06-10T19:45:40+02:00
physical_reboot_verified=yes
aw_server_active=active
activitywatch_target_active=active
afk_active=active
window_active=active
media_active=active
final_failed_count=0
server_pid_changed=yes
afk_pid_changed=yes
window_pid_changed=yes
media_pid_changed=yes
data_db_modified=no
reinstall=no

POST_VERIFICATION_NOTES:
critical_log_explanation=Failed_with_result_signal_and_connection_refused_entries_at_19:45_are_expected_from_deliberate_SIGKILL_autorestart_test
post_test_warning=20:18_aw-watcher-window_BadWindow_X11_warning_only;service_remained_active;not_autostart_failure
temporary_verifier=activitywatch-postreboot-582941.service_disabled_after_run;removed_after_report_collection
manual_gui_note=/home/daniele/.local/bin/activitywatch_aw-qt_observed_after_test_with_parent_whisker_menu;not_required_for_service_autostart;server_and_watchers_remain_single_systemd_services

REBOOT_ATTRIBUTION_CLOSURE_204638:
verdict=confirmed_by_equivalent_evidence;reboot_2026-06-10T19:43:43+02:00_was_activitywatch_autostart_test_reboot_from_Codex_prompt_582941
primary_evidence=terminal_logger_clean_log_019eb28f_lines_6296_6317_Codex_announced_controlled_physical_reboot_at_2026-06-10T17:43:42.665Z;system_journal_logind_reboot_at_2026-06-10T19:43:43+02:00
exact_command=not_preserved_in_available_terminal_logger_or_shell_history;mechanism=ordered_logind_reboot_with_ACTION_reboot_OPERATOR_daniele
not_cause=zram,OOM,kernel_panic,watchdog,thermal,brownout,USB_storage_reset
closure_note=reboot_was_expected_test_artifact_for_ActivityWatch_autostart/autorestart_verification;not_spontaneous_failure
