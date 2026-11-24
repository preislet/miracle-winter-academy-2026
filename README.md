# MIRACLE Winter Academy 2026 website

Source of the course website for the MIRACLE Winter Academy 2026,
*Data Analysis and AI-Assisted Science in Biomedical Research*
(Second Faculty of Medicine, Charles University, Prague, 30 Nov – 3 Dec 2026).

Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and deployed to
GitHub Pages by `.github/workflows/deploy.yml` on every push to `main`.

## Editing

All pages are Markdown files in `docs/`:

| Path | Content |
|---|---|
| `docs/index.md` | Home: dates, venue, tracks |
| `docs/programme.md` | Full programme (one tab per day) |
| `docs/prerequisites/` | Installation instructions (macOS / Windows / Linux tabs) |
| `docs/prerequisites/environment.yml` | Course Conda environment |
| `docs/workshops/` | One page per workshop, Basic / Advanced tabs |
| `mkdocs.yml` | Site settings and navigation |

Small edits: open a file on GitHub, click the pencil icon, commit. The site redeploys within
about a minute.

Track tabs use this syntax (four-space indent inside a tab):

```markdown
=== "Basic"

    Basic-track content

=== "Advanced"

    Advanced-track content
```

Link straight to a track tab with `workshops/git.md#basic` or `#advanced`.

## Local preview

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve          # http://127.0.0.1:8000, reloads on save
.venv/bin/mkdocs build --strict # same check as CI
```

---

The MIRACLE Winter Academy is funded by MIRACLE MSCA. MIRACLE is funded by the European Union's
Horizon Europe Research and Innovation Programme under the Marie Skłodowska-Curie Actions Grant
Agreement no. 101167512.
