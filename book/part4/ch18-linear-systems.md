# Chapter 18 · Linear Systems and Gauss–Jordan Elimination

The central computational problem of linear algebra is disarmingly plain: solve

$$
\mathit A\,\vb x = \vb b
$$

— find the input $\vb x$ that the machine $\mathit A$ sends to the output $\vb b$. Fitting a curve through data points, balancing a chemical equation, finding equilibrium prices, inverting a transformation, computing regression coefficients: all are this problem wearing different clothes. This chapter develops the algorithm that solves it — **Gauss–Jordan elimination** — together with the geometry of what solutions look like (one, none, or infinitely many), and the notion of an inverse matrix, including the crucial practical advice about when *not* to compute one.

## 18.1 Two pictures of one system

The system

$$
\begin{aligned}
x + 2y &= 5\\
3x - y &= 1
\end{aligned}
\qquad\text{i.e.}\qquad
\underbrace{\begin{bmatrix}1 & 2\\ 3 & -1\end{bmatrix}}_{\mathit A}
\begin{bmatrix}x\\ y\end{bmatrix} =
\underbrace{\begin{bmatrix}5\\ 1\end{bmatrix}}_{\vb b}
$$

can be read through either lens from Chapter 17. The **row picture**: each equation is a line, and solving means finding where all the lines meet. The **column picture**: by the column reading of $\mathit A\vb x$, the system asks for the *linear combination of the columns that produces $\vb b$*:

$$
x\begin{bmatrix}1\\3\end{bmatrix} + y\begin{bmatrix}2\\-1\end{bmatrix} = \begin{bmatrix}5\\1\end{bmatrix}.
$$

```{figure} figures/ch18-row-column-picture.png
:name: fig-row-column-picture
:alt: Left: two lines crossing at the point one comma two. Right: the two column vectors of the matrix and the target vector b, with a dashed construction showing one of the first column plus two of the second reaching b.

One system, two pictures. Left (rows): the lines $x + 2y = 5$ and $3x - y = 1$ intersect at $(1, 2)$. Right (columns): one unit of $\vb a_1 = \langle 1,3\rangle$ plus two units of $\vb a_2 = \langle 2,-1\rangle$ lands exactly on $\vb b = \langle 5,1\rangle$. The solution $(1,2)$ is simultaneously an intersection point and a recipe.
```

Both pictures generalize — in $\mathbb{R}^3$ the rows are planes intersecting (generically) in a point, and the columns are three vectors to combine — and both predict the same trichotomy of outcomes. Lines (or planes) in general position meet in **exactly one** point; parallel-and-distinct ones meet in **none**; coincident ones share **infinitely many**. In column language: $\vb b$ is reachable in one way, unreachable, or reachable in many ways. There is no fourth case for linear systems — never "exactly two solutions" — because if $\vb x_1 \ne \vb x_2$ both solve the system, so does every point $(1-t)\vb x_1 + t\vb x_2$ on the line through them (linearity; check it), yielding infinitely many at once.

## 18.2 Elimination: the algorithm

The strategy is old, systematic, and beautiful: replace the system by an *equivalent* one — same solutions — whose shape makes the answer readable. Three **elementary row operations** provably preserve the solution set:

1. swap two equations (rows);
2. multiply an equation (row) by a nonzero constant;
3. add a multiple of one equation (row) to another.

Bookkeeping is lightened by the **augmented matrix** $[\mathit A \mid \vb b\,]$, carrying coefficients and right-hand side together. The algorithm — *Gaussian elimination* — marches column by column, using row operations to create zeros below each **pivot** (the leading nonzero entry of a row), producing a staircase (**row echelon**) form solvable by back-substitution. Continuing to clear *above* each pivot as well, and scaling pivots to $1$, yields the **reduced row echelon form** (RREF), where solutions can simply be read off — that extension is the *Gauss–Jordan* variant.

```{prf:example} A 3×3 system, start to finish
:label: ex-gauss-jordan
Solve
$\;\begin{aligned}x + y + z &= 6\\ 2x - y + z &= 3\\ x + 2y + 3z &= 14.\end{aligned}$

Augment and eliminate downward. Pivot 1 is the top-left $1$; clear below it with $R_2 \leftarrow R_2 - 2R_1$ and $R_3 \leftarrow R_3 - R_1$:

$$
\left[\begin{array}{ccc|c}1 & 1 & 1 & 6\\ 2 & -1 & 1 & 3\\ 1 & 2 & 3 & 14\end{array}\right]
\;\longrightarrow\;
\left[\begin{array}{ccc|c}1 & 1 & 1 & 6\\ 0 & -3 & -1 & -9\\ 0 & 1 & 2 & 8\end{array}\right].
$$

Pivot 2: the $-3$. Clear below with $R_3 \leftarrow R_3 + \tfrac13 R_2$:

$$
\left[\begin{array}{ccc|c}1 & 1 & 1 & 6\\ 0 & -3 & -1 & -9\\ 0 & 0 & \tfrac53 & 5\end{array}\right]
\qquad\text{(row echelon form reached).}
$$

**Back-substitute:** row 3 gives $\tfrac53 z = 5 \Rightarrow z = 3$; row 2 gives $-3y - 3 = -9 \Rightarrow y = 2$; row 1 gives $x = 6 - 2 - 3 = 1$. Solution $\vb x = (1, 2, 3)$.

*Gauss–Jordan finish (alternative to back-substitution):* scale the pivots to $1$ ($R_2 \leftarrow -\tfrac13R_2$, $R_3 \leftarrow \tfrac35 R_3$) and clear upward, ending at

$$
\left[\begin{array}{ccc|c}1 & 0 & 0 & 1\\ 0 & 1 & 0 & 2\\ 0 & 0 & 1 & 3\end{array}\right],
$$

where the answer sits in the last column. **Always verify:** $\mathit A(1,2,3) = (6, 3, 14)$ ✓ — one matrix–vector product, and elimination's every step is insured.
```

```{prf:example} The singular cases
:label: ex-singular-cases
**(a) No solution.** For $\begin{aligned}x + y &= 2\\ 2x + 2y &= 5\end{aligned}$, eliminating gives $R_2 - 2R_1$: $\ 0 = 1$ — a contradiction. The rows are parallel distinct lines; the second column-picture vector is a multiple of the first, and $\vb b$ lies off their common line: unreachable. The system is **inconsistent**, flagged by a row $[\,0\ \cdots\ 0 \mid c\,]$ with $c \ne 0$.

**(b) Infinitely many.** For $\begin{aligned}x + y - z &= 4\\ 2x - y + z &= 2\end{aligned}$: adding the equations gives $3x = 6$, $x = 2$, and the first equation then says $y - z = 2$ with nothing to pin down $z$. Variables without pivots are **free**; set $z = t$ and read the rest in terms of it:

$$
\vb x = (2,\ 2 + t,\ t) = (2, 2, 0) + t\,(0, 1, 1), \qquad t \in \mathbb{R}
$$

— a *line* of solutions: one particular solution plus arbitrary multiples of a direction. Underdetermined systems (more unknowns than independent equations) always resolve this way: particular + free directions, a structure that recurs from differential equations to the null spaces of machine learning's overparametrized models.
```

The bookkeeping quantity that classifies all outcomes is the **rank**: the number of pivots elimination finds. For an $n$-unknown system, rank $n$ with no contradiction row means a unique solution; a contradiction row means none; rank $< n$ without contradiction means $n - \text{rank}$ free variables' worth of solutions. Rank is also the honest measure of how much *independent information* the equations (or a data matrix's columns) contain — two equations that say the same thing count once.

## 18.3 Inverse matrices

For square $\mathit A$, the **inverse** $\mathit A^{-1}$, *when it exists*, is the matrix undoing $\mathit A$'s transformation:

$$
\mathit A^{-1}\mathit A = \mathit A\mathit A^{-1} = \mathit I,
$$

whereupon $\mathit A\vb x = \vb b$ solves formally as $\vb x = \mathit A^{-1}\vb b$. A square matrix with an inverse is **invertible** (nonsingular); the machines that cannot be undone — those collapsing some direction to zero, like Chapter 17's projection — are **singular**, and they are exactly the matrices for which elimination comes up short of full rank (and, next chapter, exactly those with determinant zero).

For $2\times2$ matrices the inverse has a closed form worth memorizing:

$$
\begin{bmatrix}a & b\\ c & d\end{bmatrix}^{-1} = \frac{1}{ad - bc}\begin{bmatrix}d & -b\\ -c & a\end{bmatrix},
\qquad\text{provided } ad - bc \neq 0
$$

— swap the diagonal, negate the off-diagonal, divide by $ad - bc$ (a first sighting of the determinant). For the system of §18.1, $\mathit A = \begin{bmatrix}1&2\\3&-1\end{bmatrix}$ has $ad - bc = -7$, so

$$
\mathit A^{-1} = -\frac17\begin{bmatrix}-1 & -2\\ -3 & 1\end{bmatrix} = \begin{bmatrix}\tfrac17 & \tfrac27\\[2pt] \tfrac37 & -\tfrac17\end{bmatrix},
\qquad
\mathit A^{-1}\begin{bmatrix}5\\1\end{bmatrix} = \begin{bmatrix}\tfrac57 + \tfrac27\\[2pt] \tfrac{15}7 - \tfrac17\end{bmatrix} = \begin{bmatrix}1\\2\end{bmatrix} \checkmark
$$

For larger matrices, Gauss–Jordan computes inverses wholesale: augment with the identity and reduce — $[\,\mathit A \mid \mathit I\,] \to [\,\mathit I \mid \mathit A^{-1}\,]$ — since the operations turning $\mathit A$ into $\mathit I$, applied to $\mathit I$, accumulate exactly $\mathit A^{-1}$ (Exercise 12 walks one through). Useful algebra: $(\mathit{AB})^{-1} = \mathit B^{-1}\mathit A^{-1}$ (undo in reverse order, like the transpose rule and for the same reason) and $(\mathit A^{\mathsf T})^{-1} = (\mathit A^{-1})^{\mathsf T}$.

One point of professional practice, stated early and firmly: **in computation, solving a system does not mean forming an inverse.** `np.linalg.solve(A, b)` runs elimination (an LU factorization) directly — faster and more numerically accurate than computing $\mathit A^{-1}$ and multiplying. The inverse is a superb *concept* (proofs, formulas, reasoning) and a mediocre *algorithm*; reach for `inv` only when the inverse's entries are themselves the object of interest.

## 18.4 Common mistakes

```{admonition} Common Mistakes
:class: warning
**Illegal row operations.** Only the three elementary operations preserve solutions. Multiplying a row by zero destroys an equation; adding a constant (not a multiple of a row) to a row changes the system; column operations change the *variables*.

**Arithmetic drift.** Elimination is long arithmetic; one slip poisons everything downstream. Antidote (nonnegotiable): substitute the final answer into the *original* system.

**Misreading the singular flags.** $[\,0\ 0\ 0 \mid 5\,]$ means *no* solution; $[\,0\ 0\ 0\mid 0\,]$ means a redundant equation and likely *free variables* — opposite verdicts from similar-looking rows.

**Forgetting free variables.** Rank $2$ with $3$ unknowns is not "solved" at two pivot values; the answer is a parametrized family, written as particular + $t\,($direction$)$.

**Dividing by matrices.** There is no $\vb b/\mathit A$; there is $\mathit A^{-1}\vb b$ when $\mathit A^{-1}$ exists — and order matters: $\vb b\,\mathit A^{-1}$ is a shape error or a different object.

**`inv` in production.** Solving via explicit inverses is slower and less accurate; use `solve`. And check `np.linalg.matrix_rank` or condition warnings before trusting answers from nearly singular systems.
```

## 18.5 Now do it in Python

SymPy shows the algorithm's exact steps; NumPy executes the industrial version {cite}`meurer2017sympy,harris2020numpy`.

```python
import numpy as np
import sympy as sp

# --- Example 18.1: exact RREF, watching Gauss-Jordan finish ---
M = sp.Matrix([[1, 1, 1, 6],
               [2, -1, 1, 3],
               [1, 2, 3, 14]])
rref, pivots = M.rref()
print(rref)      # [[1,0,0,1],[0,1,0,2],[0,0,1,3]] -> x=(1,2,3)
print(pivots)    # (0, 1, 2): three pivot columns, full rank

# --- The same solve, production style ---
A = np.array([[1.0, 1, 1], [2, -1, 1], [1, 2, 3]])
b = np.array([6.0, 3, 14])
x = np.linalg.solve(A, b)
print(x, np.allclose(A @ x, b))          # [1. 2. 3.]  True

# --- Example 18.2: the singular cases, diagnosed by rank ---
A_bad = np.array([[1.0, 1], [2, 2]])
print(np.linalg.matrix_rank(A_bad))      # 1  (not 2: singular)
M2 = sp.Matrix([[1, 1, -1, 4], [2, -1, 1, 2]])
print(M2.rref())    # ([[1,0,0,2],[0,1,-1,2]], (0,1)): z free, x=2, y=2+z

# --- Inverses: concept vs practice ---
A2 = np.array([[1.0, 2], [3, -1]])
print(np.linalg.inv(A2))                 # [[1/7, 2/7], [3/7, -1/7]]
print(np.linalg.inv(A2) @ np.array([5.0, 1]))    # [1. 2.] -- works, but
print(np.linalg.solve(A2, np.array([5.0, 1])))   # [1. 2.] -- prefer this
```

`sp.Matrix.rref()` is the pedagogical x-ray — exact fractions, pivot columns identified — while `np.linalg.solve` is what runs inside every regression fit and simulation. Try `np.linalg.solve(A_bad, [1, 2])` once, deliberately, to meet the `LinAlgError: Singular matrix` you will otherwise first encounter at a worse moment.

**Visualization and interpretation.** Plot the two lines of §18.1's system and mark $(1,2)$; then perturb to a *nearly* singular system — say slopes $1.00$ and $1.02$ — and watch the intersection shoot far away under a tiny nudge of one intercept. That extreme sensitivity is **ill-conditioning**: systems whose row-picture lines are nearly parallel (columns nearly dependent) amplify small data errors into large answer errors, a phenomenon `np.linalg.cond(A)` quantifies and every applied scientist eventually meets. Well-posed geometry, not just correct algebra, is what makes an answer trustworthy.

```{admonition} Data Science Connection
:class: tip
Fitting a linear regression is solving a linear system: the least-squares weights satisfy the **normal equations** $\mathit X^{\mathsf T}\mathit X\,\vb w = \mathit X^{\mathsf T}\vb y$ — a square system built from the design matrix (recall $\mathit X^{\mathsf T}\mathit X$ from Chapter 17), passed straight to a solver. Rank tells you whether features are redundant (collinear columns ⇒ rank-deficient ⇒ infinitely many equally good $\vb w$: the model is unidentifiable); conditioning tells you whether the fit is numerically stable; and the "particular + free directions" structure of {prf:ref}`ex-singular-cases` is precisely the set of weight vectors an overparametrized model can choose among.
```

```{admonition} Looking Ahead
:class: seealso
Elimination decides invertibility by *running the whole algorithm*; the next chapter compresses that verdict into a single number computed from the entries — the determinant, which also measures the volume scaling of {numref}`fig-matrix-transform` and whose vanishing is the exact boundary between unique solutions and the singular cases.
```

## 18.6 Exercises

### Quick Check

1. Write the system $2x - y = 0$, $x + 3y = 7$ as $\mathit A\vb x = \vb b$ and as a column-combination statement.
2. What does the augmented row $[\,0\ \ 0 \mid 3\,]$ signify? And $[\,0\ \ 0\mid 0\,]$?
3. Solve by the $2\times2$ inverse formula: $\begin{bmatrix}2 & 1\\ 5 & 3\end{bmatrix}\vb x = \begin{bmatrix}1\\ 2\end{bmatrix}$.
4. A $4\times4$ system's elimination yields 3 pivots and no contradiction. Describe the solution set.

````{admonition} Answers to Quick Checks
:class: dropdown
1. $\begin{bmatrix}2&-1\\1&3\end{bmatrix}\vb x = \begin{bmatrix}0\\7\end{bmatrix}$; find $x, y$ with $x\langle2,1\rangle + y\langle-1,3\rangle = \langle0,7\rangle$. (Solution $(1,2)$.)
2. Inconsistent — no solution. / A redundant equation; solutions persist, possibly with freedom.
3. $ad - bc = 1$: $\mathit A^{-1} = \begin{bmatrix}3&-1\\-5&2\end{bmatrix}$, $\vb x = (3 - 2,\ -5 + 4) = (1, -1)$.
4. A one-parameter family (line) in $\mathbb{R}^4$: particular solution plus multiples of one free direction.
````

### Basic Practice

5. Solve by elimination, by hand, verifying in the original system:
   (a) $\begin{aligned}2x + y &= 7\\ x - 3y &= -7\end{aligned}$  (b) $\begin{aligned}x + 2y - z &= 4\\ 2x + y + z &= 5\\ x - y + 3z &= 2\end{aligned}$
6. Classify each system (unique/none/infinite) and give the full solution set where one exists:
   (a) $\begin{aligned}x - y &= 1\\ 2x - 2y &= 2\end{aligned}$  (b) $\begin{aligned}x - y &= 1\\ 2x - 2y &= 3\end{aligned}$  (c) $\begin{aligned}x + y + z &= 1\\ y - z &= 2\end{aligned}$
7. Find $\mathit A^{-1}$ for $\mathit A = \begin{bmatrix}4 & 7\\ 1 & 2\end{bmatrix}$, verify $\mathit A\mathit A^{-1} = \mathit I$, and use it to solve $\mathit A\vb x = \langle 1, 0\rangle$ and $\mathit A\vb x = \langle 0, 1\rangle$. What are those two solutions, as a pair?
8. For what value(s) of $k$ does $\begin{aligned}x + 2y &= 3\\ 2x + ky &= 6\end{aligned}$ have infinitely many solutions? No solution? Exactly one?

````{admonition} Solution to Exercise 8
:class: dropdown
$R_2 - 2R_1$: $[\,0\ \ k - 4 \mid 0\,]$. If $k \ne 4$: pivot in column 2, unique solution. If $k = 4$: the row is all zeros — the second equation was twice the first — leaving one equation, one free variable: infinitely many, $\vb x = (3 - 2t,\ t)$. *No* value of $k$ gives inconsistency here, because the right-hand sides were proportional too ($6 = 2\cdot3$); changing $6$ to $7$ would make $k = 4$ inconsistent instead.
````

### Intermediate Practice

9. Solve the $3\times3$ system of Exercise 5(b) again via SymPy's `rref` and identify each elementary operation the by-hand solution used.
10. **Curve fitting is a linear system.** Find the parabola $y = a + bx + cx^2$ through $(1, 2)$, $(2, 3)$, $(3, 6)$: write the three interpolation conditions as a system in $(a, b, c)$ and solve. *(The coefficient matrix, with rows $(1, x_i, x_i^2)$, is a Vandermonde matrix — the standard bridge from fitting problems to linear algebra.)*
11. Balance the combustion reaction $\mathrm{C_3H_8} + \mathrm{O_2} \to \mathrm{CO_2} + \mathrm{H_2O}$ by setting up conservation equations for C, H, O in the four unknown coefficients and solving; the one-parameter solution family, scaled to smallest whole numbers, is the balanced equation.
12. Compute the inverse of $\mathit A = \begin{bmatrix}1 & 1 & 1\\ 2 & -1 & 1\\ 1 & 2 & 3\end{bmatrix}$ (the matrix of {prf:ref}`ex-gauss-jordan`) by Gauss–Jordan on $[\,\mathit A\mid\mathit I\,]$, and check $\mathit A^{-1}(6, 3, 14) = (1,2,3)$.
13. Prove that if $\mathit A$ and $\mathit B$ are invertible then so is $\mathit{AB}$, with $(\mathit{AB})^{-1} = \mathit B^{-1}\mathit A^{-1}$, by multiplying out both orders. Then exhibit $2\times2$ matrices showing that $\mathit A + \mathit B$ invertible does *not* follow from $\mathit A, \mathit B$ invertible.

### Conceptual Understanding

14. Explain, in the column picture, what goes wrong in {prf:ref}`ex-singular-cases`(a): where do the columns of that coefficient matrix live, and where is $\vb b$?
15. Why can a linear system never have exactly two solutions? Give the one-line linearity argument from §18.1 in your own words, and state what it implies about the *shape* of any solution set (point, line, plane, …).
16. Your regression software reports that $\mathit X^{\mathsf T}\mathit X$ is singular. Translate into statements about (a) the columns of $\mathit X$, i.e. the features, and (b) the uniqueness of the fitted weights. What might a practitioner do about it?

### Python Practice

17. Verify Exercises 5–12 with `np.linalg.solve`/`sp.Matrix.rref` as appropriate. For 10, also fit with `np.polyfit(x, y, 2)` and reconcile coefficient ordering.
18. Build the $12\times12$ Hilbert matrix $h_{ij} = \frac{1}{i + j - 1}$, and solve $\mathit H\vb x = \mathit H\mathbf{1}$ (right-hand side chosen so the true answer is all ones). Report `np.linalg.cond(H)` and the worst error in your computed solution. Ill-conditioning, experienced firsthand.

### Visualization Practice

19. Plot the row pictures of Exercise 6(a)–(b): coincident lines versus parallel lines. Then plot §18.5's near-singular pair and the solution's jump under a $1\%$ intercept perturbation, annotating both intersection points.
20. For the free-variable system of {prf:ref}`ex-singular-cases`(b), plot the solution line $(2, 2+t, t)$ in 3-D along with the two constraint planes, confirming visually that the line is their intersection.

### Challenge

21. **Operation counting.** Show that eliminating an $n\times n$ system costs about $\frac{n^3}{3}$ multiplications (sum the work per pivot column), while *each additional right-hand side* costs only about $n^2$. Conclude why factoring once and reusing (as `solve` does via LU) beats re-eliminating, and why computing $\mathit A^{-1}$ (equivalent to $n$ right-hand sides) to solve *one* system wastes a factor of about $3$.
22. **Leontief input–output model.** An economy's sectors consume each other's output per unit produced according to $\mathit C = \begin{bmatrix}0.2 & 0.3\\ 0.4 & 0.1\end{bmatrix}$; external demand is $\vb d = \langle 100, 120\rangle$. Total production must satisfy $\vb x = \mathit C\vb x + \vb d$, i.e. $(\mathit I - \mathit C)\vb x = \vb d$. Solve for $\vb x$; then verify numerically that $(\mathit I - \mathit C)^{-1} = \mathit I + \mathit C + \mathit C^2 + \cdots$ by summing 50 terms — a matrix geometric series (Chapter 12's formula, grown up), convergent because $\mathit C$'s entries drain rather than amplify.

### Cumulative Review

23. *(Ch. 17)* For the shear $\mathit S = \begin{bmatrix}1&1\\0&1\end{bmatrix}$, guess $\mathit S^{-1}$ from the transformation's meaning (shear back), verify by multiplication, and reconcile with the $2\times2$ formula.
24. *(Ch. 6)* Newton's method in Chapter 6 divided by $f'(x_n)$. Its many-variable descendant solves the *linear system* $\mathit J\,\Delta\vb x = -\vb f(\vb x_n)$ at each step, where $\mathit J$ collects partial derivatives (Chapter 22). In one sentence each: what plays the role of $f'$, and why does "divide" become "solve"?

## 18.7 Summary

$\mathit A\vb x = \vb b$ reads as intersecting rows or as combining columns, and its solution set is always a point, nothing, or an infinite affine family — never anything in between. Gauss–Jordan elimination reaches the answer by three solution-preserving row operations on the augmented matrix: create pivots, zero below (echelon form, then back-substitute) or below *and* above (RREF, read off directly). Contradiction rows flag inconsistency; pivotless columns flag free variables, with solutions written as particular + span of directions; the pivot count — the rank — measures the system's independent information. Square matrices with full rank are invertible ($\mathit A^{-1}\mathit A = \mathit I$; $2\times2$ by the $ad-bc$ formula, general by $[\,\mathit A\mid\mathit I\,]$ reduction; $(\mathit{AB})^{-1} = \mathit B^{-1}\mathit A^{-1}$), but computational practice solves systems by elimination (`np.linalg.solve`), not by inverses, and watches conditioning where columns are nearly dependent. Regression's normal equations, interpolation, and equilibrium models are all this one problem; the determinant, next, is invertibility distilled to a single number.

*Parallel reading:* Strang {cite}`strang_linalg`, Chapters 2–3; Goodfellow et al., §2.3–2.4 {cite}`goodfellow_linalg`.
