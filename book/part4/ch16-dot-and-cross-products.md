# Chapter 16 · The Dot Product and the Cross Product

Chapter 15 could add vectors and scale them, but could not answer the most useful geometric questions: *what is the angle between two vectors? Are they perpendicular? How much of one lies along another?* The **dot product** answers all three with one formula, and does so in any dimension — making it, without much competition, the single most heavily used operation in machine learning. Its sibling the **cross product**, special to three dimensions, manufactures perpendicular vectors and computes areas, and will hand Chapter 19 the geometric meaning of determinants.

## 16.1 The dot product

```{prf:definition} Dot product
:label: def-dot
The **dot product** of $\vb u, \vb v \in \mathbb{R}^n$ is the scalar

$$
\vb u \cdot \vb v = u_1v_1 + u_2v_2 + \cdots + u_nv_n = \sum_{i=1}^n u_iv_i.
$$
```

Multiply matching components, add — the output is a *number*, not a vector. The algebraic properties are immediate from the formula: commutativity $\vb u\cdot\vb v = \vb v\cdot\vb u$, distributivity $\vb u\cdot(\vb v + \vb w) = \vb u\cdot\vb v + \vb u\cdot\vb w$, scalars slide freely $(c\vb u)\cdot\vb v = c(\vb u\cdot\vb v)$, and — the bridge to Chapter 15 —

$$
\vb v \cdot \vb v = v_1^2 + \cdots + v_n^2 = \|\vb v\|^2:
$$

*a vector dotted with itself is its squared length.* The dot product thus contains the norm; the surprise is that it also contains the angle.

```{prf:theorem} Geometric form of the dot product
:label: thm-dot-angle
For nonzero $\vb u, \vb v$ with angle $\theta \in [0, \pi]$ between them (tails together),

$$
\vb u \cdot \vb v = \|\vb u\|\,\|\vb v\|\cos\theta,
\qquad\text{equivalently}\qquad
\cos\theta = \frac{\vb u\cdot\vb v}{\|\vb u\|\,\|\vb v\|}.
$$
```

**Where it comes from.** The triangle with sides $\vb u$, $\vb v$, and $\vb u - \vb v$ obeys the law of cosines: $\|\vb u - \vb v\|^2 = \|\vb u\|^2 + \|\vb v\|^2 - 2\|\vb u\|\|\vb v\|\cos\theta$. Expand the left side with the algebra above — $\|\vb u - \vb v\|^2 = (\vb u - \vb v)\cdot(\vb u - \vb v) = \|\vb u\|^2 - 2\,\vb u\cdot\vb v + \|\vb v\|^2$ — and compare: the cross term delivers the theorem. (Exercise 21 of Chapter 15 asked you to keep the cross terms in view; this is why.)

The formula is best read as a **sign dictionary** for alignment:

$$
\vb u\cdot\vb v \;>\; 0 \iff \theta < 90° \text{ (broadly agreeing)},
\qquad
\vb u\cdot\vb v = 0 \iff \theta = 90°,
\qquad
\vb u\cdot\vb v < 0 \iff \theta > 90° \text{ (broadly opposing)}.
$$

The middle case earns a definition: $\vb u$ and $\vb v$ are **orthogonal** when $\vb u\cdot\vb v = 0$ — the algebraic name for perpendicular, and a *checkable* condition in any dimension: no protractor, one sum.

```{prf:example} Angle between vectors
:label: ex-dot-angle
Find the angle between $\vb a = \langle 4, 1 \rangle$ and $\vb b = \langle 2, 3\rangle$.

$$
\vb a\cdot\vb b = 8 + 3 = 11, \qquad \|\vb a\| = \sqrt{17}, \qquad \|\vb b\| = \sqrt{13},
$$

$$
\cos\theta = \frac{11}{\sqrt{17}\sqrt{13}} = \frac{11}{\sqrt{221}} \approx 0.7399
\quad\Longrightarrow\quad
\theta \approx 42.3°.
$$

(In radians, $\theta \approx 0.738$ — and note the check $\cos\theta \le 1$ passed comfortably. A computed "cosine" outside $[-1,1]$ means an arithmetic error, always.)
```

```{prf:example} Testing orthogonality in $\mathbb{R}^4$
:label: ex-dot-orthogonal
Are $\vb u = \langle 1, 2, -1, 3\rangle$ and $\vb v = \langle 2, 1, 4, 0 \rangle$ orthogonal? Is either orthogonal to $\vb w = \langle 3, -2, -1, 0\rangle$?

$\vb u\cdot\vb v = 2 + 2 - 4 + 0 = 0$: orthogonal — a right angle in four-dimensional space, certified by arithmetic. And $\vb v\cdot\vb w = 6 - 2 - 4 + 0 = 0$: also orthogonal; but $\vb u\cdot\vb w = 3 - 4 + 1 + 0 = 0$ as well. All three are mutually orthogonal — the beginnings of an orthogonal basis for a subspace of $\mathbb{R}^4$, an object Chapter 20's spectral theorem will make central.
```

## 16.2 Projection: how much of one vector lies along another

Decomposing a vector into a part *along* a chosen direction and a part *perpendicular* to it is the dot product's most valuable service.

```{prf:definition} Projection
:label: def-projection
The **(vector) projection of $\vb b$ onto $\vb a \ne \vb 0$** is

$$
\operatorname{proj}_{\vb a}\vb b \;=\; \frac{\vb a\cdot\vb b}{\vb a\cdot\vb a}\,\vb a
\;=\; \underbrace{\bigl(\hat{\vb a}\cdot\vb b\bigr)}_{\text{scalar component}}\,\hat{\vb a},
$$

the shadow $\vb b$ casts on the line through $\vb a$. The scalar $\hat{\vb a}\cdot\vb b = \|\vb b\|\cos\theta$ is the **scalar projection** (signed length of the shadow), and the remainder $\vb b - \operatorname{proj}_{\vb a}\vb b$ is orthogonal to $\vb a$.
```

The formula is forced by two requirements: the projection must be a multiple $c\,\vb a$, and the leftover $\vb b - c\vb a$ must be orthogonal to $\vb a$. Imposing $(\vb b - c\vb a)\cdot\vb a = 0$ gives $c = \frac{\vb a\cdot\vb b}{\vb a\cdot\vb a}$ — one line, and worth reproducing yourself, because *this same one line* is the seed of least-squares regression.

```{figure} figures/ch16-dot-projection.png
:name: fig-dot-projection
:alt: Vectors a and b from the origin; a thick arrow along a marks the projection of b onto a, and a dotted segment drops perpendicularly from the tip of b to the tip of the projection.

Projection of $\vb b = \langle 2,3\rangle$ onto $\vb a = \langle 4,1\rangle$: the shadow $\operatorname{proj}_{\vb a}\vb b = \frac{11}{17}\langle 4, 1\rangle \approx \langle 2.59, 0.65\rangle$ lies along $\vb a$, and the dotted residual from it to $\vb b$ meets $\vb a$ at a right angle — the defining property.
```

```{prf:example} Computing a decomposition
:label: ex-projection
Decompose $\vb b = \langle 2, 3 \rangle$ into components parallel and perpendicular to $\vb a = \langle 4, 1\rangle$.

From {prf:ref}`ex-dot-angle`, $\vb a\cdot\vb b = 11$ and $\vb a\cdot\vb a = 17$:

$$
\operatorname{proj}_{\vb a}\vb b = \frac{11}{17}\langle 4, 1\rangle = \bigl\langle \tfrac{44}{17}, \tfrac{11}{17}\bigr\rangle \approx \langle 2.588,\ 0.647\rangle,
$$

$$
\vb b_\perp = \vb b - \operatorname{proj}_{\vb a}\vb b = \bigl\langle 2 - \tfrac{44}{17},\ 3 - \tfrac{11}{17}\bigr\rangle = \bigl\langle -\tfrac{10}{17}, \tfrac{40}{17}\bigr\rangle.
$$

**Check:** $\vb a \cdot \vb b_\perp = 4\cdot(-\tfrac{10}{17}) + 1\cdot\tfrac{40}{17} = 0$ ✓, and the two parts sum back to $\vb b$ ✓. Work in physics ($W = \vb F\cdot\vb d$: only the force component along the displacement does work), error decomposition in statistics, and Chapter 23's directional derivatives all run on this decomposition.
```

**Cosine similarity.** Applied to data, the angle formula gets a name of its own: $\operatorname{sim}(\vb u, \vb v) = \frac{\vb u\cdot\vb v}{\|\vb u\|\|\vb v\|} \in [-1, 1]$ — the cosine of the angle between two feature vectors, insensitive to their magnitudes. It resolves {prf:ref}`ex-data-vector`'s puzzle from the last chapter cleanly: users A $= \langle 6,2,2\rangle$ and B $= \langle 3,1,1\rangle$ have cosine similarity exactly $1$ (same direction — identical tastes at different intensities), and the search-engine question "which document is most like this query?" is, in practice, "which document vector has the largest cosine with the query vector?"

## 16.3 The cross product

In $\mathbb{R}^3$ — and only there — a second product exists, producing a *vector*.

```{prf:definition} Cross product
:label: def-cross
For $\vb u, \vb v \in \mathbb{R}^3$,

$$
\vb u \times \vb v =
\bigl\langle\, u_2v_3 - u_3v_2,\;\; u_3v_1 - u_1v_3,\;\; u_1v_2 - u_2v_1 \,\bigr\rangle,
$$

conveniently remembered as a symbolic determinant (Chapter 19 makes the notation honest):

$$
\vb u\times\vb v = \begin{vmatrix}\vb i & \vb j & \vb k\\ u_1 & u_2 & u_3\\ v_1 & v_2 & v_3\end{vmatrix}.
$$
```

Its geometry, verifiable from the formula (Exercises 13–14):

- **Direction:** $\vb u\times\vb v$ is orthogonal to *both* $\vb u$ and $\vb v$ — check: $\vb u\cdot(\vb u\times\vb v) = 0$ identically — with orientation given by the right-hand rule (fingers sweep $\vb u$ into $\vb v$, thumb points along the product).
- **Magnitude:** $\|\vb u\times\vb v\| = \|\vb u\|\|\vb v\|\sin\theta$ — the **area of the parallelogram** spanned by the two vectors (base $\|\vb u\|$ times height $\|\vb v\|\sin\theta$).
- Consequently $\vb u\times\vb v = \vb 0$ exactly when the vectors are parallel ($\sin\theta = 0$): a degenerate parallelogram has no area. And the product is **anticommutative**: $\vb v\times\vb u = -(\vb u\times\vb v)$ — same length, opposite orientation. Order matters.

```{figure} figures/ch16-cross-product.png
:name: fig-cross-product
:alt: Three-dimensional plot of vectors u and v lying in a plane, the shaded parallelogram they span, and the cross product vector rising perpendicular to that plane with length equal to the parallelogram's area.

$\vb u\times\vb v$ for $\vb u = \langle 2, 0.5, 0\rangle$, $\vb v = \langle 0.5, 2, 0\rangle$: perpendicular to the shaded parallelogram, pointing by the right-hand rule, with length $3.75$ — the parallelogram's area.
```

```{prf:example} Area and normal vector
:label: ex-cross
For $\vb u = \langle 2, 0.5, 0\rangle$ and $\vb v = \langle 0.5, 2, 0 \rangle$ (both in the $xy$-plane), compute $\vb u \times \vb v$, the parallelogram's area, and a unit normal to the plane containing them.

$$
\vb u\times\vb v = \bigl\langle 0.5\cdot 0 - 0\cdot 2,\;\; 0\cdot 0.5 - 2\cdot 0,\;\; 2\cdot 2 - 0.5\cdot 0.5\bigr\rangle = \langle 0,\ 0,\ 3.75\rangle.
$$

Area $= \|\langle 0,0,3.75\rangle\| = 3.75$; unit normal $\hat{\vb n} = \langle 0, 0, 1\rangle$ — straight up out of the $xy$-plane, as the right-hand rule predicts for a counterclockwise pair. Triangles come free: half a parallelogram, so a triangle with these edge vectors has area $1.875$.
```

```{prf:example} A triangle in space
:label: ex-cross-triangle
Find the area of the triangle with vertices $P(1,0,0)$, $Q(0,2,0)$, $R(0,0,3)$.

Edge vectors from $P$: $\overrightarrow{PQ} = \langle -1, 2, 0\rangle$, $\overrightarrow{PR} = \langle -1, 0, 3\rangle$.

$$
\overrightarrow{PQ}\times\overrightarrow{PR} = \langle 2\cdot3 - 0,\;\; 0 - (-3),\;\; 0 + 2 \rangle = \langle 6, 3, 2\rangle,
$$

$$
\text{Area} = \tfrac12\|\langle 6,3,2\rangle\| = \tfrac12\sqrt{36+9+4} = \tfrac{7}{2}.
$$

No angles measured, no heights dropped — the cross product converts three points into an area by pure arithmetic, which is exactly how graphics engines and mesh software compute surface areas and facet normals millions of times per frame.
```

The **scalar triple product** $\vb u\cdot(\vb v\times\vb w)$ extends the story one dimension: its absolute value is the *volume* of the parallelepiped spanned by the three vectors, and it vanishes exactly when they are coplanar. Chapter 19 will recognize it as a $3\times3$ determinant — the bridge between this chapter's geometry and matrix algebra.

## 16.4 Common mistakes

```{admonition} Common Mistakes
:class: warning
**Dot products of dot products.** $\vb u\cdot\vb v$ is a *scalar*: expressions like $(\vb u\cdot\vb v)\cdot\vb w$ are scalar-times-vector (fine, but write it as $(\vb u\cdot\vb v)\,\vb w$), and "$\vb u\cdot\vb v\cdot\vb w$" is meaningless.

**Cancelling dots.** $\vb u\cdot\vb v = \vb u\cdot\vb w$ does **not** imply $\vb v = \vb w$ — it implies $\vb u\cdot(\vb v - \vb w) = 0$, i.e. the difference is merely *orthogonal to $\vb u$*. There is no division for vectors.

**cos from the wrong quotient.** The denominator in $\cos\theta$ is $\|\vb u\|\|\vb v\|$ — product of norms, not norm of the sum, and both norms, not one. A "cosine" outside $[-1, 1]$ is the standard symptom.

**Projecting onto the wrong vector.** $\operatorname{proj}_{\vb a}\vb b$ lies along $\vb a$ (the subscript), with denominator $\vb a\cdot\vb a$. Swapping the roles produces a different vector entirely unless $\|\vb a\| = \|\vb b\|$.

**Cross product carelessness.** It exists only in $\mathbb{R}^3$; it is *anti*commutative ($\vb v\times\vb u = -\vb u\times\vb v$); and it is not associative. Also the middle component's sign trips everyone: it is $u_3v_1 - u_1v_3$ (note the reversal). The determinant mnemonic, expanded carefully, protects you.

**$\times$ versus $\cdot$ in writing.** In vector work, $\times$ *means the cross product* — never write it for scalar multiplication of vectors.
```

## 16.5 Now do it in Python

NumPy provides all three products — `@` (dot), `np.cross`, and norms — and the worked examples verify in a dozen lines:

```python
import numpy as np

a = np.array([4.0, 1.0]); b = np.array([2.0, 3.0])

# --- Example 16.3: angle ---
cos_th = (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))
print(a @ b, cos_th, np.degrees(np.arccos(cos_th)))
# 11.0   0.73994...   42.2737...

# --- Example 16.5: projection and orthogonal residual ---
proj = (a @ b) / (a @ a) * a
resid = b - proj
print(proj, resid, a @ resid)      # [2.588 0.647] [-0.588 2.353]  ~0

# --- Examples 16.6-16.7: cross products ---
u = np.array([2.0, 0.5, 0.0]); v = np.array([0.5, 2.0, 0.0])
print(np.cross(u, v), np.linalg.norm(np.cross(u, v)))   # [0 0 3.75] 3.75
PQ = np.array([-1.0, 2.0, 0.0]); PR = np.array([-1.0, 0.0, 3.0])
print(0.5 * np.linalg.norm(np.cross(PQ, PR)))           # 3.5
```

Note `a @ resid` prints something like `4.4e-16` rather than exactly `0` — floating-point arithmetic's version of zero, a recurring theme: numerical orthogonality means *tiny*, not literal zero, and tests should be written `abs(a @ resid) < 1e-10`, never `== 0`.

**Cosine similarity at scale** is one line per pair — and one *matrix multiplication* for all pairs at once, a preview of Chapter 17's payoff:

```python
docs = np.array([[6, 2, 2],      # user A
                 [3, 1, 1],      # user B  (= A/2)
                 [1, 5, 0.]])    # user C
unit = docs / np.linalg.norm(docs, axis=1, keepdims=True)
print(np.round(unit @ unit.T, 3))
# [[1.    1.    0.485]
#  [1.    1.    0.485]
#  [0.485 0.485 1.   ]]
```

**Interpretation.** The similarity matrix says at a glance what Chapter 15 could only gesture at: A and B are perfectly aligned (cosine $1.0$ — same taste, different volume), while C's viewing direction sits at $\cos^{-1}(0.485) \approx 61°$ from both. Reading a matrix of dot products as a table of angles is a habit that will pay for itself weekly.

```{admonition} Data Science Connection
:class: tip
It is only mild hyperbole to call modern machine learning "dot products at industrial scale." A linear model's prediction is $\vb w\cdot\vb x + b$ — one dot product per example; a neural network layer computes many dot products in parallel (Chapter 17 packages them as a matrix product); attention in transformers scores query–key pairs by scaled dot products; and retrieval systems rank billions of embeddings by cosine similarity. The projection formula, meanwhile, *is* least-squares fitting in embryo: regression finds the combination of feature vectors nearest to the target vector, and "nearest" is enforced exactly by {prf:ref}`def-projection`'s orthogonality condition on the residual.
```

```{admonition} Looking Ahead
:class: seealso
The orthogonality integrals that powered Fourier series (Chapter 14) can now be named honestly: $\int_{-\pi}^{\pi} f g\,dx$ is a dot product with infinitely many components, the harmonics are mutually orthogonal vectors, and Fourier coefficients are scalar projections onto them — one formula, {prf:ref}`def-projection`, governing both worlds. Next, matrices arrive; every entry of a matrix product will be a dot product, and the cross product's determinant mnemonic becomes a theorem in Chapter 19.
```

## 16.6 Exercises

### Quick Check

1. Compute $\langle 1, 3, -2\rangle\cdot\langle 4, 0, 5 \rangle$.
2. For what value of $c$ are $\langle 2, c \rangle$ and $\langle 3, 6\rangle$ orthogonal?
3. What is $\|\vb u \times \vb v\|$ if $\|\vb u\| = 3$, $\|\vb v\| = 4$, and $\theta = 90°$? If $\theta = 0°$?
4. True or false: $\vb u\cdot\vb u = \|\vb u\|^2$ and $\vb u\times\vb u = \vb 0$.

````{admonition} Answers to Quick Checks
:class: dropdown
1. $4 + 0 - 10 = -6$.
2. $6 + 6c = 0 \Rightarrow c = -1$.
3. $12$ (full parallelogram — a rectangle); $0$ (degenerate).
4. Both true — the first is the norm bridge, the second the parallel-vectors rule applied to $\theta = 0$.
````

### Basic Practice

5. For $\vb u = \langle 1, -2, 2\rangle$ and $\vb v = \langle 3, 4, 0 \rangle$: compute $\vb u\cdot\vb v$, the angle between them (degrees and radians), $\operatorname{proj}_{\vb v}\vb u$, and $\vb u\times\vb v$.
6. Determine whether each pair is orthogonal, parallel, or neither: (a) $\langle 2, -1, 3\rangle$, $\langle 4, -2, 6\rangle$; (b) $\langle 1, 1, 1 \rangle$, $\langle 1, -2, 1\rangle$; (c) $\langle 2, 3\rangle$, $\langle 1, 1\rangle$.
7. Find the area of the parallelogram spanned by $\langle 1, 2, 3\rangle$ and $\langle 2, 0, 1 \rangle$, and a unit vector perpendicular to both.
8. A $50$-newton force is applied at $30°$ above horizontal to drag a crate $10$ m horizontally. Compute the work $W = \vb F\cdot\vb d$ two ways: from the angle formula, and from components.

````{admonition} Solution to Exercise 5 (projection part)
:class: dropdown
$\vb u\cdot\vb v = 3 - 8 + 0 = -5$ and $\vb v\cdot\vb v = 25$:

$$
\operatorname{proj}_{\vb v}\vb u = \frac{-5}{25}\,\vb v = -\tfrac15\langle 3,4,0\rangle = \langle -0.6, -0.8, 0 \rangle.
$$

The negative coefficient records an obtuse angle: the shadow points *backwards* along $\vb v$. Check: $\cos\theta = \frac{-5}{3\cdot 5} = -\frac13$, $\theta \approx 109.5°$ — obtuse indeed.
````

### Intermediate Practice

9. Find all vectors in $\mathbb{R}^2$ orthogonal to $\langle 3, 4\rangle$, and the *two unit* vectors among them. Generalize: describe geometrically the set of all vectors in $\mathbb{R}^3$ orthogonal to a fixed nonzero $\vb n$. *(You have just described a plane through the origin — with $\vb n$ as its **normal vector**.)*
10. Using Exercise 9's idea, find an equation for the plane through the point $(1, 2, 3)$ with normal $\vb n = \langle 2, -1, 4\rangle$: a point $\vb x$ lies on it exactly when $\vb n\cdot(\vb x - \langle 1,2,3\rangle) = 0$. Expand to the form $2x - y + 4z = d$.
11. Verify the **Cauchy–Schwarz inequality** $|\vb u\cdot\vb v| \le \|\vb u\|\|\vb v\|$ for three vector pairs of your choice, and explain in one sentence why {prf:ref}`thm-dot-angle` makes it obvious.
12. For the users of §16.5's similarity matrix, add user D $= \langle 0, 1, 5\rangle$, recompute, and rank the other users by similarity to D. Then rank them by *Euclidean distance* to D and compare the two rankings, explaining any disagreement.
13. Verify from {prf:ref}`def-cross` that $\vb u\cdot(\vb u\times\vb v) = 0$ for all $\vb u, \vb v$ (expand; watch the six terms annihilate in pairs).
14. Prove the magnitude identity $\|\vb u\times\vb v\|^2 = \|\vb u\|^2\|\vb v\|^2 - (\vb u\cdot\vb v)^2$ by brute component expansion for vectors in $\mathbb{R}^3$, then deduce $\|\vb u\times\vb v\| = \|\vb u\|\|\vb v\|\sin\theta$ from {prf:ref}`thm-dot-angle`.

### Conceptual Understanding

15. Why does "$\vb u\cdot\vb v = 0 \Rightarrow$ perpendicular" make the dot product *more* useful in $\mathbb{R}^{100}$ than pictures ever could be? Give a data-flavored example of a question it answers there.
16. Explain the difference between what $\operatorname{proj}_{\vb a}\vb b$ and the scalar $\hat{\vb a}\cdot\vb b$ each tell you, and when a practitioner would want one versus the other.
17. The cross product does not generalize to $\mathbb{R}^2$ or $\mathbb{R}^4$ (as a vector product with its properties), but the *dot* product works everywhere. Looking at the two definitions, what structural difference explains this?

### Python Practice

18. Verify Exercises 5–8 and 12 in NumPy. For 11, test Cauchy–Schwarz on 1000 random pairs in $\mathbb{R}^{20}$ and report the maximum of $\frac{|\vb u\cdot\vb v|}{\|\vb u\|\|\vb v\|}$ observed.
19. Random high-dimensional vectors are surprisingly orthogonal: for dimensions $d \in \{2, 10, 100, 1000\}$, draw 2000 pairs of standard-normal vectors, compute their cosine similarities, and report the mean and standard deviation for each $d$. Describe the trend. *(This concentration of angles near $90°$ is one face of the "curse of dimensionality.")*

### Visualization Practice

20. Recreate {numref}`fig-dot-projection` for $\vb a = \langle 1, 3\rangle$, $\vb b = \langle 4, 1 \rangle$, drawing $\vb b$, its projection onto $\vb a$, and the residual, and annotate the right angle.
21. Plot a histogram of the $d = 1000$ cosine similarities from Exercise 19 and overlay the $d = 2$ histogram. The visual contrast *is* the curse of dimensionality; caption the figure in one sentence.

### Challenge

22. **Least squares in one line.** Points $(1, 1), (2, 3), (3, 4)$ nearly lie on a line through the origin $y = mx$. In vector form, we seek the multiple of $\vb x = \langle 1,2,3\rangle$ nearest to $\vb y = \langle 1,3,4\rangle$ — which is exactly $\operatorname{proj}_{\vb x}\vb y$. Compute $m = \frac{\vb x\cdot\vb y}{\vb x\cdot\vb x}$, the fitted values, and the residual vector; verify the residual is orthogonal to $\vb x$; and plot points, line, and residuals. *(You have just derived and run univariate least-squares regression from the projection formula.)*
23. Prove the scalar triple product's cyclic symmetry $\vb u\cdot(\vb v\times\vb w) = \vb v\cdot(\vb w\times\vb u)$ by expanding both sides, and explain geometrically why any cyclic relabeling of a parallelepiped's edges leaves its volume unchanged.

### Cumulative Review

24. *(Ch. 14)* Compute the "dot product" $\int_{-\pi}^{\pi}\sin 2x\,\sin 3x\,dx$ and $\int_{-\pi}^{\pi}\sin^2 2x\,dx$, and translate both results into this chapter's vocabulary of orthogonality and squared norm.
25. *(Ch. 4, 15)* Redo Chapter 15's Exercise 22 — minimizing $\|t\vb a - \vb b\|^2$ over $t$ for $\vb a = \langle 3,4\rangle$, $\vb b = \langle 0, 5\rangle$ — by expanding with dot products, differentiating in $t$, and confirming the minimizer is the projection coefficient $\frac{\vb a\cdot\vb b}{\vb a\cdot\vb a}$.

## 16.7 Summary

The dot product $\vb u\cdot\vb v = \sum u_iv_i$ packages length ($\vb v\cdot\vb v = \|\vb v\|^2$) and angle ($\vb u\cdot\vb v = \|\vb u\|\|\vb v\|\cos\theta$) into one componentwise formula valid in every dimension; its sign classifies alignment, and its vanishing defines orthogonality — perpendicularity by arithmetic. Projection $\operatorname{proj}_{\vb a}\vb b = \frac{\vb a\cdot\vb b}{\vb a\cdot\vb a}\vb a$ splits any vector into a shadow along a direction plus an orthogonal residual, the seed of least squares; normalized, the angle formula becomes cosine similarity, the currency of retrieval and recommendation. The cross product, exclusive to $\mathbb{R}^3$, returns a vector orthogonal to both factors (right-hand rule), with magnitude the spanned parallelogram's area, vanishing exactly for parallel inputs, anticommutative, and computed by a determinant mnemonic that Chapter 19 will vindicate; the triple product extends it to volumes. In NumPy: `@`, `np.cross`, `np.linalg.norm`, with floating-point zeros read as "tiny" and whole similarity matrices computed by one matrix product — the operation the next chapter defines.

*Parallel reading:* OpenStax *Calculus Volume 3*, Sections 2.3–2.4 {cite}`openstax_calc3`; Goodfellow et al., §2.2 {cite}`goodfellow_linalg`.
