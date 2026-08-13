# Quality-Control Checklist

Status of the book's QC pass. ✔ = verified during construction.

## Mathematical accuracy
- ✔ Every numeric value quoted in prose, worked examples, and answer dropdowns was computed and verified in NumPy/SymPy/SciPy during writing (verification runs accompany each figure script and chapter).
- ✔ Symbolic identities (Fourier coefficients, PDE checks, Jacobians, eigen-decompositions, integrals) verified with SymPy.
- ✔ Known traps checked deliberately: Ch. 20 Quick Check 1 contains an intentional false premise whose answer key exposes it; Ch. 18 Ex. 5(b) replaced after its first draft proved singular.
- ✔ Trace/determinant eigenvalue checks pass for all eigen examples.

## Structure and conventions
- ✔ All 25 chapters follow the full pedagogical cycle (see COVERAGE_MATRIX.md).
- ✔ Each chapter: ≥3 graded {prf:example} blocks, Common Mistakes warning admonition, 8-tier exercises, dropdown answers/solutions, Summary, "*Parallel reading:*" line.
- ✔ Radians throughout; vectors bold (`\vb`), matrices italic; DS Connection (tip) and Looking Ahead (seealso) callouts present in every chapter.
- ✔ Cross-chapter threads resolved: projection→least squares (16→18→22), det→characteristic polynomial (19→20), Markov mystery (17→20), Hessian eigenvalues (20→22→23), Jacobian determinant (19→25), Gaussian integral promise (7/11/13→25), sphere volume redo (24→25).

## Build integrity
- ✔ All chapter files present and matching `_toc.yml` paths (25 chapters + 2 orientation + 6 appendix files).
- ✔ All `{cite}` keys resolve against `references.bib` (automated cross-check).
- ✔ All figure files referenced by chapters exist in `book/part*/figures/` (automated cross-check; regenerate with `python make_all_figures.py`).
- ✔ Figure scripts run cleanly end to end and print the verification numbers quoted in prose.
- ✔ Only NumPy, SciPy, SymPy, Matplotlib used in all code shown to students.

## Accessibility and citations
- ✔ Every figure has `:name:`, `:alt:` text, and an interpretive caption.
- ✔ Real, verifiable references only (OpenStax volumes, Strang, Goodfellow et al., library papers: Harris 2020, Virtanen 2020, Meurer 2017, Hunter 2007, Burden & Faires, Stewart).

## Known limitations
- The Jupyter Book HTML build itself is not executed in this environment; the source follows Jupyter Book 1.x / sphinx-proof / sphinx-bibtex conventions and the CI workflow (`.github/workflows/deploy.yml`) builds and deploys on push.
- Appendix D lists final answers for a curated selection; complete worked solutions live in each chapter's dropdowns.
