# Chapter 13 · Power Series and Taylor Series

When a calculator reports $\sin(1) = 0.8414709848$, what did it actually compute? Not a triangle, not a unit circle — a *polynomial*. This chapter builds the bridge from series of numbers to series of functions: **power series**, sums of the form $\sum c_k x^k$, and the **Taylor series** that represent familiar functions in that form. The linearization of Chapter 6 was the first rung — matching a function's value and slope with a line; matching ever more derivatives climbs to quadratic, cubic, and ultimately infinite-degree approximations, with Taylor's theorem quantifying the error at every rung. The result is both a computational engine (how machines evaluate $e^x$, $\sin$, $\ln$) and a theoretical lens (why those functions are what they are).

## 13.1 Power series and where they converge

```{prf:definition} Power series
:label: def-power-series
A **power series centered at $a$** is a series of the form

$$
\sum_{k=0}^{\infty} c_k\,(x - a)^k = c_0 + c_1(x-a) + c_2(x-a)^2 + \cdots,
$$

with coefficients $c_k$. For each fixed $x$ it is an ordinary series of numbers, which may converge or not — so a power series defines a function *on the set of $x$ where it converges*.
```

The prototype is the geometric series with $x$ as the ratio:

$$
\frac{1}{1 - x} = \sum_{k=0}^{\infty} x^k = 1 + x + x^2 + \cdots, \qquad |x| < 1,
$$

convergent precisely on the interval $(-1, 1)$ — and that shape of convergence set is universal:

```{prf:theorem} Radius of convergence
:label: thm-radius
Every power series $\sum c_k(x-a)^k$ has a **radius of convergence** $R \in [0, \infty]$: the series converges (absolutely) for $|x - a| < R$ and diverges for $|x - a| > R$. The ratio test computes it: $R$ is where $\lim\bigl|\frac{c_{k+1}(x-a)^{k+1}}{c_k(x-a)^k}\bigr| = |x-a|\lim\bigl|\frac{c_{k+1}}{c_k}\bigr|$ crosses $1$. Behavior *at* the endpoints $|x-a| = R$ must be checked separately, series by series.
```

```{figure} figures/ch13-geometric-radius.png
:name: fig-geometric-radius
:alt: The curve one over one minus x with partial sums of the geometric series overlaid for N equals 2, 5, 10, and 30. Inside the dashed vertical lines at minus one and plus one, higher partial sums converge to the curve; outside them the partial sums fly away from it.

Partial sums of $\sum x^k$ against $\frac{1}{1-x}$. Inside the radius (dashed lines at $\pm1$), adding terms locks onto the curve; outside, adding terms makes things *worse*. A power series is a perfect representation — but only within its radius, a boundary invisible in the formula and absolute in practice.
```

```{prf:example} Computing a radius
:label: ex-radius
Find where $\displaystyle\sum_{k=0}^{\infty}\frac{x^k}{k!}$ converges.

Ratio of consecutive terms: $\bigl|\frac{x^{k+1}/(k+1)!}{x^k/k!}\bigr| = \frac{|x|}{k+1} \to 0$ for every $x$: the limit is below $1$ *always*, so $R = \infty$ — convergence on the entire real line. Factorial denominators buy infinite radius, and the series in question is about to be revealed as $e^x$.
```

Within its radius, a power series behaves like the "infinite polynomial" it resembles: it may be **differentiated and integrated term by term**, and the resulting series have the *same radius*. This innocuous-sounding fact is a factory for new representations, as §13.3 will exploit.

## 13.2 Taylor series: which power series is a given function?

Suppose $f$ *has* a power series at $a$: $f(x) = \sum c_k(x-a)^k$. The coefficients are then forced. Set $x = a$: only the constant survives, $c_0 = f(a)$. Differentiate and set $x = a$: $c_1 = f'(a)$. Differentiate again: $2c_2 = f''(a)$. Each differentiation peels one coefficient, and after $k$ of them, $k!\,c_k = f^{(k)}(a)$:

```{prf:definition} Taylor series and Taylor polynomials
:label: def-taylor
The **Taylor series** of $f$ at $a$ (Maclaurin series when $a = 0$) is

$$
\sum_{k=0}^{\infty}\frac{f^{(k)}(a)}{k!}(x - a)^k,
$$

and its partial sum of degree $n$ is the **Taylor polynomial** $T_n(x)$ — the unique degree-$n$ polynomial matching $f$'s value and first $n$ derivatives at $a$. $T_1$ is exactly Chapter 6's linearization.
```

The five series to know by heart, all centered at $0$, each derivable in a few lines from the definition:

$$
\begin{aligned}
e^x &= \sum_{k=0}^{\infty}\frac{x^k}{k!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots && (R = \infty)\\[4pt]
\sin x &= \sum_{k=0}^{\infty}\frac{(-1)^k x^{2k+1}}{(2k+1)!} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots && (R = \infty)\\[4pt]
\cos x &= \sum_{k=0}^{\infty}\frac{(-1)^k x^{2k}}{(2k)!} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots && (R = \infty)\\[4pt]
\frac{1}{1-x} &= \sum_{k=0}^{\infty}x^k = 1 + x + x^2 + \cdots && (R = 1)\\[4pt]
\ln(1+x) &= \sum_{k=1}^{\infty}\frac{(-1)^{k+1}x^k}{k} = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots && (R = 1)
\end{aligned}
$$

For $e^x$, every derivative is $e^x$, every $f^{(k)}(0) = 1$, and the coefficients are $\frac1{k!}$ — {prf:ref}`ex-radius`'s series, explaining at last why $\sum\frac{2^k}{k!} = e^2$ in Chapter 12. For $\sin$, the derivatives cycle $\sin, \cos, -\sin, -\cos$ with values $0, 1, 0, -1$ at the origin: only odd powers survive, signs alternating — the series *is* the oddness and the oscillation of sine, written algebraically. Structure in the series mirrors structure in the function.

```{prf:example} Deriving a Taylor series from scratch
:label: ex-taylor-derive
Find the Maclaurin series of $f(x) = \ln(1+x)$.

Derivatives: $f' = (1+x)^{-1}$, $f'' = -(1+x)^{-2}$, $f''' = 2(1+x)^{-3}$, and generally $f^{(k)}(x) = (-1)^{k+1}(k-1)!\,(1+x)^{-k}$. At $0$: $f(0) = 0$ and $f^{(k)}(0) = (-1)^{k+1}(k-1)!$, so

$$
c_k = \frac{(-1)^{k+1}(k-1)!}{k!} = \frac{(-1)^{k+1}}{k},
\qquad
\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots
$$

with $R = 1$ by the ratio test. At the endpoint $x = 1$ it converges (alternating series) to $\ln 2$ — Chapter 12's alternating harmonic series, now unmasked; at $x = -1$ it is the (divergent) harmonic series: endpoints genuinely differ.
```

```{figure} figures/ch13-taylor-sin.png
:name: fig-taylor-sin
:alt: The sine curve over two full periods with Taylor polynomials of degree 1, 3, 5, 7 and 11 overlaid. The degree one line matches only near the origin; each higher degree hugs the sine curve over a wider interval before peeling away, with degree eleven tracking it across most of the plot.

Taylor polynomials of $\sin x$ at $0$. $T_1(x) = x$ is the small-angle approximation of Chapter 6; each added pair of terms extends the region of agreement outward. The polynomials eventually peel off and dive (polynomials must), but on any fixed interval, enough terms pin the curve exactly.
```

## 13.3 New series from old

Deriving coefficients from scratch, as in {prf:ref}`ex-taylor-derive`, is the slow way. Inside the radius of convergence, series may be added, multiplied, composed with polynomials, differentiated, and integrated term by term — so known series breed new ones:

**Substitution.** Replace $x$ by $-x^2$ in $e^x$:

$$
e^{-x^2} = 1 - x^2 + \frac{x^4}{2!} - \frac{x^6}{3!} + \cdots \qquad (R = \infty),
$$

the Gaussian's series, obtained in one line though the function has no elementary antiderivative.

**Term-by-term integration.** Integrate that series from $0$ to $x$:

$$
\int_0^x e^{-t^2}dt = x - \frac{x^3}{3} + \frac{x^5}{5\cdot 2!} - \frac{x^7}{7\cdot 3!} + \cdots,
$$

an explicit, rapidly convergent formula for the "impossible" integral of Chapters 8 and 11 — series succeed exactly where antiderivatives fail, which is much of why they matter.

**Differentiation.** Differentiating $\frac{1}{1-x} = \sum x^k$ gives $\frac{1}{(1-x)^2} = \sum_{k\ge1}k x^{k-1}$ (Chapter 12's Exercise 19, now fully licensed), and differentiating the $\sin$ series yields precisely the $\cos$ series — the identity $\sin' = \cos$ holding coefficient by coefficient.

```{prf:example} A limit, a derivative, and an integral, all by series
:label: ex-series-uses
**(a)** $\displaystyle\lim_{x\to0}\frac{\sin x - x}{x^3}$: substitute the series, $\sin x - x = -\frac{x^3}{6} + \frac{x^5}{120} - \cdots$, so the quotient is $-\frac16 + \frac{x^2}{120} - \cdots \to -\frac16$. No hospital rules, no guessing — series make small-$x$ behavior *legible*.

**(b)** $\displaystyle\int_0^{1}e^{-t^2}dt$ to six digits: sum the integrated series at $x=1$: $1 - \frac13 + \frac{1}{10} - \frac{1}{42} + \frac{1}{216} - \cdots = 0.746824$, matching Chapter 11's `quad` to all shown digits after seven terms — alternating, so the first omitted term bounds the error.
```

## 13.4 Taylor's theorem: the error, exactly

How far can $T_n$ be trusted? The answer generalizes Chapter 6's linearization bound rung by rung:

```{prf:theorem} Taylor's remainder theorem (Lagrange form)
:label: thm-taylor-remainder
If $f$ has $n+1$ continuous derivatives between $a$ and $x$, then

$$
f(x) = T_n(x) + R_n(x),
\qquad
R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}\,(x - a)^{n+1}
$$

for some $c$ between $a$ and $x$. Consequently $\bigl|R_n(x)\bigr| \le \dfrac{M}{(n+1)!}|x-a|^{n+1}$ with $M = \max\bigl|f^{(n+1)}\bigr|$ on the interval.
```

The remainder is *the next term, with its derivative evaluated at an unknown intermediate point* — easy to remember, easy to bound. The case $n = 1$ is Chapter 6's $\frac M2(x-a)^2$ verbatim. And the factorial in the denominator is the engine of practical convergence: for $\sin x$ (all derivatives bounded by $1$),

$$
\bigl|R_n(x)\bigr| \le \frac{|x|^{n+1}}{(n+1)!} \longrightarrow 0 \quad\text{for every } x,
$$

so the Taylor series doesn't just converge — it converges *to the function*, everywhere, with an explicit digit-count guarantee.

```{prf:example} Certified digits, by hand
:label: ex-remainder-bound
How accurate is $T_7$ for $\sin(1)$?

$$
\bigl|R_7(1)\bigr| \le \frac{1}{8!} = 2.48\times10^{-5}
$$

— but the $x^8$ coefficient of sine's series is zero, so $T_7 = T_8$ and the sharper bound is $\frac{1}{9!} = 2.76\times10^{-6}$. The actual error, computed in §13.5, is $2.73\times10^{-6}$: the bound is honest almost to the digit. Four terms of a series certify five decimal places — this economy, guaranteed in advance by {prf:ref}`thm-taylor-remainder`, is precisely how numerical libraries decide how many terms to hard-code.
```

## 13.5 Common mistakes

```{admonition} Common Mistakes
:class: warning
**Using a series outside its radius.** $\frac{1}{1-x} = \sum x^k$ at $x = 2$ "gives" $-1 = 1 + 2 + 4 + \cdots$: nonsense, because $R = 1$. Always name the radius before using a representation; {numref}`fig-geometric-radius` shows how completely things fail outside it.

**Forgetting the factorial.** The coefficient is $\frac{f^{(k)}(a)}{k!}$, not $f^{(k)}(a)$. The matching condition $T_n^{(k)}(a) = f^{(k)}(a)$ is what forces the $k!$.

**Degree versus number of terms.** For sine, $T_7$ has four nonzero terms; gaps from zero coefficients routinely cause off-by-one bookkeeping. Count powers, not terms.

**Assuming great global accuracy from a great local fit.** Every $T_n$ of $\sin$ eventually dives to $\pm\infty$ ({numref}`fig-taylor-sin`): accuracy degrades with $|x - a|^{n+1}$. Far from the center, either raise $n$ or *move the center*.

**Endpoint amnesia.** The ratio test decides $|x-a| < R$ strictly; at $|x-a| = R$ anything can happen ($\ln(1+x)$: converges at $1$, diverges at $-1$). Check endpoints when they matter.

**Termwise operations outside the radius.** Differentiation and integration term by term are theorems *inside* $(a-R, a+R)$, not identities everywhere.
```

## 13.6 Now do it in Python

SymPy manufactures Taylor series on demand; NumPy makes the convergence visible; and the remainder theorem's predictions can be checked against measured error.

```python
import sympy as sp

x = sp.symbols('x')

# --- The classic series, generated ---
print(sp.series(sp.exp(x), x, 0, 6))       # 1 + x + x²/2 + x³/6 + x⁴/24 + x⁵/120 + O(x⁶)
print(sp.series(sp.sin(x), x, 0, 8))       # x - x³/6 + x⁵/120 - x⁷/5040 + O(x⁸)
print(sp.series(sp.log(1 + x), x, 0, 6))   # x - x²/2 + x³/3 - x⁴/4 + x⁵/5 + O(x⁶)

# --- New from old: the Gaussian series by substitution ---
print(sp.series(sp.exp(-x**2), x, 0, 8))   # 1 - x² + x⁴/2 - x⁶/6 + O(x⁸)

# --- Example 13.5(a): the limit, by series and by SymPy directly ---
print(sp.limit((sp.sin(x) - x)/x**3, x, 0))    # -1/6

# --- Example 13.6: measured error vs the remainder bound ---
import numpy as np
from math import factorial
T7 = sum((-1)**k * 1.0**(2*k+1) / factorial(2*k+1) for k in range(4))
print(abs(T7 - np.sin(1)), 1/factorial(9))     # 2.73e-06 vs bound 2.76e-06
```

The last pair of numbers is the chapter in miniature: theory promised at most $2.76\times10^{-6}$, reality delivered $2.73\times10^{-6}$. Now watch convergence happen across a whole interval, and measure its speed at a point:

```python
import matplotlib.pyplot as plt

xs = np.linspace(-2*np.pi, 2*np.pi, 500)

def T_sin(xs, degree):
    return sum((-1)**k * xs**(2*k+1) / factorial(2*k+1)
               for k in range((degree + 1)//2))

for deg in [1, 3, 5, 7, 11]:
    plt.plot(xs, T_sin(xs, deg), lw=1, label=f"$T_{{{deg}}}$")
plt.plot(xs, np.sin(xs), "k", lw=2, label=r"$\sin x$")
plt.ylim(-2.5, 2.5); plt.legend(ncol=3); plt.show()

# error at x=2 as terms are added: factorial-fast decay
errs = [abs(T_sin(np.array([2.0]), d)[0] - np.sin(2)) for d in [1,3,5,7,9,11,13]]
plt.semilogy([1,3,5,7,9,11,13], errs, "o-")
plt.xlabel("degree $n$"); plt.ylabel("error at $x=2$"); plt.show()
```

**Interpretation.** The first plot reproduces {numref}`fig-taylor-sin`: each polynomial owns a widening neighborhood of the center before its inevitable polynomial dive. The semilog plot shows the error at a fixed point falling *super-exponentially* — the curve steepens, because $\frac{2^{n+1}}{(n+1)!}$ shrinks faster than any geometric sequence. Compare Chapter 12's $\sum 1/k^2$ needing $200{,}000$ terms for five digits: factorial denominators are why Taylor series, not generic series, are what machines evaluate. When you call `np.sin`, a routine built on exactly this mathematics (a polynomial fit on a reduced interval) returns in nanoseconds with all sixteen digits certified.

```{admonition} Data Science Connection
:class: tip
Second-order Taylor expansion is the daily bread of optimization: near a point, a loss function is modeled as $L(\vb w) \approx L + \nabla L\cdot\Delta + \frac12\Delta^{\!\top} H\,\Delta$ — value, gradient, curvature — and minimizing that quadratic *is* Newton's method, while trusting it only locally gives trust-region methods. The logistic sigmoid's expansion $\sigma(x)\approx\frac12 + \frac x4$ explains small-signal linearity of neurons; $\ln(1+x)\approx x - \frac{x^2}{2}$ underlies variance corrections for log-returns; and gradient boosting fits each new tree to a Taylor expansion of the loss (XGBoost uses exactly the second-order form). When Chapter 20 diagonalizes the Hessian $H$, the two halves of this course — calculus and linear algebra — meet inside this one formula.
```

```{admonition} Looking Ahead
:class: seealso
Taylor series approximate a function near *one point* by polynomials, with accuracy dying off with distance. Chapter 14 changes the basis: approximate a function across a *whole interval* by sines and cosines, with coefficients computed by integrals instead of derivatives — trading locality for global, periodic fidelity. The remainder machinery built here also retroactively proves Chapter 11's quadrature error bounds.
```

## 13.7 Exercises

### Quick Check

1. Write $T_2(x)$ for $f(x) = e^x$ at $a = 0$, and use it to estimate $e^{0.1}$.
2. What is the radius of convergence of $\sum \frac{x^k}{k!}$? Of $\sum k!\,x^k$?
3. From the $\cos$ series, read off $\lim_{x\to0}\frac{1 - \cos x}{x^2}$.
4. The Maclaurin series of an *odd* function contains which powers of $x$?

````{admonition} Answers to Quick Checks
:class: dropdown
1. $T_2(x) = 1 + x + \frac{x^2}{2}$; $e^{0.1} \approx 1.105$ (true: $1.10517$).
2. $R = \infty$; $R = 0$ (the ratio $|x|(k+1) \to \infty$ for any $x \neq 0$ — a series convergent only at its center).
3. $1 - \cos x = \frac{x^2}{2} - \frac{x^4}{24} + \cdots$, so the limit is $\frac12$.
4. Odd powers only — as with $\sin$; even functions get even powers, as with $\cos$.
````

### Basic Practice

5. Find the radius (and interval, checking endpoints) of convergence: (a) $\sum \frac{x^k}{k\,2^k}$; (b) $\sum \frac{(x-3)^k}{k^2}$; (c) $\sum \frac{k!\,x^k}{10^k}$.
6. Derive from scratch (derivative table, coefficients) the Maclaurin series of $f(x) = \frac{1}{1+x}$, and confirm it agrees with substituting $-x$ into the geometric series.
7. Using known series and substitution, write the first four nonzero terms of: (a) $e^{3x}$; (b) $\sin(x^2)$; (c) $x^2\cos x$; (d) $\frac{1}{1+x^2}$.
8. Write $T_3(x)$ for $f(x) = \sqrt{x}$ centered at $a = 4$, and use it to estimate $\sqrt{4.2}$, comparing with Chapter 6's linear estimate $2.05$ and the true $2.049390$.

````{admonition} Solution to Exercise 8
:class: dropdown
Derivatives at $4$: $f = 2$, $f' = \frac14$, $f'' = -\frac1{32}$, $f''' = \frac{3}{256}$. So

$$
T_3(x) = 2 + \frac{x-4}{4} - \frac{(x-4)^2}{64} + \frac{(x-4)^3}{512},
$$

and $T_3(4.2) = 2 + 0.05 - 0.000625 + 0.0000156 = 2.0493906$ — six correct digits, versus three from the tangent line. Each Taylor rung multiplies accuracy by roughly the small quantity $\frac{x-a}{\text{scale}}$.
````

### Intermediate Practice

9. Evaluate by series: (a) $\lim_{x\to0}\dfrac{e^x - 1 - x}{x^2}$; (b) $\lim_{x\to0}\dfrac{\ln(1+x) - \sin x}{x^2}$.
10. Integrate the series of $\frac{1}{1+x^2}$ (Exercise 7d) term by term to derive the series $\arctan x = x - \frac{x^3}{3} + \frac{x^5}{5} - \cdots$, and evaluate it at $x=1$ to obtain Leibniz's formula $\frac\pi4 = 1 - \frac13 + \frac15 - \cdots$. Then compute how many terms this series needs for six digits of $\pi$, and reflect on why nobody computes $\pi$ this way.
11. How many terms of the series for $\int_0^1 e^{-t^2}dt$ ({prf:ref}`ex-series-uses`b) guarantee an error below $10^{-10}$? (Alternating: bound by first omitted term.) Verify against `quad`.
12. Find the Taylor series of $e^x$ centered at $a = 1$ (hint: $e^x = e\cdot e^{x-1}$), and explain when re-centering beats adding terms.

### Conceptual Understanding

13. Explain why every Taylor polynomial of $\sin x$ must eventually leave the band $[-1, 1]$, no matter the degree — and reconcile that with the series converging to $\sin x$ at every point.
14. The remainder $\frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$ contains three factors. Describe what controls each — smoothness of $f$, the factorial, the distance — and which one a *user* can actually choose.
15. Both $T_n$ at a point and interpolation through $n+1$ points produce degree-$n$ polynomial approximations. Contrast where each spends its accuracy, and connect to why Simpson's rule (interpolation) and series evaluation (Taylor) coexist in numerical practice.

### Python Practice

16. Verify Exercises 5–10 with SymPy (`sp.series`, `sp.limit`, term-by-term integration via `sp.integrate` on the truncated polynomial).
17. Implement `my_exp(x, tol)` summing the $e^x$ series until the next term is below `tol`, with the range-reduction trick $e^x = (e^{x/2})^2$ applied until $|x|\le\frac12$ — then compare against `np.exp` on $x \in \{-10, -1, 0.3, 5, 20\}$ for accuracy and term counts, with and without reduction. You have now written the core of a `libm` exponential.

### Visualization Practice

18. Reproduce {numref}`fig-taylor-sin` for $\ln(1+x)$ on $(-1, 3]$ with $T_2, T_5, T_{10}, T_{25}$: the plot will show convergence for $|x|<1$ and *divergence* beyond $1$ regardless of degree — the radius made visible. Mark the boundary.
19. Heatmap the error $\log_{10}|T_n(x) - \sin x|$ over a grid of $x \in [-8, 8]$ and $n \in \{1, 3, \ldots, 21\}$; describe the shape of the "trusted region" and how it grows with $n$.

### Challenge

20. Prove the binomial series: for any real $\alpha$, $(1+x)^\alpha = \sum_{k=0}^\infty \binom{\alpha}{k}x^k$ for $|x|<1$, where $\binom{\alpha}{k} = \frac{\alpha(\alpha-1)\cdots(\alpha-k+1)}{k!}$ — deriving the coefficients from Taylor's formula. Specialize to $\alpha = -\frac12$ and connect to the series used by calculators for $\frac{1}{\sqrt{1+x}}$.
21. **Euler's formula by series.** Accepting the $e^x$ series for imaginary arguments, expand $e^{i\theta}$, separate real and imaginary parts, and recognize the $\cos$ and $\sin$ series: $e^{i\theta} = \cos\theta + i\sin\theta$. Deduce $e^{i\pi} + 1 = 0$, and note (for Chapter 14) that sines and cosines are exponentials in disguise.

### Cumulative Review

22. *(Ch. 6)* Show that Taylor's remainder with $n = 1$ is exactly Chapter 6's linearization error bound, and redo {prf:ref}`ex-lin-sqrt`'s error estimate as a corollary.
23. *(Ch. 11)* The quadrature error constants involved $f''$ and $f^{(4)}$. Expand $f$ in a Taylor polynomial about a panel's midpoint, integrate over the panel, and show the midpoint rule's error per panel is $\frac{f''(m)}{24}h^3 + O(h^5)$ — deriving, at last, where Chapter 11's $n^{-2}$ scaling comes from.

## 13.8 Summary

A power series $\sum c_k(x-a)^k$ converges on an interval of radius $R$ around its center (ratio test; endpoints case by case) and there behaves as an infinite polynomial: differentiable and integrable term by term. Matching derivatives forces the coefficients $c_k = \frac{f^{(k)}(a)}{k!}$, defining the Taylor series and its partial sums $T_n$ — the ladder whose first rung is linearization. The core catalog ($e^x$, $\sin$, $\cos$ everywhere; geometric and $\ln(1+x)$ on radius 1) plus substitution, differentiation, and integration generate the series met in practice, including for functions with no elementary antiderivative. Taylor's theorem prices the truncation: $R_n = \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$, whose factorial denominator delivers the super-fast convergence that makes series the working representation of functions in numerical software — and whose $(x-a)^{n+1}$ factor confines trust to a neighborhood of the center. Series compute limits by making small-$x$ behavior explicit, certify digits in advance, and (in second-order form) power Newton-type optimization. The next chapter swaps the polynomial basis for sines and cosines and approximates globally instead.

*Parallel reading:* OpenStax *Calculus Volume 2*, Sections 6.1–6.4 {cite}`openstax_calc2`.
