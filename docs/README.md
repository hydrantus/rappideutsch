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
├── assets/
│   ├── styles.css    ← all styling (brand colours live in :root at the top)
│   ├── app.js        ← mobile menu + header shadow
│   └── img/          ← optimised logo, teacher photo, class photos, favicon
└── .nojekyll         ← tells GitHub Pages to serve files as-is
```

Each language is a self-contained, copy-translated page. To add French,
Italian or Spanish later, copy `de/` to `fr/` / `it/` / `es/`, translate the
text, and add the language to the switcher in every page's header/footer.

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

- **Bio — years of experience** — highlighted in yellow on the page (`[X years]`).
  (Languages confirmed: German, Italian, English — already in the bio.)
- ~~**Email**~~ — done: `info@rappideutsch.ch` is live and forwards to Maria's
  Gmail, which can also reply from that address.
- **"First lesson free"** — used as the main call to action. Remove or adjust
  if that's not the offer.
- **Address** — currently "to be confirmed" in Rapperswil-Jona.
- **Class photos** — please confirm the students pictured are happy to appear
  on a public website.
- **Phone/WhatsApp** `+41 76 649 11 55` — confirm correct.
```
