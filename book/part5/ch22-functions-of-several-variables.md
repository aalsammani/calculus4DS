# Chapter 22 · Functions of Several Variables and Partial Derivatives

Real quantities rarely depend on one input. A house price depends on area *and* location *and* age; a model's loss depends on every one of its parameters; the temperature in a room depends on where you stand. This chapter begins calculus for such functions — several inputs, one output — with the two tools that make them tractable: pictures (surfaces and contour maps) and **partial derivatives**, which resurrect all of Part I by the simple discipline of changing one variable at a time. The chapter ends with the multivariable chain rule, which composes these rates exactly as Chapter 5 composed one-variable ones — and which is, under the name *backpropagation*, the algorithm that trains every neural network.

## 22.1 The objects and their pictures

```{prf:definition} Function of several variables
:label: def-multivar-function
A **function of two variables** assigns to each point $(x, y)$ in a domain $D \subseteq \mathbb{R}^2$ a real number $z = f(x, y)$; likewise $f(x, y, z)$, and in general $f(\vb x)$ for $\vb x \in \mathbb{R}^n$ — a scalar-valued function of a vector input.
```

Two visualizations carry the subject, both shown in {numref}`fig-surface-contours` for $f(x,y) = x^2 + y^2$:

**The graph** is the surface $z = f(x, y)$ floating over the domain — for $x^2 + y^2$, a bowl (paraboloid). Beautiful, but hard to read quantitatively and unavailable beyond two inputs.

**The contour map** draws, in the flat domain, the **level curves** $f(x, y) = c$ for a ladder of constants $c$ — the topographic-map idea, where each curve is a horizontal slice of the surface projected down. For the bowl these are concentric circles ($x^2 + y^2 = c$), tightening as $c$ grows. Contour reading is a skill worth deliberate practice: **closely spaced contours mean steep terrain** (the function changes a lot over a short walk), widely spaced contours mean flat; closed loops surround peaks or pits; and — the shape to memorize — contours that *cross* in an X mark a **saddle**, terrain that rises in one direction and falls in another, as $z = x^2 - y^2$ does at the origin ({numref}`fig-saddle`).

```{figure} figures/ch22-surface-contours.png
:name: fig-surface-contours
:alt: Left: a three-dimensional bowl-shaped surface. Right: its contour map, concentric circles labeled with heights, spaced more tightly away from the center.

The paraboloid $z = x^2 + y^2$ as a surface and as a contour map. Each circle is one horizontal slice; the tightening spacing outward records the bowl's steepening walls.
```

```{figure} figures/ch22-saddle.png
:name: fig-saddle
:alt: Left: a saddle-shaped surface rising along x and falling along y. Right: its contour map, hyperbolas in four sectors with the level-zero lines crossing at the origin.

The saddle $z = x^2 - y^2$: uphill along the $x$-axis, downhill along the $y$-axis. On the contour map, the $c = 0$ level is a pair of crossed lines — the X signature by which saddles are recognized in any contour plot, including the loss landscapes of machine learning.
```

For three or more inputs the graph is gone (it would need four dimensions), and level *sets* become surfaces; but the algebra — and everything that follows in this chapter — continues verbatim. High-dimensional intuition is built exactly this way: master the two-variable pictures, then trust the formulas.

A one-paragraph honesty note on **limits**: continuity for $f(x,y)$ requires $f(x,y) \to f(a,b)$ along *every* path into $(a,b)$, and with infinitely many approach paths this can genuinely fail — the standard specimen $f(x,y) = \frac{xy}{x^2+y^2}$ approaches $0$ along either axis but $\frac12$ along the line $y = x$, so it has *no* limit at the origin (Exercise 13 explores it). The functions of daily practice — polynomials, exponentials, and their compositions, away from division by zero — are continuous, and this course proceeds on that basis; the specimen stands as a reminder that "plug in" carries real assumptions.

## 22.2 Partial derivatives

The one-variable derivative asked: how does the output respond to nudging the input? With several inputs, nudge **one at a time**:

```{prf:definition} Partial derivatives
:label: def-partial
The **partial derivatives** of $f$ at $(a, b)$ are

$$
\frac{\partial f}{\partial x}(a,b) = f_x(a,b) = \lim_{h\to0}\frac{f(a+h,\ b) - f(a,b)}{h},
\qquad
\frac{\partial f}{\partial y}(a,b) = f_y(a,b) = \lim_{h\to0}\frac{f(a,\ b+h) - f(a,b)}{h}
$$

— the ordinary derivative in one variable *with every other variable frozen*. The curly $\partial$ signals that other inputs exist and are being held fixed.
```

Computationally this is wonderful news: **no new rules**. To find $f_x$, treat $y$ as a constant and differentiate with Part I's toolkit; for $f_y$, freeze $x$. Geometrically, $f_x(a,b)$ is the slope of the surface sliced by the vertical plane $y = b$ — the pitch of the terrain walking due east — and $f_y$ the slope walking due north. (Slopes in *other* directions are Chapter 23's business.)

```{prf:example} Computing partials
:label: ex-partials
For $f(x, y) = x^2 y + \sin(xy)$, find both partials.

Freezing $y$ (so $y$ and $\sin(\cdot)$'s inner $y$ are constants, chain rule as usual):

$$
f_x = 2xy + y\cos(xy).
$$

Freezing $x$:

$$
f_y = x^2 + x\cos(xy).
$$

Note the symmetry of method and the asymmetry of results — each partial keeps the differentiated variable's structure and carries the frozen one along as a passenger. Every rule from Chapters 4–5 (product, quotient, chain) applies unchanged within each partial.
```

```{prf:example} Partials as sensitivities
:label: ex-partial-sensitivity
A cylindrical tank's volume is $V(r, h) = \pi r^2 h$. Compute and interpret both partials at $r = 2$, $h = 5$ (meters).

$V_r = 2\pi r h = 20\pi \approx 62.8$ m³ per meter of radius; $V_h = \pi r^2 = 4\pi \approx 12.6$ m³ per meter of height. At this size, the volume is roughly five times more sensitive to radius than to height — the "which knob matters most?" question, answered by comparing partials, is the workhorse reasoning of engineering tolerance analysis and of feature-importance thinking in modeling. (Units discipline from Chapter 3 carries over: each partial's units are output units per *that* input's units.)
```

**Higher partials** iterate the process: $f_{xx} = \partial_x(f_x)$, $f_{yy}$, and the mixed $f_{xy} = \partial_y(f_x)$ and $f_{yx}$. A small miracle simplifies the bookkeeping:

```{prf:theorem} Clairaut's theorem
:label: thm-clairaut
If the mixed partials $f_{xy}$ and $f_{yx}$ are continuous, they are equal: $f_{xy} = f_{yx}$ — the order of differentiation does not matter.
```

For {prf:ref}`ex-partials`: $f_{xy} = \partial_y(2xy + y\cos xy) = 2x + \cos xy - xy\sin xy$, and differentiating $f_y$ with respect to $x$ gives the identical expression (Exercise 6 has you confirm). Consequently the second-order information of $f(x,y)$ fits in a *symmetric* $2\times2$ matrix $\begin{bmatrix}f_{xx} & f_{xy}\\ f_{xy} & f_{yy}\end{bmatrix}$ — the **Hessian**, whose symmetry hands it to Chapter 20's spectral theorem and whose eigenvalues will classify the bowls and saddles of the figures above. The pieces of the course are beginning to interlock.

## 22.3 Linearization: the tangent plane

Chapter 6's best idea — near a point, replace the function by its tangent line — generalizes with one word changed: tangent *plane*.

```{prf:definition} Linearization
:label: def-tangent-plane
The **linearization** of $f$ at $(a, b)$ is

$$
L(x, y) = f(a,b) + f_x(a,b)\,(x - a) + f_y(a,b)\,(y - b),
$$

whose graph $z = L(x,y)$ is the **tangent plane** to the surface at $(a, b, f(a,b))$. For $(x,y)$ near $(a,b)$, $f(x,y) \approx L(x,y)$.
```

The structure is exactly Chapter 6's $f(a) + f'(a)(x-a)$ with one correction term *per input*: each variable's nudge, priced at its own partial, contributions added. (That additivity of small changes — $\Delta f \approx f_x\Delta x + f_y\Delta y$ — is the practical heart of the definition, and of error-propagation formulas throughout the sciences.)

```{prf:example} Estimating with a tangent plane
:label: ex-tangent-plane
Estimate $\sqrt{3.1^2 + 3.9^2}$ by linearizing $f(x,y) = \sqrt{x^2 + y^2}$ at $(3, 4)$.

$f(3,4) = 5$, and $f_x = \frac{x}{\sqrt{x^2+y^2}}$, $f_y = \frac{y}{\sqrt{x^2+y^2}}$ give $f_x(3,4) = \tfrac35$, $f_y(3,4) = \tfrac45$:

$$
L(3.1,\ 3.9) = 5 + 0.6\,(0.1) + 0.8\,(-0.1) = 5 - 0.02 = 4.98.
$$

True value: $\sqrt{9.61 + 15.21} = \sqrt{24.82} = 4.98197\ldots$ — the estimate is off by $2\times10^{-3}$, the quadratic-order error of any linearization. Note the pleasant geometry of the partials: $\langle \tfrac35, \tfrac45\rangle$ is the *unit vector toward $(3,4)$* — distance from the origin grows at rate $1$ moving radially, less in other directions. Chapter 23 will name that observation.
```

## 22.4 The chain rule, multivariable edition

Suppose $z = f(x, y)$ while $x$ and $y$ themselves move in time — $x(t)$, $y(t)$, a Chapter 21 trajectory through the domain. How fast does $z$ change? Each input contributes its own chain-rule term, and the contributions add:

```{prf:theorem} Chain rule (curve through a field)
:label: thm-multivar-chain
If $z = f(x, y)$ with $x = x(t)$, $y = y(t)$ differentiable,

$$
\frac{dz}{dt} = \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt}.
$$

More generally, if $z = f(x, y)$ with $x = x(s,t)$, $y = y(s,t)$, then $\dfrac{\partial z}{\partial t} = \dfrac{\partial f}{\partial x}\dfrac{\partial x}{\partial t} + \dfrac{\partial f}{\partial y}\dfrac{\partial y}{\partial t}$, and likewise for $s$ — **one term per path** from output to the ultimate input, each term a product of the rates along that path.
```

The linearization explains why: over an instant $dt$, the inputs shift by $dx = x'\,dt$ and $dy = y'\,dt$, and $\Delta f \approx f_x\,dx + f_y\,dy$ prices the combined effect. The "sum over paths" phrasing scales to any web of dependencies — draw the dependency tree, multiply down each branch, add the branches.

```{prf:example} Rates along a trajectory
:label: ex-chain-multivar
The temperature on a plate is $T(x,y) = x^2 y$ (degrees), and a sensor moves along $x = \cos t$, $y = \sin t$. How fast is its temperature reading changing at $t = \frac{\pi}{4}$?

$$
\frac{dT}{dt} = \underbrace{2xy}_{T_x}\cdot\underbrace{(-\sin t)}_{x'} + \underbrace{x^2}_{T_y}\cdot\underbrace{\cos t}_{y'}
= -2\cos t\sin^2 t + \cos^3 t.
$$

At $t = \frac\pi4$ (so $\cos t = \sin t = \frac{\sqrt2}{2}$): $\ \frac{dT}{dt} = -2\cdot\frac{\sqrt2}{2}\cdot\frac12 + \frac{2\sqrt2}{8} = -\frac{\sqrt2}{2} + \frac{\sqrt2}{4} = -\frac{\sqrt2}{4} \approx -0.354$ degrees per unit time: the sensor is moving into cooler territory, and the two terms show why — the shrinking $x$ (first term, negative) currently outweighs the growing $y$'s benefit. Reading a chain-rule sum term by term, as credit assignment among the inputs, is precisely the skill backpropagation automates.
```

## 22.5 Common mistakes

```{admonition} Common Mistakes
:class: warning
**Forgetting what's frozen.** In $f_x$, the variable $y$ is a *constant everywhere it appears* — including inside compositions ($\partial_x \sin(xy) = y\cos(xy)$, not $\cos(xy)$) and as exponents. The most common slip is differentiating $y$'s appearances "a little."

**$\partial$ versus $d$.** Write $\partial$ for partials of multivariable functions and reserve $\frac{d}{dt}$ for genuine one-variable rates (like the chain rule's output). Mixing them muddles what is held fixed — which is the entire content of the symbol.

**Missing chain-rule terms.** $\frac{dz}{dt}$ needs one term per input that depends on $t$; dropping the $f_y\,y'$ term is the multivariable analogue of Chapter 5's forgotten inner derivative. Draw the tree.

**Assuming the surface picture too hard.** Level curves live in the *domain* (no $z$-axis); the surface lives above it. Marking "the maximum" on a contour map means finding the innermost loop, not the highest curve on the page.

**"No limit" versus "limit I can't compute."** Path-dependence ({prf:ref} two-path checks) can *disprove* a limit; agreeing along two paths proves nothing (all paths must agree). Continuity of the everyday function catalog is what licenses plugging in.

**Tangent-plane misuse at distance.** $L(x,y)$ is trustworthy only near $(a,b)$; the error grows quadratically with the step, exactly as in Chapter 6, and no plane tracks a curved surface for long.
```

## 22.6 Now do it in Python

SymPy takes partials by naming the variable; NumPy's `meshgrid` powers every surface and contour plot; and numerical partials are one-sided quotients away:

```python
import numpy as np
import sympy as sp

x, y, t = sp.symbols('x y t')

# --- Example 22.3 ---
f = x**2*y + sp.sin(x*y)
print(sp.diff(f, x))     # 2*x*y + y*cos(x*y)
print(sp.diff(f, y))     # x**2 + x*cos(x*y)
print(sp.simplify(sp.diff(f, x, y) - sp.diff(f, y, x)))    # 0: Clairaut

# --- Example 22.5: linearization check ---
g = sp.sqrt(x**2 + y**2)
L = g.subs({x: 3, y: 4}) \
    + sp.diff(g, x).subs({x: 3, y: 4})*(x - 3) \
    + sp.diff(g, y).subs({x: 3, y: 4})*(y - 4)
print(L.subs({x: 3.1, y: 3.9}), g.subs({x: 3.1, y: 3.9}).evalf())
# 4.98000...  4.98196...

# --- Example 22.6: chain rule, symbolically and numerically ---
T = x**2*y
dTdt = sp.diff(T.subs({x: sp.cos(t), y: sp.sin(t)}), t)
print(sp.simplify(dTdt.subs(t, sp.pi/4)))    # -sqrt(2)/4

# --- Numerical partial (the definition, executable) ---
fn = lambda x_, y_: x_**2*y_ + np.sin(x_*y_)
h = 1e-6
fx_num = (fn(1 + h, 2) - fn(1, 2)) / h
print(fx_num, 2*1*2 + 2*np.cos(2))           # 3.1677...  both
```

**Visualization.** The `meshgrid` idiom is the key move — build a grid of $(x, y)$ pairs, evaluate $f$ on all of them at once, and hand the arrays to `plot_surface` or `contour`:

```python
import matplotlib.pyplot as plt
xs = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(xs, xs)
Z = X**2 - Y**2
fig, ax = plt.subplots()
cs = ax.contour(X, Y, Z, levels=15)
ax.clabel(cs); ax.set_aspect("equal"); plt.show()
```

**Interpretation.** Generate the saddle's contour map yourself and find the X at the origin; then contour $f(x,y) = \sin x \sin y$ over $[-\pi, \pi]^2$ and read off, before computing anything, where the peaks, pits, and saddles sit and along which lines the terrain is flat. Contour literacy transfers directly to the loss-landscape plots ubiquitous in machine learning papers — those figures *are* this figure, with parameters for axes and loss for height.

```{admonition} Data Science Connection
:class: tip
"Holding everything else fixed" is the partial derivative's phrase, and it is also regression's: a fitted linear model's coefficient on feature $j$ *is* $\partial \hat y/\partial x_j$, the predicted response to a unit change in that feature with the others held fixed — along with all the interpretive care that caveat demands when features co-move. Sensitivity analysis ({prf:ref}`ex-partial-sensitivity` at industrial scale), the error-propagation formula $\sigma_f^2 \approx f_x^2\sigma_x^2 + f_y^2\sigma_y^2$ of measurement science, and the saliency maps that ask "which pixels most affect this classification?" are all partial derivatives doing their one job: pricing one input's influence at a time.
```

```{admonition} Looking Ahead
:class: seealso
Partials measure change along the two axis directions only. Chapter 23 packages them into a single vector — the **gradient** $\nabla f = \langle f_x, f_y\rangle$ — and shows it answers every direction at once: the chain rule of this chapter becomes a dot product $\nabla f\cdot \vb r'(t)$, the direction of steepest ascent falls out of Chapter 16's angle formula, and machine learning's fundamental algorithm (follow $-\nabla f$) is three definitions away.
```

## 22.7 Exercises

### Quick Check

1. Compute both partials of $f(x,y) = 3x^2y^4$ and evaluate at $(1, 1)$.
2. On a contour map, what do tightly packed contours indicate? What does an X-crossing indicate?
3. For $f(x,y) = e^{xy}$: find $f_x$, then $f_{xy}$.
4. If $z = f(x,y)$ with $x = 2t$ and $y = t^2$, write $\frac{dz}{dt}$ (unevaluated, in terms of partials).

````{admonition} Answers to Quick Checks
:class: dropdown
1. $f_x = 6xy^4$, $f_y = 12x^2y^3$; at $(1,1)$: $6$ and $12$.
2. Steep terrain; a saddle point.
3. $f_x = ye^{xy}$; $f_{xy} = e^{xy} + xye^{xy}$ (product rule — $y$ appears twice).
4. $\frac{dz}{dt} = 2f_x + 2t\,f_y$.
````

### Basic Practice

5. Find all first partials: (a) $f(x,y) = x^3 - 3xy^2 + 2y$; (b) $f(x,y) = \frac{x}{x + y}$; (c) $f(x,y,z) = xz\,e^{y} + \ln(x^2 + 1)$; (d) $f(x,y) = \arctan(y/x)$.
6. For {prf:ref}`ex-partials`'s function, compute $f_{xx}$, $f_{yy}$, and both mixed partials, confirming Clairaut; assemble the Hessian matrix at $(1, 0)$ and verify it is symmetric.
7. Find the tangent plane to $z = x^2 + 3xy$ at $(1, 2)$ and use it to estimate $f(1.05,\ 1.9)$; compare with the exact value.
8. A rectangular box's diagonal is $d(x,y,z) = \sqrt{x^2 + y^2 + z^2}$. If measurements $x = 3$, $y = 4$, $z = 12$ each carry up to $0.05$ of error, use $\Delta d \approx d_x\Delta x + d_y\Delta y + d_z\Delta z$ (worst case: all errors aligned) to bound the diagonal's error.

````{admonition} Solution to Exercise 7
:class: dropdown
$f(1,2) = 1 + 6 = 7$; $f_x = 2x + 3y \Rightarrow f_x(1,2) = 8$; $f_y = 3x \Rightarrow 3$:

$$
L(x,y) = 7 + 8(x - 1) + 3(y - 2), \qquad L(1.05, 1.9) = 7 + 0.4 - 0.3 = 7.1.
$$

Exact: $1.05^2 + 3(1.05)(1.9) = 1.1025 + 5.985 = 7.0875$ — the plane overshoots by $0.0125$, quadratically small in the step.
````

### Intermediate Practice

9. For the ideal-gas law $P(V, T) = \frac{nRT}{V}$, compute $P_V$ and $P_T$, interpret each with units, and verify the curious identity $\frac{\partial P}{\partial V}\frac{\partial V}{\partial T}\frac{\partial T}{\partial P} = -1$ (each factor computed from the appropriate solved form) — a warning that partial-derivative symbols do not cancel like fractions.
10. Apply the two-variable chain rule: $z = \ln(x^2 + y^2)$ with $x = e^t$, $y = e^{-t}$. Compute $\frac{dz}{dt}$, simplify (Chapter 2's hyperbolic-flavored algebra helps), and evaluate the limit as $t \to \infty$; explain the limit from the geometry of the path.
11. With $z = f(x, y)$, $x = s + t$, $y = s - t$, show $\frac{\partial z}{\partial s}\frac{\partial z}{\partial t} = f_x^2 - f_y^2$ — chain rule with two independent variables, and a first taste of how coordinate changes transform derivative expressions (Chapter 25's theme).
12. Verify that $u(x, t) = \sin(x - ct)$ satisfies the **wave equation** $u_{tt} = c^2 u_{xx}$, and that $u(x,t) = \frac{1}{\sqrt t}e^{-x^2/(4t)}$ satisfies the **heat equation** $u_t = u_{xx}$ (Chapter 14's Exercise 21, met from the other side). Partial differential equations — laws relating a function's partials — are where much of applied mathematics lives.
13. For $f(x,y) = \frac{xy}{x^2+y^2}$ (with $f(0,0) = 0$): compute the limit along the $x$-axis, the $y$-axis, and the line $y = mx$; conclude the two-path verdict; then (surprise) show both partials $f_x(0,0)$ and $f_y(0,0)$ *exist* and equal $0$. Partials existing is weaker than continuity — the axes just happen to be tame paths.

### Conceptual Understanding

14. Explain to a non-mathematician what $f_y(a,b)$ means on a topographic map, and why "the slope of the terrain" is an incomplete phrase until a direction is chosen.
15. Clairaut's theorem makes the Hessian symmetric. Using Chapter 20's spectral theorem, say what that guarantees about the Hessian's eigenvalues and eigenvectors — and speculate (correctly) about what sign patterns of those eigenvalues should mean at a bowl bottom versus a saddle.
16. A regression on strongly correlated features reports $\partial\hat y/\partial x_1 = 5$. Why does the partial's "holding $x_2$ fixed" clause make real-world interpretation delicate when $x_1$ and $x_2$ never vary independently in the data?

### Python Practice

17. Verify Exercises 5–13 in SymPy (for 13, use `sp.limit` along parametrized paths). For 8, also estimate the error bound by direct evaluation at the worst corner and compare with the linear estimate.
18. Write `grad_numeric(f, p, h=1e-6)` returning the vector of one-sided difference quotients of a callable `f(np.array)` at point `p` (loop over coordinates, perturb one at a time). Test it on {prf:ref}`ex-partials` at $(1, 2)$ against SymPy, and keep it — Chapter 23 uses it to check gradients, and gradient-checking is a real debugging practice in ML engineering.

### Visualization Practice

19. Produce surface-plus-contour figures (as in {numref}`fig-surface-contours`) for $f(x,y) = \sin x\sin y$ and for $f(x,y) = x^2 + 2y^2$ (Chapter 23's running example). On each contour map, mark every peak, pit, and saddle you can identify by eye.
20. Plot the surface $z = x^2 + 3xy$ near $(1,2)$ together with its tangent plane from Exercise 7 (both via `plot_surface`, the plane semi-transparent), on two zoom levels: a wide view where they visibly separate and a tight view where they merge — Chapter 6's zoom-in linearity, one dimension up.

### Challenge

21. **Least squares by partials.** For data $(1,2), (2,2.5), (3,4)$, the loss $L(m, b) = \sum_i (mx_i + b - y_i)^2$ is a function of two variables. Compute $L_m$ and $L_b$, set both to zero, solve the resulting $2\times2$ linear system (Chapter 18), and confirm against `np.polyfit(x, y, 1)`. You have just derived the normal equations by hand — the multivariable-calculus route to the formula Chapter 18 stated.
22. **Laplace's equation.** Show that $f(x,y) = \ln(x^2 + y^2)$ satisfies $f_{xx} + f_{yy} = 0$ away from the origin, and likewise $f(x,y) = e^x\cos y$. Functions with this property (harmonic functions) have the remarkable mean-value property — the value at a point equals the average on any circle around it; verify it numerically for $e^x\cos y$ at the origin with a 1000-point circle average.

### Cumulative Review

23. *(Ch. 6)* Newton's method for *two* equations $f(x,y) = 0$, $g(x,y) = 0$ updates by solving $\begin{bmatrix}f_x & f_y\\ g_x & g_y\end{bmatrix}\Delta = -\langle f, g\rangle$ (Chapter 18's Exercise 24, now computable). Run two iterations by hand for $f = x^2 + y^2 - 4$, $g = xy - 1$ from $(2, 1)$, and check the residuals shrink.
24. *(Ch. 13)* The two-variable Taylor expansion begins $f \approx L(x,y) + \tfrac12\bigl[f_{xx}(x-a)^2 + 2f_{xy}(x-a)(y-b) + f_{yy}(y-b)^2\bigr]$. Write the quadratic term as $\tfrac12\,\vb h^{\mathsf T}\mathit H\,\vb h$ with $\vb h = \langle x - a,\ y-b\rangle$ and $\mathit H$ the Hessian — one matrix expression replacing three terms, and the form in which optimization theory always writes it.

## 22.8 Summary

A function $f(x,y)$ is pictured twice — as a surface and as a contour map, with spacing encoding steepness and X-crossings marking saddles — and differentiated one input at a time: partial derivatives freeze all other variables and reuse Part I's rules wholesale, measuring axis-direction slopes and one-at-a-time sensitivities. Mixed second partials commute (Clairaut), making the Hessian symmetric and eigen-ready. The linearization $L = f + f_x\Delta x + f_y\Delta y$ is the tangent plane — one correction term per input, quadratic error, the engine of estimation and error propagation. The chain rule composes rates along any dependency web — one term per path, multiply along, add across — computing rates along trajectories now and powering backpropagation later. Limits can be path-dependent (two disagreeing paths refute one), but the everyday function catalog is continuous. In code: `sp.diff(f, x)`, `meshgrid` + `contour`/`plot_surface`, and numerical difference quotients for gradient checking. Next: all the partials in one vector, and the best direction to move.

*Parallel reading:* OpenStax *Calculus Volume 3*, Sections 4.1–4.5 {cite}`openstax_calc3`.
