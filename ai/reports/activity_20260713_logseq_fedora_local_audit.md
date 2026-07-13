# Activity 20260713 Logseq Fedora Local Audit

ID=activity_20260713_logseq_fedora_local_audit
DATE=2026-07-13
STATUS=WARNING
CATEGORY=qa
IMPORTANCE=P2
HOST=fedora
SCOPE=local_read_only_logseq_installability_audit

SUMMARY:
- Verified `/home/daniele/Downloads/logseq-darwin-x64-builds` without downloads, installs, extraction, Wine, emulators, or conversions.
- Found Logseq 2.0.1 macOS Intel artifacts only: `Logseq-darwin-x64-2.0.1.dmg`, `Logseq-darwin-x64-2.0.1.zip`, matching blockmaps, `VERSION`, and `latest-x64-mac.yml`.
- Manifest `latest-x64-mac.yml` identifies `darwin-x64` / `mac`; zip contains `Logseq.app`; streamed executable is `Mach-O 64-bit x86_64`; plist declares macOS SDK and minimum macOS 12.0.
- Fedora target host is Linux x86_64; these packages are not installable as native Fedora/Linux packages because Fedora expects ELF/Linux binaries, AppImage, RPM, or Flatpak, not macOS `.app`/Mach-O/DMG artifacts.
- Local search found `/usr/bin/flatpak` and Flathub remote metadata/icons, but no installed `com.logseq.Logseq`, no `logseq` command in PATH, no Logseq RPM, no Logseq AppImage, and no Logseq GNOME launcher.
- Linux package needed for this host: Logseq Linux x86_64 package, preferably `Logseq-linux-x64-2.0.1.AppImage` for a same-version offline file, or Flatpak app ID `com.logseq.Logseq` if installing via Flatpak later.

BLOCKERS:
- Existing local package set is macOS-only and cannot satisfy Fedora installation.

RECOMMENDATION:
- Do not install the existing darwin/macOS artifacts on Fedora.
- Stop until a Linux x86_64 Logseq package is provided or explicit approval is given to install via Flatpak/network in a separate task.
