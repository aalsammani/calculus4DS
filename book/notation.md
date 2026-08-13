# Notation Guide

Mathematics is a language, and this page is its dictionary for this book. Skim it now; return whenever a symbol is unclear. Every chapter follows these conventions without exception.

## Numbers, sets, and intervals

| Notation | Meaning |
|---|---|
| $\mathbb{R}$ | the set of real numbers |
| $\mathbb{R}^n$ | the set of vectors with $n$ real components |
| $\mathbb{Z}$, $\mathbb{N}$ | the integers; the natural numbers $1, 2, 3, \dots$ |
| $x \in S$ | $x$ is an element of the set $S$ |
| $[a, b]$ | the closed interval $a \le x \le b$ |
| $(a, b)$ | the open interval $a < x < b$ (context distinguishes this from a coordinate pair) |
| $\{x : P(x)\}$ | the set of all $x$ satisfying property $P$ |
| $\approx$ | approximately equal (numerical approximation, never exact equality) |
| $\to$ | "approaches" or "maps to," depending on context |

## Functions

| Notation | Meaning |
|---|---|
| $f(x)$ | the value of the function $f$ at the input $x$ |
| $f : A \to B$ | $f$ takes inputs from the set $A$ and produces outputs in $B$ |
| $(f \circ g)(x) = f(g(x))$ | composition: apply $g$ first, then $f$ |
| $f^{-1}$ | the inverse function of $f$ (**not** the reciprocal $1/f$) |
| $e^x = \exp(x)$ | the natural exponential function |
| $\ln x$ | the natural logarithm (base $e$); $\log_b x$ for other bases |
| $\sin x,\ \cos x,\ \tan x$ | trigonometric functions; **angles are in radians throughout** |

## Calculus

| Notation | Meaning |
|---|---|
| $\displaystyle \lim_{x \to a} f(x)$ | the limit of $f(x)$ as $x$ approaches $a$ |
| $f'(x)$ or $\dfrac{df}{dx}$ | the derivative of $f$; both notations are used and mean the same thing |
| $f''(x)$, $f^{(n)}(x)$ | second derivative; $n$-th derivative |
| $\dfrac{d}{dx}\bigl[\,\cdot\,\bigr]$ | the differentiation operator applied to what follows |
| $\displaystyle \int f(x)\,dx$ | the indefinite integral (general antiderivative) of $f$ |
| $\displaystyle \int_a^b f(x)\,dx$ | the definite integral of $f$ from $a$ to $b$ |
| $F(x)\Big|_a^b = F(b) - F(a)$ | evaluation notation used with the Fundamental Theorem |
| $\Delta x$ | a finite (not infinitesimal) change in $x$ |
| $\dfrac{\partial f}{\partial x}$ or $f_x$ | the partial derivative of $f$ with respect to $x$ |
| $\nabla f$ | the gradient vector of $f$ |
| $\displaystyle \iint_R f\,dA$ | the double integral of $f$ over the region $R$ |

## Series

| Notation | Meaning |
|---|---|
| $\displaystyle \sum_{k=1}^{n} a_k$ | the finite sum $a_1 + a_2 + \cdots + a_n$ |
| $\displaystyle \sum_{k=1}^{\infty} a_k$ | an infinite series (the limit of partial sums) |
| $n!$ | the factorial $n(n-1)\cdots 2 \cdot 1$, with $0! = 1$ |
| $T_n(x)$ | the Taylor polynomial of degree $n$ |
| $R_n(x)$ | the remainder (truncation error) after $T_n(x)$ |

## Vectors and matrices

| Notation | Meaning |
|---|---|
| $\mathbf{v}$, $\mathbf{x}$ | vectors are bold lowercase letters |
| $v_1, v_2, \dots, v_n$ | the components (entries) of $\mathbf{v}$; scalars are italic |
| $\|\mathbf{v}\|$ | the magnitude (Euclidean norm, length) of $\mathbf{v}$ |
| $\hat{\mathbf{u}}$ | a unit vector (magnitude 1) |
| $\mathbf{u} \cdot \mathbf{v}$ | the dot product |
| $\mathbf{u} \times \mathbf{v}$ | the cross product (defined in $\mathbb{R}^3$) |
| $A$, $B$ | matrices are italic uppercase letters |
| $a_{ij}$ | the entry of $A$ in row $i$, column $j$ |
| $A \in \mathbb{R}^{m \times n}$ | $A$ has $m$ rows and $n$ columns |
| $A^{\mathsf T}$ | the transpose of $A$ |
| $I$ or $I_n$ | the identity matrix ($n \times n$ when the size matters) |
| $A^{-1}$ | the inverse of $A$ (when it exists) |
| $\det(A)$ or $\lvert A \rvert$ | the determinant of $A$ |
| $A\mathbf{x} = \mathbf{b}$ | a linear system: coefficient matrix, unknown vector, right-hand side |
| $\lambda$ | an eigenvalue |
| $\mathbf{0}$ | the zero vector |

Column vectors are the default: $\mathbf{v} \in \mathbb{R}^n$ means

$$
\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix},
$$

and a vector written horizontally in running text, $(v_1, \dots, v_n)$, still denotes this column.

## Python conventions

Code follows one style everywhere in the book: `import numpy as np`, `import matplotlib.pyplot as plt`, `import sympy as sp`. Variables mirror the mathematics (`dx` for $\Delta x$, `grad_f` for $\nabla f$). Comments explain the mathematical step being performed, not the Python syntax. Numerical output is printed with enough digits to compare against hand calculation, and every script that verifies a hand computation says so in a comment.
