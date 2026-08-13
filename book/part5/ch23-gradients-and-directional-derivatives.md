# Chapter 23 · Gradients and Directional Derivatives

Partial derivatives answered "how steep is the terrain walking due east? due north?" — two directions out of infinitely many. This chapter answers all the rest at once, with a single vector: the **gradient** $\nabla f$, whose dot product with any unit direction prices the slope that way. Out of that one formula falls the chapter's headline geometry — the gradient points *straight uphill*, perpendicular to the contours, with magnitude the steepest available rate — and out of the geometry falls the most consequential algorithm in modern computing: to minimize a function, walk against its gradient. This is the chapter where the course's calculus and linear algebra finally run as one machine.

## 23.1 The gradient vector

```{prf:definition} Gradient
:label: def-gradient
The **gradient** of $f$ is the vector of its partial derivatives:

$$
\nabla f(x, y) = \bigl\langle f_x(x,y),\ f_y(x,y)\bigr\rangle,
\qquad
\nabla f(\vb x) = \Bigl\langle \frac{\partial f}{\partial x_1}, \ldots, \frac{\partial f}{\partial x_n}\Bigr\rangle
$$

— a vector *field*: at each point of the domain, one arrow. (Pronounced "grad $f$"; the symbol $\nabla$ is "nabla" or "del.")
```

For the running example $f(x,y) = x^2 + 2y^2$ (an elliptical bowl — contours are ellipses, twice as squeezed in $y$): $\nabla f = \langle 2x, 4y\rangle$. At $(1, 1)$ the arrow is $\langle 2, 4\rangle$; at the bottom of the bowl, $\nabla f(0,0) = \vb 0$. {numref}`fig-gradient-field` plots the whole field over the contour map, and the two facts that leap from the picture — arrows perpendicular to contours, arrows pointing uphill — are theorems within the page.

```{figure} figures/ch23-gradient-field.png
:name: fig-gradient-field
:alt: Contour ellipses of the function x squared plus two y squared, overlaid with a grid of red arrows that everywhere cross the contours at right angles, pointing away from the center.

The gradient field of $f = x^2 + 2y^2$ over its contours. Every arrow crosses its contour at a right angle and points toward higher levels — steepest ascent, everywhere. A ball rolling downhill, or an optimizer minimizing a loss, follows these arrows *backwards*.
```

## 23.2 Directional derivatives

Fix a point $\vb p$ and a **unit** direction $\vb u$. Walking from $\vb p$ along $\vb u$ traces the line $\vb r(t) = \vb p + t\vb u$ (Chapter 21), and the function's value along the walk is $g(t) = f(\vb r(t))$. Its rate at the start is *the slope of $f$ in the direction $\vb u$*:

```{prf:definition} Directional derivative
:label: def-directional
$$
D_{\vb u} f(\vb p) = \frac{d}{dt}\,f(\vb p + t\vb u)\Big|_{t = 0}.
$$
```

Chapter 22's chain rule evaluates it instantly: with $x' = u_1$ and $y' = u_2$ along the line,

$$
D_{\vb u} f = f_x\,u_1 + f_y\,u_2,
$$

which is exactly a dot product:

```{prf:theorem} Gradient form of the directional derivative
:label: thm-directional-gradient
For unit $\vb u$:

$$
D_{\vb u} f(\vb p) = \nabla f(\vb p)\cdot\vb u.
$$
```

One vector, computed once, now answers every direction by dotting — and Chapter 16's angle formula reads the answer's structure out loud. Since $\nabla f\cdot\vb u = \|\nabla f\|\cos\theta$ ($\vb u$ being unit), where $\theta$ is the angle between the chosen direction and the gradient:

```{prf:theorem} The gradient's geometry
:label: thm-gradient-geometry
At any point where $\nabla f \ne \vb 0$:

1. **Steepest ascent:** $D_{\vb u}f$ is maximized when $\vb u$ points along $\nabla f$ ($\theta = 0$), with maximal rate $\|\nabla f\|$.
2. **Steepest descent:** minimized along $-\nabla f$, with rate $-\|\nabla f\|$.
3. **Level directions:** $D_{\vb u}f = 0$ exactly when $\vb u \perp \nabla f$ — so the gradient is **perpendicular to the level curve** through the point (moving along a contour changes nothing, and those no-change directions are precisely the orthogonal complement of $\nabla f$).
```

The three statements are one $\cos\theta$ dial, read at $0°$, $180°$, and $90°$ — {numref}`fig-gradient-field` in equation form.

```{prf:example} A full gradient workup
:label: ex-directional
For $f(x, y) = x^2 y$ at the point $(2, 1)$: find the rate of change toward the point $(5, 5)$; the direction and rate of steepest ascent; and one direction of zero change.

**Gradient:** $\nabla f = \langle 2xy,\ x^2\rangle$, so $\nabla f(2,1) = \langle 4, 4\rangle$.

**Toward $(5,5)$:** the displacement is $\langle 3, 4\rangle$, normalized (nonnegotiable) $\vb u = \langle \tfrac35, \tfrac45\rangle$:

$$
D_{\vb u}f = \langle 4,4\rangle\cdot\langle\tfrac35, \tfrac45\rangle = \frac{12 + 16}{5} = 5.6.
$$

**Steepest ascent:** along $\hat{\nabla f} = \frac{1}{\sqrt2}\langle 1, 1\rangle$, at rate $\|\nabla f\| = \sqrt{32} \approx 5.657$. (Sanity check: $5.6 < 5.657$ — the chosen direction, at a small angle to the gradient, captures almost the full rate. Any $D_{\vb u}f$ exceeding $\|\nabla f\|$ signals an unnormalized $\vb u$.)

**Zero change:** any unit vector orthogonal to $\langle 4,4\rangle$, e.g. $\frac{1}{\sqrt2}\langle 1, -1\rangle$ — the tangent direction of the level curve $x^2y = 4$ passing through $(2,1)$.
```

The perpendicularity of gradients and level sets is a workhorse in its own right: in three variables, $\nabla F$ at a point of the level *surface* $F(x,y,z) = c$ is that surface's **normal vector**, from which tangent planes to arbitrary surfaces follow by Chapter 16's Exercise 10 recipe (Exercise 10 below).

## 23.3 Critical points and the second-derivative test

Where can a smooth function attain a local maximum or minimum? Only where no direction goes uphill and none downhill — where every directional derivative vanishes, i.e.

$$
\nabla f = \vb 0 \qquad(\textbf{critical point}).
$$

As in Chapter 4, the condition is necessary, not sufficient: bowls (minima), domes (maxima), and — new in two dimensions — *saddles* all zero the gradient. The classifier is the second-order information, and Chapter 22's symmetric Hessian $\mathit H = \begin{bmatrix}f_{xx} & f_{xy}\\ f_{xy} & f_{yy}\end{bmatrix}$ is exactly built for the job: near a critical point, $f \approx f(\vb p) + \tfrac12\vb h^{\mathsf T}\mathit H\vb h$ (Chapter 22, Exercise 24), and the quadratic's shape is governed by $\mathit H$'s **eigenvalues** (real, with orthogonal eigenvectors, by the spectral theorem — the promised payoff of Chapter 20):

```{prf:theorem} Second-derivative test
:label: thm-second-derivative-test
At a critical point with Hessian eigenvalues $\lambda_1, \lambda_2$:

- both $\lambda_i > 0$: **local minimum** (bowl — curving up in every direction);
- both $\lambda_i < 0$: **local maximum** (dome);
- opposite signs: **saddle** (up along one eigenvector, down along the other);
- any $\lambda_i = 0$: the test is inconclusive.

Equivalent $2\times2$ shortcut, using $\det\mathit H = \lambda_1\lambda_2$ and $f_{xx}$: $\det\mathit H > 0$ with $f_{xx} > 0$ (min) or $f_{xx} < 0$ (max); $\det \mathit H < 0$ (saddle).
```

```{prf:example} Classifying critical points
:label: ex-critical-points
Find and classify the critical points of $f(x,y) = x^3 - 3x + y^2$.

$\nabla f = \langle 3x^2 - 3,\ 2y\rangle = \vb 0$ requires $x = \pm 1$, $y = 0$: two critical points. The Hessian is $\begin{bmatrix}6x & 0\\ 0 & 2\end{bmatrix}$ — already diagonal, eigenvalues on display.

At $(1, 0)$: eigenvalues $6, 2$, both positive — **local minimum**, value $f = -2$.
At $(-1, 0)$: eigenvalues $-6, 2$, mixed — **saddle**.

The eigenvector reading adds texture at the minimum: the bowl curves three times harder along $x$ (eigenvalue $6$) than along $y$ (eigenvalue $2$) — contours there are ellipses squeezed along $x$. That anisotropy, quantified by the eigenvalue ratio, is about to matter enormously.
```

## 23.4 Gradient descent

Theorem {prf:ref}`thm-gradient-geometry` is an algorithm waiting to be run: from any point, the direction $-\nabla f$ loses altitude fastest, so *step that way, repeatedly*:

$$
\vb x_{k+1} = \vb x_k - \eta\,\nabla f(\vb x_k),
$$

with **learning rate** $\eta > 0$ setting the stride. This is **gradient descent** — the method by which essentially all of machine learning fits its models, since "training" means minimizing a loss function of the parameters, and for millions of parameters the gradient (computed by backpropagation, i.e. the chain rule) is the only affordable compass.

Its behavior on the running bowl $f = x^2 + 2y^2$ is completely transparent, because the update decouples: $\nabla f = \langle 2x, 4y\rangle$ gives

$$
x_{k+1} = (1 - 2\eta)\,x_k, \qquad y_{k+1} = (1 - 4\eta)\,y_k
$$

— two geometric sequences (Chapter 12). Convergence demands both factors inside $(-1, 1)$: $\eta < \tfrac12$, with the *stiffer* coordinate ($y$, curvature $4$) setting the ceiling. Choose $\eta = 0.1$: the $y$-error shrinks by $0.6$ per step, the $x$-error only by $0.8$ — the iterate swiftly drops to the valley floor of the ellipse, then crawls along it. In eigen-language: the convergence factors are $1 - \eta\lambda_i$ for the Hessian's eigenvalues $\lambda_i$, the usable $\eta$ is capped by $\lambda_{\max}$, the slowest error mode decays at the rate set by $\lambda_{\min}$, and the ratio $\kappa = \lambda_{\max}/\lambda_{\min}$ — the **condition number** — governs the total effort. Everything practitioners experience as "training is slow and zigzags" is this paragraph; everything called *preconditioning*, *feature scaling*, or *adaptive optimizers* is engineering to shrink $\kappa$'s effect. Chapters 12, 20, 22, and 23 in one loop.

## 23.5 Common mistakes

```{admonition} Common Mistakes
:class: warning
**Unnormalized directions.** $D_{\vb u}f = \nabla f\cdot\vb u$ *requires unit* $\vb u$; feeding a raw displacement scales the answer by its length. Symptom: a "directional derivative" exceeding $\|\nabla f\|$.

**Gradient as a location.** $\nabla f(\vb p)$ is a direction *attached at $\vb p$*, not a point to move to; and it lives in the *domain* (input space), not on the surface.

**"The gradient points toward the maximum."** It points in the locally steepest uphill direction — which, in a curved landscape, need not aim at any maximum at all (follow the field in {numref}`fig-gradient-field`: the arrows bend). Gradient descent's path is a curve, not a beeline.

**Critical point = extremum.** Saddles also zero the gradient; classify with the Hessian, and remember the test can be inconclusive (eigenvalue zero).

**Sign slips in descent.** *Minimizing* steps along $-\nabla f$; a dropped minus sign performs enthusiastic gradient *ascent*. (Both are useful; only one is intended.)

**Learning-rate faith.** Too large diverges (factor $|1 - \eta\lambda| > 1$), too small crawls; neither failure is subtle in a loss-versus-iteration plot, so always draw one.
```

## 23.6 Now do it in Python

```python
import numpy as np
import sympy as sp

# --- Example 23.5 symbolically ---
x, y = sp.symbols('x y')
f = x**2*y
grad = sp.Matrix([sp.diff(f, x), sp.diff(f, y)])
g_at = np.array(grad.subs({x: 2, y: 1}), dtype=float).ravel()
print(g_at)                            # [4. 4.]
u = np.array([3.0, 4.0]) / 5
print(g_at @ u, np.linalg.norm(g_at))  # 5.6   5.6568...

# --- Gradient descent on the running bowl ---
grad_f = lambda p: np.array([2*p[0], 4*p[1]])
p = np.array([2.0, 1.0])
eta = 0.1
trail = [p.copy()]
for _ in range(60):
    p = p - eta * grad_f(p)
    trail.append(p.copy())
trail = np.array(trail)
print(trail[[1, 5, 20, 60]])
# step 1: [1.6, 0.6] -> ... -> step 60: ~[3e-6, 5e-14]: y-error long gone,
# x-error (the small-eigenvalue mode) still dying at rate 0.8 per step
```

Try $\eta = 0.45$ (the $y$-coordinate oscillates, factor $1 - 4\eta = -0.8$), then $\eta = 0.55$ (divergence: $|1-4\eta| > 1$) — the theory of §23.4, watched live. And verify any symbolic gradient with Chapter 22's `grad_numeric`: agreement between the analytic and finite-difference gradients is the standard test (called a *gradient check*) for backpropagation code.

**Visualization and interpretation.** Overlay `trail` on the contour map of $f$:

```python
import matplotlib.pyplot as plt
xs = np.linspace(-2.2, 2.2, 200)
X, Y = np.meshgrid(xs, xs)
fig, ax = plt.subplots()
ax.contour(X, Y, X**2 + 2*Y**2, levels=15)
ax.plot(*trail.T, "o-", ms=3, color="tab:red")
ax.set_aspect("equal"); plt.show()
```

The path plunges perpendicular to the contours (steepest descent, as designed), reaches the shallow valley quickly in $y$, then inches along the flat direction — the anisotropy of {prf:ref}`ex-critical-points` made kinetic. Repeat on the saddle $x^2 - y^2$ from a start slightly off the axis and watch descent *escape* along the negative-eigenvalue direction: saddles repel descent, one reason high-dimensional optimization works better than early pessimism predicted.

```{admonition} Data Science Connection
:class: tip
This chapter is the mathematical core of model training. The loss $L(\vb w)$ is a function of millions of parameters; backpropagation is the chain rule computing $\nabla L$; the optimizer steps $\vb w \leftarrow \vb w - \eta\nabla L$ (stochastic gradient descent estimates $\nabla L$ from mini-batches; momentum and Adam reshape the step); the learning rate is $\eta$; loss-landscape plots are contour maps; and convergence speed is the Hessian eigenvalue story of §23.4 — with feature standardization, batch normalization, and preconditioners all in the business of taming $\kappa = \lambda_{\max}/\lambda_{\min}$. A data scientist who owns {prf:ref}`thm-gradient-geometry` and §23.4 owns the *why* behind a large fraction of the field's daily vocabulary.
```

```{admonition} Looking Ahead
:class: seealso
Differentiation in several variables is now complete: partials, gradients, directions, optimization. Integration's turn — Chapter 24 sums $f(x,y)$ over two-dimensional regions (volumes, averages, probabilities), and Chapter 25 changes coordinates under the integral, with Chapter 19's determinant pricing the area distortion.
```

## 23.7 Exercises

### Quick Check

1. Compute $\nabla f$ for $f(x,y) = 3x^2 + xy^3$ and evaluate at $(1, 2)$.
2. At a point where $\nabla f = \langle -3, 4\rangle$: what is the steepest-ascent rate? The steepest-descent direction (unit vector)?
3. What is $D_{\vb u}f$ along a direction tangent to a level curve?
4. A critical point has Hessian eigenvalues $5$ and $-2$. Classify it.

````{admonition} Answers to Quick Checks
:class: dropdown
1. $\langle 6x + y^3,\ 3xy^2\rangle$; at $(1,2)$: $\langle 14, 12\rangle$.
2. $\|\nabla f\| = 5$; direction $\langle \tfrac35, -\tfrac45\rangle$.
3. Zero — that is what "level" means, and why $\nabla f \perp$ contours.
4. Saddle (opposite signs).
````

### Basic Practice

5. For $f(x,y) = xe^{y} + y^2$ at $(2, 0)$: compute $\nabla f$, the directional derivative toward $(2, 0) + \langle -1, 1\rangle$ (normalize!), the maximum rate of increase and its direction, and a zero-change direction.
6. Find the equation of the tangent plane to the *level surface* $x^2 + y^2 + z^2 = 14$ at $(1, 2, 3)$, using $\nabla F$ as the normal (Chapter 16's plane recipe). Check that the result matches the geometric fact that a sphere's tangent plane is perpendicular to its radius.
7. Find and classify all critical points: (a) $f = x^2 + y^2 - 4x + 6y$; (b) $f = xy(3 - x - y)$; (c) $f = x^4 + y^4 - 4xy$.
8. For $f = x^2 + 2y^2$, verify at three points of your choosing that $\nabla f$ is perpendicular to the level ellipse through the point (compute the contour's tangent by implicit differentiation, Chapter 5, and dot).

````{admonition} Solution to Exercise 7(a)
:class: dropdown
$\nabla f = \langle 2x - 4,\ 2y + 6\rangle = \vb 0$ at $(2, -3)$ only. Hessian $\operatorname{diag}(2,2)$: both eigenvalues positive — local (indeed global) minimum, $f(2,-3) = -13$. Completing squares confirms: $f = (x-2)^2 + (y+3)^2 - 13$.
````

### Intermediate Practice

9. A hiker stands at $(1, 2)$ on terrain of height $h(x,y) = 100 - 2x^2 - 3y^2$. What direction is steepest ascent, at what grade (rate)? If the hiker walks so as to keep altitude constant, along what direction do they set out? What path shape do they trace overall?
10. Show that for any differentiable $f$ and the curve $\vb r(t)$ following steepest ascent ($\vb r' = \nabla f(\vb r)$), the height $f(\vb r(t))$ is nondecreasing, with $\frac{d}{dt}f(\vb r(t)) = \|\nabla f\|^2$ (chain rule + dot product) — the one-line "why gradient ascent ascends."
11. Do the full §23.4 analysis for $f = 5x^2 + y^2$: Hessian eigenvalues, the exact stability threshold for $\eta$, the per-step factors at $\eta = 0.15$, and the number of steps for the *slow* mode's error to fall below $10^{-6}$ of its start (Chapter 2 logarithms).
12. **Constrained hint of things to come.** Maximize $f(x, y) = xy$ on the circle $x^2 + y^2 = 2$ by parametrizing the circle ($x = \sqrt2\cos t$, $y = \sqrt2\sin t$), reducing to one variable, and optimizing with Chapter 4. Then observe: at your maximizer, $\nabla f$ is parallel to the constraint's gradient $\nabla(x^2+y^2)$ — the pattern behind Lagrange multipliers, which handle such problems without parametrizing.

### Conceptual Understanding

13. Explain why the gradient must be perpendicular to level curves *using only* the directional-derivative formula and the meaning of "level" — no pictures.
14. In $\mathbb{R}^{1000}$, what does it even mean to say "the gradient points uphill," given that no one can see the surface? Which parts of {prf:ref}`thm-gradient-geometry` survive verbatim in high dimension, and why?
15. Two loss surfaces have Hessian eigenvalue ratios $\kappa = 1.5$ and $\kappa = 500$ at their minima. Predict, with reasons, how gradient descent behaves on each, and name one practical intervention for the second case.

### Python Practice

16. Verify Exercises 5–12 (SymPy for gradients and Hessians, `np.linalg.eigh` for classification, a descent loop for 11 — confirm your predicted step count).
17. Implement gradient *ascent* on the terrain of Exercise 9 from four widely spaced starts, overlaying all trails on the contour map. All should converge to the summit at the origin; measure and compare their step counts, and explain any differences via the starting points' gradient magnitudes.

### Visualization Practice

18. Reproduce {numref}`fig-gradient-field` for $f = xe^{-x^2-y^2}$ (a bump-and-dip landscape): contours plus normalized gradient arrows. Mark the two critical points and classify them from the picture before confirming with the Hessian.
19. Plot descent trails on $f = x^2 + 2y^2$ for $\eta \in \{0.05, 0.2, 0.45, 0.55\}$ in a 2×2 grid: smooth convergence, brisk convergence, oscillating convergence, divergence. Title each panel with its $\eta$ and the factors $1 - 2\eta$, $1 - 4\eta$.

### Challenge

20. **Momentum.** Implement gradient descent with momentum, $\vb v_{k+1} = \beta\vb v_k - \eta\nabla f(\vb x_k)$, $\vb x_{k+1} = \vb x_k + \vb v_{k+1}$, on the badly conditioned bowl $f = 50x^2 + y^2$ ($\kappa = 50$... eigenvalues $100$ and $2$). Tune $(\eta, \beta)$ to beat plain descent's best step count to $\|\vb x\| < 10^{-6}$ by at least $5\times$, plot both trails, and describe *how* momentum's trajectory differs (hint: it accumulates velocity along the flat valley while averaging out the oscillation across it).
21. **Newton in optimization.** The update $\vb x_{k+1} = \vb x_k - \mathit H^{-1}\nabla f(\vb x_k)$ (solve, don't invert — Chapter 18) uses curvature to rescale the step. Show that on any quadratic $f = \tfrac12\vb x^{\mathsf T}\mathit A\vb x$ with $\mathit A$ invertible it converges in *one* step from anywhere, verify on $f = 50x^2 + y^2$, and explain in an eigenvalue sentence why Newton is immune to conditioning — and in a cost sentence why ML at scale still prefers gradient methods.

### Cumulative Review

22. *(Ch. 6)* Chapter 6's one-variable Newton found roots of $f'$ to optimize $f$. Show Exercise 21's update reduces exactly to Chapter 6's $x_{k+1} = x_k - f'(x_k)/f''(x_k)$ in one dimension.
23. *(Ch. 16, 20)* At a minimum with Hessian $\mathit H = \begin{bmatrix}3&1\\1&3\end{bmatrix}$ (Chapter 20's Exercise 5(a): eigenvalues $4, 2$, eigenvectors $\langle1,\pm1\rangle$), sketch the local contours: ellipses with axes along the eigenvectors, squeezed along which one? Verify by plotting $\tfrac12\vb h^{\mathsf T}\mathit H\vb h$'s contours.

## 23.8 Summary

The gradient $\nabla f = \langle f_x, f_y, \ldots\rangle$ turns all the partials into one vector field, and the chain rule turns direction-questions into dot products: $D_{\vb u}f = \nabla f\cdot\vb u$ for unit $\vb u$. Chapter 16's angle formula then reads off the geometry — steepest ascent along $\nabla f$ at rate $\|\nabla f\|$, steepest descent opposite, zero change perpendicular, whence gradients cross level curves (and level surfaces) at right angles and supply their normal vectors. Extrema hide among critical points ($\nabla f = \vb 0$), classified by the symmetric Hessian's eigenvalues: all positive a minimum, all negative a maximum, mixed a saddle. Gradient descent operationalizes the geometry — $\vb x \leftarrow \vb x - \eta\nabla f$ — with convergence factors $1 - \eta\lambda_i$ per Hessian eigenmode: stability capped by $\lambda_{\max}$, speed throttled by $\lambda_{\min}$, and the condition number $\kappa$ ruling the experience; this loop, fed by backpropagation's chain rule, is how machine learning trains. In code: symbolic gradients checked against finite differences, descent trails overlaid on contours, and learning-rate pathologies reproduced on demand. Differentiation done; integration over regions is next.

*Parallel reading:* OpenStax *Calculus Volume 3*, Sections 4.6–4.7 {cite}`openstax_calc3`; Goodfellow et al., §4.3 {cite}`goodfellow_linalg`.
