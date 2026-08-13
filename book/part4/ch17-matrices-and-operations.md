# Chapter 17 · Matrices and Matrix Operations

A matrix is, at first glance, just a rectangular grid of numbers — a spreadsheet without labels. The insight that makes linear algebra a subject rather than a filing system is that a matrix is also a *machine*: it acts on vectors, transforming all of $\mathbb{R}^n$ at once, and multiplying two matrices composes their machines. This chapter builds matrix arithmetic — addition, scaling, the all-important product, and the transpose — while keeping both faces in view: the grid of data and the transformation it performs.

## 17.1 The object and its arithmetic

```{prf:definition} Matrix
:label: def-matrix
An **$m \times n$ matrix** is a rectangular array of numbers with $m$ rows and $n$ columns:

$$
\mathit{A} = \begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n}\\ a_{21} & a_{22} & \cdots & a_{2n}\\ \vdots & & \ddots & \vdots\\ a_{m1} & a_{m2} & \cdots & a_{mn}\end{bmatrix},
$$

with $a_{ij}$ the entry in **row $i$, column $j$** — row index first, always. Matrices are written as italic capitals ($\mathit A$, $\mathit B$); a vector in $\mathbb{R}^m$ is the special case $n = 1$ (a column matrix).
```

Shapes matter constantly, so say them aloud: "$\mathit A$ is $3\times2$" means 3 rows, 2 columns. Addition and scalar multiplication are componentwise, exactly as for vectors, and defined only between matrices of *identical* shape:

$$
(\mathit A + \mathit B)_{ij} = a_{ij} + b_{ij}, \qquad (c\mathit A)_{ij} = c\,a_{ij}.
$$

They inherit all the usual laws. Some recurring special citizens: the **zero matrix** (all zeros); **square** matrices ($m = n$); **diagonal** matrices (nonzero entries only where $i = j$); and the **identity matrix**

$$
\mathit I = \begin{bmatrix}1 & 0 & \cdots\\ 0 & 1 & \\ \vdots & & \ddots\end{bmatrix},
$$

which will act as the number $1$ of matrix arithmetic. The **transpose** $\mathit A^{\mathsf T}$ flips rows and columns, $(\mathit A^{\mathsf T})_{ij} = a_{ji}$, turning $m\times n$ into $n \times m$; a square matrix with $\mathit A^{\mathsf T} = \mathit A$ is **symmetric** — a class with a starring role in Chapter 20.

## 17.2 The matrix–vector product: two readings

The product of an $m\times n$ matrix with a vector $\vb x \in \mathbb{R}^n$ is a vector $\mathit A\vb x \in \mathbb{R}^m$, and it can be read two ways — both essential, each illuminating what the other obscures.

**Reading 1 (rows): one dot product per output component.**

$$
(\mathit A\vb x)_i = (\text{row } i \text{ of } \mathit A)\cdot \vb x = \sum_{j=1}^n a_{ij}x_j.
$$

**Reading 2 (columns): a linear combination of the columns.**

$$
\mathit A\vb x = x_1\,\vb a_1 + x_2\,\vb a_2 + \cdots + x_n\,\vb a_n,
$$

where $\vb a_j$ is the $j$-th column: the input's components are *recipe amounts*, and the output mixes the columns accordingly.

```{prf:example} One product, two readings
:label: ex-matvec
Compute $\mathit A\vb x$ for $\mathit A = \begin{bmatrix} 1 & 2\\ 3 & -1\\ 0 & 4\end{bmatrix}$, $\vb x = \begin{bmatrix}2 \\ 1\end{bmatrix}$.

By rows — three dot products: $\langle 1,2\rangle\cdot\langle 2,1\rangle = 4$; $\ \langle 3,-1\rangle\cdot\langle2,1\rangle = 5$; $\ \langle 0,4\rangle\cdot\langle2,1\rangle = 4$.

By columns — a linear combination:

$$
2\begin{bmatrix}1\\3\\0\end{bmatrix} + 1\begin{bmatrix}2\\-1\\4\end{bmatrix} = \begin{bmatrix}4\\5\\4\end{bmatrix}.
$$

Same answer, $\mathit A\vb x = \langle 4, 5, 4\rangle$, and note the shape logic: $(3\times 2)(2\times 1) = 3\times 1$ — inner dimensions must match and are consumed; outer dimensions survive.
```

The column reading powers the chapter's central idea: a matrix **is** a transformation. The function $T(\vb x) = \mathit A\vb x$ maps $\mathbb{R}^n \to \mathbb{R}^m$, it is **linear** — $\mathit A(\vb u + \vb v) = \mathit A\vb u + \mathit A\vb v$ and $\mathit A(c\vb v) = c\,\mathit A\vb v$, straight from the definitions — and it is completely determined by where it sends the standard basis. Indeed $\mathit A\vb e_j$ picks out column $j$ ("one unit of ingredient $j$, nothing else"), so:

> **The columns of $\mathit A$ are the images of the basis vectors.** To know the whole transformation, know where $\vb e_1, \ldots, \vb e_n$ land.

```{figure} figures/ch17-matrix-transform.png
:name: fig-matrix-transform
:alt: Left: the unit square with basis vectors e1 and e2 along its edges. Right: the sheared and stretched parallelogram image under the matrix A, with the transformed basis vectors along its edges equal to the columns of A.

The matrix $\mathit A = \begin{bmatrix}1 & 1\\ 0 & 1.5\end{bmatrix}$ as a transformation of the plane. The basis vectors land on the columns of $\mathit A$ — $\vb e_1 \mapsto \langle 1, 0\rangle$, $\vb e_2\mapsto\langle 1, 1.5\rangle$ — and the whole unit square follows linearly, carried to the parallelogram they span. Every linear map is "where does the grid go?"
```

```{prf:example} Designing a transformation
:label: ex-rotation
Find the matrix that rotates the plane counterclockwise by angle $\theta$.

Track the basis: $\vb e_1 = \langle 1, 0\rangle$ rotates to $\langle\cos\theta, \sin\theta\rangle$, and $\vb e_2 = \langle 0,1\rangle$ to $\langle -\sin\theta, \cos\theta\rangle$. Install these as columns:

$$
\mathit R_\theta = \begin{bmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{bmatrix}.
$$

Sanity checks: $\theta = 0$ gives $\mathit I$ (rotate by nothing = do nothing); $\theta = \frac\pi2$ gives $\begin{bmatrix}0 & -1\\ 1 & 0\end{bmatrix}$, sending $\langle 1, 0\rangle \mapsto \langle 0,1\rangle$ ✓. Building matrices by asking *where should the basis go?* is the working method — no formulas memorized, just columns installed.
```

## 17.3 The matrix–matrix product: composition

Apply $\mathit B$'s transformation, then $\mathit A$'s. The composite $\vb x \mapsto \mathit A(\mathit B\vb x)$ is again linear, so it must be some matrix — call it $\mathit{AB}$ — and demanding $(\mathit{AB})\vb x = \mathit A(\mathit B\vb x)$ for all $\vb x$ *forces* the multiplication rule:

```{prf:definition} Matrix product
:label: def-matmul
For $\mathit A$ of shape $m\times n$ and $\mathit B$ of shape $n \times p$, the product $\mathit{AB}$ has shape $m \times p$ with entries

$$
(\mathit{AB})_{ik} = \sum_{j=1}^{n} a_{ij}b_{jk} = (\text{row } i \text{ of } \mathit A)\cdot(\text{column } k \text{ of } \mathit B).
$$

Equivalently, column by column: the $k$-th column of $\mathit{AB}$ is $\mathit A$ applied to the $k$-th column of $\mathit B$.
```

The dot-product recipe — *row of the left, column of the right* — is the computational face; "composition of machines" is the meaning; and the column view ties them: $\mathit{AB}$'s columns record where $\mathit A$ sends $\mathit B$'s columns.

```{prf:example} Multiplying, and the failure of commutativity
:label: ex-matmul
For $\mathit A = \begin{bmatrix}2 & 1\\ 0 & 3\end{bmatrix}$ and $\mathit B = \begin{bmatrix}1 & -1\\ 4 & 2\end{bmatrix}$, compute $\mathit{AB}$ and $\mathit{BA}$.

$$
\mathit{AB} = \begin{bmatrix} 2\cdot1 + 1\cdot4 & 2\cdot(-1)+1\cdot2\\ 0\cdot1+3\cdot4 & 0\cdot(-1)+3\cdot2\end{bmatrix} = \begin{bmatrix}6 & 0\\ 12 & 6 \end{bmatrix},
\qquad
\mathit{BA} = \begin{bmatrix}2 & -2\\ 8 & 10\end{bmatrix}.
$$

$\mathit{AB} \neq \mathit{BA}$ — and composition explains why this is *expected*, not pathological: "rotate then stretch" and "stretch then rotate" are different procedures. Order of operations is real for matrices; every algebraic manipulation must respect it.
```

What survives from ordinary algebra, and what does not, is worth stating plainly. **Surviving:** associativity $(\mathit{AB})\mathit C = \mathit A(\mathit{BC})$ (composition is inherently associative — a genuinely useful freedom in choosing computation order), distributivity $\mathit A(\mathit B + \mathit C) = \mathit{AB} + \mathit{AC}$, the identity's role $\mathit{AI} = \mathit{IA} = \mathit A$, and powers $\mathit A^k$ of square matrices (apply $k$ times). **Not surviving:** commutativity, as seen; cancellation ($\mathit{AB} = \mathit{AC}$ does not force $\mathit B = \mathit C$); and the zero-product property ($\mathit{AB} = \mathit 0$ is possible with both factors nonzero — try $\mathit A = \mathit B = \begin{bmatrix}0&1\\0&0\end{bmatrix}$, whose square is zero). Division waits for Chapter 18's inverses, and exists only sometimes.

The transpose interacts with products by *reversing* them:

$$
(\mathit{AB})^{\mathsf T} = \mathit B^{\mathsf T}\mathit A^{\mathsf T}, \qquad (\mathit A^{\mathsf T})^{\mathsf T} = \mathit A, \qquad (\mathit A + \mathit B)^{\mathsf T} = \mathit A^{\mathsf T} + \mathit B^{\mathsf T},
$$

(the reversal is forced by shapes alone: if $\mathit{A}$ is $m\times n$ and $\mathit B$ is $n\times p$, only $\mathit B^{\mathsf T}\mathit A^{\mathsf T}$ has compatible dimensions). One consequence used everywhere in statistics: $\mathit A^{\mathsf T}\mathit A$ is always defined, always square, always symmetric — it is the matrix of all dot products between $\mathit A$'s columns, and it will reappear as the "Gram matrix" of least squares and covariance.

```{prf:example} A data matrix at work
:label: ex-data-matrix
A dataset of three houses uses features (area in $100$ m², bedrooms): rows of the **design matrix** $\mathit X = \begin{bmatrix}1.2 & 3\\ 0.8 & 2\\ 2.0 & 4\end{bmatrix}$. A linear pricing model has weights $\vb w = \langle 250, 40\rangle$ (thousand dollars per unit of each feature). Predict all prices at once.

$$
\mathit X\vb w = \begin{bmatrix}1.2\cdot250 + 3\cdot40\\ 0.8\cdot 250 + 2\cdot 40\\ 2.0\cdot250 + 4\cdot40\end{bmatrix} = \begin{bmatrix}420\\ 280\\ 660\end{bmatrix} \text{ (thousand dollars).}
$$

One matrix–vector product = the whole dataset scored. By the row reading, each prediction is a dot product $\vb x_i\cdot\vb w$ (Chapter 16's linear model, per house); by the column reading, the prediction vector is a combination of *feature columns* — $250\,(\text{area column}) + 40\,(\text{bedroom column})$ — the viewpoint from which regression (Chapter 18) asks: *which combination of columns best matches the observed prices?*
```

## 17.4 Common mistakes

```{admonition} Common Mistakes
:class: warning
**Treating $\mathit{AB}$ as entrywise.** The product is rows-dot-columns; entrywise multiplication is a different operation (the Hadamard product, `A * B` in NumPy) with different uses. `A @ B` is the matrix product.

**Ignoring shape compatibility.** $\mathit{AB}$ requires (cols of $\mathit A$) $=$ (rows of $\mathit B$). Announce shapes before multiplying — $(m\times n)(n\times p) \to m\times p$ — and most errors die at the announcement.

**Commuting freely.** Expanding $(\mathit A + \mathit B)^2$ as $\mathit A^2 + 2\mathit{AB} + \mathit B^2$ is wrong; the correct expansion is $\mathit A^2 + \mathit{AB} + \mathit{BA} + \mathit B^2$, and the middle terms merge only if the matrices happen to commute.

**Forgetting the transpose reversal.** $(\mathit{AB})^{\mathsf T} = \mathit B^{\mathsf T}\mathit A^{\mathsf T}$ — socks on, then shoes on; shoes off, then socks off.

**Cancelling.** From $\mathit{AB} = \mathit{AC}$, concluding $\mathit B = \mathit C$ requires $\mathit A$ to be invertible (Chapter 18); in general it fails.

**Row/column index amnesia.** $a_{ij}$ is row $i$, column $j$ — and in code, `A[i, j]` likewise, with zero-based indices. Off-by-transposition bugs produce shape errors when lucky and silently wrong numbers when not; `assert` shapes.
```

## 17.5 Now do it in Python

NumPy's `@` operator is the matrix product; `.T` transposes; `*` is entrywise (a distinction to internalize on day one) {cite}`harris2020numpy`:

```python
import numpy as np

# --- Example 17.2: matrix-vector, both readings ---
A = np.array([[1.0, 2], [3, -1], [0, 4]])
x = np.array([2.0, 1])
print(A @ x)                                   # [4. 5. 4.]
print(x[0]*A[:, 0] + x[1]*A[:, 1])             # same: column combination

# --- Example 17.4: products and non-commutativity ---
A = np.array([[2.0, 1], [0, 3]])
B = np.array([[1.0, -1], [4, 2]])
print(A @ B)        # [[ 6.  0.] [12.  6.]]
print(B @ A)        # [[ 2. -2.] [ 8. 10.]]
print(A * B)        # entrywise -- a DIFFERENT operation: [[2. -1.] [0. 6.]]

# --- Transpose reversal, checked ---
print(np.allclose((A @ B).T, B.T @ A.T))       # True

# --- Example 17.5: score a whole dataset ---
X = np.array([[1.2, 3], [0.8, 2], [2.0, 4]])
w = np.array([250.0, 40])
print(X @ w)                                   # [420. 280. 660.]
```

Two professional habits ride along. First, `np.allclose` for comparing float matrices — never `==`. Second, shape narration: `A.shape` is `(3, 2)`, and a comment like `# (n_samples, n_features) @ (n_features,) -> (n_samples,)` above each product documents the computation better than prose.

**Visualization.** Watching a matrix act on many points at once is the fastest route to transformation intuition:

```python
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 100)
circle = np.vstack([np.cos(theta), np.sin(theta)])    # shape (2, 100)
A = np.array([[1.0, 1.0], [0.0, 1.5]])
image = A @ circle                                    # 100 points transformed at once

fig, ax = plt.subplots()
ax.plot(*circle, color="gray", label="unit circle")
ax.plot(*image, color="tab:blue", label="image under A")
ax.set_aspect("equal"); ax.legend(); plt.show()
```

**Interpretation.** The circle maps to an ellipse — every linear map sends circles to ellipses (possibly degenerate), a fact that quietly contains this Part's remaining story: the ellipse's axes and their lengths are the *eigenvector directions and singular values* of Chapter 20. Try $\mathit R_\theta$ from {prf:ref}`ex-rotation` (circle stays a circle: rotations preserve lengths) and $\operatorname{diag}(2, \tfrac12)$ (axes stretch independently), and predict each picture before running it.

```{admonition} Data Science Connection
:class: tip
The design matrix — rows are observations, columns are features — is the standard container of tabular machine learning, and `X @ w` is *batch prediction*: every linear model, and every layer of every neural network ($\mathit W\vb x + \vb b$ followed by a nonlinearity), is matrix multiplication at its core. This is also why GPUs matter: they are matrix-multiplication engines, and the reason `A @ B` in NumPy beats any hand-written loop by orders of magnitude — optimized BLAS routines — is the same reason deep learning is feasible at all. Goodfellow et al. §2.1–2.2 covers exactly this ground {cite}`goodfellow_linalg`.
```

```{admonition} Looking Ahead
:class: seealso
Two urgent questions now have precise form. *Can a transformation be undone?* — inverses, and the systems $\mathit A\vb x = \vb b$ they solve, are Chapter 18. *By how much does a transformation distort area?* — {numref}`fig-matrix-transform`'s parallelogram has a computable area, the determinant of Chapter 19. And the ellipse just plotted points to Chapter 20.
```

## 17.6 Exercises

### Quick Check

1. For $\mathit A$ of shape $4\times 2$ and $\mathit B$ of shape $2\times 5$: which of $\mathit{AB}$, $\mathit{BA}$, $\mathit A^{\mathsf T}\mathit B$ exist, and with what shapes?
2. Compute $\begin{bmatrix}1 & 2\\ 3 & 4\end{bmatrix}\begin{bmatrix}1\\ -1\end{bmatrix}$ by rows, then by columns.
3. What matrix scales $x$-coordinates by $3$ and leaves $y$ alone?
4. True or false: if $\mathit A$ is symmetric, so is $\mathit A^2$.

````{admonition} Answers to Quick Checks
:class: dropdown
1. $\mathit{AB}$: $4\times5$. $\mathit{BA}$: undefined ($5 \ne 4$). $\mathit A^{\mathsf T}\mathit B$: $(2\times4)(2\times5)$ — undefined ($4\ne2$).
2. Rows: $\langle 1-2,\ 3-4\rangle$; columns: $1\begin{bmatrix}1\\3\end{bmatrix} - 1\begin{bmatrix}2\\4\end{bmatrix}$. Both: $\langle -1, -1\rangle$.
3. $\operatorname{diag}(3, 1) = \begin{bmatrix}3&0\\0&1\end{bmatrix}$ (install the images of the basis as columns).
4. True: $(\mathit A^2)^{\mathsf T} = \mathit A^{\mathsf T}\mathit A^{\mathsf T} = \mathit A\,\mathit A = \mathit A^2$.
````

### Basic Practice

5. With $\mathit A = \begin{bmatrix}1 & 0 & 2\\ -1 & 3 & 1\end{bmatrix}$, $\mathit B = \begin{bmatrix}3 & 1\\ 2 & 1\\ 1 & 0\end{bmatrix}$, $\vb v = \langle 1, 2, -1\rangle$: compute $\mathit A\vb v$, $\mathit{AB}$, $\mathit{BA}$, $\mathit A^{\mathsf T}$, and $\mathit A\mathit A^{\mathsf T}$, announcing every shape first.
6. Verify with {prf:ref}`ex-matmul`'s matrices that $(\mathit{AB})^{\mathsf T} = \mathit B^{\mathsf T}\mathit A^{\mathsf T}$ and that $(\mathit A + \mathit B)^2 \ne \mathit A^2 + 2\mathit{AB} + \mathit B^2$, identifying which cross term causes the failure.
7. Write the $2\times2$ matrices for: reflection across the $x$-axis; reflection across the line $y = x$; projection onto the $x$-axis; rotation by $90°$. *(For each: where do $\vb e_1, \vb e_2$ go?)*
8. Using {prf:ref}`ex-data-matrix`'s design matrix, a competing model has $\vb w' = \langle 300, 10\rangle$. Compute both models' predictions in one product by assembling $\mathit W = [\vb w\ \ \vb w']$ (shape $2\times2$) and computing $\mathit X\mathit W$; interpret each column of the result.

````{admonition} Solution to Exercise 7 (projection part)
:class: dropdown
Projection onto the $x$-axis: $\vb e_1 \mapsto \vb e_1$ and $\vb e_2 \mapsto \vb 0$, so $\mathit P = \begin{bmatrix}1 & 0\\ 0 & 0\end{bmatrix}$. Note $\mathit P^2 = \mathit P$ — projecting twice changes nothing after the first time, the defining equation of all projection matrices (compare {prf:ref}`def-projection`'s idempotent shadow).
````

### Intermediate Practice

9. Compute $\mathit R_{\alpha}\mathit R_{\beta}$ for the rotation matrices of {prf:ref}`ex-rotation` symbolically, and show — using the angle-sum identities of Chapter 2 — that the product is $\mathit R_{\alpha+\beta}$. (Composition of rotations is rotation by the sum; and since addition commutes, these particular matrices *do* commute.)
10. A matrix $\mathit N$ is **nilpotent** if some power is zero. Show $\mathit N = \begin{bmatrix}0&1&0\\0&0&1\\0&0&0\end{bmatrix}$ satisfies $\mathit N^3 = \mathit 0$, and describe what the transformation does to $\vb e_1, \vb e_2, \vb e_3$ that makes repeated application eventually annihilate everything.
11. For a general $m\times n$ matrix $\mathit X$, show that $\mathit X^{\mathsf T}\mathit X$ is symmetric, and that its $(j,k)$ entry is the dot product of columns $j$ and $k$ of $\mathit X$. What are its diagonal entries?
12. **Markov step.** A subscription service tracks states (active, churned) with monthly transition matrix $\mathit P = \begin{bmatrix}0.9 & 0.2\\ 0.1 & 0.8\end{bmatrix}$ (columns: current state; entries: probability of next state). Starting from $\vb x_0 = \langle 1, 0\rangle$ (all active), compute $\vb x_1 = \mathit P\vb x_0$, $\vb x_2$, $\vb x_3$ by hand, then $\mathit P^{50}\vb x_0$ in NumPy. The iterates approach $\langle \tfrac23, \tfrac13\rangle$; Chapter 20 will explain *why* and find that limit without iterating.

### Conceptual Understanding

13. Explain why defining $\mathit{AB}$ so that $(\mathit{AB})\vb x = \mathit A(\mathit B\vb x)$ leaves no freedom in the rows-dot-columns formula — where exactly does the sum $\sum_j a_{ij}b_{jk}$ come from in the composition?
14. "The columns of $\mathit A$ tell you everything about the transformation." Defend this claim using linearity, and explain what goes wrong for a *non*linear function like $f(x,y) = (x^2, y)$ — why don't two probe inputs suffice there?
15. Give a real-data interpretation for each factor and the product in $\mathit X^{\mathsf T}\mathit X$ when $\mathit X$ is a (centered) design matrix — what does entry $(j,k)$ measure about features $j$ and $k$?

### Python Practice

16. Verify Exercises 5–12 in NumPy (for 9, verify numerically at $\alpha = 0.3$, $\beta = 1.1$ with `np.allclose`). For 12, print $\mathit P^k\vb x_0$ for $k = 1, 2, 5, 10, 50$ and watch the convergence.
17. Time the difference that vectorization makes: score a design matrix of shape $(100\,000, 50)$ against a weight vector with `X @ w`, and again with an explicit Python double loop. Report the speed ratio. *(Use `time.perf_counter`; expect two to three orders of magnitude.)*

### Visualization Practice

18. Reproduce the circle-to-ellipse experiment of §17.5 for four matrices — a rotation, a diagonal stretch, the shear $\begin{bmatrix}1&1\\0&1\end{bmatrix}$, and the projection of Exercise 7 — in a 2×2 grid of subplots, predicting each panel before plotting. Which matrix collapses the circle to a segment, and what property of the matrix does that foreshadow?
19. Animate (or plot as small multiples) the Markov iterates of Exercise 12 as points $(\text{active}, \text{churned})$ marching toward $(\tfrac23, \tfrac13)$, for three different starting vectors on the line $x + y = 1$. What do all trajectories share?

### Challenge

20. Show that the shear $\mathit S = \begin{bmatrix}1 & 1\\ 0 & 1\end{bmatrix}$ satisfies $\mathit S^k = \begin{bmatrix}1 & k\\ 0 & 1\end{bmatrix}$ (induction), while the rotation $\mathit R_{\pi/6}$ satisfies $\mathit R_{\pi/6}^{12} = \mathit I$. Two matrices, two utterly different long-run behaviors under powering; compute $\|\mathit S^k\vb e_2\|$ and $\|\mathit R^k\vb e_2\|$ as functions of $k$ to quantify the difference. *(Chapter 20's eigenvalues will predict such behavior from the matrix alone.)*
21. **Adjacency powers.** For the directed graph on nodes $\{1,2,3,4\}$ with edges $1{\to}2, 2{\to}3, 3{\to}1, 3{\to}4, 4{\to}2$, build the adjacency matrix $\mathit M$ ($m_{ij} = 1$ if $j \to i$) and prove-by-meaning, then verify in NumPy, that $(\mathit M^k)_{ij}$ counts directed paths of length exactly $k$ from $j$ to $i$. How many length-6 paths run from node 1 to node 2?

### Cumulative Review

22. *(Ch. 16)* Every entry of $\mathit{AB}$ is a dot product. Use Cauchy–Schwarz (Ch. 16, Ex. 11) to bound $|(\mathit{AB})_{ik}|$ by the norms of the relevant row and column, and verify the bound on {prf:ref}`ex-matmul`.
23. *(Ch. 5)* The function $f(t) = \mathit R_t\,\vb v$ rotates a fixed vector by a growing angle. Differentiate the components of $\mathit R_t\langle 1, 0\rangle = \langle\cos t, \sin t\rangle$ and verify that $f'(t)$ is $f(t)$ rotated by $90°$ — i.e. $f'(t) = \mathit R_{\pi/2}f(t)$. *(Uniform circular motion's velocity is perpendicular to position; Chapter 21 builds on exactly this.)*

## 17.7 Summary

A matrix is a grid *and* a machine. Addition and scaling are entrywise; the matrix–vector product reads two ways — dot products with rows, or a linear combination of columns — with the column view revealing every matrix as a linear transformation whose columns are the destinations of the basis vectors (whence rotation, reflection, shear, and projection matrices are *built*, not memorized). The matrix–matrix product is composition, forced into the rows-dot-columns formula, associative and distributive but *not* commutative, without cancellation, and with $(\mathit{AB})^{\mathsf T} = \mathit B^{\mathsf T}\mathit A^{\mathsf T}$; the identity $\mathit I$ plays $1$, and $\mathit X^{\mathsf T}\mathit X$ — square, symmetric, dot products of columns — awaits its statistical career. In NumPy: `@` multiplies, `*` does not, shapes are announced and asserted, and one product scores an entire dataset — the reason this operation, run on hardware built for it, underlies effectively all of machine learning. Next: undoing the machine, $\mathit A\vb x = \vb b$.

*Parallel reading:* OpenStax *Calculus Volume 3* has no matrix chapter; use Goodfellow et al., §2.1–2.2 {cite}`goodfellow_linalg` and Strang {cite}`strang_linalg`, Chapter 2.
