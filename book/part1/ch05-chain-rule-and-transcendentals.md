# Chapter 5 · The Chain Rule and the Transcendental Functions

Chapter 4's rules handle sums, products, and quotients, but they are silent on the most common structure in applied mathematics: **composition**. Functions in practice are nested — $e^{-x^2}$, $\ln(1 + x^2)$, $\sin(2\pi t)$, $\sqrt{3x+1}$ — and every one of them defeats the toolkit so far. This chapter supplies the missing rule, the chain rule, and then uses it (together with two special limits) to differentiate the transcendental functions: sine, cosine, and their relatives; the exponential; and the logarithm. By the chapter's end you will be able to differentiate essentially any function built from the standard parts.

## 5.1 The chain rule

Begin with intuition. Suppose a hiker's altitude depends on position along a trail, gaining $50$ meters of altitude per kilometer, and position depends on time, at $4$ kilometers per hour. How fast is altitude changing with time? Plainly $50 \times 4 = 200$ meters per hour: *rates multiply through a chain of dependence*. That is the whole content of the chain rule.

```{prf:theorem} Chain rule
:label: thm-chain-rule
If $g$ is differentiable at $x$ and $f$ is differentiable at $g(x)$, then the composition $f \circ g$ is differentiable at $x$ and

$$
\frac{d}{dx}\,f\bigl(g(x)\bigr) \;=\; f'\bigl(g(x)\bigr)\cdot g'(x).
$$

In Leibniz notation, writing $u = g(x)$ and $y = f(u)$:

$$
\frac{dy}{dx} = \frac{dy}{du}\cdot\frac{du}{dx}.
$$
```

The Leibniz form looks like a fraction cancellation, and that mnemonic is intentional and safe here. In words: *differentiate the outer function, leaving the inside alone; then multiply by the derivative of the inside.*

**Where it comes from.** For $h \neq 0$, write $\Delta u = g(x+h) - g(x)$ and manipulate the difference quotient:

$$
\frac{f(g(x+h)) - f(g(x))}{h}
= \frac{f(g(x) + \Delta u) - f(g(x))}{\Delta u} \cdot \frac{\Delta u}{h},
$$

valid whenever $\Delta u \neq 0$. As $h \to 0$, continuity of $g$ forces $\Delta u \to 0$, so the first factor tends to $f'(g(x))$ and the second to $g'(x)$. (A fully rigorous proof patches the case where $\Delta u = 0$ for values of $h$ near zero; see OpenStax *Calculus Volume 1*, §3.6 {cite}`openstax_calc1`. The idea, though, is exactly the hiker's: rates through a chain multiply.)

```{prf:example} Chain rule, power outside
:label: ex-chain-power
Differentiate $y = (x^2 + 1)^{50}$.

Expanding is out of the question. Decompose: outer $f(u) = u^{50}$, inner $u = x^2 + 1$. Then $f'(u) = 50u^{49}$ and $u' = 2x$, so

$$
y' = 50\,(x^2+1)^{49}\cdot 2x = 100x\,(x^2+1)^{49}.
$$

The special case of the chain rule with a power outside, $\frac{d}{dx}\,[u(x)]^n = n\,[u(x)]^{n-1}u'(x)$, is used so often it has a name: the **general power rule**.
```

```{prf:example} Chain rule, root outside
:label: ex-chain-root
Differentiate $y = \sqrt{3x + 1}$.

Write $y = (3x+1)^{1/2}$: outer $u^{1/2}$ with derivative $\tfrac12 u^{-1/2}$, inner $3x+1$ with derivative $3$:

$$
y' = \frac{1}{2}(3x+1)^{-1/2}\cdot 3 = \frac{3}{2\sqrt{3x+1}}.
$$

**Check at a point:** at $x = 1$, $y' = \frac{3}{4}$; a central difference $\frac{\sqrt{3(1.001)+1} - \sqrt{3(0.999)+1}}{0.002} = 0.74999\ldots$ agrees.
```

```{prf:example} A three-link chain
:label: ex-chain-triple
Differentiate $y = \bigl(1 + \sqrt{x^2+4}\,\bigr)^3$.

Chains compose: work from the outside in, multiplying a derivative per layer.

$$
y' = 3\bigl(1 + \sqrt{x^2+4}\bigr)^2 \cdot \frac{d}{dx}\Bigl[1 + \sqrt{x^2+4}\Bigr]
   = 3\bigl(1 + \sqrt{x^2+4}\bigr)^2 \cdot \frac{2x}{2\sqrt{x^2+4}}
   = \frac{3x\bigl(1+\sqrt{x^2+4}\bigr)^2}{\sqrt{x^2+4}}.
$$

The discipline that prevents errors: at each layer, ask *what is the outermost operation?* and differentiate only it, copying its contents verbatim, before descending.
```

## 5.2 Derivatives of the trigonometric functions

The chain rule needs raw materials: derivatives of the basic functions to put at the ends of chains. For sine, return to the limit definition, expand with the angle-sum identity of Chapter 2, and separate:

$$
\begin{aligned}
\frac{\sin(x+h) - \sin x}{h}
&= \frac{\sin x\cos h + \cos x \sin h - \sin x}{h}\\[4pt]
&= \sin x \cdot \frac{\cos h - 1}{h} \;+\; \cos x \cdot \frac{\sin h}{h}.
\end{aligned}
$$

Chapter 3 established $\lim_{h\to0}\frac{\sin h}{h} = 1$, and the companion limit $\lim_{h\to0}\frac{\cos h - 1}{h} = 0$ follows from it (multiply by the conjugate $\frac{\cos h + 1}{\cos h + 1}$ and use $\sin^2 h = 1 - \cos^2 h$). Taking $h \to 0$:

$$
\frac{d}{dx}\sin x = \cos x.
$$

An identical computation with the cosine angle-sum identity gives $\frac{d}{dx}\cos x = -\sin x$, and the quotient rule then delivers the rest. The full set:

$$
\begin{array}{llll}
\dfrac{d}{dx}\sin x = \cos x, &
\dfrac{d}{dx}\cos x = -\sin x, &
\dfrac{d}{dx}\tan x = \sec^2 x, \\[8pt]
\dfrac{d}{dx}\sec x = \sec x\tan x, &
\dfrac{d}{dx}\csc x = -\csc x \cot x, &
\dfrac{d}{dx}\cot x = -\csc^2 x.
\end{array}
$$

Only the first two need memorizing cold; the others regenerate in one line each. For instance, for tangent:

$$
\frac{d}{dx}\tan x = \frac{d}{dx}\frac{\sin x}{\cos x}
= \frac{\cos x\cos x - \sin x(-\sin x)}{\cos^2 x}
= \frac{\cos^2 x + \sin^2 x}{\cos^2 x} = \frac{1}{\cos^2 x} = \sec^2 x,
$$

where the Pythagorean identity collapses the numerator. Notice, throughout, the pattern: every "co-" function's derivative carries a minus sign.

```{prf:example} Trig plus chain
:label: ex-trig-chain
Differentiate (a) $y = \sin(x^2)$ and (b) $y = \sin^2 x$.

These look similar and are not. In (a) the *sine* is outside: $y' = \cos(x^2)\cdot 2x$. In (b) the *square* is outside, since $\sin^2 x$ means $(\sin x)^2$: $y' = 2\sin x \cdot \cos x$, which the double-angle identity compresses to $\sin 2x$. Deciding *which function is outermost* is the entire skill.
```

```{prf:example} A modeling standard: the sinusoid
:label: ex-sinusoid
A seasonal demand signal is modeled as $D(t) = 40 + 12\sin\!\bigl(\tfrac{2\pi}{365}\,t\bigr)$ units at day $t$. Find $D'(t)$ and the maximum rate of change.

By the chain rule, $D'(t) = 12\cos\!\bigl(\tfrac{2\pi}{365}t\bigr)\cdot\tfrac{2\pi}{365} = \tfrac{24\pi}{365}\cos\!\bigl(\tfrac{2\pi}{365}t\bigr)$. Since cosine peaks at $1$, the demand changes fastest at $\tfrac{24\pi}{365} \approx 0.2066$ units/day — occurring where the sine factor is zero, i.e., mid-way between the seasonal extremes, exactly as intuition about waves suggests: a wave changes fastest as it crosses its midline, not at its crest.
```

## 5.3 The exponential function

Chapter 2 promised that $e$ is the base whose exponential has slope equal to height. Here is where that comes from. For any base $b > 0$, the difference quotient of $b^x$ factors remarkably:

$$
\frac{b^{x+h} - b^x}{h} = b^x\cdot\frac{b^h - 1}{h},
$$

so the derivative of $b^x$ is $b^x$ times a *constant* — the number $\lim_{h\to0}\frac{b^h-1}{h}$, which is the curve's slope at $x = 0$. Every exponential's growth rate is proportional to its current value; the base only sets the constant. The number $e$ is *defined* as the base making that constant exactly $1$ (numerically, $\frac{2^h - 1}{h} \to 0.693\ldots$ and $\frac{3^h-1}{h} \to 1.098\ldots$ as $h \to 0$, so such a base exists between $2$ and $3$). Hence:

$$
\boxed{\;\frac{d}{dx}\,e^x = e^x\;}
$$

— the only function (up to constant multiples) equal to its own derivative. The limiting constants just computed are in fact $\ln 2$ and $\ln 3$, and in general, writing $b^x = e^{x\ln b}$ and applying the chain rule:

$$
\frac{d}{dx}\,b^x = e^{x \ln b}\cdot \ln b = b^x \ln b.
$$

```{figure} figures/ch05-exp-slope-height.png
:name: fig-exp-slope-height
:alt: The exponential curve e to the x with tangent segments drawn at x equals negative one, zero, and one; at each marked point an annotation records that the tangent slope equals the height of the curve there.

The defining property of $e^x$: at every point, the tangent's slope equals the curve's height. At $x=0$ both are $1$; at $x=1$ both are $e$. This self-similarity of value and rate is why $e^x$ models systems whose growth is proportional to their size.
```

```{prf:example} The Gaussian's derivative
:label: ex-gaussian-deriv
Differentiate $y = e^{-x^2}$, the bell-curve kernel at the heart of the normal distribution.

Outer $e^u$, inner $u = -x^2$ with $u' = -2x$:

$$
y' = e^{-x^2}\cdot(-2x) = -2x\,e^{-x^2}.
$$

**Interpretation.** The factor $e^{-x^2}$ is always positive, so the sign of $y'$ is the sign of $-2x$: positive for $x<0$, zero at $x = 0$, negative for $x > 0$. The bell rises, crests exactly at the center, and falls — the derivative proves the peak sits at $x=0$ rather than merely suggesting it.
```

## 5.4 The logarithm, and logarithmic differentiation

The natural log is the inverse of $e^x$, and its derivative follows from that relationship. Start from the identity $e^{\ln x} = x$ (valid for $x>0$) and differentiate both sides, using the chain rule on the left:

$$
e^{\ln x}\cdot \frac{d}{dx}\ln x = 1
\quad\Longrightarrow\quad
x \cdot \frac{d}{dx}\ln x = 1
\quad\Longrightarrow\quad
\boxed{\;\frac{d}{dx}\ln x = \frac{1}{x}\;} \quad (x > 0).
$$

This is a small marvel: the transcendental function $\ln x$ has the perfectly algebraic derivative $1/x$ — the one power of $x$ that the power rule for antiderivatives will miss in Chapter 7, a coincidence that is not a coincidence. For other bases, change of base gives $\log_b x = \frac{\ln x}{\ln b}$, so $\frac{d}{dx}\log_b x = \frac{1}{x\ln b}$. And composing with an inner function:

$$
\frac{d}{dx}\ln\bigl(u(x)\bigr) = \frac{u'(x)}{u(x)},
$$

a form so common in statistics (score functions, log-likelihood gradients) that it deserves recognition on sight.

```{prf:example} Log with a chain
:label: ex-log-chain
Differentiate $y = \ln(1 + x^2)$.

$$
y' = \frac{2x}{1+x^2}.
$$

No product of separate derivatives, no leftover logarithm: inner derivative over inner function, done.
```

**Logarithmic differentiation** turns the log laws into a differentiation technique: take $\ln$ of both sides first, simplify with the laws, then differentiate. It is the standard route for variable-to-variable powers and for big products.

```{prf:example} Logarithmic differentiation: $x^x$
:label: ex-x-to-x
Differentiate $y = x^x$ for $x > 0$.

Neither the power rule (exponent isn't constant) nor the exponential rule (base isn't constant) applies. Take logs:

$$
\ln y = x\ln x.
$$

Differentiate both sides — left side by the chain rule ($\frac{d}{dx}\ln y = \frac{y'}{y}$), right side by the product rule:

$$
\frac{y'}{y} = 1\cdot \ln x + x\cdot\frac1x = \ln x + 1
\quad\Longrightarrow\quad
y' = x^x(\ln x + 1).
$$

Note the byproduct: $y' = 0$ when $\ln x = -1$, i.e. $x = 1/e$, locating the curve's minimum at $x = e^{-1} \approx 0.368$.
```

The same $\ln$-both-sides move also settles old business: for any real $n$ and $x>0$, $\ln(x^n) = n\ln x$ gives $\frac{y'}{y} = \frac nx$, so $y' = n\frac{x^n}{x} = nx^{n-1}$ — the power rule for **all real exponents**, as promised in Chapter 4.

## 5.5 Common mistakes

```{admonition} Common Mistakes
:class: warning
**Forgetting the inner derivative.** Writing $\frac{d}{dx}\sin(x^2) = \cos(x^2)$ omits the factor $2x$. The chain rule *always* pays out one derivative per layer; a quick audit — count your layers, count your factors — catches this.

**Misreading which function is outside.** $\sin(x^2)$ versus $\sin^2 x$ ({prf:ref}`ex-trig-chain`): different compositions, different derivatives. When unsure, rewrite with explicit parentheses before differentiating.

**Applying the power rule to $b^x$ or $x^x$.** $\frac{d}{dx}2^x$ is $2^x\ln 2$, not $x\,2^{x-1}$; the power rule requires a *constant* exponent. And $x^x$ requires logarithmic differentiation ({prf:ref}`ex-x-to-x`).

**Dropping the minus on the "co-" functions.** $\frac{d}{dx}\cos x = -\sin x$. In a long chain-rule computation this lost sign is the single most common error; make checking it a reflex.

**Writing $\frac{d}{dx}\ln(u) = \frac{1}{u}$.** Incomplete unless $u = x$: the correct form is $u'/u$.

**Degrees again.** $\frac{d}{dx}\sin x = \cos x$ is a radian fact. Differentiating a degree-based sinusoid imports a factor $\pi/180$ through the chain rule.
```

## 5.6 Now do it in Python

SymPy knows every rule in this chapter; the point of the code is to *check our hand answers* and to see the chain rule as an algorithm.

```python
import sympy as sp

x = sp.symbols('x', positive=True)

# --- Verify the worked examples ---
print(sp.diff((x**2 + 1)**50, x))            # 100*x*(x**2+1)**49   (Ex 5.2)
print(sp.diff(sp.sqrt(3*x + 1), x))          # 3/(2*sqrt(3*x+1))    (Ex 5.3)
print(sp.diff(sp.sin(x**2), x))              # 2*x*cos(x**2)        (Ex 5.5a)
print(sp.simplify(sp.diff(sp.sin(x)**2, x))) # sin(2*x)             (Ex 5.5b)
print(sp.diff(sp.exp(-x**2), x))             # -2*x*exp(-x**2)      (Ex 5.7)
print(sp.diff(sp.log(1 + x**2), x))          # 2*x/(x**2+1)         (Ex 5.8)
print(sp.simplify(sp.diff(x**x, x)))         # x**x*(log(x)+1)      (Ex 5.9)

# --- The two special limits behind Sections 5.2-5.3 ---
h = sp.symbols('h')
print(sp.limit((sp.cos(h) - 1)/h, h, 0))     # 0
print(sp.limit((2**h - 1)/h, h, 0))          # log(2)
```

A numerical spot-check makes the "slope equals height" property of $e^x$ concrete:

```python
import numpy as np

def central(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)

for x0 in [-1.0, 0.0, 1.0, 2.5]:
    print(f"x={x0:4}:  slope = {central(np.exp, x0):.6f}   height = {np.exp(x0):.6f}")
```

Every line prints two equal numbers: the derivative of $e^x$ at each point *is* its value there, to six digits.

**Visualization.** Plot $f(x) = e^{-x^2}$ with its derivative $-2xe^{-x^2}$ on shared axes:

```python
import matplotlib.pyplot as plt

t = np.linspace(-3, 3, 400)
plt.plot(t, np.exp(-t**2), label=r"$e^{-x^2}$")
plt.plot(t, -2*t*np.exp(-t**2), label=r"derivative $-2xe^{-x^2}$")
plt.axhline(0, color="k", lw=0.6)
plt.legend(); plt.xlabel("x"); plt.show()
```

**Interpretation.** The derivative curve crosses zero exactly under the bell's peak, is positive on the rising left flank and negative on the falling right flank, and has its own extremes where the bell is steepest (at $x = \pm 1/\sqrt2$, computable by setting the *second* derivative to zero — try it). Reading paired $f$/$f'$ plots fluently is a skill worth deliberate practice; it is how practitioners debug models and how Chapter 6 will reason about approximation error.

```{admonition} Data Science Connection
:class: tip
**Backpropagation is the chain rule.** A neural network is a long composition — linear map, nonlinearity, linear map, nonlinearity, … , loss — and training requires the derivative of the loss with respect to every parameter. Backpropagation computes it by applying the chain rule layer by layer from the outside in, exactly as in {prf:ref}`ex-chain-triple`, caching each layer's local derivative and multiplying. The derivative $\sigma' = \sigma(1-\sigma)$ of the logistic function and the $u'/u$ form of log-loss gradients are both single lines from this chapter.
```

```{admonition} Looking Ahead
:class: seealso
Every derivative formula in this chapter will be read *backwards* in Part II as an antiderivative formula, and the chain rule read backwards becomes **substitution** (Chapter 8), the most important integration technique. The chain rule also returns in many-variable form in Chapter 23, where it underlies the gradient computations of optimization.
```

## 5.7 Exercises

### Quick Check

1. Differentiate: $\ \sin(5x)$, $\ e^{3x}$, $\ \ln(2x)$, $\ (2x+1)^4$.
2. In $y = \cos^3 x$, which function is outermost? Differentiate it.
3. What is $\frac{d}{dx}\,3^x$?
4. True or false: $\frac{d}{dx}\ln(x^2) = \frac{1}{x^2}$.

````{admonition} Answers to Quick Checks
:class: dropdown
1. $5\cos(5x)$;  $3e^{3x}$;  $\frac{1}{x}$ (since $\ln 2x = \ln 2 + \ln x$, or by $u'/u = 2/2x$);  $8(2x+1)^3$.
2. The cube: $y' = 3\cos^2 x\cdot(-\sin x) = -3\cos^2 x\sin x$.
3. $3^x\ln 3$.
4. False: $u'/u = 2x/x^2 = 2/x$. (Equivalently $\ln x^2 = 2\ln|x|$.)
````

### Basic Practice

5. Differentiate each function:
   (a) $y = (4x^3 - x)^7$;  (b) $y = \sqrt{1 - x^2}$;  (c) $y = e^{\cos x}$;  (d) $y = \tan(3x)$;  (e) $y = \ln(x^2 + 4x)$;  (f) $y = 5^{2x}$.
6. Differentiate $y = x^2 e^{3x}$ (product rule outside, chain rule inside).
7. Differentiate $y = \dfrac{\sin x}{1 + \cos x}$ and simplify using a Pythagorean identity.
8. Find the tangent line to $y = e^{-x^2}$ at $x = 1$.

````{admonition} Solution to Exercise 7
:class: dropdown
Quotient rule:

$$
y' = \frac{\cos x(1+\cos x) - \sin x(-\sin x)}{(1+\cos x)^2}
   = \frac{\cos x + \cos^2 x + \sin^2 x}{(1+\cos x)^2}
   = \frac{\cos x + 1}{(1+\cos x)^2}
   = \frac{1}{1 + \cos x}.
$$
````

````{admonition} Solution to Exercise 8
:class: dropdown
From {prf:ref}`ex-gaussian-deriv`, $y' = -2xe^{-x^2}$, so the slope at $x=1$ is $-2e^{-1} = -2/e$ and the point is $(1, 1/e)$. Tangent:

$$
y = \frac{1}{e} - \frac{2}{e}(x - 1) = \frac{3 - 2x}{e}.
$$

Numerically $y \approx 0.3679 - 0.7358(x-1)$.
````

### Intermediate Practice

9. Differentiate $y = \sin\!\bigl(\sqrt{x^2+1}\bigr)$, identifying each of the three layers before you begin.
10. Use logarithmic differentiation to differentiate (a) $y = (x^2+1)^{\sin x}$ for the general form, and (b) $y = \dfrac{x^3\sqrt{x+1}}{(2x+5)^4}$ — where taking logs turns one hard quotient into three easy terms.
11. The logistic function is $\sigma(x) = \dfrac{1}{1 + e^{-x}}$. Show that $\sigma'(x) = \sigma(x)\bigl(1 - \sigma(x)\bigr)$.
12. For $D(t) = 40 + 12\sin\!\bigl(\tfrac{2\pi}{365}t\bigr)$ from {prf:ref}`ex-sinusoid`, find all $t$ in $[0, 365)$ where $D'(t) = 0$, and state what is happening to demand there.

````{admonition} Hint for Exercise 11
:class: dropdown
Write $\sigma(x) = (1 + e^{-x})^{-1}$ and use the general power rule; then verify that $\frac{e^{-x}}{(1+e^{-x})^2}$ equals $\sigma(1-\sigma)$ by computing $1 - \sigma = \frac{e^{-x}}{1+e^{-x}}$.
````

### Conceptual Understanding

13. Explain in plain language, using the hiker analogy or your own, why the chain rule multiplies rates rather than adding them.
14. Both $y = e^{2x}$ and $y = (e^x)^2$ define the same function. Differentiate each form by the rules suggested by its notation and confirm the answers agree. What does this illustrate about well-formed rules?
15. The function $f(x) = b^x$ satisfies $f'(x) = k\,f(x)$ for a constant $k$ depending on $b$. Explain why this proportionality — rather than the specific value of $k$ — is the reason exponentials model population growth, radioactive decay, and compound interest.

### Python Practice

16. Verify all six parts of Exercise 5 with SymPy, and verify Exercise 11 by checking that `sp.simplify(sp.diff(sigma, x) - sigma*(1 - sigma))` is $0$.
17. Write a function that, given a NumPy-callable `f` and array `xs`, plots `f` and its central-difference derivative on shared axes. Apply it to $f(x) = \sin(x^2)$ on $[0, 3]$, and explain the increasingly rapid oscillation of the derivative in terms of the factor $2x$.

### Visualization Practice

18. Plot $\sigma(x)$ and $\sigma'(x)$ from Exercise 11 on $[-6, 6]$. Where is $\sigma'$ largest, and what is its maximum value? Confirm by evaluating your formula.
19. Reproduce {numref}`fig-exp-slope-height` for $y = 2^x$ instead: tangent segments at $x = -1, 0, 1$. Their slopes will *not* equal the heights — annotate each with the ratio slope/height and observe that it is constant. What constant?

### Challenge

20. Differentiate $y = \ln\!\bigl(x + \sqrt{x^2+1}\bigr)$ and simplify fully; the answer is remarkably clean. *(This function, the inverse hyperbolic sine, returns in Chapter 10.)*
21. Assuming only that $g$ is differentiable, invertible, and $g'\bigl(g^{-1}(x)\bigr) \neq 0$, differentiate both sides of $g\bigl(g^{-1}(x)\bigr) = x$ to derive the **inverse function rule** $\bigl(g^{-1}\bigr)'(x) = \dfrac{1}{g'\bigl(g^{-1}(x)\bigr)}$, and use it to re-derive $\frac{d}{dx}\ln x = \frac1x$ and to show $\frac{d}{dx}\arctan x = \frac{1}{1+x^2}$.

### Cumulative Review

22. *(Ch. 3)* Evaluate $\displaystyle\lim_{h\to 0}\frac{e^h - 1}{h}$ and explain what derivative this limit is.
23. *(Ch. 4)* Differentiate $y = \dfrac{x e^x}{x^2+1}$ using the quotient rule with a product-rule numerator, then check with SymPy.

## 5.8 Summary

The chain rule, $\frac{d}{dx}f(g(x)) = f'(g(x))\,g'(x)$, differentiates compositions by multiplying one derivative per layer, outermost first with the inside copied verbatim. Combined with the base derivatives established here — $\sin' = \cos$, $\cos' = -\sin$ (from the two special limits), $\tan' = \sec^2$ (quotient rule plus Pythagoras), $\frac{d}{dx}e^x = e^x$ (the defining property of $e$), $\frac{d}{dx}b^x = b^x\ln b$, and $\frac{d}{dx}\ln x = \frac1x$ (from inverting the exponential) — it differentiates every function built from standard parts. Logarithmic differentiation handles variable powers like $x^x$ and unwieldy products, and en route it completed the power rule for all real exponents. In code, SymPy executes these rules exactly, and pairing a function's plot with its derivative's plot is a habit that turns formulas into understanding. Differential calculus's toolkit is now complete; the next chapter puts it to work on approximation.

*Parallel reading:* OpenStax *Calculus Volume 1*, Sections 3.5–3.9 {cite}`openstax_calc1`.
