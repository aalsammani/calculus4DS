# Coverage Matrix — CSCI 504 Syllabus ↔ Textbook

Every topic on the CSCI 504 (Calculus and Matrix Fundamentals) syllabus, mapped to the chapters and sections that teach it. Reference texts on the syllabus: OpenStax Calculus Vols. 1–3, Goodfellow et al. Ch. 2, Strang.

| Syllabus topic | Chapter(s) | Notes |
|---|---|---|
| **Review of functions; exponential, logarithmic, trigonometric functions** | Ch. 1, Ch. 2 | Radians established as default; log laws; unit-circle trig |
| **Limits and the derivative** | Ch. 3 | Difference quotients, tangent problem, continuity |
| **Differentiation rules** | Ch. 4 | Power/product/quotient rules, higher derivatives, optimization |
| **The chain rule; derivatives of transcendentals** | Ch. 5 | Includes implicit differentiation |
| **Linearization and Newton's method** | Ch. 6 | Revisited in Chs. 18, 22–23 (multivariable Newton) |
| **Antiderivatives; the Fundamental Theorem of Calculus** | Ch. 7 | Both parts of FTC; improper integrals |
| **Integration by substitution** | Ch. 8 | Reframed as 1-D change of variables in Ch. 25 |
| **Areas between curves; volumes** | Ch. 9 | Disks, washers, shells; average value |
| **Integration by parts; trigonometric substitution** | Ch. 10 | Powers the orthogonality integrals of Ch. 14 |
| **Numerical integration** | Ch. 11 | Midpoint/trapezoid/Simpson with error orders; extended to 2-D and Monte Carlo in Ch. 24 |
| **Summation notation, sequences, and series** | Ch. 12 | Geometric/harmonic/p-series, convergence tests |
| **Power series and Taylor series** | Ch. 13 | Radius of convergence; standard expansions; error bounds |
| **Fourier series** (optional topic) | Ch. 14 | Coefficients via orthogonality; Gibbs; Parseval; linked to dot products (Ch. 16) and eigenbases (Ch. 20) |
| **Vectors in the plane and in space** | Ch. 15 | Components, arrows, linear combinations, norms |
| **The dot product and the cross product** | Ch. 16 | Angles, orthogonality, projection (→ least squares), areas |
| **Matrices and matrix operations** | Ch. 17 | Matrix as transformation; composition; transpose; design matrices |
| **Systems of linear equations; Gauss–Jordan elimination** | Ch. 18 | Row/column pictures, RREF, rank, free variables, inverses |
| **Determinants** | Ch. 19 | Cofactors, pivot products, volume scaling, laws |
| **Eigenvalues and eigenvectors** | Ch. 20 | Characteristic polynomial, diagonalization, powers, spectral theorem, PCA/Markov applications |
| **Vector-valued functions** | Ch. 21 | Velocity/acceleration, projectile motion, arc length |
| **Functions of several variables; limits** | Ch. 22 §22.1 | Surfaces, contour maps, path-dependence of limits |
| **Partial derivatives** | Ch. 22 §22.2 | Higher/mixed partials, Clairaut, Hessian |
| **Multivariable chain rule** | Ch. 22 §22.4 | One-term-per-path form; backpropagation connection |
| **Directional derivatives and the gradient** | Ch. 23 | Steepest ascent, level-set orthogonality, critical points, gradient descent |
| **Double integrals** | Ch. 24 | Fubini, general regions, order reversal, probability applications |
| **Polar coordinates; integrals in polar form** | Ch. 25 | Jacobian $r$, polar areas, Gaussian integral |

## Pedagogical cycle compliance

Every chapter contains: motivation → intuition → formal definitions ({prf:definition}) → derivations → 3+ graded worked examples → do-by-hand work → Python implementation (NumPy/SciPy/SymPy/Matplotlib only) → visualization with interpretation → Common Mistakes (warning admonition) → tiered exercises (Quick Check → Basic → Intermediate → Conceptual → Python → Visualization → Challenge → Cumulative Review) with collapsible hints/solutions → summary → parallel reading pointer into the syllabus's reference texts.

## Cross-references into data science practice

Least squares/regression: Chs. 16, 17, 18, 22, 23 · Gradient descent & conditioning: Chs. 12, 20, 23 · PCA & spectral methods: Ch. 20 · Markov chains/PageRank: Chs. 17, 20 · Probability integrals & Gaussians: Chs. 24, 25 · Backpropagation: Chs. 5, 22, 23 · Monte Carlo: Chs. 11, 24 · Numerical practice (conditioning, `solve` vs `inv`, float comparison): Chs. 11, 18, 19.
