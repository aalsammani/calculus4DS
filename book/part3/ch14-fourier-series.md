# Chapter 14 · Fourier Series

Taylor series approximate a function by polynomials, matching it perfectly at one point and trusting it outward. This chapter changes the basis and the philosophy: **Fourier series** approximate a *periodic* function by sines and cosines, matching it *on average across the whole period*. Where Taylor answers "what does $f$ look like near $a$?", Fourier answers "what frequencies is $f$ made of?" — the natural question for signals, seasonal data, sound, and vibration. The mathematics needed is exactly what Parts I–II built: definite integrals, integration by parts, and the trigonometric identities of Chapter 2. This chapter treats the classical period-$2\pi$ theory; it is the optional capstone of Part III and the historical gateway to signal processing.

## 14.1 The idea: functions as combinations of waves

A **periodic function** with period $2\pi$ satisfies $f(x + 2\pi) = f(x)$ for all $x$; it is determined by its values on any window of length $2\pi$, conventionally $[-\pi, \pi]$. The building blocks available at that period are the constant $1$ and the harmonics

$$
\cos x,\ \sin x,\ \cos 2x,\ \sin 2x,\ \cos 3x,\ \sin 3x,\ \ldots
$$

— waves completing $1, 2, 3, \ldots$ full cycles per period. Fourier's audacious claim (1807, met with disbelief by the referees) was that essentially *any* periodic function, jumps and corners included, is an infinite combination of these:

$$
f(x) \;\sim\; \frac{a_0}{2} \;+\; \sum_{k=1}^{\infty}\bigl(a_k\cos kx + b_k\sin kx\bigr).
$$

The task is to find the coefficients — how much of each frequency $f$ contains — and the tool that isolates them is a pair of integral identities.

## 14.2 Orthogonality: the coefficient extractor

The harmonics obey a striking system of integral relations over one period (proved by the product-to-sum identities, or by the integration-by-parts computation you did in Chapter 10, Exercise 13):

```{prf:theorem} Orthogonality relations
:label: thm-orthogonality
For positive integers $m, n$:

$$
\int_{-\pi}^{\pi}\sin mx\,\sin nx\;dx =
\begin{cases}0, & m\ne n\\ \pi, & m=n\end{cases}
\qquad
\int_{-\pi}^{\pi}\cos mx\,\cos nx\;dx =
\begin{cases}0, & m\ne n\\ \pi, & m=n\end{cases}
$$

and $\displaystyle\int_{-\pi}^{\pi}\sin mx\,\cos nx\;dx = 0$ always; also $\int_{-\pi}^{\pi}\cos nx\,dx = \int_{-\pi}^{\pi}\sin nx\,dx = 0$.
```

In words: *distinct harmonics ignore each other in integration* — every cross-product averages to zero — while each harmonic paired with itself yields $\pi$. (The vocabulary is deliberate: these are the trig analogue of perpendicular vectors having zero dot product, an analogy Part IV will make exact — the integral of a product is a dot product with infinitely many components.)

Orthogonality turns coefficient-finding into a mechanical act. Multiply the claimed expansion by one chosen harmonic, say $\sin nx$, and integrate over the period: on the right, *every term dies* except the one matching partner $b_n\sin nx$, which contributes $b_n\pi$. Solving:

```{prf:definition} Fourier coefficients
:label: def-fourier-coefficients
The **Fourier series** of an integrable function $f$ on $[-\pi,\pi]$ has coefficients

$$
a_k = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\cos kx\;dx \quad(k \ge 0),
\qquad
b_k = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\sin kx\;dx \quad(k \ge 1).
$$

(The convention of writing the constant term as $\frac{a_0}{2}$ lets one formula cover $a_0$: the constant term is the **average value** $\frac{1}{2\pi}\int_{-\pi}^{\pi}f$.)
```

Two symmetry shortcuts eliminate half the work before it starts. If $f$ is **odd** ($f(-x) = -f(x)$), every $f(x)\cos kx$ is odd and integrates to zero: all $a_k = 0$, sines only. If $f$ is **even**, all $b_k = 0$, cosines only — and the surviving integrals may be computed as $\frac{2}{\pi}\int_0^\pi$.

## 14.3 Three classical expansions

```{prf:example} The square wave
:label: ex-fourier-square
Find the Fourier series of the square wave $f(x) = \begin{cases}-1, & -\pi < x < 0\\ +1, & 0 < x < \pi\end{cases}$.

$f$ is odd, so $a_k = 0$ and

$$
b_k = \frac{2}{\pi}\int_0^{\pi}\sin kx\;dx
    = \frac{2}{\pi}\left[\frac{-\cos kx}{k}\right]_0^{\pi}
    = \frac{2}{\pi k}\bigl(1 - \cos k\pi\bigr)
    = \frac{2}{\pi k}\bigl(1 - (-1)^k\bigr).
$$

The factor $1 - (-1)^k$ is $2$ for odd $k$ and $0$ for even $k$: even harmonics are absent entirely, and

$$
f(x) \sim \frac{4}{\pi}\left(\sin x + \frac{\sin 3x}{3} + \frac{\sin 5x}{5} + \cdots\right).
$$

A jump discontinuity costs slowly-decaying coefficients ($\sim 1/k$): sharp edges are expensive in frequencies, a principle that governs everything from audio compression to why low-pass-filtered images look soft.
```

```{figure} figures/ch14-fourier-square.png
:name: fig-fourier-square
:alt: A square wave together with Fourier partial sums using increasing numbers of harmonics; the approximations ripple around the flat portions, improve with more terms, but persistently overshoot just next to each jump.

Partial sums of the square wave's Fourier series. More harmonics track the flat portions ever better — but beside each jump the sum *overshoots by about 9%* no matter how many terms are taken (the measured peak with 100 harmonics is $1.1790$, against the theoretical Gibbs constant $1.17898\ldots$). The overshoot narrows but never shrinks in height: the **Gibbs phenomenon**.
```

```{prf:example} The sawtooth
:label: ex-fourier-sawtooth
Find the Fourier series of $f(x) = x$ on $(-\pi, \pi)$, extended periodically.

Odd again, so sines only; integration by parts (Chapter 10, $u = x$, $dv = \sin kx\,dx$):

$$
b_k = \frac{2}{\pi}\int_0^{\pi} x\sin kx\;dx
    = \frac{2}{\pi}\left[\frac{-x\cos kx}{k} + \frac{\sin kx}{k^2}\right]_0^{\pi}
    = \frac{2}{\pi}\cdot\frac{-\pi(-1)^k}{k}
    = \frac{2(-1)^{k+1}}{k},
$$

giving

$$
x \sim 2\left(\sin x - \frac{\sin 2x}{2} + \frac{\sin 3x}{3} - \cdots\right), \qquad -\pi < x < \pi.
$$

At $x = \frac{\pi}{2}$ this specializes to $\frac{\pi}{4} = 1 - \frac13 + \frac15 - \cdots$ — the Leibniz series, recovered here as one point-evaluation of a Fourier expansion.
```

```{prf:example} The parabola, and a famous sum
:label: ex-fourier-parabola
Find the Fourier series of $f(x) = x^2$ on $[-\pi, \pi]$, and use it.

Even function: cosines only. The average is $a_0/2$ with $a_0 = \frac{2}{\pi}\int_0^\pi x^2dx = \frac{2\pi^2}{3}$. For $k \ge 1$, two rounds of parts (as in {prf:ref}`ex-parts-twice` of Chapter 10) give

$$
a_k = \frac{2}{\pi}\int_0^{\pi}x^2\cos kx\;dx = \frac{4(-1)^k}{k^2},
$$

so

$$
x^2 \sim \frac{\pi^2}{3} + 4\sum_{k=1}^{\infty}\frac{(-1)^k}{k^2}\cos kx.
$$

This expansion converges *at the endpoints too* (the periodic extension of $x^2$ is continuous — the pieces meet at $x=\pm\pi$), and evaluating at $x = \pi$, where $\cos k\pi = (-1)^k$:

$$
\pi^2 = \frac{\pi^2}{3} + 4\sum_{k=1}^{\infty}\frac{1}{k^2}
\quad\Longrightarrow\quad
\sum_{k=1}^{\infty}\frac{1}{k^2} = \frac{\pi^2}{6}.
$$

The **Basel problem** — which defeated the Bernoullis and made Euler's name — falls out of one Fourier expansion evaluated at one point. Chapter 12 could only report that this $p$-series converges; now you possess its value, $1.644934\ldots$
```

## 14.4 What convergence means here

For a piecewise-smooth $f$ (finitely many jumps and corners per period — everything in practice), the classical convergence theorem states: at each point where $f$ is continuous, the Fourier series converges to $f(x)$; at each jump, it converges to the **midpoint** of the jump, $\frac{f(x^-) + f(x^+)}{2}$ — the square wave's series returns $0$ at $x=0$, splitting the difference. Near a jump, partial sums exhibit the **Gibbs phenomenon** visible in {numref}`fig-fourier-square`: an overshoot of about $9\%$ of the jump that narrows with more terms but never diminishes in height. Smoothness buys speed: coefficients decay like $1/k$ for jump discontinuities (square wave, sawtooth), $1/k^2$ for continuous functions with corners (the parabola's periodic extension), and faster the smoother the periodic extension — a dictionary between a function's roughness and its frequency content.

Two contrasts with Taylor series organize the picture. Taylor uses data at *one point* (all derivatives there) and approximates *locally*, superbly near the center, with polynomial pieces that fly off to $\pm\infty$; Fourier uses data *across the period* (integrals of $f$) and approximates *globally*, tolerating jumps that Taylor cannot even define, with bounded waves that repeat forever. Neither is better; they answer different questions, and mature practice keeps both.

## 14.5 Common mistakes

```{admonition} Common Mistakes
:class: warning
**Forgetting the $\frac{1}{\pi}$** in the coefficient formulas — the orthogonality integrals equal $\pi$, not $1$, and the normalization must repay it.

**Halving errors on $a_0$.** With the $\frac{a_0}{2}$ convention, the constant term of the series is the *average* of $f$; writing $a_0$ itself as the constant term doubles it. State your convention and stay loyal.

**Symmetry claimed but not owned.** The even/odd shortcuts apply to $f$'s behavior on $(-\pi,\pi)$ — the sawtooth $f(x) = x$ is odd there, but $f(x) = x$ on $(0, 2\pi)$ extended is neither even nor odd. Check symmetry on the *actual* expansion window.

**Expecting equality at jumps.** The series converges to jump midpoints, not to your preferred one-sided value; and no finite partial sum eliminates the Gibbs overshoot. Neither is a bug in your coefficients.

**Integrating by parts with limits dropped.** The boundary terms $\bigl[uv\bigr]_{-\pi}^{\pi}$ in coefficient computations frequently *don't* vanish (they carry the $(-1)^k$ factors, as in {prf:ref}`ex-fourier-sawtooth`); dropping them silently is the classic coefficient error.

**Radian amnesia, final warning.** All of this chapter's integrals live in radians; the period is $2\pi$, not $360$.
```

## 14.6 Now do it in Python

SymPy computes coefficients symbolically — good for verifying hand integration — and NumPy assembles partial sums for the eye.

```python
import sympy as sp

x = sp.symbols('x')
k = sp.symbols('k', integer=True, positive=True)

# --- Verify the three classical expansions' coefficients ---
b_saw = sp.integrate(x*sp.sin(k*x), (x, -sp.pi, sp.pi))/sp.pi
print(sp.simplify(b_saw))                     # -2*(-1)**k/k  == 2(-1)^{k+1}/k

a_par = sp.integrate(x**2*sp.cos(k*x), (x, -sp.pi, sp.pi))/sp.pi
print(sp.simplify(a_par))                     # 4*(-1)**k/k**2

f_sq = sp.Piecewise((-1, x < 0), (1, True))
b_sq = sp.integrate(f_sq*sp.sin(k*x), (x, -sp.pi, sp.pi))/sp.pi
print(sp.simplify(b_sq))                      # 2*(1 - (-1)**k)/(pi*k)

# --- Basel payoff, numerically ---
import numpy as np
print((1/np.arange(1, 200_001)**2).sum(), np.pi**2/6)   # 1.6449290..., 1.6449340...
```

Note the Basel check's gap in the sixth decimal: after *two hundred thousand* terms the tail $\sum_{k>N} k^{-2} \approx \frac1N$ still contributes $5\times10^{-6}$. The exact value from {prf:ref}`ex-fourier-parabola` beats brute-force summation decisively — analysis giving what computation only crawls toward, the same lesson Chapter 12's harmonic series taught in reverse.

Partial sums for any coefficient recipe, vectorized:

```python
def fourier_partial(bs, x, N):
    """Sum b_k sin(kx) for k=1..N; bs(k) supplies coefficients."""
    ks = np.arange(1, N + 1)
    return (bs(ks) * np.sin(np.outer(x, ks))).sum(axis=1)

t = np.linspace(-np.pi, np.pi, 2000)
saw = fourier_partial(lambda ks: 2*(-1.0)**(ks+1)/ks, t, 40)
```

**Visualization and interpretation.** Plot `saw` against the true line $y = t$: the fit is excellent mid-interval, degrades toward $\pm\pi$ where the periodic extension jumps from $\pi$ down to $-\pi$, and rings with Gibbs oscillation beside those jumps. Then plot the coefficient magnitudes $|b_k|$ against $k$ on a log-log scale for the sawtooth ($\sim 1/k$) and the parabola ($\sim 1/k^2$): the decay *rate* is the smoothness of the function, read directly off the spectrum. Looking at data through its coefficients rather than its values — the **spectral view** — is the habit this chapter exists to seed.

```{admonition} Data Science Connection
:class: tip
Fourier's idea, discretized, is the **Discrete Fourier Transform**, computed by the FFT algorithm (`numpy.fft`) in $O(n\log n)$ — arguably the most-used algorithm in scientific computing. Its fingerprints in data work: extracting seasonality from time series (a year of daily sales decomposes into weekly and annual harmonics); the sine/cosine *time features* fed to forecasting models are truncated Fourier bases; spectrograms turn audio into the images that speech models consume; and positional encodings in transformer architectures are precisely a bank of sines and cosines at geometrically spaced frequencies. When a signal is periodic, frequency space is its honest coordinate system.
```

```{admonition} Looking Ahead
:class: seealso
Orthogonality did all the work in this chapter, and it is a *linear-algebra* phenomenon: the harmonics behave like perpendicular axes, and Fourier coefficients are coordinates — projections onto those axes. Part IV builds that language properly (dot products, orthogonal bases, projections), after which the coefficient formulas of {prf:ref}`def-fourier-coefficients` will re-read as one more instance of a universal recipe: coefficient = inner product with a unit basis vector.
```

## 14.7 Exercises

### Quick Check

1. What is the constant term of the Fourier series of $f$, in terms of $f$?
2. A function is even on $(-\pi,\pi)$. Which coefficients vanish?
3. The square-wave series at $x = 0$ converges to what value, and why?
4. Coefficients decaying like $1/k^2$ suggest what about the function?

````{admonition} Answers to Quick Checks
:class: dropdown
1. Its average value over the period, $\frac{1}{2\pi}\int_{-\pi}^{\pi}f = \frac{a_0}{2}$.
2. All $b_k$ (the sine coefficients).
3. To $0$ — the midpoint of the jump from $-1$ to $+1$ (also visible term by term: every $\sin(k\cdot 0) = 0$).
4. Continuous, with corners (kinks) but no jumps — like the periodic extension of $x^2$ or the triangle wave.
````

### Basic Practice

5. Verify the orthogonality relation $\int_{-\pi}^{\pi}\cos 2x\cos 3x\,dx = 0$ by the product-to-sum identity, and $\int_{-\pi}^{\pi}\cos^2 3x\,dx = \pi$ by power reduction.
6. Compute the Fourier series of $f(x) = \begin{cases}0, & -\pi<x<0\\ 1, & 0<x<\pi\end{cases}$ — either directly, or with no integration at all by writing $f = \frac12 + \frac12(\text{square wave})$ and citing {prf:ref}`ex-fourier-square`.
7. Find the Fourier series of $f(x) = |\sin x|$ *(even; the integrals $\int_0^\pi \sin x\cos kx\,dx$ need a product-to-sum identity)* and state its constant term — the average of a rectified sine, a number every electrical engineer knows.
8. Using the sawtooth series at $x = \frac\pi2$, derive the Leibniz formula $\frac\pi4 = 1 - \frac13 + \frac15 - \cdots$, and estimate how many terms it needs for 3-decimal accuracy via Chapter 12's alternating-series bound.

````{admonition} Solution to Exercise 6
:class: dropdown
$f = \frac12 + \frac12 f_{\text{sq}}$ where $f_{\text{sq}}$ is {prf:ref}`ex-fourier-square`'s wave, so by linearity of the coefficient integrals:

$$
f(x) \sim \frac12 + \frac{2}{\pi}\left(\sin x + \frac{\sin 3x}{3} + \frac{\sin 5x}{5} + \cdots\right).
$$

Decomposing a function into known pieces before integrating is as valuable here as it was in Chapter 8.
````

### Intermediate Practice

9. Find the Fourier series of the triangle wave $f(x) = |x|$ on $[-\pi,\pi]$. *(Even; parts once. Answer: $\frac{\pi}{2} - \frac{4}{\pi}\sum_{k \text{ odd}}\frac{\cos kx}{k^2}$.)* Then evaluate it at $x=0$ to sum $\sum_{k\text{ odd}}\frac{1}{k^2}$, and combine with the Basel value to find $\sum_{k \text{ even}}\frac{1}{k^2}$ — confirming the even part is exactly $\frac14$ of the whole, as reindexing $k = 2m$ predicts.
10. Differentiate the triangle-wave series of Exercise 9 term by term and compare with the square-wave series of {prf:ref}`ex-fourier-square`. Explain why differentiating a Fourier series costs one power of $k$ in coefficient decay, and what that predicts about differentiating the *square* wave's series.
11. The square wave's partial sum with harmonics through $k = N$ has its first peak near $x = \frac{\pi}{N+1}$. Numerically locate the peak for $N = 25, 51, 101$ and confirm the overshoot height approaches the Gibbs value $\frac{2}{\pi}\int_0^\pi\frac{\sin t}{t}dt = 1.17898\ldots$ — the $\operatorname{Si}$ function of Chapter 7's challenge, resurfacing.
12. A daily-sampled signal has period 7 (weekly seasonality). Adapt {prf:ref}`def-fourier-coefficients` to period $2L$ ($L = 3.5$) by substituting appropriately, and state the harmonics' frequencies in cycles per day.

### Conceptual Understanding

13. Taylor and Fourier both write $f$ as an infinite combination of basis functions. Contrast them on: what data of $f$ they consume, where they are accurate, and what happens outside that region.
14. Explain why a jump discontinuity forces coefficients no smaller than order $1/k$, arguing from Exercise 10's differentiation principle run in reverse (integration *gains* a power of $k$).
15. The orthogonality relations were called "perpendicularity" for functions. Propose the analogy explicitly: what plays the role of vectors, of the dot product, and of coordinates? *(Part IV will grade your answer.)*

### Python Practice

16. Verify Exercises 7 and 9's coefficients with SymPy, then plot 3-term and 15-term partial sums of the triangle wave against $|x|$ and describe how much faster it converges than the square wave — and connect that to the $1/k^2$ versus $1/k$ decay.
17. Load one year of a synthetic daily series `y = 10 + 3*np.sin(2*np.pi*np.arange(365)/7) + rng.normal(0, 1, 365)` and compute `np.fft.rfft(y)`. Identify the frequency bin with the largest magnitude (after the constant) and confirm it corresponds to the weekly cycle. One line of spectrum reading has just performed seasonality detection.

### Visualization Practice

18. Reproduce {numref}`fig-fourier-square` for the sawtooth: partial sums with 5, 20, and 80 terms over two full periods (plot the periodic extension, not just $y=x$), highlighting the jump at $x = \pi$ and the midpoint value there.
19. For the parabola series of {prf:ref}`ex-fourier-parabola`, plot the maximum absolute error of the $N$-term partial sum against $N$ on a log-log scale for $N = 1,\ldots,100$. What slope do you observe, and how does it follow from the $1/k^2$ coefficients?

### Challenge

20. Apply **Parseval's identity** — $\frac{1}{\pi}\int_{-\pi}^{\pi}f^2\,dx = \frac{a_0^2}{2} + \sum_{k\ge1}(a_k^2+b_k^2)$, the statement that energy is preserved between a function and its spectrum — to the sawtooth of {prf:ref}`ex-fourier-sawtooth` to prove the Basel result $\sum\frac{1}{k^2} = \frac{\pi^2}{6}$ a second way, and to the parabola to evaluate $\sum_{k\ge1}\frac{1}{k^4}$. *(Answer to the latter: $\frac{\pi^4}{90}$.)*
21. The **heat equation** origin story: Fourier invented these series to solve for temperature in a rod. Given initial temperature $f(x) = $ the square wave and the fact that each harmonic $\sin kx$ decays in time as $e^{-k^2 t}\sin kx$, write the temperature $u(x,t)$ as a series, plot it at $t = 0, 0.01, 0.1, 1$, and explain physically why the Gibbs wiggles vanish almost instantly while the broad shape survives — high frequencies die fastest, at rate $k^2$.

### Cumulative Review

22. *(Ch. 10)* Re-derive the sawtooth coefficient $b_k = \frac{2(-1)^{k+1}}{k}$ showing every step of the integration by parts, including the boundary term that supplies $(-1)^k$.
23. *(Ch. 13)* The function $g(x) = \frac{4}{\pi}\sin x$ is both the first Fourier partial sum of the square wave and an analytic function with its own Taylor series. Write the degree-3 Taylor polynomial of $g$ at $0$, and reflect in a sentence: Taylor of Fourier, each basis doing its own job.

## 14.8 Summary

A $2\pi$-periodic function decomposes into harmonics, $f \sim \frac{a_0}{2} + \sum(a_k\cos kx + b_k\sin kx)$, with coefficients extracted by the orthogonality relations — distinct harmonics integrate to zero against each other, so multiplying by one harmonic and integrating isolates its coefficient: $a_k = \frac1\pi\int f\cos kx$, $b_k = \frac1\pi\int f\sin kx$, the constant term being $f$'s average. Even functions take cosines only, odd functions sines only. The classical trio — square wave ($\frac4\pi\sum_{\text{odd}}\frac{\sin kx}{k}$), sawtooth ($2\sum\frac{(-1)^{k+1}}{k}\sin kx$), parabola (whose evaluation at $\pi$ solves the Basel problem, $\sum k^{-2} = \frac{\pi^2}6$) — exhibits the general dictionary: smoother periodic extensions have faster-decaying coefficients ($1/k$ for jumps, $1/k^2$ for corners), convergence lands on midpoints at jumps, and beside every jump the Gibbs overshoot of $\approx 9\%$ persists at any truncation. Fourier is Taylor's global, integral-fed counterpart; computationally it becomes the FFT, and conceptually its orthogonality is the bridge into the linear algebra of Part IV.

*Parallel reading:* OpenStax *Calculus Volume 2*, Section 6.4 exercises hint at the theme; fuller treatments are in any signals text — and the linear-algebra reading returns in {cite}`strang_linalg`.
