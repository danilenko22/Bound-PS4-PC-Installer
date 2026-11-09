# Bound (PS4) – PC Installer & Launcher

A one-click Windows installer and launcher that turns your own legally dumped PS4 copy of
**Bound (`CUSA04380`)** into a ready-to-play PC installation running on the
[shadPS4](https://github.com/shadps4-emu/shadPS4) emulator — **with fixes** for the GPU slowdown
(~10 FPS or a black screen after returning to the main menu), the dark memory scenes, the missing
door at the end of the first memory and the flickering shadows on lit walls.

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

* **"PS4 system fonts not found"** notification: shadPS4 uses its bundled fallback fonts. If you
  already use shadPS4 with fonts dumped from your own console (`%APPDATA%\shadPS4\fonts`), the
  installer copies them automatically and the message does not appear.
* **Windows SmartScreen** "Unknown publisher": the executable is not signed. Click **More info → Run anyway**.

## The fixes (technical)

Bound keeps a GPU particle counter in the same memory page as constants written by the CPU. With
shadPS4's default `readbacks_mode = 0`, a CPU write marks the whole page as CPU-modified and the next
upload overwrites the GPU-written counter with stale CPU data (float constants such as `0.1` / `25.0`,
about one billion when read as an integer). An indirect-dispatch shader then launches millions of
work groups, the GPU stays at 100 % and the game drops to ~10 FPS or a black screen.

The launcher runs shadPS4 v0.20 with **`readbacks_mode = 2` (Precise)**, so GPU data is read back
before the CPU touches that page. Result: a stable 60 FPS in gameplay and menus (tested on an
AMD Radeon RX 9070 XT). Precise (not Relaxed) is required because the game also *reads* GPU-written
state: with Relaxed the white door at the end of the first memory never appears.

**Dark memory scenes.** The memory scenes (table, chess) rendered as dark silhouettes because
shadPS4 dropped the sample index when a shader reads a multisampled *storage* image, so Bound's
per-sample fog shader read garbage
([`patches/shadps4-msaa-storage-image-sample.patch`](patches/shadps4-msaa-storage-image-sample.patch)).

**Flickering wall shadows.** Lit walls made of broken pieces flickered into shadow for single
frames. The compute shader that rebuilds the normals of those pieces has a branch that overwrites
a few vertex normals; on shadPS4 that data comes out wrong and changes every frame, and the
lighting shader offsets its shadow lookup along the normal, so whole walls toggled between light
and shadow. The bundled shadPS4 drops that branch for this one shader when it is translated
([`patches/shadps4-bound-wall-flicker.patch`](patches/shadps4-bound-wall-flicker.patch)). No game
code is included or modified on disk. The installer also clears shadPS4's shader cache for Bound
so old translations are not reused.

**PSN error at startup.** Bound asks for the PSN account at boot and shows the system error dialog
`0x80550006` (signed out) when it is missing. The bundled shadPS4 includes a small patch
([`patches/shadps4-offline-psn-error-dialog.patch`](patches/shadps4-offline-psn-error-dialog.patch)):
in offline mode that specific dialog is accepted automatically, so the game starts without the
message. Online features (leaderboards) are not available.

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

## Artwork

The installer banner is original abstract artwork generated by `make_background.py` (no game assets).
Once installed, the launcher shows the game's own title image (`sce_sys/pic1.png`) taken from the
user's copy of the game.

## Building from source

Requires Python 3.10+ with `pyinstaller` and `pillow` (`build.bat` also generates the icon and banner).

1. Put the unmodified third-party binaries in `payload\`:
   * `payload\emulator\shadPS4.exe` – shadPS4 commit [`b2d7ec7d`](https://github.com/shadps4-emu/shadPS4/tree/b2d7ec7d31f9ad9426db93afe079db8679b3e1e0) built with all the patches in `patches\` applied
   * `payload\extractor\` – `pkg_extractor.exe`, `libc++.dll`, `zlib1.dll` from [ShadPs4Plus PKG Extractor v1.1](https://github.com/ZuanCrisp/shadPS4PlusPKGExtractor/releases/tag/v1.1)
   * `payload\licenses\` – `GPL-2.0.txt` and `THIRD_PARTY_NOTICES.txt` (included in this repo)
2. Run `build.bat`. The result is `dist\Bound.exe`.

## Credits and licenses

* Installer/launcher: MIT License (see `LICENSE`).
* [shadPS4](https://github.com/shadps4-emu/shadPS4) – GPL-2.0-or-later, by the shadPS4 Emulator Project (bundled with small patches, see `patches/`).
* [ShadPs4Plus PKG Extractor](https://github.com/ZuanCrisp/shadPS4PlusPKGExtractor) – GPL-2.0.

Bound is a trademark of its respective owners. This project is not affiliated with or endorsed by
Sony Interactive Entertainment, Plastic Studios or the shadPS4 team.

---

## Español

Instalador y launcher para jugar **Bound (PS4, `CUSA04380`)** en PC con shadPS4, usando tus propios
PKG. Incluye los arreglos de la caída a ~10 FPS al volver al menú, las escenas de recuerdos
oscuras, la puerta blanca que no aparecía y el parpadeo de sombras en los muros iluminados.

1. Descarga **`Bound.exe`** desde [Releases](../../releases) y ábrelo (no hace falta Python).
2. Elige la carpeta de instalación y tus **PKG** (base + actualización v1.03) o tu carpeta **`CUSA04380`** ya extraída.
3. Pulsa **Instalar** y juega con el acceso directo **Bound** del escritorio.

El instalador se muestra en español si Windows está en español. No incluye archivos del juego,
firmware ni fuentes de PS4.
