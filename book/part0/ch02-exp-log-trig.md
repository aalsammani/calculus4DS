# Chapter 2 · Exponentials, Logarithms, and Trigonometry

Three families of functions appear so often in calculus and data science that they deserve a chapter of their own before the calculus begins: exponential functions, their inverses the logarithms, and the trigonometric functions. Each will be differentiated in Chapter 5 and integrated in Part II; here we make sure their algebra and their graphs are second nature.

## 2.1 Exponential functions

Linear growth adds a fixed *amount* per step; exponential growth multiplies by a fixed *factor* per step. A quantity that doubles daily, a population growing 3% per year, an investment compounding, an epidemic in its early phase, the loss decay of a training run — all are exponential.

```{prf:definition} Exponential function
:label: def-exponential
For a base $b > 0$ with $b \neq 1$, the **exponential function with base $b$** is

$$f(x) = b^x, \qquad x \in \mathbb{R},$$

with domain all of $\mathbb{R}$ and range $(0, \infty)$. It is increasing when $b > 1$ and decreasing when $0 < b < 1$.
```

The laws of exponents govern all algebra with these functions. For $b > 0$ and all real $x, y$:

$$
b^x b^y = b^{x+y}, \qquad \frac{b^x}{b^y} = b^{x-y}, \qquad (b^x)^y = b^{xy}, \qquad b^0 = 1, \qquad b^{-x} = \frac{1}{b^x}.
$$

Among all bases, one is special. The number

$$
e = 2.718281828\ldots
$$

is the base for which the exponential curve's slope at any point equals its height at that point — a fact we will *prove* in Chapter 5 and which makes $e^x$ the native exponential of calculus. For now, treat $e$ as a particular constant between $2$ and $3$; any exponential can be rewritten in base $e$, since $b^x = e^{x \ln b}$.

```{figure} figures/ch02-exp-log.png
:name: fig-exp-log
:alt: Left panel shows the increasing curves of 2 to the x, e to the x, and 5 to the x, all passing through the point zero comma one. Right panel shows natural log, log base 2, and log base 10, all passing through one comma zero and rising slowly.

Left: exponentials $b^x$ for $b = 2, e, 5$. All pass through $(0,1)$ since $b^0 = 1$; larger bases climb faster. Right: logarithms, their inverses, all pass through $(1, 0)$ and grow without bound but ever more slowly.
```

Exponential growth is *qualitatively* faster than polynomial growth: for any base $b>1$ and any power $n$, the ratio $b^x / x^n$ eventually grows without bound. The figure below makes the point concretely for $2^x$ versus $x^3$; the curves cross for the last time near $x \approx 9.94$, and beyond that the exponential wins by an ever-widening margin.

```{figure} figures/ch02-exp-vs-poly.png
:name: fig-exp-vs-poly
:alt: The cubic x cubed initially lies above 2 to the x, but the exponential curve overtakes it near x equals ten and then rises far more steeply.

$x^3$ versus $2^x$. The polynomial leads at first, but past their final crossing near $x \approx 9.94$ the exponential dominates permanently. This "eventually exponentials win" behavior is why algorithmic running times of $2^n$ are catastrophic while $n^3$ is merely slow.
```

## 2.2 Logarithms

The logarithm answers the question the exponential poses in reverse. The exponential asks: *given the exponent, what is the value?* The logarithm asks: *given the value, what was the exponent?*

```{prf:definition} Logarithm
:label: def-logarithm
For $b > 0$, $b \neq 1$, the **logarithm base $b$** is the inverse of $b^x$:

$$\log_b x = y \quad\Longleftrightarrow\quad b^y = x.$$

Its domain is $(0, \infty)$ and its range is all of $\mathbb{R}$. The **natural logarithm** is $\ln x = \log_e x$.
```

Every statement about logarithms is a statement about exponents read backwards. $\log_2 8 = 3$ *because* $2^3 = 8$; $\ln 1 = 0$ *because* $e^0 = 1$; $\log_{10} 0.01 = -2$ *because* $10^{-2} = 0.01$. The inverse relationship in function form:

$$
\ln(e^x) = x \ \text{ for all } x, \qquad e^{\ln x} = x \ \text{ for all } x > 0.
$$

The exponent laws translate into the **logarithm laws**. For $x, y > 0$ and any real $r$:

$$
\ln(xy) = \ln x + \ln y, \qquad
\ln\!\frac{x}{y} = \ln x - \ln y, \qquad
\ln(x^r) = r \ln x,
$$

and any base converts to any other by the **change of base formula** $\log_b x = \dfrac{\ln x}{\ln b}$.

Logarithms turn multiplication into addition and powers into multiplication — historically the reason they were invented, and currently the reason they pervade data science: they compress huge dynamic ranges (log-scale plots), stabilize products of many small probabilities (log-likelihoods), and linearize power laws.

```{prf:example} Solving exponential equations
:label: ex-solve-exponential
Solve $5 \cdot 3^{2t} = 40$ for $t$.

Isolate the exponential, then take a logarithm of both sides:

$$
3^{2t} = 8 \;\Longrightarrow\; \ln\bigl(3^{2t}\bigr) = \ln 8 \;\Longrightarrow\; 2t \ln 3 = \ln 8 \;\Longrightarrow\; t = \frac{\ln 8}{2 \ln 3}.
$$

Numerically $t = \frac{2.0794}{2(1.0986)} \approx 0.9464$. Check: $3^{2(0.9464)} = 3^{1.8928} \approx 8.0$. ✓
```

```{prf:example} Doubling time
:label: ex-doubling
A dataset grows by 15% per month, so its size after $t$ months is $S(t) = S_0 (1.15)^t$. How long until it doubles?

We need $(1.15)^t = 2$:

$$
t \ln 1.15 = \ln 2 \;\Longrightarrow\; t = \frac{\ln 2}{\ln 1.15} = \frac{0.6931}{0.1398} \approx 4.96 \text{ months}.
$$

**Interpretation.** About five months per doubling — so in a year (about 2.4 doublings) storage needs grow by a factor of $(1.15)^{12} \approx 5.35$. Percent-per-period growth compounds much faster than intuition suggests, which is exactly why one computes rather than guesses.
```

```{prf:example} Extracting a power law from logs
:label: ex-power-law
Measurements suggest a relationship $y = C x^p$. Taking logarithms of both sides,

$$
\ln y = \ln C + p \ln x,
$$

which is a *linear* equation in the variables $(\ln x, \ln y)$ with slope $p$ and intercept $\ln C$. If two measured points are $(x, y) = (2, 12)$ and $(8, 96)$, then

$$
p = \frac{\ln 96 - \ln 12}{\ln 8 - \ln 2} = \frac{\ln(96/12)}{\ln(8/2)} = \frac{\ln 8}{\ln 4} = \frac{3\ln 2}{2 \ln 2} = \frac{3}{2},
$$

and $C = y/x^p = 12/2^{3/2} = 12/(2\sqrt 2) = 3\sqrt{2} \approx 4.243$. This log-log linearization is a standard first move in exploratory data analysis.
```

## 2.3 Trigonometric functions

Calculus measures angles in **radians**: the radian measure of an angle is the length of the arc it cuts from a circle of radius 1. A full revolution is the full circumference, $2\pi$; a straight angle is $\pi$; a right angle is $\pi/2$. Degrees convert by $180° = \pi$ radians. Radians are not a stylistic preference — the clean derivative formulas of Chapter 5 ($\sin' = \cos$) are *only true in radians*.

```{prf:definition} Sine and cosine
:label: def-sin-cos
Place an angle $\theta$ at the origin, measured counterclockwise from the positive $x$-axis, and let it intersect the unit circle at a point $P$. Then

$$\cos\theta = \text{the $x$-coordinate of } P, \qquad \sin\theta = \text{the $y$-coordinate of } P.$$

Both functions are defined for all real $\theta$, take values in $[-1, 1]$, and are **periodic with period $2\pi$**: $\sin(\theta + 2\pi) = \sin\theta$ and likewise for cosine.
```

```{figure} figures/ch02-unit-circle.png
:name: fig-unit-circle
:alt: Left: a unit circle with an angle theta marked, the horizontal leg labeled cosine theta and vertical leg labeled sine theta, meeting the circle at a highlighted point. Right: the sine and cosine waves over two full periods, visibly identical curves offset by a quarter period.

Left: the unit-circle definition — $\cos\theta$ and $\sin\theta$ are coordinates of a point on the circle. Right: as $\theta$ advances, those coordinates trace the familiar waves. Cosine is sine shifted left by $\pi/2$, which the graphs make visible.
```

Because the point $(\cos\theta, \sin\theta)$ lies on the unit circle $x^2 + y^2 = 1$, we get for free the single most important identity in trigonometry:

$$
\sin^2\theta + \cos^2\theta = 1.
$$

The remaining four trigonometric functions are ratios of these two:

$$
\tan\theta = \frac{\sin\theta}{\cos\theta}, \qquad
\cot\theta = \frac{\cos\theta}{\sin\theta}, \qquad
\sec\theta = \frac{1}{\cos\theta}, \qquad
\csc\theta = \frac{1}{\sin\theta},
$$

each undefined where its denominator vanishes ($\tan$ and $\sec$ at odd multiples of $\pi/2$, for example). Dividing the Pythagorean identity by $\cos^2\theta$ gives its second form, needed for trigonometric substitution in Chapter 10:

$$
\tan^2\theta + 1 = \sec^2\theta.
$$

The values you should be able to produce without a calculator:

| $\theta$ | $0$ | $\pi/6$ | $\pi/4$ | $\pi/3$ | $\pi/2$ | $\pi$ |
|---|---|---|---|---|---|---|
| $\sin\theta$ | $0$ | $1/2$ | $\sqrt{2}/2$ | $\sqrt{3}/2$ | $1$ | $0$ |
| $\cos\theta$ | $1$ | $\sqrt{3}/2$ | $\sqrt{2}/2$ | $1/2$ | $0$ | $-1$ |
| $\tan\theta$ | $0$ | $1/\sqrt{3}$ | $1$ | $\sqrt{3}$ | undef. | $0$ |

Two identity families will be used later and are worth recording now. The **angle-sum identities**

$$
\sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta, \qquad
\cos(\alpha + \beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta,
$$

and, setting $\alpha = \beta = \theta$, the **double-angle identities**

$$
\sin 2\theta = 2\sin\theta\cos\theta, \qquad
\cos 2\theta = \cos^2\theta - \sin^2\theta = 1 - 2\sin^2\theta = 2\cos^2\theta - 1.
$$

Rearranged, the last two give the **half-angle (power-reduction) forms** $\sin^2\theta = \tfrac{1 - \cos 2\theta}{2}$ and $\cos^2\theta = \tfrac{1 + \cos 2\theta}{2}$, indispensable when we integrate squared trig functions in Chapter 10.

```{prf:example} Exact evaluation without a calculator
:label: ex-trig-exact
Compute $\sin\!\frac{5\pi}{6}$ and $\cos\!\frac{5\pi}{6}$.

The angle $5\pi/6$ lies in the second quadrant, $\pi/6$ short of $\pi$. Its **reference angle** is $\pi/6$. In the second quadrant, sine is positive ($y > 0$) and cosine negative ($x < 0$), so

$$
\sin\frac{5\pi}{6} = +\sin\frac{\pi}{6} = \frac{1}{2}, \qquad
\cos\frac{5\pi}{6} = -\cos\frac{\pi}{6} = -\frac{\sqrt{3}}{2}.
$$

Check with the Pythagorean identity: $\left(\tfrac12\right)^2 + \left(\tfrac{\sqrt3}{2}\right)^2 = \tfrac14 + \tfrac34 = 1.$ ✓
```

Finally, the restricted-domain inverses. $\arcsin x$ (also written $\sin^{-1}x$) is the angle in $[-\pi/2, \pi/2]$ whose sine is $x$; $\arccos x$ the angle in $[0, \pi]$ whose cosine is $x$; $\arctan x$ the angle in $(-\pi/2, \pi/2)$ whose tangent is $x$. Thus $\arcsin\frac12 = \pi/6$, and $\arctan 1 = \pi/4$. These reappear as antiderivatives in Part II.

## 2.4 Now do it in Python

The code verifies our hand results from this chapter — the doubling time, the exact trig values, and an identity — and demonstrates the log-scale plotting that makes exponential data legible.

```python
import numpy as np

# --- Verify Example 2.2: doubling time at 15% growth ---
t_double = np.log(2) / np.log(1.15)
print(t_double)                 # expect about 4.96
print(1.15**t_double)           # expect 2.0 (definition of doubling time)

# --- Verify Example 2.4: exact values at 5*pi/6 ---
theta = 5*np.pi/6
print(np.sin(theta), 1/2)                  # both 0.5
print(np.cos(theta), -np.sqrt(3)/2)        # both -0.8660...

# --- Spot-check an identity at random angles ---
rng = np.random.default_rng(0)
th = rng.uniform(-10, 10, size=5)
print(np.sin(th)**2 + np.cos(th)**2)       # expect five 1.0's
```

SymPy works with these functions *exactly*, returning symbolic values rather than decimals — often the more useful check:

```python
import sympy as sp

print(sp.sin(sp.Rational(5, 6) * sp.pi))    # expect 1/2, exactly
print(sp.solve(sp.Eq(5 * 3**(2*sp.Symbol('t')) - 40, 0)))  # ln(8)/(2 ln 3) form
print(sp.simplify(sp.cos(2*sp.Symbol('x'))
                  - (1 - 2*sp.sin(sp.Symbol('x'))**2)))    # expect 0
```

**Visualization: the power of log scales.** Exponential data plotted on ordinary axes hides everything but its final surge; on a logarithmic vertical axis, exponentials become straight lines whose slopes reveal their growth rates.

```python
import matplotlib.pyplot as plt

x = np.linspace(0, 30, 200)
fig, axes = plt.subplots(1, 2, figsize=(9, 3.6))
for b in (1.1, 1.3, 1.6):
    axes[0].plot(x, b**x, label=f"${b}^x$")
    axes[1].semilogy(x, b**x, label=f"${b}^x$")   # log-scale y-axis
axes[0].set_title("Linear axes: only the fastest curve is visible")
axes[1].set_title("Log axes: each exponential is a straight line")
for ax in axes:
    ax.set_xlabel("x"); ax.legend()
plt.tight_layout(); plt.show()
```

**Interpretation.** On the left, $1.1^x$ and $1.3^x$ look flat next to $1.6^x$ — the picture misleads. On the right, all three are straight lines with slopes proportional to $\ln b$, and their behavior over the whole range is comparable at a glance. Whenever data spans several orders of magnitude, reach for a log scale.

```{admonition} Common Mistakes
:class: warning
**Degrees in code.** `np.sin(30)` computes the sine of 30 *radians* (about $-0.988$), not of $30°$. Convert first: `np.sin(np.deg2rad(30))` gives $0.5$. Everything in this book is radians.

**$\ln(x + y) \neq \ln x + \ln y$.** The log of a *product* splits; the log of a sum does not simplify at all. Similarly $\ln(x)/\ln(y)$ is not $\ln(x/y)$ — the former is $\log_y x$ by change of base.

**$\sin^{-1}x$ versus $(\sin x)^{-1}$.** By convention $\sin^{-1}$ means arcsine, while $\sin^2 x$ means $(\sin x)^2$. The notation is inconsistent; the meaning, unfortunately, must be memorized.

**Forgetting the quadrant.** $\arcsin$ returns values only in $[-\pi/2, \pi/2]$, so $\arcsin(\sin\theta)$ equals $\theta$ only for $\theta$ in that interval: $\arcsin\bigl(\sin\frac{5\pi}{6}\bigr) = \frac{\pi}{6}$, not $\frac{5\pi}{6}$.
```

```{admonition} Data Science Connection
:class: tip
The logistic (sigmoid) function of classification, $\sigma(x) = \dfrac{1}{1 + e^{-x}}$, is built from $e^x$; the log-loss it is trained with is built from $\ln$; and periodic features (hour of day, day of year) are routinely encoded as $\sin$/$\cos$ pairs precisely because of the unit-circle definition — the pair $(\cos\theta, \sin\theta)$ places each time on a circle so that 11:59 PM sits next to 12:01 AM, as it should.
```

## 2.5 Exercises

### Quick Check

1. Evaluate without a calculator: $\log_2 32$, $\ln e^7$, $10^{\log_{10} 4}$, $\log_5 1$.
2. Convert $135°$ to radians and $\pi/5$ to degrees.
3. What are the domain and range of $\ln x$? Of $e^x$? How are the answers related?
4. Which is larger for very large $x$: $x^{100}$ or $1.01^x$?

````{admonition} Answers to Quick Checks
:class: dropdown
1. $5$; $7$; $4$; $0$.
2. $135° = \frac{3\pi}{4}$; $\ \pi/5 = 36°$.
3. $\ln$: domain $(0,\infty)$, range $\mathbb{R}$. $e^x$: domain $\mathbb{R}$, range $(0,\infty)$. Each is the other with domain and range swapped, because the functions are inverses.
4. $1.01^x$ — any exponential with base $>1$ eventually exceeds any fixed power.
````

### Basic Practice

5. Solve for $x$: (a) $e^{3x} = 20$;  (b) $\log_2(x - 1) = 5$;  (c) $4 \cdot 2^{x} = 3^{x}$.
6. Simplify using log laws: (a) $\ln(e^2 x^3) - 3\ln x$;  (b) $\log_{10} 50 + \log_{10} 2$.
7. Using reference angles, evaluate exactly: $\cos\frac{2\pi}{3}$, $\sin\frac{7\pi}{6}$, $\tan\frac{3\pi}{4}$.
8. Given $\sin\theta = \frac{3}{5}$ with $\theta$ in the second quadrant, find $\cos\theta$ and $\tan\theta$ exactly.

````{admonition} Solution to Exercise 5(c)
:class: dropdown
Take natural logs of $4 \cdot 2^x = 3^x$:

$$
\ln 4 + x\ln 2 = x \ln 3
\;\Longrightarrow\;
\ln 4 = x(\ln 3 - \ln 2)
\;\Longrightarrow\;
x = \frac{\ln 4}{\ln(3/2)} \approx \frac{1.3863}{0.4055} \approx 3.419.
$$

Check: $4 \cdot 2^{3.419} \approx 4(10.70) \approx 42.8$ and $3^{3.419} \approx 42.8$. ✓
````

````{admonition} Solution to Exercise 8
:class: dropdown
From $\sin^2\theta + \cos^2\theta = 1$: $\cos^2\theta = 1 - \frac{9}{25} = \frac{16}{25}$, so $\cos\theta = \pm\frac45$. In the second quadrant cosine is negative: $\cos\theta = -\frac{4}{5}$. Then $\tan\theta = \dfrac{\sin\theta}{\cos\theta} = \dfrac{3/5}{-4/5} = -\dfrac{3}{4}$.
````

### Intermediate Practice

9. A quantity decays exponentially with half-life 12 hours: $Q(t) = Q_0 \left(\tfrac12\right)^{t/12}$. How long until only 10% remains?
10. Derive the identity $\cos^2\theta = \frac{1 + \cos 2\theta}{2}$ from the double-angle formula for cosine, showing each algebraic step.
11. Solve $2\sin^2 x - \sin x - 1 = 0$ for all $x$ in $[0, 2\pi)$. *(Hint: it factors like a quadratic in $\sin x$.)*
12. Show that $\ln\bigl(x + \sqrt{x^2 - 1}\bigr) + \ln\bigl(x - \sqrt{x^2-1}\bigr) = 0$ for $x \ge 1$, and explain what this says about the two quantities inside the logarithms.

````{admonition} Hint for Exercise 11
:class: dropdown
Let $s = \sin x$. Then $2s^2 - s - 1 = (2s + 1)(s - 1)$. Solve each factor, then find *all* angles in $[0, 2\pi)$ with those sine values — one factor gives one angle, the other gives two.
````

### Conceptual Understanding

13. Explain why $b = 1$ is excluded in the definition of the exponential function and of $\log_b$.
14. Your plot of app downloads over three years looks like a hockey stick. A colleague says "growth exploded last quarter." Using this chapter, give an alternative explanation and describe the single plot change that would distinguish the two hypotheses.
15. Explain geometrically, using the unit circle, why $\sin(\pi - \theta) = \sin\theta$ and $\cos(-\theta) = \cos\theta$.

### Python Practice

16. Verify your answer to Exercise 9 numerically, and then reproduce it symbolically with `sp.solve`.
17. Write a loop (or vectorized expression) that checks the angle-sum identity $\sin(\alpha+\beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta$ at 1000 random pairs $(\alpha, \beta)$ and prints the maximum absolute discrepancy. Explain why the result is not exactly zero.

### Visualization Practice

18. Plot $\tan x$ on $(-\pi/2, \pi/2)$ and on a wider window with its vertical asymptotes indicated by dashed lines. Explain the asymptotes using the definition $\tan = \sin/\cos$.
19. Generate data $y = 3x^{2.5}$ for $x$ from 1 to 100, plot it on linear axes and on log-log axes, and read the exponent $2.5$ off the log-log slope between two chosen points, as in {prf:ref}`ex-power-law`.

### Challenge

20. Without a calculator, determine which is larger: $e^\pi$ or $\pi^e$. *(Hint: compare $\frac{\ln x}{x}$ at $x = e$ and $x = \pi$; you may use the fact, provable in Chapter 6, that $\frac{\ln x}{x}$ is decreasing for $x > e$.)*
21. The **hyperbolic functions** are $\cosh x = \frac{e^x + e^{-x}}{2}$ and $\sinh x = \frac{e^x - e^{-x}}{2}$. Prove that $\cosh^2 x - \sinh^2 x = 1$ and explain in one sentence the analogy and the difference with $\sin^2 + \cos^2 = 1$.

## 2.6 Summary

Exponentials $b^x$ multiply by a fixed factor per unit step, share the point $(0,1)$, and eventually outgrow every polynomial; base $e \approx 2.71828$ is the calculus-native choice. Logarithms invert exponentials, turning products into sums and powers into multiples; $\ln$ and $e^x$ undo each other, and log scales make exponential data readable. Trigonometric functions come from coordinates on the unit circle, are $2\pi$-periodic, and satisfy $\sin^2 + \cos^2 = 1$ together with the angle-sum, double-angle, and power-reduction identities that Part II's integration techniques will require. Radians are mandatory. Python verifies all of this numerically (NumPy) and exactly (SymPy), and `semilogy`/log-log plots are the standard tools for exponential and power-law data.

*Parallel reading:* OpenStax *Calculus Volume 1*, Sections 1.3–1.5 {cite}`openstax_calc1`.
