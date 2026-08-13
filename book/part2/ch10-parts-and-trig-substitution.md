# Chapter 10 · Integration by Parts and Trigonometric Substitution

Substitution reverses the chain rule; this chapter's first technique, **integration by parts**, reverses the product rule, and it handles the integrals substitution cannot touch — products of *unrelated* functions like $x e^x$ and $x\sin x$, and logarithms standing alone. The second technique, **trigonometric substitution**, dissolves square roots of quadratics such as $\sqrt{a^2 - x^2}$ by a substitution that runs in the unusual direction, replacing $x$ by a trigonometric function so that a Pythagorean identity collapses the root. Together with substitution these complete the standard by-hand toolkit — and knowing the toolkit's boundaries is part of the chapter too.

## 10.1 Integration by parts

Integrate both sides of the product rule $(uv)' = u'v + uv'$:

$$
uv = \int u'v\,dx + \int uv'\,dx,
$$

and rearrange:

```{prf:theorem} Integration by parts
:label: thm-parts
For differentiable $u$ and $v$,

$$
\int u\,dv = uv - \int v\,du,
$$

or in expanded notation, $\displaystyle\int u(x)\,v'(x)\,dx = u(x)v(x) - \int v(x)\,u'(x)\,dx$.
```

Read it as a *trade*: the integral of $u\,dv$ is exchanged for the integral of $v\,du$ — the price being the boundary term $uv$. The trade is profitable when the new integral is simpler than the old, and that decides how to split the integrand: **choose $u$ to be the factor that improves when differentiated, and $dv$ the factor you can integrate.** Polynomials improve when differentiated (they lose a degree); logarithms and inverse trig functions improve dramatically (they become algebraic). The classroom mnemonic **LIATE** ranks candidates for $u$: **L**ogarithmic, **I**nverse trig, **A**lgebraic, **T**rigonometric, **E**xponential — pick $u$ from as early in the list as possible. It is a heuristic, not a law, but it almost never misleads.

```{prf:example} The prototype
:label: ex-parts-xex
Evaluate $\displaystyle\int x\,e^x\,dx$.

By LIATE, $u = x$ (algebraic) and $dv = e^x dx$. Then $du = dx$ and $v = e^x$:

$$
\int x e^x\,dx = x e^x - \int e^x\,dx = x e^x - e^x + C = (x - 1)e^x + C.
$$

**Check:** $\frac{d}{dx}\bigl[(x-1)e^x\bigr] = e^x + (x-1)e^x = xe^x$. ✓ Notice what happened: differentiating $u = x$ *demoted* it to the constant $1$, leaving a basic integral. The wrong split — $u = e^x$, $dv = x\,dx$ — would trade up to $\int \frac{x^2}{2}e^x dx$, strictly worse. When a parts attempt makes the integral uglier, swap the roles and retry.
```

```{prf:example} The logarithm, integrated at last
:label: ex-parts-ln
Evaluate $\displaystyle\int \ln x\,dx$.

There seems to be no product — but there is an invisible factor of $1$. Take $u = \ln x$, $dv = 1\,dx$, so $du = \frac{dx}{x}$, $v = x$:

$$
\int\ln x\,dx = x\ln x - \int x\cdot\frac{1}{x}\,dx = x\ln x - x + C.
$$

The trade converted a transcendental integrand into the integral of $1$. The same trick integrates $\arctan x$ and $\arcsin x$ (Exercises), and it is why L and I sit atop LIATE: as $u$ they *disappear* into algebraic $du$'s.
```

```{prf:example} Parts, twice
:label: ex-parts-twice
Evaluate $\displaystyle\int x^2\sin x\,dx$.

$u = x^2$, $dv = \sin x\,dx$: $du = 2x\,dx$, $v = -\cos x$:

$$
\int x^2\sin x\,dx = -x^2\cos x + 2\int x\cos x\,dx.
$$

The new integral needs parts again ($u = x$, $dv = \cos x\,dx$):

$$
\int x\cos x\,dx = x\sin x - \int\sin x\,dx = x\sin x + \cos x.
$$

Assembling:

$$
\int x^2\sin x\,dx = -x^2\cos x + 2x\sin x + 2\cos x + C.
$$

Each round of parts strips one power from the polynomial; $x^n$ against a sine, cosine, or exponential takes exactly $n$ rounds. (For large $n$ this bookkeeping is systematized by "tabular integration," worth looking up once you understand the loop it abbreviates.)
```

```{prf:example} The boomerang
:label: ex-parts-boomerang
Evaluate $I = \displaystyle\int e^x\cos x\,dx$.

Neither factor ever improves — the exponential is immortal, the cosine just cycles. Apply parts anyway, twice, with $u$ the trig factor both times. First: $u = \cos x$, $dv = e^xdx$:

$$
I = e^x\cos x + \int e^x\sin x\,dx.
$$

Second, on the new integral: $u = \sin x$, $dv = e^xdx$:

$$
\int e^x \sin x\,dx = e^x\sin x - \int e^x\cos x\,dx = e^x\sin x - I.
$$

The original integral has returned — as an *unknown in an equation*. Substitute back and solve algebraically:

$$
I = e^x\cos x + e^x\sin x - I
\quad\Longrightarrow\quad
2I = e^x(\cos x + \sin x)
\quad\Longrightarrow\quad
I = \frac{e^x(\sin x + \cos x)}{2} + C.
$$

**Check:** differentiating gives $\frac{e^x(\sin x + \cos x) + e^x(\cos x - \sin x)}{2} = e^x\cos x$. ✓ Two cautions: keep the *same* type of choice for $u$ in both rounds (trig both times, or exponential both times) or the second round simply undoes the first; and remember the $+C$ appears when solving, since $I$ denotes an antiderivative family.
```

**Definite integrals** carry the boundary term through evaluation: $\int_a^b u\,dv = \bigl[uv\bigr]_a^b - \int_a^b v\,du$. For instance $\int_0^1 xe^x dx = \bigl[(x-1)e^x\bigr]_0^1 = 0 - (-1) = 1$.

### Powers of sine and cosine

The volume integral of Chapter 9's Exercise 13 needed $\int\sin^2x\,dx$; here is the standard route, using the power-reduction identities of Chapter 2 rather than parts:

$$
\int \sin^2 x\,dx = \int\frac{1 - \cos 2x}{2}\,dx = \frac{x}{2} - \frac{\sin 2x}{4} + C,
\qquad
\int \cos^2 x\,dx = \frac{x}{2} + \frac{\sin 2x}{4} + C.
$$

Odd powers go by substitution instead: in $\int \sin^3x\,dx = \int(1-\cos^2x)\sin x\,dx$, put $u = \cos x$. The general principle — *even powers: reduce with identities; odd powers: peel one factor and substitute* — handles the trigonometric integrals that arise in Fourier analysis (Chapter 14) and in the substitutions of the next section.

## 10.2 Trigonometric substitution

Square roots of quadratic expressions — $\sqrt{a^2 - x^2}$, $\sqrt{a^2 + x^2}$, $\sqrt{x^2 - a^2}$ — resist both substitution (no inner derivative present) and parts. The remedy is a substitution in the *reverse* direction: instead of naming a piece of the integrand $u$, we *replace* $x$ by a trigonometric expression chosen so a Pythagorean identity eliminates the root:

| Root | Substitution | Identity used | Root becomes |
|---|---|---|---|
| $\sqrt{a^2 - x^2}$ | $x = a\sin\theta$ | $1 - \sin^2\theta = \cos^2\theta$ | $a\cos\theta$ |
| $\sqrt{a^2 + x^2}$ | $x = a\tan\theta$ | $1 + \tan^2\theta = \sec^2\theta$ | $a\sec\theta$ |
| $\sqrt{x^2 - a^2}$ | $x = a\sec\theta$ | $\sec^2\theta - 1 = \tan^2\theta$ | $a\tan\theta$ |

(with $\theta$ restricted to ranges where the emerging trig values are nonnegative, e.g. $\theta\in[-\frac\pi2,\frac\pi2]$ for the sine substitution). After integrating in $\theta$, convert back to $x$ by drawing the **reference triangle** encoding the substitution:

```{figure} figures/ch10-trig-sub-triangle.png
:name: fig-trig-sub-triangle
:alt: A right triangle with angle theta, opposite side labeled x, hypotenuse labeled a, and adjacent side labeled square root of a squared minus x squared.

The reference triangle for $x = a\sin\theta$: opposite $x$, hypotenuse $a$, hence adjacent $\sqrt{a^2 - x^2}$. Any trigonometric function of $\theta$ appearing in the antiderivative can be read off as a ratio of sides — the dictionary for translating $\theta$-answers back into $x$.
```

```{prf:example} The area of a circle, finally proved
:label: ex-trig-sub-circle
Evaluate $\displaystyle\int \sqrt{1 - x^2}\,dx$, and deduce the area of the unit circle.

Substitute $x = \sin\theta$, $dx = \cos\theta\,d\theta$; the root becomes $\sqrt{1 - \sin^2\theta} = \cos\theta$:

$$
\int\cos\theta\cdot\cos\theta\,d\theta = \int\cos^2\theta\,d\theta
= \frac{\theta}{2} + \frac{\sin 2\theta}{4}
= \frac{\theta + \sin\theta\cos\theta}{2}.
$$

Translate back with the triangle ($a = 1$): $\theta = \arcsin x$, $\sin\theta = x$, $\cos\theta = \sqrt{1-x^2}$:

$$
\int\sqrt{1-x^2}\,dx = \frac{\arcsin x + x\sqrt{1 - x^2}}{2} + C.
$$

The quarter-circle area is then $\int_0^1\sqrt{1-x^2}\,dx = \frac{\arcsin 1}{2} = \frac{\pi}{4}$, so the full unit circle has area $\pi$ — the formula every schoolchild memorizes, now an actual theorem of integration.
```

```{prf:example} A tangent substitution
:label: ex-trig-sub-tan
Evaluate $\displaystyle\int\frac{dx}{\sqrt{x^2 + 4}}$.

Here $a = 2$: substitute $x = 2\tan\theta$, $dx = 2\sec^2\theta\,d\theta$, and $\sqrt{x^2+4} = 2\sec\theta$:

$$
\int\frac{2\sec^2\theta}{2\sec\theta}\,d\theta = \int\sec\theta\,d\theta = \ln\bigl|\sec\theta + \tan\theta\bigr| + C',
$$

using the standard secant integral. The triangle for $x = 2\tan\theta$ has opposite $x$, adjacent $2$, hypotenuse $\sqrt{x^2+4}$, so $\sec\theta = \frac{\sqrt{x^2+4}}{2}$ and $\tan\theta = \frac{x}{2}$:

$$
\int\frac{dx}{\sqrt{x^2+4}} = \ln\left|\frac{\sqrt{x^2+4} + x}{2}\right| + C' = \ln\bigl(x + \sqrt{x^2+4}\bigr) + C,
$$

the constant $-\ln 2$ having been absorbed into $C$. (Compare Chapter 5, Exercise 20: this is the inverse hyperbolic sine, and its derivative was exactly $\frac{1}{\sqrt{x^2+1}}$ — the two chapters shake hands.)
```

For **definite** integrals, convert the limits into $\theta$ along with everything else and skip the triangle entirely: in {prf:ref}`ex-trig-sub-circle`, $x: 0 \to 1$ becomes $\theta: 0 \to \frac\pi2$, and $\int_0^{\pi/2}\cos^2\theta\,d\theta = \frac\pi4$ directly.

## 10.3 Common mistakes

```{admonition} Common Mistakes
:class: warning
**Forgetting the minus sign in parts.** The formula is $uv$ **minus** $\int v\,du$, and with trig antiderivatives ($v = -\cos x$) double negatives multiply. Write each piece deliberately.

**Choosing $u$ and $dv$ against the grain.** If the new integral is worse, the split was backwards — swap and redo rather than pressing on. LIATE prevents most of these.

**Boomerang bookkeeping.** In {prf:ref}`ex-parts-boomerang`, switching the *type* of $u$ between rounds returns you to the starting integral with nothing gained (the identity $I = I$); and forgetting that solving $2I = \ldots$ still needs a $+C$ loses the constant.

**Dropping $d\theta$'s factor.** In $x = a\sin\theta$, $dx$ is $a\cos\theta\,d\theta$, not $d\theta$. The substituted integral must have every piece — including $dx$ — translated.

**Sloppy back-translation.** After a trig substitution, answers like $\frac{\theta + \sin\theta\cos\theta}{2}$ must return to $x$ via the triangle; leaving a $\theta$ in the final answer, or translating $\cos\theta$ as $\sqrt{1-x^2}/a$ when the substitution was tangent-type, are both common. Draw the triangle for the substitution actually used.

**Reaching for heavy machinery early.** $\int x\sqrt{1 - x^2}\,dx$ is a plain $u$-substitution ($u = 1-x^2$), *not* a trig substitution — the factor $x$ is the inner derivative in disguise. Always check for an ordinary substitution first.
```

## 10.4 Now do it in Python

```python
import sympy as sp

x = sp.symbols('x')

# --- Integration by parts examples ---
print(sp.integrate(x * sp.exp(x), x))            # (x - 1)*exp(x)
print(sp.integrate(sp.log(x), x))                # x*log(x) - x
print(sp.integrate(x**2 * sp.sin(x), x))         # -x**2*cos(x) + 2*x*sin(x) + 2*cos(x)
print(sp.integrate(sp.exp(x) * sp.cos(x), x))    # exp(x)*sin(x)/2 + exp(x)*cos(x)/2
print(sp.integrate(x * sp.exp(x), (x, 0, 1)))    # 1

# --- Trig substitution examples ---
print(sp.integrate(sp.sqrt(1 - x**2), x))        # x*sqrt(1-x**2)/2 + asin(x)/2
print(sp.integrate(sp.sqrt(1 - x**2), (x, 0, 1)))  # pi/4
print(sp.integrate(1 / sp.sqrt(x**2 + 4), x))    # asinh(x/2)
print(sp.expand_log(sp.logcombine(
    sp.asinh(x/2).rewrite(sp.log))))             # log(x/2 + sqrt(x**2/4 + 1))

# --- Powers of sine ---
print(sp.integrate(sp.sin(x)**2, x))             # x/2 - sin(x)*cos(x)/2
print(sp.integrate(sp.sin(x)**3, x))             # cos(x)**3/3 - cos(x)
```

Two reconciliations are worth pausing on. SymPy writes the $\sin^2$ antiderivative as $\frac{x}{2} - \frac{\sin x\cos x}{2}$, ours as $\frac{x}2 - \frac{\sin 2x}{4}$; the double-angle identity shows they are the same expression. And for {prf:ref}`ex-trig-sub-tan`, SymPy answers `asinh(x/2)` — rewriting it as a logarithm (last line above) recovers our $\ln\bigl(x + \sqrt{x^2+4}\bigr)$ up to the absorbed constant $\ln\frac12$. *Different-looking antiderivatives that differ by a constant are both correct*; checking `sp.simplify(sp.diff(ans1 - ans2, x))` returns $0$ settles any doubt.

**Visualization and interpretation.** Plot the boomerang integrand and its antiderivative:

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 4*np.pi, 600)
F = np.exp(t) * (np.sin(t) + np.cos(t)) / 2
plt.semilogy(t, np.abs(np.exp(t) * np.cos(t)) + 1e-3, label=r"$|e^x\cos x|$")
plt.semilogy(t, np.abs(F) + 1e-3, label=r"$|F(x)|$")
plt.legend(); plt.xlabel("x"); plt.show()
```

On the log scale both trace straight corridors of slope $1/\ln 10$ per unit — the exponential envelope — with periodic dips at the cosine's zeros. The antiderivative inherits the integrand's structure (exponential growth modulated by oscillation), which is exactly what the closed form $\frac{e^x(\sin x + \cos x)}{2}$ says in symbols. Reading a formula and its graph as two descriptions of one object is the habit these chapters keep rehearsing.

```{admonition} Data Science Connection
:class: tip
Integration by parts is a workhorse of theoretical statistics: it converts $\mathbb E[X] = \int_0^\infty x\,p(x)\,dx$ into $\int_0^\infty (1 - P(x))\,dx$ (expectation as area above the CDF), underlies Stein's identity $\mathbb E[Xf(X)] = \mathbb E[f'(X)]$ for Gaussian $X$ — the engine of modern score-based generative models — and produces the moment formulas of the gamma and normal families. Trig substitution's job, meanwhile, is done in practice by its consequences: every table entry involving $\sqrt{1-x^2}$ or $\arctan$ that your statistics software uses was proved this way.
```

```{admonition} Looking Ahead
:class: seealso
Repeated parts applied to $\int f(t)\,dt$ with cleverly chosen boundary terms produces Taylor's theorem with integral remainder — Chapter 13's foundation. The $\int\sin^2$ and $\int\sin mx\sin nx$ computations of this chapter are precisely the *orthogonality integrals* on which Fourier series (Chapter 14) stand. And Chapter 11 addresses the honest question this chapter raises: what to do when no technique produces a closed form — which, outside textbooks, is most of the time.
```

## 10.5 Exercises

### Quick Check

1. For $\int x\cos x\,dx$, name $u$ and $dv$ per LIATE, and give the answer.
2. Evaluate $\int_1^e \ln x\,dx$ using {prf:ref}`ex-parts-ln`.
3. Which substitution dissolves $\sqrt{9 - x^2}$? What does the root become?
4. True or false: $\int x\sqrt{x^2 - 4}\,dx$ requires a secant substitution.

````{admonition} Answers to Quick Checks
:class: dropdown
1. $u = x$, $dv = \cos x\,dx$: $x\sin x + \cos x + C$.
2. $\bigl[x\ln x - x\bigr]_1^e = (e - e) - (0 - 1) = 1$.
3. $x = 3\sin\theta$; the root becomes $3\cos\theta$.
4. False — $u = x^2 - 4$ works directly, since the factor $x$ is (half) its derivative. Ordinary substitution first, always.
````

### Basic Practice

5. Evaluate by parts, checking (a) by differentiation:
   (a) $\displaystyle\int x\sin x\,dx$;  (b) $\displaystyle\int x e^{-x}\,dx$;  (c) $\displaystyle\int x^2\ln x\,dx$;  (d) $\displaystyle\int \arctan x\,dx$.
6. Evaluate the definite integrals $\displaystyle\int_0^{\pi} x\cos x\,dx$ and $\displaystyle\int_0^{1} x e^{2x}\,dx$.
7. Evaluate $\displaystyle\int\cos^2(3x)\,dx$ by power reduction.
8. Evaluate $\displaystyle\int\frac{dx}{\sqrt{25 - x^2}}$ and $\displaystyle\int\frac{x^2}{\sqrt{1 - x^2}}\,dx$.

````{admonition} Solution to Exercise 5(d)
:class: dropdown
The invisible-$1$ trick: $u = \arctan x$, $dv = dx$, so $du = \frac{dx}{1+x^2}$, $v = x$:

$$
\int\arctan x\,dx = x\arctan x - \int\frac{x}{1+x^2}\,dx = x\arctan x - \frac12\ln(1+x^2) + C,
$$

the leftover integral being the $u'/u$ pattern of Chapter 8.
````

### Intermediate Practice

9. Evaluate $\displaystyle\int e^{2x}\sin(3x)\,dx$ by the boomerang method, and verify by differentiation.
10. Evaluate $\displaystyle\int \sin^3x\cos^2x\,dx$ *(peel one sine; substitute $u = \cos x$)*.
11. Evaluate $\displaystyle\int \sqrt{4 - x^2}\,dx$ and use it to find the area of the ellipse-slice region under $y = \sqrt{4-x^2}$ from $x = -1$ to $x = 1$.
12. Evaluate $\displaystyle\int\frac{dx}{x^2\sqrt{x^2 - 9}}$ for $x > 3$ (secant substitution; translate back with the triangle).
13. Derive the reduction formula $\displaystyle\int x^n e^x\,dx = x^n e^x - n\int x^{n-1}e^x\,dx$ and apply it three times to evaluate $\int x^3 e^x\,dx$.

### Conceptual Understanding

14. Parts trades $\int u\,dv$ for $\int v\,du$. Explain, in terms of what differentiation does to each LIATE class, why logarithms make excellent $u$'s and terrible $dv$'s.
15. The boomerang method solved an equation for $I$. What property of $e^x$ and the sinusoids — visible in their derivatives — makes the original integral reappear after exactly two rounds?
16. All three trig substitutions are *inverse* substitutions: we replace the variable rather than naming a subexpression. Explain why this direction is legitimate (what guarantees we can return to $x$?), and which restriction on $\theta$ secures it.

### Python Practice

17. Verify Exercises 5–13 with SymPy. For Exercise 9, reconcile SymPy's form with your boomerang answer via `sp.simplify` of the difference.
18. Compute $\int_0^{\pi}\sin(mx)\sin(nx)\,dx$ symbolically for all $m, n \in \{1,2,3\}$ and display the results as a $3\times3$ table. State the pattern you observe (it is the orthogonality that powers Chapter 14).

### Visualization Practice

19. Plot $y = \sqrt{1-x^2}$ on $[-1,1]$ with equal axis scaling, shade $[0,1]$, and annotate with the value $\frac\pi4$ from {prf:ref}`ex-trig-sub-circle`. Then add the substituted picture: a second panel of $\cos^2\theta$ on $[0, \frac\pi2]$ shaded, annotated with the same area.
20. For $F(x) = \int_0^x t\sin t\,dt = \sin x - x\cos x$: plot $F$ and the integrand together on $[0, 6\pi]$ and explain the growing amplitude of $F$'s oscillation in terms of the factor $x$ in the integrand.

### Challenge

21. Establish the reduction formula $\displaystyle\int\sin^n x\,dx = -\frac{\sin^{n-1}x\cos x}{n} + \frac{n-1}{n}\int\sin^{n-2}x\,dx$ by parts (split $\sin^n = \sin^{n-1}\cdot\sin$), and use it to show $\displaystyle\int_0^{\pi/2}\sin^4x\,dx = \frac{3\pi}{16}$.
22. Evaluate $\displaystyle\int \sec\theta\,d\theta$ by the classic multiply-by-one trick with $\frac{\sec\theta + \tan\theta}{\sec\theta+\tan\theta}$, justifying the substitution that finishes it. (This is the missing lemma of {prf:ref}`ex-trig-sub-tan` — and historically, a celebrated seventeenth-century problem arising from the Mercator projection.)

### Cumulative Review

23. *(Ch. 8)* Evaluate $\displaystyle\int x\sqrt{1 - x^2}\,dx$ by ordinary substitution, and explain why trig substitution, though it also works, is the slower road here.
24. *(Ch. 9)* Using Exercise 7's result, compute the volume of the solid from rotating $y = \cos(3x)$, $0 \le x \le \frac{\pi}{6}$, about the $x$-axis.

## 10.6 Summary

Integration by parts, $\int u\,dv = uv - \int v\,du$, reverses the product rule: choose $u$ to improve under differentiation (LIATE: logs and inverse trig first, then powers, then trig/exponential as $dv$), iterate to strip polynomial factors, use the invisible factor $1$ to integrate $\ln$ and $\arctan$, and solve algebraically when the integral boomerangs back ($e^x\cos x$). Even powers of sine and cosine fall to power-reduction identities; odd powers to peel-and-substitute. Trigonometric substitution eliminates $\sqrt{a^2-x^2}$, $\sqrt{a^2+x^2}$, $\sqrt{x^2-a^2}$ via $x = a\sin\theta$, $a\tan\theta$, $a\sec\theta$ respectively, with the reference triangle translating answers back to $x$ and limit-conversion streamlining definite integrals — but only after checking that no ordinary substitution applies. SymPy verifies everything, teaching along the way that antiderivatives differing by a constant or an identity are equally right. The by-hand toolkit is now complete; the next chapter confronts the integrals it cannot reach.

*Parallel reading:* OpenStax *Calculus Volume 2*, Sections 3.1–3.3 {cite}`openstax_calc2`.
