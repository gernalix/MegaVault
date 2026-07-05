# prompt_739284 home-backup bwlimit follow-up

date=2026-06-13
host=daniele-Surface-Pro
scope=home-incremental-backup.service status+I/O measurement+bwlimit_config_change
protocol=../MEGAVAULT_PROTOCOL.md
host_profile=../global/HOST_PROFILE.md
prior_report=prompt_483920_external_disk_io_diagnosis.md

SUMMARY:
backup_state=active_running;systemd=activating/start expected_for_long_oneshot;not_blocked
service=home-incremental-backup.service user;started=2026-06-13T05:25:53+02:00;MainPID=3671550
timer=home-incremental-backup.timer;OnCalendar=03:40;RandomizedDelaySec=2h;Persistent=true;not_disabled
snapshot=.incomplete-20260613052609-3671550;path=/media/daniele/Seagate6TB2/home-backups/snapshots/.incomplete-20260613052609-3671550
snapshot_size=3.7G_by_du;status_json_snapshot_size=3.7GB;free_gb=2888
progress=rsync_progress_live;tail_after_more_file_discovery_showed_64_percent,about_512KiB/s,ETA_about_1h10;earlier_91_percent_was_not_final_due_incremental_recursion
errors=none_seen_in_tail_or_status;last_error_empty

CONFIG_CHANGE:
config_live=/home/daniele/.config/home-backup/home-backup.env
config_key=HOME_BACKUP_BWLIMIT_KB
old_value=512KiB/s
new_value=1024KiB/s
backup_file=/home/daniele/.config/home-backup/home-backup.env.bak-20260613-073520
script=/home/daniele/home_incremental_backup.sh uses BWLIMIT_KB -> rsync --bwlimit=$BWLIMIT_KB
unit_change=no;daemon_reload_needed=no
current_run_effect=no;running rsync argv still --bwlimit=512;new_value_applies_next_service_start
restart_current_backup=no;reason=current_run_progressing_and_restart_unneeded_would_risk_incomplete_snapshot_churn

MEASUREMENT:
tools_installed=sysstat installed 2026-06-13 to provide iostat,pidstat
iostat_preinstall=missing;pidstat_preinstall=missing;iotop_available=yes
iotop=rsync receiver PID3676881 wrote mostly 224-676KiB/s;backup process priority=idle
pidstat_10s=PID3676881 avg_write=506.67KiB/s;PID3676819 avg_read=1537.11KiB/s;other codex processes wrote more than backup during sample
iostat_10s=cpu_iowait_samples_2.02-8.01_percent_after_first_avg;root_sda_util_25-79_percent;dest_sdc_mostly_low_activity_with_flush_spikes;zram_active
psi_after=io some avg10=36.46 full avg10=3.56;memory some avg10=2.12 full avg10=1.23;cpu some avg10=53.88
load_after=17.02,13.98,9.36;mem_available=3.2GiB;swap_free=8.7GiB
status_checkpoint=load_x100=1827 memory_psi_avg10_x100=99 io_psi_avg10_x100=3550;coexistence_active=1;mega_rsync_pid=1243360;mega_bwlimit=5120KiB/s

DECISION:
chosen_bwlimit=1024KiB/s
why_not_2048_or_4096=I/O_PSI_and_load_high,root_USB_disk_busy,shared_USB_hub_topology,mega_rsync_coexistence_active
why_safe=only_2x_current_low_cap,still_nice19+ionice_idle+runtime_guards+coexistence_checks+large_free_space;does_not_change_dest_or_retention_or_snapshot_logic
rollback=restore backup_file or set HOME_BACKUP_BWLIMIT_KB back to 512 then wait next run;no snapshot deletion_needed

VERIFY:
config_verify=grep '^HOME_BACKUP_BWLIMIT_KB=' /home/daniele/.config/home-backup/home-backup.env -> 1024
current_argv_verify=ps showed running rsync still --bwlimit=512
timer_verify=systemctl --user list-timers --all | grep home-incremental -> active elapsed current run;timer not disabled
monitor_cmd=sudo iotop -oP -d 1

