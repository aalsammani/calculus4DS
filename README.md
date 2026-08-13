# Calculus and Matrix Fundamentals

An open, interactive textbook for **CSCI 504: Calculus and Matrix Fundamentals**, the graduate mathematics bridge course for the Data Science MS program. The book covers single-variable differential and integral calculus, series and Taylor approximation, vectors and matrix fundamentals, and multivariable calculus, following the course syllabus.

The book's pedagogical cycle for every major concept is:

**Understand → Do by Hand → Implement in Python → Visualize → Interpret → Practice**

Students first learn the mathematics and carry out the essential calculations by hand; Python is then used to verify, explore, and visualize, never to replace understanding.

## Repository layout

```
csci504-textbook/
├── README.md                  ← this file
├── LICENSE                    ← licensing recommendation (CC BY 4.0 + MIT)
├── requirements.txt           ← build and computational environment
├── COVERAGE_MATRIX.md         ← syllabus-topic → chapter/section map
├── QC_CHECKLIST.md            ← chapter-level quality-control checklist
├── PROGRESS.md                ← authoring status and continuation point
├── .github/workflows/deploy.yml  ← GitHub Pages CI deployment
├── book/                      ← Jupyter Book source
│   ├── _config.yml            ← book configuration
│   ├── _toc.yml               ← table of contents / navigation
│   ├── references.bib         ← BibTeX bibliography
│   ├── index.md               ← landing page
│   ├── getting-started.md     ← how to read the book, set up Python
│   ├── notation.md            ← book-wide notation guide
│   ├── part0/ … part5/        ← chapters (MyST Markdown)
│   └── appendices/            ← reference sheets, answers, glossary
└── figures/scripts/           ← Python scripts that generate every figure
```

Every figure in the book is produced by a script in `figures/scripts/`; no figure is hand-drawn or imported from elsewhere, so the entire book is reproducible from source.

## Installing dependencies

Python 3.10+ is required. From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Building the book locally

```bash
jupyter-book build book/
```

The HTML site is written to `book/_build/html/`. Open `book/_build/html/index.html` in a browser. To force a clean rebuild:

```bash
jupyter-book clean book/ && jupyter-book build book/
```

## Regenerating figures

```bash
python figures/scripts/make_all_figures.py
```

This regenerates every PNG under `book/*/figures/`. Individual figure scripts can also be run directly; each is self-contained and documents which figure(s) it produces.

## Running the notebooks

Chapters are MyST Markdown with embedded, pre-verified code. Companion executable notebooks (where present, under `book/notebooks/`) can be run with:

```bash
jupyter lab
```

or opened in Google Colab via the launch button on each notebook page of the built site.

## Publishing with GitHub Pages

1. Create a GitHub repository and push this project to the `main` branch.
2. Update `repository.url` in `book/_config.yml` to the new repository URL.
3. In the repository **Settings → Pages**, set the source to **GitHub Actions**.
4. Push to `main`. The workflow in `.github/workflows/deploy.yml` builds the book and deploys it; the site URL appears in the workflow summary.

No manual `ghp-import` step is needed; deployment is fully automated by CI.

## Maintaining and updating the book

- Edit chapter files under `book/`; the navigation lives in `book/_toc.yml`.
- Keep notation consistent with `book/notation.md`.
- Add new references to `book/references.bib` and cite with `` {cite}`key` ``.
- After edits, run a local build and skim the changed pages before pushing.
- Record chapter status changes in `PROGRESS.md` and re-run the checks in `QC_CHECKLIST.md` for any chapter you modify.
- The book is plain Markdown + Python and has no host-specific dependencies, so migrating later from GitHub Pages to university cloud hosting only requires pointing a web server (or another CI pipeline) at `book/_build/html/`.

## License

See `LICENSE` for the recommended open-licensing structure (CC BY 4.0 for content, MIT for code).
