# Chapter 9 · Areas Between Curves and Volumes of Solids

The definite integral was born from one geometric problem — area under a curve — but the *method* behind it is far more general: slice a quantity into thin pieces, approximate each piece by something simple, add, and take the limit. This chapter applies the slicing method to two families of geometry problems: areas of regions between curves, and volumes of solids, including solids of revolution by disks, washers, and cylindrical shells. Beyond the formulas, the goal is the *skill of setting up integrals from pictures*, which is the form in which integration earns its keep in applications.

## 9.1 Area between two curves

If $f(x) \ge g(x)$ on $[a, b]$, the region trapped between the two graphs has, at each $x$, a vertical cross-section of height $f(x) - g(x)$. A thin strip of width $dx$ there contributes area $\bigl(f(x)-g(x)\bigr)dx$, and summing the strips:

```{prf:theorem} Area between curves
:label: thm-area-between
If $f$ and $g$ are continuous with $f(x) \ge g(x)$ on $[a,b]$, the area of the region between the graphs is

$$
A = \int_a^b \bigl[\,f(x) - g(x)\,\bigr]\,dx \qquad \text{(top minus bottom).}
$$
```

The recipe in practice: **sketch** the curves; **find intersections** (solve $f = g$) to get the limits if they are not given; identify **which curve is on top** on each piece (test one point); **integrate top minus bottom**, splitting the interval wherever the curves change places.

```{prf:example} The standard first region
:label: ex-area-x-x2
Find the area between $y = x$ and $y = x^2$.

**Intersections:** $x = x^2 \Rightarrow x(x - 1) = 0 \Rightarrow x = 0, 1$. **Top curve:** at $x = \frac12$, the line gives $\frac12$ and the parabola $\frac14$, so the line is on top. **Integrate:**

$$
A = \int_0^1 \bigl(x - x^2\bigr)\,dx = \left[\frac{x^2}{2} - \frac{x^3}{3}\right]_0^1 = \frac12 - \frac13 = \frac16.
$$
```

```{figure} figures/ch09-area-between.png
:name: fig-area-between
:alt: The line y equals x and the parabola y equals x squared meeting at the origin and at the point one comma one, with the lens-shaped region between them shaded and labeled with area one sixth.

The region of {prf:ref}`ex-area-x-x2`: between $y=x$ (top) and $y=x^2$ (bottom) from $x=0$ to $x=1$. Each vertical strip has height $x - x^2$; integrating those heights sweeps out the area $\frac16$.
```

```{prf:example} When the top changes
:label: ex-area-crossing
Find the total area enclosed between $y = \sin x$ and $y = \cos x$ over $[0, \pi]$.

The curves cross where $\sin x = \cos x$: at $x = \frac{\pi}{4}$. Cosine is on top before the crossing, sine after, so the area splits:

$$
A = \int_0^{\pi/4}(\cos x - \sin x)\,dx + \int_{\pi/4}^{\pi}(\sin x - \cos x)\,dx.
$$

First piece: $\bigl[\sin x + \cos x\bigr]_0^{\pi/4} = \sqrt2 - 1$. Second: $\bigl[-\cos x - \sin x\bigr]_{\pi/4}^{\pi} = 1 - \bigl(-\sqrt2\bigr) = 1 + \sqrt2$. Total:

$$
A = (\sqrt2 - 1) + (1 + \sqrt2) = 2\sqrt2 \approx 2.828.
$$

Integrating $\cos - \sin$ straight across $[0,\pi]$ without splitting would have produced $-\sqrt2 - 1 + \ldots$ — cancellation, not area. *Total area between curves is the integral of $|f - g|$*, and splitting at crossings is how one computes it.
```

Sometimes strips work better horizontally. If a region is bounded by curves more naturally written $x = $ function of $y$ — say $x = h(y)$ on the right and $x = k(y)$ on the left for $c \le y \le d$ — then

$$
A = \int_c^d\bigl[\,h(y) - k(y)\,\bigr]\,dy \qquad\text{(right minus left)},
$$

and a region like the one between $y^2 = x$ and $y = x - 2$ (Exercise 8) that needs two pieces with vertical strips needs only one with horizontal strips. Choosing the slicing direction that avoids splitting is the first taste of a recurring theme: *set up the integral in the coordinates that fit the region*.

## 9.2 Volumes by cross-sections

The slicing idea lifts from 2-D to 3-D verbatim. Slice a solid perpendicular to an axis; if the cross-section at position $x$ has area $A(x)$, a slab of thickness $dx$ has volume $A(x)\,dx$, and

$$
V = \int_a^b A(x)\,dx.
$$

The area-between-curves formula is the special case where "slices" are line segments; here they are plane regions. Everything reduces to *knowing the cross-sectional area as a function of position*.

```{prf:example} A pyramid, resolved by slicing
:label: ex-pyramid
A pyramid has a square base of side $s$ and height $h$, apex centered above the base. Find its volume.

Measure $x$ downward from the apex. By similar triangles, the square cross-section at depth $x$ has side $\frac{s x}{h}$, hence area $A(x) = \frac{s^2x^2}{h^2}$. Then

$$
V = \int_0^h \frac{s^2}{h^2}x^2\,dx = \frac{s^2}{h^2}\cdot\frac{h^3}{3} = \frac{1}{3}s^2 h,
$$

the classical "one-third base times height," derived in three lines rather than received on authority. The factor $\frac13$ is visibly the integral $\int_0^1 t^2\,dt$: it comes from areas growing *quadratically* along the axis.
```

## 9.3 Solids of revolution: disks and washers

Rotate a plane region about an axis and the cross-sections perpendicular to that axis are **disks** (or, if the region does not touch the axis, **washers** — disks with holes). A disk of radius $R$ has area $\pi R^2$; a washer with outer radius $R$ and inner radius $r$ has area $\pi(R^2 - r^2)$. Feeding these into the cross-section formula:

$$
V_{\text{disk}} = \int_a^b \pi\,\bigl[R(x)\bigr]^2\,dx,
\qquad
V_{\text{washer}} = \int_a^b \pi\Bigl(\bigl[R(x)\bigr]^2 - \bigl[r(x)\bigr]^2\Bigr)\,dx,
$$

where the radius functions are read off the region: for rotation about the $x$-axis, $R(x)$ is the distance from the axis to the region's outer boundary — usually just the top curve's height.

```{prf:example} A disk-method volume
:label: ex-disk
The region under $y = \sqrt x$ from $x=0$ to $x=4$ is rotated about the $x$-axis. Find the volume of the resulting solid.

Each cross-section at $x$ is a disk of radius $R(x) = \sqrt x$, area $\pi x$:

$$
V = \int_0^4 \pi\bigl(\sqrt x\bigr)^2\,dx = \pi\int_0^4 x\,dx = \pi\cdot\frac{16}{2} = 8\pi \approx 25.13.
$$
```

```{figure} figures/ch09-disk-solid.png
:name: fig-disk-solid
:alt: Left: the region under the square root curve with one vertical radius segment highlighted. Right: a three-dimensional horn-shaped solid of revolution generated by rotating that region about the x axis, with one circular cross-section drawn.

Left: the region under $y=\sqrt x$ with a representative radius. Right: rotating about the $x$-axis sweeps each vertical segment into a disk of area $\pi x$; stacking the disks from $0$ to $4$ builds the solid, and integrating their areas gives its volume $8\pi$.
```

```{prf:example} A washer-method volume
:label: ex-washer
The region between $y = x$ and $y = x^2$ (the region of {prf:ref}`ex-area-x-x2`) is rotated about the $x$-axis. Find the volume.

At each $x \in [0,1]$ the cross-section is a washer: outer radius to the top curve, $R = x$; inner radius to the bottom curve, $r = x^2$:

$$
V = \pi\int_0^1\bigl(x^2 - x^4\bigr)\,dx = \pi\left(\frac13 - \frac15\right) = \frac{2\pi}{15} \approx 0.4189.
$$

The crucial discipline: **square the radii separately.** $R^2 - r^2 \neq (R - r)^2$; using the region's height $x - x^2$ as a "radius" is the single most common volume error, and it is wrong because the hole's absence of material must be subtracted as $\pi r^2$, not folded into the outer radius.
```

## 9.4 Solids of revolution: cylindrical shells

Disks slice *perpendicular* to the rotation axis. Sometimes those slices are awkward — rotating a region about the $y$-axis when its curves are given as $y = f(x)$ would force inverting the functions. The **shell method** slices *parallel* to the axis instead: a vertical strip at position $x$, of height $h(x)$ and width $dx$, sweeps into a thin cylindrical shell of radius $x$, circumference $2\pi x$, and hence volume $2\pi x\,h(x)\,dx$ — a rolled-up rectangle. Summing shells:

$$
V = \int_a^b 2\pi\,(\text{radius})(\text{height})\,dx = \int_a^b 2\pi\,x\,h(x)\,dx
\qquad\text{(rotation about the } y\text{-axis, region in } x \ge 0).
$$

```{prf:example} A shell-method volume
:label: ex-shell
The region under $y = x - x^2$ (above the $x$-axis, so $0 \le x \le 1$) is rotated about the **$y$-axis**. Find the volume.

Vertical strips have radius $x$ and height $x - x^2$:

$$
V = 2\pi\int_0^1 x\,(x - x^2)\,dx = 2\pi\int_0^1 (x^2 - x^3)\,dx = 2\pi\left(\frac13 - \frac14\right) = \frac{\pi}{6} \approx 0.5236.
$$

Attempting disks here would require solving $y = x - x^2$ for $x$ (two branches of a quadratic) and washering between them — possible, and miserable. Method choice is not taste; it is matching the slicing direction to how the boundary is described.
```

```{figure} figures/ch09-shell.png
:name: fig-shell
:alt: The arch of y equals x minus x squared with one vertical strip highlighted at x, labeled with its radius x from the y axis and its height x minus x squared, ready to be swept into a cylindrical shell.

The shell picture for {prf:ref}`ex-shell`: the highlighted strip, radius $x$ from the rotation axis and height $x - x^2$, sweeps into a cylindrical shell of volume $2\pi x (x - x^2)\,dx$. Integrating over the strips fills the solid from its core outward.
```

**Choosing between disks and shells.** Ask: in which direction are the boundary curves functions? Strips **perpendicular** to the axis of rotation ⇒ disks/washers; strips **parallel** to the axis ⇒ shells. If $y = f(x)$ and you rotate about the $x$-axis, disks are natural; about the $y$-axis, shells are. For axes other than the coordinate axes (say, rotation about $y = -1$), the same setups apply with radii measured *from the new axis*: replace $R(x)$ by $f(x) + 1$, and so on — always draw the radius on your sketch before writing the integral.

## 9.5 Common mistakes

```{admonition} Common Mistakes
:class: warning
**Bottom minus top.** A negative "area" signals the subtraction is reversed or the curves cross inside the interval. Sketch first; test a point.

**Ignoring crossings.** Between crossings the top changes; total area needs the interval split ({prf:ref}`ex-area-crossing`). One integral of $f - g$ across a crossing silently cancels area.

**$(R - r)^2$ instead of $R^2 - r^2$** in washers — see {prf:ref}`ex-washer`. Radii are squared *before* subtracting.

**Radius measured from the wrong place.** The radius runs from the *axis of rotation* to the curve, not from the $x$-axis, and not the height of the region. Rotating about $y = 2$ the curve $y = f(x) \le 2$ has $R(x) = 2 - f(x)$.

**Shells with the wrong pairing.** In $2\pi\int(\text{radius})(\text{height})$, the radius is the distance of the *strip* from the axis (usually the variable itself), the height is the *length* of the strip. Swapping them is dimensionally invisible and numerically fatal.

**Mixing the variable of integration.** Disks about the $y$-axis integrate in $y$; shells about the $y$-axis integrate in $x$. The variable follows the slicing, not the axis.
```

## 9.6 Now do it in Python

Symbolic checks of every example, then a numerical cross-check of the two rotation methods against each other — the strongest test available, since disks and shells must agree on any solid both can describe.

```python
import sympy as sp

x, y = sp.symbols('x y')

# --- Areas (Examples 9.2, 9.3) ---
print(sp.integrate(x - x**2, (x, 0, 1)))                          # 1/6
A = (sp.integrate(sp.cos(x) - sp.sin(x), (x, 0, sp.pi/4))
     + sp.integrate(sp.sin(x) - sp.cos(x), (x, sp.pi/4, sp.pi)))
print(sp.simplify(A))                                             # 2*sqrt(2)

# --- Volumes (Examples 9.4-9.7) ---
print(sp.integrate(sp.pi * x, (x, 0, 4)))                         # 8*pi
print(sp.integrate(sp.pi * (x**2 - x**4), (x, 0, 1)))             # 2*pi/15
print(sp.integrate(2*sp.pi * x * (x - x**2), (x, 0, 1)))          # pi/6
s, h = sp.symbols('s h', positive=True)
print(sp.integrate(s**2 * x**2 / h**2, (x, 0, h)))                # h*s**2/3
```

Now the cross-method check on {prf:ref}`ex-disk`'s solid. Rotating $y=\sqrt x$, $0\le x\le 4$, about the $x$-axis by *shells* means horizontal strips at height $y \in [0, 2]$, radius $y$, extending from $x = y^2$ to $x = 4$:

```python
print(sp.integrate(2*sp.pi * y * (4 - y**2), (y, 0, 2)))          # 8*pi again
```

Both methods give $8\pi$: two completely different slicings of one solid, one volume. A Monte Carlo estimate provides a third, method-free opinion — throw random points into a bounding box and count the fraction landing inside the solid:

```python
import numpy as np

rng = np.random.default_rng(1)
N = 2_000_000
X = rng.uniform(0, 4, N)
Y = rng.uniform(-2, 2, N)
Z = rng.uniform(-2, 2, N)
inside = Y**2 + Z**2 <= X            # distance from x-axis at most sqrt(x)
box_volume = 4 * 4 * 4
print(box_volume * inside.mean(), 8*np.pi)    # ~25.13 vs 25.1327...
```

**Interpretation.** The Monte Carlo answer lands within a few hundredths of $8\pi$ — crude next to the exact integral, but it *knows nothing about calculus*, only about the solid's defining inequality. When an exact method and an ignorant method agree, the setup (radius, limits, axis) was right, and setup is where volume problems are won or lost.

```{admonition} Data Science Connection
:class: tip
"Area between curves" is a quantity you will actually compute: the region between a model's predicted-demand curve and realized demand is cumulative forecast error; the area between two probability densities, $\frac12\int|p - q|$, is the *total variation distance* between distributions; and the area under an ROC curve (AUC) — the standard classifier metric — is a definite integral estimated by exactly the strip-summing of this chapter. The Monte Carlo volume estimate above is a first meeting with the sampling methods that dominate high-dimensional integration in statistics, where slicing becomes infeasible.
```

## 9.7 Exercises

### Quick Check

1. Set up (do not evaluate) the area integral between $y = 4 - x^2$ and $y = x + 2$.
2. A solid's cross-sections have area $A(x) = 6x^2$ for $0 \le x \le 2$. Its volume is?
3. Rotating the region under $y = 3$ over $[0, 5]$ about the $x$-axis gives what solid, and what volume — by formula and by disks?
4. For rotation about the $y$-axis with curves given as $y = f(x)$: disks or shells, and why?

````{admonition} Answers to Quick Checks
:class: dropdown
1. Intersections: $4 - x^2 = x + 2 \Rightarrow x^2 + x - 2 = 0 \Rightarrow x = -2, 1$; the parabola is on top: $\int_{-2}^{1}\bigl[(4 - x^2) - (x+2)\bigr]dx$ (value: $\frac92$).
2. $\int_0^2 6x^2dx = 16$.
3. A cylinder of radius 3, length 5: $\pi r^2 h = 45\pi$; disks: $\int_0^5 \pi\cdot 3^2dx = 45\pi$. ✓
4. Shells — strips parallel to the axis keep $f$ as a height and avoid inverting it.
````

### Basic Practice

5. Find the area between $y = x^2$ and $y = 2x + 3$.
6. Find the area enclosed by $y = e^x$, $y = e^{-x}$, and $x = 1$.
7. The region under $y = x^2$ from $0$ to $2$ is rotated about the $x$-axis. Find the volume by disks.
8. Find the area of the region bounded by $x = y^2$ and $x = y + 2$, using horizontal strips.
9. The region of Exercise 7 is instead rotated about the $y$-axis. Find the volume by shells.

````{admonition} Solution to Exercise 8
:class: dropdown
Intersections: $y^2 = y + 2 \Rightarrow (y-2)(y+1) = 0 \Rightarrow y = -1, 2$. Right curve is the line $x = y+2$, left is the parabola $x = y^2$:

$$
A = \int_{-1}^{2}\bigl[(y + 2) - y^2\bigr]dy = \left[\frac{y^2}{2} + 2y - \frac{y^3}{3}\right]_{-1}^{2} = \frac{10}{3} - \left(-\frac{7}{6}\right) = \frac{9}{2}.
$$

Vertical strips would have needed two integrals (the bottom boundary changes at $x=1$); horizontal strips need one. Choosing the slicing direction *is* the solution.
````

### Intermediate Practice

10. Find the volume when the region between $y = \sqrt x$ and $y = \frac{x}{2}$ is rotated about the $x$-axis (washers — find the intersections first).
11. Redo Exercise 10 rotating about the **$y$-axis**, choosing your method, and check both answers with SymPy.
12. A solid has as its base the disk $x^2 + y^2 \le 1$, and cross-sections perpendicular to the $x$-axis are squares (side spanning the disk). Find its volume.
13. Find the volume when the region under $y = \sin x$, $0 \le x \le \pi$, is rotated about the $x$-axis. *(You will need $\sin^2 x = \frac{1-\cos 2x}{2}$ from Chapter 2 — a preview of Chapter 10's methods.)*

````{admonition} Hint for Exercise 12
:class: dropdown
At position $x$ the disk's chord has length $2\sqrt{1-x^2}$; the square on it has area $4(1 - x^2)$. Integrate over $[-1, 1]$. (Answer: $\frac{16}{3}$.)
````

### Conceptual Understanding

14. Explain why the washer method subtracts $\pi r^2$ rather than using radius $R - r$: what physical part of the solid does $\pi r^2\,dx$ represent?
15. The disk and shell computations of §9.6 gave the same $8\pi$ from different integrals, $\pi\int_0^4 x\,dx$ and $2\pi\int_0^2 y(4-y^2)\,dy$. In one paragraph, explain why agreement had to happen and what changing the slicing direction corresponds to.
16. Describe a region and axis for which *neither* pure disks nor pure shells avoids splitting the integral, and explain what feature of the boundary causes it.

### Python Practice

17. Verify Exercises 10–13 with SymPy, and add a Monte Carlo check (as in §9.6) for Exercise 12's square-cross-section solid.
18. Write a function `revolve_volume(f_expr, a, b, axis)` that returns the exact disk (axis `"x"`) or shell (axis `"y"`) volume for the region under `f_expr` on $[a,b]$, and test it against {prf:ref}`ex-disk` and {prf:ref}`ex-shell`.

### Visualization Practice

19. Recreate the left panel of {numref}`fig-disk-solid` for the washer solid of {prf:ref}`ex-washer`: the region between $y=x$ and $y=x^2$ with one representative washer's outer and inner radii drawn and labeled.
20. Using Matplotlib's 3-D toolkit as in the figure script, render the solid of {prf:ref}`ex-shell` (rotate $y = x-x^2$ about the $y$-axis) and confirm visually that it is a bowl-with-rolled-rim shape whose widest material sits near $x = \frac12$ — then connect that observation to where the shell integrand $x(x-x^2)$ peaks.

### Challenge

21. Derive the volume of a sphere of radius $r$ by rotating $y = \sqrt{r^2 - x^2}$ about the $x$-axis, and the volume of a cone of radius $r$ and height $h$ by rotating a suitable line. Confirm the classical formulas $\frac43\pi r^3$ and $\frac13\pi r^2 h$.
22. **Gabriel's horn.** Rotate $y = \frac1x$, $x \ge 1$, about the $x$-axis. Show the volume out to $x = T$ is $\pi\bigl(1 - \frac1T\bigr)$, hence the infinite horn has *finite* volume $\pi$ — and then show its cross-sectional radius decays so slowly that $\int_1^T \frac{2\pi}{x}dx$ (a lower bound for its surface area) grows without bound. An object you could fill with paint but never paint: state precisely which two integrals disagree about being finite, and why.

### Cumulative Review

23. *(Ch. 8)* Evaluate the volume integral $\pi\int_0^{2}x\,e^{-x^2}dx$ (the solid from rotating $y = \sqrt{x}\,e^{-x^2/2}$ about the $x$-axis) by substitution.
24. *(Ch. 6)* The volume of {prf:ref}`ex-disk` as a function of the right endpoint is $V(b) = \pi b^2/2$. Use a linearization at $b = 4$ to estimate the volume if the solid is extended to $b = 4.1$, and compare with the exact value.

## 9.8 Summary

Slicing converts geometry into integrals. Area between curves is $\int(\text{top} - \text{bottom})\,dx$ — or $\int(\text{right} - \text{left})\,dy$ when horizontal strips fit the boundary better — with the interval split at every crossing. Volumes follow from $V = \int A(x)\,dx$ for any solid whose cross-sectional areas are known, which for solids of revolution specializes to disks $\pi R^2$, washers $\pi(R^2 - r^2)$ with radii squared separately and measured from the rotation axis, and shells $2\pi(\text{radius})(\text{height})$ when strips run parallel to the axis. Method choice follows the direction in which boundaries are honest functions. SymPy certifies the algebra, cross-method and Monte Carlo comparisons certify the *setup*, and the slice-approximate-sum-limit template itself — not any single formula — is the transferable content, reappearing in arc length, probability, and the double integrals of Part V.

*Parallel reading:* OpenStax *Calculus Volume 1*, Sections 6.1–6.3 {cite}`openstax_calc1`.
