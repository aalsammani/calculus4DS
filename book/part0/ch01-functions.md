# Chapter 1 · Functions and Their Graphs

Calculus is the mathematics of change, but before we can ask *how a quantity changes*, we need a precise way to describe *how one quantity depends on another*. That is what a function is. This chapter rebuilds the idea of a function carefully, because every derivative, integral, and gradient in this book is a statement about functions, and small confusions here compound later.

## 1.1 Why functions

Consider three questions a data scientist meets weekly. How does a server's response time depend on its load? How does a model's prediction error depend on a tuning parameter? How does revenue depend on price? Each asks for a *rule* connecting an input to an output. The mathematical object that captures such a rule, stripped of any particular application, is the function.

The word "rule" is doing careful work. A function is not a formula; formulas are merely one way to specify functions. A function can be given by a table of measurements, a graph, an algorithm, or a sentence, so long as the rule is unambiguous: one input, one output.

```{prf:definition} Function, domain, range
:label: def-function
A **function** $f$ from a set $A$ to a set $B$, written $f : A \to B$, is a rule that assigns to each element $x \in A$ exactly one element $f(x) \in B$.

The set $A$ of allowed inputs is the **domain** of $f$. The set of outputs actually produced, $\{\, f(x) : x \in A \,\}$, is the **range** of $f$.
```

The phrase *exactly one* is the entire content of the definition. A rule that sometimes gives two outputs for one input (for instance, "$y$ is a number whose square is $x$", which gives both $2$ and $-2$ when $x = 4$) is not a function. A rule that gives no output for some input in its claimed domain is not a function on that domain either.

In this book the domain and range are subsets of the real numbers $\mathbb{R}$ unless stated otherwise. When a function is given only by a formula, its domain is understood to be the **natural domain**: every real input for which the formula produces a real number.

```{prf:example} Finding natural domains
:label: ex-natural-domain
Find the natural domain of each function.

**(a)** $f(x) = \dfrac{1}{x - 3}$. Division is defined except when the denominator is zero, so the domain is every real number except $3$: $\{x \in \mathbb{R} : x \neq 3\}$.

**(b)** $g(x) = \sqrt{5 - x}$. A real square root requires a nonnegative radicand: $5 - x \ge 0$, so $x \le 5$. The domain is the interval $(-\infty, 5]$.

**(c)** $h(x) = \dfrac{\sqrt{x}}{x - 2}$. Both constraints apply at once: $x \ge 0$ from the square root and $x \neq 2$ from the denominator. The domain is $[0, 2) \cup (2, \infty)$.
```

## 1.2 Function notation, evaluation, and the difference quotient

The notation $f(x)$ reads "$f$ of $x$" and means *the output of $f$ at the input $x$*. It does **not** mean $f$ times $x$. The input slot accepts anything that names a number: $f(2)$, $f(-a)$, $f(x + h)$, even $f(f(x))$.

Evaluation at a compound expression is a purely mechanical substitution, but it is the single most common source of algebra errors in a calculus course, so we practice it deliberately.

```{prf:example} Evaluating at expressions
:label: ex-evaluation
Let $f(x) = x^2 - 4x + 1$. Compute $f(3)$, $f(-2)$, $f(a + 1)$, and $f(x + h)$.

Substituting the entire input into *every* occurrence of $x$:

$$
\begin{aligned}
f(3) &= 3^2 - 4(3) + 1 = 9 - 12 + 1 = -2,\\[2pt]
f(-2) &= (-2)^2 - 4(-2) + 1 = 4 + 8 + 1 = 13,\\[2pt]
f(a+1) &= (a+1)^2 - 4(a+1) + 1 = a^2 + 2a + 1 - 4a - 4 + 1 = a^2 - 2a - 2,\\[2pt]
f(x+h) &= (x+h)^2 - 4(x+h) + 1 = x^2 + 2xh + h^2 - 4x - 4h + 1.
\end{aligned}
$$

Note the parentheses around $-2$ and around $x + h$: the input is substituted as a *unit*.
```

The last computation is not idle practice. The expression

$$
\frac{f(x+h) - f(x)}{h},
$$

called the **difference quotient**, measures the average rate of change of $f$ between $x$ and $x + h$, and Chapter 3 will define the derivative as its limiting value as $h$ shrinks to $0$. Being able to form and simplify difference quotients cleanly *is* the algebraic prerequisite for differential calculus.

```{prf:example} Simplifying a difference quotient
:label: ex-diff-quotient
For $f(x) = x^2 - 4x + 1$, simplify $\dfrac{f(x+h) - f(x)}{h}$ for $h \neq 0$.

Using $f(x+h)$ from {prf:ref}`ex-evaluation`:

$$
\begin{aligned}
\frac{f(x+h) - f(x)}{h}
&= \frac{\bigl(x^2 + 2xh + h^2 - 4x - 4h + 1\bigr) - \bigl(x^2 - 4x + 1\bigr)}{h}\\[4pt]
&= \frac{2xh + h^2 - 4h}{h}
 = \frac{h\,(2x + h - 4)}{h}
 = 2x + h - 4.
\end{aligned}
$$

Every term without an $h$ cancels — it always does, and if it doesn't, an algebra error has occurred. Keep this result in mind: when $h \to 0$ in Chapter 3, it will become the derivative $2x - 4$.
```

## 1.3 Graphs

The **graph** of $f$ is the set of all points $(x, f(x))$ in the plane as $x$ runs over the domain. The graph converts the rule into a picture: domain is the shadow of the curve on the horizontal axis, range is its shadow on the vertical axis, and the defining "exactly one output" condition becomes geometric.

```{figure} figures/ch01-function-machine.png
:name: fig-function-machine
:alt: Graph of the parabola f(x) = x squared minus 2x plus 2, with dashed lines tracing the input x equals 3 up to the curve and across to the output f of 3 equals 5.

Reading a graph: the input $x = 3$ is traced vertically to the curve and horizontally to the output $f(3) = 5$. Every question about a function's values can be answered this way from its graph.
```

Because each input has exactly one output, no vertical line can cross the graph of a function more than once. This **vertical line test** instantly classifies curves: a parabola opening upward is a function's graph; a full circle is not (a vertical line through its interior crosses it twice).

Four families of functions supply most of this book's examples, and you should know their shapes on sight.

```{figure} figures/ch01-family-gallery.png
:name: fig-family-gallery
:alt: Four panels showing a straight line for 2x minus 1, an upward parabola for x squared, the square root curve rising and bending rightward, and the reciprocal curve 1 over x decreasing toward zero.

Four basic families. Linear functions $mx+b$ change at a constant rate $m$. Even-power functions like $x^2$ are symmetric about the vertical axis. $\sqrt{x}$ grows but ever more slowly. $1/x$ is undefined at $0$ and approaches $0$ as $x$ grows.
```

Beyond these, **polynomials** $p(x) = a_n x^n + \cdots + a_1 x + a_0$ (defined for all real $x$), **rational functions** (ratios of polynomials, defined wherever the denominator is nonzero), and **piecewise functions** (different formulas on different pieces of the domain) will appear throughout. A piecewise example worth memorizing is the absolute value,

$$
|x| = \begin{cases} x, & x \ge 0,\\ -x, & x < 0, \end{cases}
$$

whose V-shaped graph has a corner at the origin — a feature that will matter when we ask where derivatives exist.

### Transformations

New graphs come from old ones by shifting, scaling, and reflecting. If the graph of $f$ is known, then:

| New function | Effect on the graph of $f$ |
|---|---|
| $f(x) + c$ | shift **up** by $c$ (down if $c<0$) |
| $f(x - c)$ | shift **right** by $c$ (left if $c<0$) |
| $c\,f(x)$, $c > 1$ | stretch vertically by factor $c$ |
| $-f(x)$ | reflect across the $x$-axis |
| $f(-x)$ | reflect across the $y$-axis |

The horizontal shift trips everyone at least once: $f(x - 1)$ moves the graph *right*, not left, because the input $x = 1$ now plays the role $0$ used to play.

```{figure} figures/ch01-transformations.png
:name: fig-transformations
:alt: Left panel shows the parabola x squared together with its right-shift (x minus 1) squared and its upward shift x squared plus 2. Right panel shows the same parabola with a vertical stretch 2 x squared and a reflection negative x squared.

Transformations of $y = x^2$. Left: $(x-1)^2$ shifts right by 1 and $x^2 + 2$ shifts up by 2. Right: $2x^2$ stretches vertically and $-x^2$ reflects across the $x$-axis. Notice which operations act on the input (horizontal effects) and which on the output (vertical effects).
```

## 1.4 Composition and inverse functions

Real computations chain functions together: standardize the data, then square, then sum. Mathematics calls chaining **composition**.

```{prf:definition} Composition
:label: def-composition
Given functions $f$ and $g$, the **composition** $f \circ g$ is the function defined by

$$(f \circ g)(x) = f\bigl(g(x)\bigr),$$

whose domain consists of every $x$ in the domain of $g$ for which $g(x)$ lies in the domain of $f$. The inner function $g$ acts first.
```

Order matters. With $f(x) = x^2$ and $g(x) = x + 1$,

$$
(f \circ g)(x) = f(x+1) = (x+1)^2, \qquad (g \circ f)(x) = g(x^2) = x^2 + 1,
$$

and these differ at almost every $x$ (try $x = 1$: the first gives $4$, the second $2$). Just as important as *composing* is *decomposing*: seeing $h(x) = \sqrt{3x + 1}$ as "the square root of $(3x+1)$", an outer function $\sqrt{\;\cdot\;}$ wrapped around an inner function $3x + 1$. The chain rule of Chapter 5 — arguably the most-used rule in applied mathematics — is exactly a rule for differentiating compositions, and applying it begins with this decomposition skill.

An **inverse function** undoes a function: if $f$ sends $a$ to $b$, then $f^{-1}$ sends $b$ back to $a$, so that

$$
f^{-1}\bigl(f(x)\bigr) = x \quad\text{and}\quad f\bigl(f^{-1}(y)\bigr) = y.
$$

Not every function has an inverse. If two different inputs share an output ($f(2) = f(-2) = 4$ for $f(x) = x^2$ on all of $\mathbb{R}$), then no rule can send that output back to "the" input. A function is invertible precisely when it is **one-to-one**: distinct inputs always give distinct outputs (graphically, every *horizontal* line crosses the graph at most once). We often restore invertibility by restricting the domain — $x^2$ on $[0, \infty)$ is one-to-one, and its inverse is $\sqrt{x}$.

To find an inverse formula, write $y = f(x)$, solve for $x$ in terms of $y$, then swap the letters. For $f(x) = 3x - 5$: from $y = 3x - 5$ we get $x = (y+5)/3$, so $f^{-1}(x) = (x + 5)/3$.

```{figure} figures/ch01-inverse-reflection.png
:name: fig-inverse-reflection
:alt: The curves y equals x squared for nonnegative x and y equals square root of x, shown as mirror images across the dashed line y equals x.

A function and its inverse are reflections of one another across the line $y = x$, because inverting swaps the roles of input and output — that is, swaps the two coordinate axes.
```

```{admonition} Common Mistakes
:class: warning
**$f^{-1}(x)$ is not $\dfrac{1}{f(x)}$.** The superscript $-1$ on a function name means *inverse function*, never reciprocal. For $f(x) = 3x - 5$, the inverse is $(x+5)/3$, while the reciprocal is $1/(3x-5)$ — completely different objects.

**$f(x+h) \neq f(x) + f(h)$ in general.** Check with $f(x) = x^2$: $f(1+1) = 4$ but $f(1) + f(1) = 2$. Substitution means replacing $x$ by the whole input, then expanding honestly.

**$f(x-c)$ shifts right, not left.** Horizontal transformations act "backwards" because they modify the input before the function sees it.

**Losing domain restrictions.** Simplifying $\frac{x^2 - 1}{x - 1}$ to $x + 1$ is valid only for $x \neq 1$; the original function is undefined there, and the restriction travels with the simplified formula.
```

## 1.5 Now do it in Python

In Python, a mathematical function becomes — fittingly — a function definition, and its graph becomes a plot built from many sampled points. The code below reproduces our running example and *verifies the hand computations* of {prf:ref}`ex-evaluation` and {prf:ref}`ex-diff-quotient`.

```python
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """f(x) = x^2 - 4x + 1, accepting a number or a NumPy array."""
    return x**2 - 4*x + 1

# --- Verify the hand evaluations from Example 1.2 ---
print(f(3))     # expect -2
print(f(-2))    # expect 13

# --- Verify the simplified difference quotient from Example 1.3 ---
# By hand we found (f(x+h) - f(x))/h = 2x + h - 4. Test at x = 5, h = 0.1:
x, h = 5.0, 0.1
print((f(x + h) - f(x)) / h)   # direct computation
print(2*x + h - 4)             # hand-simplified formula: must match
```

Running this prints `-2`, `13`, and then `6.1` twice — the direct difference quotient and the hand-simplified formula agree exactly, which is the point: the algebra was correct.

SymPy can carry out the *symbolic* algebra itself, which is a useful independent check on longer simplifications:

```python
import sympy as sp

x, h = sp.symbols('x h')
f_expr = x**2 - 4*x + 1
dq = (f_expr.subs(x, x + h) - f_expr) / h
print(sp.simplify(dq))   # expect 2*x + h - 4
```

Finally, plotting: sample the domain densely with `np.linspace`, evaluate, and draw.

```python
xs = np.linspace(-1, 5, 200)          # 200 sample points on [-1, 5]
plt.plot(xs, f(xs), label=r"$f(x) = x^2 - 4x + 1$")
plt.axhline(0, color="k", lw=0.6)
plt.xlabel("x"); plt.ylabel("f(x)")
plt.legend(); plt.show()
```

**Interpretation.** The plot shows a parabola with vertex near $x = 2$ — and completing the square, $f(x) = (x-2)^2 - 3$, confirms the vertex is exactly $(2, -3)$. The difference quotient $2x + h - 4$ is negative for $x$ well left of 2 and positive well right of 2, matching the picture: the function falls, bottoms out, then rises. Numbers, symbols, and picture tell one consistent story; when they don't, something is wrong, and finding what is how you learn.

```{admonition} Data Science Connection
:class: tip
Every predictive model is a function: inputs (features) go in, a prediction comes out. A trained regression model is literally a formula $f(x) = w_1 x_1 + \cdots + w_n x_n + b$; a neural network is a large *composition* of simple functions. The vocabulary of this chapter — domain (what inputs are valid), range (what outputs are possible), composition (chained processing), inverse (recovering input from output) — is the working vocabulary of model-building.
```

```{admonition} Looking Ahead
:class: seealso
The difference quotient of §1.2 becomes the **derivative** in Chapter 3. Decomposing functions (§1.4) becomes the **chain rule** in Chapter 5. Inverse functions return when we differentiate $\ln x$ (Chapter 5) and when we change variables in integrals (Chapter 8).
```

## 1.6 Exercises

### Quick Check

1. Can a function assign the output $7$ to both inputs $2$ and $5$? Can it assign both outputs $2$ and $5$ to the input $7$?
2. What is the natural domain of $f(x) = \sqrt{x - 4}$?
3. True or false: the graph of $f(x - 3)$ is the graph of $f$ shifted left by 3.
4. If $f(x) = 2x + 1$, what is $f(f(0))$?

````{admonition} Answers to Quick Checks
:class: dropdown
1. Yes to the first (two inputs may share an output); no to the second (one input, one output — that is the definition).
2. $[4, \infty)$, since we need $x - 4 \ge 0$.
3. False — it shifts *right* by 3.
4. $f(0) = 1$, then $f(1) = 3$.
````

### Basic Practice

5. For $g(x) = 3x^2 - x$, compute $g(0)$, $g(-1)$, $g(2a)$, and $g(x+h)$.
6. Find the natural domain of each function: (a) $\dfrac{x}{x^2 - 9}$;  (b) $\sqrt{2x + 6}$;  (c) $\dfrac{1}{\sqrt{x - 1}}$.
7. Let $f(x) = x^2 + 1$ and $g(x) = \sqrt{x}$. Find formulas and domains for $(f \circ g)(x)$ and $(g \circ f)(x)$.
8. Find the inverse of $f(x) = \dfrac{x - 2}{5}$ and verify that $f^{-1}(f(x)) = x$.

````{admonition} Solution to Exercise 6
:class: dropdown
**(a)** The denominator factors as $(x-3)(x+3)$ and must be nonzero, so the domain is all reals except $\pm 3$: $\{x : x \neq 3,\ x \neq -3\}$.

**(b)** Require $2x + 6 \ge 0$, i.e. $x \ge -3$: domain $[-3, \infty)$.

**(c)** The radicand must be nonnegative *and* the denominator nonzero, so $x - 1 > 0$ strictly: domain $(1, \infty)$. Note how the strict inequality arises from combining the two constraints.
````

````{admonition} Solution to Exercise 8
:class: dropdown
Set $y = \dfrac{x-2}{5}$ and solve for $x$: $5y = x - 2$, so $x = 5y + 2$. Swapping letters, $f^{-1}(x) = 5x + 2$. Verification:

$$
f^{-1}(f(x)) = 5\cdot\frac{x-2}{5} + 2 = (x - 2) + 2 = x. \checkmark
$$
````

### Intermediate Practice

9. Simplify the difference quotient $\dfrac{f(x+h)-f(x)}{h}$ completely (the $h$ in the denominator must cancel) for: (a) $f(x) = 3x^2 + 2x$;  (b) $f(x) = \dfrac{1}{x}$;  (c) $f(x) = \sqrt{x}$ *(hint: multiply by the conjugate)*.
10. Write $h(x) = (2x^3 - 7)^5$ as a composition $f \circ g$ of two simpler functions, in two different ways.
11. The function $f(x) = x^2 - 6x + 5$ is not one-to-one on $\mathbb{R}$. Find the largest interval of the form $[c, \infty)$ on which it *is* one-to-one, and find the inverse on that interval.

````{admonition} Hint for Exercise 9(b)
:class: dropdown
Combine $\frac{1}{x+h} - \frac{1}{x}$ over the common denominator $x(x+h)$ before dividing by $h$.
````

````{admonition} Solution to Exercise 9(b)
:class: dropdown
$$
\frac{1}{h}\left(\frac{1}{x+h} - \frac{1}{x}\right)
= \frac{1}{h}\cdot\frac{x - (x+h)}{x(x+h)}
= \frac{1}{h}\cdot\frac{-h}{x(x+h)}
= \frac{-1}{x(x+h)}.
$$

As a preview of Chapter 3: letting $h \to 0$ gives $-1/x^2$, which will be the derivative of $1/x$.
````

### Conceptual Understanding

12. Explain, using the definition of a function, why the vertical line test works.
13. Your colleague claims that because $(f\circ g)(x)$ and $(g \circ f)(x)$ are both "just $f$ and $g$ combined," they must be equal. Refute the claim with a concrete example and one sentence of explanation.
14. A dataset records daily temperature at noon for one year. Explain in what sense this table *is* a function, and identify its domain and a reasonable codomain.

### Python Practice

15. Define `f(x) = x**3 - 2*x` in Python and verify numerically, at three different points, that your hand-simplified difference quotient from the pattern of Exercise 9 is correct for $h = 0.01$.
16. Use SymPy's `simplify` to check your answers to Exercise 9(a) and 9(c).

### Visualization Practice

17. Plot $f(x) = |x - 2| + 1$ on $[-2, 6]$. Identify the corner point from the plot and explain algebraically why it occurs there.
18. On one set of axes, plot $\sqrt{x}$, $\sqrt{x - 2}$, and $\sqrt{x} - 2$ on suitable domains, with a legend. Write one sentence explaining how the three graphs are related.

### Challenge

19. Suppose $f$ is one-to-one and $g(x) = f(x - 3) + 4$. Express $g^{-1}$ in terms of $f^{-1}$, and verify your formula on the concrete case $f(x) = x^3$.
20. Show that $f(x) = \dfrac{x}{1 + |x|}$ is one-to-one on all of $\mathbb{R}$, find its range, and find a formula for $f^{-1}$ on that range.

## 1.7 Summary

A function is a rule assigning exactly one output to each input; its domain is the set of legal inputs, its range the set of realized outputs. Function notation is substitution of the *entire* input, and mastery of the difference quotient $\frac{f(x+h)-f(x)}{h}$ is the direct on-ramp to derivatives. Graphs turn rules into curves (vertical line test), and standard transformations — shifts, stretches, reflections — generate families of graphs from a few memorized shapes. Composition chains functions with order mattering; inverses undo one-to-one functions and mirror their graphs across $y = x$. In Python, functions become `def` and graphs become `plt.plot` over `np.linspace` samples, with NumPy verifying values and SymPy verifying algebra.

*Parallel reading:* OpenStax *Calculus Volume 1*, Chapter 1 (Functions and Graphs) {cite}`openstax_calc1`.
