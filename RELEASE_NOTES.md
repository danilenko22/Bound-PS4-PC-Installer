### 🛠️ Bound PC Installer v1.1.0

Same one-click installer and launcher, now with every graphics fix found so far.

---

### ✨ What's New
* **No more flickering shadows:** lit walls made of broken pieces no longer flicker into shadow. The bundled shadPS4 skips a branch of one compute shader whose data came out wrong on the emulator.
* **Memory scenes render correctly:** the table and chess memories are no longer dark silhouettes (MSAA storage-image fix in shadPS4).
* **The white door appears:** `readbacks_mode = 2` (Precise), so the door at the end of the first memory shows up and you can progress.
* **Fresh shader cache:** installing clears shadPS4's cached shaders for Bound so old translations are not reused.

---

### 📥 How to Install or Update
1. Download **`Bound.exe`** from the **Assets** section below.
2. Run it and choose the install folder. **To update, pick your existing install folder:** your saves are kept.
3. Select your **base game PKG** and the **v1.03 update PKG**, or your already extracted **`CUSA04380`** folder.
4. Click **Start installation** and play with the **Bound** shortcut.

---

### 💡 Notes
* The first time you reach new areas there can be short stutters while shaders compile; they are cached afterwards.
* No game files, PS4 firmware or system fonts are included.
* Bundled shadPS4: v0.20 (`b2d7ec7d`) + the patches in [`patches/`](https://github.com/danilenko22/Bound-PS4-PC-Installer/tree/main/patches).
* **Windows SmartScreen:** the executable is unsigned. Click **More info → Run anyway**.
