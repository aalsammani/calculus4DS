# Chapter 8 · Integration by Substitution

Differentiation is mechanical; integration is recognition. The single most valuable pattern to recognize — the one that unlocks the majority of integrals met in practice — is a chain rule that has already fired: an integrand containing a *function and its inner derivative side by side*. The technique that exploits it, **substitution** (or $u$-substitution), is the chain rule run in reverse, and this chapter develops it from mechanics through judgment.

## 8.1 The idea: undoing the chain rule

Differentiate $F(x) = \sin(x^2)$ and the chain rule produces

$$
F'(x) = \cos(x^2)\cdot 2x.
$$

Read backwards, this says

$$
\int 2x\cos(x^2)\,dx = \sin(x^2) + C,
$$

and the anatomy of the integrand is the pattern to internalize: an *outer* function $\cos(\cdot)$ evaluated at an *inner* function $x^2$, multiplied by the inner function's derivative $2x$. Whenever an integrand has the shape

$$
\int f\bigl(g(x)\bigr)\,g'(x)\,dx,
$$

the chain rule guarantees the answer $F(g(x)) + C$, where $F$ is an antiderivative of $f$.

Substitution is the bookkeeping that makes the pattern mechanical. Introduce a new variable for the inner function, $u = g(x)$, and write its differential $du = g'(x)\,dx$ — a notation Chapter 3 promised would behave like a fraction, and here is the payoff. The integral transforms:

$$
\int f\bigl(g(x)\bigr)\,\underbrace{g'(x)\,dx}_{du} \;=\; \int f(u)\,du \;=\; F(u) + C \;=\; F\bigl(g(x)\bigr) + C.
$$

The complicated $x$-integral becomes a basic $u$-integral from Chapter 7's table; solve it, then translate back.

```{prf:example} The mechanics, step by step
:label: ex-usub-mechanics
Evaluate $\displaystyle\int x^2\sqrt{x^3 + 5}\;dx$.

**Choose $u$ = the inside function:** $u = x^3 + 5$. **Compute the differential:** $du = 3x^2\,dx$, so $x^2\,dx = \frac{du}{3}$. **Substitute everything** — no $x$ may survive:

$$
\int \sqrt{u}\cdot\frac{du}{3} = \frac13\int u^{1/2}\,du = \frac13\cdot\frac{u^{3/2}}{3/2} + C = \frac{2}{9}u^{3/2} + C.
$$

**Translate back:**

$$
\int x^2\sqrt{x^3+5}\,dx = \frac29\bigl(x^3+5\bigr)^{3/2} + C.
$$

**Verify by differentiating** (chain rule): $\frac29\cdot\frac32(x^3+5)^{1/2}\cdot 3x^2 = x^2\sqrt{x^3+5}$. ✓ The constant $\frac13$ that appeared when solving $du = 3x^2dx$ is exactly what makes the check succeed; fumbled constants are substitution's most common casualty, and the check catches them every time.
```

**How to choose $u$.** Look for a function whose derivative is *also present*, up to a constant factor. Reliable candidates, in rough order of priority: the inside of a composition (under a root, inside parentheses raised to a power, in an exponent, inside a trig function or log); a denominator; the "ugliest" subexpression. If a choice leaves stray $x$'s that cannot be expressed in $u$, abandon it and try another — failed substitutions cost thirty seconds and teach pattern recognition.

```{prf:example} Three standard shapes
:label: ex-usub-shapes
**(a) Exponent as inner function:** $\displaystyle\int x\,e^{-x^2}dx$. Let $u = -x^2$, $du = -2x\,dx$, so $x\,dx = -\frac{du}{2}$:

$$
-\frac12\int e^u\,du = -\frac12 e^u + C = -\frac12 e^{-x^2} + C.
$$

**(b) Denominator as inner function:** $\displaystyle\int \frac{x}{x^2+1}\,dx$. Let $u = x^2+1$, $du = 2x\,dx$:

$$
\frac12\int\frac{du}{u} = \frac12\ln|u| + C = \frac12\ln(x^2+1) + C,
$$

the absolute value dropping since $x^2 + 1 > 0$. The general form $\int \frac{g'}{g} = \ln|g| + C$ is worth knowing on sight — it is the $u'/u$ derivative pattern of Chapter 5 reversed.

**(c) Trig with linear inside:** $\displaystyle\int \cos(3x + 1)\,dx$. Let $u = 3x+1$, $du = 3\,dx$:

$$
\frac13\int\cos u\,du = \frac13\sin(3x+1) + C.
$$

Linear substitutions $u = ax + b$ always work and always contribute the factor $\frac1a$; with practice they are done by inspection.
```

```{prf:example} A disguised pattern
:label: ex-usub-tan
Evaluate $\displaystyle\int \tan x\,dx$.

No pattern is visible until $\tan$ is unpacked: $\int\frac{\sin x}{\cos x}dx$. Now the denominator's derivative ($-\sin x$) is present up to sign. Let $u = \cos x$, $du = -\sin x\,dx$:

$$
\int\frac{\sin x}{\cos x}\,dx = -\int\frac{du}{u} = -\ln|\cos x| + C = \ln|\sec x| + C.
$$

The lesson generalizes: rewriting (definitions, identities, splitting fractions) often *creates* the substitution pattern that the original form hides.
```

## 8.2 Substitution in definite integrals

For definite integrals there are two correct workflows. Either substitute, antidifferentiate in $u$, convert back to $x$, and use the original limits — or, more elegantly, **convert the limits along with the variable** and never return to $x$: if $u = g(x)$, then $x$ running from $a$ to $b$ means $u$ running from $g(a)$ to $g(b)$, and

$$
\int_a^b f\bigl(g(x)\bigr)g'(x)\,dx = \int_{g(a)}^{g(b)} f(u)\,du.
$$

```{prf:example} Changing the limits
:label: ex-usub-definite
Evaluate $\displaystyle\int_0^{\sqrt{\pi/2}} 2x\cos\bigl(x^2\bigr)\,dx$.

Let $u = x^2$, $du = 2x\,dx$. Limits transform: $x = 0 \Rightarrow u = 0$; $x = \sqrt{\pi/2} \Rightarrow u = \pi/2$. Then

$$
\int_0^{\pi/2}\cos u\,du = \sin u\Big|_0^{\pi/2} = 1 - 0 = 1.
$$

No back-translation, no reuse of $x$-limits on a $u$-antiderivative — the classic error this workflow makes impossible.
```

```{figure} figures/ch08-substitution-areas.png
:name: fig-substitution-areas
:alt: Two panels. Left: the region under the curve 2x cosine of x squared from zero to root pi over two, tall and narrow near the right end. Right: the region under cosine u from zero to pi over two. Both shaded regions are labeled as having the same area, equal to one.

The two sides of {prf:ref}`ex-usub-definite`, drawn. Substitution is a *change of variable*: it reshapes the region — stretching here, compressing there, with the factor $du = 2x\,dx$ as the local exchange rate — while preserving total area. Both shaded regions have area exactly $1$.
```

This geometric reading is worth a pause: substitution does not "cancel symbols," it *re-parametrizes accumulation*, and the differential $du = g'(x)dx$ is the conversion factor between a sliver of width $dx$ and its image of width $du$. The same idea, with the conversion factor grown into a determinant, becomes the change-of-variables formula for multiple integrals in Part V (the "Jacobian"), and it is why $r\,dr\,d\theta$ will carry an extra $r$ in polar coordinates.

```{prf:example} When the substitution must be solved for $x$
:label: ex-usub-backsolve
Evaluate $\displaystyle\int_0^{4} \frac{x}{\sqrt{2x+1}}\,dx$.

Let $u = 2x + 1$, so $du = 2\,dx$ — but a lone $x$ remains in the numerator. Solve the substitution for it: $x = \frac{u-1}{2}$. Limits: $x=0 \Rightarrow u=1$; $x=4 \Rightarrow u=9$. Then

$$
\int_1^{9}\frac{(u-1)/2}{\sqrt u}\cdot\frac{du}{2}
= \frac14\int_1^9\bigl(u^{1/2} - u^{-1/2}\bigr)\,du
= \frac14\Bigl[\tfrac{2}{3}u^{3/2} - 2u^{1/2}\Bigr]_1^9.
$$

Evaluating: at $9$: $\frac23\cdot 27 - 2\cdot 3 = 18 - 6 = 12$; at $1$: $\frac23 - 2 = -\frac43$. So the integral is $\frac14\bigl(12 + \frac43\bigr) = \frac14\cdot\frac{40}{3} = \frac{10}{3}$.

Substitutions that require back-solving are a step harder but no different in kind: express *every* $x$-object ($x$, $dx$, limits) in $u$-terms, then integrate.
```

## 8.3 Common mistakes

```{admonition} Common Mistakes
:class: warning
**Leaving a stray $x$ in a $u$-integral.** An expression like $\int x\,u^3\,du$ is meaningless — mixed variables cannot be integrated. Either the $x$ converts (back-solve, as in {prf:ref}`ex-usub-backsolve`) or the substitution is wrong.

**Dropping the constant from $du$.** If $du = 3x^2dx$, then $x^2dx$ is $\frac{du}{3}$, not $du$. Differentiating your answer catches this instantly.

**Old limits on a new variable.** Writing $\int_0^{\sqrt{\pi/2}}\cos u\,du$ in {prf:ref}`ex-usub-definite` would be wrong: those are $x$-limits. Either convert the limits or convert the antiderivative back — never mix.

**"Substituting" what isn't there.** Substitution requires the inner derivative to be present *as a factor*. $\int \cos(x^2)\,dx$ — no $2x$ available — is beyond substitution (and in fact beyond all elementary methods; Chapter 11 handles it numerically). Recognizing what a technique *cannot* do is part of knowing the technique.

**Forgetting $+C$** in the indefinite case, as always.
```

## 8.4 Now do it in Python

SymPy is the referee for hand practice — and, usefully, its answers sometimes *look* different from yours while being equally correct, differing by a constant or an identity. Learning to reconcile the two forms is itself good calculus.

```python
import sympy as sp

x = sp.symbols('x')

# --- Verify the worked examples ---
print(sp.integrate(x**2 * sp.sqrt(x**3 + 5), x))     # 2*(x**3+5)**(3/2)/9
print(sp.integrate(x * sp.exp(-x**2), x))            # -exp(-x**2)/2
print(sp.integrate(x / (x**2 + 1), x))               # log(x**2+1)/2
print(sp.integrate(sp.tan(x), x))                    # -log(cos(x))
print(sp.integrate(2*x*sp.cos(x**2), (x, 0, sp.sqrt(sp.pi/2))))   # 1
print(sp.integrate(x / sp.sqrt(2*x + 1), (x, 0, 4)))              # 10/3

# --- And the one substitution can't touch ---
print(sp.integrate(sp.cos(x**2), x))   # answer involves fresnelc: not elementary
```

The last line is instructive: SymPy returns an answer in terms of the *Fresnel function* — a special function defined, in the spirit of Chapter 7's $\operatorname{Si}$, as this very integral. When a computer algebra system responds with an unfamiliar named function, it is telling you no combination of standard parts works; numerically, of course, `scipy.integrate.quad` evaluates such integrals without complaint.

A numerical cross-check of {prf:ref}`ex-usub-backsolve` closes the loop between technique and truth:

```python
from scipy.integrate import quad
val, _ = quad(lambda t: t / (2*t + 1)**0.5, 0, 4)
print(val, 10/3)      # 3.3333333... and 3.3333333...
```

**Interpretation.** Three independent routes — hand substitution, symbolic integration, adaptive numerics — agree on $\frac{10}{3}$. In working practice you will often run exactly this triangle: derive by hand for understanding, confirm symbolically for algebra, confirm numerically for arithmetic.

```{admonition} Data Science Connection
:class: tip
Change of variables is a load-bearing idea in probability. If a random variable $X$ has density $p_X$ and you transform it, $Y = g(X)$, the density of $Y$ acquires the factor $\left|\frac{dx}{dy}\right|$ — precisely substitution's differential bookkeeping, which is what keeps total probability equal to $1$ (areas preserved, as in {numref}`fig-substitution-areas`). Normalizing flows, a family of generative models, are built entirely from this formula iterated through many layers.
```

## 8.5 Exercises

### Quick Check

1. For $\int (2x+7)^{10}\,dx$, what is the natural $u$, and what does $dx$ become?
2. Evaluate $\int e^{5x}\,dx$ by inspection.
3. True or false: $\displaystyle\int_0^1 x(x^2+1)^3dx = \int_0^1 \frac{u^3}{2}\,du$.
4. Which of these yields to substitution: $\int x e^{x^2}dx$ or $\int e^{x^2}dx$? Why?

````{admonition} Answers to Quick Checks
:class: dropdown
1. $u = 2x+7$, $dx = \frac{du}{2}$; answer $\frac{(2x+7)^{11}}{22}+C$.
2. $\frac15 e^{5x} + C$.
3. False — the limits must transform: $u = x^2 + 1$ runs from $1$ to $2$, so the right side should be $\int_1^2 \frac{u^3}{2}du$.
4. The first: its factor $x$ is (half of) the derivative of the exponent. The second lacks that factor and has no elementary antiderivative.
````

### Basic Practice

5. Evaluate each indefinite integral; verify (a) and (d) by differentiation:
   (a) $\displaystyle\int (3x-2)^5\,dx$;  (b) $\displaystyle\int x^3\sqrt{x^4+9}\,dx$;  (c) $\displaystyle\int \frac{e^{1/x}}{x^2}\,dx$;  (d) $\displaystyle\int \sin^4 x\cos x\,dx$;  (e) $\displaystyle\int \frac{\ln x}{x}\,dx$;  (f) $\displaystyle\int \frac{dx}{x\ln x}$.
6. Evaluate each definite integral, transforming the limits:
   (a) $\displaystyle\int_0^2 x\,e^{x^2}\,dx$;  (b) $\displaystyle\int_0^{\pi/4}\tan x\sec^2x\,dx$;  (c) $\displaystyle\int_1^{2} \frac{x\,dx}{(x^2+2)^2}$.
7. Evaluate $\displaystyle\int \frac{\sin(\sqrt x)}{\sqrt x}\,dx$.

````{admonition} Solution to Exercise 5(e)
:class: dropdown
Let $u = \ln x$, $du = \frac{dx}{x}$: the integral is $\int u\,du = \frac{u^2}{2} + C = \frac{(\ln x)^2}{2} + C$.

Compare (f): the *same* substitution gives $\int \frac{du}{u} = \ln|\ln x| + C$. Two integrands differing only in where the $\ln$ sits, two quite different answers — pattern-matching, not memorization, is the skill.
````

````{admonition} Solution to Exercise 6(a)
:class: dropdown
$u = x^2$: $du = 2x\,dx$; limits $0 \to 0$, $2 \to 4$:

$$
\frac12\int_0^4 e^u\,du = \frac{e^4 - 1}{2} \approx 26.799.
$$
````

### Intermediate Practice

8. Evaluate $\displaystyle\int_0^1 x\sqrt{1-x}\,dx$ by back-solving the substitution $u = 1 - x$ for $x$, in the style of {prf:ref}`ex-usub-backsolve`.
9. Evaluate $\displaystyle\int \cot x\,dx$ and $\displaystyle\int \frac{e^x}{e^x + 1}\,dx$, and explain what single pattern both instantiate.
10. Show by substitution that $\displaystyle\int_0^{a} f(x)\,dx = \int_0^{a} f(a - x)\,dx$ for continuous $f$, and use the identity to evaluate $\displaystyle\int_0^{\pi/2}\frac{\sin x}{\sin x + \cos x}\,dx$ without finding any antiderivative. *(Add the integral to its reflected twin.)*
11. A signal's energy over $[0, T]$ is $E = \int_0^T A^2 e^{-2t/\tau}\,dt$ with amplitude $A$ and time constant $\tau$. Compute $E$, then find its limit as $T \to \infty$ and interpret the role of $\tau$.

### Conceptual Understanding

12. Explain, using {numref}`fig-substitution-areas`, why the differential's factor $g'(x)$ is necessary for areas to be preserved — what would go wrong if we substituted $u = g(x)$ but wrote $du = dx$?
13. Substitution reverses the chain rule. State which differentiation rule the technique of the *next* chapter's companion (integration by parts, Chapter 10) reverses, by inspecting the product rule and integrating both of its sides.
14. Why is it not a contradiction that $\int x e^{x^2}dx$ is elementary while $\int e^{x^2}dx$ is not, even though the second integrand looks simpler?

### Python Practice

15. Check all parts of Exercises 5 and 6 with SymPy. Where SymPy's form differs from yours (as in 5(f) or the $\tan$ integral), reconcile the two using `sp.simplify` on their difference, and state the constant.
16. For {prf:ref}`ex-usub-definite`, confirm numerically with `quad` that the $x$-integral and the $u$-integral are equal, and then *break* the correspondence deliberately by omitting the factor $2x$; report how the value changes and explain.

### Visualization Practice

17. Recreate the two-panel spirit of {numref}`fig-substitution-areas` for Exercise 6(a): the region under $xe^{x^2}$ on $[0,2]$ beside the region under $\frac12 e^u$ on $[0,4]$, annotating both with the common area $\frac{e^4-1}{2}$.
18. Plot the integrand of Exercise 10's showpiece, $\frac{\sin x}{\sin x + \cos x}$, on $[0, \pi/2]$, and overlay its reflection $\frac{\cos x}{\sin x + \cos x}$. What visual symmetry corresponds to the algebraic identity you proved, and where do the curves cross?

### Challenge

19. Evaluate $\displaystyle\int \frac{dx}{1 + e^x}$ *(one route: multiply by $\frac{e^{-x}}{e^{-x}}$ first)*, and verify by differentiation.
20. Evaluate $\displaystyle\int_0^{\pi}\frac{x\sin x}{1+\cos^2 x}\,dx$ using the reflection identity of Exercise 10 to remove the factor $x$, then a substitution to finish. *(The answer is $\frac{\pi^2}{4}$.)*

### Cumulative Review

21. *(Ch. 5)* Differentiate $y = \ln\bigl(\cos(x^2)\bigr)$, then write the antiderivative statement your result establishes.
22. *(Ch. 7)* Find $\dfrac{d}{dx}\displaystyle\int_0^{x^3}\frac{dt}{1+t^2}$ two ways: by FTC Part 1 with the chain rule, and by first evaluating the integral exactly (its antiderivative is in Chapter 7's table) and then differentiating. Confirm agreement.

## 8.6 Summary

Substitution reverses the chain rule: when an integrand contains a composition $f(g(x))$ multiplied by the inner derivative $g'(x)$, setting $u = g(x)$, $du = g'(x)\,dx$ converts the integral to $\int f(u)\,du$, solvable from the basic table, with constants from the differential tracked scrupulously and every answer checkable by differentiation. Good $u$-candidates are insides of compositions, exponents, and denominators; rewriting with identities often reveals hidden patterns ($\int\tan$, $\int g'/g = \ln|g|$), and stray $x$'s are handled by back-solving $x$ in terms of $u$. In definite integrals, transform the limits and never look back. Geometrically, substitution re-parametrizes area with $du$ as the local exchange rate — the seed of the Jacobian in Part V — and in probability the same bookkeeping is the change-of-variables formula for densities. Where the pattern is absent ($\int e^{x^2}$), substitution rightly fails, and numerical methods stand ready.

*Parallel reading:* OpenStax *Calculus Volume 1*, Section 5.5; Volume 2, Section 1.5 {cite}`openstax_calc1,openstax_calc2`.
