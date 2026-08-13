# Chapter 7 · Antiderivatives, the Definite Integral, and the Fundamental Theorem

Part I asked: given a function, what is its rate of change? Part II asks the reverse: given a rate of change, what is the function — and given a function, what does it *accumulate*? These sound like two different questions. The astonishment at the heart of calculus, and of this chapter, is that they are the same question, a fact called the Fundamental Theorem of Calculus. It converts the hard geometric problem of area into the algebraic problem of undoing derivatives.

## 7.1 Antiderivatives: differentiation in reverse

```{prf:definition} Antiderivative
:label: def-antiderivative
A function $F$ is an **antiderivative** of $f$ on an interval if $F'(x) = f(x)$ for every $x$ in the interval.
```

For $f(x) = 2x$, the function $F(x) = x^2$ qualifies, since $(x^2)' = 2x$. But so do $x^2 + 5$ and $x^2 - \pi$: adding any constant leaves the derivative unchanged. That is the *only* freedom — two antiderivatives of the same function on an interval differ by a constant (if $F' = G'$ then $(F - G)' = 0$, and only constants have zero derivative on an interval). We therefore write the **general antiderivative**, or **indefinite integral**, with an arbitrary constant:

$$
\int f(x)\,dx = F(x) + C.
$$

The $+C$ is not bureaucratic decoration; it records that the rate $f$ determines the function $F$ only up to knowing one value — a starting point. Velocity determines a trip's displacement, not where the trip began.

Every derivative formula from Part I, read right to left, is now an integral formula. The essential table:

$$
\begin{array}{ll}
\displaystyle\int x^n\,dx = \frac{x^{n+1}}{n+1} + C \quad (n \neq -1),
& \displaystyle\int \frac{1}{x}\,dx = \ln|x| + C,\\[10pt]
\displaystyle\int e^x\,dx = e^x + C,
& \displaystyle\int b^x\,dx = \frac{b^x}{\ln b} + C,\\[10pt]
\displaystyle\int \cos x\,dx = \sin x + C,
& \displaystyle\int \sin x\,dx = -\cos x + C,\\[10pt]
\displaystyle\int \sec^2 x\,dx = \tan x + C,
& \displaystyle\int \frac{1}{1+x^2}\,dx = \arctan x + C.
\end{array}
$$

The power rule for integrals — *raise the exponent by one, divide by the new exponent* — reverses the power rule for derivatives, and its excluded case $n = -1$ is exactly where $\ln|x|$ steps in (the absolute value extends the formula to negative $x$, where $\frac{d}{dx}\ln(-x) = \frac{1}{x}$ as well). Linearity carries over too: $\int (af + bg)\,dx = a\!\int\! f\,dx + b\!\int\! g\,dx$.

```{prf:example} Basic antiderivatives
:label: ex-antiderivative-basic
Evaluate $\displaystyle\int \left(6x^2 - \frac{4}{x^3} + 5\right)dx$.

Rewrite as powers, integrate term by term:

$$
\int\bigl(6x^2 - 4x^{-3} + 5\bigr)\,dx
= 6\cdot\frac{x^3}{3} - 4\cdot\frac{x^{-2}}{-2} + 5x + C
= 2x^3 + \frac{2}{x^2} + 5x + C.
$$

**Always verify by differentiating:** $\frac{d}{dx}\bigl[2x^3 + 2x^{-2} + 5x\bigr] = 6x^2 - 4x^{-3} + 5$. ✓ Differentiation is easy and checking is free; make it a reflex.
```

```{prf:example} Recovering a function from its rate and one value
:label: ex-ivp
An object moves with velocity $v(t) = 3t^2 - 4t + 1$ m/s, starting at position $s(0) = 2$ m. Find $s(t)$.

Position is an antiderivative of velocity: $s(t) = t^3 - 2t^2 + t + C$. The initial condition selects $C$: $s(0) = C = 2$, so

$$
s(t) = t^3 - 2t^2 + t + 2.
$$

One rate plus one anchor value determines the whole trajectory — the pattern behind every differential-equation model you will meet later.
```

## 7.2 The definite integral: accumulation as a limit

Change perspective from *undoing* to *accumulating*. What is the area under the curve $y = x^2$ from $x=0$ to $x=1$? No formula from geometry applies to a curved boundary. The strategy — one of the oldest in mathematics — is to approximate with shapes we can handle: slice $[0,1]$ into $n$ strips of width $\Delta x = \frac1n$, erect a rectangle on each with height taken from the function, and add.

```{figure} figures/ch07-riemann-sums.png
:name: fig-riemann-sums
:alt: Three panels showing the parabola x squared on the unit interval covered by ten rectangles using left endpoints, midpoints, and right endpoints, with computed sums 0.2850, 0.3325, and 0.3850.

Riemann sums for $\int_0^1 x^2\,dx$ with $n = 10$. Left endpoints underestimate ($0.2850$), right endpoints overestimate ($0.3850$), midpoints nearly hit the target ($0.3325$). The true area, $\tfrac13 = 0.3333\ldots$, is squeezed in between, and all three sums converge to it as $n\to\infty$.
```

The sum of rectangle areas, $\sum_{k=1}^{n} f(x_k^*)\,\Delta x$ with $x_k^*$ a sample point in the $k$-th strip, is a **Riemann sum**. Refining the slicing pins the area down: with midpoints, $n = 10$ gives $0.33250$, $n = 100$ gives $0.3333250$, $n = 1000$ gives $0.33333325$ — visibly converging to $\tfrac13$.

```{prf:definition} Definite integral
:label: def-definite-integral
The **definite integral** of $f$ from $a$ to $b$ is the limit of Riemann sums as the slicing refines:

$$
\int_a^b f(x)\,dx \;=\; \lim_{n\to\infty} \sum_{k=1}^{n} f(x_k^*)\,\Delta x,
$$

when this limit exists (it does for every continuous $f$). The numbers $a, b$ are the **limits of integration**; $f$ is the **integrand**; $dx$ names the integration variable and echoes the width $\Delta x$ of a vanishing strip.
```

Where $f$ dips below the axis, its rectangles have negative heights, so the integral counts **signed area**: area above the axis minus area below. That is a feature, not a defect — accumulated quantities (net displacement, net profit, net charge) genuinely cancel.

```{figure} figures/ch07-signed-area.png
:name: fig-signed-area
:alt: One full period of the sine curve with the hump above the axis shaded green and labeled plus two, the hump below shaded red and labeled minus two.

$\int_0^{2\pi}\sin x\,dx = 0$: the positive hump ($+2$) and negative hump ($-2$) cancel exactly. Total *distance* along the curve is a different question with a different integral ($\int|\sin x|\,dx = 4$).
```

Basic properties follow directly from the sum picture: the integral is linear; it splits over subintervals, $\int_a^b = \int_a^c + \int_c^b$; reversing the limits flips the sign, $\int_b^a = -\int_a^b$; and $\int_a^a f = 0$.

## 7.3 The Fundamental Theorem of Calculus

Computing limits of Riemann sums directly is heroic and unsustainable. The escape route comes from an unexpected direction: study accumulated area *as a function of its right endpoint* and ask how it changes.

```{figure} figures/ch07-accumulation.png
:name: fig-accumulation
:alt: Two stacked panels. Top: the curve t squared with the area under it shaded from zero up to a movable right endpoint. Bottom: the accumulated area plotted as a function of that endpoint, tracing the cubic x cubed over three.

Top: the shaded area under $f(t)=t^2$ from $0$ to a movable endpoint $x$. Bottom: that accumulated area as a function $A(x)$. How fast does the shaded region grow as the boundary sweeps right? At rate equal to the curve's current height — which is the Fundamental Theorem.
```

Let $A(x) = \int_a^x f(t)\,dt$. Nudge the endpoint from $x$ to $x + h$: the area gains a sliver of width $h$ and height essentially $f(x)$, so $A(x+h) - A(x) \approx f(x)\,h$, giving $\frac{A(x+h)-A(x)}{h} \approx f(x)$ — and in the limit, exactly. Accumulation differentiates back to the accumulated function.

```{prf:theorem} Fundamental Theorem of Calculus
:label: thm-ftc
Let $f$ be continuous on $[a, b]$.

**Part 1.** The accumulation function $A(x) = \displaystyle\int_a^x f(t)\,dt$ is differentiable, and

$$A'(x) = f(x).$$

**Part 2.** If $F$ is *any* antiderivative of $f$, then

$$
\int_a^b f(x)\,dx = F(b) - F(a) \;\eqqcolon\; F(x)\Big|_a^b.
$$
```

Part 1 says accumulation and differentiation are inverse processes. Part 2 is its practical payoff, and it follows in two lines: $A$ and $F$ are both antiderivatives of $f$, hence differ by a constant, and evaluating that constant at $x=a$ (where $A(a) = 0$) gives $A(b) = F(b) - F(a)$. The area problem — a limit of thousands of rectangles — collapses to *find an antiderivative, evaluate it twice, subtract*.

```{prf:example} The Riemann-sum labor, redone in one line
:label: ex-ftc-basic
Evaluate $\displaystyle\int_0^1 x^2\,dx$.

An antiderivative of $x^2$ is $\frac{x^3}{3}$, so

$$
\int_0^1 x^2\,dx = \frac{x^3}{3}\bigg|_0^1 = \frac13 - 0 = \frac13,
$$

confirming exactly what the Riemann sums in {numref}`fig-riemann-sums` were crawling toward. No $+C$ is needed in definite integrals — any constant would cancel in the subtraction.
```

```{prf:example} A trigonometric definite integral
:label: ex-ftc-trig
Evaluate $\displaystyle\int_0^{\pi/2} \bigl(2\cos x - \sin x\bigr)\,dx$.

$$
\Bigl[\,2\sin x + \cos x\,\Bigr]_0^{\pi/2}
= \bigl(2\cdot 1 + 0\bigr) - \bigl(0 + 1\bigr) = 1.
$$

Note both signs carefully: the antiderivative of $-\sin x$ is $+\cos x$. Evaluating at the *lower* limit and subtracting is where most arithmetic slips occur; write both evaluations out.
```

```{prf:example} Net change from a rate
:label: ex-net-change
Water drains from a tank at the rate $r(t) = 20 - 4t$ liters per minute (valid for $0 \le t \le 5$). How much water leaves during the first three minutes?

The net amount is the accumulated rate:

$$
\int_0^3 (20 - 4t)\,dt = \Bigl[\,20t - 2t^2\,\Bigr]_0^3 = 60 - 18 = 42 \text{ liters}.
$$

This **net change theorem** reading of FTC Part 2 — the integral of a rate over $[a,b]$ is the total change over $[a,b]$ — is how integrals most often appear in applications: rate in, total out.
```

```{prf:example} Differentiating an accumulation function
:label: ex-ftc-part1
Find $\dfrac{d}{dx}\displaystyle\int_2^{x} \sqrt{1 + t^3}\,dt$ and $\dfrac{d}{dx}\displaystyle\int_0^{x^2} \sin(t^2)\,dt$.

The first is FTC Part 1 verbatim: the derivative is the integrand evaluated at the endpoint, $\sqrt{1 + x^3}$ — no antiderivative required (none exists in elementary form, and the theorem does not care). The second has a *chain*: with $A(u) = \int_0^u \sin(t^2)\,dt$, the target is $A(x^2)$, so

$$
\frac{d}{dx}A(x^2) = A'(x^2)\cdot 2x = \sin\bigl(x^4\bigr)\cdot 2x.
$$

FTC Part 1 composes with the chain rule exactly like any other derivative fact.
```

## 7.4 Common mistakes

```{admonition} Common Mistakes
:class: warning
**Dropping the $+C$** in indefinite integrals — or, conversely, carrying it into definite ones. Indefinite: family of functions, needs $C$. Definite: a single number, no $C$.

**The power rule where it doesn't apply.** $\int x^{-1}dx$ is $\ln|x| + C$, not $\frac{x^0}{0}$. And $\int e^x dx = e^x + C$, not $\frac{e^{x+1}}{x+1}$ — the power rule is for $x^{\text{const}}$, nothing else.

**Sign errors with sine and cosine.** $\int \sin = -\cos$, $\int\cos = +\sin$. Two seconds of differentiation checks either.

**Treating the integral as always-positive area.** $\int_0^{2\pi}\sin x\,dx = 0$; geometric area requires integrating $|f|$ or splitting at the zero crossings.

**Evaluating only at the top limit.** $F(b) - F(a)$ needs both. When $a = 0$ it is tempting to skip $F(0)$; do the evaluation anyway ($F(0)$ is frequently *not* zero — see $\cos$).

**Integrating across a discontinuity.** $\int_{-1}^{1}\frac{dx}{x^2}$ is *not* $\bigl[-x^{-1}\bigr]_{-1}^1 = -2$ (a negative "area" under a positive function — impossible). FTC's hypothesis is continuity on the whole interval; here the integrand blows up at $0$ and the integral in fact diverges.
```

## 7.5 Now do it in Python

Three tools, three roles: SymPy finds antiderivatives symbolically and evaluates definite integrals exactly; NumPy builds Riemann sums so you can *watch* the definition converge; SciPy's `quad` is the production-grade numerical integrator {cite}`virtanen2020scipy`.

```python
import numpy as np
import sympy as sp
from scipy.integrate import quad

x = sp.symbols('x')

# --- Verify Examples 7.2 and 7.5-7.7 symbolically ---
print(sp.integrate(6*x**2 - 4/x**3 + 5, x))        # 2*x**3 + 5*x + 2/x**2
print(sp.integrate(x**2, (x, 0, 1)))               # 1/3, exactly
print(sp.integrate(2*sp.cos(x) - sp.sin(x), (x, 0, sp.pi/2)))   # 1
print(sp.integrate(20 - 4*x, (x, 0, 3)))           # 42

# --- Watch the Riemann definition converge (midpoint rule) ---
f = lambda t: t**2
for n in [10, 100, 1000, 10_000]:
    edges = np.linspace(0, 1, n + 1)
    mids = (edges[:-1] + edges[1:]) / 2
    print(n, np.sum(f(mids)) * (1/n))    # -> 0.3325, 0.333325, ...

# --- Production numerical integration ---
val, err_estimate = quad(f, 0, 1)
print(val, err_estimate)                 # 0.33333..., ~3.7e-15
```

The Riemann loop is deliberately naive — it *is* {prf:ref}`def-definite-integral`, executed. Watching `0.3325 → 0.333325 → 0.33333325` march toward $1/3$ makes the limit definition tangible in a way no proof can. `quad`, by contrast, reaches machine precision instantly using the adaptive descendants of methods you will meet in Chapter 11, and returns an error estimate alongside the value — read it.

**Visualization.** FTC Part 1 can be *seen* by plotting an accumulation function next to a numerical derivative of it:

```python
import matplotlib.pyplot as plt

f = np.cos
xs = np.linspace(0, 2*np.pi, 400)
A = np.array([quad(f, 0, xi)[0] for xi in xs])   # A(x) = ∫₀ˣ cos t dt

fig, axes = plt.subplots(2, 1, sharex=True, figsize=(7, 5))
axes[0].plot(xs, A, color="tab:green", label=r"$A(x)=\int_0^x \cos t\,dt$")
axes[0].plot(xs, np.sin(xs), "k:", lw=1, label=r"$\sin x$ (they coincide)")
axes[0].legend()
axes[1].plot(xs, np.gradient(A, xs), color="tab:red", label=r"$A'(x)$ numerically")
axes[1].plot(xs, f(xs), "k:", lw=1, label=r"$\cos x$")
axes[1].legend(); axes[1].set_xlabel("x")
plt.show()
```

**Interpretation.** The top panel shows the accumulated area under cosine tracing out the sine curve — FTC Part 2 with a moving endpoint. The bottom panel differentiates the accumulation numerically and recovers the cosine — FTC Part 1, verified by machine. Accumulate, then differentiate: you get back what you started with.

```{admonition} Data Science Connection
:class: tip
Integrals are how probability is *extracted* from continuous models: if $p(x)$ is a probability density, then $\int_a^b p(x)\,dx$ is the probability of landing in $[a,b]$, the CDF is precisely the accumulation function $P(x) = \int_{-\infty}^x p(t)\,dt$, and FTC Part 1 is the familiar statistical fact that the density is the derivative of the CDF. Expected values, the AUC metric for classifiers, and the normalizing constants of Bayesian inference are all definite integrals — mostly computed by the numerical methods of Chapter 11, since (as with $e^{-x^2}$) closed-form antiderivatives are a luxury.
```

```{admonition} Looking Ahead
:class: seealso
FTC makes integration only as easy as *finding antiderivatives* — which, unlike differentiation, is genuinely hard: there is no mechanical recipe, and some elementary functions have no elementary antiderivative at all. Chapters 8 and 10 build the two main techniques (substitution, integration by parts) by reversing the chain and product rules; Chapter 11 handles the rest numerically.
```

## 7.6 Exercises

### Quick Check

1. Give the general antiderivative of $x^4$, of $\frac1x$, of $\cos x$, of $e^x$.
2. Evaluate $\displaystyle\int_1^3 2x\,dx$ mentally.
3. If $\int_0^5 f = 12$ and $\int_0^2 f = 7$, what is $\int_2^5 f$?
4. What is $\dfrac{d}{dx}\displaystyle\int_0^x e^{-t^2}dt$?

````{admonition} Answers to Quick Checks
:class: dropdown
1. $\frac{x^5}{5}+C$; $\ \ln|x|+C$; $\ \sin x + C$; $\ e^x + C$.
2. $x^2\big|_1^3 = 9 - 1 = 8$.
3. $12 - 7 = 5$ (splitting property).
4. $e^{-x^2}$ (FTC Part 1; no antiderivative needed or available).
````

### Basic Practice

5. Find each indefinite integral, and check one of them by differentiating:
   (a) $\displaystyle\int (x^3 - 6x + 2)\,dx$;  (b) $\displaystyle\int \left(\sqrt{x} + \frac{1}{\sqrt{x}}\right)dx$;  (c) $\displaystyle\int \frac{3}{x}\,dx$;  (d) $\displaystyle\int (4e^x + \sin x)\,dx$;  (e) $\displaystyle\int \frac{x^2 + 1}{x^2}\,dx$ *(divide first)*.
6. Evaluate each definite integral by FTC:
   (a) $\displaystyle\int_0^2 (3x^2 - 2x)\,dx$;  (b) $\displaystyle\int_1^4 \frac{1}{\sqrt x}\,dx$;  (c) $\displaystyle\int_0^{\pi} \sin x\,dx$;  (d) $\displaystyle\int_1^e \frac{1}{x}\,dx$.
7. A car's velocity is $v(t) = 30 + 2t$ m/s. How far does it travel between $t = 0$ and $t = 10$ seconds?
8. Solve the initial-value problem: $f'(x) = 6x^2 - 1$ with $f(1) = 4$.

````{admonition} Solution to Exercise 6(c)
:class: dropdown
$$
\int_0^{\pi}\sin x\,dx = \bigl[-\cos x\bigr]_0^{\pi} = (-\cos\pi) - (-\cos 0) = (1) - (-1) = 2.
$$

One arch of sine has area exactly $2$ — a number worth remembering, and the benchmark integral for Chapter 11's error experiments.
````

### Intermediate Practice

9. Compute the *signed* area and the *geometric* (total) area between $f(x) = x^2 - 4$ and the $x$-axis on $[0, 3]$. *(Split at the zero crossing.)*
10. Find $\dfrac{d}{dx}\displaystyle\int_x^{5} \ln(1+t^2)\,dt$ and $\dfrac{d}{dx}\displaystyle\int_1^{\sin x} \sqrt{1+t^4}\,dt$.
11. Marginal cost for producing the $x$-th unit is $C'(x) = 0.03x^2 - 2x + 40$ dollars/unit, and fixed costs are $C(0) = 500$. Find the total cost function $C(x)$ and the cost of the first 20 units, $C(20) - C(0)$.
12. Without computing either integral, explain which is larger: $\int_0^1 x^2\,dx$ or $\int_0^1 x^3\,dx$, then verify by FTC.

````{admonition} Hint for Exercise 9
:class: dropdown
$x^2 - 4 = 0$ at $x=2$. Signed: $\int_0^3(x^2-4)dx$. Geometric: $-\int_0^2(x^2-4)\,dx + \int_2^3(x^2-4)\,dx$ — flip the sign of the below-axis piece. (Answers: $-3$ and $\frac{16}{3} + \frac{7}{3} = \frac{23}{3}$.)
````

### Conceptual Understanding

13. Explain in your own words why *every* continuous function has an antiderivative, even ones like $e^{-x^2}$ with no elementary formula for it. *(FTC Part 1 is the answer; say why.)*
14. State precisely what is wrong with the computation $\int_{-1}^{1} x^{-2}\,dx = \bigl[-x^{-1}\bigr]_{-1}^{1} = -1 - 1 = -2$ and what the correct conclusion about this integral is.
15. Your teammate says: "the integral of velocity is distance traveled." Refine the statement so it is exactly correct, distinguishing displacement from distance.

### Python Practice

16. Verify Exercises 5 and 6 with SymPy. For 6(d), confirm SymPy returns exactly $1$ and explain why $\int_1^e \frac{dx}{x} = 1$ is, in a precise sense, the *definition* of $e$ working backwards.
17. Write `riemann(f, a, b, n, rule)` supporting `"left"`, `"right"`, `"mid"`, and produce the convergence table of §7.5 for $\int_0^{\pi}\sin x\,dx = 2$. How large must $n$ be for the midpoint rule's error to drop below $10^{-6}$?

### Visualization Practice

18. Reproduce the essence of {numref}`fig-signed-area` for $f(x) = x^3 - x$ on $[-1.5, 1.5]$: shade positive and negative regions in different colors and annotate each with its (FTC-computed) signed area.
19. Plot the accumulation function $A(x) = \int_0^x (t^2 - 1)\,dt$ on $[-2.5, 2.5]$ (via `quad` in a loop or its exact formula $\frac{x^3}{3} - x$) beneath a plot of the integrand, and mark where $A$ has local extrema. What feature of the *integrand* sits at those points, and why does FTC Part 1 predict it?

### Challenge

20. Evaluate $\displaystyle\lim_{n\to\infty}\sum_{k=1}^{n}\frac{k^3}{n^4}$ by recognizing it as a Riemann sum of a specific integral.
21. Define $\operatorname{Si}(x) = \int_0^x \frac{\sin t}{t}\,dt$ (with the integrand's removable hole at $0$ filled by the value $1$, courtesy of Chapter 3). Using only FTC Part 1 and Part I tools, find where $\operatorname{Si}$ has its first local maximum for $x>0$, then plot $\operatorname{Si}$ numerically on $[0, 20]$ and describe its long-run behavior.

### Cumulative Review

22. *(Ch. 5)* Differentiate $F(x) = e^{-x}\sin x$; then write the corresponding antiderivative statement $\int(\ldots)dx = e^{-x}\sin x + C$ that your computation has just established.
23. *(Ch. 6)* Use a linearization of $F(x) = \int_0^x \sqrt{1+t^3}\,dt$ at $a = 2$ to estimate $F(2.1)$, given $F(2) \approx 3.2412$. *(FTC Part 1 hands you $F'(2)$.)*

## 7.7 Summary

An antiderivative of $f$ is any $F$ with $F' = f$; all antiderivatives on an interval differ by a constant, giving the indefinite integral $\int f\,dx = F(x) + C$, with a table obtained by reading Part I's derivative formulas backwards ($n=-1$ handled by $\ln|x|$). The definite integral $\int_a^b f\,dx$ is the limit of Riemann sums — signed area, accumulated quantity — and exists for every continuous integrand. The Fundamental Theorem joins the two ideas: accumulation functions differentiate back to the integrand (Part 1), and consequently definite integrals evaluate by $F(b) - F(a)$ for any antiderivative (Part 2), turning geometry into algebra. Read as the net change theorem, $\int_a^b(\text{rate}) = \text{total change}$. In code: SymPy integrates exactly, hand-built Riemann sums animate the definition, and `scipy.integrate.quad` delivers machine-precision values with error estimates. What remains — and it is a genuine craft — is *finding* antiderivatives, which the next chapters take up.

*Parallel reading:* OpenStax *Calculus Volume 1*, Sections 4.10 and 5.1–5.4 {cite}`openstax_calc1`.
