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

## Deploying to GitHub Pages

1. Push this repository to GitHub.
2. Repo **Settings → Pages**.
3. **Source:** *Deploy from a branch*. **Branch:** `main`, **Folder:** `/docs`.
4. Save. The site goes live at `https://<user>.github.io/<repo>/` in a minute.

(For a custom domain like `rappideutsch.ch`, add it under Settings → Pages and
point a CNAME at GitHub.)

## ⚠️ Placeholders to confirm with Maria before going live

- **Bio — years of experience** — highlighted in yellow on the page (`[X years]`).
  (Languages confirmed: German, Italian, English — already in the bio.)
- **Email** — `info@rappideutsch.ch` is published as a contact option; confirm
  the domain/mailbox is set up before going live.
- **"First lesson free"** — used as the main call to action. Remove or adjust
  if that's not the offer.
- **Address** — currently "to be confirmed" in Rapperswil-Jona.
- **Class photos** — please confirm the students pictured are happy to appear
  on a public website.
- **Phone/WhatsApp** `+41 76 649 11 55` — confirm correct.
```
