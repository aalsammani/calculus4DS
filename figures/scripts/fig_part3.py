"""Figures for Part III (Chapters 12-14): series. Prints verification
numbers quoted in the chapters."""

import numpy as np
import matplotlib.pyplot as plt

from bookstyle import apply_style, savefig, COLORS

apply_style()

# ---------------------------------------------------- ch12-geometric-partial
fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.6))
N = 12
n = np.arange(1, N + 1)
partial = 1 - (0.5) ** n          # sum_{k=1}^n (1/2)^k
axes[0].plot(n, partial, "o-", color=COLORS["blue"])
axes[0].axhline(1, color=COLORS["gray"], ls="--", lw=1.2)
axes[0].annotate("limit $= 1$", (7.5, 1.015), color=COLORS["gray"])
axes[0].set_xlabel("number of terms $n$")
axes[0].set_ylabel("partial sum $s_n$")
axes[0].set_title(r"$\sum_{k=1}^{\infty} (1/2)^k$: converges")
axes[0].set_ylim(0.4, 1.08)

M = 200
m = np.arange(1, M + 1)
H = np.cumsum(1.0 / m)
axes[1].plot(m, H, color=COLORS["red"], label="harmonic partial sums $H_n$")
axes[1].plot(m, np.log(m) + 0.5772, ":", color=COLORS["gray"],
             label=r"$\ln n + \gamma$")
axes[1].set_xlabel("number of terms $n$")
axes[1].set_title(r"$\sum 1/k$: diverges (like $\ln n$)")
axes[1].legend(fontsize=9)
savefig(fig, "part3", "ch12-convergence-divergence")
print("geometric partial sums:", [f"{s:.6f}" for s in partial[[0, 1, 3, 9]]])
print("H_10, H_100, H_200:", H[9], H[99], H[199])
print("ln(200)+gamma:", np.log(200) + 0.5772156649)

# ------------------------------------------------------- ch13-taylor-sin
fig, ax = plt.subplots(figsize=(7.6, 4.4))
x = np.linspace(-2 * np.pi, 2 * np.pi, 600)
ax.plot(x, np.sin(x), color="k", lw=2.2, label=r"$\sin x$")


def taylor_sin(x, degree):
    total = np.zeros_like(x)
    term_sign = 1.0
    from math import factorial
    for k in range(1, degree + 1, 2):
        total = total + term_sign * x**k / factorial(k)
        term_sign = -term_sign
    return total


for deg, color in [(1, COLORS["orange"]), (3, COLORS["green"]),
                   (5, COLORS["sky"]), (7, COLORS["purple"]),
                   (11, COLORS["red"])]:
    ax.plot(x, taylor_sin(x, deg), lw=1.4, color=color,
            label=f"$T_{{{deg}}}(x)$")
ax.set_ylim(-2.6, 2.6)
ax.axhline(0, color="k", lw=0.5)
ax.set_xlabel("$x$")
ax.legend(fontsize=9, ncol=3)
ax.set_title("Taylor polynomials of $\\sin x$ at $0$: "
             "each degree hugs the curve farther out")
savefig(fig, "part3", "ch13-taylor-sin")
from math import factorial
x0 = 1.0
approx = sum((-1)**k * x0**(2*k+1) / factorial(2*k+1) for k in range(4))
print("T7(1) =", approx, " sin(1) =", np.sin(1),
      " err:", abs(approx - np.sin(1)))
print("remainder bound 1/9! =", 1 / factorial(9))

# ------------------------------------------------- ch13-geometric-radius
fig, ax = plt.subplots(figsize=(7.2, 4.2))
x = np.linspace(-1.35, 0.98, 600)
ax.plot(x, 1 / (1 - x), color="k", lw=2.2, label=r"$\frac{1}{1-x}$")
for N, color in [(2, COLORS["orange"]), (5, COLORS["green"]),
                 (10, COLORS["sky"]), (30, COLORS["red"])]:
    s = np.zeros_like(x)
    for k in range(N + 1):
        s += x**k
    ax.plot(x, s, lw=1.3, color=color, label=f"$N={N}$")
ax.axvline(-1, color=COLORS["gray"], ls="--", lw=1.2)
ax.axvline(1, color=COLORS["gray"], ls="--", lw=1.2)
ax.annotate("radius of convergence:\nworks only for $|x|<1$",
            (-0.92, 5.6), fontsize=9, color=COLORS["gray"])
ax.set_ylim(-2, 8)
ax.set_xlabel("$x$")
ax.legend(fontsize=9)
ax.set_title(r"Partial sums of $\sum x^k$ versus $\frac{1}{1-x}$")
savefig(fig, "part3", "ch13-geometric-radius")

# ------------------------------------------------------ ch14-fourier-square
fig, axes = plt.subplots(2, 2, figsize=(9.8, 5.6), sharex=True, sharey=True)
x = np.linspace(-np.pi, 3 * np.pi, 1500)
square = np.sign(np.sin(x))


def fourier_square(x, N):
    s = np.zeros_like(x)
    for k in range(1, N + 1, 2):
        s += (4 / np.pi) * np.sin(k * x) / k
    return s


for ax, N in zip(axes.flat, [1, 3, 9, 33]):
    ax.plot(x, square, color=COLORS["gray"], lw=1.0)
    ax.plot(x, fourier_square(x, N), color=COLORS["blue"], lw=1.4)
    nterms = (N + 1) // 2
    ax.set_title(f"harmonics through $k={N}$ ({nterms} terms)", fontsize=10)
    ax.set_ylim(-1.55, 1.55)
for ax in axes[1]:
    ax.set_xlabel("$x$")
fig.suptitle("Fourier partial sums of the square wave "
             "$\\frac{4}{\\pi}\\sum_{k\\ odd} \\frac{\\sin kx}{k}$", y=1.0)
savefig(fig, "part3", "ch14-fourier-square")
peak = fourier_square(np.linspace(0.001, 0.5, 4000), 199).max()
print("Gibbs overshoot with 100 terms:", peak, "(theory ~1.1789797)")

print("Part 3 figures complete.")
