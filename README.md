# Bound (PS4) – PC Installer & Launcher

A one-click Windows installer and launcher that turns your own legally dumped PS4 copy of
**Bound (`CUSA04380`)** into a ready-to-play PC installation running on the
[shadPS4](https://github.com/shadps4-emu/shadPS4) emulator — **with the fix for the GPU slowdown**
that drops the game to ~10 FPS (or a black screen) after returning to the main menu.

> **No game files are included.** You must provide your own dumped PKG files or game folder.
> No PS4 firmware or system fonts are needed or included.

## Download

Get **`Bound.exe`** from the [Releases](../../releases) page. It is a single file — no Python,
no extra downloads.

## How to install

1. Run `Bound.exe`.
2. Choose the install folder (default `C:\Games\Bound`, ~2 GB).
3. Pick your game source:
   * **PKG files** – base game PKG (required) and the **v1.03 update PKG** (recommended), or
   * **Extracted folder** – your `CUSA04380` folder (a `CUSA04380-patch` folder next to it is detected automatically).
4. Click **Start installation**. It takes about a minute.
5. Play with the **Bound** shortcut on your Desktop.

## Launcher options

* Fullscreen (borderless) or windowed, window resolution (720p – 4K)
* Game language (English, Spanish, French, German, Italian, Portuguese, Russian, Japanese)
* FPS counter
* **Launch directly next time** – skips the launcher. Hold **Shift** while opening the shortcut to get the launcher back.
* Buttons to open the saves folder and the install folder

## Controls

Controllers (DualShock 4, DualSense, Xbox…) work out of the box. Default keyboard:

| PS4 | Key | PS4 | Key |
|---|---|---|---|
| Left stick | W A S D | Right stick | I J K L |
| Cross / Circle / Square / Triangle | N / B / V / C | D-pad | Arrow keys |
| L1 / R1 | Q / U | L2 / R2 | E / O |
| L3 / R3 | X / M | Options | Enter |
| Touchpad | Space | | |

## Known messages (harmless)

* **"An error has occurred. Code: 0x80550006"** at startup: the game asks for a PSN sign-in, which an
  offline emulator cannot provide. Press **OK** — the game works normally (online features are not available).
* **"PS4 system fonts not found"** notification: shadPS4 uses its bundled fallback fonts. If you
  already use shadPS4 with fonts dumped from your own console (`%APPDATA%\shadPS4\fonts`), the
  installer copies them automatically and the message does not appear.
* **Windows SmartScreen** "Unknown publisher": the executable is not signed. Click **More info → Run anyway**.

## The fix (technical)

Bound keeps a GPU particle counter in the same memory page as constants written by the CPU. With
shadPS4's default `readbacks_mode = 0`, a CPU write marks the whole page as CPU-modified and the next
upload overwrites the GPU-written counter with stale CPU data (float constants such as `0.1` / `25.0`,
about one billion when read as an integer). An indirect-dispatch shader then launches millions of
work groups, the GPU stays at 100 % and the game drops to ~10 FPS or a black screen.

The launcher runs shadPS4 v0.20 with **`readbacks_mode = 1` (Relaxed)**, so GPU data is read back
before the CPU writes to that page. Result: a stable 60 FPS in gameplay and menus (tested on an
AMD Radeon RX 9070 XT).

## Files and folders

```
C:\Games\Bound\
├── Bound.exe                 launcher (same file as the installer)
├── emulator\shadPS4.exe      portable shadPS4 v0.20
├── emulator\user\            emulator settings, logs and saves (home\1000\savedata)
├── game\CUSA04380\           your game files (+ CUSA04380-patch)
└── licenses\                 third-party licenses
```

**Uninstall:** delete the install folder and the Desktop shortcut (back up `emulator\user\home\1000\savedata` first if you want to keep your saves).

## Building from source

Requires Python 3.10+ with `pyinstaller` and `pillow`.

1. Put the unmodified third-party binaries in `payload\`:
   * `payload\emulator\shadPS4.exe` – shadPS4 commit [`b2d7ec7d`](https://github.com/shadps4-emu/shadPS4/tree/b2d7ec7d31f9ad9426db93afe079db8679b3e1e0)
   * `payload\extractor\` – `pkg_extractor.exe`, `libc++.dll`, `zlib1.dll` from [ShadPs4Plus PKG Extractor v1.1](https://github.com/ZuanCrisp/shadPS4PlusPKGExtractor/releases/tag/v1.1)
   * `payload\licenses\` – `GPL-2.0.txt` and `THIRD_PARTY_NOTICES.txt` (included in this repo)
2. Run `build.bat`. The result is `dist\Bound.exe`.

## Credits and licenses

* Installer/launcher: MIT License (see `LICENSE`).
* [shadPS4](https://github.com/shadps4-emu/shadPS4) – GPL-2.0-or-later, by the shadPS4 Emulator Project.
* [ShadPs4Plus PKG Extractor](https://github.com/ZuanCrisp/shadPS4PlusPKGExtractor) – GPL-2.0.

Bound is a trademark of its respective owners. This project is not affiliated with or endorsed by
Sony Interactive Entertainment, Plastic Studios or the shadPS4 team.

---

## Español

Instalador y launcher para jugar **Bound (PS4, `CUSA04380`)** en PC con shadPS4, usando tus propios
PKG. Incluye el arreglo de la caída a ~10 FPS al volver al menú (`readbacks_mode = 1`).

1. Descarga **`Bound.exe`** desde [Releases](../../releases) y ábrelo (no hace falta Python).
2. Elige la carpeta de instalación y tus **PKG** (base + actualización v1.03) o tu carpeta **`CUSA04380`** ya extraída.
3. Pulsa **Instalar** y juega con el acceso directo **Bound** del escritorio.

El instalador se muestra en español si Windows está en español. El aviso **0x80550006** al arrancar
es normal (no hay PSN en el emulador): pulsa **OK** y el juego funciona igual. No incluye archivos del
juego, firmware ni fuentes de PS4.
