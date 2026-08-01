# SECRET_REGISTRY
VERSION=1
STATUS=AUTHORITATIVE_PATH_REGISTRY
UPDATED=2026-08-01
SECRET_ROOT=/home/daniele/.config/codex/secrets
ENV_FILES=config+secret_paths_only
MULTILINE_SECRETS=separate_files
PRIVATE_KEY_MODE=600
SECRET_HARDCODE=forbidden
SECRET_REPO_STORAGE=forbidden
SECRET_OUTPUT=forbidden
SECRET_PATH_REPROMPT=forbidden_if_canonical_registry_exists
ORACLE_ENV=/home/daniele/.config/codex/secrets/oracle.env
ORACLE_KEY=/home/daniele/.config/codex/secrets/oracle_vm_rsa
ORACLE_KEY_FINGERPRINT=SHA256:cmihWRlHSLgX1YGGRx7zukWWql3Am4rCqCx/Hp27uXU
ORACLE_KEY_OWNER=daniele:daniele
ORACLE_KEY_MODE=600
ORACLE_SAFETY_COPY=/home/daniele/repository-safety/prompt-816429/oracle-secrets/oracle_vm_rsa.before-migration
ORACLE_OLD_PATH=/home/daniele/MegaVault/secrets/oracle-cloud/oracle-vm-rsa
ORACLE_OLD_PATH_STATUS=preserved_pending_remaining_consumer_migration
ORACLE_CONSUMER=ssh_config;status=verified
ORACLE_CONSUMER=oracle-backup-service;status=verified
ORACLE_CONSUMER=vm_oracle;status=verified;helper=/home/daniele/projects/vm_oracle/scripts/oracle_ssh.sh
ORACLE_CONSUMER=datasette5;status=pending_serial_discovery
ORACLE_CONSUMER=telegram_insert_bot;status=pending_serial_discovery
ORACLE_VALIDATION=owner_mode+key_parse+sha256+fingerprint+direct_SSH+alias_SSH+SCP_read_only_PASS
ORACLE_REMOTE_MUTATION=none
ORACLE_VERIFIED=2026-08-01
MULTITIMER_ENV=/home/daniele/.config/codex/secrets/multitimer.env
MULTITIMER_ENV_OWNER=daniele:daniele
MULTITIMER_ENV_MODE=600
MULTITIMER_BITWARDEN_ITEM=MultiTimeTracker Play Store Signing;uuid=1cda2c3d-422d-4b16-a29e-b47100574349;fields=login.password,key_alias,key_password,attachment
MULTITIMER_BITWARDEN_ITEM=MultiTimeTracker Pixel Direct-Update Signing Key;uuid=f6a323da-7feb-4b0b-ac13-b48b00c893ae;fields=alias,store_password,key_password,attachment
MULTITIMER_CONSUMER=/home/daniele/projects/MultiTimeTracker/app/build.gradle.kts;status=verified
MULTITIMER_SECRET_FILES=separate_files;mode=600;tracked=no
MULTITIMER_VALIDATION=two_item_fingerprint+signed_APK_AAB+Pixel_in_place+secret_scan_PASS
MULTITIMER_VERIFIED=2026-08-01
