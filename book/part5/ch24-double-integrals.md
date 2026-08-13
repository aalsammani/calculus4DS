# Chapter 24 · Double Integrals

Part II integrated over intervals; this chapter integrates over *regions of the plane*. The construction is Riemann's, verbatim — chop, sample, multiply by size, add, refine — with rectangles replacing subintervals and volume replacing area. The working method is better news still: a **double integral evaluates as two single integrals in sequence**, one variable at a time, so Part II's entire toolkit is re-hired rather than replaced. Volumes, averages over regions, total quantities from densities, and the probability computations of joint distributions are the immediate dividends.

## 24.1 The definition: volume by boxes

Let $f(x, y) \ge 0$ on a rectangle $R = [a, b]\times[c, d]$. Partition $R$ into small subrectangles of area $\Delta A = \Delta x\,\Delta y$; on each, sample the height and erect a box; add the box volumes; refine.

```{prf:definition} Double integral
:label: def-double-integral
$$
\iint_R f(x, y)\, dA
= \lim_{\Delta A \to 0} \sum_{i,j} f(x_i^*, y_j^*)\;\Delta A,
$$

when the limit exists (it does for continuous $f$). For $f \ge 0$ it is the **volume** under the surface $z = f(x,y)$ over $R$; in general it is signed volume, above-minus-below, exactly as Chapter 7's signed area.
```

```{figure} figures/ch24-double-integral-boxes.png
:name: fig-double-integral-boxes
:alt: A tilted plane surface over a rectangle, with a six-by-six grid of vertical boxes underneath it whose tops approximate the surface.

Riemann's construction, one dimension up: boxes under the plane $z = 4 - x - y$ over $[0,1]\times[0,2]$. The midpoint-sampled $6\times6$ box total is $5.0000$ against the exact volume $5$ — midpoint sampling is as unreasonably good here as it was in Chapter 7 (for a plane it is exact, since linear over- and under-shoots cancel within each cell).
```

All the structural properties carry over from Chapter 7 by the same limit arguments: linearity, additivity over subregions ($\iint_{R_1\cup R_2} = \iint_{R_1} + \iint_{R_2}$ for non-overlapping pieces), and order preservation. Two specializations earn their own names: $\iint_R 1\,dA$ is the **area** of $R$ (boxes of height 1 — a slab whose volume equals the base's area), and

$$
\bar f = \frac{1}{\text{Area}(R)}\iint_R f\,dA
$$

is the **average value** of $f$ over the region — total divided by extent, Chapter 7's average upgraded.

## 24.2 Fubini: iterate the integrals

The definition computes nothing; slicing does. Fix $x$ and integrate the slice's profile in $y$; then integrate the slice areas in $x$:

```{prf:theorem} Fubini's theorem
:label: thm-fubini
For $f$ continuous on $R = [a,b]\times[c,d]$:

$$
\iint_R f\,dA
= \int_a^b\!\!\left[\int_c^d f(x, y)\,dy\right] dx
= \int_c^d\!\!\left[\int_a^b f(x, y)\,dx\right] dy
$$

— an **iterated integral**, computable inside-out with Part II's techniques, in either order.
```

The inner integral treats the outer variable as a constant — the *integration* counterpart of partial differentiation's freeze-the-others discipline, and the same mental muscle.

```{prf:example} An iterated integral, both orders
:label: ex-fubini
Compute $\displaystyle\iint_R xy^2\,dA$ over $R = [0,1]\times[0,2]$.

Inner in $y$ first ($x$ frozen):

$$
\int_0^2 xy^2\,dy = x\cdot\frac{y^3}{3}\Big|_0^2 = \frac{8x}{3},
\qquad\text{then}\qquad
\int_0^1 \frac{8x}{3}\,dx = \frac{8}{3}\cdot\frac12 = \frac43.
$$

Other order: $\int_0^1 xy^2\,dx = \frac{y^2}{2}$, then $\int_0^2\frac{y^2}2\,dy = \frac{8}{6} = \frac43$ ✓. (When the integrand *factors* as $g(x)h(y)$ over a rectangle, the whole computation splits: $\iint = \left(\int_0^1 x\,dx\right)\left(\int_0^2 y^2\,dy\right) = \frac12\cdot\frac83 = \frac43$ — a shortcut that probability will use constantly for independent variables.)
```

```{prf:example} A volume
:label: ex-volume-plane
Find the volume under $z = 4 - x - y$ over $R = [0,1]\times[0,2]$ ({numref}`fig-double-integral-boxes`).

$$
\int_0^1\!\!\int_0^2 (4 - x - y)\,dy\,dx
= \int_0^1\Bigl[4y - xy - \tfrac{y^2}{2}\Bigr]_0^2 dx
= \int_0^1 (8 - 2x - 2)\,dx
= \int_0^1 (6 - 2x)\,dx = 5.
$$

Interpretation check: the plane's height over the rectangle averages $\bar f = \frac{5}{2}$ (volume over area $2$) — and indeed the height at the rectangle's *center* $(\tfrac12, 1)$ is $4 - \tfrac12 - 1 = \tfrac52$: for a linear roof, average height is center height, which is also why the midpoint boxes in the figure are exact.
```

## 24.3 General regions

Most regions aren't rectangles. The fix: let the *inner limits depend on the outer variable*. For a region bounded below and above by curves $y = g_1(x)$ and $y = g_2(x)$ over $a \le x \le b$ (a **Type I** region — vertical slices):

$$
\iint_D f\,dA = \int_a^b\!\!\int_{g_1(x)}^{g_2(x)} f(x, y)\,dy\,dx,
$$

and symmetrically for regions carved by horizontal slices (**Type II**: $x$ between $h_1(y)$ and $h_2(y)$). The discipline that prevents nearly all errors: **draw the region, then describe it in slices** before writing any integral sign — the limits *are* the region.

```{prf:example} Integrating over a triangle
:label: ex-triangle-region
Compute $\displaystyle\iint_D xy\,dA$ where $D$ is the triangle with vertices $(0,0)$, $(1, 0)$, $(1, 1)$.

Sketch: the region under the line $y = x$ for $0\le x\le 1$. Vertical slices run from $y = 0$ up to $y = x$:

$$
\int_0^1\!\!\int_0^{x} xy\,dy\,dx
= \int_0^1 x\cdot\frac{x^2}{2}\,dx = \int_0^1\frac{x^3}{2}dx = \frac18.
$$

The same region sliced horizontally: for $0 \le y \le 1$, $x$ runs from $y$ to $1$, and $\int_0^1\!\int_y^1 xy\,dx\,dy = \int_0^1 y\,\frac{1 - y^2}{2}dy = \frac18$ ✓. Notice the limits' anatomy: *outer limits are constants; inner limits may contain the outer variable, never their own.* An inner limit containing $y$ inside a $dy$ integral is a syntax error of the subject.
```

```{prf:example} Reversing the order to make an integral possible
:label: ex-reverse-order
Evaluate $\displaystyle\int_0^1\!\!\int_x^1 e^{y^2}\,dy\,dx$.

As written, the inner antiderivative $\int e^{y^2}dy$ does not exist in elementary form (Chapter 7's old nemesis, sign flipped). But the integral *describes a region* — $x \le y \le 1$ over $0\le x\le 1$: the triangle above the line $y = x$ — and that region re-slices horizontally as $0 \le x \le y$ for $0 \le y \le 1$:

$$
\int_0^1\!\!\int_0^{y} e^{y^2}\,dx\,dy
= \int_0^1 y\,e^{y^2}\,dy
= \frac{e^{y^2}}{2}\Big|_0^1 = \frac{e - 1}{2}
$$

— the inner integral manufactured exactly the factor $y$ that Chapter 8's substitution needed. Order reversal is not bookkeeping; it is a genuine technique, and this example (a classic) is its advertisement.
```

## 24.4 Common mistakes

```{admonition} Common Mistakes
:class: warning
**Limits invented without a sketch.** The limits encode the region; writing them from the problem's words instead of a drawing is the dominant error source. Sketch, slice, then integrate.

**Variable limits in the wrong place.** Outer limits: constants. Inner limits: functions of the outer variable only. Any limit containing the variable being integrated is malformed.

**Freezing failures in the inner integral.** In $\int f(x,y)\,dy$, the variable $x$ is constant — including inside exponents and as factors, mirroring the partial-derivative discipline. ($\int_0^2 xy^2dy = \frac{8x}{3}$, not $\frac{x^2y^3}{6}$-style hybrids.)

**Reversing order without re-deriving limits.** Swapping $dx\,dy \to dy\,dx$ while keeping the same numbers is only valid on rectangles. General regions must be re-sliced ({prf:ref}`ex-reverse-order` done lazily gives nonsense).

**Volume versus signed volume.** Where $f$ dips negative, the integral subtracts, as in Chapter 7; a geometric volume of an oscillating surface needs $\iint |f|\,dA$ or split regions.

**Area versus volume confusion.** $\iint_D 1\,dA$ is the *area* of $D$ (useful!); $\iint_D f\,dA$ is not "area" for other $f$. Units track it: $dA$ carries (length)², the integrand its own units.
```

## 24.5 Now do it in Python

SymPy nests `integrate` calls exactly as Fubini nests integrals; SciPy's `dblquad` is the numerical workhorse:

```python
import sympy as sp
from scipy import integrate
import numpy as np

x, y = sp.symbols('x y')

# --- Examples 24.3-24.4 exactly ---
print(sp.integrate(x*y**2, (y, 0, 2), (x, 0, 1)))       # 4/3
print(sp.integrate(4 - x - y, (y, 0, 2), (x, 0, 1)))    # 5

# --- Example 24.5: variable inner limits ---
print(sp.integrate(x*y, (y, 0, x), (x, 0, 1)))          # 1/8

# --- Example 24.6: the reversed-order classic ---
print(sp.integrate(sp.exp(y**2), (x, 0, y), (y, 0, 1))) # -1/2 + E/2

# --- Numerically: dblquad(f(y, x), x_lo, x_hi, y_lo(x), y_hi(x)) ---
val, err = integrate.dblquad(lambda y_, x_: x_*y_, 0, 1, 0, lambda x_: x_)
print(val)                                              # 0.125
```

Mind `dblquad`'s conventions — the integrand takes `(y, x)` in that order, and the $y$ limits may be callables of $x$: the Type-I structure, encoded. Its error estimate rides along in the second return value.

**Monte Carlo, the other honest method.** For regions or dimensions where slicing is painful, integrate by *sampling*: the average of $f$ at uniform random points, times the region's area, estimates the integral:

```python
rng = np.random.default_rng(0)
N = 1_000_000
pts = rng.uniform(0, 1, size=(N, 2))
inside = pts[:, 1] <= pts[:, 0]                  # the triangle y <= x
est = (pts[inside, 0]*pts[inside, 1]).sum() / N  # mean over the SQUARE times its area 1
print(est)                                       # ~0.1250 (exact: 1/8)
```

**Interpretation.** The estimate lands within about $10^{-3}$ of $\frac18$ — Monte Carlo's error shrinks like $1/\sqrt N$ regardless of dimension, which is terrible compared to Chapter 11's rules in one dimension and *unbeatable* in fifty, where grids are hopeless ($10$ points per axis in $50$ dimensions is $10^{50}$ evaluations). This dimension-indifference is why Monte Carlo methods own high-dimensional integration — which is to say, own much of Bayesian statistics and statistical physics.

```{admonition} Data Science Connection
:class: tip
Double integrals are how joint probability works: a joint density $p(x,y)$ satisfies $\iint p\,dA = 1$, probabilities of events are integrals over regions ($P(X < Y)$ is an integral over a triangle — literally {prf:ref}`ex-triangle-region`'s geometry), marginal densities are inner integrals ($p_X(x) = \int p(x,y)\,dy$: Fubini's inner slice), and expectations are $\iint g(x,y)\,p(x,y)\,dA$. Independence is exactly the factorization shortcut of {prf:ref}`ex-fubini`. And when the integrals cannot be done — high-dimensional posteriors — the field reaches for the Monte Carlo estimator above, elaborated into MCMC.
```

```{admonition} Looking Ahead
:class: seealso
Circular regions make Cartesian slices ugly — a disk's vertical slice has limits $\pm\sqrt{r^2 - x^2}$, and worse awaits inside. Chapter 25 changes coordinates to polar, where disks are rectangles; the area element becomes $r\,dr\,d\theta$, with Chapter 19's determinant explaining the extra $r$ — and the course's last chapter closes the loop by evaluating the Gaussian integral that Chapters 7 and 13 could only name.
```

## 24.6 Exercises

### Quick Check

1. Evaluate $\displaystyle\int_0^2\!\!\int_0^3 (2x + y)\,dy\,dx$.
2. Over which region does $\displaystyle\int_0^1\!\!\int_0^{x^2} f\,dy\,dx$ integrate? Sketch-describe it.
3. What is $\iint_D 5\,dA$ if $D$ has area $3$?
4. True or false: $\displaystyle\iint_R g(x)h(y)\,dA = \Bigl(\int g\Bigr)\Bigl(\int h\Bigr)$ over any region $R$.

````{admonition} Answers to Quick Checks
:class: dropdown
1. $\int_0^2 (6x + \tfrac92)\,dx = 12 + 9 = 21$.
2. The region under the parabola $y = x^2$, above the $x$-axis, for $0\le x\le 1$.
3. $15$ — constant times area (a slab).
4. False in general — the factorization requires a *rectangle* (constant limits); over a triangle the inner limits couple the variables.
````

### Basic Practice

5. Evaluate over the given rectangles, choosing the friendlier order:
   (a) $\iint x e^{xy}\,dA$, $R = [0,1]\times[0,1]$ (integrate in $y$ first);
   (b) $\iint \frac{y}{1 + x^2}\,dA$, $R = [0, 1]\times[0, 2]$ (it factors);
   (c) $\iint x\cos(x + y)\,dA$, $R = [0, \tfrac\pi2]\times[0,\tfrac\pi2]$.
6. Find the volume under $z = 9 - x^2 - y^2$ over $R = [-1, 1]\times[-1,1]$, and the average height of that roof over the square.
7. Integrate $f(x,y) = x + y$ over the triangle with vertices $(0,0)$, $(2,0)$, $(0,2)$, slicing both ways and confirming agreement.
8. Compute the area of the region between $y = x^2$ and $y = \sqrt x$ via $\iint_D 1\,dA$, and check against Chapter 9's area-between-curves formula — the two are the same computation, with the inner integral pre-evaluated.

````{admonition} Solution to Exercise 7 (vertical slices)
:class: dropdown
The hypotenuse is $x + y = 2$; slices run $0 \le y \le 2 - x$ for $0\le x\le 2$:

$$
\int_0^2\!\!\int_0^{2-x}(x+y)\,dy\,dx
= \int_0^2\Bigl[x(2-x) + \tfrac{(2-x)^2}{2}\Bigr]dx
= \int_0^2\Bigl(2x - x^2 + 2 - 2x + \tfrac{x^2}2\Bigr)dx
= \int_0^2\Bigl(2 - \tfrac{x^2}2\Bigr)dx = 4 - \tfrac43 = \tfrac83.
$$
````

### Intermediate Practice

9. Reverse the order of integration and evaluate: (a) $\displaystyle\int_0^1\!\!\int_{\sqrt y}^{1}\, \frac{2}{1+x^3}\,dx\,dy$ *(the reversed inner integral produces the substitution factor)*; (b) $\displaystyle\int_0^{\pi}\!\!\int_x^{\pi}\frac{\sin y}{y}\,dy\,dx$ *(Chapter 7's Si-integrand, defeated by re-slicing).*
10. A city's population density is $\rho(x, y) = 4000\,e^{-x^2-y^2}$ people/km² on the square $[-2,2]^2$ (km). Set up and numerically evaluate the total population and the average density; explain why the two differ by exactly the factor $16$.
11. For the joint density $p(x, y) = 6xy^2$ on $[0,1]^2$ (check it integrates to 1): compute $P(X > Y)$ as an integral over the triangle $x > y$, and the marginal $p_X(x) = \int_0^1 p\,dy$. Are $X$ and $Y$ independent? (Does $p$ factor?)
12. Prove the average-value property used in {prf:ref}`ex-volume-plane`: for any *linear* $f(x,y) = \alpha + \beta x + \gamma y$ over a rectangle, $\bar f$ equals $f$ at the rectangle's center. (Integrate; or argue by the symmetry of $x - \bar x$ about the center.)

### Conceptual Understanding

13. Explain why Fubini's inner integral $\int_c^d f(x, y)\,dy$ is "a slice's area, as a function of where you slice," and how that reduces the double integral to Chapter 9's volumes-by-cross-sections.
14. State precisely what goes wrong if one "reverses order" over a non-rectangular region without re-deriving limits, using {prf:ref}`ex-reverse-order`'s region as the concrete case.
15. Grid-based numerical integration in $d$ dimensions with $n$ points per axis costs $n^d$ evaluations; Monte Carlo's error is $\sim1/\sqrt N$ independent of $d$. Find the dimension at which Monte Carlo with $10^6$ samples beats a $10$-points-per-axis grid on evaluation count, and explain the term "curse of dimensionality" in one sentence.

### Python Practice

16. Verify Exercises 5–11 (SymPy where exact, `dblquad` for 10; for 11, also estimate $P(X>Y)$ by Monte Carlo sampling from $p$ via rejection and compare).
17. Write `monte_carlo_2d(f, region_test, box, N)` estimating $\iint_D f\,dA$ for a region given by an indicator function inside a bounding box. Validate on {prf:ref}`ex-triangle-region` ($\tfrac18$) and on the unit disk's area ($\pi$), reporting the error's decay as $N$ runs through $10^3, 10^4, \ldots, 10^7$ — confirm the $1/\sqrt N$ law on a log-log plot.

### Visualization Practice

18. Recreate {numref}`fig-double-integral-boxes` for $f = 9 - x^2 - y^2$ over $[-1,1]^2$ with $4\times4$, $8\times8$, and $16\times16$ midpoint boxes, printing each approximation next to the exact value from Exercise 6.
19. Plot the two regions of Exercise 9 with both slicing directions indicated (a few representative vertical and horizontal segments), making visually clear why one order is computable and the other stalls.

### Challenge

20. **Expected distance.** Two points are dropped uniformly at random on $[0,1]$. Their expected separation is $\mathbb E|X - Y| = \iint_{[0,1]^2}|x - y|\,dA$. Evaluate by splitting the square along $y = x$ (symmetry halves the work), then confirm by simulation. *(Answer: $\tfrac13$.)*
21. **Volume of the sphere, by slices.** Compute the volume of the ball $x^2 + y^2 + z^2 \le r^2$ as $2\iint_D \sqrt{r^2 - x^2 - y^2}\,dA$ over the disk $D$ — in Cartesian coordinates, enduring the $\sqrt{r^2 - x^2}$ limits and a trig substitution (Chapter 10). Keep your work: Chapter 25 redoes it in polar coordinates in three lines, and the comparison is the entire sales pitch for changing coordinates.

### Cumulative Review

22. *(Ch. 11)* Implement the two-dimensional midpoint rule as a double loop (or outer product) and apply it to {prf:ref}`ex-fubini`'s integral with $n = 4, 8, 16$ per axis. What convergence order do you observe, and how does it relate to the one-dimensional midpoint rule's $n^{-2}$?
23. *(Ch. 13)* Estimate $\iint_{[0,0.5]^2} e^{xy}\,dA$ by replacing $e^{xy}$ with its first three Taylor terms $1 + xy + \tfrac{(xy)^2}{2}$, integrating term by term (each factors!), and bound the error using the next term. Compare with `dblquad`.

## 24.7 Summary

The double integral $\iint_R f\,dA$ is Riemann's limit of boxes — signed volume under a surface, with $\iint 1\,dA$ recovering area and total-over-area defining the average — and Fubini's theorem computes it as iterated single integrals, inner variable integrated with the outer frozen, either order on rectangles (factoring outright when the integrand separates). General regions enter through slice-dependent limits: sketch, slice (vertically or horizontally), and let the drawing dictate limits — outer constant, inner depending only on the outer — with order reversal, *re-derived from the region*, as a genuine technique that cracks otherwise impossible integrands. Applications run from volumes and averages to densities and joint probability (normalization, region probabilities, marginals as inner integrals, independence as factorization). Computationally: nested `sp.integrate`, `dblquad` with its callable limits, and Monte Carlo sampling whose dimension-blind $1/\sqrt N$ error makes it the only game in high dimension. Round regions await better coordinates — polar, next, with a determinant in the area element.

*Parallel reading:* OpenStax *Calculus Volume 3*, Sections 5.1–5.2 {cite}`openstax_calc3`.
