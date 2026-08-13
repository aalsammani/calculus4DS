"""Figures for Part 0 (Chapters 1-2): functions, exponentials, logs, trig."""

import numpy as np
import matplotlib.pyplot as plt

from bookstyle import apply_style, savefig, COLORS

apply_style()

# ---------------------------------------------------------------- ch01-machine
# A function as an input-output rule, shown as graph with one input traced.
fig, ax = plt.subplots(figsize=(7, 4.2))
x = np.linspace(-1, 4, 400)
f = lambda t: t**2 - 2 * t + 2
ax.plot(x, f(x), color=COLORS["blue"], label=r"$f(x) = x^2 - 2x + 2$")
x0 = 3
ax.plot([x0, x0], [0, f(x0)], ls="--", color=COLORS["gray"], lw=1.4)
ax.plot([-1, x0], [f(x0), f(x0)], ls="--", color=COLORS["gray"], lw=1.4)
ax.plot(x0, f(x0), "o", color=COLORS["red"], zorder=5)
ax.annotate("input $x=3$", xy=(3, 0), xytext=(3.15, 1.6),
            arrowprops=dict(arrowstyle="->", color=COLORS["gray"]))
ax.annotate("output $f(3)=5$", xy=(-1, 5), xytext=(-0.6, 6.4),
            arrowprops=dict(arrowstyle="->", color=COLORS["gray"]))
ax.set_xlabel("$x$")
ax.set_ylabel("$f(x)$")
ax.set_title("A function assigns exactly one output to each input")
ax.set_xlim(-1, 4.6)
ax.set_ylim(0, 8)
ax.legend(loc="upper left")
savefig(fig, "part0", "ch01-function-machine")

# ---------------------------------------------------------------- ch01-gallery
# Gallery of basic function families.
fig, axes = plt.subplots(2, 2, figsize=(8, 5.6))
panels = [
    (lambda t: 2 * t - 1, (-3, 3), r"linear: $2x-1$"),
    (lambda t: t**2, (-3, 3), r"quadratic: $x^2$"),
    (np.sqrt, (0, 9), r"square root: $\sqrt{x}$"),
    (lambda t: 1 / t, (0.15, 4), r"reciprocal: $1/x$"),
]
for ax, (g, (a, b), title) in zip(axes.flat, panels):
    t = np.linspace(a, b, 300)
    ax.plot(t, g(t), color=COLORS["blue"])
    ax.set_title(title, fontsize=11)
    ax.axhline(0, color="k", lw=0.6)
    ax.axvline(0, color="k", lw=0.6)
fig.suptitle("Four basic function families", y=1.02)
fig.tight_layout()
savefig(fig, "part0", "ch01-family-gallery")

# ---------------------------------------------------------- ch01-transformations
fig, axes = plt.subplots(1, 2, figsize=(9, 3.8), sharey=True)
t = np.linspace(-3, 3, 300)
base = t**2
axes[0].plot(t, base, color=COLORS["gray"], lw=1.6, label=r"$x^2$")
axes[0].plot(t, (t - 1) ** 2, color=COLORS["blue"], label=r"$(x-1)^2$: right 1")
axes[0].plot(t, base + 2, color=COLORS["orange"], label=r"$x^2 + 2$: up 2")
axes[0].set_title("Shifts")
axes[0].legend(fontsize=9)
axes[1].plot(t, base, color=COLORS["gray"], lw=1.6, label=r"$x^2$")
axes[1].plot(t, 2 * base, color=COLORS["green"], label=r"$2x^2$: stretch")
axes[1].plot(t, -base, color=COLORS["red"], label=r"$-x^2$: reflect")
axes[1].set_title("Scalings and reflection")
axes[1].legend(fontsize=9)
for ax in axes:
    ax.set_xlabel("$x$")
    ax.set_ylim(-5, 9)
axes[0].set_ylabel("$y$")
savefig(fig, "part0", "ch01-transformations")

# --------------------------------------------------------------- ch01-inverse
fig, ax = plt.subplots(figsize=(5.4, 5.4))
t = np.linspace(0, 4, 300)
ax.plot(t, t**2, color=COLORS["blue"], label=r"$f(x)=x^2,\ x\geq 0$")
ax.plot(t, np.sqrt(t), color=COLORS["orange"], label=r"$f^{-1}(x)=\sqrt{x}$")
ax.plot(t, t, ls="--", color=COLORS["gray"], lw=1.4, label="$y=x$")
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)
ax.set_aspect("equal")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_title("A function and its inverse are mirror images across $y=x$")
ax.legend(loc="upper left", fontsize=9)
savefig(fig, "part0", "ch01-inverse-reflection")

# ------------------------------------------------------------------- ch02-exp
fig, axes = plt.subplots(1, 2, figsize=(9, 3.8))
t = np.linspace(-2, 3, 300)
for b, c in [(2, "sky"), (np.e, "blue"), (5, "purple")]:
    label = "$e^x$" if b == np.e else f"${b}^x$"
    axes[0].plot(t, b**t, color=COLORS[c], label=label)
axes[0].set_title("Exponential growth $b^x$ for $b>1$")
axes[0].set_xlabel("$x$")
axes[0].legend()
axes[0].set_ylim(0, 20)
t2 = np.linspace(0.05, 8, 300)
axes[1].plot(t2, np.log(t2), color=COLORS["blue"], label=r"$\ln x$")
axes[1].plot(t2, np.log2(t2), color=COLORS["sky"], label=r"$\log_2 x$")
axes[1].plot(t2, np.log10(t2), color=COLORS["purple"], label=r"$\log_{10} x$")
axes[1].axvline(1, color=COLORS["gray"], lw=1, ls="--")
axes[1].set_title("Logarithms: all pass through $(1, 0)$")
axes[1].set_xlabel("$x$")
axes[1].legend()
savefig(fig, "part0", "ch02-exp-log")

# ----------------------------------------------------------- ch02-exp-vs-poly
fig, ax = plt.subplots()
t = np.linspace(0, 12, 400)
ax.plot(t, t**3, color=COLORS["orange"], label="$x^3$")
ax.plot(t, 2**t, color=COLORS["blue"], label="$2^x$")
ax.axvline(9.94, color=COLORS["gray"], lw=1, ls="--")
ax.annotate("beyond here $2^x$ wins forever", xy=(9.94, 1500),
            xytext=(4.6, 2600),
            arrowprops=dict(arrowstyle="->", color=COLORS["gray"]))
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_title("Exponentials eventually dominate every polynomial")
ax.set_ylim(0, 4200)
ax.legend()
savefig(fig, "part0", "ch02-exp-vs-poly")

# ----------------------------------------------------------- ch02-unit-circle
fig, axes = plt.subplots(1, 2, figsize=(9.2, 4.0),
                         gridspec_kw={"width_ratios": [1, 1.35]})
th = np.linspace(0, 2 * np.pi, 400)
axc = axes[0]
axc.plot(np.cos(th), np.sin(th), color=COLORS["gray"], lw=1.4)
ang = 2.3
axc.plot([0, np.cos(ang)], [0, np.sin(ang)], color=COLORS["blue"], lw=2)
axc.plot([np.cos(ang), np.cos(ang)], [0, np.sin(ang)],
         color=COLORS["green"], lw=2)
axc.plot([0, np.cos(ang)], [0, 0], color=COLORS["orange"], lw=3)
axc.plot(np.cos(ang), np.sin(ang), "o", color=COLORS["red"], zorder=5)
arc = np.linspace(0, ang, 60)
axc.plot(0.28 * np.cos(arc), 0.28 * np.sin(arc), color=COLORS["red"], lw=1.3)
axc.annotate(r"$\theta$", (0.36 * np.cos(ang / 2), 0.36 * np.sin(ang / 2)),
             fontsize=12)
axc.annotate(r"$\cos\theta$", (-0.62, -0.16), color=COLORS["orange"])
axc.annotate(r"$\sin\theta$", (np.cos(ang) - 0.62, 0.42),
             color=COLORS["green"])
axc.set_aspect("equal")
axc.set_xlim(-1.25, 1.25)
axc.set_ylim(-1.25, 1.25)
axc.set_title("The unit circle")
axc.axhline(0, color="k", lw=0.6)
axc.axvline(0, color="k", lw=0.6)
axw = axes[1]
t = np.linspace(0, 4 * np.pi, 500)
axw.plot(t, np.sin(t), color=COLORS["green"], label=r"$\sin\theta$")
axw.plot(t, np.cos(t), color=COLORS["orange"], label=r"$\cos\theta$")
axw.set_xticks(np.pi * np.arange(0, 5))
axw.set_xticklabels(["0", r"$\pi$", r"$2\pi$", r"$3\pi$", r"$4\pi$"])
axw.set_xlabel(r"$\theta$ (radians)")
axw.set_title("Reading the circle produces the waves")
axw.legend(loc="upper right")
savefig(fig, "part0", "ch02-unit-circle")

print("Part 0 figures complete.")
