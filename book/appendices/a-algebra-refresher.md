# Appendix A · Algebra Refresher

A compact review of the precalculus algebra this book assumes. Each identity is stated with a worked instance and the classic error it prevents. Skim now; return whenever a manipulation in the chapters feels rusty.

## A.1 Exponents and radicals

$$
a^m a^n = a^{m+n}, \qquad \frac{a^m}{a^n} = a^{m-n}, \qquad (a^m)^n = a^{mn}, \qquad a^{-n} = \frac{1}{a^n}, \qquad a^{1/n} = \sqrt[n]{a}.
$$

Instance: $\dfrac{x^{3/2}\,x^{-1}}{x^{1/2}} = x^{3/2 - 1 - 1/2} = x^0 = 1$.

Errors to avoid: $(a + b)^2 \neq a^2 + b^2$ (it is $a^2 + 2ab + b^2$); $\sqrt{a^2 + b^2} \neq a + b$; $\sqrt{x^2} = |x|$, not $x$. These three account for a remarkable share of calculus mistakes, especially inside derivatives and integrals.

## A.2 Factoring patterns

$$
a^2 - b^2 = (a-b)(a+b), \qquad
a^3 \pm b^3 = (a \pm b)(a^2 \mp ab + b^2),
$$

$$
ax^2 + bx + c = a(x - r_1)(x - r_2) \ \text{with} \ r_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}.
$$

The discriminant $b^2 - 4ac$ counts real roots (two if positive, one if zero, none if negative) — the fact behind Chapter 19's characteristic polynomials having two, one, or no real eigenvalues. Completing the square, $x^2 + bx = \left(x + \frac b2\right)^2 - \frac{b^2}{4}$, is used in Chapter 23 (classifying quadratics) and Chapter 25 (Gaussian integrals).

## A.3 Fractions and rational expressions

$$
\frac ab + \frac cd = \frac{ad + bc}{bd}, \qquad
\frac{a/b}{c/d} = \frac{ad}{bc}, \qquad
\frac{a + b}{c} = \frac ac + \frac bc \quad\text{but}\quad \frac{a}{b + c} \neq \frac ab + \frac ac.
$$

Cancellation requires a common *factor* of the entire numerator and denominator: $\frac{x^2 - 1}{x - 1} = x + 1$ (for $x \ne 1$) because $x - 1$ factors out; $\frac{x^2 + 1}{x + 1}$ simplifies no further.

## A.4 Logarithm laws

For $a, b > 0$ (Chapter 2 derives these from exponent laws):

$$
\ln(ab) = \ln a + \ln b, \qquad \ln\frac ab = \ln a - \ln b, \qquad \ln(a^p) = p\ln a, \qquad e^{\ln a} = a.
$$

Error to avoid: $\ln(a + b)$ has **no** expansion — the laws convert products to sums, never sums to anything.

## A.5 Inequalities and absolute value

Multiplying an inequality by a negative number reverses it. $|x| < a \iff -a < x < a$; $|x| > a \iff x > a$ or $x < -a$. The triangle inequality $|a + b| \le |a| + |b|$ reappears for vectors in Chapter 15.

## A.6 Lines and slopes

Through $(x_0, y_0)$ with slope $m$: $\ y = y_0 + m(x - x_0)$ — the *point–slope form*, deliberately memorized in this arrangement because Chapter 6's linearization $L(x) = f(a) + f'(a)(x - a)$ **is** this form. Parallel lines share $m$; perpendicular lines have slopes multiplying to $-1$.

## A.7 Summation notation

$$
\sum_{k=1}^{n} a_k = a_1 + a_2 + \cdots + a_n, \qquad
\sum_{k=1}^n k = \frac{n(n+1)}{2}, \qquad
\sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}{6}.
$$

The index is a bound variable ($\sum_k a_k = \sum_j a_j$); constants factor out; sums split over addition. Chapter 12 builds on this notation heavily; Chapter 7's Riemann sums use it from the start.
