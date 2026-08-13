# Chapter 25 · Polar Coordinates and Change of Variables

The course ends where good mathematics often does: with a change of viewpoint that makes hard things easy. Cartesian coordinates treat the plane as a grid of squares — perfect for rectangles, awkward for anything round: Chapter 24's disk integrals dragged $\sqrt{r^2 - x^2}$ limits through every step. **Polar coordinates** describe points by distance and direction instead, turning disks, rings, and sectors into coordinate rectangles. The price of admission is one factor in the area element — $dA = r\,dr\,d\theta$ — and the deep reason for that factor is a determinant (Chapter 19, taking a bow). The reward is the chapter's finale: the Gaussian integral $\int_{-\infty}^{\infty}e^{-x^2}dx = \sqrt\pi$, unreachable by every one-variable technique in this book, falls in five lines — and with it, the normalizing constant of the normal distribution that all of statistics stands on.

## 25.1 The coordinate system

```{prf:definition} Polar coordinates
:label: def-polar
A point with Cartesian coordinates $(x, y)$ has **polar coordinates** $(r, \theta)$, where $r \ge 0$ is the distance from the origin and $\theta$ the angle from the positive $x$-axis (radians, counterclockwise):

$$
x = r\cos\theta, \qquad y = r\sin\theta;
\qquad\qquad
r = \sqrt{x^2 + y^2}, \qquad \tan\theta = \frac yx
$$

(with $\theta$'s quadrant read from the signs of $x$ and $y$, not blindly from arctangent).
```

The conversion is Chapter 2's unit-circle definition of sine and cosine, promoted to a coordinate system. The coordinate curves swap character: "$r = $ constant" is a circle, "$\theta = $ constant" a ray — the polar grid of {numref}`fig-polar-element` — so regions with circular symmetry become *boxes in $(r,\theta)$*: the disk of radius $R$ is $0 \le r \le R$, $0\le\theta\le2\pi$; an annulus is $1 \le r\le 2$; a quarter-disk caps $\theta$ at $\frac\pi2$. Whole curves simplify too: $x^2 + y^2 = 9$ collapses to $r = 3$, and new curves become easy to write, like the **cardioid** $r = 1 + \cos\theta$ ({numref}`fig-polar-element`, right) — the heart-shaped orbit of a point whose distance from the origin swells and shrinks with direction. (Microphone pickup patterns are drawn in exactly these coordinates, and the cardioid microphone is named for this curve.)

```{figure} figures/ch25-polar-element.png
:name: fig-polar-element
:alt: Left: a polar grid of concentric circles and rays, with one small cell between two radii and two angles highlighted in red. Right: a heart-shaped cardioid curve.

Left: the polar grid, with one **polar rectangle** highlighted: the cell between radii $r$ and $r + dr$ and angles $\theta$ and $\theta + d\theta$. Its area is (arc length) × (thickness) $= (r\,d\theta)(dr)$ — the extra $r$ that enters every polar integral. Right: the cardioid $r = 1 + \cos\theta$, a curve awkward in $(x,y)$ and one line in $(r,\theta)$.
```

## 25.2 The area element: why $r\,dr\,d\theta$

Chop the plane along the polar grid. A cell between radii $r, r+dr$ and angles $\theta, \theta + d\theta$ is nearly a rectangle with sides $dr$ (radial) and $r\,d\theta$ (the arc: radius times angle — radians earning their keep one last time). Hence

$$
dA = r\,dr\,d\theta,
$$

*not* $dr\,d\theta$: cells far from the origin are wider, and the factor $r$ prices that stretching. The same conclusion falls out of Part IV with more machinery and more generality. The map $(r, \theta)\mapsto(x, y)$ has Jacobian matrix of partial derivatives

$$
\mathit J = \begin{bmatrix}\dfrac{\partial x}{\partial r} & \dfrac{\partial x}{\partial\theta}\\[6pt] \dfrac{\partial y}{\partial r} & \dfrac{\partial y}{\partial\theta}\end{bmatrix}
= \begin{bmatrix}\cos\theta & -r\sin\theta\\ \sin\theta & r\cos\theta\end{bmatrix},
\qquad
\det\mathit J = r\cos^2\theta + r\sin^2\theta = r,
$$

and Chapter 19 taught exactly what that determinant means: the local **area-scaling factor** of the transformation. A tiny $dr\times d\theta$ rectangle in the $(r,\theta)$ plane lands in the $(x,y)$ plane as a patch of area $|\det\mathit J|\,dr\,d\theta = r\,dr\,d\theta$. This is the general **change-of-variables** principle — new coordinates cost a Jacobian-determinant factor — of which $u$-substitution's $|dx/du|$ (Chapter 8) was the one-dimensional case and polar is the most-used two-dimensional one.

```{prf:theorem} Double integrals in polar coordinates
:label: thm-polar-integral
If a region $D$ is described by $\alpha\le\theta\le\beta$, $\ g_1(\theta)\le r\le g_2(\theta)$, then

$$
\iint_D f(x, y)\,dA
= \int_\alpha^\beta\!\!\int_{g_1(\theta)}^{g_2(\theta)}
f(r\cos\theta,\ r\sin\theta)\;\, r\,dr\,d\theta.
$$
```

Everything from Chapter 24 applies — iterate inside-out, limits from a sketch — with two substitutions in the integrand and one unforgettable factor of $r$.

```{prf:example} The circle's area, honestly
:label: ex-circle-area-polar
Compute the area of the disk $x^2 + y^2 \le R^2$.

$$
\iint_D 1\,dA = \int_0^{2\pi}\!\!\int_0^R r\,dr\,d\theta
= \int_0^{2\pi}\frac{R^2}{2}\,d\theta = \pi R^2.
$$

Two integrals, no square roots, no trig substitution — compare Chapter 9's semicircle labor. The factors tell the story: $\frac{R^2}2$ is each pie-slice's area per radian, and $2\pi$ radians complete the pie. (And the inner antiderivative $\frac{r^2}{2}$ exists *because* the Jacobian's $r$ is there — dropping it gives "area $2\pi R$," a length, the units already screaming.)
```

```{prf:example} The sphere, revisited in three lines
:label: ex-sphere-polar
Chapter 24's Exercise 21 computed the ball's volume $2\iint_D\sqrt{R^2 - x^2 - y^2}\,dA$ in Cartesian pain. In polar, the integrand is $\sqrt{R^2 - r^2}$ and the disk is a box:

$$
V = 2\int_0^{2\pi}\!\!\int_0^R \sqrt{R^2 - r^2}\;r\,dr\,d\theta
= 2\cdot2\pi\cdot\Bigl[-\tfrac13(R^2 - r^2)^{3/2}\Bigr]_0^R
= 4\pi\cdot\frac{R^3}{3} = \frac{4}{3}\pi R^3.
$$

The Jacobian's $r$ is *precisely* the substitution factor $u = R^2 - r^2$ wants (Chapter 8's pattern-matching, supplied automatically by the coordinate change) — the same happy conspiracy as {prf:ref}`ex-reverse-order`, and the reason radially symmetric integrals melt in polar coordinates.
```

```{prf:example} Area enclosed by the cardioid
:label: ex-cardioid-area
Find the area inside $r = 1 + \cos\theta$.

The region is $0\le r\le 1+\cos\theta$ for $0\le\theta\le2\pi$:

$$
A = \int_0^{2\pi}\!\!\int_0^{1+\cos\theta} r\,dr\,d\theta
= \int_0^{2\pi}\frac{(1+\cos\theta)^2}{2}\,d\theta
= \frac12\int_0^{2\pi}\bigl(1 + 2\cos\theta + \cos^2\theta\bigr)\,d\theta.
$$

Over a full period $\cos\theta$ integrates to zero and $\cos^2\theta$ averages $\frac12$ (Chapter 10's power-reduction, or Chapter 14's constant Fourier term), so $A = \frac12\left(2\pi + 0 + \pi\right) = \frac{3\pi}{2}$. The intermediate formula $A = \int\frac12 r(\theta)^2\,d\theta$ — the inner integral pre-evaluated — is the classical **polar area formula**: each infinitesimal pie-slice contributes $\frac12 r^2\,d\theta$, a triangle with base $r\,d\theta$ and height $r$.
```

## 25.3 The Gaussian integral: the promised finale

The bell curve $e^{-x^2}$ has no elementary antiderivative — Chapters 7, 11, and 13 all met the fact and worked around it. Its integral over the whole line nonetheless has an exact value, and the trick (Poisson's) is among the most celebrated in mathematics: *square the integral, and the two copies become a double integral with circular symmetry.*

```{prf:theorem} Gaussian integral
:label: thm-gaussian
$$
I = \int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}.
$$
```

**Derivation.** Write $I^2$ as a product of two independent copies and merge them (Fubini, run in reverse; the factoring shortcut of {prf:ref}`ex-fubini`):

$$
I^2 = \left(\int_{-\infty}^{\infty}e^{-x^2}dx\right)\left(\int_{-\infty}^{\infty}e^{-y^2}dy\right)
= \iint_{\mathbb{R}^2} e^{-(x^2+y^2)}\,dA.
$$

The integrand depends only on the distance from the origin — pure radial symmetry — so switch to polar, where $x^2 + y^2 = r^2$ and $dA = r\,dr\,d\theta$:

$$
I^2 = \int_0^{2\pi}\!\!\int_0^{\infty} e^{-r^2}\,r\,dr\,d\theta
= 2\pi\Bigl[-\tfrac12 e^{-r^2}\Bigr]_0^{\infty}
= 2\pi\cdot\frac12 = \pi,
$$

and $I = \sqrt\pi$ (positive integrand). Once again the Jacobian's $r$ is exactly the factor the substitution $u = r^2$ requires: in one dimension $e^{-x^2}$ is unintegrable, but $r\,e^{-r^2}$ is a freshman exercise, and the coordinate change *manufactures* the difference. Rescaling ($x = t/\sqrt{2}\sigma$, Chapter 8) gives the form statistics uses:

$$
\int_{-\infty}^{\infty}\frac{1}{\sqrt{2\pi}\,\sigma}\,e^{-t^2/2\sigma^2}\,dt = 1
$$

— the normal density integrates to one, *because* of this calculation. The mysterious $\sqrt{2\pi}$ in the most famous formula in statistics is the area-stretching factor of the polar grid, i.e., ultimately, a determinant.

## 25.4 Common mistakes

```{admonition} Common Mistakes
:class: warning
**The forgotten $r$.** $dA = r\,dr\,d\theta$, always. Omitting the Jacobian factor is the signature polar error; a units check (each term of a polar area integrand should carry length²) catches it.

**Blind arctangent.** $\theta = \arctan(y/x)$ only in the right half-plane; the point $(-1, -1)$ has $\theta = \frac{5\pi}4$ (or $-\frac{3\pi}4$), not $\arctan(1) = \frac\pi4$. Use the signs of $x, y$ (or `np.arctan2(y, x)`).

**Double-covered regions.** Curves like $r = \cos\theta$ (a circle) are traced completely on $\theta\in[-\frac\pi2, \frac\pi2]$; integrating over $[0, 2\pi]$ retraces and double-counts. Sketch the curve and find the honest $\theta$ range first.

**Substituting halfway.** The integrand must be *fully* rewritten: $f(x,y) \to f(r\cos\theta, r\sin\theta)$, with $x^2 + y^2 \to r^2$ the friendly special case. Mixed $x$-and-$r$ expressions are meaningless.

**Choosing polar reflexively.** Polar pays when the *region* or the *integrand* has circular symmetry; over a plain rectangle it manufactures misery. Coordinates are chosen to fit the problem — the actual lesson of this chapter.

**Degrees.** Arc length $r\,d\theta$, the area element, and every formula here assume radians. Final chapter, same first warning.
```

## 25.5 Now do it in Python

```python
import numpy as np
import sympy as sp
from scipy import integrate

r, th = sp.symbols('r theta', nonnegative=True)

# --- Examples 25.4-25.6 exactly ---
R = sp.symbols('R', positive=True)
print(sp.integrate(r, (r, 0, R), (th, 0, 2*sp.pi)))              # pi*R**2
print(sp.integrate(2*sp.sqrt(R**2 - r**2)*r,
                   (r, 0, R), (th, 0, 2*sp.pi)))                 # 4*pi*R**3/3
print(sp.integrate(r, (r, 0, 1 + sp.cos(th)), (th, 0, 2*sp.pi))) # 3*pi/2

# --- Theorem 25.7: the Gaussian, both ways ---
print(sp.integrate(sp.exp(-sp.Symbol('x')**2),
                   (sp.Symbol('x'), -sp.oo, sp.oo)))             # sqrt(pi)
val, _ = integrate.quad(lambda x: np.exp(-x**2), -np.inf, np.inf)
print(val, np.sqrt(np.pi))              # 1.7724538509... twice
```

**Visualization.** Matplotlib speaks polar natively — `plt.subplots(subplot_kw={"projection": "polar"})` — and plotting $r(\theta)$ curves is one line each. Draw the classics and read each from its formula before rendering: the cardioid $1 + \cos\theta$; the three-petal rose $\cos 3\theta$ (petals where $r > 0$; count the sign changes); the spiral $r = \theta/4$; the circle $r = 2\cos\theta$ (verify it's a circle by converting: multiply by $r$ to get $r^2 = 2r\cos\theta$, i.e. $x^2 + y^2 = 2x$).

**Interpretation.** As a capstone experiment, verify the Gaussian trick numerically end to end: `dblquad` the function $e^{-(x^2+y^2)}$ over a large square in Cartesian coordinates, take the square root, and watch $\sqrt{\pi}$ emerge from a computation that never left $(x, y)$ — then time it against the one-line polar/`quad` version. Same number, two coordinate systems, one of them built for the job: the course's closing argument in code.

```{admonition} Data Science Connection
:class: tip
The change-of-variables idea graduates directly into the field's machinery. Transforming a probability density under $\vb y = g(\vb x)$ costs the factor $|\det \mathit J|$ — the exact polar logic — which is how **normalizing flows** build flexible distributions (training maximizes log-likelihoods containing $\log|\det\mathit J|$ terms, Chapter 19's `slogdet` in production). The Gaussian normalization $\sqrt{2\pi}\sigma$ computed above appears in every likelihood, every Kalman filter, every variational bound involving normal distributions; radially symmetric ("isotropic") Gaussians are the default noise model precisely because they are polar-friendly; and Box–Muller sampling *generates* normal random numbers by running this chapter's derivation backwards — sampling an angle uniformly and a radius from $r\,e^{-r^2/2}$.
```

```{admonition} Looking Ahead
:class: seealso
This chapter closes the book, and the threads knot deliberately: Chapter 2's radians measured the arcs in $dA$; Chapter 8's substitution became a Jacobian; Chapter 19's determinant priced the grid's stretch; Chapter 24's Fubini let two impossible one-dimensional integrals merge into one easy two-dimensional one. What lies beyond runs in every direction from here — triple integrals and spherical coordinates (the same Jacobian story, one dimension up), Lagrange multipliers (Chapter 23's Exercise 12, systematized), probability theory standing on the Gaussian integral, and the numerical linear algebra and optimization that Parts IV–V opened. The mathematics of your data science coursework starts on the ground this book has prepared.
```

## 25.6 Exercises

### Quick Check

1. Convert to polar: the point $(1, \sqrt3)$; the curve $x^2 + y^2 = 25$; the region $\{x^2 + y^2 \le 4,\ y \ge 0\}$.
2. Convert the polar point $(r, \theta) = (2, \frac{3\pi}{4})$ to Cartesian.
3. What is the area element in polar coordinates, and where does the extra factor come from (one phrase)?
4. Evaluate $\displaystyle\int_0^{\pi/2}\!\!\int_0^2 r\,dr\,d\theta$ and say what region's area it is.

````{admonition} Answers to Quick Checks
:class: dropdown
1. $(r, \theta) = (2, \frac\pi3)$; $\ r = 5$; $\ 0\le r\le 2,\ 0\le\theta\le\pi$.
2. $(2\cos\frac{3\pi}4,\ 2\sin\frac{3\pi}4) = (-\sqrt2, \sqrt2)$.
3. $dA = r\,dr\,d\theta$; the Jacobian determinant of the polar map (arc length $r\,d\theta$ times $dr$).
4. $\frac\pi2\cdot\frac{4}{2} = \pi$ — the quarter-disk of radius 2 (a quarter of $4\pi$ ✓).
````

### Basic Practice

5. Evaluate using polar coordinates:
   (a) $\iint_D (x^2 + y^2)\,dA$, $D$ the unit disk;
   (b) $\iint_D e^{-(x^2+y^2)}dA$, $D$ the disk of radius 2;
   (c) $\iint_D y\,dA$, $D$ the upper half-disk of radius 1 (predict the sign first);
   (d) $\iint_D \frac{1}{\sqrt{x^2+y^2}}\,dA$, $D$ the annulus $1 \le r \le 3$.
6. Find the volume under the cone $z = \sqrt{x^2 + y^2}$... rather, *between* the cone and the plane $z = 2$ (the region where the cone sits below the plane), by integrating $2 - \sqrt{x^2+y^2}$ over the disk $r \le 2$.
7. Sketch and find the area of one petal of the rose $r = \cos 3\theta$ (first find the $\theta$-interval of one petal from $r \ge 0$).
8. Convert $\displaystyle\int_{-1}^{1}\!\!\int_0^{\sqrt{1-x^2}} (x^2 + y^2)\,dy\,dx$ to polar and evaluate; identify the region that made the Cartesian limits ugly.

````{admonition} Solution to Exercise 7
:class: dropdown
$r = \cos3\theta \ge 0$ for $-\frac\pi6\le\theta\le\frac\pi6$: one petal. Its area:

$$
A = \int_{-\pi/6}^{\pi/6}\frac{\cos^2 3\theta}{2}\,d\theta
= \frac12\int_{-\pi/6}^{\pi/6}\frac{1 + \cos6\theta}{2}\,d\theta
= \frac14\Bigl[\theta + \frac{\sin6\theta}{6}\Bigr]_{-\pi/6}^{\pi/6} = \frac{\pi}{12}.
$$

(Sanity: three petals give $\frac\pi4$, comfortably less than the unit disk's $\pi$ that contains them.)
````

### Intermediate Practice

9. Verify the Jacobian computation of §25.2 with SymPy (`sp.Matrix(...).jacobian(...)` and `.det()`), and repeat for the scaled map $x = ar\cos\theta$, $y = br\sin\theta$ (elliptical coordinates): show $\det\mathit J = abr$, and use it to derive the ellipse's area $\pi ab$ — Chapter 19's Exercise 24, now by integration.
10. Compute the average distance from the origin over the unit disk, $\bar r = \frac{1}{\pi}\iint_D\sqrt{x^2+y^2}\,dA$, and explain intuitively why the answer exceeds $\frac12$.
11. Find the area *inside* the cardioid $r = 1+\cos\theta$ and *outside* the circle $r = 1$ (sketch first; the curves cross where $\cos\theta = 0$).
12. The **centroid** of a region has coordinates $\bar x = \frac1A\iint x\,dA$, $\bar y = \frac1A\iint y\,dA$. Find the centroid of the upper half-disk of radius $R$ (symmetry gives $\bar x$ free; polar handles $\bar y$). *(Answer: $\bar y = \frac{4R}{3\pi}$, a classical constant of engineering tables.)*
13. Evaluate $\displaystyle\int_0^\infty e^{-x^2/2}\,dx$ two ways: by rescaling {prf:ref}`thm-gaussian` (Chapter 8 substitution), and by rerunning the polar argument for the quarter-plane. *(Answer: $\sqrt{\pi/2}$.)*

### Conceptual Understanding

14. Explain to a student one chapter behind you why the $r$ in $r\,dr\,d\theta$ *must* be there, giving both the arc-length picture and the determinant argument, and state which one generalizes to arbitrary coordinate changes.
15. The Gaussian trick squares a one-dimensional integral to make a two-dimensional one — seemingly a step backwards. Identify precisely which two features of the two-dimensional version make it computable when the one-dimensional one is not.
16. When would you *not* use polar coordinates for a region containing the origin? Give a concrete integrand/region pair where Cartesian wins despite circular geometry, and the principle behind your example.

### Python Practice

17. Verify Exercises 5–13 in SymPy/SciPy. For 12, also confirm the centroid by a Monte Carlo average of sampled points in the half-disk (rejection sampling from the bounding rectangle).
18. Implement Box–Muller: from uniform samples $u_1, u_2$, set $r = \sqrt{-2\ln u_1}$, $\theta = 2\pi u_2$, and return $(r\cos\theta, r\sin\theta)$. Generate $10^5$ pairs, histogram each coordinate against the normal density $\frac{1}{\sqrt{2\pi}}e^{-t^2/2}$, and explain in two sentences how this algorithm is {prf:ref}`thm-gaussian`'s derivation run in reverse.

### Visualization Practice

19. In a $2\times2$ grid of polar-projection subplots, draw the cardioid, the rose $\cos3\theta$, the spiral $\theta/4$ (for $0\le\theta\le6\pi$), and the lemniscate $r^2 = \cos2\theta$ (plot where the right side is nonnegative). Caption each with its area or arc-range subtlety.
20. Visualize the Gaussian trick: plot the surface $z = e^{-(x^2+y^2)}$ and, beside it, the radial profile $r e^{-r^2}$ whose one-dimensional integral $\frac12$ times $2\pi$ gives the volume $\pi$. Annotate where the factor $r$ enters.

### Challenge

21. **The bell curve's second moment.** Differentiate the scaled Gaussian identity $\int_{-\infty}^\infty e^{-ax^2}dx = \sqrt{\pi/a}$ with respect to the parameter $a$ (differentiate under the integral sign) to prove $\int_{-\infty}^{\infty}x^2 e^{-x^2}dx = \frac{\sqrt\pi}{2}$, and conclude that the standard normal distribution has variance $1$. One derivative, taken in the right place, replaced an integration by parts.
22. **Volume of the $n$-ball (capstone).** Using the Gaussian in $n$ dimensions — $\left(\sqrt\pi\right)^n = \int_{\mathbb{R}^n}e^{-\|\vb x\|^2}d\vb x$, evaluated radially as $\int_0^\infty e^{-r^2}\,(\text{surface area of } r\text{-sphere})\,dr$ — derive that the unit ball's volume is $V_n = \pi^{n/2}/\Gamma(\frac n2 + 1)$, compute $V_n$ numerically for $n = 1, \ldots, 20$ (use `scipy.special.gamma`), and plot it. The volume *peaks near $n = 5$ and then collapses toward zero* — high-dimensional balls are almost all "corners" — one of the strangest true facts behind the curse of dimensionality that haunts nearest-neighbor methods.

### Cumulative Review

23. *(Ch. 9, 19)* The map $x = ar\cos\theta, y = br\sin\theta$ of Exercise 9 factors as (polar map) followed by the matrix $\operatorname{diag}(a, b)$. Multiply the two Jacobian determinants and confirm the chain-rule-for-determinants gives the same $abr$ — Chapter 19's product rule, meeting Chapter 22's chain rule.
24. *(Ch. 12–13)* Expand $e^{-r^2} = \sum_{k\ge0}\frac{(-r^2)^k}{k!}$, integrate $\int_0^1 e^{-r^2}r\,dr$ term by term, and compare the partial sums' convergence with the exact $\frac{1 - e^{-1}}{2}$. One last alternating series, one last error bound from the first omitted term.

## 25.7 Summary

Polar coordinates $(r, \theta)$ — distance and direction, with $x = r\cos\theta$, $y = r\sin\theta$ — turn circles, annuli, sectors, and curves like the cardioid into coordinate boxes, and the change costs exactly one factor: $dA = r\,dr\,d\theta$, readable as arc-times-thickness and provable as the Jacobian determinant $\det\mathit J = r$ — Chapter 19's area-scaling number, making polar integration the two-dimensional face of the general change-of-variables principle whose one-dimensional case was substitution. With it, the disk's area is two trivial integrals, the sphere's volume three lines, polar areas follow $\frac12\int r^2 d\theta$, and — the book's closing set piece — squaring $\int e^{-x^2}dx$ and going polar yields $\sqrt\pi$: the impossible one-variable integral solved by choosing coordinates that fit its symmetry, and the source of the $\sqrt{2\pi}$ normalizing the normal distribution. The habits this course has drilled — check by computing, verify symbolically and numerically, draw before integrating, pick representations that fit the structure — are the durable content; the formulas now know where to live.

*Parallel reading:* OpenStax *Calculus Volume 3*, Section 5.3 (and Volume 2, §7.3–7.4 for polar curves) {cite}`openstax_calc3,openstax_calc2`.
