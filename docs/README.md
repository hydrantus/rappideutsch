# Rappideutsch — website

A simple, static website for **Rappideutsch**, a private German school in
Rapperswil-Jona (teacher: Maria Bernardina Milano).

No framework, no build step — just HTML, CSS and a few lines of vanilla
JavaScript. You can open `index.html` directly in a browser, or serve the
folder with any static web server.

## Structure

```
docs/
├── index.html        ← English (default)
├── de/index.html     ← German
├── it/index.html     ← Italian
├── fr/index.html     ← French
├── assets/
│   ├── styles.css    ← all styling (brand colours live in :root at the top)
│   ├── app.js        ← mobile menu + header shadow
│   └── img/          ← optimised logo, teacher photo, class photos, favicon
├── sitemap.xml       ← the four language pages, for search engines
├── robots.txt        ← points at the sitemap
└── .nojekyll         ← tells GitHub Pages to serve files as-is
```

Each language is a self-contained, copy-translated page, so every text change
has to be made in all four. To add Spanish later, copy `de/` to `es/`,
translate the text, and add the language to the switcher in every page's
header/footer.

## Local preview

```bash
cd docs
python3 -m http.server 8000
# then open http://localhost:8000
```

## Deployment

The site is live at **https://rappideutsch.ch/** via GitHub Pages
(Settings → Pages: *Deploy from a branch*, `main`, `/docs`). The `CNAME` file
in this folder sets the custom domain; DNS for `rappideutsch.ch` is managed at
Infomaniak and points at GitHub Pages. Pushing to `main` redeploys within a
minute. `www.rappideutsch.ch` and the old `hydrantus.github.io/rappideutsch/`
address redirect to the domain.

## ⚠️ Placeholders to confirm with Maria before going live

- ~~**Bio — years of experience**~~ — done: "over 20 years" / "über 20 Jahre"
  (Maria confirmed). Languages confirmed too: German, Italian, English.
- ~~**Email**~~ — done: `info@rappideutsch.ch` is live and forwards to Maria's
  Gmail, which can also reply from that address.
- ~~**"First lesson free"**~~ — removed (Maria didn't want it). Replaced by a
  **Prices** section; the call to action is now simply "get in touch".
- ~~**Address**~~ — done: Bernardina Milano, Neuhüsli-Park 12, 8645 Rapperswil-Jona.
- ~~**Class photos**~~ — confirmed.
- ~~**Phone/WhatsApp**~~ `+41 76 649 11 55` — confirmed.

## 🗓 Scheduled change: online price on 1 January 2027

The online lesson is CHF 15 / 60 min as a launch price **until 31 Dec 2026**,
then CHF 19 / 60 min. On 1 Jan 2027 update the "Online" price card in
`index.html`, `de/index.html`, `it/index.html` and `fr/index.html`: change
the price to CHF 19, delete the launch-price note, and in the JSON-LD block in
each page's `<head>` change the online offer's `price` to 19 and remove its
`priceValidUntil`.

## Search visibility (outside the code)

- Register https://rappideutsch.ch/ in Google Search Console and submit
  `https://rappideutsch.ch/sitemap.xml`.
- Create a Google Business Profile for Rappideutsch with the Neuhüsli-Park 12
  address, phone and website — for a local school this brings more visitors
  than any on-page change.
```
