# Chapter 19 · Determinants

Chapter 18 decided whether a matrix is invertible by running the whole elimination algorithm. This chapter compresses that verdict — and much more — into a single number, the **determinant**. Geometrically it answers Chapter 17's open question: *by what factor does the transformation scale area (or volume)?* Algebraically it answers Chapter 18's: *is the machine reversible?* The two answers coincide because they must: a transformation that flattens volume to zero has destroyed information no inverse can recover.

## 19.1 The 2×2 case: signed area

```{prf:definition} Determinant (2×2)
:label: def-det-2x2
$$
\det\begin{bmatrix}a & b\\ c & d\end{bmatrix}
= \begin{vmatrix}a & b\\ c & d\end{vmatrix}
= ad - bc.
$$
```

The quantity already appeared twice — as the denominator of the $2\times2$ inverse (Chapter 18) and inside the cross product (Chapter 16) — and its geometric meaning is the chapter's anchor:

```{prf:theorem} Determinant as area scaling
:label: thm-det-area
$|\det \mathit A|$ is the area of the parallelogram spanned by the columns of $\mathit A$ — equivalently, the factor by which the transformation $\vb x \mapsto \mathit A\vb x$ scales *every* area. The sign records orientation: positive when the columns keep the counterclockwise order of $\vb e_1, \vb e_2$, negative when the transformation flips the plane over.
```

```{figure} figures/ch19-determinant-area.png
:name: fig-determinant-area
:alt: The gray unit square and, overlaid, the blue parallelogram spanned by the vectors three one and one two, labeled with area equal to the determinant, five.

The matrix $\mathit A = \begin{bmatrix}3 & 1\\ 1 & 2\end{bmatrix}$ carries the unit square (area $1$) to the parallelogram spanned by its columns $\langle3,1\rangle$ and $\langle1,2\rangle$ — area $\det = 6 - 1 = 5$. Every region's area, not just the square's, is multiplied by $5$, because every region is (in the limit) a union of tiny squares that each scale the same way.
```

The "every area" claim is what makes the determinant a property of the *transformation*, not of one parallelogram: any region tiles by small squares, each square maps to a small copy of the fundamental parallelogram, so all areas scale by the same $|\det|$. And the degenerate case is the punchline: $\det = 0$ means the columns are parallel (or one is $\vb 0$) — the parallelogram collapses to a segment, the transformation squashes the plane onto a line, distinct inputs collide, and no inverse can exist. *Zero determinant $\iff$ singular*, now visible rather than merely computable.

```{prf:example} Area, orientation, singularity
:label: ex-det-2x2
Compute and interpret: (a) $\begin{vmatrix}3 & 1\\ 1 & 2\end{vmatrix}$, (b) $\begin{vmatrix}1 & 2\\ 3 & -1\end{vmatrix}$, (c) $\begin{vmatrix}2 & 4\\ 3 & 6\end{vmatrix}$.

(a) $6 - 1 = 5$: areas quintuple, orientation preserved ({numref}`fig-determinant-area`). (b) $-1 - 6 = -7$: areas scale by $7$ and the plane is flipped (this is Chapter 18's system matrix; its invertibility, used there, is certified here by $-7 \ne 0$). (c) $12 - 12 = 0$: the second column is twice the first — collapse, singular, no inverse; and the system $\mathit A\vb x = \vb b$ with this matrix has no solution or infinitely many, never one.
```

## 19.2 Higher dimensions: cofactor expansion

For $3\times3$ matrices the determinant measures *volume* scaling of the parallelepiped spanned by the columns — precisely the scalar triple product $\vb a_1\cdot(\vb a_2\times\vb a_3)$ of Chapter 16, which is why the cross product's "determinant mnemonic" was no coincidence. Computationally, the standard recursive recipe is **cofactor expansion**: along any row (or column), each entry multiplies the determinant of the submatrix obtained by deleting its row and column (its **minor**), with signs alternating in a checkerboard $\begin{smallmatrix}+&-&+\\ -&+&-\\ +&-&+\end{smallmatrix}$:

$$
\det \mathit A = a_{11}\begin{vmatrix}a_{22}&a_{23}\\ a_{32}&a_{33}\end{vmatrix}
- a_{12}\begin{vmatrix}a_{21}&a_{23}\\ a_{31}&a_{33}\end{vmatrix}
+ a_{13}\begin{vmatrix}a_{21}&a_{22}\\ a_{31}&a_{32}\end{vmatrix}
\qquad\text{(expansion along row 1).}
$$

```{prf:example} A 3×3 determinant, two ways
:label: ex-det-3x3
Compute $\det \mathit A$ for $\mathit A = \begin{bmatrix}1 & 1 & 1\\ 2 & -1 & 1\\ 1 & 2 & 3\end{bmatrix}$ — the system matrix of Chapter 18's {prf:ref}`ex-gauss-jordan`.

**Cofactors along row 1:**

$$
\det\mathit A = 1\begin{vmatrix}-1&1\\2&3\end{vmatrix} - 1\begin{vmatrix}2&1\\1&3\end{vmatrix} + 1\begin{vmatrix}2&-1\\1&2\end{vmatrix}
= 1(-5) - 1(5) + 1(5) = -5.
$$

**Via elimination:** Chapter 18's reduction of this very matrix used *no row swaps* and reached pivots $1, -3, \tfrac53$. For any elimination by row-replacement operations only, the determinant is the **product of the pivots** (times $-1$ per row swap, if any):

$$
\det\mathit A = 1\cdot(-3)\cdot\tfrac53 = -5. \checkmark
$$

Two unrelated-looking computations, one answer — and the second scales: cofactor expansion costs on the order of $n!$ operations, elimination about $n^3/3$. For $n = 20$ that is the difference between $2\times10^{18}$ and $\sim2700$; libraries compute determinants by elimination, always. Cofactors remain valuable for theory, for small matrices, and for matrices with many zeros (expand along the emptiest row).
```

Expansion along a zero-rich row is worth one illustration: a **triangular** matrix (all zeros below — or above — the diagonal) expands trivially down its first column at every level, giving

$$
\det(\text{triangular}) = \text{product of the diagonal entries}
$$

— which is *why* the pivot-product rule works: elimination's row-replacement steps do not change the determinant (a property below), and they end at a triangular matrix.

## 19.3 The determinant's laws

The properties that make determinants usable, all consistent with (and provable from) the volume interpretation:

1. $\det \mathit I = 1$ — the identity scales nothing.
2. Swapping two rows flips the sign — orientation reverses.
3. Multiplying one row by $c$ multiplies the determinant by $c$ — stretch one edge of the box.
   Consequently $\det(c\mathit A) = c^n\det\mathit A$ for $n\times n$ matrices ($n$ edges stretched), *not* $c\det\mathit A$.
4. Adding a multiple of one row to another **leaves the determinant unchanged** — shearing a box preserves volume (base and height unchanged). This is the license behind the pivot method.
5. $\det \mathit A = 0$ exactly when $\mathit A$ is singular (rows/columns dependent; the box is flat).
6. **Product rule:** $\det(\mathit{AB}) = (\det\mathit A)(\det\mathit B)$ — composed transformations multiply their scale factors. Immediate corollary: $\det(\mathit A^{-1}) = \dfrac{1}{\det\mathit A}$, since the round trip $\mathit A^{-1}\mathit A = \mathit I$ must scale by $1$.
7. $\det(\mathit A^{\mathsf T}) = \det\mathit A$ — every row statement above is also a column statement.

Conspicuously absent: any rule for $\det(\mathit A + \mathit B)$. There is none — determinants respect multiplication, not addition, and assuming otherwise is the subject's classic trap.

```{prf:example} Reasoning by the laws
:label: ex-det-laws
Given $3\times3$ matrices with $\det\mathit A = -5$ and $\det\mathit B = 2$, evaluate what can be evaluated: $\det(\mathit{AB})$, $\det(\mathit A^2\mathit B^{\mathsf T})$, $\det(2\mathit A)$, $\det(\mathit A^{-1}\mathit B\mathit A)$, and $\det(\mathit A + \mathit B)$.

By the product rule and its friends: $\det(\mathit{AB}) = -10$; $\ \det(\mathit A^2\mathit B^{\mathsf T}) = (-5)^2\cdot 2 = 50$; $\ \det(2\mathit A) = 2^3(-5) = -40$ (law 3, three rows); $\ \det(\mathit A^{-1}\mathit B\mathit A) = \frac{1}{-5}\cdot 2\cdot(-5) = 2$ — conjugation preserves determinants, a fact Chapter 20 will lean on. And $\det(\mathit A + \mathit B)$: **cannot be determined** from the given data; no law applies.
```

```{prf:example} A singularity threshold
:label: ex-det-threshold
For which $k$ is $\mathit M = \begin{bmatrix}1 & 2 & 1\\ 0 & k & 3\\ 2 & 4 & k\end{bmatrix}$ singular?

Expand along the first column (two entries, one of them zero):

$$
\det\mathit M = 1\begin{vmatrix}k & 3\\ 4 & k\end{vmatrix} - 0 + 2\begin{vmatrix}2 & 1\\ k & 3\end{vmatrix}
= (k^2 - 12) + 2(6 - k) = k^2 - 2k.
$$

Singular exactly when $k^2 - 2k = k(k-2) = 0$: at $k = 0$ and $k = 2$. For every other $k$, systems with this matrix have unique solutions. One polynomial in $k$ replaced infinitely many elimination runs — the determinant as an *invertibility function* of parameters, the exact move Chapter 20 will make with $\det(\mathit A - \lambda\mathit I)$.
```

For completeness, **Cramer's rule** expresses each unknown of $\mathit A\vb x = \vb b$ (when $\det\mathit A \ne 0$) as a ratio of determinants: $x_i = \det(\mathit A_i)/\det(\mathit A)$, where $\mathit A_i$ is $\mathit A$ with column $i$ replaced by $\vb b$. It is elegant, occasionally handy for $2\times2$ work and symbolic formulas, and computationally hopeless beyond that — elimination remains the algorithm.

## 19.4 Common mistakes

```{admonition} Common Mistakes
:class: warning
**$\det(\mathit A + \mathit B) = \det\mathit A + \det\mathit B$.** False, and not fixable; determinants are multiplicative, not additive. ($\det$ of a sum has no formula in terms of the summands' determinants.)

**$\det(c\mathit A) = c\det\mathit A$.** The scalar exits once *per row*: $c^n\det\mathit A$. Doubling a $3\times3$ matrix multiplies volumes by $8$.

**Checkerboard sign slips.** The cofactor sign of entry $(i,j)$ is $(-1)^{i+j}$ — expansion along row 2 *starts with a minus*. Write the sign pattern in the margin before expanding.

**Row operations bookkeeping.** Replacement (law 4) is free; swaps flip the sign; scalings multiply. Determinant-via-elimination must track the last two — forgetting a swap negates the answer.

**"$\det = $ small" read as "nearly singular."** Scale-dependent: $\det(0.1\,\mathit I_{10}) = 10^{-10}$ for a perfectly well-behaved matrix. Near-singularity is measured by conditioning (Chapter 18), not by the raw determinant's size; only *exactly* zero (or zero-up-to-roundoff relative to the matrix's scale) means singular.

**Non-square determinants.** Undefined. For rectangular data matrices the analogous quantities come from $\mathit X^{\mathsf T}\mathit X$ or the singular values — not from $\det\mathit X$.
```

## 19.5 Now do it in Python

```python
import numpy as np
import sympy as sp

# --- Examples 19.3-19.4 ---
A = np.array([[3.0, 1], [1, 2]])
print(np.linalg.det(A))                      # 5.000000000000001
A3 = np.array([[1.0, 1, 1], [2, -1, 1], [1, 2, 3]])
print(np.linalg.det(A3))                     # -5.000000000000002

# --- The laws, checked on random matrices ---
rng = np.random.default_rng(0)
A, B = rng.normal(size=(4, 4)), rng.normal(size=(4, 4))
print(np.allclose(np.linalg.det(A @ B),
                  np.linalg.det(A) * np.linalg.det(B)))    # True
print(np.allclose(np.linalg.det(A.T), np.linalg.det(A)))   # True
print(np.allclose(np.linalg.det(2*A),
                  2**4 * np.linalg.det(A)))                # True: c^n
print(np.isclose(np.linalg.det(A + B),
                 np.linalg.det(A) + np.linalg.det(B)))     # False: no sum law

# --- Example 19.6 symbolically ---
k = sp.symbols('k')
M = sp.Matrix([[1, 2, 1], [0, k, 3], [2, 4, k]])
print(sp.factor(M.det()))                    # k*(k - 2)
```

Note the floating fuzz on the very first line: `5.000000000000001`, because NumPy computes determinants by elimination in floating point. SymPy's `M.det()` is exact and shows its algebra; NumPy's is fast and approximate — the by-now-familiar division of labor. Random-matrix property checks, as above, are a cheap and surprisingly strong habit: one seed, four laws, four verdicts.

**Visualization and interpretation.** Reuse Chapter 17's unit-square experiment for a *family* of matrices $\mathit A_t = \begin{bmatrix}1 & t\\ t & 1\end{bmatrix}$ as $t$ runs from $0$ to $1.4$: plot the image parallelogram and title each frame with $\det = 1 - t^2$. The parallelogram thins as $t \to 1$, degenerates to a segment exactly at $t = 1$ ($\det = 0$: the columns coincide), and *flips orientation* beyond ($\det < 0$ — watch the vertex order reverse). Determinant-as-volume, determinant-zero-as-collapse, and sign-as-orientation, all in one animation you can write in ten lines.

```{admonition} Data Science Connection
:class: tip
Determinants price *volume change*, and that is precisely what multivariable probability needs. The change-of-variables formula for densities — Chapter 8's $|dx/dy|$ factor, grown up — uses $|\det \mathit J|$ of the Jacobian matrix (Chapter 22), and normalizing-flow models train by maximizing log-likelihoods containing exactly a $\log|\det\mathit J|$ term. The multivariate normal density carries $\det\mathit\Sigma$ of the covariance matrix (the "generalized variance": the volume of the data's uncertainty ellipsoid), and its log-determinant appears in every Gaussian log-likelihood, Kalman filter, and Bayesian model-evidence computation. Practical footnote: those formulas compute `slogdet` — sign and log of the determinant — precisely because raw determinants of large matrices over- or underflow (law 3 at scale).
```

```{admonition} Looking Ahead
:class: seealso
The determinant's finest hour is next: the eigenvalue equation $\mathit A\vb v = \lambda\vb v$ rearranges to $(\mathit A - \lambda\mathit I)\vb v = \vb 0$, which has nonzero solutions exactly when $\det(\mathit A - \lambda\mathit I) = 0$ — {prf:ref}`ex-det-threshold`'s parameter trick, upgraded into the **characteristic polynomial** whose roots are the eigenvalues.
```

## 19.6 Exercises

### Quick Check

1. Compute $\begin{vmatrix}4 & 2\\ 7 & 5\end{vmatrix}$ and the area of the parallelogram spanned by $\langle4,7\rangle$ and $\langle2,5\rangle$.
2. $\det\mathit A = 3$ for a $3\times3$ matrix. What are $\det(\mathit A^{-1})$, $\det(\mathit A^{\mathsf T})$, $\det(-\mathit A)$?
3. Without expanding, evaluate $\begin{vmatrix}2 & 5 & 1\\ 0 & 3 & 8\\ 0 & 0 & 4\end{vmatrix}$.
4. True or false: if two rows of a matrix are equal, its determinant is zero.

````{admonition} Answers to Quick Checks
:class: dropdown
1. $20 - 14 = 6$; the area is $|6| = 6$.
2. $\tfrac13$; $\ 3$; $\ (-1)^3\cdot 3 = -3$.
3. Triangular: $2\cdot3\cdot4 = 24$.
4. True — swapping the equal rows must flip the sign yet changes nothing, so $\det = -\det = 0$. (Geometrically: two identical edges, flat box.)
````

### Basic Practice

5. Compute by cofactor expansion, choosing the easiest row or column:
   (a) $\begin{vmatrix}2 & 0 & 1\\ 3 & 1 & 2\\ -1 & 0 & 4\end{vmatrix}$  (b) $\begin{vmatrix}1 & 2 & 3\\ 4 & 5 & 6\\ 7 & 8 & 9\end{vmatrix}$  (c) $\begin{vmatrix}1 & 0 & 2\\ 0 & 3 & 0\\ 4 & 0 & 5\end{vmatrix}$
6. Recompute 5(a) by elimination (track any swaps), confirming the cofactor answer.
7. Find all $t$ making $\begin{bmatrix}1 & t\\ t & 4\end{bmatrix}$ singular, and describe geometrically what happens to its column parallelogram at those values.
8. The triangle with vertices $(0,0)$, $(4,1)$, $(2,3)$ has area $\tfrac12\left|\det\begin{bmatrix}4 & 2\\ 1 & 3\end{bmatrix}\right|$. Compute it, and explain the formula via {prf:ref}`thm-det-area` and Chapter 16's half-parallelogram rule.

````{admonition} Solution to Exercise 5(b)
:class: dropdown
Expansion (or the shortcut of noticing row 3 $-$ row 2 $=$ row 2 $-$ row 1 $= \langle 3,3,3\rangle$): rows are dependent, so the determinant is $0$ — this famous matrix is singular. Cofactors confirm: $1(45-48) - 2(36-42) + 3(32-35) = -3 + 12 - 9 = 0$.
````

### Intermediate Practice

9. Verify law 4 concretely: for $\mathit A = \begin{bmatrix}3&1\\1&2\end{bmatrix}$, replace $R_2 \leftarrow R_2 - \tfrac13R_1$ and recompute the determinant; then explain via {numref}`fig-determinant-area` why shearing the parallelogram's top edge parallel to its base cannot change area.
10. Using only the laws (no expansion), determine $\det\mathit B$ where $\mathit B$ is obtained from a matrix with $\det\mathit A = 6$ by: swapping rows 1 and 3, then doubling row 2, then adding $5\,R_1$ to $R_2$.
11. Prove from the product rule that similar matrices have equal determinants: if $\mathit B = \mathit P^{-1}\mathit A\mathit P$ then $\det \mathit B = \det\mathit A$. *(Chapter 20 will say: eigen-structure survives change of basis.)*
12. Compute the volume of the parallelepiped spanned by $\langle 1,0,2\rangle$, $\langle 0,3,0\rangle$, $\langle 4,0,5\rangle$ twice: as $|\vb u\cdot(\vb v\times\vb w)|$ (Chapter 16) and as a $3\times3$ determinant (Exercise 5(c)). Confirm agreement and state the general identity.
13. Solve Chapter 18's $2\times2$ system ($x + 2y = 5$, $3x - y = 1$) by Cramer's rule, and count the multiplications used versus elimination's.

### Conceptual Understanding

14. Explain in one paragraph why "$\det\mathit A = 0$" and "$\mathit A\vb x = \vb b$ fails to have a unique solution" must be the same condition, connecting the flat-box picture to the column picture of Chapter 18.
15. Law 6 says scale factors multiply under composition. Use it to explain — without computing anything — why no product of rotation matrices can ever equal a matrix with determinant $2$.
16. A colleague reports $\det(\mathit X^{\mathsf T}\mathit X) = 10^{-15}$ for their $8$-feature design matrix and concludes "singular — features are collinear." Give one reason the conclusion may be right and one reason the evidence is insufficient (consider units/scaling), and name the better diagnostic.

### Python Practice

17. Verify Exercises 5–12 numerically (and 7, {prf:ref}`ex-det-threshold` symbolically). For 11, test on random $4\times4$ $\mathit A$ and $\mathit P$.
18. Estimate the probability that a random $3\times3$ matrix with entries drawn uniformly from $\{-1, 0, 1\}$ is singular, by sampling $200\,000$ matrices and counting $\det = 0$ (exact integer arithmetic: build with `rng.integers` and round the determinant). Report your estimate. *(Exactly-singular matrices are rare but not negligible on this discrete grid — contrast with continuous random entries, where singularity has probability zero.)*

### Visualization Practice

19. Implement §19.5's animation-as-small-multiples: images of the unit square under $\mathit A_t = \begin{bmatrix}1&t\\ t&1\end{bmatrix}$ for $t \in \{0, 0.5, 0.9, 1.0, 1.1, 1.4\}$, each panel titled with $\det = 1 - t^2$, with vertices labeled in order so the orientation flip at $t > 1$ is visible.
20. For $100$ random $2\times2$ matrices with standard-normal entries, scatter-plot $|\det|$ against the numerically computed area of the image of the unit square (via the shoelace formula on the transformed corners). The points should fall on the line $y = x$; annotate the two or three near-zero-determinant matrices and describe their parallelograms.

### Challenge

21. Prove the $2\times2$ product rule $\det(\mathit{AB}) = \det\mathit A\det\mathit B$ by direct expansion of both sides — four entries each, eight products, watch the cross terms cancel. Then give the one-sentence geometric proof that works in all dimensions.
22. **Vandermonde.** Show by row reduction (subtract suitable multiples working upward) that $\det\begin{bmatrix}1 & a & a^2\\ 1 & b & b^2\\ 1 & c & c^2\end{bmatrix} = (b-a)(c-a)(c-b)$, and conclude the polynomial-interpolation system of Chapter 18, Exercise 10 has a unique solution exactly when the interpolation points are distinct — the theorem that makes curve fitting well-posed.

### Cumulative Review

23. *(Ch. 16)* The cross product mnemonic wrote $\vb u\times\vb v$ as a determinant with $\vb i, \vb j, \vb k$ in the top row. Expand that determinant by cofactors along the top row and confirm it reproduces {prf:ref}`def-cross` exactly — the mnemonic is cofactor expansion.
24. *(Ch. 9)* The linear map $\mathit A = \operatorname{diag}(3, 2)$ carries the unit disk to an ellipse. Using determinant-as-area-scaling, find the ellipse's area — then confirm by the $\pi ab$ formula. *(In Chapter 25 the same scaling factor reappears as the Jacobian of a coordinate change.)*

## 19.7 Summary

The determinant assigns each square matrix one number with two synchronized meanings: the signed volume-scaling factor of its transformation (columns span the fundamental parallelogram/parallelepiped; sign tracks orientation) and the verdict on invertibility ($\det = 0 \iff$ collapse $\iff$ singular). Computation: $ad - bc$ in 2×2; cofactor expansion with checkerboard signs along any row or column (best where zeros live) for small or symbolic cases; product-of-pivots via elimination — replacements free, swaps flip sign, scalings multiply — for everything else, since cofactors cost $n!$ against elimination's $n^3$. The laws: $\det\mathit I = 1$, $\det(\mathit{AB}) = \det\mathit A\det\mathit B$ (hence $\det\mathit A^{-1} = 1/\det\mathit A$ and similarity-invariance), $\det\mathit A^{\mathsf T} = \det\mathit A$, $\det(c\mathit A) = c^n\det\mathit A$, triangular = diagonal product — and *no* law for sums. Applications flow from the volume reading (Jacobians, Gaussian likelihoods via `slogdet`, generalized variance) and from the singularity reading, whose parameter form $\det(\mathit A - \lambda\mathit I) = 0$ is the doorway to eigenvalues, next.

*Parallel reading:* Strang {cite}`strang_linalg`, Chapter 5; OpenStax *Calculus Volume 3*, §2.4 (the 3×3 case via triple products) {cite}`openstax_calc3`.
