# Appendix C · Python Quick Reference

The complete computational vocabulary of this book, organized by task. Libraries: NumPy {cite}`harris2020numpy`, SciPy {cite}`virtanen2020scipy`, SymPy {cite}`meurer2017sympy`, Matplotlib {cite}`hunter2007matplotlib`.

## Setup

```python
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy import integrate, optimize
```

## Symbolic calculus (SymPy)

```python
x, y, t = sp.symbols('x y t')

sp.diff(sp.sin(x**2), x)              # derivative: 2*x*cos(x**2)
sp.diff(f, x, 2)                      # second derivative
sp.diff(f, x, y)                      # mixed partial
sp.integrate(x*sp.exp(x), x)          # antiderivative (no +C shown)
sp.integrate(sp.exp(-x**2), (x, -sp.oo, sp.oo))   # definite: sqrt(pi)
sp.integrate(f, (y, 0, x), (x, 0, 1)) # iterated double integral
sp.limit(sp.sin(x)/x, x, 0)           # limits
sp.series(sp.exp(x), x, 0, 6)         # Taylor series to order 6
sp.solve(x**2 - 5*x + 6, x)           # equation solving: [2, 3]
sp.simplify(expr); sp.factor(expr); sp.expand(expr)
expr.subs({x: 2, y: 1})               # substitution
sp.lambdify(x, expr)                  # symbolic -> fast numeric function
sp.Matrix([[1, 2], [3, 4]])           # matrices: .det(), .inv(), .rref(),
                                      # .eigenvects(), .T, .jacobian(...)
```

## Numerical arrays and linear algebra (NumPy)

```python
v = np.array([1.0, 2, 3]); A = np.array([[1.0, 2], [3, 4]])
v.shape, A.shape                       # ALWAYS check shapes
np.linspace(0, 1, 101)                 # grids
A @ v; A @ B                           # matrix product (never * for this)
A * B                                  # entrywise (Hadamard) -- different!
A.T                                    # transpose
np.linalg.norm(v)                      # magnitude
np.cross(u, w)                         # cross product (3-D)
np.linalg.solve(A, b)                  # solve Ax=b (PREFER over inv)
np.linalg.inv(A); np.linalg.det(A)     # inverse, determinant
np.linalg.matrix_rank(A)               # rank
np.linalg.eig(A)                       # eigenvalues/vectors (general)
np.linalg.eigh(S)                      # symmetric: real, orthonormal, sorted
np.linalg.matrix_power(A, k)           # A^k
np.linalg.cond(A)                      # condition number
np.allclose(X, Y)                      # float comparison (never ==)
rng = np.random.default_rng(0)         # seeded random generator
rng.normal(size=(100, 5)); rng.uniform(0, 1, size=N)
```

## Numerical calculus (SciPy + NumPy)

```python
integrate.quad(f, a, b)                       # 1-D integral -> (value, err)
integrate.quad(f, -np.inf, np.inf)            # improper limits fine
integrate.dblquad(f, a, b, g1, g2)            # 2-D: f(y, x); y-limits callable
np.trapezoid(ys, xs)                          # trapezoid on samples
optimize.brentq(f, a, b)                      # root in bracketing interval
optimize.newton(f, x0, fprime=fp)             # Newton's method
np.gradient(ys, xs)                           # numerical derivative of samples
(f(x + h) - f(x)) / h                         # difference quotient, h ~ 1e-6
```

## Plotting (Matplotlib)

```python
fig, ax = plt.subplots()
ax.plot(xs, ys, label="f"); ax.legend(); ax.set_xlabel("x")
ax.scatter(xs, ys, s=6); ax.axhline(0, lw=0.5)
ax.quiver(0, 0, vx, vy, angles="xy", scale_units="xy", scale=1)  # arrows
ax.set_aspect("equal")                     # essential for geometry

X, Y = np.meshgrid(xs, ys)                 # 2-D grids
cs = ax.contour(X, Y, Z, levels=15); ax.clabel(cs)
fig = plt.figure(); ax3 = fig.add_subplot(projection="3d")
ax3.plot_surface(X, Y, Z, cmap="viridis")
fig, ax = plt.subplots(subplot_kw={"projection": "polar"})
ax.plot(theta, r)                          # polar curves
```

## Idioms this book relies on

```python
# Gradient descent (Ch. 23)
p = p0.copy()
for _ in range(steps):
    p = p - eta * grad_f(p)

# Power iteration (Ch. 20)
v = rng.normal(size=n)
for _ in range(100):
    v = A @ v; v /= np.linalg.norm(v)

# Monte Carlo integration (Ch. 24)
pts = rng.uniform(0, 1, size=(N, 2))
est = f(pts[:, 0], pts[:, 1]).mean() * area

# Numerical gradient check (Chs. 22-23)
def grad_numeric(f, p, h=1e-6):
    g = np.zeros_like(p)
    for i in range(len(p)):
        q = p.copy(); q[i] += h
        g[i] = (f(q) - f(p)) / h
    return g
```

## The recurring gotchas

Radians everywhere (`np.sin` etc.); `@` vs `*`; `np.allclose` not `==`; floating "zero" means `< 1e-10`; `pip`-style reproducibility via `requirements.txt`; seed your random generators; check `.shape` before multiplying; prefer `solve` to `inv`; SymPy is exact-but-slow, NumPy fast-but-approximate — use each for what it is.
