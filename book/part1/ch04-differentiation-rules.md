# Chapter 4 · Differentiation Rules

Chapter 3 defined the derivative as a limit and computed a handful of examples by hand. Each took several lines of careful algebra. Since differentiation is something applied mathematics does constantly, computing every derivative from the definition would be like doing all arithmetic with tally marks. This chapter converts the definition, once and for all, into a small toolkit of **rules** — worked out from the limit definition so you know they are theorems rather than conventions — after which differentiating becomes fast, reliable algebra.

## 4.1 The power rule and linearity

Chapter 3 found a pattern: $\frac{d}{dx}x^2 = 2x$ and $\frac{d}{dx}x^3 = 3x^2$; the exponent drops down as a coefficient and decreases by one. This pattern holds far more generally.

```{prf:theorem} Power rule
:label: thm-power-rule
For every real constant $n$,

$$\frac{d}{dx}\,x^n = n\,x^{n-1}$$

wherever $x^n$ and $x^{n-1}$ are defined.
```

**Where it comes from (positive integers).** For a positive integer $n$, the binomial expansion gives

$$
(x+h)^n = x^n + n x^{n-1} h + \binom{n}{2}x^{n-2}h^2 + \cdots + h^n,
$$

so

$$
\frac{(x+h)^n - x^n}{h} = n x^{n-1} + \underbrace{\binom{n}{2}x^{n-2}h + \cdots + h^{n-1}}_{\text{every term carries an } h},
$$

and as $h \to 0$ all trailing terms vanish, leaving $n x^{n-1}$. The rule extends to negative and fractional exponents (Chapter 3's hand computations $\frac{d}{dx}x^{-1} = -x^{-2}$ and $\frac{d}{dx}x^{1/2} = \tfrac12 x^{-1/2}$ are exactly the power rule at $n = -1$ and $n = \tfrac12$), and to all real exponents once logarithmic differentiation is available in Chapter 5.

Two structural rules let us differentiate any *combination* of pieces we can differentiate individually. Both follow from the limit definition because limits respect sums and constant multiples.

```{prf:theorem} Linearity of the derivative
:label: thm-linearity
If $f$ and $g$ are differentiable and $c$ is a constant, then

$$
\frac{d}{dx}\bigl[c\,f(x)\bigr] = c\,f'(x),
\qquad
\frac{d}{dx}\bigl[f(x) + g(x)\bigr] = f'(x) + g'(x).
$$

Also $\frac{d}{dx}[c] = 0$: constants have zero rate of change.
```

Linearity plus the power rule dispatches every polynomial in one pass.

```{prf:example} Differentiating a polynomial
:label: ex-diff-polynomial
Differentiate $p(x) = 4x^5 - 7x^3 + \dfrac{x^2}{2} - 9x + 12$.

Term by term, each via the power rule:

$$
p'(x) = 4(5x^4) - 7(3x^2) + \tfrac12(2x) - 9 + 0 = 20x^4 - 21x^2 + x - 9.
$$
```

```{prf:example} Rewriting before differentiating
:label: ex-rewrite-first
Differentiate $f(x) = \dfrac{3}{x^4} + 5\sqrt[3]{x} - \dfrac{2}{\sqrt{x}}$.

The productive first move is to rewrite everything as a power of $x$:

$$
f(x) = 3x^{-4} + 5x^{1/3} - 2x^{-1/2},
$$

then apply the power rule to each term:

$$
f'(x) = -12x^{-5} + \tfrac{5}{3}x^{-2/3} + x^{-3/2}
      = -\frac{12}{x^5} + \frac{5}{3x^{2/3}} + \frac{1}{x^{3/2}}.
$$

Most "hard" differentiation problems in this family are rewriting problems in disguise.
```

```{figure} figures/ch04-tangent-family.png
:name: fig-tangent-family
:alt: The parabola x squared with short tangent segments drawn at four points; segments far from the origin are visibly steeper than those near it.

The power rule made visible: tangent segments to $y = x^2$ at $x = -1.5, -0.5, 0.5, 1.5$ have slopes $2x = -3, -1, 1, 3$. The formula $f'(x) = 2x$ is a compact description of this entire family of slopes.
```

## 4.2 The product rule

The derivative of a sum is the sum of derivatives — so it is tempting to guess that the derivative of a product is the product of derivatives. The guess is *false*, and one counterexample kills it: with $f(x) = g(x) = x$, the product is $x^2$ with derivative $2x$, while the product of derivatives is $1 \cdot 1 = 1$.

The correct rule can be discovered by thinking of $f$ and $g$ as the sides of a rectangle with area $A = f g$. When $x$ changes a little, each side changes a little, and the area gains two thin strips: one of size (change in $f$) $\times$ $g$, one of size $f$ $\times$ (change in $g$) — plus a tiny corner that vanishes in the limit.

```{prf:theorem} Product rule
:label: thm-product-rule
If $f$ and $g$ are differentiable, then

$$
\frac{d}{dx}\bigl[f(x)\,g(x)\bigr] = f'(x)\,g(x) + f(x)\,g'(x).
$$
```

**Derivation.** Add and subtract the mixed term $f(x+h)g(x)$ in the numerator of the difference quotient — the standard trick for separating the two changes:

$$
\begin{aligned}
\frac{f(x{+}h)g(x{+}h) - f(x)g(x)}{h}
&= \frac{f(x{+}h)g(x{+}h) - f(x{+}h)g(x) \;+\; f(x{+}h)g(x) - f(x)g(x)}{h}\\[4pt]
&= f(x{+}h)\,\frac{g(x{+}h)-g(x)}{h} \;+\; g(x)\,\frac{f(x{+}h)-f(x)}{h}.
\end{aligned}
$$

As $h \to 0$: $f(x+h) \to f(x)$ (differentiable functions are continuous), and the two quotients converge to $g'(x)$ and $f'(x)$. The result is $f g' + g f'$. $\blacksquare$

```{prf:example} Product rule, basic
:label: ex-product-basic
Differentiate $y = (x^2 + 1)(x^3 - 2x)$.

With $f = x^2+1$, $g = x^3 - 2x$, so $f' = 2x$, $g' = 3x^2 - 2$:

$$
y' = (2x)(x^3 - 2x) + (x^2+1)(3x^2 - 2) = 2x^4 - 4x^2 + 3x^4 + x^2 - 2 = 5x^4 - 3x^2 - 2.
$$

**Check** (available here because the product is expandable): $y = x^5 - x^3 - 2x$, whose derivative by the power rule is $5x^4 - 3x^2 - 2$. ✓ When both routes exist, running both is a free correctness proof.
```

## 4.3 The quotient rule

```{prf:theorem} Quotient rule
:label: thm-quotient-rule
If $f$ and $g$ are differentiable and $g(x) \neq 0$, then

$$
\frac{d}{dx}\!\left[\frac{f(x)}{g(x)}\right] = \frac{f'(x)\,g(x) - f(x)\,g'(x)}{g(x)^2}.
$$
```

A memory aid, with "hi" the numerator and "lo" the denominator: *lo d-hi minus hi d-lo, over lo-lo*. The order in the numerator matters — the minus sign makes the rule antisymmetric, unlike the product rule.

**Derivation from the product rule.** Write $q = f/g$, so $f = qg$. Differentiating both sides with the product rule: $f' = q'g + qg'$. Solve for $q'$:

$$
q' = \frac{f' - qg'}{g} = \frac{f' - \frac{f}{g}g'}{g} = \frac{f'g - fg'}{g^2}. \qquad \blacksquare
$$

```{prf:example} Quotient rule, basic
:label: ex-quotient-basic
Differentiate $y = \dfrac{x^2}{x + 3}$.

With hi $= x^2$, lo $= x + 3$:

$$
y' = \frac{(2x)(x+3) - x^2(1)}{(x+3)^2} = \frac{2x^2 + 6x - x^2}{(x+3)^2} = \frac{x^2 + 6x}{(x+3)^2} = \frac{x(x+6)}{(x+3)^2}.
$$

**Interpretation.** The derivative is zero at $x = 0$ and $x = -6$ — two horizontal tangents — and undefined at $x = -3$, where the function itself has a vertical asymptote. The derivative's formula narrates the graph.
```

```{prf:example} Choosing the easier tool
:label: ex-choose-tool
Differentiate $y = \dfrac{x^4 - 3x^2 + 5}{x^2}$.

The quotient rule works, but division first is faster and safer:

$$
y = x^2 - 3 + 5x^{-2} \quad\Longrightarrow\quad y' = 2x - 10x^{-3} = 2x - \frac{10}{x^3}.
$$

**Rule of craft:** before reaching for the product or quotient rule, spend five seconds asking whether algebra can simplify the expression into a plain sum of powers.
```

```{prf:example} An applied product: revenue and marginal revenue
:label: ex-marginal-revenue
A ride service estimates that at price $p$ dollars per ride it serves $q(p) = 1200 - 40p$ rides per day, so daily revenue is $R(p) = p\,q(p) = p(1200 - 40p)$. Find $R'(p)$, interpret it, and find where revenue stops rising.

By the product rule (or by expanding):

$$
R'(p) = (1)(1200 - 40p) + p(-40) = 1200 - 80p.
$$

**Interpretation.** $R'(p)$ is *marginal revenue*: at $p = 10$, $R'(10) = 400$, so a further \$1 price increase adds about \$400/day; at $p = 20$, $R'(20) = -400$, and raising price now *loses* about \$400/day because ridership falls faster than the price gain. Revenue peaks where $R'(p) = 0$: $p = 15$ dollars, giving $R(15) = 15 \cdot 600 = \$9000$/day. The sign of the derivative, not the formula for revenue itself, is what answers the business question.
```

## 4.4 Higher-order derivatives

Since $f'$ is a function, it can be differentiated again: $f'' = (f')'$ is the **second derivative**, and $f^{(n)}$ the $n$-th. If $f$ is position, $f'$ is velocity and $f''$ is acceleration — the rate at which the rate changes. Graphically $f''$ measures bending: where $f'' > 0$ the graph is concave up (holds water), where $f''<0$ concave down. For $p(x) = 4x^5 - 7x^3$:

$$
p' = 20x^4 - 21x^2, \qquad p'' = 80x^3 - 42x, \qquad p''' = 240x^2 - 42,
$$

and each differentiation lowers every degree by one, so $p^{(6)} = 0$ identically: a degree-5 polynomial has six nonzero derivatives at most. Second derivatives return in Chapter 6 (error of linearization) and Chapter 13 (Taylor's quadratic term).

## 4.5 Common mistakes

```{admonition} Common Mistakes
:class: warning
**$(fg)' \neq f'g'$ and $(f/g)' \neq f'/g'$.** The one-line counterexample $f = g = x$ disposes of both. When you feel the pull of these "rules," recompute the counterexample.

**Quotient-rule order.** The numerator is $f'g - fg'$, derivative-of-the-top first. Swapping the terms flips the sign of every answer.

**Differentiating through a power incorrectly:** $\frac{d}{dx}(x^2+1)^3$ is *not* $3(x^2+1)^2$ — a composition is hiding inside, and it needs the chain rule (Chapter 5). Until then, expand first if you must differentiate such a thing.

**Forgetting that $\frac{d}{dx}[\pi^2] = 0$.** Anything with no $x$ in it — $\pi^2$, $e^3$, $\ln 5$ — is a constant, and its derivative is $0$, not something obtained by the power rule.

**Not simplifying before differentiating.** {prf:ref}`ex-choose-tool` is the model: algebra first often turns a two-rule problem into a power-rule problem.
```

## 4.6 Now do it in Python

SymPy applies every rule of this chapter exactly, which makes it the ideal answer-checker for hand practice. NumPy's central differences supply an independent numerical check.

```python
import sympy as sp

x = sp.symbols('x')

# --- Verify Example 4.3 (product rule) ---
y = (x**2 + 1) * (x**3 - 2*x)
print(sp.expand(sp.diff(y, x)))          # expect 5*x**4 - 3*x**2 - 2

# --- Verify Example 4.5 (quotient rule) ---
y = x**2 / (x + 3)
print(sp.simplify(sp.diff(y, x)))        # expect x*(x + 6)/(x + 3)**2

# --- Verify Example 4.7 (marginal revenue) ---
p = sp.symbols('p')
R = p * (1200 - 40*p)
Rp = sp.diff(R, p)
print(Rp, sp.solve(Rp, p))               # expect 1200 - 80*p, [15]

# --- Higher-order derivatives (Section 4.4) ---
poly = 4*x**5 - 7*x**3
print([sp.diff(poly, x, n) for n in range(1, 7)])   # sixth entry is 0
```

A numerical cross-check of the quotient-rule result at one point:

```python
import numpy as np

f  = lambda t: t**2 / (t + 3)
fp = lambda t: t * (t + 6) / (t + 3)**2          # our hand answer

t0, h = 2.0, 1e-6
central = (f(t0 + h) - f(t0 - h)) / (2 * h)      # definition-based estimate
print(central, fp(t0))                           # 0.64 and 0.64: agreement
```

**Interpretation.** At $x = 2$ the hand formula gives $\frac{2 \cdot 8}{25} = 0.64$ and the difference quotient agrees to about ten digits. Note the division of labor: the *rules* produced the formula valid at every $x$; the numerics confirmed it at a point. A formula is checked by spot-testing; it is produced by mathematics.

```{admonition} Data Science Connection
:class: tip
Modern machine-learning frameworks differentiate enormous functions by **automatic differentiation**: they represent a computation as elementary operations and apply exactly this chapter's rules (plus the chain rule) mechanically, propagating derivatives through sums, products, and quotients. When a library "computes gradients," it is executing the product rule at scale. The rules you are practicing by hand are the literal instruction set of that machinery.
```

## 4.7 Exercises

### Quick Check

1. Differentiate: $x^{7}$, $\ \sqrt[4]{x}$, $\ \dfrac{5}{x^3}$, $\ 6$.
2. If $f(2) = 3$, $f'(2) = -1$, $g(2) = 5$, $g'(2) = 4$, compute $(fg)'(2)$ and $\left(\frac{f}{g}\right)'(2)$.
3. What is the 4th derivative of $x^3 + 100x^2$?
4. True or false: $\frac{d}{dx}\left[e^2\right] = 2e$.

````{admonition} Answers to Quick Checks
:class: dropdown
1. $7x^6$; $\ \frac14 x^{-3/4}$; $\ -15x^{-4}$; $\ 0$.
2. $(fg)'(2) = f'g + fg' = (-1)(5)+(3)(4) = 7$; $\left(\frac{f}{g}\right)'(2) = \frac{f'g - fg'}{g^2} = \frac{-5-12}{25} = -\frac{17}{25}$.
3. $0$ (the third derivative is the constant $6$).
4. False: $e^2$ is a constant, so the derivative is $0$.
````

### Basic Practice

5. Differentiate each function:
   (a) $f(x) = 2x^6 - 4x^3 + x - 11$;  (b) $g(t) = \sqrt{t} + \dfrac{4}{t}$;  (c) $h(x) = (3x^2 - 1)(x^2 + 2x)$;  (d) $y = \dfrac{2x + 1}{x - 4}$;  (e) $y = \dfrac{x^3 - 8}{x}$ *(simplify first)*.
6. Find the equation of the tangent line to $y = \dfrac{x}{x^2+1}$ at $x = 1$.
7. Compute $f''(x)$ for $f(x) = x^4 - 6x^2$ and determine where $f''(x) = 0$.

````{admonition} Solution to Exercise 6
:class: dropdown
Quotient rule: $y' = \dfrac{(1)(x^2+1) - x(2x)}{(x^2+1)^2} = \dfrac{1 - x^2}{(x^2+1)^2}$.

At $x = 1$: slope $y'(1) = \frac{0}{4} = 0$, point $y(1) = \frac12$. Horizontal tangent: $y = \frac12$. (A picture confirms: $x/(x^2+1)$ crests exactly at $x = 1$.)
````

### Intermediate Practice

8. For which values of $x$ does $f(x) = x^3 - 6x^2 + 9x + 1$ have a horizontal tangent line? Determine, using the sign of $f'$ on each interval, whether each is a local peak or valley.
9. Differentiate $y = \dfrac{(x^2+1)(x-3)}{x}$ two ways: (i) expand into powers of $x$ first, (ii) product and quotient rules directly. Confirm the answers agree.
10. Suppose the number of users of an app is $u(t) = 500 + 300t$ (thousands) and the average revenue per user is $r(t) = 2 - 0.1t$ (dollars), with $t$ in months. Total revenue is $R(t) = u(t)\,r(t)$. Compute $R'(t)$ with the product rule, evaluate $R'(4)$, and interpret its sign in one sentence.
11. Find constants $a, b$ so that the parabola $y = ax^2 + bx$ passes through $(2, 6)$ with slope $5$ there.

````{admonition} Hint for Exercise 8
:class: dropdown
$f'(x) = 3x^2 - 12x + 9 = 3(x-1)(x-3)$. Test the sign of $f'$ at a point in each of the three intervals the roots create.
````

### Conceptual Understanding

12. The product rule has a plus sign and the quotient rule a minus sign. Give an intuitive reason: when the denominator of a fraction grows, what happens to the fraction?
13. Explain why every polynomial of degree $n$ satisfies $p^{(n+1)}(x) = 0$ identically, and what this says about how many derivatives can carry information about $p$.
14. If $f'(a)$ exists, must $f''(a)$ exist? Support your answer with the example $f(x) = x\,|x|$ (compute $f'$ on each side of $0$ first).

### Python Practice

15. Use SymPy to check every part of Exercise 5, and to find and classify the horizontal-tangent points in Exercise 8 (`sp.solve` on $f'$, then evaluate $f''$ at the roots).
16. Write a function `tangent_line(f_expr, x0)` that uses SymPy to return the tangent line to `f_expr` at `x0` as an expression $f(x_0) + f'(x_0)(x - x_0)$. Test it against Exercise 6.

### Visualization Practice

17. Plot $f(x) = x^3 - 6x^2 + 9x + 1$ and $f'(x)$ in stacked panels sharing an $x$-axis (as in {numref}`fig-f-and-fprime`). Mark the roots of $f'$ in both panels with vertical dashed lines and confirm visually that they align with $f$'s peak and valley.
18. Reproduce {numref}`fig-tangent-family` for $f(x) = x^3$ at $x_0 = -1, 0, 1$: short tangent segments on the curve, slopes computed by the power rule.

### Challenge

19. Prove the **extended product rule** $(fgh)' = f'gh + fg'h + fgh'$ by applying the two-factor product rule twice, and use it to differentiate $y = x(x^2+1)(x^3+2)$ without expanding.
20. Derive the **reciprocal rule** $\left(\frac{1}{g}\right)' = -\frac{g'}{g^2}$ directly from the limit definition (imitate {prf:ref}`ex-deriv-def-recip` with $g$ in place of $x$), and then show the quotient rule follows by writing $\frac{f}{g} = f \cdot \frac{1}{g}$ and using the product rule.

### Cumulative Review

21. *(Ch. 1)* For $f(x) = \frac{1}{x+2}$, simplify the difference quotient $\frac{f(x+h)-f(x)}{h}$ completely, take $h \to 0$, and confirm the result matches what the quotient rule gives for the same function.
22. *(Ch. 2)* Solve $e^{2x} - 3e^x + 2 = 0$ exactly. *(Hint: quadratic in $e^x$.)*

## 4.8 Summary

The power rule $\frac{d}{dx}x^n = nx^{n-1}$, together with linearity, differentiates all polynomials and, after rewriting roots and reciprocals as powers, far more. Products obey $(fg)' = f'g + fg'$ — derived by the add-and-subtract trick — and quotients obey $(f/g)' = (f'g - fg')/g^2$, with the order in the numerator mattering. Simplifying before differentiating is a habit that prevents errors and work. Repeated differentiation yields higher-order derivatives, with $f''$ measuring how the slope itself changes. SymPy `diff` verifies formulas exactly; central differences verify them numerically at chosen points; and the derivative's applied meaning — marginal change, sensitivity — is what makes these rules the workhorse of quantitative reasoning. One rule is still missing: compositions like $(x^2+1)^{50}$ or $e^{-x^2}$ defeat everything in this chapter, and the chain rule of Chapter 5 exists to handle exactly them.

*Parallel reading:* OpenStax *Calculus Volume 1*, Sections 3.3 and 3.4 {cite}`openstax_calc1`.
