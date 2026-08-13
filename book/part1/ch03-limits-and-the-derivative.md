# Chapter 3 · Limits and the Derivative

This chapter answers the founding question of differential calculus: *what is the instantaneous rate of change of a function?* Average rates over an interval are elementary — the difference quotient of Chapter 1 computes them. The difficulty is that "instantaneous" seems to demand a rate over an interval of length zero, which would be the meaningless expression $0/0$. The resolution is the idea of a **limit**, and we develop exactly as much limit theory as the derivative requires: enough to be correct, no more.

## 3.1 Motivation: from average to instantaneous

A vehicle's position along a road is $s(t) = t^2$ meters after $t$ seconds. Its **average velocity** between times $1$ and $1 + h$ is distance over elapsed time:

$$
\frac{s(1+h) - s(1)}{h} = \frac{(1+h)^2 - 1}{h} = \frac{2h + h^2}{h} = 2 + h \quad (h \neq 0).
$$

Over the second from $t=1$ to $t=2$ ($h = 1$) the average velocity is $3$ m/s; over a tenth of a second, $2.1$ m/s; over a thousandth, $2.001$ m/s. The averages are closing in on the value $2$, and no measurement over any positive interval will ever equal it — yet $2$ m/s is plainly the right answer to "how fast at the instant $t = 1$?" The speedometer reads what the averages *approach*. Making "approach" precise is the job of the limit.

## 3.2 Limits, just enough

```{prf:definition} Limit (working definition)
:label: def-limit
To say

$$\lim_{x \to a} f(x) = L$$

means: the values $f(x)$ can be made as close to $L$ as desired by taking $x$ sufficiently close to $a$ (on either side), without requiring $x = a$. The value $f(a)$ itself — even whether it exists — is irrelevant to the limit.
```

This is the informal version of the rigorous $\varepsilon$–$\delta$ definition found in analysis courses; for this book's purposes the working definition, used carefully, is sufficient. Three points deserve emphasis. First, the limit is about the *approach*, never the arrival: in §3.1 the quantity $2 + h$ is undefined at $h = 0$, yet its limit as $h \to 0$ is plainly $2$. Second, the approach must give the same answer from both sides; when the one-sided limits $\lim_{x \to a^-}$ (from the left) and $\lim_{x \to a^+}$ (from the right) disagree, the two-sided limit does not exist. Third, most limits in practice require no subtlety at all: for the well-behaved (**continuous**) functions that make up most of this book — polynomials, rational functions on their domains, roots, exponentials, logarithms, sines and cosines — the limit is found by substitution, $\lim_{x\to a} f(x) = f(a)$.

The interesting cases are exactly the ones substitution cannot handle: the **indeterminate form** $\frac{0}{0}$, where numerator and denominator both vanish. Every derivative computation is such a case, and the standard remedy is algebra first, limit second: cancel the offending factor, then substitute.

```{prf:example} A $0/0$ limit by factoring
:label: ex-limit-factor
Evaluate $\displaystyle \lim_{x \to 3} \frac{x^2 - 9}{x - 3}$.

Substituting $x = 3$ gives $0/0$: indeterminate. Factor and cancel (legitimate since $x \neq 3$ during the approach):

$$
\lim_{x \to 3} \frac{(x-3)(x+3)}{x - 3} = \lim_{x\to 3}\,(x + 3) = 6.
$$

The graph of the original function is the line $y = x + 3$ with a hole at $(3, 6)$; the limit "fills the hole."
```

```{prf:example} A limit that does not exist
:label: ex-limit-dne
Evaluate $\displaystyle \lim_{x \to 0} \frac{|x|}{x}$.

For $x > 0$ the function equals $1$; for $x < 0$ it equals $-1$. The right-hand limit is $1$, the left-hand limit is $-1$; since they disagree, the two-sided limit **does not exist**. One-sided disagreement is the most common way limits fail.
```

One famous limit cannot be found by algebra and will be *needed* to differentiate sine in Chapter 5, so we record it now with numerical evidence:

$$
\lim_{x \to 0} \frac{\sin x}{x} = 1 \qquad (x \text{ in radians}).
$$

| $x$ | $0.5$ | $0.1$ | $0.01$ | $0.001$ |
|---|---|---|---|---|
| $\dfrac{\sin x}{x}$ | $0.9588511$ | $0.9983342$ | $0.9999833$ | $0.9999998$ |

The table (computed in §3.6) and the figure both point unmistakably to $1$; a geometric proof compares the areas of a triangle, circular sector, and larger triangle and can be found in OpenStax *Calculus Volume 1*, §2.3 {cite}`openstax_calc1`. The result is one reason radians are mandatory: in degrees, this limit is $\pi/180$, and every derivative formula would carry that factor forever.

```{figure} figures/ch03-sinx-over-x.png
:name: fig-sinx-over-x
:alt: The graph of sine x over x, a wave-damped curve with a small open circle at the point zero comma one indicating the function is undefined there while the curve approaches height one from both sides.

The function $\frac{\sin x}{x}$ is undefined at $x=0$ (open circle), yet approaches $1$ from both sides. This is the essence of a limit: behavior *near* a point, independent of behavior *at* it.
```

## 3.3 The derivative

```{prf:definition} Derivative
:label: def-derivative
The **derivative** of $f$ at $x$ is

$$
f'(x) \;=\; \lim_{h \to 0} \frac{f(x+h) - f(x)}{h},
$$

provided the limit exists, in which case $f$ is **differentiable** at $x$. Equivalent notations: $f'(x) = \dfrac{df}{dx} = \dfrac{d}{dx}f(x)$.
```

The definition packages the whole story so far: the fraction is the average rate of change over $[x, x+h]$ (a secant slope), and the limit extracts the instantaneous rate (the tangent slope). The derivative of $f$ is itself a new *function*, whose value at each point is the slope of $f$'s graph there.

```{figure} figures/ch03-secants-to-tangent.png
:name: fig-secants
:alt: The parabola x squared with three secant lines through the point one comma one drawn for shrinking values of h, visibly rotating toward a limiting red tangent line of slope two.

Secant lines through $(1,1)$ on $y = x^2$ for $h = 1.5, 1.0, 0.5$ have slopes $3.5, 3.0, 2.5$, rotating toward the tangent line of slope exactly $2$ as $h \to 0$. The derivative is the slope the secants approach.
```

```{prf:example} A derivative from the definition — polynomial
:label: ex-deriv-def-poly
Find $f'(x)$ for $f(x) = x^2 - 4x + 1$ directly from the definition.

Chapter 1 ({prf:ref}`ex-diff-quotient`) already did the algebra: for $h \neq 0$,

$$
\frac{f(x+h)-f(x)}{h} = 2x + h - 4.
$$

Now take the limit — the expression is a polynomial in $h$, so substitution works:

$$
f'(x) = \lim_{h\to 0}\,(2x + h - 4) = 2x - 4.
$$

**Interpretation.** The parabola has slope $2x - 4$: negative for $x < 2$ (falling), zero at $x = 2$ (the vertex, a flat point), positive for $x > 2$ (rising) — exactly what its graph shows.
```

```{prf:example} A derivative from the definition — reciprocal
:label: ex-deriv-def-recip
Find $g'(x)$ for $g(x) = \dfrac{1}{x}$ (for $x \neq 0$).

Form the difference quotient and combine fractions before letting $h \to 0$:

$$
\frac{g(x+h) - g(x)}{h}
= \frac{1}{h}\left(\frac{1}{x+h} - \frac{1}{x}\right)
= \frac{1}{h}\cdot\frac{x - (x + h)}{x(x+h)}
= \frac{-h}{h\,x(x+h)}
= \frac{-1}{x(x+h)}.
$$

Therefore

$$
g'(x) = \lim_{h \to 0} \frac{-1}{x(x+h)} = -\frac{1}{x^2}.
$$

**Interpretation.** The slope is negative everywhere ($1/x$ always falls, on each branch) and steepest near $x = 0$, flattening as $|x|$ grows — matching the graph in {numref}`fig-family-gallery`.
```

```{prf:example} A derivative from the definition — square root
:label: ex-deriv-def-sqrt
Find $f'(x)$ for $f(x) = \sqrt{x}$ at points $x > 0$.

The difference quotient $\frac{\sqrt{x+h} - \sqrt{x}}{h}$ is $0/0$-bound; multiply by the conjugate to release it:

$$
\frac{\sqrt{x+h}-\sqrt{x}}{h}\cdot\frac{\sqrt{x+h}+\sqrt{x}}{\sqrt{x+h}+\sqrt{x}}
= \frac{(x + h) - x}{h\left(\sqrt{x+h}+\sqrt{x}\right)}
= \frac{1}{\sqrt{x+h}+\sqrt{x}},
$$

so

$$
f'(x) = \lim_{h\to 0}\frac{1}{\sqrt{x+h}+\sqrt{x}} = \frac{1}{2\sqrt{x}}.
$$

**Interpretation.** As $x$ grows, $\frac{1}{2\sqrt x}$ shrinks: the square-root curve keeps rising but ever more gently. Near $x = 0^+$ the slope blows up — the graph leaves the origin vertically.
```

### Reading a function through its derivative

Because $f'(x)$ is the slope of $f$ at $x$, the sign of $f'$ narrates the behavior of $f$: where $f' > 0$, $f$ is increasing; where $f' < 0$, decreasing; where $f' = 0$, the graph is momentarily flat — a candidate peak, valley, or plateau. This one observation underlies all of optimization.

```{figure} figures/ch03-f-and-fprime.png
:name: fig-f-and-fprime
:alt: Two stacked panels sharing an x axis. The top shows the cubic x cubed minus 3x with a local peak at x equals negative one and a local valley at x equals one. The bottom shows its derivative 3 x squared minus 3, a parabola crossing zero exactly at plus and minus one.

$f(x) = x^3 - 3x$ (top) and $f'(x) = 3x^2 - 3$ (bottom). The derivative crosses zero at $x = \pm 1$, precisely where the original function has its local peak and valley; $f'$ is positive exactly where $f$ climbs.
```

### When differentiation fails

Differentiability can fail. At a **corner**, like $|x|$ at $0$, the one-sided secant slopes disagree ($-1$ from the left, $+1$ from the right), so the defining limit does not exist. At a **vertical tangent**, like $\sqrt[3]{x}$ at $0$, the slopes exist but grow without bound. And at any **discontinuity** — a jump or hole — differentiation fails automatically: differentiability implies continuity, never the reverse.

```{figure} figures/ch03-abs-corner.png
:name: fig-abs-corner
:alt: The V-shaped graph of absolute value of x with dashed lines of slope negative one and positive one along its two arms, illustrating that the two one-sided slopes at the corner disagree.

$|x|$ at its corner: left-secants report slope $-1$, right-secants report $+1$. No single number serves as "the" slope, so $f'(0)$ does not exist. Corners matter in practice — the ReLU activation $\max(0, x)$ ubiquitous in neural networks has exactly this corner.
```

## 3.4 Do it by hand: a complete workflow

Before any shortcut rules exist (they arrive in Chapter 4), here is the full manual procedure on a fresh problem. Find the equation of the tangent line to $f(x) = x^2 - 4x + 1$ at $x = 3$.

**Step 1 — the slope.** From {prf:ref}`ex-deriv-def-poly`, $f'(x) = 2x - 4$, so the tangent slope at $x=3$ is $f'(3) = 2$.

**Step 2 — the point.** $f(3) = 9 - 12 + 1 = -2$, so the line passes through $(3, -2)$.

**Step 3 — point-slope form.**

$$
y - (-2) = 2(x - 3) \quad\Longrightarrow\quad y = 2x - 8.
$$

A sanity check that costs ten seconds and catches most errors: the tangent must touch the curve at the point of tangency. At $x = 3$: line gives $2(3) - 8 = -2 = f(3)$. ✓

## 3.5 Common mistakes

```{admonition} Common Mistakes
:class: warning
**Setting $h = 0$ too early.** The difference quotient is undefined at $h = 0$; the entire method is to simplify *first* (cancel the $h$) and take the limit *last*. If your simplified quotient still has $h$ downstairs, the algebra is unfinished or wrong.

**Confusing $f'(a)$ with $f(a)$.** One is the slope at $a$, the other the height at $a$. Both are needed for a tangent line, and they answer different questions.

**"The limit doesn't exist because the function is undefined there."** Irrelevant — see {numref}`fig-sinx-over-x`. Limits ignore the point itself.

**Treating the derivative as a fraction of two numbers.** The Leibniz symbol $\frac{df}{dx}$ is a single indivisible notation for a limit, not a ratio $df \div dx$ (although its fraction-like behavior in Chapters 5 and 8 is a deliberate, and provable, design feature of the notation).

**Assuming continuity implies differentiability.** $|x|$ is continuous everywhere yet not differentiable at $0$. The implication runs only the other way.
```

## 3.6 Now do it in Python

Numerically, a derivative can be *estimated* by a difference quotient with small $h$ — exactly the definition, stopped short of the limit. The code verifies our three hand-computed derivatives.

```python
import numpy as np

def numerical_derivative(f, x, h=1e-6):
    """Central difference estimate of f'(x).

    (f(x+h) - f(x-h)) / (2h) straddles x symmetrically and is far more
    accurate than the one-sided quotient for the same h.
    """
    return (f(x + h) - f(x - h)) / (2 * h)

# --- Verify Example 3.3: d/dx [x^2 - 4x + 1] = 2x - 4 ---
f = lambda x: x**2 - 4*x + 1
for x0 in [0.0, 1.0, 3.0]:
    print(numerical_derivative(f, x0), 2*x0 - 4)   # pairs should match

# --- Verify Example 3.4: d/dx [1/x] = -1/x^2, at x = 2 ---
print(numerical_derivative(lambda x: 1/x, 2.0), -1/4)

# --- Verify Example 3.5: d/dx [sqrt(x)] = 1/(2 sqrt x), at x = 9 ---
print(numerical_derivative(np.sqrt, 9.0), 1/6)

# --- The sin(x)/x table from Section 3.2 ---
for x in [0.5, 0.1, 0.01, 0.001]:
    print(f"sin({x})/{x} = {np.sin(x)/x:.7f}")
```

Each printed pair agrees to many decimal places, confirming the hand algebra. SymPy computes the limit and the derivative *exactly*, which makes it an independent referee:

```python
import sympy as sp

x, h = sp.symbols('x h')

print(sp.limit(sp.sin(x)/x, x, 0))                    # expect 1
print(sp.limit(((x + h)**2 - 4*(x + h) + 1
                - (x**2 - 4*x + 1))/h, h, 0))         # expect 2*x - 4
print(sp.diff(1/x, x), sp.diff(sp.sqrt(x), x))        # -1/x**2, 1/(2*sqrt(x))
```

**Interpretation.** Three independent instruments — hand algebra, floating-point difference quotients, and exact symbolic computation — return the same answers. This triangulation is the working method of the whole book: when the three disagree, one of them (usually the hand algebra, occasionally the numerics via a poor choice of $h$) contains an error worth finding.

```{admonition} Data Science Connection
:class: tip
The derivative is the mathematics of **sensitivity**: $f'(x)$ tells you how much the output moves per unit nudge of the input. "How much does predicted revenue change per dollar of price?" and "how much does the loss change per unit change in this model weight?" are both derivative questions, and the second one — evaluated for millions of weights at once — is what *training* a model means. The gradient of Part V is this chapter's derivative grown to many variables.
```

```{admonition} Looking Ahead
:class: seealso
Computing every derivative from the limit definition would be unbearable. Chapter 4 harvests the definition once and for all into a small set of **rules** that reduce differentiation to mechanical algebra. The limit definition remains the meaning; the rules become the method.
```

## 3.7 Exercises

### Quick Check

1. Evaluate $\displaystyle\lim_{x \to 2}\,(x^3 - 5x)$ and say why substitution is justified.
2. If $f'(4) = -3$, is $f$ increasing or decreasing near $x = 4$? Roughly how much does $f$ change if $x$ moves from $4$ to $4.01$?
3. True or false: if $f$ is continuous at $a$, then $f'(a)$ exists.
4. What is $\displaystyle\lim_{h \to 0}\frac{(2+h)^2 - 4}{h}$, and what derivative does this limit compute?

````{admonition} Answers to Quick Checks
:class: dropdown
1. $8 - 10 = -2$; polynomials are continuous, so limits are found by substitution.
2. Decreasing; $\Delta f \approx f'(4)\,\Delta x = (-3)(0.01) = -0.03$.
3. False ($|x|$ at $0$).
4. Expanding: $\frac{4h + h^2}{h} = 4 + h \to 4$. It is $f'(2)$ for $f(x) = x^2$.
````

### Basic Practice

5. Evaluate each limit or state that it does not exist:
   (a) $\displaystyle\lim_{x\to 5}\frac{x^2 - 25}{x - 5}$;  (b) $\displaystyle\lim_{x\to 1}\frac{x^2 + 2x - 3}{x - 1}$;  (c) $\displaystyle\lim_{x\to 0}\frac{x}{|x|}$;  (d) $\displaystyle\lim_{h\to 0}\frac{\sqrt{9+h} - 3}{h}$.
6. Using the definition of the derivative, find $f'(x)$ for: (a) $f(x) = 5x - 7$;  (b) $f(x) = x^2 + 3x$;  (c) $f(x) = x^3$. *(For (c): $(x+h)^3 = x^3 + 3x^2h + 3xh^2 + h^3$.)*
7. Find the equation of the tangent line to $f(x) = x^2 + 3x$ at $x = -1$, using your derivative from 6(b).

````{admonition} Solution to Exercise 5(d)
:class: dropdown
Multiply by the conjugate:

$$
\frac{\sqrt{9+h}-3}{h}\cdot\frac{\sqrt{9+h}+3}{\sqrt{9+h}+3}
= \frac{(9+h)-9}{h(\sqrt{9+h}+3)} = \frac{1}{\sqrt{9+h}+3} \xrightarrow[h \to 0]{} \frac{1}{6}.
$$

This limit is precisely $f'(9)$ for $f(x)=\sqrt{x}$, agreeing with $\frac{1}{2\sqrt 9}$ from {prf:ref}`ex-deriv-def-sqrt`.
````

````{admonition} Solution to Exercise 6(c)
:class: dropdown
$$
\frac{(x+h)^3 - x^3}{h} = \frac{3x^2 h + 3x h^2 + h^3}{h} = 3x^2 + 3xh + h^2 \xrightarrow[h\to 0]{} 3x^2.
$$

So $\dfrac{d}{dx}x^3 = 3x^2$ — one more data point for the pattern ($x^2 \mapsto 2x$, $x^3 \mapsto 3x^2$) that Chapter 4 will name the power rule.
````

### Intermediate Practice

8. Using the definition, find $f'(x)$ for $f(x) = \dfrac{1}{x + 2}$ and for $f(x) = \sqrt{2x}$.
9. For $f(x) = x^3 - 3x$ (as in {numref}`fig-f-and-fprime`), use $f'(x) = 3x^2 - 3$ to find all points where the tangent line is horizontal, and all points where the tangent slope equals $9$.
10. The function $f(x) = \begin{cases} x^2, & x \le 1 \\ 2x - 1, & x > 1\end{cases}$ is continuous at $x=1$ (both pieces give $1$). Show, by computing the one-sided limits of the difference quotient at $x = 1$, that $f$ *is* differentiable there, and explain geometrically why this piecewise function is smooth while $|x|$ is not.

### Conceptual Understanding

11. Explain the difference between $\dfrac{f(b)-f(a)}{b-a}$ and $f'(a)$, and describe a real scenario (from any field) where each is the more useful quantity.
12. Sketch (by hand) a function that is continuous everywhere, differentiable everywhere except at $x = -1$ and $x = 2$, with $f' > 0$ on $(-1, 2)$. Explain your sketch's features.
13. A colleague computes $\lim_{h\to0}\frac{f(3+h)-f(3)}{h}$ by plugging in $h = 0$ and declares the limit "undefined, $0/0$." Explain the error and the correct procedure in two or three sentences.

### Python Practice

14. Implement `forward_difference(f, x, h)` returning $\frac{f(x+h)-f(x)}{h}$. For $f(x) = \sin x$ at $x = 1$, print the error against the true derivative $\cos 1$ for $h = 10^{-1}, 10^{-2}, \dots, 10^{-12}$. You will see the error shrink and then *grow* again; write one sentence proposing why. *(Answer: floating-point cancellation — subtracting two nearly equal numbers destroys precision. Chapter 11 returns to this.)*
15. Use SymPy to verify both derivatives in Exercise 8.

### Visualization Practice

16. Plot $f(x) = x^3 - 3x$ and, at the point $x_0 = 1.5$, its secant lines for $h = 1, 0.5, 0.1$ together with its tangent line, reproducing the spirit of {numref}`fig-secants`. Label the slopes in the legend.
17. Plot $f(x) = \dfrac{x^2-9}{x-3}$ on $[0, 6]$, marking the hole at $x = 3$ with an open circle, and annotate the limiting value.

### Challenge

18. Using the definition of the derivative and the limit $\lim_{h\to 0}\frac{\sin h}{h} = 1$ together with $\lim_{h \to 0}\frac{\cos h - 1}{h} = 0$ (which you may assume), prove that $\frac{d}{dx}\sin x = \cos x$. *(Hint: expand $\sin(x+h)$ with the angle-sum identity from Chapter 2.)*
19. Give an example of a function differentiable everywhere on $\mathbb{R}$ whose derivative is *not* continuous, or explain why you believe none exists, and then look up "$x^2 \sin(1/x)$" to check yourself.

## 3.8 Summary

A limit describes the value a function approaches, independent of its value (or lack of one) at the point; substitution handles continuous functions, algebraic cancellation handles the $0/0$ forms, and $\lim_{x\to0}\frac{\sin x}{x} = 1$ in radians. The derivative $f'(x) = \lim_{h\to0}\frac{f(x+h)-f(x)}{h}$ is the instantaneous rate of change and the tangent slope; it is a function in its own right whose sign narrates where $f$ rises and falls. From the definition we established $\frac{d}{dx}x^2 = 2x$, $\frac{d}{dx}x^3=3x^2$, $\frac{d}{dx}\frac1x = -\frac{1}{x^2}$, and $\frac{d}{dx}\sqrt{x} = \frac{1}{2\sqrt x}$. Differentiability fails at corners, vertical tangents, and discontinuities, and implies continuity. Numerically the central difference $\frac{f(x+h)-f(x-h)}{2h}$ estimates derivatives; symbolically SymPy's `diff` and `limit` verify them exactly.

*Parallel reading:* OpenStax *Calculus Volume 1*, Chapter 2 (Limits) and Sections 3.1–3.2 {cite}`openstax_calc1`.
