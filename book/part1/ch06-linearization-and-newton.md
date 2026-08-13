# Chapter 6 · Linearization and Newton's Method

This chapter cashes in the derivative for its two most practical dividends. The first, **linearization**, exploits the defining fact about tangent lines — that they hug their curve — to replace complicated functions by lines, locally, with controllable error. The second, **Newton's method**, iterates that replacement to solve equations that have no algebraic solution, and does so with astonishing speed. Between them these ideas power calculators, numerical libraries, and the optimization routines that train statistical models; they are the first place in the course where calculus stops describing and starts *computing*.

## 6.1 Linear approximation

Zoom in on the graph of a differentiable function at a point and it straightens: at sufficient magnification, curve and tangent line become indistinguishable. Linearization takes this seriously as a computational method — near the point of tangency, *use the line instead of the curve*.

```{prf:definition} Linearization
:label: def-linearization
The **linearization** of a differentiable function $f$ at the point $a$ is the tangent-line function

$$
L(x) = f(a) + f'(a)\,(x - a),
$$

and the **linear approximation** is the estimate $f(x) \approx L(x)$ for $x$ near $a$.
```

The formula is the point-slope equation of the tangent line, rearranged to read as a recipe: *start at the known value $f(a)$, then correct by the rate $f'(a)$ times the displacement $x - a$.*

```{prf:example} Approximating a square root by hand
:label: ex-lin-sqrt
Estimate $\sqrt{4.2}$ without a calculator.

Choose a nearby point where the function is easy: $a = 4$, where $f(x) = \sqrt x$ gives $f(4) = 2$ and, by Chapter 3, $f'(x) = \frac{1}{2\sqrt x}$ so $f'(4) = \frac14$. The linearization is

$$
L(x) = 2 + \tfrac14(x - 4),
$$

and therefore

$$
\sqrt{4.2} \approx L(4.2) = 2 + \tfrac14(0.2) = 2.05.
$$

The true value is $\sqrt{4.2} = 2.04939\ldots$; the estimate is off by about $0.0006$, an error of $0.03\%$, for the cost of one multiplication.
```

```{figure} figures/ch06-linearization.png
:name: fig-linearization
:alt: The square root curve with its tangent line at the point four comma two. Near the point of tangency the two are visually indistinguishable; markers at x equals 4.2 show the true value on the curve and the estimate on the line almost coinciding.

Linearization of $\sqrt{x}$ at $a = 4$. Near the point of tangency the tangent line and the curve agree so closely that the true value $\sqrt{4.2}$ (square marker) and the estimate $L(4.2)$ (triangle) nearly coincide. Farther from $a$, the gap — the approximation error — visibly opens.
```

```{prf:example} Small-angle approximation
:label: ex-lin-sin
Linearize $f(x) = \sin x$ at $a = 0$.

$f(0) = 0$ and $f'(0) = \cos 0 = 1$, so $L(x) = 0 + 1\cdot(x - 0) = x$:

$$
\sin x \approx x \quad \text{for small } x \text{ (radians)}.
$$

At $x = 0.1$: $\sin(0.1) = 0.099833\ldots$ versus the approximation $0.1$ — agreement to three decimal places. This *small-angle approximation* is a workhorse of physics and engineering, and it restates the limit $\lim_{x\to0}\frac{\sin x}{x}=1$ of Chapter 3 in approximation language. Note it fails in degrees ($\sin 10° \approx 0.17$, nowhere near $10$): the radian convention is what makes the tangent slope equal $1$.
```

```{prf:example} Sensitivity via differentials
:label: ex-differentials
A sphere's radius is measured as $r = 10$ cm with possible error $\pm 0.1$ cm. Estimate the resulting error in the computed volume $V = \tfrac43\pi r^3$.

The linear approximation, written in increment form $\Delta V \approx V'(r)\,\Delta r$ (the **differential** form $dV = V'(r)\,dr$), gives with $V'(r) = 4\pi r^2$:

$$
\Delta V \approx 4\pi(10)^2(0.1) = 40\pi \approx 125.7 \text{ cm}^3.
$$

Against a volume of $V(10) = \tfrac{4000\pi}{3} \approx 4188.8$ cm³, that is a relative error of about $3\%$ — three times the $1\%$ relative error in $r$, and the factor of three is no accident: taking logs of $V = \tfrac43\pi r^3$ and differentiating gives $\frac{\Delta V}{V} \approx 3\,\frac{\Delta r}{r}$. Cubing an input triples its *relative* uncertainty. Propagating measurement error through formulas this way is a small preview of a large subject.
```

### How good is the approximation?

The error $f(x) - L(x)$ is governed by the **second** derivative: the tangent line matches $f$ in value and slope at $a$, so what it misses is curvature. The precise statement (proved via Taylor's theorem in Chapter 13) is that for $x$ near $a$,

$$
\bigl|f(x) - L(x)\bigr| \;\le\; \frac{M}{2}\,(x-a)^2,
\qquad M = \max \bigl|f''\bigr| \text{ between } a \text{ and } x.
$$

Two features deserve attention now. The error scales like $(x-a)^2$ — halving the distance quarters the error, which is why linearization is superb close-in and useless far away. And the constant involves $f''$: functions with small curvature linearize well. In {prf:ref}`ex-lin-sqrt`, $f''(x) = -\tfrac14 x^{-3/2}$ has magnitude at most $\tfrac14\cdot 4^{-3/2} = \tfrac{1}{32}$ on $[4, 4.2]$, so the bound predicts an error at most $\tfrac{1}{64}(0.2)^2 = 0.000625$ — and the actual error $0.00061$ sits just under it. The mathematics not only estimates but certifies.

## 6.2 Newton's method

Linearization approximates values. Turned sideways, it solves equations. Suppose we need a root of $f(x) = 0$ — a point where the graph crosses the axis — and algebra offers no formula. Newton's idea: from a guess $x_0$, replace the curve by its tangent line at $x_0$ and solve *the line's* root exactly, which takes one step of algebra. That root, generally much closer to the true one, becomes the next guess, and the process repeats.

The tangent at $x_n$ is $y = f(x_n) + f'(x_n)(x - x_n)$; setting $y = 0$ and solving for $x$:

```{prf:definition} Newton's method
:label: def-newton
Given $f$ differentiable and an initial guess $x_0$, iterate

$$
x_{n+1} \;=\; x_n - \frac{f(x_n)}{f'(x_n)},
$$

stopping when successive iterates (or $|f(x_n)|$) are smaller than a chosen tolerance.
```

```{figure} figures/ch06-newton.png
:name: fig-newton
:alt: The parabola x squared minus 2 with tangent lines drawn at successive Newton iterates starting from x equals two; each tangent's axis crossing lands visibly closer to the starred true root at square root of two.

Two steps of Newton's method on $f(x) = x^2 - 2$ from $x_0 = 2$. Each tangent line's crossing with the axis (triangles) becomes the next iterate, sliding rapidly toward the true root $\sqrt2$ (star).
```

```{prf:example} Computing $\sqrt 2$ by hand
:label: ex-newton-sqrt2
Solve $x^2 - 2 = 0$ by Newton's method from $x_0 = 2$.

With $f(x) = x^2 - 2$ and $f'(x) = 2x$, the iteration simplifies pleasantly:

$$
x_{n+1} = x_n - \frac{x_n^2 - 2}{2x_n} = \frac{x_n}{2} + \frac{1}{x_n}
\quad\text{(average of } x_n \text{ and } 2/x_n\text{)}.
$$

By hand: $x_1 = 1 + \tfrac12 = 1.5$; then $x_2 = 0.75 + \tfrac{1}{1.5} = 0.75 + 0.666\overline{6} = 1.41\overline{6}$. Already correct to two decimals after two steps. The full progression, with errors against $\sqrt2 = 1.41421356\ldots$:

| $n$ | $x_n$ | error |
|---|---|---|
| 0 | $2.000000000000$ | $5.9\times10^{-1}$ |
| 1 | $1.500000000000$ | $8.6\times10^{-2}$ |
| 2 | $1.416666666667$ | $2.5\times10^{-3}$ |
| 3 | $1.414215686275$ | $2.1\times10^{-6}$ |
| 4 | $1.414213562375$ | $1.6\times10^{-12}$ |

Watch the error's *exponents*: roughly $-1, -2, -3, -6, -12$. Each step approximately **doubles the number of correct digits** — the signature of *quadratic convergence*, which holds whenever the root is simple ($f' \neq 0$ there) and the start is reasonably close. Four steps here deliver more precision than any physical measurement can use. (This particular iteration — average $x$ with $2/x$ — was known to the Babylonians; Newton's derivation via tangents explains *why* it works and generalizes it to every equation.)
```

```{prf:example} An equation with no algebraic solution
:label: ex-newton-transcendental
Find the solution of $\cos x = x$.

No algebra will isolate $x$; but the solution is a root of $f(x) = \cos x - x$, with $f'(x) = -\sin x - 1$. A sketch (or the intermediate value theorem: $f(0) = 1 > 0$, $f(1) = \cos 1 - 1 < 0$) locates a root in $(0, 1)$; take $x_0 = 1$. Then

$$
x_1 = 1 - \frac{\cos 1 - 1}{-\sin 1 - 1} = 1 - \frac{-0.459698}{-1.841471} = 1 - 0.249636 = 0.750364,
$$

and continuing (by the same arithmetic, done in §6.4's code): $x_2 = 0.739113$, $x_3 = 0.739085$, at which point $x_4$ agrees with $x_3$ to all twelve printed digits. The unique real solution of $\cos x = x$ is $x = 0.739085\ldots$ — a number with no closed form, delivered to machine precision in three steps.
```

### When Newton misbehaves

The method's speed comes with conditions. If $f'(x_n) \approx 0$, the tangent is nearly horizontal and its root lands far away — iterates can shoot off wildly (try $f(x) = x^2 - 2$ from $x_0 = 0.01$ and watch $x_1 = 100.005$). A poor starting guess can converge to a *different* root than intended, cycle, or diverge. And at a repeated root (where $f$ and $f'$ vanish together, as for $f(x) = (x-1)^2$), convergence degrades from quadratic to merely linear. Practical use therefore pairs Newton's method with a bracketing sanity check or a plot; production root-finders such as SciPy's `brentq` combine Newton-like speed with guaranteed-convergence safeguards {cite}`burden_faires`.

## 6.3 Common mistakes

```{admonition} Common Mistakes
:class: warning
**Linearizing at the wrong point.** The expansion point $a$ must be where $f$ and $f'$ are *known exactly* — to estimate $\sqrt{4.2}$, expand at $4$, not at $4.2$. If your $L(x)$ contains the very quantity you are estimating, restart.

**Using $L$ far from $a$.** The error grows like $(x-a)^2$; the tangent line to $\sqrt x$ at $4$ estimates $\sqrt{9}$ as $3.25$ — off by $8\%$. Linearization is a *local* tool, and "how local" is exactly what the error bound quantifies.

**Sign slips in the Newton update.** The formula *subtracts* $f(x_n)/f'(x_n)$. Adding it drives iterates away from the root. If your errors grow, check this first.

**Stopping on the wrong criterion.** "$f(x_n)$ is small" and "$x_n$ has stopped moving" are different conditions; a very flat function can make the first true far from a root. Robust code checks both.

**Forgetting radians once more.** In {prf:ref}`ex-newton-transcendental`, $\cos 1$ means the cosine of one radian ($0.5403$), not of one degree.
```

## 6.4 Now do it in Python

Newton's method is four lines of Python, and writing it yourself — once — is worth more than any number of library calls.

```python
import numpy as np

def newton(f, fprime, x0, tol=1e-12, max_iter=50):
    """Newton's method; returns the iterate history so convergence is visible."""
    xs = [x0]
    for _ in range(max_iter):
        x = xs[-1]
        step = f(x) / fprime(x)
        xs.append(x - step)
        if abs(step) < tol:
            break
    return xs

# --- Verify Example 6.5: sqrt(2), reproducing the hand table ---
xs = newton(lambda x: x**2 - 2, lambda x: 2*x, x0=2.0)
for n, x in enumerate(xs):
    print(f"x_{n} = {x:.12f}   error = {abs(x - np.sqrt(2)):.3e}")

# --- Verify Example 6.6: the root of cos(x) = x ---
xs = newton(lambda x: np.cos(x) - x, lambda x: -np.sin(x) - 1, x0=1.0)
print([f"{x:.6f}" for x in xs])       # 1.0, 0.750364, 0.739113, 0.739085, ...

# --- Verify Example 6.2: linear approximation of sqrt(4.2) ---
L = lambda x: 2 + (x - 4)/4
print(L(4.2), np.sqrt(4.2))           # 2.05 vs 2.049390...
```

The first block reproduces the error table of {prf:ref}`ex-newton-sqrt2` digit for digit; the second confirms $0.739085$; the third shows estimate and truth side by side. SymPy supplies the derivative when differentiating by hand would be tedious, closing the loop between this chapter and the last:

```python
import sympy as sp

x = sp.symbols('x')
f_expr = sp.cos(x) - x
fp_expr = sp.diff(f_expr, x)                       # -sin(x) - 1, automatically
f  = sp.lambdify(x, f_expr)
fp = sp.lambdify(x, fp_expr)
print(newton(f, fp, 1.0)[-1])                      # 0.7390851332151607
```

**Visualization.** Convergence speed is best seen on a log scale, where quadratic convergence appears as an error curve that plunges ever more steeply:

```python
import matplotlib.pyplot as plt

xs = newton(lambda t: t**2 - 2, lambda t: 2*t, 2.0)
errors = [abs(t - np.sqrt(2)) for t in xs[:-1]]
plt.semilogy(range(len(errors)), errors, "o-")
plt.xlabel("iteration $n$"); plt.ylabel("error $|x_n - \\sqrt{2}|$")
plt.title("Quadratic convergence: correct digits double each step")
plt.show()
```

**Interpretation.** On the log axis the points fall along a curve whose downward slope *steepens* — linear convergence would give a straight line, quadratic gives this accelerating dive. Five markers span twelve orders of magnitude. When you later meet optimization algorithms advertised as "Newton-type," this plot is the performance they are promising, and its price — needing derivatives, needing a decent start — is the trade they are managing.

```{admonition} Data Science Connection
:class: tip
Training a model means minimizing a loss function, and minima live where derivatives vanish — so optimization is root-finding for $f'$. Applying Newton's method to $f'$ gives the **Newton optimization step** $x_{n+1} = x_n - f'(x_n)/f''(x_n)$, the one-dimensional ancestor of the second-order methods used to fit logistic regression and gradient-boosted trees. Linearization, meanwhile, is the daily currency of applied work: "the model's sensitivity to this input," error propagation as in {prf:ref}`ex-differentials`, and gradient descent itself — which follows the linear approximation downhill in many dimensions (Chapter 23).
```

```{admonition} Looking Ahead
:class: seealso
Linearization is the first rung of a ladder: matching value and slope gives the tangent line; matching curvature too gives a quadratic; continuing gives the **Taylor polynomials** of Chapter 13, with the error bound of §6.1 as the first case of Taylor's remainder theorem. Newton's method reappears there as well, seen through Taylor's lens, and again in many dimensions in Part V.
```

## 6.5 Exercises

### Quick Check

1. Write the linearization of $f(x) = x^3$ at $a = 2$.
2. Using $L(x) = x$ for $\sin x$ near $0$, estimate $\sin(0.05)$.
3. One Newton step for $f(x) = x^2 - 9$ from $x_0 = 4$ gives what $x_1$?
4. True or false: if Newton's method converges, it always converges to the root nearest the starting guess.

````{admonition} Answers to Quick Checks
:class: dropdown
1. $f(2) = 8$, $f'(2) = 12$: $L(x) = 8 + 12(x-2)$.
2. $\sin(0.05) \approx 0.05$ (true value $0.0499792$).
3. $x_1 = 4 - \frac{16-9}{8} = 4 - 0.875 = 3.125$ (heading for the root $3$).
4. False — a tangent can vault the iterate across the graph to a distant root; nearness gives no guarantee.
````

### Basic Practice

5. Find the linearization of each function at the given point, then use it to estimate the given value:
   (a) $f(x) = \sqrt{x}$ at $a = 25$; estimate $\sqrt{26}$.
   (b) $f(x) = \ln x$ at $a = 1$; estimate $\ln(1.1)$.
   (c) $f(x) = x^{1/3}$ at $a = 27$; estimate $\sqrt[3]{26}$.
6. Carry out two Newton steps *by hand* (fractions welcome) for $f(x) = x^3 - 5$ from $x_0 = 2$, and compare with $5^{1/3} = 1.70998$.
7. A cube's side is measured as $5.0$ cm with error at most $\pm0.02$ cm. Use differentials to estimate the maximum error in the computed volume, and express it as a relative error.

````{admonition} Solution to Exercise 5(b)
:class: dropdown
$f(1) = 0$, $f'(x) = 1/x$ so $f'(1) = 1$: $L(x) = x - 1$, giving $\ln(1.1) \approx 0.1$. True value $0.09531$. The approximation $\ln(1+u)\approx u$ for small $u$ is used constantly in statistics and finance (log-returns), and this exercise is its derivation.
````

````{admonition} Solution to Exercise 6
:class: dropdown
$f'(x) = 3x^2$. Step 1: $x_1 = 2 - \frac{8-5}{12} = 2 - \frac14 = \frac74 = 1.75$. Step 2: $f(1.75) = 5.359375 - 5 = 0.359375$, $f'(1.75) = 9.1875$, so

$$
x_2 = 1.75 - \frac{0.359375}{9.1875} = 1.75 - 0.039116 = 1.710884.
$$

Error after two steps: $|1.710884 - 1.709976| \approx 9.1\times10^{-4}$.
````

### Intermediate Practice

8. For $f(x) = \sqrt{1+x}$: find the linearization at $a=0$, use it to estimate $\sqrt{1.06}$, and then use the error bound of §6.1 with $M = \max|f''|$ on $[0, 0.06]$ to give a guaranteed bracket for the true value.
9. The equation $x^3 - x - 2 = 0$ has exactly one real root. Locate it in an interval of length 1 using sign changes, then find it to six decimal places with Newton's method (by calculator or code), reporting your iterates.
10. Show that applying Newton's method to $f(x) = x^2 - c$ (for $c>0$) gives the iteration $x_{n+1} = \frac12\left(x_n + \frac{c}{x_n}\right)$, and explain in one sentence why the iterate is always between $x_n$ and $c/x_n$.
11. Try Newton's method on $f(x) = x^{1/3}$ (root at $0$) starting from $x_0 = 1$: compute $x_1$ and $x_2$ symbolically. What is happening, and which hypothesis of good behavior is violated?

````{admonition} Hint for Exercise 11
:class: dropdown
With $f' = \frac13 x^{-2/3}$, the update is $x_{n+1} = x_n - \frac{x_n^{1/3}}{\frac13 x_n^{-2/3}} = x_n - 3x_n = -2x_n$. The iterates alternate sign and *double* in magnitude — divergence. The vertical tangent at the root ($f'$ unbounded) breaks the method.
````

### Conceptual Understanding

12. Explain why the linearization error involves $f''$ and not $f'$: what feature of the function does the tangent line already capture perfectly, and what is the first feature it misses?
13. Two functions pass through $(3, 7)$ with slope $2$ there; one has $|f''| \le 0.1$ nearby and the other $|f''| \le 10$. For which is the estimate $f(3.5) \approx 8$ more trustworthy, and by roughly what factor in the error bound?
14. Newton's method needs $f'$; the **secant method** replaces $f'(x_n)$ with the slope through the last two iterates. State one advantage and one disadvantage you would expect from that substitution.

### Python Practice

15. Extend the `newton` function to raise a clear error when $|f'(x_n)|$ falls below $10^{-14}$, and demonstrate the safeguard triggering on $f(x) = x^2 - 2$ from $x_0 = 0$.
16. Solve $e^{-x} = x$ to twelve digits, obtaining the derivative via SymPy's `lambdify` as in §6.4. Report the root and the number of iterations from $x_0 = 0.5$.

### Visualization Practice

17. Plot $f(x) = \ln x$ and its linearization at $a = 1$ on $(0.1, 3]$, shading (with `fill_between`) the vertical gap between them. Where does the estimate overshoot versus undershoot, and how does the sign of $f''$ explain it?
18. Reproduce the semilog convergence plot of §6.4 for the root of $x^3 - x - 2$ (Exercise 9), and add, for comparison, the error sequence of simple **bisection** on the same problem starting from your bracketing interval. Describe the visual difference between quadratic and linear convergence.

### Challenge

19. Prove the error-doubling heuristic for {prf:ref}`ex-newton-sqrt2`: writing $e_n = x_n - \sqrt2$, show algebraically that $e_{n+1} = \dfrac{e_n^2}{2x_n}$, and conclude that near the root $e_{n+1} \approx \dfrac{e_n^2}{2\sqrt2}$ — the error is squared at every step.
20. **Kepler's equation** $M = E - \varepsilon\sin E$ must be solved for $E$ given $M$ and eccentricity $\varepsilon$ in orbital mechanics. For $M = 1$ and $\varepsilon = 0.8$, solve for $E$ with Newton's method to ten digits, and plot iterate count as a function of $\varepsilon \in [0, 0.95]$ from the start $E_0 = M$. What happens as $\varepsilon \to 1$, and why (look at $f'$)?

### Cumulative Review

21. *(Ch. 4–5)* Find the linearization of $f(x) = \dfrac{e^x}{1+x}$ at $a = 0$ (quotient rule first), and use it to estimate $f(0.1)$.
22. *(Ch. 2)* Newton's method for $f(x) = \ln x - 1$ from $x_0 = 3$: compute one step by hand and identify the exact root it is approaching.

## 6.6 Summary

The linearization $L(x) = f(a) + f'(a)(x-a)$ replaces a curve by its tangent line, with error at most $\frac{M}{2}(x-a)^2$ for $M$ bounding $|f''|$ nearby: excellent close to $a$, quadratically worse with distance, and better for flatter functions. Written in increments, the same idea propagates uncertainty: $\Delta f \approx f'(a)\,\Delta x$. Newton's method solves $f(x)=0$ by repeatedly following tangent lines to the axis, $x_{n+1} = x_n - f(x_n)/f'(x_n)$, doubling correct digits each step near a simple root — with known failure modes (flat tangents, bad starts, repeated roots) that practical software guards against. Both techniques are the derivative *applied*, they are each a few lines of Python, and both are first glimpses of larger machinery: Taylor approximation and numerical optimization. Part I of the book — differential calculus — is now complete; Part II reverses the operation and asks what accumulates.

*Parallel reading:* OpenStax *Calculus Volume 1*, Sections 4.1–4.2 and 4.9 {cite}`openstax_calc1`; convergence theory in {cite}`burden_faires`.
