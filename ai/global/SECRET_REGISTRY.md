# SECRET_REGISTRY
VERSION=2
STATUS=AUTHORITATIVE_PATH_REGISTRY
UPDATED=2026-08-01
SECRET_ROOT=/home/daniele/.config/codex/secrets
SECRET_DISCOVERY=mandatory_before_consumer_change
ENV_FILES=used_config+simple_secrets+secret_paths_only
MULTILINE_SECRETS=separate_files
PRIVATE_KEYS=separate_files
SECRET_FILE_MODE=600
SECRET_HARDCODE=forbidden
SECRET_REPO_STORAGE=forbidden
SECRET_OUTPUT=forbidden
SECRET_HISTORY_REWRITE=manual_explicit_only
SECRET_ROTATION=never_automatic
BACKUP_DECRYPTION_KEY_PRESERVATION=mandatory
SECRET_PATH_REPROMPT=forbidden_if_canonical_registry_exists

SECRET=oracle_connection;classification=ACTIVE_REQUIRED;env=/home/daniele/.config/codex/secrets/oracle.env;key=/home/daniele/.config/codex/secrets/oracle_vm_rsa;type=env+SSH_private_key;source=migrated;consumers=ssh_config,oracle-backup-service,vm_oracle;validation=owner+mode+key_parse+fingerprint_continuity+SSH_read_only+SCP_read_only+rsync_dry_run_PASS;legacy=/home/daniele/MegaVault/secrets/oracle-cloud/oracle-vm-rsa;legacy_status=removed_after_verified_safety_copy;last_verified=2026-08-01
SECRET=telegram_shared;classification=ACTIVE_REQUIRED;env=/home/daniele/.config/codex/secrets/telegram.env;type=env;source=existing+rotated_by_user;consumers=amici_fb,telegram_insert_bot,fedora-system-monitor,fedora-t7-backup,luoghi-app,SuperContacts;validation=parser+consumer_checks+live_TEST_delivery_PASS;exposure_status=historical_tokens_invalidated;rotation_required=no;last_verified=2026-08-01
SECRET=luoghi_maps;classification=ACTIVE_REQUIRED;env=/home/daniele/.config/codex/secrets/map.env;type=env;source=migrated;consumers=luoghi-app;validation=parser+Gradle_key_injection+build+Pixel_runtime_PASS;legacy=luoghi-app/maps-api.properties;legacy_status=removed_after_verified_safety_copy;last_verified=2026-08-01
SECRET=multitimetracker_signing;classification=ACTIVE_REQUIRED;env=/home/daniele/.config/codex/secrets/multitimer.env;files=/home/daniele/.config/codex/secrets/multitimetracker_upload.p12,/home/daniele/.config/codex/secrets/multitimetracker_update_compat.keystore;type=env+keystore;source=bitwarden;consumer=MultiTimeTracker;bitwarden_item=MultiTimeTracker_Play_Store_Signing;bitwarden_uuid=1cda2c3d-422d-4b16-a29e-b47100574349;bitwarden_item=MultiTimeTracker_Pixel_Direct-Update_Signing_Key;bitwarden_uuid=f6a323da-7feb-4b0b-ac13-b48b00c893ae;validation=two_item_fingerprint+signed_APK+AAB+Pixel_in_place+secret_scan_PASS;last_verified=2026-08-01
SECRET=android_shared_update_signing;classification=ACTIVE_REQUIRED;env=/home/daniele/.config/codex/secrets/android_signing.env;key=/home/daniele/.config/codex/secrets/android_shared_update.keystore;type=env+keystore;source=migrated;consumers=luoghi-app,wordpulse,Soldi,SuperContacts,Sostanze;validation=certificate_continuity+signed_APK+Pixel_in_place_PASS;last_verified=2026-08-01
SECRET=fedora_t7_backup_decryption;classification=ACTIVE_REQUIRED;key=/home/daniele/.config/codex/secrets/fedora_t7_backup.restic_password;type=restic_password_file;source=migrated;consumer=fedora-t7-backup;validation=systemd_LoadCredential+historical_live_snapshot+restic_check+listing_PASS;legacy=/etc/credstore.encrypted/t7-restic-password;legacy_status=preserved_as_encrypted_recovery_copy;last_verified=2026-08-01
SECRET=fedora_system_monitor_uptime_kuma_push;classification=ACTIVE_REQUIRED;file=/home/daniele/.config/codex/secrets/fedora_system_monitor_uptime_kuma.toml;type=TOML_simple_secrets;source=migrated;consumer=fedora-system-monitor;validation=config_check+live_collection+heartbeat_delivery_PASS;legacy=/etc/fedora-system-monitor/uptime-kuma.toml;legacy_status=removed_after_verified_safety_copy;last_verified=2026-08-01
SECRET=datasette_remote_runtime;classification=ACTIVE_REQUIRED;type=remote_env;source=existing_remote;consumer=datasette5;canonical_path=remote:/etc/datasette/datasette.env;validation=remote_runtime_config_present;local_copy=forbidden;exception=root_only_remote_authority;last_verified=2026-08-01
SECRET=kuma_admin;classification=ACTIVE_OPTIONAL;env=/home/daniele/.config/codex/secrets/kuma.env;type=env;source=existing;consumer=external_Uptime_Kuma_admin_tooling;scope_repo_consumer=none_verified;validation=owner+mode+parser_PASS;last_verified=2026-08-01
