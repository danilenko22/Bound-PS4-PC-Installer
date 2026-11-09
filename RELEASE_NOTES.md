### 🎉 Initial Release (v1.0.0)

A standalone Windows installer and launcher that turns your legally dumped PS4 copy of **Bound (`CUSA04380`)** into a ready-to-play PC installation on **shadPS4** — including the fix for the GPU slowdown that drops the game to ~10 FPS (or a black screen) after returning to the main menu.

---

### 📥 How to Install & Play
1. Download **`Bound.exe`** from the **Assets** section below.
2. Run it and choose the install folder (default `C:\Games\Bound`, ~2 GB).
3. Select your **base game PKG** and the **v1.03 update PKG** — or your already extracted **`CUSA04380`** folder.
4. Click **Start installation** (about a minute).
5. Play with the **Bound** shortcut on your Desktop.

---

### ✨ What's Included
* **The FPS fix:** shadPS4 v0.20 with `readbacks_mode = 1`, so a GPU particle counter is no longer overwritten by stale CPU data. Stable 60 FPS in gameplay and menus.
* **No PSN error at startup:** the bundled shadPS4 auto-accepts the offline "signed out" dialog (`0x80550006`).
* **Zero setup:** portable shadPS4, no PS4 firmware or system fonts required.
* **PKG or folder install:** extracts and merges the base game and the update automatically.
* **Launcher options:** fullscreen/windowed, resolution up to 4K, game language, FPS counter.
* **Direct play:** check *"Launch directly next time"*; hold **Shift** while opening the shortcut to get the launcher back.
* **English / Spanish** interface (follows the Windows language). No console windows.
* **Clean look:** original artwork in the installer; the launcher shows Bound's title image from your own game files.

---

### 💡 Notes
* If you already use shadPS4 with fonts dumped from your own PS4, the installer copies them automatically; otherwise bundled fallback fonts are used.
* **Windows SmartScreen:** the executable is unsigned — click **More info → Run anyway**.
* Saves: `<install folder>\emulator\user\home\1000\savedata` (button in the launcher).

*This release contains no copyrighted game files, firmware or fonts. You must provide your own legally dumped PS4 files. Bundled third-party software: shadPS4 (commit b2d7ec7d + one patch in `patches/`, GPL-2.0) and ShadPs4Plus PKG Extractor v1.1 (GPL-2.0) — see `licenses\THIRD_PARTY_NOTICES.txt`.*

SHA-256 (`Bound.exe`): B10FF22453B73CBD9B6715961600A5D15384DD121B5722025D140DB4F76ABE44
