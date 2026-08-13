# Appendix E · Glossary

Concise definitions of the book's technical vocabulary, with the chapter where each term is introduced.

**Antiderivative** (Ch. 7) — a function $F$ with $F' = f$; unique up to an added constant.

**Arc length** (Chs. 9, 21) — the length of a curve; $\int\|\vb r'(t)\|\,dt$ for a parametrized curve.

**Augmented matrix** (Ch. 18) — coefficient matrix with the right-hand side appended, $[\mathit A\mid\vb b]$, for bookkeeping elimination.

**Chain rule** (Chs. 5, 22) — derivative of a composition: outer derivative at the inner value times inner derivative; in several variables, one such product per dependency path, summed.

**Characteristic polynomial** (Ch. 20) — $\det(\mathit A - \lambda\mathit I)$; its roots are the eigenvalues.

**Concavity** (Ch. 4) — the direction a graph bends; the sign of $f''$.

**Condition number** (Chs. 18, 23) — sensitivity measure of a matrix/problem; for symmetric positive definite matrices, $\lambda_{\max}/\lambda_{\min}$; governs gradient descent's difficulty.

**Continuous** (Chs. 3, 22) — limit equals value; in several variables, along every approach path.

**Contour map / level curve** (Ch. 22) — the sets $f(x,y) = c$ drawn in the domain; spacing encodes steepness.

**Convergence** (Ch. 12) — a sequence or series approaching a finite limit; for series, convergence of the partial-sum sequence.

**Critical point** (Chs. 4, 23) — where the derivative (gradient) vanishes; candidate for extremum, classified by second-order information.

**Cross product** (Ch. 16) — $\vb u\times\vb v$ in $\mathbb{R}^3$: vector orthogonal to both factors, magnitude the spanned parallelogram's area.

**Determinant** (Ch. 19) — signed volume-scaling factor of a square matrix's transformation; zero exactly for singular matrices.

**Diagonalization** (Ch. 20) — factoring $\mathit A = \mathit P\mathit D\mathit P^{-1}$ with eigenvectors in $\mathit P$, eigenvalues in diagonal $\mathit D$.

**Directional derivative** (Ch. 23) — rate of change of $f$ along a unit direction: $D_{\vb u}f = \nabla f\cdot\vb u$.

**Dot product** (Ch. 16) — $\sum u_iv_i = \|\vb u\|\|\vb v\|\cos\theta$; encodes length and angle; zero means orthogonal.

**Double integral** (Ch. 24) — Riemann limit of box volumes over a plane region; computed as iterated single integrals (Fubini).

**Eigenvalue / eigenvector** (Ch. 20) — a scaling factor and invariant direction of a matrix: $\mathit A\vb v = \lambda\vb v$, $\vb v \ne \vb 0$.

**Fourier series** (Ch. 14) — expansion of a periodic function in sines and cosines, coefficients by orthogonality integrals.

**Fundamental Theorem of Calculus** (Ch. 7) — differentiation and integration are inverse: $\int_a^b f = F(b) - F(a)$, and the accumulation function's derivative is the integrand.

**Gaussian integral** (Ch. 25) — $\int_{-\infty}^\infty e^{-x^2}dx = \sqrt\pi$; evaluated by squaring and converting to polar coordinates.

**Gradient** (Ch. 23) — $\nabla f$, the vector of partial derivatives; points in the direction of steepest ascent, perpendicular to level sets.

**Gradient descent** (Ch. 23) — iterative minimization $\vb x \leftarrow \vb x - \eta\nabla f(\vb x)$; the training algorithm of machine learning.

**Hessian** (Chs. 22–23) — the symmetric matrix of second partials; its eigenvalues classify critical points and set optimization difficulty.

**Improper integral** (Ch. 7) — integral with an infinite limit or unbounded integrand, defined as a limit of proper ones.

**Integration by parts** (Ch. 10) — $\int u\,dv = uv - \int v\,du$; the product rule integrated.

**Jacobian** (Chs. 22, 25) — matrix of partial derivatives of a transformation; its determinant is the local area/volume scaling used in change of variables.

**Learning rate** (Ch. 23) — the step-size multiplier $\eta$ in gradient descent.

**Limit** (Ch. 3) — the value a function approaches as its input approaches a point; the foundation beneath derivative and integral.

**Linear combination** (Ch. 15) — $c_1\vb v_1 + \cdots + c_k\vb v_k$; the master construction of linear algebra.

**Linearization / tangent plane** (Chs. 6, 22) — best linear approximation at a point: $f(a) + f'(a)(x-a)$, or with one correction term per variable.

**Magnitude / norm** (Ch. 15) — vector length $\sqrt{\sum v_i^2}$.

**Matrix** (Ch. 17) — rectangular number array; equivalently a linear transformation whose columns are the images of the basis vectors.

**Monte Carlo integration** (Ch. 24) — estimating integrals by averaging over random samples; error $\sim 1/\sqrt N$ in any dimension.

**Newton's method** (Chs. 6, 18, 23) — root-finding/optimization by repeatedly solving the linearized problem.

**Orthogonal** (Ch. 16) — perpendicular; dot product zero.

**Partial derivative** (Ch. 22) — derivative in one variable with the others held fixed.

**Pivot** (Ch. 18) — leading nonzero entry of a row in elimination; the pivot count is the rank.

**Polar coordinates** (Ch. 25) — $(r,\theta)$: distance and direction; area element $r\,dr\,d\theta$.

**Power series / Taylor series** (Ch. 13) — infinite polynomial $\sum c_k(x-a)^k$; Taylor's coefficients come from derivatives at the center.

**Projection** (Ch. 16) — component of one vector along another: $\frac{\vb a\cdot\vb b}{\vb a\cdot\vb a}\vb a$; the seed of least squares.

**Radius of convergence** (Ch. 13) — half-width of the interval where a power series converges.

**Rank** (Ch. 18) — number of pivots; the independent information in a matrix's rows/columns.

**Riemann sum** (Ch. 7) — sample-value × piece-size, summed; its refinement limit defines the integral.

**RREF** (Ch. 18) — reduced row echelon form; the terminus of Gauss–Jordan elimination where solutions are read off.

**Saddle point** (Chs. 22–23) — critical point rising in one direction and falling in another; mixed-sign Hessian eigenvalues.

**Singular matrix** (Chs. 18–19) — square matrix with no inverse; determinant zero; collapses some direction.

**Spectral theorem** (Ch. 20) — symmetric matrices have real eigenvalues and orthonormal eigenvectors.

**Substitution** (Ch. 8) — the chain rule integrated; change of variable with $dx$ converted.

**Transpose** (Ch. 17) — rows-for-columns flip $\mathit A^{\mathsf T}$; reverses products.

**Unit vector** (Ch. 15) — vector of magnitude 1; pure direction, produced by normalization $\vb v/\|\vb v\|$.

**Vector** (Ch. 15) — ordered list of numbers; equivalently an arrow with direction and length.

**Vector-valued function** (Ch. 21) — a curve: scalar input, vector output; differentiates componentwise into velocity and acceleration.
