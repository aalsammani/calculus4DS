# Chapter 11 · Numerical Integration

The techniques of Chapters 8 and 10 are powerful and incomplete — provably so: integrands as innocent as $e^{-x^2}$, $\frac{\sin x}{x}$, and $\sqrt{1 + x^4}$ have no elementary antiderivatives at all, and integrands defined only by data (sensor readings, sampled signals) have no formulas to manipulate in the first place. Yet their *definite* integrals are perfectly meaningful numbers, and applications need them. This chapter builds the machinery that computes definite integrals directly from function values: the trapezoid rule, Simpson's rule, and the error analysis that tells you how much to trust each — the analysis being the real content, since an answer without an accuracy estimate is a guess.

## 11.1 The trapezoid rule

Chapter 7's Riemann sums approximate with flat-topped rectangles, wasteful because a constant is a poor stand-in for a varying function. The first upgrade: connect consecutive sample points with straight chords, replacing rectangles with trapezoids. On a grid $a = x_0 < x_1 < \cdots < x_n = b$ of uniform spacing $h = \frac{b-a}{n}$, the trapezoid over $[x_{k}, x_{k+1}]$ has area $h\,\frac{f(x_k) + f(x_{k+1})}{2}$, and summing telescopes the interior values:

```{prf:definition} Trapezoid rule
:label: def-trapezoid
$$
T_n \;=\; h\left[\frac{f(x_0)}{2} + f(x_1) + f(x_2) + \cdots + f(x_{n-1}) + \frac{f(x_n)}{2}\right],
\qquad h = \frac{b - a}{n}.
$$

Each interior point serves two trapezoids (right wall of one, left wall of the next) and so appears with weight $1$; the two endpoints serve one each, weight $\frac12$.
```

```{prf:example} The trapezoid rule by hand
:label: ex-trap-hand
Approximate $\displaystyle\int_0^{\pi}\sin x\,dx$ (exact value $2$, from Chapter 7) with $n = 4$.

Here $h = \frac\pi4$ and the samples are $\sin 0 = 0$, $\sin\frac\pi4 = \frac{\sqrt2}{2}$, $\sin\frac\pi2 = 1$, $\sin\frac{3\pi}{4} = \frac{\sqrt2}{2}$, $\sin\pi = 0$:

$$
T_4 = \frac{\pi}{4}\left[\frac{0}{2} + \frac{\sqrt2}{2} + 1 + \frac{\sqrt2}{2} + \frac{0}{2}\right]
= \frac{\pi}{4}\bigl(1 + \sqrt2\bigr) = 1.8961.
$$

Error: $2 - 1.8961 = 0.1039$. Doubling to $n = 8$ gives $T_8 = 1.9742$, error $0.0258$ — almost exactly **one quarter** of before. That $4\times$ improvement per doubling is no accident, and predicting it is the next section's business. Note also the error's *sign*: chords under a concave-down curve lie below it, so the trapezoid rule *underestimates* here — curvature tells you which side of the truth you are on.
```

## 11.2 Simpson's rule

If chords beat flat tops, curves should beat chords. **Simpson's rule** fits a parabola through each consecutive *triple* of points $(x_{2k}, x_{2k+1}, x_{2k+2})$ — which is why it requires $n$ **even** — and integrates the parabolas exactly. Working out the integral of the interpolating parabola over a double panel (Exercise 20) yields weights in the memorable pattern $1, 4, 2, 4, 2, \ldots, 4, 1$:

```{prf:definition} Simpson's rule
:label: def-simpson
For even $n$, with $h = \frac{b-a}{n}$:

$$
S_n = \frac{h}{3}\Bigl[f(x_0) + 4f(x_1) + 2f(x_2) + 4f(x_3) + \cdots + 2f(x_{n-2}) + 4f(x_{n-1}) + f(x_n)\Bigr].
$$
```

```{figure} figures/ch11-trap-vs-simpson.png
:name: fig-trap-vs-simpson
:alt: Two panels over one arch of the sine curve with four subintervals. Left panel: straight chords connecting the sample points visibly cut off the top of the arch. Right panel: parabolic arcs through consecutive point triples hug the curve almost perfectly.

The same four subintervals, two approximations. Trapezoid chords (left) visibly undercut the sine arch near its crest; Simpson's parabolic arcs (right) are indistinguishable from the curve at this resolution. The visual gap is the accuracy gap: errors $0.104$ versus $0.0046$ at $n = 4$.
```

```{prf:example} Simpson's rule by hand
:label: ex-simpson-hand
Repeat {prf:ref}`ex-trap-hand` with Simpson's rule, $n = 4$.

Same five samples, new weights $1, 4, 2, 4, 1$:

$$
S_4 = \frac{\pi/4}{3}\left[0 + 4\cdot\frac{\sqrt2}{2} + 2\cdot 1 + 4\cdot\frac{\sqrt2}{2} + 0\right]
= \frac{\pi}{12}\bigl(2 + 4\sqrt2\bigr) = 2.00456.
$$

Error $0.00456$ — from the *same five function evaluations* that gave the trapezoid rule an error twenty-three times larger. Better use of the same information, free of charge: that is the recurring theme of numerical analysis.
```

## 11.3 Error analysis: how much can you trust the answer?

The error formulas, derived from the Taylor machinery of Chapter 13 and proved in {cite}`burden_faires`, are:

$$
\bigl|E_T\bigr| \le \frac{(b-a)^3}{12\,n^2}\max_{[a,b]}\bigl|f''\bigr|,
\qquad
\bigl|E_S\bigr| \le \frac{(b-a)^5}{180\,n^4}\max_{[a,b]}\bigl|f^{(4)}\bigr|.
$$

Every factor carries meaning. The derivative factors say each rule is *exact* on the functions whose relevant derivative vanishes: trapezoids on straight lines ($f'' = 0$), Simpson on cubics ($f^{(4)} = 0$ — one degree better than the parabola fit suggests, a happy accident of symmetry). Rough functions, with large higher derivatives, are hard for everyone. Most important are the powers of $n$:

$$
E_T \sim \frac{C}{n^2} \qquad\text{versus}\qquad E_S \sim \frac{C'}{n^4}.
$$

Doubling the sample count divides the trapezoid error by $4$ but Simpson's by $16$. On a log-log plot, error versus $n$ is a straight line of slope $-2$ or $-4$, and *checking that slope is how practitioners verify an implementation*:

```{figure} figures/ch11-error-scaling.png
:name: fig-error-scaling
:alt: A log-log plot of absolute error against number of subintervals from 4 to 256 for both rules applied to the integral of sine from zero to pi. The trapezoid errors fall along a straight reference line of slope minus two; the Simpson errors along a much steeper line of slope minus four, reaching two and a half times ten to the minus ten by n equals 256.

Measured errors for $\int_0^\pi \sin x\,dx = 2$. Both rules trace straight lines on log-log axes — trapezoid along the slope $-2$ guide, Simpson along slope $-4$. At $n = 256$: trapezoid error $2.5\times10^{-5}$; Simpson error $2.5\times10^{-10}$, five orders of magnitude better from identical samples.
```

The measured table behind the figure (generated by the script in §11.5, and reproducible by you):

| $n$ | trapezoid error | Simpson error |
|---|---|---|
| 4 | $1.04\times10^{-1}$ | $4.56\times10^{-3}$ |
| 16 | $6.43\times10^{-3}$ | $1.66\times10^{-5}$ |
| 64 | $4.02\times10^{-4}$ | $6.45\times10^{-8}$ |
| 256 | $2.51\times10^{-5}$ | $2.52\times10^{-10}$ |

Each 4-fold increase in $n$ divides the trapezoid column by $\approx16 = 4^2$ and the Simpson column by $\approx256 = 4^4$, exactly as the exponents promise.

```{prf:example} Using the bound before computing
:label: ex-error-bound
How many subintervals guarantee the trapezoid rule computes $\int_0^\pi \sin x\,dx$ with error below $10^{-6}$?

With $|f''| = |\!-\!\sin x| \le 1$ and $b - a = \pi$:

$$
\frac{\pi^3}{12n^2} \le 10^{-6}
\quad\Longleftrightarrow\quad
n \ge \sqrt{\frac{\pi^3}{12\cdot10^{-6}}} = 1607.6,
$$

so $n = 1608$ suffices — guaranteed, before evaluating anything. The same target with Simpson's rule ($|f^{(4)}| \le 1$): $n^4 \ge \frac{\pi^5}{180\cdot 10^{-6}}$, giving $n \ge 36.4$, so $n = 38$ (even). Sixteen hundred samples versus thirty-eight: the exponent on $n$, not the constant, is what separates methods.
```

**Beyond fixed rules.** Production integrators such as SciPy's `quad` are *adaptive*: they estimate the error on each subinterval (by comparing two rules of different order), subdivide only where the estimate is large — near spikes, kinks, or rapid oscillation — and stop when a requested tolerance is met, returning the error estimate alongside the answer. The principles are exactly this chapter's; the engineering is the placement of effort where the integrand is difficult.

## 11.4 Common mistakes

```{admonition} Common Mistakes
:class: warning
**Odd $n$ with Simpson's rule.** The $1,4,2,\dots,4,1$ pattern needs point-triples; odd $n$ breaks it and quietly corrupts the answer. Check parity first.

**Miscounting the weights.** Endpoints get $\frac12$ (trapezoid) or $1$ (Simpson); Simpson's interior weights *alternate* $4, 2, 4, \dots$ starting and ending with $4$. A weight audit — trapezoid weights sum to $n$, Simpson's to $3n$ — catches most slips.

**Confusing $n$ with the number of points.** $n$ subintervals means $n + 1$ samples. Off-by-one here shifts every node.

**Trusting a single $n$.** One computation gives a number; two computations (say $n$ and $2n$) give a number *and* an error estimate — if they agree to six digits, roughly six digits are right. Never report an integral from a single resolution.

**Applying the rules across a singularity or discontinuity.** Like FTC, the error bounds assume smoothness; an integrand blowing up inside $[a,b]$ (recall $\int_{-1}^1 x^{-2}dx$ from Chapter 7) invalidates everything. Inspect, split at known bad points, or use library routines designed for them.

**Forgetting that data can be non-uniform.** The formulas above assume equal spacing; for measured data at irregular times use the general trapezoid form $\sum \frac{f(x_k)+f(x_{k+1})}{2}(x_{k+1}-x_k)$ — which is what `np.trapezoid` does with an `x` argument.
```

## 11.5 Now do it in Python

Implement both rules yourself once — vectorized, no loops — then meet the library versions.

```python
import numpy as np

def trapezoid(f, a, b, n):
    x = np.linspace(a, b, n + 1)
    y = f(x)
    h = (b - a) / n
    return h * (y[0]/2 + y[1:-1].sum() + y[-1]/2)

def simpson(f, a, b, n):
    if n % 2:
        raise ValueError("Simpson's rule needs even n")
    x = np.linspace(a, b, n + 1)
    y = f(x)
    h = (b - a) / n
    return (h/3) * (y[0] + 4*y[1:-1:2].sum() + 2*y[2:-2:2].sum() + y[-1])

# --- Reproduce the hand computations and the error table ---
print(trapezoid(np.sin, 0, np.pi, 4))    # 1.8961188...  (Ex 11.2)
print(simpson(np.sin, 0, np.pi, 4))      # 2.0045597...  (Ex 11.4)
for n in [4, 16, 64, 256]:
    eT = abs(trapezoid(np.sin, 0, np.pi, n) - 2)
    eS = abs(simpson(np.sin, 0, np.pi, n) - 2)
    print(f"n={n:4d}   trap {eT:.2e}   simpson {eS:.2e}")
```

The slicing `y[1:-1:2]` grabs the odd-indexed (weight-4) samples and `y[2:-2:2]` the even interior (weight-2) ones — the weight pattern *as code*. Now the integrals that motivated the chapter, via the standard library tools:

```python
from scipy.integrate import quad

# No elementary antiderivative exists — numerics is the only route
val, err = quad(lambda t: np.exp(-t**2), 0, 1)
print(val, err)          # 0.7468241328124271, ~8.3e-15

# The Gaussian integral: quad handles infinite limits too
val, err = quad(lambda t: np.exp(-t**2), -np.inf, np.inf)
print(val, np.sqrt(np.pi))   # 1.7724538509... both — the famous √π

# Data, not formulas: integrate sampled measurements
t_data = np.array([0.0, 0.5, 1.1, 1.4, 2.0, 2.8, 3.0])   # irregular times
v_data = np.array([0.0, 4.2, 8.9, 10.1, 11.8, 12.6, 12.7])  # speeds
print(np.trapezoid(v_data, t_data))     # distance traveled ≈ 26.6
```

**Interpretation.** Three situations, three tools. For a smooth integrand with no antiderivative, `quad` returns fourteen correct digits and *says so* via its error estimate — read that second output every time. For $\int_{-\infty}^{\infty}e^{-x^2}dx$ it reproduces $\sqrt\pi$, a constant you will meet again as the normal distribution's normalizer. For raw data there is no function to adaptively sample — the trapezoid rule on the measured points is the honest answer, and its $n^{-2}$ character means better data beats better algorithms. Finally, reproduce {numref}`fig-error-scaling` with `plt.loglog` and your own `trapezoid`/`simpson`: seeing your implementation's errors fall on the slope $-2$ and $-4$ lines is the standard correctness test of the field, and a satisfying one.

```{admonition} Data Science Connection
:class: tip
Numerical integration is running silently all through the statistics stack: every p-value and every normal-table lookup is $\int$ of a density evaluated by machinery like this chapter's (the error function $\operatorname{erf}$ is *defined* as $\frac{2}{\sqrt\pi}\int_0^x e^{-t^2}dt$); the AUC metric integrates an ROC curve known only at finitely many thresholds — trapezoid rule on data, exactly as above; and Bayesian model evidence is an integral that in high dimensions defeats grids entirely, which is why Monte Carlo methods (first glimpsed in Chapter 9) take over there. Knowing *when* quadrature is trustworthy — smoothness, dimension, singularities — is the practitioner's version of this chapter's error analysis.
```

```{admonition} Looking Ahead
:class: seealso
Both error bounds lean on high-order derivatives controlling how far a function strays from its polynomial stand-ins — precisely the question Taylor's theorem answers in Chapter 13, where these bounds are finally provable. The oscillatory integrals that stress quadrature ($\int \sin(50x)e^{-x}dx$, Exercise 17) reappear constructively in Chapter 14, where oscillations become the *basis* for representing functions.
```

## 11.6 Exercises

### Quick Check

1. Write out the trapezoid rule for $\int_0^2 f\,dx$ with $n = 4$: nodes and weights.
2. Why does Simpson's rule require even $n$?
3. Trapezoid error at $n=10$ is $0.008$. Estimate it at $n = 20$ and at $n = 40$.
4. Which is exact for $f(x) = x^3$ on any interval: trapezoid, Simpson, both, or neither?

````{admonition} Answers to Quick Checks
:class: dropdown
1. $h = \frac12$; $T_4 = \frac12\bigl[\frac{f(0)}{2} + f(\tfrac12) + f(1) + f(\tfrac32) + \frac{f(2)}{2}\bigr]$.
2. Each parabola is fit through three consecutive points, consuming subintervals in pairs.
3. $\approx 0.002$, then $\approx 0.0005$: each doubling divides by $4$.
4. Simpson only: $f^{(4)} = 0$ for cubics, so $E_S = 0$; but $f'' = 6x \neq 0$, so trapezoids err.
````

### Basic Practice

5. By hand, approximate $\int_0^1 x^2\,dx$ with $T_4$ and $S_4$; compare both with the exact $\frac13$ and explain Simpson's result.
6. By hand (calculator arithmetic allowed), approximate $\int_1^2 \frac{1}{x}\,dx$ with $T_4$, and compare with the exact value $\ln 2 = 0.6931$. Does the rule over- or under-estimate, and how does the sign of $f''$ predict that?
7. A river's depth (m) is measured every $2$ m across its $12$ m width: $0, 1.8, 3.1, 3.9, 3.4, 2.1, 0$. Estimate the cross-sectional area by the trapezoid rule, and by Simpson's rule.
8. Use the trapezoid error bound to find $n$ guaranteeing error below $10^{-4}$ for $\int_0^1 e^{x}\,dx$, then verify with your implementation that the guarantee holds (with room to spare — bounds are pessimistic).

````{admonition} Solution to Exercise 5
:class: dropdown
$h = \frac14$, samples $0, \frac{1}{16}, \frac14, \frac{9}{16}, 1$.

$T_4 = \frac14\bigl[0 + \frac1{16} + \frac14 + \frac9{16} + \frac12\bigr] = \frac{11}{32} = 0.34375$ (error $\frac{1}{96} \approx 0.0104$).

$S_4 = \frac{1}{12}\bigl[0 + \frac4{16} + \frac24 + \frac{36}{16} + 1\bigr] = \frac{1}{12}\cdot 4 = \frac13$ — **exact**, as it must be: the integrand is a parabola, and Simpson integrates parabolas without error.
````

### Intermediate Practice

9. For $\int_0^1 e^{-x^2}dx$: compute $T_n$ and $S_n$ for $n = 8, 16, 32$, and use the agreement pattern between successive values to state how many digits of $0.746824$ each method has secured at $n=32$.
10. The error function is $\operatorname{erf}(x) = \frac{2}{\sqrt\pi}\int_0^x e^{-t^2}dt$. Tabulate it at $x = 0.5, 1.0, 1.5, 2.0$ with Simpson's rule ($n = 64$), check against `scipy.special.erf`, and explain the connection to normal-distribution probabilities.
11. Verify the claim of {numref}`fig-error-scaling` quantitatively: from your error table for $\int_0^\pi\sin$, compute the empirical order $p = \log_2\bigl(E(n)/E(2n)\bigr)$ for each doubling and each rule, and confirm $p \to 2$ and $p \to 4$.
12. Apply both rules with $n = 8$ to $\int_0^1\sqrt{x}\,dx = \frac23$. The observed errors are far worse than the sine benchmark at the same $n$ — diagnose why using the error formulas' derivative factors ($f''(x) = -\frac14x^{-3/2}$ near $0$).

### Conceptual Understanding

13. The trapezoid rule is the average of the left- and right-endpoint Riemann sums. Prove this in one line from the formulas, and explain geometrically why averaging cancels most of their (opposite-signed) errors.
14. Explain why Simpson's rule being exact for cubics — not just the parabolas it fits — follows from symmetry: consider $\int_{-h}^{h}x^3\,dx$ and what the rule computes for it.
15. Adaptive integrators concentrate points where the integrand is "difficult." Using the error bounds, state precisely what local property of $f$ makes a region difficult, and give two examples of integrands with a difficult region inside $[0,1]$.

### Python Practice

16. Implement `simpson_error_order(f, a, b, exact)` returning the empirical convergence order of Exercise 11 for any integrand, and run it on $\int_0^1 e^x dx$ and on Exercise 12's $\sqrt x$ — reporting the degraded order the singularity causes.
17. Integrate $\int_0^{2\pi}\sin(50x)e^{-x}\,dx$ with `quad` using default settings; note any warning, then fix the computation (increase `limit`, or split the interval) and report the value. What property of the integrand caused the trouble?

### Visualization Practice

18. Reproduce {numref}`fig-trap-vs-simpson` for $f(x) = e^{-x^2}$ on $[0, 2]$ with $n = 4$, shading the region between each approximant and the true curve, and report the two errors in the panel titles.
19. Make the log-log error plot for $\int_0^1\sqrt x\,dx$ (both rules, $n = 4$ to $1024$) with slope guides at $-2$, $-4$, and $-1.5$. Which guide do the data actually follow, and what does that say about how singularities, not methods, can set the convergence rate?

### Challenge

20. Derive Simpson's basic weights: fit a parabola $p(x)$ through $(-h, f_{-1})$, $(0, f_0)$, $(h, f_1)$ and integrate it over $[-h, h]$ to obtain $\frac h3(f_{-1} + 4f_0 + f_1)$.
21. **Romberg extrapolation.** Given the trapezoid error's form $E \approx C n^{-2}$, show the combination $\frac{4T_{2n} - T_n}{3}$ cancels the leading error term — and verify numerically that this combination applied to your $\int_0^\pi\sin$ trapezoid values reproduces Simpson's values exactly. (Repeating the trick generates the Romberg method.)

### Cumulative Review

22. *(Ch. 10)* The integral $\int_0^1 x e^x\,dx$ is computable both exactly (parts: value $1$) and numerically. Find the smallest even $n$ for which Simpson's rule matches the exact answer to $10^{-8}$.
23. *(Ch. 6, 7)* FTC Part 1 plus quadrature lets you *plot* an antiderivative no table contains: graph $F(x) = \int_0^x e^{-t^2}dt$ on $[0,3]$ by cumulative Simpson sums, and mark the value it approaches (relate it to $\frac{\sqrt\pi}{2}$ from §11.5).

## 11.7 Summary

When antiderivatives are unavailable — impossible ($e^{-x^2}$), or absent because the integrand is data — definite integrals are computed from samples. The trapezoid rule joins samples by chords, $T_n = h\bigl[\frac{f_0}2 + f_1 + \cdots + \frac{f_n}2\bigr]$, with error $\sim n^{-2}$ scaled by $\max|f''|$; Simpson's rule fits parabolas through point-triples (even $n$, weights $1,4,2,\ldots,4,1$), with error $\sim n^{-4}$ scaled by $\max|f^{(4)}|$ and exactness through cubics. The exponents are the story: on log-log axes errors are lines of slope $-2$ and $-4$, doubling $n$ buys $4\times$ or $16\times$, and matching the measured slope validates an implementation. Error bounds turn accuracy targets into sample counts *in advance*; comparing two resolutions supplies an error estimate *after*; and singularities inside the interval degrade every rule's advertised rate. Adaptive library integrators (`scipy.integrate.quad`) automate the subdivision and report their own error — an output to be read, not ignored. This closes Part II's account of single integrals: exact methods where they reach, guaranteed numerics everywhere else.

*Parallel reading:* OpenStax *Calculus Volume 2*, Section 3.6 {cite}`openstax_calc2`; the error theory in {cite}`burden_faires`.
