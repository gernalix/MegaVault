# Prompt 593804 - Oracle VM SSH access

activity=593804
date=2026-07-14
status=PASS
scope=Fedora SSH client access to Oracle Cloud VM

CONFIG:
alias=oracle-vm
host=150.230.148.128
user=ubuntu
key_path=/home/daniele/MegaVault/secrets/oracle-cloud/oracle-vm-rsa
wrapper=/home/daniele/MegaVault/secrets/oracle-cloud/connect.sh
launcher=/home/daniele/.local/bin/oracle-vm

SECURITY:
private_key_storage=protected_MegaVault_secrets_path
private_key_mode=0600
secrets_dir_mode=0700
gitignore=secrets/**+oracle-vm-rsa+access.env
pem_in_docs=forbidden
public_key_fingerprint=SHA256:cmihWRlHSLgX1YGGRx7zukWWql3Am4rCqCx/Hp27uXU
host_key_fingerprint=ED25519_SHA256:jeMdcW+n3CdSv33xHSLgLx8tO4L4Pk3h6ziTgre0wUE
filesystem_at_rest=home_on_crypto_LUKS_btrfs

VALIDATION:
key_delimiters=PASS
ssh_keygen_parse=PASS
private_public_match=PASS
tcp_22=PASS
ssh_config_parse=PASS
ssh_batch_auth=PASS
remote_command=PASS
interactive_tty=PASS
remote_hostname=instance-20260201-1126
remote_system=Linux_instance-20260201-1126_6.8.0-1054-oracle_Ubuntu

NOTES:
do_not_copy_private_key_into_markdown_prompts_logs_git_or_shell_history=yes
do_not_commit_ignored_secrets=yes
