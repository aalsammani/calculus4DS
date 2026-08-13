# Chapter 15 · Vectors in the Plane and in Space

Part IV changes subject, from functions of one variable to the mathematics of *many numbers at once*. The primitive object is the **vector** — an ordered list of numbers with a geometric soul — and it is no exaggeration to say that vectors are the native data type of data science: a customer is a vector of attributes, an image is a vector of pixel intensities, a document is a vector of word counts, and a model's parameters are one very long vector. This chapter builds the object itself: components, arrows, the two fundamental operations, length, and direction, in two dimensions where we can draw and in three (and then $n$) where the applications live.

## 15.1 Two views of one object

```{prf:definition} Vector
:label: def-vector
A **vector** in $\mathbb{R}^n$ is an ordered $n$-tuple of real numbers, written as a column

$$
\vb{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix}
$$

(or, inline, $\vb v = \langle v_1, \ldots, v_n\rangle$). The numbers $v_i$ are its **components**. Vectors are printed in bold ($\vb v$); handwritten work uses an arrow ($\vec v$). A single real number, by contrast, is called a **scalar**.
```

The same object supports two mental pictures, and fluency means switching between them freely.

**The algebraic view:** $\vb v$ is a list — a row of a spreadsheet, a point's coordinates, a record. Nothing spatial required, and $n$ can be $2$ or $2$ million.

**The geometric view:** $\vb v$ is an **arrow** — a displacement of $v_1$ in the $x$-direction and $v_2$ in the $y$-direction. Crucially, the arrow is defined by *direction and length only*, not by where it starts: the arrow from $(0,0)$ to $(3,1)$ and the arrow from $(5,2)$ to $(8,3)$ are the *same vector* $\langle 3, 1\rangle$. Drawn from the origin, a vector's tip lands on the point with the same coordinates, which is why points and vectors are used interchangeably; drawn from anywhere else, it represents a displacement. The vector between two points is found by subtraction, tip minus tail: the vector from $P(1, 4)$ to $Q(5, 2)$ is $\overrightarrow{PQ} = \langle 5-1,\, 2-4\rangle = \langle 4, -2\rangle$.

## 15.2 The two operations

Everything in linear algebra is built from exactly two operations, both performed componentwise.

```{prf:definition} Vector addition and scalar multiplication
:label: def-vector-ops
For $\vb u, \vb v \in \mathbb{R}^n$ and a scalar $c$:

$$
\vb u + \vb v = \begin{bmatrix} u_1 + v_1 \\ \vdots \\ u_n + v_n\end{bmatrix},
\qquad
c\,\vb v = \begin{bmatrix} c\,v_1 \\ \vdots \\ c\,v_n\end{bmatrix}.
$$
```

Geometrically, addition is **tip-to-tail**: slide $\vb v$'s tail to $\vb u$'s tip; the sum runs from $\vb u$'s tail to $\vb v$'s new tip. Equivalently, $\vb u + \vb v$ is the diagonal of the parallelogram the two arrows span — the two constructions in {numref}`fig-vector-operations` are the same picture. Scalar multiplication **rescales**: $2\vb w$ doubles the length, $\tfrac12\vb w$ halves it, and a negative scalar flips the direction, with $-\vb v$ the exact reverse of $\vb v$. Subtraction combines the two: $\vb u - \vb v = \vb u + (-\vb v)$, the arrow *from the tip of $\vb v$ to the tip of $\vb u$* when both start together — worth drawing once and remembering forever, since "difference vectors" (error = observed − predicted) are everywhere in applications.

```{figure} figures/ch15-vector-operations.png
:name: fig-vector-operations
:alt: Left panel: vectors u and v drawn from the origin with dashed copies completing a parallelogram whose diagonal is u plus v. Right panel: a vector w with the scaled versions two w, and negative w, showing stretching and reversal.

The two fundamental operations. Left: $\vb u + \vb v$ by tip-to-tail, equivalently the parallelogram diagonal. Right: scalar multiples of $\vb w$ stretch ($2\vb w$), and flip ($-\vb w$) the arrow while keeping it on the same line.
```

These operations obey the familiar laws of arithmetic — commutativity $\vb u + \vb v = \vb v + \vb u$, associativity, distributivity $c(\vb u + \vb v) = c\vb u + c\vb v$, and so on — precisely because each component obeys them. The zero vector $\vb 0 = \langle 0, \ldots, 0\rangle$ is the identity for addition (an arrow of no displacement).

A **linear combination** chains the two operations: $c_1\vb v_1 + c_2\vb v_2 + \cdots + c_k\vb v_k$. It is the master construction of the subject — Chapters 17–18 will reveal that multiplying by a matrix, and solving a linear system, are both statements about linear combinations — so it deserves a name and attention now.

```{prf:example} Component arithmetic
:label: ex-vector-arithmetic
Let $\vb u = \langle 3, 1 \rangle$ and $\vb v = \langle 1, 2\rangle$ (the vectors of {numref}`fig-vector-operations`). Compute $\vb u + \vb v$, $\ \vb u - \vb v$, and the linear combination $2\vb u - 3\vb v$.

$$
\vb u + \vb v = \langle 4, 3\rangle, \qquad
\vb u - \vb v = \langle 2, -1\rangle, \qquad
2\vb u - 3\vb v = \langle 6 - 3,\ 2 - 6\rangle = \langle 3, -4\rangle.
$$

Nothing here is deep — and that is the point: the algebra is trivially mechanical, which frees all attention for what combinations *mean* geometrically.
```

## 15.3 Length and direction

```{prf:definition} Magnitude
:label: def-magnitude
The **magnitude** (length, norm) of $\vb v \in \mathbb{R}^n$ is

$$
\|\vb v\| = \sqrt{v_1^2 + v_2^2 + \cdots + v_n^2}.
$$
```

In the plane this is the Pythagorean theorem applied to the arrow's horizontal and vertical legs; in $\mathbb{R}^3$, Pythagoras applied twice; in $\mathbb{R}^n$, the definition simply continues the pattern. Magnitude interacts with scaling exactly as geometry demands: $\|c\vb v\| = |c|\,\|\vb v\|$. A vector of magnitude $1$ is a **unit vector** — pure direction, no size — and any nonzero $\vb v$ is turned into one by dividing by its own length:

$$
\hat{\vb v} = \frac{\vb v}{\|\vb v\|} \qquad\text{(normalization).}
$$

Every nonzero vector thus factors as (length) × (direction): $\vb v = \|\vb v\|\,\hat{\vb v}$ — a decomposition used constantly, since many questions care about only one factor.

```{prf:example} Normalizing
:label: ex-normalize
Find the magnitude and direction of $\vb v = \langle 3, -4 \rangle$, and the vector of length $10$ in the same direction.

$\|\vb v\| = \sqrt{9 + 16} = 5$, so $\hat{\vb v} = \langle \frac35, -\frac45\rangle$ (check: $\frac{9}{25} + \frac{16}{25} = 1$ ✓). The length-$10$ version is $10\,\hat{\vb v} = \langle 6, -8\rangle$ — equivalently $2\vb v$, since the target length happened to be twice the original.
```

The **standard basis vectors** point along the axes with unit length: in $\mathbb{R}^2$, $\vb i = \langle 1, 0\rangle$ and $\vb j = \langle 0, 1\rangle$; in $\mathbb{R}^3$, additionally $\vb k = \langle 0,0,1\rangle$. Every vector is transparently a linear combination of them,

$$
\langle 3, 1, -2 \rangle = 3\vb i + \vb j - 2\vb k,
$$

which shows the components in their true light: *coordinates are coefficients* — the recipe for building the vector from standard ingredients. Change the ingredients (a theme for Chapter 20) and the same arrow gets new coordinates.

## 15.4 Three dimensions, then $n$

$\mathbb{R}^3$ adds a $z$-axis perpendicular to the $xy$-plane, by convention forming a **right-handed** system: curl the right hand's fingers from the $+x$ toward the $+y$ axis and the thumb points along $+z$. All the machinery transfers without modification, including the distance between points as the magnitude of their difference vector:

$$
d(P, Q) = \|\overrightarrow{PQ}\| = \sqrt{(q_1 - p_1)^2 + (q_2 - p_2)^2 + (q_3 - p_3)^2}.
$$

```{prf:example} Geometry in $\mathbb{R}^3$
:label: ex-3d-distance
An aircraft is at $P(2, -1, 10)$ (kilometers) and a waypoint at $Q(5, 3, 11)$. Find the displacement vector, the straight-line distance, and the unit vector giving the flight direction.

$$
\overrightarrow{PQ} = \langle 3, 4, 1\rangle, \qquad
\|\overrightarrow{PQ}\| = \sqrt{9 + 16 + 1} = \sqrt{26} \approx 5.10 \text{ km},
$$

$$
\hat{\vb d} = \frac{1}{\sqrt{26}}\langle 3, 4, 1 \rangle \approx \langle 0.588,\ 0.784,\ 0.196\rangle.
$$

Direction times distance recovers the displacement: $\sqrt{26}\,\hat{\vb d} = \overrightarrow{PQ}$. ✓
```

Beyond three dimensions the pictures stop but *nothing else does*: $\mathbb{R}^{50}$ has vectors, addition, scaling, linear combinations, magnitudes, unit vectors, and distances, all by the same componentwise formulas, all obeying the same laws. This is the quiet superpower of the algebraic view — geometry's theorems, proved by algebra, keep working where geometry's drawings cannot follow. When Chapter 16's dot product adds angles to the toolkit, phrases like "these two customers point in similar directions" will be literal mathematics in $\mathbb{R}^{1000}$.

```{prf:example} A data vector
:label: ex-data-vector
A streaming service logs each user's weekly hours as $\langle\text{drama},\ \text{comedy},\ \text{documentary}\rangle$. User A is $\vb a = \langle 6, 2, 2 \rangle$, user B is $\vb b = \langle 3, 1, 1\rangle$.

The difference $\vb a - \vb b = \langle 3, 1, 1\rangle$ measures how the users' habits differ, and its magnitude $\sqrt{11} \approx 3.32$ is a distance between users — the quantity nearest-neighbor recommendation methods rank by. Meanwhile $\vb b = \tfrac12 \vb a$: B is a half-intensity copy of A, *identical in direction*. Are A and B "similar"? By distance, moderately; by direction, perfectly — a genuine modeling decision (does total watch-time matter, or only taste profile?), and the normalization $\hat{\vb v}$ of §15.3 is precisely how one discards intensity to compare pure taste.
```

## 15.5 Common mistakes

```{admonition} Common Mistakes
:class: warning
**Adding magnitudes.** $\|\vb u + \vb v\| \ne \|\vb u\| + \|\vb v\|$ in general — the tip-to-tail triangle makes the sum's length *at most* the sum of lengths (equality only for parallel, same-direction vectors). Compute the sum first, then its magnitude.

**Confusing points with the vectors between them.** The vector from $P$ to $Q$ is $Q - P$ (tip minus tail), not $P - Q$ and not $\langle P, Q\rangle$. Reversing the subtraction reverses the direction.

**Normalizing by a component instead of the length.** $\hat{\vb v} = \vb v/\|\vb v\|$, with the full square-root-of-sum-of-squares in the denominator.

**Treating vectors of different dimensions as compatible.** $\langle 1, 2\rangle + \langle 1, 2, 3\rangle$ is undefined — no silent padding. (NumPy's broadcasting rules will *sometimes* do something in such cases; that something is not vector addition, and it is a classic source of silent bugs.)

**Sloppy notation.** Keep scalars and vectors typographically distinct ($c$ vs $\vb v$); expressions like "$\vb u + 3$" (vector plus scalar) are undefined in mathematics even where NumPy permits them.
```

## 15.6 Now do it in Python

NumPy's `ndarray` is the working incarnation of $\mathbb{R}^n$, with the two fundamental operations as ordinary arithmetic {cite}`harris2020numpy`:

```python
import numpy as np

u = np.array([3.0, 1.0])
v = np.array([1.0, 2.0])

# --- Example 15.3: the two operations are componentwise arithmetic ---
print(u + v)            # [4. 3.]
print(u - v)            # [ 2. -1.]
print(2*u - 3*v)        # [ 3. -4.]

# --- Examples 15.4-15.5: magnitude and normalization ---
w = np.array([3.0, -4.0])
print(np.linalg.norm(w))              # 5.0
w_hat = w / np.linalg.norm(w)
print(w_hat, np.linalg.norm(w_hat))   # [ 0.6 -0.8]  1.0

# --- Example 15.6: 3-D displacement, distance, direction ---
P = np.array([2.0, -1.0, 10.0])
Q = np.array([5.0, 3.0, 11.0])
d = Q - P
print(d, np.linalg.norm(d))           # [3. 4. 1.]  5.0990...
print(d / np.linalg.norm(d))          # [0.588  0.784  0.196]
```

Every operation vectorizes: `u + v` adds a million components as readily as two, in optimized compiled code, which is why idiomatic numerical Python contains almost no explicit loops. One habit to install immediately: **check shapes**. `u.shape` reports the dimensions, and shape mismatches — or worse, shape *matches* achieved by broadcasting when you didn't intend them — are the field's most common bug. `assert u.shape == v.shape` before a delicate operation is one line of cheap insurance.

**Visualization.** Matplotlib's `quiver` draws vector fields and single arrows; a serviceable arrow plot for the parallelogram law:

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
for vec, color in [(u, "tab:blue"), (v, "tab:green"), (u + v, "tab:red")]:
    ax.quiver(0, 0, *vec, angles="xy", scale_units="xy", scale=1, color=color)
ax.set_xlim(-1, 5); ax.set_ylim(-1, 4); ax.set_aspect("equal")
plt.show()
```

**Interpretation.** The red arrow is the diagonal of the parallelogram — and if you re-draw with `v` replaced by `-v`, the diagonal becomes the *other* one, illustrating that $\vb u + \vb v$ and $\vb u - \vb v$ are the two diagonals of the same parallelogram. Small experiments like this, one line changed and re-run, are how the geometric intuitions of this chapter get soldered in.

```{admonition} Data Science Connection
:class: tip
The row of a dataset *is* a vector, and this chapter's vocabulary is the field's daily speech: **feature vector** (one observation's numbers), **residual vector** (observed minus predicted — a difference vector whose magnitude is the error that training minimizes), **normalization** (unit vectors, so that scale doesn't masquerade as signal), and **distance between points** (the engine of $k$-nearest-neighbors and clustering). Goodfellow, Bengio, and Courville's deep learning text opens its mathematics with exactly this material {cite}`goodfellow_linalg` — vectors first, everything else after.
```

```{admonition} Looking Ahead
:class: seealso
Two operations are conspicuously missing: nothing yet *multiplies* two vectors, and nothing measures the **angle** between them. Chapter 16 supplies both — the dot product (angles, projections, similarity) and, special to $\mathbb{R}^3$, the cross product (perpendiculars, areas). Then matrices arrive as machines that act on vectors, and the linear combinations defined here become the key to everything they do.
```

## 15.7 Exercises

### Quick Check

1. Given $\vb u = \langle 2, -1\rangle$, $\vb v = \langle 0, 3 \rangle$: compute $\vb u + \vb v$, $\ 3\vb u$, and $\ \vb u - 2\vb v$.
2. What is $\|\langle 6, 8 \rangle\|$? The unit vector in its direction?
3. Find the vector from $P(4, 1)$ to $Q(1, 5)$ and its magnitude.
4. True or false: if $\|\vb u\| = \|\vb v\|$ then $\vb u = \pm\vb v$.

````{admonition} Answers to Quick Checks
:class: dropdown
1. $\langle 2, 2\rangle$; $\ \langle 6, -3\rangle$; $\ \langle 2, -7\rangle$.
2. $10$; $\ \langle 0.6, 0.8\rangle$.
3. $\overrightarrow{PQ} = \langle -3, 4\rangle$, magnitude $5$.
4. False — equal lengths say nothing about direction: $\langle 1, 0\rangle$ and $\langle 0,1\rangle$ have length 1.
````

### Basic Practice

5. For $\vb a = \langle 1, 2, -2\rangle$ and $\vb b = \langle 3, 0, 4\rangle$, compute $\vb a + \vb b$, $\ \vb a - \vb b$, $\ \|\vb a\|$, $\ \|\vb b\|$, $\ \hat{\vb a}$, and $\ 2\vb a + \tfrac12\vb b$.
6. Write $\langle 5, -2, 7\rangle$ as a combination of $\vb i, \vb j, \vb k$, and conversely write $4\vb i - \vb k$ in component form.
7. Find the point $Q$ such that $\overrightarrow{PQ} = \langle 2, -3, 1 \rangle$ with $P(1, 1, 1)$, and the distance from $P$ to $Q$.
8. A ship travels with displacement $\langle 30, 40\rangle$ km, then $\langle -10, 15 \rangle$ km. Find the total displacement, its magnitude, and the unit vector pointing back to the start.

````{admonition} Solution to Exercise 8
:class: dropdown
Total: $\langle 20, 55\rangle$ km, magnitude $\sqrt{400 + 3025} = \sqrt{3425} \approx 58.5$ km. The return direction is the *negative*, normalized:

$$
-\frac{\langle 20, 55\rangle}{\sqrt{3425}} \approx \langle -0.342,\ -0.940\rangle.
$$
````

### Intermediate Practice

9. Find all scalars $c$ for which $\|c\,\langle 2, -1, 2 \rangle\| = 12$, and explain geometrically why there are two.
10. The **midpoint** of points $P$ and $Q$ (as position vectors $\vb p, \vb q$) is $\frac12(\vb p + \vb q)$. Verify this for $P(2, 6)$, $Q(8, 0)$, then generalize: what point does $(1-t)\,\vb p + t\,\vb q$ trace as $t$ runs from $0$ to $1$? *(This parametrization of a segment returns in Chapter 21.)*
11. Vectors $\vb u$ and $\vb v$ are **parallel** if one is a scalar multiple of the other. Determine whether each pair is parallel: (a) $\langle 2, -4, 6\rangle$ and $\langle -3, 6, -9 \rangle$; (b) $\langle 1, 2, 3\rangle$ and $\langle 2, 4, 5\rangle$.
12. Using {prf:ref}`ex-data-vector`'s setup, a third user has $\vb c = \langle 1, 5, 0\rangle$. Which of A and C is closer to B in distance? Which has direction closer to B's (compare unit vectors componentwise for now — Chapter 16 gives the proper tool)? What does the disagreement between the two verdicts tell a recommender-system designer?

### Conceptual Understanding

13. Explain why the parallelogram construction and the tip-to-tail construction of $\vb u + \vb v$ must give the same answer, using the commutativity $\vb u + \vb v = \vb v + \vb u$.
14. The triangle inequality states $\|\vb u + \vb v\| \le \|\vb u\| + \|\vb v\|$. Draw the picture that justifies the name, and describe the exact condition for equality.
15. In your own words: what does it mean that "coordinates are coefficients," and why might the *same* data vector deserve different coordinates for different purposes? Give a data example (units, scaling, or otherwise).

### Python Practice

16. Verify Exercises 5–9 in NumPy. For Exercise 9, solve for $c$ numerically by computing $\|\langle 2,-1,2\rangle\|$ first.
17. Generate 10 random points in $\mathbb{R}^5$ with `rng.normal(size=(10, 5))`, and write a function `nearest(points, x)` returning the row nearest to a query vector `x` in Euclidean distance (use `np.linalg.norm(points - x, axis=1)` — note the broadcasting, and note `axis=1`). You have implemented the core of $k$-nearest-neighbors for $k=1$.

### Visualization Practice

18. Recreate {numref}`fig-vector-operations`'s left panel for your own choice of $\vb u, \vb v$, drawing both diagonals of the parallelogram and labeling them $\vb u + \vb v$ and $\vb u - \vb v$.
19. Plot the *unit circle's worth of directions* $\{\langle\cos\theta, \sin\theta\rangle\}$ as 24 arrows from the origin, then overlay the same 24 directions scaled by $2 + \cos 3\theta$. The result is a first **vector-valued function** picture; describe the pattern you see. *(Chapter 21 makes this a definition.)*

### Challenge

20. Prove algebraically, for $\mathbb{R}^n$, that $\|\vb u + \vb v\|^2 + \|\vb u - \vb v\|^2 = 2\|\vb u\|^2 + 2\|\vb v\|^2$ (the **parallelogram law**: the diagonals' squared lengths sum to the sides'). Expand the squared norms componentwise and watch the cross terms cancel — then keep those cross terms $\sum u_iv_i$ in view: they are the star of the next chapter.
21. **Centroids.** For data vectors $\vb x_1, \ldots, \vb x_m$, the mean vector is $\bar{\vb x} = \frac1m\sum\vb x_i$. Show that $\bar{\vb x}$ minimizes the total squared distance $f(\vb c) = \sum_i\|\vb x_i - \vb c\|^2$ — one dimension at a time, using Chapter 4's derivative to minimize each coordinate separately. *(You have just proved why "the average" is the least-squares summary of a cloud of points, and why $k$-means clustering computes centroids.)*

### Cumulative Review

22. *(Ch. 6)* The magnitude function along a parametrized ray, $g(t) = \|t\,\langle 3, 4\rangle - \langle 0, 5\rangle\|^2 = 25t^2 - 40t + 25$, measures squared distance from the point $(0,5)$ to points on the ray. Minimize it with Chapter 4's tools; the minimizing $t$ gives the nearest point. *(Chapter 16 will redo this in one line as a projection.)*
23. *(Ch. 13)* The magnitude $\|\langle 1, t, t^2/2\rangle\|$ for small $t$ is $\sqrt{1 + t^2 + t^4/4}$. Use the binomial series $(1+u)^{1/2} \approx 1 + \frac u2$ to approximate it to second order in $t$.

## 15.8 Summary

A vector is an ordered list of numbers *and* an arrow with direction and length — the algebraic and geometric views of one object, connected by drawing the arrow from the origin. Two componentwise operations generate everything: addition (tip-to-tail, or parallelogram diagonal) and scalar multiplication (stretch, shrink, flip), combining into linear combinations, the subject's master construction. Magnitude $\|\vb v\| = \sqrt{\sum v_i^2}$ extends Pythagoras to any dimension; dividing by it yields the unit vector $\hat{\vb v}$, splitting every vector into length times direction; the standard basis $\vb i, \vb j, \vb k$ exposes components as coefficients. Points, displacements ($Q - P$), and distances transfer intact from $\mathbb{R}^2$ to $\mathbb{R}^3$ to $\mathbb{R}^n$, where drawings fail but formulas do not — which is exactly what lets geometry organize high-dimensional data. In NumPy, vectors are arrays, the operations are ordinary arithmetic, and shape-checking is the first discipline. Missing still: multiplication and angles — the next chapter's dot and cross products.

*Parallel reading:* OpenStax *Calculus Volume 3*, Sections 2.1–2.2 {cite}`openstax_calc3`; Goodfellow et al., §2.1 {cite}`goodfellow_linalg`.
