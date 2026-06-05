# megavault-project-exporter Changelog

## 2026-06-05
- Created exporter project for prompt `#271684`.
- Added cached project+MegaVault bundle creation.
- Added local, remote Mint SSH, and headless transfer modes.
- Registered MegaVault AI and human documentation.
- Installed/tested local clipboard tools and fixed X11 fallback when `wl-copy` exists but no Wayland socket is available.
- Made the printed Mint clipboard command try `wl-copy`, `xclip`, and `xsel` instead of assuming Wayland.
- Switched X11 `xclip`/`xsel` clipboard handling to verified text path because XFCE did not retain the `x-special` file target reliably.
- Detached `xclip`/`xsel` providers with `setsid -f` so the verified clipboard survives after the exporter command exits.
