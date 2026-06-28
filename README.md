[README.md](https://github.com/user-attachments/files/29435015/README.md)
# 🎴 Mudae Toolkit

A single-file browser tool for managing your [Mudae](https://mudae.net) harem. No install, no account, no server —

---

## ✨ Features

### 🗂 Sorter
Visualise and reorder your harem as draggable tiles.

- Paste your `$mmasi-` or `$mmsaty+ri-c+x+ko` (recommended) output to load all characters at once
- Drag tiles to arrange them in any order, then generate a `$sortmarry` command to sync that order to Mudae
- Create named colour-coded **visual groups** (e.g. by series or priority) — right-click any tile to assign it
- Pick a specific image for each character via the 🖼 gallery button, then batch-generate `$ci` commands to set them all in Discord
- Undo / redo support, image cache, and a **Snapshot** button to save a PNG of your full grid

### 📝 Noter
A card-based view of every character with note and colour management.

- Group characters by series, note, colour, keys, kakera, gender, roulette type, or owner
- Click any character card to assign or edit a `$n` note or `$ec` colour
- Filter by kakera range, key count, owner, gender, and roulette type
- Generate all your `$n` or `$ec` commands in one click, copy them one at a time in sequence
- Ranking mode lets you drag-set a priority number within each group
- Export a PNG snapshot of the full noter view

### 💞 Wishlist
Import and manage your wishlist from `$wishlist` / `$wl` output.

- ⭐ marks star-wished characters, ✅ marks ones you already own
- Reorder entries by dragging, generate `$wish` commands in the right order
- Search and add characters directly from within the tool
- **Download AHK Script** — generates an AutoHotkey v2 script that types and sends every command into Discord automatically, 3 seconds apart

### 🎨 Colors
Auto-extract colours from character images and apply them in bulk.

- Paste `$mmysi-c-` output; the tool fetches each image and samples its dominant colour
- Six palette modes: Vibrant, Muted, DarkVibrant, DarkMuted, LightVibrant, LightMuted
- Override any colour with a manual picker before generating commands
- **Download AHK Script** — generates an AutoHotkey v2 script that types and sends every `$ec` command into Discord automatically, 2 seconds apart

### ✂️ Cropper
Crop images and animated GIFs to Mudae's required **225×350px** (9:14) format.

- Load by URL or drag-and-drop file upload (supports static images and GIFs)
- Drag the crop box to reposition; live 225×350 preview updates in real time
- GIF output uses **median-cut colour quantisation + Floyd-Steinberg dithering** for smooth, low-banding results
- After downloading, upload to [Imgur](https://imgur.com) or [imgchest](https://imgchest.com), then use `$ai CharName $ <link>` in Discord

---

## 🚀 Getting Started

1. Either download, clone this repo or go to [Site](itsdrnk.github.io/mudaesorter)
- ↓ IF downloaded ↓
2. Open `index.html` in any modern browser — nothing else needed
- Then
3. Create a profile for your account (top bar → **+ New**)
4. Go to the **Sorter** tab, paste your `$mmasi-` output, and click **Replace All Characters**

> **Tip:** Use `$mmsaty+ri-c+x+ko` instead of `$mmasi-` to also load kakera values, key counts, colour tags, owner names, and roulette info.

---

## 💾 Profiles & Data

All data is saved to your **browser's localStorage** automatically — nothing is sent anywhere.

- Create multiple profiles
- **Export Profile** saves a `.json` file you can back up or share
- **Import Profile** restores from that file on any device
- **Export All / Import All** backs up every profile at once

---

## 🤖 AutoHotkey Setup (for Colors tab)

The AHK script requires **AutoHotkey v2** (free):

👉 [autohotkey.com/download](https://www.autohotkey.com/download)

Once installed, run the downloaded `.ahk` file with Discord open and focused. It will type and send each `$ec` command automatically. Move your mouse or press any key to stop it early.

---

## 🛠 Technical Notes

- Pure vanilla HTML/JS — no framework, no build step
- All processing (GIF decoding, colour sampling, image cropping) happens client-side
- GIF encoding uses [omggif](https://github.com/deanm/omggif) with a custom median-cut + Floyd-Steinberg pipeline
- Colour extraction uses [Vibrant.js](https://github.com/jariz/vibrant.js)
- Image-to-canvas via [html2canvas](https://html2canvas.hertzen.com)
- CORS proxy (`mudae_proxy.py`) is included if you want to load Mudae URLs directly — run it locally with `python mudae_proxy.py`

---

## 📋 Useful Mudae Commands

| Command | What it gives you |
|---|---|
| `$mmasi-` | Basic harem list (name, series, image) |
| `$mmsaty+ri-c+x+ko` | Full harem data (kakera, keys, colour, owner, roulette) |
| `$mmysi-c-` | Images for colour extraction |
| `$wishlist` / `$wl` | Your current wishlist |
| `$sortmarry <list>` | Reorders your harem to match a name list |
| `$ci <name> $ <index>` | Sets a character's displayed image |
| `$n <name> $ <note>` | Sets a note on a character |
| `$ec <name> $ <#hex>` | Sets the embed colour for a character |
| `$ai <name> $ <url>` | Adds a custom image to a character |

---

*made for fun — some parts may be broken*
