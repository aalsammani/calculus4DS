# Chapter 12 · Summation, Sequences, and Infinite Series

Part III changes the object of study from continuous accumulation to *discrete* accumulation: adding up infinitely many numbers. The question sounds paradoxical — how can an endless sum have a finite answer? — and the resolution, via limits of partial sums, is one of analysis's cleanest ideas. The payoff for data science is direct: series are how functions get represented on computers (Chapter 13), how signals get decomposed (Chapter 14), and the sums themselves — geometric series above all — appear throughout probability, discounting, and algorithm analysis. This chapter builds the language (summation notation, sequences), the central definition (convergence of a series), the essential examples (geometric and harmonic), and the basic tests for telling convergence from divergence.

## 12.1 Summation notation

The capital-sigma notation compresses sums:

$$
\sum_{k=1}^{n} a_k = a_1 + a_2 + \cdots + a_n,
$$

with $k$ the (bound, renameable) **index**, running from the lower to the upper limit. Manipulating sums uses exactly two rules, the discrete twins of integral linearity:

$$
\sum_k (a_k + b_k) = \sum_k a_k + \sum_k b_k,
\qquad
\sum_k c\,a_k = c\sum_k a_k,
$$

plus re-indexing (shifting $k$) when convenient. Three closed forms recur constantly and are worth owning:

$$
\sum_{k=1}^n 1 = n,
\qquad
\sum_{k=1}^n k = \frac{n(n+1)}{2},
\qquad
\sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}{6}.
$$

(The second is Gauss's schoolroom trick: pair first with last, $1 + n = 2 + (n-1) = \cdots$, giving $\frac n2$ pairs each summing to $n+1$.) These formulas are what made Chapter 7's Riemann-sum limits computable by hand; here they serve as warm-ups for infinite sums.

```{prf:example} A Riemann sum, revisited with closed forms
:label: ex-summation-riemann
Compute $\displaystyle\lim_{n\to\infty}\sum_{k=1}^{n}\frac{k^2}{n^3}$ exactly.

$$
\sum_{k=1}^n \frac{k^2}{n^3} = \frac{1}{n^3}\cdot\frac{n(n+1)(2n+1)}{6}
= \frac{2n^3 + 3n^2 + n}{6n^3} \;\longrightarrow\; \frac{2}{6} = \frac13.
$$

This is the right-endpoint Riemann sum for $\int_0^1 x^2\,dx$ evaluated without calculus — the closed form doing what FTC did. Discrete and continuous accumulation keep answering each other's questions; that dialogue is the theme of the Part.
```

## 12.2 Sequences and their limits

```{prf:definition} Sequence; limit of a sequence
:label: def-sequence
A **sequence** $(a_n)$ is a function from the positive integers to the reals: an infinite ordered list $a_1, a_2, a_3, \ldots$ The sequence **converges** to $L$, written $\lim_{n\to\infty}a_n = L$, if $a_n$ gets and stays arbitrarily close to $L$ as $n$ grows; otherwise it **diverges**.
```

Sequence limits behave like the function limits of Chapter 3 (sums, products, quotients pass through), and indeed if $a_n = f(n)$ for a function with $\lim_{x\to\infty}f(x) = L$, the sequence inherits the limit — putting Part I's tools at our disposal. The workhorse facts:

$$
\frac{1}{n^p} \to 0 \ (p > 0),
\qquad
r^n \to 0 \ (|r| < 1),
\qquad
\frac{c^n}{n!} \to 0 \ (\text{any } c),
\qquad
n^{1/n} \to 1,
$$

and the ordering of growth rates from Chapter 2 — logarithms $\ll$ powers $\ll$ exponentials $\ll$ factorials — settles most quotient limits by inspection: $\frac{n^{100}}{1.01^n} \to 0$, slowly but surely.

```{prf:example} Sequence limits by Part I methods
:label: ex-seq-limits
(a) $a_n = \dfrac{3n^2 - n}{5n^2 + 4}$: divide by $n^2$ → $\dfrac{3 - 1/n}{5 + 4/n^2} \to \dfrac35$.

(b) $a_n = \left(1 + \dfrac1n\right)^{\!n}$: the compound-interest sequence of Chapter 2, converging to $e = 2.71828\ldots$ (take logs: $n\ln(1 + \frac1n) = \frac{\ln(1+h)}{h}\big|_{h=1/n} \to 1$, the derivative of $\ln$ at $1$).

(c) $a_n = (-1)^n$: bounces between $\pm1$ forever — bounded but divergent. Boundedness alone is not convergence; the values must *settle*.
```

## 12.3 Infinite series: the central definition

```{prf:definition} Series, partial sums, convergence
:label: def-series
Given a sequence $(a_k)$, the **infinite series** $\sum_{k=1}^{\infty} a_k$ is the limit of its **partial sums** $s_n = \sum_{k=1}^{n}a_k$:

$$
\sum_{k=1}^{\infty} a_k \;=\; \lim_{n\to\infty} s_n,
$$

when the limit exists (the series **converges**, to that value); otherwise the series **diverges**. An infinite sum is thus not a new kind of addition but a *limit of ordinary finite additions*.
```

Everything about series flows from taking this definition literally. The two archetypes, side by side:

```{prf:example} The geometric series
:label: ex-geometric
For a ratio $r$, consider $\sum_{k=0}^{\infty} r^k = 1 + r + r^2 + \cdots$. The partial sum has a closed form — multiply $s_n = 1 + r + \cdots + r^n$ by $r$, subtract, and solve:

$$
s_n = \frac{1 - r^{n+1}}{1 - r} \qquad (r \neq 1).
$$

If $|r| < 1$ then $r^{n+1} \to 0$ and the series converges; if $|r| \ge 1$ the terms don't shrink and it diverges:

$$
\boxed{\;\sum_{k=0}^{\infty} r^k = \frac{1}{1 - r} \quad\text{for } |r| < 1.\;}
$$

Concretely, $\sum_{k=1}^\infty \left(\frac12\right)^k = \frac{1/2}{1 - 1/2} = 1$: half, plus a quarter, plus an eighth… fills the whole unit. The partial sums $0.5, 0.75, 0.9375, 0.999023, \ldots$ close half the remaining gap at every step ({numref}`fig-convergence-divergence`, left). More generally, first term $a$ and ratio $r$ give $\frac{a}{1-r}$ — a formula you will use weekly: discounted rewards in reinforcement learning ($\sum \gamma^k r_k$), expected numbers of trials, perpetuity values, steady states.
```

```{prf:example} The harmonic series
:label: ex-harmonic
The terms of $\sum_{k=1}^{\infty}\frac1k = 1 + \frac12 + \frac13 + \cdots$ shrink to zero — yet the series **diverges**. Group the terms:

$$
1 + \frac12 + \underbrace{\frac13 + \frac14}_{>\,\frac24 = \frac12} + \underbrace{\frac15 + \cdots + \frac18}_{>\,\frac48 = \frac12} + \underbrace{\frac19 + \cdots + \frac1{16}}_{>\,\frac12} + \cdots
$$

Each block exceeds $\frac12$, and there are infinitely many blocks: the partial sums pass every bound — but *glacially*, growing like $\ln n$ (the partial sums $H_n$ satisfy $H_n \approx \ln n + 0.5772$; numerically $H_{200} = 5.8780$ against $\ln 200 + \gamma = 5.8755$). Divergence can be slow enough that no computation would ever reveal it — only analysis does.
```

```{figure} figures/ch12-convergence-divergence.png
:name: fig-convergence-divergence
:alt: Two panels. Left: partial sums of the geometric series with ratio one half climbing steps toward the dashed limit line at one. Right: partial sums of the harmonic series rising without bound along a logarithmic curve, closely tracked by the dotted curve natural log n plus gamma.

The two archetypes. Left: geometric partial sums race to the limit $1$, halving the gap each term. Right: harmonic partial sums never level off — they climb forever along $\ln n + \gamma$, diverging too slowly for any finite computation to notice.
```

The harmonic series carries the chapter's most important warning, worth promoting to a theorem read *contrapositively*:

```{prf:theorem} Divergence test ($n$-th term test)
:label: thm-divergence-test
If $\sum a_k$ converges, then $a_k \to 0$. Equivalently: **if $a_k \not\to 0$, the series diverges.** The converse is false — $a_k \to 0$ guarantees nothing, as the harmonic series shows.
```

## 12.4 Convergence tests

With the definition and archetypes in place, most series are classified by *comparison to what we know*. Three tests cover this course's needs (a broader battery lives in OpenStax Volume 2, Chapter 5 {cite}`openstax_calc2`).

**The integral test and $p$-series.** For positive decreasing $f$, the sum $\sum f(k)$ and the integral $\int_1^\infty f(x)\,dx$ converge or diverge together — rectangles of the sum sandwich the area under the curve. Applying it to $f(x) = x^{-p}$, where $\int_1^\infty x^{-p}dx$ is finite exactly when $p > 1$:

$$
\sum_{k=1}^{\infty}\frac{1}{k^p}
\quad\text{converges for } p > 1, \text{ diverges for } p \le 1.
$$

So $\sum\frac1{k^2}$ converges (to $\frac{\pi^2}{6}$, a famous value verified numerically in §12.6), $\sum \frac{1}{\sqrt k}$ diverges, and the harmonic series is precisely the boundary case $p=1$ falling on the divergent side.

**Comparison.** A positive series smaller, term by term (or in ratio, asymptotically), than a convergent one converges; larger than a divergent one, diverges. In practice: identify the dominant behavior of $a_k$ for large $k$ and compare to the matching geometric or $p$-series. $\sum\frac{1}{k^2+3k+7}$ behaves like $\sum\frac1{k^2}$: convergent. $\sum\frac{k}{k^2+1}$ behaves like $\sum\frac1k$: divergent.

**Ratio test.** Compute $\rho = \lim_{k\to\infty}\bigl|\frac{a_{k+1}}{a_k}\bigr|$: if $\rho < 1$ the series converges (its tail is eventually dominated by a geometric series of ratio $\approx\rho$); if $\rho>1$ it diverges; $\rho = 1$ is silent (both $\sum\frac1k$ and $\sum\frac1{k^2}$ give $\rho=1$). The ratio test shines when factorials or $k$-th powers appear — which makes it *the* tool for the power series of Chapter 13.

```{prf:example} The ratio test on a factorial series
:label: ex-ratio-test
Does $\displaystyle\sum_{k=0}^{\infty}\frac{2^k}{k!}$ converge?

$$
\rho = \lim_{k\to\infty}\frac{2^{k+1}/(k+1)!}{2^k/k!} = \lim_{k\to\infty}\frac{2}{k+1} = 0 < 1:
$$

convergent, decisively — factorial growth in the denominator crushes any exponential. (Its value, $e^2$, is a Chapter 13 revelation.)
```

Finally, **alternating series** — terms of flip-flopping sign like $\sum\frac{(-1)^{k+1}}{k} = 1 - \frac12 + \frac13 - \cdots$ — converge under weak conditions (terms decreasing to zero; this one sums to $\ln 2$), with the practical bonus that the error after $n$ terms is at most the first omitted term. Sign cancellation rescues series whose absolute versions diverge; such *conditional* convergence is delicate (rearranging terms can change the sum), whereas series with $\sum|a_k| < \infty$ (**absolute** convergence) behave like finite sums in every way.

## 12.5 Common mistakes

```{admonition} Common Mistakes
:class: warning
**"Terms go to zero, so it converges."** The harmonic series is the permanent counterexample. The divergence test only ever proves *divergence*.

**Geometric formula outside its license.** $\frac{1}{1-r}$ requires $|r| < 1$. Writing $\sum 2^k = \frac{1}{1-2} = -1$ is absurd on its face — a sum of positives cannot be negative — yet the formula, misapplied, "produces" it.

**Off-by-one with the starting index.** $\sum_{k=0}^\infty r^k = \frac1{1-r}$ but $\sum_{k=1}^\infty r^k = \frac{r}{1-r}$: the first term matters. Write out the first term or two before invoking any formula.

**Concluding from $\rho = 1$.** The ratio test is silent there; switch to comparison or the $p$-series scale.

**Trusting partial sums numerically.** $H_n$ at $n = 10^6$ is about $14.4$ and still climbing — a computation that "looks convergent" for a divergent series. Numerics illustrates; analysis decides.

**Rearranging conditionally convergent series.** Legal for absolutely convergent series only; otherwise the sum itself can change (Riemann's rearrangement theorem — Exercise 20 for a taste).
```

## 12.6 Now do it in Python

Partial sums are one line of NumPy (`cumsum`), which makes the definition of convergence something you can *watch*.

```python
import numpy as np

# --- The two archetypes, numerically ---
k = np.arange(1, 21)
geo = np.cumsum(0.5 ** k)
print(geo[[0, 1, 3, 9, 19]])     # 0.5, 0.75, 0.9375, 0.999023, 0.99999905

k = np.arange(1, 200_001)
H = np.cumsum(1.0 / k)
print(H[9], H[99], H[-1])                 # 2.9290, 5.1874, 12.7832...
print(np.log(200_000) + 0.5772156649)     # 12.7832... — the ln n + γ law

# --- A convergent p-series and its famous limit ---
S = np.cumsum(1.0 / k**2)
print(S[-1], np.pi**2 / 6)       # 1.6449291..., 1.6449341...: five digits after 200k terms

# --- Ratio test, empirically, for Example 12.7 ---
kk = np.arange(0, 30)
terms = 2.0**kk / np.array([np.math.factorial(int(j)) for j in kk])
print((terms[1:] / terms[:-1])[:6])   # 2.0, 1.0, 0.667, 0.5, 0.4, 0.333 → 0
print(terms.cumsum()[-1], np.exp(2))  # 7.389056... both
```

SymPy evaluates many series *exactly*, and confirms divergence where numerics cannot:

```python
import sympy as sp

n = sp.symbols('n')
print(sp.Sum(sp.Rational(1, 2)**n, (n, 1, sp.oo)).doit())   # 1
print(sp.Sum(1/n**2, (n, 1, sp.oo)).doit())                 # pi**2/6
print(sp.Sum(1/n, (n, 1, sp.oo)).doit())                    # oo — divergence, certified
print(sp.Sum((-1)**(n+1)/n, (n, 1, sp.oo)).doit())          # log(2)
```

**Visualization and interpretation.** Plot the partial sums of $\sum\frac1{k^2}$ and of $\sum\frac1k$ on the same axes out to $n = 10{,}000$: one flattens under $\frac{\pi^2}{6} \approx 1.645$, the other climbs along $\ln n$ without pause. Then plot the *tail* $\frac{\pi^2}{6} - S_n$ of the first on log-log axes — it falls like $\frac1n$ (the integral test's error estimate), which tells you this convergent series is a *slow* one: five digits cost $200{,}000$ terms above. Convergence rate, not just convergence, is what computation cares about, and it is why Chapter 13's factorial-denominator series (ten digits from ten terms) are the ones machines actually use.

```{admonition} Data Science Connection
:class: tip
Geometric series *are* the mathematics of discounting: an agent receiving reward $r$ every step, discounted by $\gamma$ per step, accumulates value $\sum_{k=0}^\infty \gamma^k r = \frac{r}{1-\gamma}$ — the formula behind value functions in reinforcement learning, and the reason $\gamma \to 1$ makes horizons effectively infinite. The expected number of Bernoulli trials to first success, $\sum_k k(1-p)^{k-1}p = \frac1p$, is a differentiated geometric series (Exercise 19). And the divergence of the harmonic series is why "average of all data seen so far" learning rates ($\eta_k = \frac1k$) can keep learning forever: $\sum \eta_k = \infty$ ensures the steps can travel any distance, while $\sum \eta_k^2 < \infty$ keeps the noise bounded — the classic Robbins–Monro conditions, verbatim from this chapter's two archetypes.
```

```{admonition} Looking Ahead
:class: seealso
Everything here is scaffolding for Chapter 13, where the terms $a_k$ become $c_k x^k$ — series with a *variable* — and the ratio test decides for which $x$ they converge. The geometric series becomes the first and most important power series, $\frac1{1-x} = \sum x^k$, and differentiating or integrating it term by term will mass-produce others.
```

## 12.7 Exercises

### Quick Check

1. Expand and evaluate $\sum_{k=1}^{4}(2k - 1)$.
2. Does $\sum_{k=0}^{\infty}\left(\frac{3}{4}\right)^k$ converge? To what?
3. $a_k = \frac{k}{2k+1} \to \frac12 \neq 0$. What do you conclude about $\sum a_k$?
4. For which $p$ does $\sum k^{-p}$ converge?

````{admonition} Answers to Quick Checks
:class: dropdown
1. $1 + 3 + 5 + 7 = 16$ (the first four odd numbers — always $n^2$).
2. Yes: geometric, $|r| = \frac34 < 1$, sum $\frac{1}{1 - 3/4} = 4$.
3. Diverges, by the divergence test — terms must vanish for any hope of convergence.
4. $p > 1$.
````

### Basic Practice

5. Evaluate in closed form: (a) $\sum_{k=1}^{100}k$; (b) $\sum_{k=1}^{n}(3k^2 - 2k + 1)$; (c) $\sum_{k=3}^{\infty}\left(\frac12\right)^k$ *(mind the starting index)*.
6. Find the limit of each sequence or state divergence: (a) $\frac{5n^3+n}{2n^3-7}$; (b) $\frac{\ln n}{n}$; (c) $\frac{(-1)^n n}{n+1}$; (d) $\frac{3^n}{n!}$.
7. Determine convergence or divergence, naming the test: (a) $\sum\frac{1}{k^3}$; (b) $\sum\frac{k+1}{k}$; (c) $\sum\frac{1}{\sqrt{k}}$; (d) $\sum\frac{5^k}{k!}$; (e) $\sum\frac{1}{k^2+k}$.
8. A ball dropped from height $2$ m rebounds to $60\%$ of each fall. Find the total vertical distance it travels.

````{admonition} Solution to Exercise 8
:class: dropdown
Down $2$, then up-and-down $2(0.6), 2(0.6)^2, \ldots$ each counted twice:

$$
D = 2 + 2\sum_{k=1}^{\infty}2(0.6)^k = 2 + 4\cdot\frac{0.6}{0.4} = 2 + 6 = 8 \text{ m}.
$$
````

### Intermediate Practice

9. Express the repeating decimal $0.727272\ldots$ as a geometric series and hence as a fraction.
10. Use the integral test explicitly (set up and evaluate the integral) to decide $\sum_{k=2}^{\infty}\frac{1}{k\ln k}$ — a series that diverges *more slowly than harmonic*, defeating naive comparison.
11. **Telescoping.** Show $\frac{1}{k(k+1)} = \frac1k - \frac1{k+1}$, write the partial sum $s_n$ of $\sum_{k\ge1}\frac{1}{k(k+1)}$ in collapsed form, and evaluate the series exactly.
12. For the alternating series $\sum_{k=1}^\infty \frac{(-1)^{k+1}}{k^2}$: show it converges, and determine how many terms guarantee the partial sum is within $10^{-4}$ of the true value.

### Conceptual Understanding

13. Explain in your own words why the divergence test cannot be reversed, using the harmonic series and the picture of {numref}`fig-convergence-divergence`.
14. Zeno worried that crossing a room requires completing infinitely many half-crossings. Write the total time as a geometric series (constant speed) and explain how {prf:ref}`def-series` dissolves the paradox.
15. The ratio test compares a series to geometric behavior. Explain why it must fail (give $\rho=1$) on every $p$-series, whose terms decay polynomially rather than geometrically.

### Python Practice

16. Verify Exercises 7 and 11 with SymPy's `Sum(...).doit()`, and Exercise 9 with `sp.nsimplify(0.72727272727, rational=True)` as a cross-check.
17. Compute partial sums of $\sum\frac{(-1)^{k+1}}{k}$ to $n = 10^5$ and compare with $\ln 2$; then sum the *same terms rearranged* — two positives, one negative, repeating — to $10^5$ terms and report what value the rearrangement approaches instead ($\approx \frac32\ln 2$). Conditional convergence, demonstrated.

### Visualization Practice

18. Reproduce the spirit of {numref}`fig-convergence-divergence` for $\sum\frac1{k^2}$ (limit line at $\frac{\pi^2}{6}$) and $\sum\frac{1}{\sqrt k}$, and add a log-log plot of the first one's tail $\frac{\pi^2}6 - s_n$ with a slope $-1$ guide, confirming the $\frac1n$ convergence rate claimed in §12.6.

### Challenge

19. Differentiate the geometric series identity $\sum_{k=0}^\infty x^k = \frac{1}{1-x}$ term by term (legal inside $|x|<1$; Chapter 13 justifies it) to show $\sum_{k=1}^\infty k x^{k-1} = \frac{1}{(1-x)^2}$, and deduce the mean of the geometric distribution: $\sum_{k=1}^{\infty}k(1-p)^{k-1}p = \frac1p$.
20. (Riemann's warning, hands-on.) Prove that the positive terms of $\sum\frac{(-1)^{k+1}}{k}$ alone form a divergent series, and use that to argue informally that its terms can be rearranged to converge to *any* prescribed real number.

### Cumulative Review

21. *(Ch. 7)* The integral test compares $\sum_{k=1}^\infty \frac{1}{k^2}$ with $\int_1^\infty x^{-2}dx$. Evaluate the integral, and explain which of the two the picture shows is larger.
22. *(Ch. 11)* Approximate $\sum_{k=1}^{\infty}\frac1{k^2}$ by summing 100 terms and then *correcting with an integral*: show the tail satisfies $\int_{101}^\infty x^{-2}dx < \sum_{k=101}^\infty k^{-2} < \int_{100}^\infty x^{-2}dx$, and use the midpoint of those bounds to gain three extra digits over the raw partial sum.

## 12.8 Summary

Sigma notation with its linearity rules, the closed forms for $\sum k$ and $\sum k^2$, and sequences with their limits (governed by the growth hierarchy $\ln \ll$ powers $\ll$ exponentials $\ll$ factorials) set the stage for the central definition: an infinite series is the limit of its partial sums, no more and no less. The geometric series converges to $\frac{a}{1-r}$ exactly when $|r|<1$; the harmonic series diverges despite vanishing terms, growing like $\ln n$ — together they calibrate all intuition. Tools: the divergence test (one-directional), the integral test and the $p$-series dichotomy ($p>1$ converges), comparison against known scales, the ratio test ($\rho<1$ converges, tailor-made for factorials and powers), and alternating-series convergence with its first-omitted-term error bound, plus the absolute-versus-conditional distinction that licenses (or forbids) rearrangement. Numerically, `cumsum` animates partial sums, but slow divergence and slow convergence alike counsel humility: analysis decides, computation illustrates, and *rate* of convergence is the practical currency. Next: put an $x$ in the terms, and series become functions.

*Parallel reading:* OpenStax *Calculus Volume 2*, Sections 5.1–5.6 {cite}`openstax_calc2`.
