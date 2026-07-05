# prompt_914672 home-backup bwlimit safety

date=2026-06-13
host=daniele-Surface-Pro
scope=home-incremental-backup.service bwlimit_safety_recheck;diagnostic+docs_update
protocol=../MEGAVAULT_PROTOCOL.md
host_profile=../global/HOST_PROFILE.md
prior_report=prompt_739284_home_backup_bwlimit_followup.md

SUMMARY:
backup_state=active_running;systemd=activating/start expected_for_long_oneshot;not_blocked_by_systemd_status_alone
service=home-incremental-backup.service user;started=2026-06-13T05:25:53+02:00;MainPID=3671550
timer=home-incremental-backup.timer;OnCalendar=03:40;RandomizedDelaySec=2h;Persistent=true;not_disabled
current_run_argv=rsync --bwlimit=512 -R /home/daniele/./Documents -> /media/daniele/Seagate6TB2/home-backups/snapshots/.incomplete-20260613052609-3671550/
config_live=/home/daniele/.config/home-backup/home-backup.env;HOME_BACKUP_BWLIMIT_KB=1024;applies_next_run_only
config_backup_previous=/home/daniele/.config/home-backup/home-backup.env.bak-20260613-073520;value=512
config_change=none;reason=metrics_do_not_justify_2048_to_5120_now

TOPOLOGY_CONFIRMED:
root_disk=/dev/sda2 ext4 mounted /;Samsung_PSSD_T7_Shield;root_and_home_on_USB
internal_nvme=/dev/nvme0n1;Windows_BitLocker_partitions;not_linux_root
backup_dest=/dev/sdc1 ext4 mounted /media/daniele/Seagate6TB2;Seagate_ST6000DM003
source_4tb=/dev/sdb2->/dev/mapper/source_bitlocker mounted /media/daniele/Seagate Expansion Drive readonly
constraint=T7_root+Seagate4TB+Seagate6TB2 share SABRENT hub and one Surface USB path;do_not_assume_independent_storage

LIVE_PROCESSES:
home_backup_rsync=PIDs 3676819,3676867,3676881;effective_bwlimit=512KiB/s
home_backup_receiver=PID3676881 avg_write=510.31KiB/s over 60s;dest=/dev/sdc1
home_backup_sender=PID3676819 avg_read=1092.69KiB/s over 60s;source=/dev/sda2 path /home/daniele/Documents/...
codex_io=sum_codex_avg_write=10906.18KiB/s over 60s;all Codex open files under /home/daniele/.codex on /dev/sda2
mega_transfer_rsync=PIDs 1243360,1243370,1352135;argv_bwlimit=5120KiB/s;source=/media/daniele/Seagate Expansion Drive;dest=/media/daniele/Seagate6TB2/vecchio disco;no_significant_io_in_completed_sample
fuser_seagate6tb2=kernel mount plus home backup timeout/rsync PIDs 3676798,3676819,3676867,3676881

MEASUREMENT_60S:
cpu_psi_after=some avg10=21.46 avg60=23.24 avg300=27.13;full avg10=0 avg60=0
io_psi_after=some avg10=12.22 avg60=14.20 avg300=15.03;full avg10=4.18 avg60=4.75
memory_psi_after=some avg10=0.87 avg60=0.40 avg300=1.03;full avg10=0.79 avg60=0.31
uptime_load=8.84,8.57,9.36 during measurement start
memory=7.7GiB total;available 4.1-4.2GiB;free 208-407MiB
swap_total=11GiB;used 2.3-2.5GiB;disk_swap_used_about_119MiB;zram_used_2.1-2.4GiB data
diskstats_20s=/dev/sda read=3.864MiB/s write=8.532MiB/s;/dev/sdc read=0 write=0.391MiB/s;/dev/sdb+dm-0+nvme0n1=0
iostat_observation=/dev/sda frequently 70-80% util in sample bursts;/dev/sdc mostly low throughput with flush/await spikes;zram active
dmesg_filtered=no USB reset/I/O error/ext4/jbd2/sda/sdc storage errors in last filtered tail;only Wi-Fi/Bluetooth reset lines seen

DECISION:
chosen_value=keep_HOME_BACKUP_BWLIMIT_KB_1024
not_chosen=2048,4096,5120
reason_not_safe=io_psi_avg60_high;io_full_avg60_nonzero;cpu_psi_high;zram_heavily_used;T7_root_busy;Codex_writes_on_root_about_10.6MiB/s;shared_USB_hub;active_backup_running_at_512;historical_freeze/load_guard_risk
threshold_logic=prompt_required_2048_plus_only_when_PSI_low,swap/zram_stable_low,await_ok,no_USB_errors;current_PSI_and_zram_fail_conservative_gate
current_run_effect=no_change;running rsync remains --bwlimit=512 until service exits
next_run_effect=config remains HOME_BACKUP_BWLIMIT_KB=1024
rollback=restore /home/daniele/.config/home-backup/home-backup.env.bak-20260613-073520 or set HOME_BACKUP_BWLIMIT_KB=512;no snapshot deletion_needed
future_retest_gate=consider_2048 only when io some avg10/avg60 near low single digits,io full near 0,zram materially lower/no growth,T7 util not burst-saturated,no concurrent heavy Codex/browser writes,no mega transfer,clean dmesg

VERIFY:
commands=systemctl --user status/cat; journalctl --user -u home-incremental-backup.service -n 200; pgrep/lsof targeted rsync; fuser -vm Seagate6TB2; iostat -xz 1 60; pidstat -d 1 60; PSI/free/swapon/zramctl/dmesg filtered
no_destructive_actions=no stop,no kill,no restart,no timer_disable,no snapshot_delete,no benchmark
monitor_cmd=iostat -xz 1;pidstat -d 1;fuser -vm /media/daniele/Seagate6TB2
