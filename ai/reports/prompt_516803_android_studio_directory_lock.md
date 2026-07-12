META:
activity_id=516803
timestamp_utc=2026-07-12T11:23:44Z
host=fedora Fedora_Linux_44_Workstation
result=PASS
scope=Android Studio Flatpak DirectoryLock diagnosis, minimal recovery, graphical launch-close regression

INSTALLATION:
type=Flatpak system installation from flathub
application_id=com.google.AndroidStudio
version=2026.1.1.10
commit=29500a3ec68b584dcc76f5d18862624ebbde260ac4f0349305bf1220bbef6c76
gnome_desktop=/var/lib/flatpak/exports/share/applications/com.google.AndroidStudio.desktop
gnome_exec=/usr/bin/flatpak run --branch=stable --arch=x86_64 --command=android-studio-wrapper --file-forwarding com.google.AndroidStudio
studio_command=/app/extra/bin/studio
jre=/app/extra/jbr JRE_21.0.10+-14961533-b1163.108
duplicates=none found in Flatpak,RPM,/opt,/usr/local,user launchers,or JetBrains Toolbox
flatpak_overrides=none at global,user,or app scope; manifest permissions include home access and JAVA_HOME=/app/extra/jbr

PATHS:
config=/home/daniele/.var/app/com.google.AndroidStudio/config/Google/AndroidStudio2026.1.1
system_cache=/home/daniele/.var/app/com.google.AndroidStudio/cache/Google/AndroidStudio2026.1.1
log=/home/daniele/.var/app/com.google.AndroidStudio/cache/Google/AndroidStudio2026.1.1/log/idea.log
custom_plugins=/home/daniele/.var/app/com.google.AndroidStudio/data/Google/AndroidStudio2026.1.1;absent=no custom plugin directory
bundled_plugins=/app/extra/plugins;loaded list verified in idea.log
sdk=/home/daniele/Android/Sdk
avd=/home/daniele/.android/avd

INCIDENT:
incident_id=ANDROID_STUDIO_FLATPAK_STALE_DIRECTORYLOCK_SOCKET
symptom=DirectoryLock CannotActivateException with BindException Address already in use and ConnectException Connection refused
first_stale_artifact_utc=2026-07-09T17:11:52Z
confirmed_failed_launch_utc=2026-07-12T11:08:04Z
root_cause=The Android Studio session started 2026-07-09T17:11:52Z did not complete IDE shutdown after its last log activity on 2026-07-10. Its filesystem Unix socket .port and DirectoryLock markers remained although no Studio process or Flatpak instance existed. A new process could not bind the pathname and could not connect because no listener owned it.
classification=C stale socket or lock without process owner;preceded by incomplete Flatpak IDE shutdown
pid_namespace=3;the IDE is PID 3 inside its Flatpak PID namespace,not host PID 3
stale_owner_host_pid=UNKNOWN;process had already exited and idea.log records only namespace PID 3
failed_launch_host_pid=16895 from journal com.google.AndroidStudio.desktop/studio
verified_mapping_examples=host 59180->NSpid 3;host 87969->NSpid 3;host 96823->NSpid 3;namespace 4026533357
processes_terminated=none
signals_used=none;all successful test instances received normal WM_DELETE_WINDOW and logged IDE_SHUTDOWN

STALE_ARTIFACTS:
artifact=/home/daniele/.var/app/com.google.AndroidStudio/cache/Google/AndroidStudio2026.1.1/.port;socket;inode=63152;owner=daniele:daniele;mode=srwxr-xr-x;mtime=2026-07-09T17:11:52.444543734Z;owners=none by ss,lsof,fuser,/proc/net/unix
artifact=/home/daniele/.var/app/com.google.AndroidStudio/cache/Google/AndroidStudio2026.1.1/.pid;regular;inode=15455;owner=daniele:daniele;mode=-rw-r--r--;content=3;mtime=2026-07-09T17:11:53.038533215Z
artifact=/home/daniele/.var/app/com.google.AndroidStudio/config/Google/AndroidStudio2026.1.1/.lock;regular;inode=63153;owner=daniele:daniele;mode=-rw-r--r--;content=3;mtime=2026-07-09T17:11:52.448543663Z
backup=/home/daniele/.local/state/android-studio-recovery/activity-516803-20260712T131700+0200
fix=Moved only .port,.pid,.lock to backup after proving no Studio process,Flatpak instance,listener,or file owner existed;no cache,config,SDK,AVD,project,or plugin deletion.
backup_retention=preserved;not deleted
incident_sqlite=/home/daniele/sync_root/db/incident_registry.sqlite;upserted+event_appended+integrity_check_ok
incident_sqlite_backup=/home/daniele/sync_root/db/backups/incident_registry.activity-516803.pre-update.20260712T112344Z.sqlite;mode=0600

TESTS:
first_launch=PASS;exact android-studio-wrapper;host PID 59180,NSpid 3;new .port owned by studio fd 11;main XWayland window MultiTimeTracker IsViewable Normal 2800x1776;two title queries responsive;no DirectoryLock errors
first_close=PASS;normal WM_DELETE_WINDOW;IDE_SHUTDOWN at 2026-07-12T11:18:03.794Z;host PID,sandbox,.port,.lock released
second_launch=PASS;exact desktop Exec supervised under transient user unit;host PID 87969,NSpid 3;main window MultiTimeTracker IsViewable Normal 2800x1776;two title queries responsive;no DirectoryLock errors
second_close=PASS;normal WM_DELETE_WINDOW;IDE_SHUTDOWN at 2026-07-12T11:22:13.908Z;host PID,sandbox,.port,.lock released
final_reopen=PASS;host PID 96823,NSpid 3;main window IsViewable and title progressed to MultiTimeTracker;socket owned by studio;normal close;IDE_SHUTDOWN at 2026-07-12T11:22:49.955Z
final_runtime=PASS;no Android Studio process,Flatpak instance,.port,or .lock;only normal persistent .pid marker remains
log_regression=PASS;no new DirectoryLock,CannotActivateException,Address already in use,or Connection refused after fix
vfs_recovery=PASS;first fixed start logged NOT_CLOSED_PROPERLY recovered,no problems remain

DATA_PRESERVATION:
sdk=PASS;build-tools,cmdline-tools,emulator,platform-tools,platforms,skins,sources,system-images present
plugins=PASS;bundled Android,Kotlin,Gradle,Compose,Firebase,NDK and related plugins loaded;no custom plugin directory existed before or after
avd=PASS;Luoghi_API35_Google_x86_64 and Luoghi_API36_Google_x86_64 listed by avdmanager
adb=PASS;server PID 2819 remained listening on 127.0.0.1:5037;adb-device-keeper.service remained active+enabled;two configured Wi-Fi devices remained device
projects=PASS;no project source edit made;MultiTimeTracker .idea/codeStyles was already untracked with birth timestamp 2026-07-09T19:54:51Z

BLOCKERS:
resolved=The first pgrep safety expression matched its own diagnostic shell;precondition exited 42 before writes;replacement used exact process names plus Flatpak state.
resolved=Java Access Bridge did not expose Android Studio in AT-SPI;because idea.log proved XToolkit,the graphical gate used XWayland xwininfo,wmctrl,xprop,and xdotool.
resolved=Unsustained gtk-launch commands caused bwrap --die-with-parent to end a test sandbox;the resulting test-only .port and .lock were proven ownerless and preserved under backup/test-harness-interrupted-launch. Reliable later tests ran the exact desktop Exec as the main process of transient user units.

PREVENTION:
procedure=After a crash,first verify flatpak ps,pgrep/ps,NSpid,ss,lsof,and fuser. Only when no valid Studio instance or listener exists,move .port and .lock to a timestamped backup. Never kill host PID 3 and never automate blind lock deletion.
automation=none created;no lock cleanup service or launcher override added

EVIDENCE:
command=flatpak info com.google.AndroidStudio;flatpak ps;ps;pgrep;lsns;/proc/PID/status;ss -xlpn;lsof;fuser;stat;od;journalctl;idea.log;xwininfo;wmctrl;xprop;xdotool;avdmanager;adb devices -l;systemctl --user
journal=2026-07-12T11:08:04Z studio host PID 16895 emitted CannotActivateException plus BindException and ConnectException
namespace=/proc/59180/status NSpid 59180 3 and /proc/87969/status NSpid 87969 3
socket=ss showed .port LISTEN owned by studio host PID 59180 or 87969 after fix;normal shutdown removed pathname

GIT:
megavault_initial=clean on codex/684219-t7-connect-backup-global tracking origin
project_observed=/home/daniele/projects/MultiTimeTracker had pre-existing untracked .idea/codeStyles;not modified or removed
