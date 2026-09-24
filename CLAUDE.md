# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Static marketing website for **Rappideutsch**, a private German school in
Rapperswil-Jona, Switzerland (teacher: Maria Bernardina Milano). It is a favour
project — the goal is an engaging, friendly, professional site that Maria can
review and iterate on.

Plain **HTML + CSS + a little vanilla JS**. No framework, no build step, no
`package.json`, no bundler. Files are edited and served as-is.

> **Brand spelling:** the brand is **Rappideutsch** (with an *i*). On-page text,
> alt/aria labels, the favicon, the GitHub repo (`hydrantus/rappideutsch`) and
> the live URL `https://rappideutsch.ch/` all use the *i* form.
> The only leftover *j* is this local directory name, which is cosmetic.

## Commands

```bash
# Local preview (open http://localhost:8000, or http://<this-box-LAN-IP>:8000
# from another device — the --bind is what makes it reachable over the LAN)
cd docs && python3 -m http.server 8000 --bind 0.0.0.0

# Dump the course catalogue source spreadsheet to CSV
# (auto-installs pandas + openpyxl into the active venv on first run;
#  create the venv first with `python3 -m venv .venv` if it doesn't exist)
source .venv/bin/activate && python read_excel.py

# Regenerate an optimised web image from a source original (macOS `sips`)
#   - transparent PNGs (logo): keep alpha, cap width
sips -s format png --resampleWidth 620 "materials/<source>.png" --out docs/assets/img/<name>.png
#   - transparent cutouts that are large (teacher photo): WebP with alpha, ~10x smaller
#     (needs Pillow in the venv: pip install pillow)
python3 -c "from PIL import Image; Image.open('materials/<source>.png').save('docs/assets/img/<name>.webp', 'WEBP', quality=82, method=6)"
#   - photos: re-encode JPEG, cap the long edge
sips -s format jpeg -s formatOptions 72 --resampleHeightWidthMax 1400 "materials/<source>.jpeg" --out docs/assets/img/<name>.jpg
```

There are no tests, linters, or CI.

## Deployment

GitHub Pages, **Deploy from branch → `main` → `/docs`**, on the custom domain
**`https://rappideutsch.ch/`** (`docs/CNAME`). DNS lives at Infomaniak
(domain id 2208763; API token in the gitignored `.env`): four A records on the
apex to GitHub Pages' IPs plus `www` → `hydrantus.github.io`. The old
`https://hydrantus.github.io/rappideutsch/` redirects to the domain.
`docs/.nojekyll` keeps Pages from mangling the files. Pushing to `main`
redeploys; there is no build.

**SEO plumbing (keep consistent across all language pages):** every page has
an absolute `rel="canonical"`, absolute `hreflang` links for all languages plus
`x-default` (→ English), `og:url`/`og:locale`, a meta description of ≤155
characters that leads with the local keyword ("Deutschkurse in
Rapperswil-Jona" etc.), and a JSON-LD `LanguageSchool`/`LocalBusiness` block
with the address, phone, email and the three prices. `docs/sitemap.xml` lists
the four pages with hreflang alternates and `docs/robots.txt` points at it.
Adding a language or changing prices/address means updating the JSON-LD on
every page and the sitemap too. Search Console / Google Business Profile
registration is done outside the repo by Andrej.

**All internal references use relative paths** (see below) so the site works
both on the domain root and on the github.io sub-path. The one exception:
`og:image` must be an **absolute** URL (`https://rappideutsch.ch/...`) or
WhatsApp/social previews break — that was a deliberate fix, don't revert it to
a relative path.

**Email** (`info@rappideutsch.ch`, published on the contact section): the free
Infomaniak "Starter" mail service bundled with the domain. One real mailbox,
`milano.bernardina@rappideutsch.ch`, with `info@` as an alias; everything
forwards to Maria's Gmail, which also sends as both addresses through
Infomaniak's SMTP (`mail.infomaniak.com:465`, mailbox login). MX/SPF/DKIM
records were written by Infomaniak when the service was activated — don't
touch them, and don't touch the A/CNAME records that point the site at GitHub.

**Handover:** the plan is to hand the whole thing to Maria eventually (Infomaniak
account + GitHub repo, or move the site into Infomaniak's free 10 MB Starter web
space so GitHub drops out). Until then the Infomaniak API token in `.env` stays.
Note that "connecting" the domain to Infomaniak web hosting in their manager
rewrites the apex A records and would silently take the site off GitHub Pages.

## Architecture

```
docs/                 ← the published website (this is the Pages root)
  index.html          ← English (site root)
  de/index.html       ← German
  it/index.html       ← Italian
  fr/index.html       ← French
  assets/styles.css   ← ALL styling
  assets/app.js       ← mobile nav toggle + header shadow on scroll (that's it)
  assets/img/         ← optimised, web-sized assets actually served
  sitemap.xml, robots.txt
materials/            ← large SOURCE originals (NOT served): logos, teacher
                        photo, class photos, "Überblick web-site.xlsx" course
                        catalogue. Optimised copies are derived into docs/assets/img.
  unused-drafts/      ← rejected/unused concepts (AI logo drafts etc.), kept
                        for reference only; nothing here is used anywhere
read_excel.py         ← reads the course catalogue xlsx → CSV
```

**Localization is by copy-translation, not a framework — this is intentional.**
Each language is a fully self-contained HTML page; translated strings are
hard-coded. Any content change must be made in **all four** pages (`en`,
`de`, `it`, `fr`). To add a language (Spanish is possible later):

1. Copy `docs/de/` → `docs/es/` and translate all visible text,
   `lang="…"`, `<title>`, meta description, and `alt`/`aria` text.
2. Update the **language switcher** (in every page's `<header>` and `<footer>`)
   and the `<link rel="alternate" hreflang>` tags on every page.
3. Add the new URL to `docs/sitemap.xml` (as its own `<url>` and as an
   `xhtml:link` alternate in every entry) and set `canonical`, `og:url`,
   `og:locale` and the JSON-LD `url`/`inLanguage`/`description` on the new page.

**Path conventions** (keep relative so the Pages sub-path works):
- Root page (`docs/index.html`): `assets/...`, language links like `de/`.
- Sub-folder pages (`docs/de/`, `docs/it/`, `docs/fr/`): `../assets/...`, EN link `../`, sibling language `../de/`.

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

**Dated content:** the online lesson price (`#prices` section, all four pages) is a
launch price valid until 31 Dec 2026 and must be changed to CHF 19 on 1 Jan
2027 in the price card **and** in the JSON-LD offer (`priceValidUntil`) on all
four pages — see `docs/README.md`.
