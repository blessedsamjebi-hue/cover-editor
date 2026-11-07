# Cover Editor

Offline Canva + Photoshop-style design editor by Sam Jabathuai: one HTML file, no server.

## Layout
- `src/editor.html` – the whole editor (placeholders `__FONTS_LINK__`, `__ASSETS__`, `__DOC__` are filled by the build)
- `tools/build.py` – builds the app; `tools/templates.py` – ready-made editable templates
- `renderer/fonts/` – bundled fonts (Jost, Playfair Display, Poppins, Montserrat) for the desktop build
- `brand/` – app logo and icons (Aurora gradient); `build/icon.png` – 1024 px icon for a future desktop package

## Build
```bash
python3 tools/build.py                 # -> renderer/index.html (desktop renderer, bundled fonts)
python3 tools/build.py --web OUT.html  # -> one self-contained browser file (Google Fonts)
```
The Verdura Clear Skin Pack template reads its photos from
`Sam 2026/Social media/LinkedIn/November 2026/Verdura Clear Skin Pack/assets`, which is not in this repo.
Without that folder, remove `verdura_cover` from `TEMPLATES` in `tools/build.py`.

The Electron desktop app is not set up yet.
