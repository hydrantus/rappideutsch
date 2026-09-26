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
# from another device — it binds 0.0.0.0 so it is reachable over the LAN).
# Use this rather than `python3 -m http.server`: plain http.server sends no
# Cache-Control, so a reviewing browser can keep serving an old styles.css for
# an entire session and every CSS change looks like it silently did nothing.
python3 serve.py

# Dump the course catalogue source spreadsheet to CSV
# (auto-installs pandas + openpyxl into the active venv on first run;
#  create the venv first with `python3 -m venv .venv` if it doesn't exist)
source .venv/bin/activate && python read_excel.py

# Regenerate an optimised web image from a source original.
# On Linux (no `sips`) use Pillow for all of the below, e.g.
#   python3 -c "from PIL import Image; im=Image.open(SRC); im.resize(...).save(DST, quality=84)"
# macOS `sips` recipes:
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
`rappideutsch-handover.md` in the project root is Andrej's handover note for
Maria and contains **plaintext account passwords**: it is gitignored, must
never be committed, quoted, or copied anywhere, and its contents must not be
read into a response. `tmp/` is a gitignored local scratch folder.
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
  intern/             ← hidden pages, not linked from anywhere on the site
                        and disallowed in robots.txt (still publicly
                        reachable by direct URL — nothing here is secret).
                        intern/logo-foto/ is a one-off feedback page for
                        Maria's peers to compare logo/photo options; safe
                        to delete once she's done collecting opinions.
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

## Content status

All real-content items (experience, address, phone, class-photo consent,
email) were confirmed by Maria on 2026-09-24; `docs/README.md` keeps the
ticked-off list. **The hero photo is now an opaque 3:4 shot of Maria at her
desk** (`docs/assets/img/teacher.webp`, from `materials/20260926 Lehrerin -
Arbeitszimmer.jpg`), not the old transparent cut-out — so `.hero-photo` is a
rounded, shadowed frame and `.hero-blob` is the offset colour card behind it.
Swapping in another photo means keeping the 3:4 ratio or adjusting both rules
plus the `width`/`height` attributes on all four pages. **Maria does not want a "first lesson free" offer** — it was
removed and replaced by the Prices section; don't reintroduce it. The Italian
and French pages are Claude translations from the German page and have not
yet been proof-read by a native speaker or by Maria.

If a placeholder is ever needed again, wrap it in `<span class="placeholder">`
(highlighted yellow) so it is easy to grep for.

**Dated content:** the online lesson price (`#prices` section, all four pages) is a
launch price valid until 31 Dec 2026 and must be changed to CHF 19 on 1 Jan
2027 in the price card **and** in the JSON-LD offer (`priceValidUntil`) on all
four pages — see `docs/README.md`.

**Logo change (2026-09-26):** Maria picked the castle/puzzle logo that was
shown as "Konzept 3" on the internal feedback page. Its source original is
`materials/20260926 Rappideutsch logo - Burg.png` (it was promoted out of
`materials/unused-drafts/`). Everything under `docs/assets/img/` that carries
the logo was regenerated from it: `logo.png`, `logo-mark.webp`,
`logo-wordmark.webp`, `logo-dark.png`, `logo-og.jpg` and `favicon.svg` (now a
hand-drawn castle, no longer the mountains-and-lake motif). The source has an
off-white paper background, not transparency — the transparent copies were cut
by keying out the paper colour and un-premultiplying the anti-aliased edges, so
re-deriving them by naive thresholding will produce visible fringes. The logo's
blue `#2d75a7` and orange `#f07b19` are now `--blue` and `--orange` in
`:root`; the orange also replaced the Swiss red on the `.eyebrow .dot`.

**Logo prominence (resolved 2026-09-25):** the header uses a side-by-side
lockup made from two crops of the source PNG, `docs/assets/img/logo-mark.webp`
(castle mark) and `docs/assets/img/logo-wordmark.webp` (the "Rappideutsch"
wordmark), classes `.brand-mark` / `.brand-word` — under 600px only the icon
shows. **Both crops are trimmed tight to the artwork, with no transparent
padding**, because `.brand` aligns them with `align-items: flex-end`: the
wordmark's baseline is meant to land on the castle's base line, and the
negative `margin-bottom` on `.brand-word` is exactly the depth of the "pp"
descenders (18.65% of the wordmark's height) so they hang below it. Re-export
either crop with padding and that alignment drifts. The footer logo (`logo-dark.png`) is sized to fill the same vertical
space as the nav columns beside it (`.footer-brand img`, currently 200px
tall), with no separate tagline paragraph since the logo already contains it.
There is deliberately no logo in the hero — it was tried and dropped as
redundant with the header.
