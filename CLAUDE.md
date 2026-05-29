# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Static marketing website for **Rappideutsch**, a private German school in
Rapperswil-Jona, Switzerland (teacher: Maria Bernardina Milano). It is a favour
project — the goal is an engaging, friendly, professional site that Maria can
review and iterate on.

Plain **HTML + CSS + a little vanilla JS**. No framework, no build step, no
`package.json`, no bundler. Files are edited and served as-is.

> **Brand spelling, in flux:** the brand is **Rappideutsch** (with an *i*). All
> on-page text, alt/aria labels and the favicon now use the *i* form. Still on
> the old **Rappjdeutsch** (*j*) spelling: the GitHub repo
> (`hydrantus/rappjdeutsch`), this local directory, and therefore the live URL
> `https://hydrantus.github.io/rappjdeutsch/` — a repo/directory rename to the
> *i* form is pending. Because of this, the absolute `og:image` URL still points
> at the `rappjdeutsch` repo path; **update it once the repo is renamed.**

## Commands

```bash
# Local preview (open http://localhost:8000)
cd docs && python3 -m http.server 8000

# Dump the course catalogue source spreadsheet to CSV
# (auto-installs pandas + openpyxl into the active venv on first run)
source .venv/bin/activate && python read_excel.py

# Regenerate an optimised web image from a source original (macOS `sips`)
#   - transparent PNGs (logo, teacher cutout): keep alpha, cap width
sips -s format png --resampleWidth 620 "materials/<source>.png" --out docs/assets/img/<name>.png
#   - photos: re-encode JPEG, cap the long edge
sips -s format jpeg -s formatOptions 72 --resampleHeightWidthMax 1400 "materials/<source>.jpeg" --out docs/assets/img/<name>.jpg
```

There are no tests, linters, or CI.

## Deployment

GitHub Pages, **Deploy from branch → `main` → `/docs`**. Live at
`https://hydrantus.github.io/rappjdeutsch/`. `docs/.nojekyll` keeps Pages from
mangling the files. Pushing to `main` redeploys; there is no build.

Because the site is served under the `/rappjdeutsch/` sub-path, **all internal
references use relative paths** (see below). The one exception: `og:image` must
be an **absolute** URL (`https://hydrantus.github.io/...`) or WhatsApp/social
previews break — that was a deliberate fix, don't revert it to a relative path.

## Architecture

```
docs/                 ← the published website (this is the Pages root)
  index.html          ← English (site root)
  de/index.html       ← German
  assets/styles.css   ← ALL styling
  assets/app.js       ← mobile nav toggle + header shadow on scroll (that's it)
  assets/img/         ← optimised, web-sized assets actually served
materials/            ← large SOURCE originals (NOT served): logos, teacher
                        photo, class photos, "Überblick web-site.xlsx" course
                        catalogue. Optimised copies are derived into docs/assets/img.
read_excel.py         ← reads the course catalogue xlsx → CSV
```

**Localization is by copy-translation, not a framework — this is intentional.**
Each language is a fully self-contained HTML page; translated strings are
hard-coded. To add a language (French/Italian/Spanish are planned):

1. Copy `docs/de/` → `docs/fr/` (or `it`/`es`) and translate all visible text,
   `lang="…"`, `<title>`, meta description, and `alt`/`aria` text.
2. Update the **language switcher** (in every page's `<header>` and `<footer>`)
   and the `<link rel="alternate" hreflang>` tags on every page.

**Path conventions** (keep relative so the Pages sub-path works):
- Root page (`docs/index.html`): `assets/...`, language links like `de/`.
- Sub-folder pages (`docs/de/index.html`): `../assets/...`, EN link `../`.

**Theming:** every brand colour lives in CSS custom properties in `:root` at the
top of `docs/assets/styles.css`. Re-skin there; the rest of the CSS references
the variables. Headings use Poppins, body uses Inter (loaded from Google Fonts).

**Content source of truth:** course levels and descriptions come from
`materials/Überblick web-site.xlsx` (run `read_excel.py` to read it).

## Before-launch placeholders

`docs/README.md` tracks the real-content items still to be confirmed with Maria
(bio specifics, address, the "first lesson free" offer, class-photo consent,
phone number). On-page placeholders are wrapped in `<span class="placeholder">`
(highlighted yellow) — grep for that class to find them.
