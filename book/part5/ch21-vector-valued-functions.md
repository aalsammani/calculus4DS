# Chapter 21 · Vector-Valued Functions

Part V reunites the two halves of the course. Parts I–III did calculus on functions with one input and one output; Part IV built the algebra of vectors. Now they merge — beginning with the simplest hybrid, a function whose *input* is a single number (time, usually) and whose *output* is a vector: a moving point. Everything from Part I transfers with almost embarrassing ease — derivatives componentwise, the derivative *is* velocity, integrals recover position — and the payoff is the mathematics of trajectories: orbits, projectiles, robot arms, and (in data terms) any quantity that traces a path through a feature space over time.

## 21.1 Curves as functions

```{prf:definition} Vector-valued function
:label: def-vector-function
A **vector-valued function** assigns to each real $t$ in an interval a vector

$$
\vb r(t) = \langle x(t),\ y(t)\rangle
\quad\text{or}\quad
\vb r(t) = \langle x(t),\ y(t),\ z(t)\rangle,
$$

with **component functions** $x(t), y(t), \ldots$ — ordinary functions of Part I. As $t$ runs, the tip of $\vb r(t)$ traces a **curve**; the function is the curve *plus a schedule* for traversing it (a **parametrization**).
```

The distinction between curve and parametrization matters: $\vb r(t) = \langle\cos t, \sin t\rangle$ and $\vb s(t) = \langle\cos 2t, \sin 2t\rangle$ trace the same unit circle, the second at twice the speed. A curve is a road; a parametrization is a particular drive along it. Familiar examples: the **line** through point $\vb p$ with direction $\vb d$ is $\vb r(t) = \vb p + t\,\vb d$ (Chapter 15's Exercise 10, now official — with $t \in [0,1]$ and $\vb d = \vb q - \vb p$ it traces the segment from $\vb p$ to $\vb q$); the circle of radius $a$ is $\langle a\cos t, a\sin t\rangle$; and the graph of any old-fashioned function $f$ is the special case $\langle t, f(t)\rangle$ — Part I was secretly studying curves that never doubled back.

Limits, continuity, derivatives, and integrals all act **componentwise**, so no genuinely new theory is needed — only new interpretation:

```{prf:definition} Derivative of a vector function
:label: def-vector-derivative
$$
\vb r'(t) = \lim_{h\to0}\frac{\vb r(t+h) - \vb r(t)}{h} = \langle x'(t),\ y'(t),\ z'(t)\rangle.
$$

For a moving point, $\vb r'(t)$ is the **velocity** $\vb v(t)$ — tangent to the curve, pointing in the direction of travel, with magnitude the **speed** $\|\vb r'(t)\|$; the second derivative $\vb r''(t)$ is the **acceleration**.
```

The limit's numerator $\vb r(t+h) - \vb r(t)$ is a chord vector (Chapter 15's tip-minus-tail); dividing by $h$ and shrinking makes the chord swing into tangency — Chapter 3's secant-to-tangent story, replayed with arrows. Note the vocabulary split that one-variable calculus never needed: **velocity** is a vector (direction and rate), **speed** is its scalar magnitude.

```{prf:example} Circular motion, differentiated
:label: ex-circular-motion
For $\vb r(t) = \langle\cos t, \sin t\rangle$, compute velocity, speed, and acceleration, and interpret.

$$
\vb v(t) = \langle -\sin t, \cos t\rangle, \qquad
\|\vb v(t)\| = \sqrt{\sin^2 t + \cos^2 t} = 1, \qquad
\vb a(t) = \langle -\cos t, -\sin t \rangle = -\vb r(t).
$$

Three classical facts drop out. The speed is constant ($1$ radian of arc per unit time — the arc-length meaning of radians from Chapter 2). The velocity is perpendicular to the position — $\vb r\cdot\vb v = -\cos t\sin t + \sin t\cos t = 0$ — tangent to the circle, as {numref}`fig-parametric-motion` shows (this is Chapter 17's Exercise 23, now in its natural home). And the acceleration points *opposite the position*: straight at the center. Uniform circular motion accelerates centripetally not by slowing down but by *turning* — a vector can change with constant magnitude, something one-variable calculus could not even express.
```

```{figure} figures/ch21-parametric-motion.png
:name: fig-parametric-motion
:alt: Left: the unit circle with velocity arrows drawn tangent at three points. Right: a projectile's parabolic arc rising and falling.

Left: circular motion — at each marked time the velocity $\vb r'(t)$ (red) is tangent to the path. Right: projectile motion $\vb r(t) = \langle v_0\cos\alpha\,t,\ v_0\sin\alpha\,t - 4.9t^2\rangle$ for $v_0 = 20$ m/s, $\alpha = 50°$: constant horizontal velocity, uniformly decelerating vertical velocity, a parabola in space.
```

```{prf:example} Projectile motion
:label: ex-projectile
A ball leaves the origin at $v_0 = 20$ m/s, angle $\alpha = 50°$, under gravity $g = 9.8$ m/s². Find its path, flight time, range, and peak height.

Acceleration is the given: $\vb a = \langle 0, -9.8\rangle$. Integrate componentwise (constants fixed by the launch data $\vb v(0) = \langle v_0\cos\alpha,\ v_0\sin\alpha\rangle$, $\vb r(0) = \vb 0$):

$$
\vb v(t) = \langle v_0\cos\alpha,\ v_0\sin\alpha - 9.8t\rangle,
\qquad
\vb r(t) = \bigl\langle v_0\cos\alpha\,t,\ \ v_0\sin\alpha\,t - 4.9t^2\bigr\rangle.
$$

Flight ends when $y = 0$ again: $t\,(v_0\sin\alpha - 4.9t) = 0$ gives $T = \frac{2v_0\sin\alpha}{9.8} \approx 3.13$ s. Range: $x(T) = v_0\cos\alpha\,T \approx 40.2$ m. Peak: where $y'(t) = 0$, i.e. $t = T/2$, height $\frac{(v_0\sin\alpha)^2}{2\cdot 9.8}\approx 12.0$ m. One vector antiderivative did the work of two Part-I problems run in parallel — which is all it is: the components never interact until a question (like "where does it land?") couples them.
```

Differentiation rules transfer componentwise too, with three product rules where one used to be — for a scalar function times a vector function, for dot products, and for cross products:

$$
\frac{d}{dt}\bigl[\vb u\cdot\vb v\bigr] = \vb u'\cdot\vb v + \vb u\cdot\vb v',
\qquad
\frac{d}{dt}\bigl[\vb u\times\vb v\bigr] = \vb u'\times\vb v + \vb u\times\vb v'
$$

(orders preserved in the cross case — Chapter 16's anticommutativity demands it). One elegant dividend: if $\|\vb r(t)\|$ is constant, then $\vb r\cdot\vb r$ is constant, so differentiating gives $2\,\vb r\cdot\vb r' = 0$ — *motion on a sphere is always perpendicular to the position vector*, the general truth behind {prf:ref}`ex-circular-motion`.

## 21.2 Arc length

How far does the point travel? Speed integrated over time:

```{prf:theorem} Arc length
:label: thm-arc-length
The length of the curve traced by $\vb r(t)$, $a \le t \le b$ (traversed once), is

$$
L = \int_a^b \|\vb r'(t)\|\,dt
= \int_a^b \sqrt{x'(t)^2 + y'(t)^2 \,(+\, z'(t)^2)}\;dt.
$$
```

The formula is Chapter 7 in disguise — distance is the integral of speed — and its inner Pythagorean expression is the length of the tiny displacement $\vb r'(t)\,dt$ in each instant: chop the curve into near-straight steps, add their lengths, take the limit. Riemann's recipe, aimed at a curve.

```{prf:example} Two arc lengths
:label: ex-arc-length
**(a) The helix** $\vb r(t) = \langle\cos t, \sin t, t\rangle$, $0 \le t \le 2\pi$ (a spiral staircase: circling while rising).

$$
\vb r'(t) = \langle -\sin t, \cos t, 1\rangle,
\qquad
\|\vb r'\| = \sqrt{\sin^2 t + \cos^2 t + 1} = \sqrt2,
$$

$$
L = \int_0^{2\pi}\sqrt2\,dt = 2\sqrt2\,\pi \approx 8.886.
$$

Constant speed makes the integral trivial — the helix is a circle's worth of horizontal travel and a $2\pi$ rise, combined by Pythagoras.

**(b) The parabola** $\vb r(t) = \langle t, t^2\rangle$, $0\le t\le 1$: here $\|\vb r'\| = \sqrt{1 + 4t^2}$, and

$$
L = \int_0^1\sqrt{1+4t^2}\,dt = \frac{2\sqrt5 + \operatorname{arcsinh} 2}{4} \approx 1.4789
$$

— by the trig substitution $2t = \tan\theta$ of Chapter 10 (or a table). The pattern is typical: arc-length integrands carry square roots, most have no elementary antiderivative (the ellipse's famously doesn't), and numerical integration (Chapter 11) is the standard tool. The *formula* is simple; the *integrals* are where hand methods retire.
```

## 21.3 Common mistakes

```{admonition} Common Mistakes
:class: warning
**Differentiating the magnitude componentwise.** $\|\vb r(t)\|$ is a scalar function built nonlinearly from the components; $\frac{d}{dt}\|\vb r\| \ne \|\vb r'\|$ in general (constant-speed circular motion has $\frac{d}{dt}\|\vb r\| = 0$ but $\|\vb r'\| = 1$). Differentiate components, or use $\frac{d}{dt}\|\vb r\|^2 = 2\vb r\cdot\vb r'$.

**Speed versus velocity.** "The derivative is the speed" is wrong twice: the derivative is the velocity *vector*; its magnitude is the speed.

**Curve = parametrization.** Two functions can trace one curve at different rates; arc length is a property of the *curve* only if each point is traversed once — a parametrization that retraces doubles the integral.

**Dropping components in integration constants.** Each component integration has its *own* constant; the vector constant $\vb C$ in {prf:ref}`ex-projectile` had two entries fixed by two initial conditions.

**Tangent line confusions.** The tangent line at $t_0$ is $\vb r(t_0) + s\,\vb r'(t_0)$ — through the *point*, along the *velocity*; students often anchor it at the origin.

**Degrees again.** Parametrizations with $\cos t$, $\sin t$ presume radians; the derivative rules require it (Chapter 5's warning, permanently in force).
```

## 21.4 Now do it in Python

Componentwise calculus means arrays of components; SymPy differentiates symbolically, NumPy/SciPy handle motion and lengths numerically:

```python
import numpy as np
import sympy as sp

# --- Example 21.3 symbolically ---
t = sp.symbols('t')
r = sp.Matrix([sp.cos(t), sp.sin(t)])
v = r.diff(t)
a = v.diff(t)
print(v.T, a.T, sp.simplify(v.dot(v)))   # [-sin, cos], [-cos, -sin], 1
print(sp.simplify(r.dot(v)))             # 0: velocity ⟂ position

# --- Example 21.4: projectile numerically ---
v0, alpha, g = 20.0, np.radians(50), 9.8
T = 2*v0*np.sin(alpha)/g
print(T, v0*np.cos(alpha)*T, (v0*np.sin(alpha))**2/(2*g))
# 3.1267...  40.196...  11.976...

# --- Example 21.5: arc lengths ---
from scipy.integrate import quad
L_helix, _ = quad(lambda s: np.sqrt(2), 0, 2*np.pi)
L_parab, _ = quad(lambda s: np.sqrt(1 + 4*s**2), 0, 1)
print(L_helix, 2*np.sqrt(2)*np.pi)       # 8.8857...  both
print(L_parab)                            # 1.47894...
```

**Visualization.** Plotting a parametric curve is two lines — evaluate the components on a fine grid of $t$, then `ax.plot(x, y)` — and animating motion is just plotting a marker at increasing $t$. Reproduce {numref}`fig-parametric-motion`'s left panel and add the acceleration arrows: at every point they aim at the center, the centripetal picture drawn by your own code. Then try the **cycloid** $\langle t - \sin t,\ 1 - \cos t\rangle$ (the path of a point on a rolling wheel's rim) and look at its velocity at $t = 0, 2\pi, \ldots$: the point on the rim is momentarily *stationary* each time it touches the ground — a fact your plot will show as cusps and $\|\vb v\| = 0$ will confirm.

**Interpretation.** Reading trajectories through velocity and acceleration vectors is a transferable skill: in data settings, $\vb r(t)$ might be a customer's position in feature space over months, an optimizer's parameter vector over training steps, or a sensor's state over time; "which direction is it heading, and how fast?" is $\vb r'$, and "is the movement turning or settling?" is $\vb r''$. Gradient-descent trajectories in Chapter 23 will be exactly such curves.

```{admonition} Data Science Connection
:class: tip
Training a model *is* a vector-valued function of time: the parameter vector $\vb w(t)$ traces a curve through $\mathbb{R}^p$ as the optimizer runs, its "velocity" is (minus) the gradient, and practitioners routinely diagnose training by curve-reading — oscillation across a valley, slow crawl along one, momentum as velocity smoothing. Elsewhere, parametric curves model everything from GPS tracks (arc length = distance traveled) to Bézier curves in graphics and font rendering, and interpolating between two embeddings $\vb p, \vb q$ by $(1-t)\vb p + t\vb q$ — the humble segment parametrization — is how generative models "morph" one output into another.
```

```{admonition} Looking Ahead
:class: seealso
This chapter varied *time* and watched a vector output. The next varies *space*: functions $f(x, y)$ with a vector input and scalar output — surfaces, contour maps, and the question "how does $f$ change as I move in this direction?", whose answer (Chapter 23) multiplies this chapter's velocity vectors by the next chapter's partial derivatives via a chain rule.
```

## 21.5 Exercises

### Quick Check

1. For $\vb r(t) = \langle t^2, e^{3t}\rangle$: find $\vb r'(t)$ and $\vb r'(0)$.
2. Parametrize the segment from $P(1, 2)$ to $Q(4, 0)$, $0 \le t \le 1$.
3. A particle has constant speed. Must its velocity be constant? Must its acceleration be $\vb 0$?
4. Compute the speed of $\vb r(t) = \langle 3t, 4t\rangle$ and the arc length for $0 \le t \le 2$.

````{admonition} Answers to Quick Checks
:class: dropdown
1. $\langle 2t, 3e^{3t}\rangle$; $\ \langle 0, 3\rangle$.
2. $\vb r(t) = \langle 1, 2\rangle + t\,\langle 3, -2\rangle = \langle 1 + 3t,\ 2 - 2t\rangle$.
3. No and no — circular motion has constant speed but turning velocity and nonzero (centripetal) acceleration.
4. Speed $\|\langle 3,4\rangle\| = 5$; length $\int_0^2 5\,dt = 10$ (a straight segment: rate × time).
````

### Basic Practice

5. For $\vb r(t) = \langle 2\cos t,\ 2\sin t,\ 3t\rangle$: compute velocity, speed, acceleration, and the arc length over $[0, 2\pi]$; verify $\vb a$ has no vertical component and explain why.
6. Find the tangent line to $\vb r(t) = \langle t^2, t^3\rangle$ at $t = 1$, in parametric form.
7. A drone's acceleration is $\vb a(t) = \langle 0, 0, -2\rangle$ with $\vb v(0) = \langle 1, 2, 5\rangle$ and $\vb r(0) = \langle 0,0,10\rangle$. Integrate twice to find $\vb r(t)$, and the time and location of landing ($z = 0$).
8. Verify for $\vb u(t) = \langle t, t^2\rangle$ and $\vb v(t) = \langle \cos t, \sin t\rangle$ that $\frac{d}{dt}[\vb u\cdot\vb v] = \vb u'\cdot\vb v + \vb u\cdot\vb v'$ by computing both sides.

````{admonition} Solution to Exercise 6
:class: dropdown
$\vb r(1) = \langle 1, 1\rangle$ and $\vb r'(t) = \langle 2t, 3t^2\rangle$ so $\vb r'(1) = \langle 2, 3\rangle$:

$$
\boldsymbol\ell(s) = \langle 1, 1\rangle + s\,\langle 2, 3\rangle = \langle 1 + 2s,\ 1 + 3s\rangle.
$$

(As a check, eliminating $s$ gives $y = 1 + \tfrac32(x - 1)$, slope $\tfrac32 = \frac{dy/dt}{dx/dt}\big|_{t=1}$ — the parametric slope formula.)
````

### Intermediate Practice

9. For projectile motion at fixed $v_0$, show the range $R(\alpha) = \frac{v_0^2\sin2\alpha}{g}$ and use Chapter 4's optimization to prove $\alpha = 45°$ maximizes it. What does {prf:ref}`ex-projectile`'s $50°$ range lose relative to the optimum?
10. Prove the constant-magnitude theorem from §21.1 formally — if $\|\vb r(t)\| = c$ for all $t$ then $\vb r\cdot\vb r' \equiv 0$ — and apply it: why must the Earth's orbital velocity be perpendicular to its position vector *only if* the orbit is circular?
11. The cycloid is $\vb r(t) = \langle t - \sin t,\ 1 - \cos t\rangle$. Compute $\vb v(t)$, show the speed is $\sqrt{2 - 2\cos t} = 2\left|\sin\frac t2\right|$ (Chapter 2's half-angle identity), and find the arc length of one arch ($0 \le t \le 2\pi$). *(Answer: 8 — an arch is exactly 8 radii long, a classical gem.)*
12. Two particles: $\vb r_1(t) = \langle t, t^2 \rangle$ and $\vb r_2(t) = \langle 1 + 2t,\ 4t - 1\rangle$. Do their *paths* intersect? Do the *particles* collide? (Different questions — solve them separately.)

### Conceptual Understanding

13. Explain the difference between $\vb r'(t_0)$, the tangent *line* at $t_0$, and the tangent line's direction being non-unique (any multiple works) — connecting to eigen-directions' scale freedom from Chapter 20.
14. Why does reparametrizing a curve (traversing it on a different schedule) change velocity and speed but not arc length? Point to the exact place in {prf:ref}`thm-arc-length` where a substitution absorbs the schedule change.
15. In one paragraph: what could "acceleration" mean for a model's parameter trajectory during training, and why might a practitioner care about its direction relative to the velocity?

### Python Practice

16. Verify Exercises 5–12 (SymPy for derivatives and the half-angle simplification; `quad` for lengths; a fine-grid path plot to settle Exercise 12 visually before solving it algebraically).
17. Write `arc_length(r, a, b)` taking a callable `r(t)` returning an array, estimating length by summing `np.linalg.norm(np.diff(pts, axis=0), axis=1)` over a fine grid. Test against the helix's exact $2\sqrt2\pi$ and report the error at 100, 1000, and 10000 grid points; what convergence order do you observe, and which Chapter 11 rule does this method secretly resemble?

### Visualization Practice

18. Plot the cycloid over three arches with velocity arrows every quarter-period, marking the cusps where speed hits zero; add a small circle at one instant showing the rolling-wheel interpretation if you're feeling ambitious.
19. Plot the 3-D helix of Exercise 5 with `ax.plot(projection='3d')`, coloring the curve by speed (constant — the colorbar should be flat) and then repeat for $\vb r(t) = \langle\cos t, \sin t, t^2/6\rangle$, where the coloring shows acceleration into the climb.

### Challenge

20. **Kepler warm-up.** For motion under a central force, $\vb a(t)$ is always parallel to $\vb r(t)$. Show that $\vb L(t) = \vb r(t)\times\vb v(t)$ is then constant (differentiate with the cross-product rule and use $\vb w \times \vb w = \vb 0$ twice), and interpret: the motion stays in one plane and sweeps area at a constant rate — Kepler's second law, in four lines of vector calculus.
21. **Bézier curves.** The cubic Bézier with control points $\vb p_0, \ldots, \vb p_3$ is $\vb B(t) = (1-t)^3\vb p_0 + 3(1-t)^2t\,\vb p_1 + 3(1-t)t^2\vb p_2 + t^3\vb p_3$. Show $\vb B(0) = \vb p_0$, $\vb B(1) = \vb p_3$, $\vb B'(0) = 3(\vb p_1 - \vb p_0)$ — the curve leaves along the first control edge — and plot one with its control polygon. Every font glyph on your screen is drawn from these.

### Cumulative Review

22. *(Ch. 9–10)* The curve $\langle t, \cosh t\rangle$ (the hanging-chain catenary, with $\cosh t = \frac{e^t + e^{-t}}{2}$) has speed $\sqrt{1 + \sinh^2 t} = \cosh t$. Find the arc length over $[0, 1]$ exactly, and note the rare pleasure: an arc-length integral with a clean antiderivative.
23. *(Ch. 20)* The linear system $\vb x_{k+1} = \mathit A\vb x_k$ of Chapter 20 is a *discrete-time* trajectory. For $\mathit A = \begin{bmatrix}0.96 & -0.20\\ 0.20 & 0.96\end{bmatrix}$ (a slight rotation-with-shrink: eigenvalues $0.96 \pm 0.20i$, magnitude $\approx 0.98$), iterate 200 steps from $\langle 1, 0\rangle$ and plot the points. Describe the curve and connect its inward spiral to the eigenvalue magnitude.

## 21.6 Summary

A vector-valued function $\vb r(t)$ is a moving point: componentwise limits, derivatives, and integrals need no new theory, but gain new meaning — $\vb r'$ is the velocity vector (tangent, direction of travel), its magnitude the speed, $\vb r''$ the acceleration, with product rules for scalar, dot, and cross combinations and the constant-magnitude corollary $\vb r\cdot\vb r' = 0$ for motion on circles and spheres. Integrating acceleration twice with vector constants reconstructs trajectories (projectiles: parabolas from $\langle 0, -g\rangle$); curves are distinct from their parametrizations (roads versus drives), and the distance driven is arc length $\int\|\vb r'\|\,dt$ — Riemann's sum of tiny Pythagorean steps, exactly computable for helices and cycloids, numerically for almost everything else. In code: SymPy differentiates component matrices, `quad` handles the square-root integrands, and parametric plots with velocity arrows turn trajectory-reading — including the optimizer trajectories of machine learning — into a visual skill. Next: many inputs, one output — surfaces and partial derivatives.

*Parallel reading:* OpenStax *Calculus Volume 3*, Sections 3.1–3.3 {cite}`openstax_calc3`.
