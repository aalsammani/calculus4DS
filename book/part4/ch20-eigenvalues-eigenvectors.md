# Chapter 20 · Eigenvalues and Eigenvectors

A matrix moves every vector — stretching, rotating, shearing all of $\mathbb{R}^n$ at once. Yet almost every matrix keeps a few secret directions along which its action is embarrassingly simple: vectors on those lines are merely *scaled*, never turned. Those directions are the **eigenvectors**, the scaling factors are the **eigenvalues**, and together they are the matrix's skeleton: they predict what powers $\mathit A^k$ do in the long run (settling Chapter 17's Markov mystery), they are the axes of the ellipse every linear map makes from a circle, and — as principal component analysis — they are how data science finds the directions that matter in a cloud of high-dimensional data.

## 20.1 The defining equation

```{prf:definition} Eigenvalue and eigenvector
:label: def-eigen
A nonzero vector $\vb v$ is an **eigenvector** of a square matrix $\mathit A$, with **eigenvalue** $\lambda$, if

$$
\mathit A\vb v = \lambda\,\vb v
$$

— the output is a scalar multiple of the input: same line through the origin, length scaled by $\lambda$ (and reversed if $\lambda < 0$). The zero vector is excluded (it satisfies the equation trivially for every $\lambda$), but $\lambda = 0$ is allowed — an eigenvalue $0$ means some direction is crushed to the origin.
```

Every nonzero multiple of an eigenvector is again an eigenvector with the same $\lambda$ (linearity), so eigenvectors are really eigen-*directions*; one usually reports a convenient representative or a unit vector.

How to find them? Rearrange the defining equation:

$$
\mathit A\vb v = \lambda\vb v
\iff
(\mathit A - \lambda\mathit I)\,\vb v = \vb 0.
$$

A *nonzero* solution $\vb v$ exists exactly when the matrix $\mathit A - \lambda\mathit I$ is singular — and Chapter 19 built the singularity detector:

```{prf:theorem} Characteristic equation
:label: thm-characteristic
$\lambda$ is an eigenvalue of $\mathit A$ if and only if

$$
\det(\mathit A - \lambda\mathit I) = 0.
$$

For an $n\times n$ matrix the left side is a degree-$n$ polynomial in $\lambda$ (the **characteristic polynomial**), so there are at most $n$ eigenvalues; the eigenvectors for each $\lambda$ are the nonzero solutions of the homogeneous system $(\mathit A - \lambda\mathit I)\vb v = \vb 0$, found by elimination.
```

The workflow is thus a tour of the whole Part: a determinant finds the $\lambda$'s (Chapter 19), elimination with free variables finds the $\vb v$'s (Chapter 18), and the meaning lives in the transformation picture (Chapter 17).

```{prf:example} The full computation
:label: ex-eigen-computation
Find the eigenvalues and eigenvectors of $\mathit A = \begin{bmatrix}2 & 1\\ 1 & 2\end{bmatrix}$.

**Eigenvalues.**

$$
\det(\mathit A - \lambda \mathit I) = \begin{vmatrix}2-\lambda & 1\\ 1 & 2-\lambda\end{vmatrix}
= (2-\lambda)^2 - 1 = \lambda^2 - 4\lambda + 3 = (\lambda - 3)(\lambda - 1),
$$

so $\lambda_1 = 3$ and $\lambda_2 = 1$.

**Eigenvectors.** For $\lambda_1 = 3$: $(\mathit A - 3\mathit I)\vb v = \begin{bmatrix}-1 & 1\\ 1 & -1\end{bmatrix}\vb v = \vb 0$ gives $v_1 = v_2$ — a free-variable line, exactly as a singular system must — so $\vb v_1 = \langle 1, 1\rangle$. For $\lambda_2 = 1$: $\begin{bmatrix}1&1\\1&1\end{bmatrix}\vb v = \vb 0$ gives $v_2 = -v_1$, so $\vb v_2 = \langle 1, -1 \rangle$.

**Check** (always one multiplication): $\mathit A\langle1,1\rangle = \langle 3,3\rangle = 3\langle1,1\rangle$ ✓; $\ \mathit A\langle1,-1\rangle = \langle 1,-1\rangle$ ✓.

**Two free consistency tests:** the **trace** (diagonal sum) equals the eigenvalue sum: $2 + 2 = 3 + 1$ ✓; and the determinant equals the eigenvalue *product*: $4 - 1 = 3\cdot1$ ✓. These identities hold for every square matrix and catch most arithmetic errors instantly.
```

```{figure} figures/ch20-eigen-directions.png
:name: fig-eigen-directions
:alt: The unit circle and its image under A, an ellipse tilted at 45 degrees; a long arrow along the direction one-one labeled lambda equals three, and a shorter arrow along one-negative-one labeled lambda equals one, marking the ellipse's axes.

$\mathit A = \begin{bmatrix}2&1\\1&2\end{bmatrix}$ sends the unit circle to an ellipse — and the eigenvectors are the directions that don't turn: along $\langle 1,1\rangle$ vectors stretch by $3$; along $\langle 1,-1\rangle$ they stay put ($\lambda = 1$). Those two invariant directions are precisely the ellipse's axes: Chapter 17's circle-to-ellipse observation, explained.
```

Geometrically, {numref}`fig-eigen-directions` is the whole story: a generic vector, being a mix of the two eigen-directions, gets its $\langle1,1\rangle$-part tripled and its $\langle1,-1\rangle$-part left alone, and therefore *turns* toward the dominant direction — but the eigen-directions themselves only stretch. That "mix, scale each part, reassemble" reading is the key that unlocks matrix powers.

## 20.2 Diagonalization: the eigenbasis view

Suppose $\mathit A$ ($n\times n$) has $n$ linearly independent eigenvectors $\vb v_1, \ldots, \vb v_n$ with eigenvalues $\lambda_1, \ldots, \lambda_n$. Pack the eigenvectors as columns of $\mathit P$ and the eigenvalues into a diagonal $\mathit D$; then the $n$ equations $\mathit A\vb v_i = \lambda_i\vb v_i$ compress into $\mathit A\mathit P = \mathit P\mathit D$, i.e.

$$
\mathit A = \mathit P\,\mathit D\,\mathit P^{-1}
\qquad\text{(}\mathit A\text{ is \textbf{diagonalizable}).}
$$

Read right to left, this factorization *narrates* the transformation: $\mathit P^{-1}$ re-expresses the input in eigen-coordinates ("how much of each $\vb v_i$?"), $\mathit D$ scales each coordinate by its $\lambda_i$ — the transformation is trivial in the right coordinates — and $\mathit P$ translates back. Chapter 15's slogan that *coordinates are coefficients* pays off here: the eigenbasis is the coordinate system in which $\mathit A$ is just a diagonal stretch.

The immediate dividend is **powers**:

$$
\mathit A^k = (\mathit P\mathit D\mathit P^{-1})(\mathit P\mathit D\mathit P^{-1})\cdots = \mathit P\,\mathit D^k\,\mathit P^{-1},
\qquad
\mathit D^k = \operatorname{diag}(\lambda_1^k, \ldots, \lambda_n^k)
$$

— the inner $\mathit P^{-1}\mathit P$ pairs annihilate, and powering a matrix reduces to powering numbers. Equivalently, expanding a starting vector in the eigenbasis, $\vb x_0 = c_1\vb v_1 + \cdots + c_n\vb v_n$:

$$
\mathit A^k\vb x_0 = c_1\lambda_1^k\vb v_1 + \cdots + c_n\lambda_n^k\vb v_n.
$$

Long-run behavior is now legible from the eigenvalues alone: components with $|\lambda| < 1$ decay geometrically, $|\lambda| > 1$ explode, $\lambda = 1$ persist — and the largest $|\lambda|$ wins. Chapter 17's Exercise 20 puzzle (why the shear's iterates grow linearly while the rotation's cycle) and Chapter 12's geometric sequences have become one theory.

```{prf:example} The Markov chain, solved
:label: ex-eigen-markov
Chapter 17's subscription model iterated $\mathit P = \begin{bmatrix}0.9 & 0.2\\ 0.1 & 0.8\end{bmatrix}$ and crept numerically toward $\langle\tfrac23, \tfrac13\rangle$. Explain with eigenvalues.

Characteristic polynomial: $(0.9-\lambda)(0.8-\lambda) - 0.02 = \lambda^2 - 1.7\lambda + 0.7 = (\lambda - 1)(\lambda - 0.7)$, so $\lambda = 1$ and $\lambda = 0.7$.

For $\lambda = 1$: $(\mathit P - \mathit I)\vb v = \vb 0$ gives $-0.1v_1 + 0.2v_2 = 0$, i.e. $\vb v_1 = \langle 2, 1\rangle$. For $\lambda = 0.7$: $\vb v_2 = \langle 1, -1\rangle$.

Any starting distribution splits as $\vb x_0 = c_1\langle 2,1\rangle + c_2\langle 1,-1\rangle$, and

$$
\mathit P^k \vb x_0 = c_1\,(1)^k\langle 2,1\rangle + c_2\,(0.7)^k\langle 1,-1\rangle
\;\xrightarrow{k\to\infty}\; c_1\langle 2, 1\rangle.
$$

The $\lambda = 1$ component is the **steady state** — normalized to sum to $1$ (probabilities): $\langle \tfrac23, \tfrac13\rangle$, exactly the numerical limit — and the $0.7^k$ factor is the *rate* of convergence: the "memory" of the initial condition dies by $30\%$ per month. No iteration required: two eigenpairs told us the destination *and* the speed. This is precisely the mathematics of Google's PageRank, whose ranking vector is the $\lambda = 1$ eigenvector of a web-scale transition matrix.
```

Two cautionary specimens complete the picture. The **shear** $\begin{bmatrix}1&1\\0&1\end{bmatrix}$ has characteristic polynomial $(1-\lambda)^2$ — eigenvalue $1$ twice — but $(\mathit A - \mathit I)\vb v = \vb 0$ yields only the single direction $\langle 1, 0\rangle$: one eigen-line where diagonalization needs two independent directions. Repeated eigenvalues *may* fall short of eigenvectors, and such matrices are not diagonalizable (their powers show the tell-tale polynomial-times-geometric growth, the shear's $\mathit S^k = \begin{bmatrix}1&k\\0&1\end{bmatrix}$). And the **rotation** $\mathit R_\theta$ ($0 < \theta < \pi$) turns *every* real direction, so it has no real eigenvectors at all; its characteristic roots are the complex pair $\cos\theta \pm i\sin\theta$, of absolute value $1$ — complex eigenvalues on the unit circle are exactly how "pure oscillation, no growth" announces itself. Both phenomena matter in applications, but the main highway of this course runs through the matrices where nothing goes wrong — and there is a theorem guaranteeing a large, important class of them.

## 20.3 Symmetric matrices: the spectral theorem

```{prf:theorem} Spectral theorem (real symmetric case)
:label: thm-spectral
Every symmetric matrix $\mathit A = \mathit A^{\mathsf T}$ has real eigenvalues and a full set of $n$ eigenvectors that can be chosen **mutually orthogonal** (and unit length). Consequently $\mathit A = \mathit Q\mathit D\mathit Q^{\mathsf T}$ with $\mathit Q$'s columns an orthonormal eigenbasis — the change of basis is a rotation/reflection, and its inverse is just the transpose.
```

{prf:ref}`ex-eigen-computation` displays it in miniature: $\begin{bmatrix}2&1\\1&2\end{bmatrix}$ is symmetric, its eigenvalues $3, 1$ are real, and its eigenvectors $\langle1,1\rangle$, $\langle1,-1\rangle$ are orthogonal (dot product $0$ — check). The ellipse of {numref}`fig-eigen-directions` therefore has *perpendicular* axes, as ellipses should. The theorem is the deep reason data science trusts eigen-methods: the matrices the field cares most about — covariance matrices $\mathit X^{\mathsf T}\mathit X$ (Chapter 17), kernel matrices, graph Laplacians — are symmetric by construction, so their eigenstructure is guaranteed real, orthogonal, and numerically friendly (`np.linalg.eigh`).

## 20.4 Common mistakes

```{admonition} Common Mistakes
:class: warning
**Solving $\det(\mathit A - \lambda\mathit I) = 0$ and stopping.** Eigen*values* are half the answer; each needs its eigen*vector* from $(\mathit A - \lambda\mathit I)\vb v = \vb 0$. Conversely, "the eigenvector" is never unique — any nonzero scalar multiple qualifies; NumPy's normalized columns and your hand answer $\langle 1,1\rangle$ are the same eigenvector.

**Expecting $(\mathit A - \lambda\mathit I)\vb v = \vb 0$ to have a unique solution.** It is *supposed* to be singular — a free variable is the success condition, not an error. If elimination yields only $\vb v = \vb 0$, the $\lambda$ was wrong.

**Skipping the trace/determinant check.** $\sum\lambda_i = \operatorname{tr}\mathit A$ and $\prod\lambda_i = \det\mathit A$ cost seconds and catch sign slips in the characteristic polynomial.

**Assuming every matrix diagonalizes.** Repeated eigenvalues can be short of eigenvectors (the shear); real matrices can have complex eigenvalues (rotations). Symmetric matrices are the safe harbor.

**Eigen-facts applied to sums and products.** Eigenvalues of $\mathit A + \mathit B$ or $\mathit{AB}$ are *not* sums/products of the separate eigenvalues in general (the matrices' eigenvectors differ). What is safe: $\mathit A^k$ has eigenvalues $\lambda^k$ (same eigenvectors), $\mathit A^{-1}$ has $1/\lambda$, and $\mathit A + c\mathit I$ has $\lambda + c$.

**Reading eigenvector *signs* as meaningful.** $\vb v$ and $-\vb v$ are the same eigendirection; software may return either. In PCA, a component "flipping sign" between runs is not a change in the analysis.
```

## 20.5 Now do it in Python

```python
import numpy as np

# --- Example 20.3 ---
A = np.array([[2.0, 1], [1, 2]])
vals, vecs = np.linalg.eig(A)
print(vals)          # [3. 1.]
print(vecs)          # columns: [0.7071, 0.7071], [-0.7071, 0.7071]
# verify the defining equation, column by column:
for lam, v in zip(vals, vecs.T):
    print(np.allclose(A @ v, lam * v))       # True, True
print(np.isclose(vals.sum(), np.trace(A)),   # trace check
      np.isclose(vals.prod(), np.linalg.det(A)))   # det check

# --- Example 20.5: Markov, destination and speed ---
P = np.array([[0.9, 0.2], [0.1, 0.8]])
vals, vecs = np.linalg.eig(P)
steady = vecs[:, np.argmax(vals)]
print(steady / steady.sum())                 # [0.6667 0.3333]

# --- Diagonalization computes powers ---
D = np.diag(vals)
Pm = vecs
print(np.allclose(np.linalg.matrix_power(P, 20),
                  Pm @ np.diag(vals**20) @ np.linalg.inv(Pm)))   # True

# --- Symmetric matrices: use eigh ---
vals_s, vecs_s = np.linalg.eigh(A)           # sorted ascending, orthonormal Q
print(np.allclose(vecs_s @ vecs_s.T, np.eye(2)))                 # True: Q Qᵀ = I
```

`eig` for general matrices (may return complex values — try it on a rotation matrix), `eigh` for symmetric ones (guaranteed real, orthonormal, faster). Note that `eig` normalizes eigenvectors to unit length; your hand-computed $\langle 1, 1\rangle$ appears as $\langle 0.7071, 0.7071\rangle$ — same direction, different representative.

**Visualization and interpretation: PCA in fifteen lines.** Generate correlated data, and let the covariance matrix's eigenvectors find its natural axes:

```python
rng = np.random.default_rng(1)
X = rng.normal(size=(500, 2)) @ np.array([[2.0, 0.8], [0.8, 1.0]])   # correlated cloud
X = X - X.mean(axis=0)
C = X.T @ X / len(X)                 # covariance matrix -- symmetric!
vals, vecs = np.linalg.eigh(C)

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.scatter(*X.T, s=6, alpha=0.4)
for lam, v in zip(vals, vecs.T):
    ax.quiver(0, 0, *(2*np.sqrt(lam)*v), angles="xy",
              scale_units="xy", scale=1, color="tab:red", width=0.012)
ax.set_aspect("equal"); plt.show()
print(vals / vals.sum())             # share of variance along each axis
```

The two red arrows — eigenvectors of the covariance matrix, scaled by $\sqrt\lambda$ — align with the cloud's long and short directions, and `vals/vals.sum()` reports what fraction of the total variance each explains. That *is* principal component analysis: to compress $50$-dimensional data to $2$, keep the two eigenvectors with the largest eigenvalues and project onto them. The spectral theorem guarantees the axes are orthogonal; the eigenvalues rank their importance.

```{admonition} Data Science Connection
:class: tip
Eigenanalysis is the field's X-ray machine. **PCA** (above) is eigenvectors of the covariance matrix — dimensionality reduction, visualization, denoising. **PageRank** is the steady-state eigenvector of a link-transition matrix ({prf:ref}`ex-eigen-markov` at web scale, computed by power iteration: just multiply repeatedly and normalize, since the dominant eigenvalue wins). **Spectral clustering** partitions graphs with the low eigenvectors of the Laplacian. And in optimization, the eigenvalues of the Hessian (Chapter 23's second-derivative matrix) govern gradient descent: the ratio $\lambda_{\max}/\lambda_{\min}$ — the condition number — dictates how fast training converges and why ill-scaled features slow it down.
```

```{admonition} Looking Ahead
:class: seealso
Part IV is complete: vectors, products, matrices, systems, determinants, and now the eigen-decomposition that ties them together. Part V returns to calculus and aims it at many variables — where derivatives become gradient *vectors*, second derivatives become symmetric *matrices* whose eigenvalues classify maxima and minima, and integrals acquire Jacobian determinants. Everything built here rides along.
```

## 20.6 Exercises

### Quick Check

1. Verify that $\langle 1, 2 \rangle$ is an eigenvector of $\begin{bmatrix}4 & 1\\ 2 & 3\end{bmatrix}$ and find its eigenvalue. (One multiplication.)
2. What are the eigenvalues of $\operatorname{diag}(5, -2, 1)$? Of any triangular matrix?
3. A $3\times3$ matrix has eigenvalues $2, 3, 4$. What are its trace and determinant? The eigenvalues of $\mathit A^{-1}$? Of $\mathit A^2$?
4. True or false: if $\vb v$ is an eigenvector of $\mathit A$, so is $-5\vb v$.

````{admonition} Answers to Quick Checks
:class: dropdown
1. $\mathit A\langle1,2\rangle = \langle 6, 8\rangle$… which is *not* a multiple of $\langle 1,2\rangle$ — recheck: $\langle 4+2,\ 2+6\rangle = \langle 6, 8\rangle$. Not an eigenvector? Try $\langle 1, 2\rangle$ against the eigenvalue candidates: the true eigenvectors are $\langle 1, 1\rangle$ ($\lambda = 5$) and $\langle 1, -2\rangle$ ($\lambda = 2$). The check-by-multiplying habit just did its job: the *claim* was false, and one product exposed it.
2. $5, -2, 1$; the diagonal entries — $\det(\mathit A - \lambda\mathit I)$ of a triangular matrix is the product of $(a_{ii} - \lambda)$.
3. Trace $9$, determinant $24$; $\ \tfrac12, \tfrac13, \tfrac14$; $\ 4, 9, 16$.
4. True — any nonzero multiple, same $\lambda$.
````

### Basic Practice

5. For each matrix, find eigenvalues and eigenvectors by hand, run the trace/det checks, and verify one eigenpair by multiplication:
   (a) $\begin{bmatrix}3 & 1\\ 1 & 3\end{bmatrix}$  (b) $\begin{bmatrix}2 & 3\\ 0 & 5\end{bmatrix}$  (c) $\begin{bmatrix}1 & 2\\ 2 & 4\end{bmatrix}$  (d) $\begin{bmatrix}0 & 1\\ -1 & 0\end{bmatrix}$ *(what goes wrong, and what kind of matrix is this?)*
6. Diagonalize matrix 5(a) as $\mathit P\mathit D\mathit P^{-1}$ and use the factorization to compute its $5$th power by hand; confirm with `matrix_power`.
7. For 5(c): one eigenvalue is $0$. Find its eigenvector, connect $\lambda = 0$ to the matrix's determinant and rank, and describe geometrically what the transformation does to that eigendirection.
8. The Fibonacci recursion $\langle F_{k+1}, F_k\rangle = \begin{bmatrix}1&1\\1&0\end{bmatrix}\langle F_k, F_{k-1}\rangle$ iterates a matrix. Find its eigenvalues (the golden ratio $\varphi = \frac{1+\sqrt5}{2}$ and its conjugate) and explain, via §20.2's expansion, why $F_{k+1}/F_k \to \varphi$.

````{admonition} Solution to Exercise 5(a)
:class: dropdown
$(3-\lambda)^2 - 1 = \lambda^2 - 6\lambda + 8 = (\lambda-2)(\lambda-4)$: eigenvalues $2, 4$ (trace $6 = 2+4$ ✓, det $8 = 2\cdot4$ ✓). $\lambda = 4$: $v_1 = v_2$, take $\langle 1,1\rangle$; $\lambda = 2$: $v_2 = -v_1$, take $\langle 1,-1\rangle$. Symmetric matrix — orthogonal eigenvectors, as promised by {prf:ref}`thm-spectral`. Verify: $\mathit A\langle1,1\rangle = \langle4,4\rangle$ ✓.
````

### Intermediate Practice

9. Show that if $\mathit A\vb v = \lambda\vb v$ then $\mathit A^k\vb v = \lambda^k\vb v$ (induction) and $(\mathit A + c\mathit I)\vb v = (\lambda + c)\vb v$; conclude the eigenvalues of $\mathit A^2 - 3\mathit A$ in terms of $\mathit A$'s. *(Polynomials in $\mathit A$ keep $\mathit A$'s eigenvectors.)*
10. A Markov survey matrix $\mathit P = \begin{bmatrix}0.7 & 0.4\\ 0.3 & 0.6\end{bmatrix}$ moves voters between two parties monthly. Find both eigenvalues, the steady-state split, and the number of months until the transient component decays below $1\%$ of its initial size (solve $|\lambda_2|^k < 0.01$ with Chapter 2's logarithms).
11. Prove that eigenvectors with *distinct* eigenvalues are linearly independent, at least for two: if $c_1\vb v_1 + c_2\vb v_2 = \vb 0$ with $\lambda_1 \ne \lambda_2$, apply $\mathit A$ to the equation, then eliminate to force $c_1 = c_2 = 0$.
12. For the symmetric matrix $\mathit C = \begin{bmatrix}5 & 2\\ 2 & 2\end{bmatrix}$ (a covariance matrix): find eigenvalues and orthonormal eigenvectors, write $\mathit C = \mathit Q\mathit D\mathit Q^{\mathsf T}$, and report the fraction of "variance" carried by the dominant direction.
13. Verify the spectral theorem's orthogonality on {prf:ref}`ex-eigen-markov`'s $\mathit P$ — and explain the trap: $\langle 2,1\rangle\cdot\langle1,-1\rangle = 1 \ne 0$. Why does this *not* contradict {prf:ref}`thm-spectral`?

### Conceptual Understanding

14. Explain to a colleague, using {numref}`fig-eigen-directions`, why a generic vector rotates toward the dominant eigendirection under repeated application of $\mathit A$ — and what this has to do with the power-iteration algorithm for computing PageRank.
15. Why must the characteristic polynomial trick — demanding $\det(\mathit A - \lambda\mathit I) = 0$ — produce *singular* systems for the eigenvector step? Connect to Chapter 18's free variables and explain why that is a feature.
16. The spectral theorem gives symmetric matrices orthogonal eigenvectors. Interpreting a covariance matrix's eigenvectors as "directions of variation," explain in one paragraph why orthogonality is exactly what makes PCA components useful as *non-redundant* summaries.

### Python Practice

17. Verify Exercises 5–12 with `eig`/`eigh`. For 8, compute $F_{30}$ three ways: recursion, `matrix_power`, and the diagonalization formula $\mathit P\mathit D^{30}\mathit P^{-1}$, and compare.
18. Implement **power iteration**: `v = A @ v; v /= np.linalg.norm(v)` in a loop, applied to {prf:ref}`ex-eigen-computation`'s matrix from a random start. Print the Rayleigh quotient `v @ A @ v` each step and count iterations to 6-digit agreement with $\lambda = 3$; relate the speed to the ratio $|\lambda_2/\lambda_1| = 1/3$.

### Visualization Practice

19. Recreate the PCA scatter of §20.5 for three clouds with increasing correlation (off-diagonal $0, 0.6, 0.95$), plotting the scaled eigenvectors on each. Describe how the eigenvalue *ratio* changes and what it says about compressibility of each cloud to one dimension.
20. For $\mathit A = \begin{bmatrix}2&1\\1&2\end{bmatrix}$, take 12 unit vectors around the circle and draw each $\vb v$ and $\mathit A\vb v$ as paired arrows. Annotate the two positions where the pair is parallel. This is {numref}`fig-eigen-directions` rebuilt from raw arrows — the eigenvector definition made kinetic.

### Challenge

21. **Closed-form Fibonacci.** Diagonalize $\begin{bmatrix}1&1\\1&0\end{bmatrix}$ exactly (SymPy helps) and derive Binet's formula $F_k = \frac{\varphi^k - \psi^k}{\sqrt5}$ with $\psi = \frac{1-\sqrt5}{2}$. Verify for $k = 10$ ($F_{10} = 55$), and explain why rounding $\varphi^k/\sqrt5$ to the nearest integer works for all $k \ge 1$ (consider $|\psi| < 1$ and Chapter 12's geometric decay).
22. **Second differences and vibration.** The symmetric matrix $\mathit L = \begin{bmatrix}2&-1&0\\-1&2&-1\\0&-1&2\end{bmatrix}$ (a discrete Laplacian) has eigenvalues $2 - \sqrt2,\ 2,\ 2+\sqrt2$ with eigenvectors that sample sine waves: $\vb v_j$ has components $\sin\frac{jk\pi}{4}$. Verify both claims numerically, plot the three eigenvectors as functions of index, and connect what you see to Chapter 14: the eigenvectors of this matrix *are* a discrete Fourier basis, which is no accident — Fourier analysis is the eigenanalysis of translation-symmetric systems.

### Cumulative Review

23. *(Ch. 19)* Similar matrices share eigenvalues: using $\det(\mathit P^{-1}\mathit A\mathit P - \lambda\mathit I) = \det(\mathit P^{-1}(\mathit A - \lambda\mathit I)\mathit P)$ and Chapter 19's Exercise 11, prove that $\mathit P^{-1}\mathit A\mathit P$ has the same characteristic polynomial as $\mathit A$.
24. *(Ch. 12–13)* The expansion $\mathit A^k\vb x_0 = \sum c_i\lambda_i^k\vb v_i$ is a linear combination of geometric sequences. Using Chapter 12's convergence criteria, state precisely the condition on the eigenvalues for $\mathit A^k\vb x_0$ to (a) converge to $\vb 0$ for every $\vb x_0$, (b) remain bounded, (c) converge to a nonzero limit for generic $\vb x_0$.

## 20.7 Summary

An eigenvector is a direction a matrix does not turn — $\mathit A\vb v = \lambda\vb v$ — found by a two-step algorithm that unites the whole Part: eigenvalues are the roots of the characteristic polynomial $\det(\mathit A - \lambda\mathit I) = 0$ (a determinant), eigenvectors are the free-variable solutions of the resulting singular systems (elimination), with trace $= \sum\lambda_i$ and $\det = \prod\lambda_i$ as instant checks. With $n$ independent eigenvectors, $\mathit A = \mathit P\mathit D\mathit P^{-1}$: the transformation is a diagonal stretch in eigen-coordinates, powers become $\mathit P\mathit D^k\mathit P^{-1}$, and long-run behavior reads off the eigenvalue magnitudes — steady states live at $\lambda = 1$ (Markov chains, PageRank), transients decay at the second eigenvalue's rate, shears warn that repeated eigenvalues may not diagonalize, rotations that real matrices may need complex eigenvalues. Symmetric matrices — covariance matrices above all — are the guaranteed case: real eigenvalues, orthonormal eigenvectors ($\mathit A = \mathit Q\mathit D\mathit Q^{\mathsf T}$), computed by `eigh`, and directly interpretable as PCA's principal axes ranked by variance. The matrix's skeleton, extracted; Part V now sends calculus into $\mathbb{R}^n$ to meet it.

*Parallel reading:* Strang {cite}`strang_linalg`, Chapter 6; Goodfellow et al., §2.7 {cite}`goodfellow_linalg`.
