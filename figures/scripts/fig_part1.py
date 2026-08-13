"""Figures for Part I (Chapters 3-6): derivatives, chain rule, linearization,
Newton's method. Also prints verification numbers used in chapter prose."""

import numpy as np
import matplotlib.pyplot as plt

from bookstyle import apply_style, savefig, COLORS

apply_style()

# ------------------------------------------------------------ ch03-secants
f = lambda t: t**2
a = 1.0
fig, ax = plt.subplots(figsize=(7, 4.6))
t = np.linspace(-0.2, 2.6, 300)
ax.plot(t, f(t), color=COLORS["blue"], label="$f(x) = x^2$")
for h, shade in [(1.5, 0.35), (1.0, 0.55), (0.5, 0.8)]:
    m = (f(a + h) - f(a)) / h
    ax.plot(t, f(a) + m * (t - a), color=COLORS["orange"], alpha=shade, lw=1.6,
            label=f"secant, $h={h}$ (slope {m:.1f})")
ax.plot(t, f(a) + 2 * (t - a), color=COLORS["red"], lw=2.2,
        label="tangent (slope 2)")
ax.plot(a, f(a), "o", color="k", zorder=6)
ax.set_xlim(-0.2, 2.6)
ax.set_ylim(-0.5, 6)
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_title("Secant lines through $(1, 1)$ approach the tangent as $h \\to 0$")
ax.legend(fontsize=8.5, loc="upper left")
savefig(fig, "part1", "ch03-secants-to-tangent")

# ------------------------------------------------------- ch03-sinx-over-x
fig, ax = plt.subplots()
t = np.linspace(-3 * np.pi, 3 * np.pi, 601)
t = t[t != 0]
ax.plot(t, np.sin(t) / t, color=COLORS["blue"])
ax.plot(0, 1, "o", mfc="white", mec=COLORS["blue"], zorder=5)
ax.annotate("hole at $x=0$; values approach 1", xy=(0, 1), xytext=(2.2, 1.02),
            arrowprops=dict(arrowstyle="->", color=COLORS["gray"]))
ax.set_xlabel("$x$")
ax.set_ylabel("$\\sin x \\, / \\, x$")
ax.set_title("$\\lim_{x\\to 0} \\dfrac{\\sin x}{x} = 1$ even though $f(0)$ is undefined")
savefig(fig, "part1", "ch03-sinx-over-x")

# verification table for the chapter
for x in [0.5, 0.1, 0.01, 0.001]:
    print(f"sin({x})/{x} = {np.sin(x)/x:.7f}")

# -------------------------------------------------------- ch03-f-and-fprime
fig, axes = plt.subplots(2, 1, figsize=(7, 5.6), sharex=True)
t = np.linspace(-2.2, 2.2, 400)
g = t**3 - 3 * t
gp = 3 * t**2 - 3
axes[0].plot(t, g, color=COLORS["blue"])
axes[0].set_ylabel("$f(x) = x^3 - 3x$")
axes[0].axvline(-1, color=COLORS["gray"], lw=1, ls="--")
axes[0].axvline(1, color=COLORS["gray"], lw=1, ls="--")
axes[1].plot(t, gp, color=COLORS["green"])
axes[1].axhline(0, color="k", lw=0.8)
axes[1].axvline(-1, color=COLORS["gray"], lw=1, ls="--")
axes[1].axvline(1, color=COLORS["gray"], lw=1, ls="--")
axes[1].set_ylabel("$f'(x) = 3x^2 - 3$")
axes[1].set_xlabel("$x$")
axes[0].set_title("Where $f'$ is positive, $f$ rises; where $f'=0$, $f$ has a flat point")
savefig(fig, "part1", "ch03-f-and-fprime")

# --------------------------------------------------------------- ch03-corner
fig, ax = plt.subplots(figsize=(5.6, 3.8))
t = np.linspace(-2, 2, 400)
ax.plot(t, np.abs(t), color=COLORS["blue"], label="$f(x)=|x|$")
ax.plot(t[t <= 0], -t[t <= 0] * 0 - t[t <= 0] * 0 - 1 * t[t <= 0],
        ls="--", lw=1.2, color=COLORS["orange"])
ax.plot(t[t >= 0], t[t >= 0], ls="--", lw=1.2, color=COLORS["green"])
ax.annotate("slope $-1$ from the left", (-1.8, 1.5), color=COLORS["orange"],
            fontsize=9)
ax.annotate("slope $+1$ from the right", (0.55, 1.5), color=COLORS["green"],
            fontsize=9)
ax.set_title("A corner: no single tangent slope exists at $x=0$")
ax.set_xlabel("$x$")
savefig(fig, "part1", "ch03-abs-corner")

# ------------------------------------------------------ ch04-tangent-family
fig, ax = plt.subplots()
t = np.linspace(-2.4, 2.4, 300)
ax.plot(t, t**2, color=COLORS["blue"], label="$f(x)=x^2$")
for x0 in [-1.5, -0.5, 0.5, 1.5]:
    s = np.linspace(x0 - 0.7, x0 + 0.7, 20)
    ax.plot(s, x0**2 + 2 * x0 * (s - x0), color=COLORS["red"], lw=1.4)
    ax.plot(x0, x0**2, "o", color="k", ms=4, zorder=5)
ax.set_title("Tangent slopes to $x^2$ are $2x$: steeper as $|x|$ grows")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.legend()
savefig(fig, "part1", "ch04-tangent-family")

# -------------------------------------------------------- ch05-exp-property
fig, ax = plt.subplots()
t = np.linspace(-2, 2.2, 300)
ax.plot(t, np.exp(t), color=COLORS["blue"], label="$y = e^x$")
for x0 in [-1, 0, 1]:
    s = np.linspace(x0 - 0.6, x0 + 0.6, 20)
    ax.plot(s, np.exp(x0) + np.exp(x0) * (s - x0), color=COLORS["red"], lw=1.4)
    ax.plot(x0, np.exp(x0), "o", color="k", ms=4, zorder=5)
    ax.annotate(f"height $=$ slope $= e^{{{x0}}}$", (x0 + 0.06, np.exp(x0) - 0.42),
                fontsize=8.5)
ax.set_title("The defining property of $e^x$: slope equals height everywhere")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_ylim(-0.6, 9.5)
ax.legend(loc="upper left")
savefig(fig, "part1", "ch05-exp-slope-height")

# --------------------------------------------------------- ch06-linearization
fig, ax = plt.subplots()
t = np.linspace(0, 9, 300)
ax.plot(t, np.sqrt(t), color=COLORS["blue"], label="$f(x)=\\sqrt{x}$")
L = lambda s: 2 + (s - 4) / 4
ax.plot(t, L(t), color=COLORS["red"], lw=1.8,
        label="tangent line $L(x) = 2 + \\frac{1}{4}(x-4)$")
ax.plot(4, 2, "o", color="k", zorder=5)
ax.plot(4.2, np.sqrt(4.2), "s", color=COLORS["green"], ms=6, zorder=5)
ax.plot(4.2, L(4.2), "^", color=COLORS["red"], ms=6, zorder=5)
ax.annotate("near $x=4$ the curve and line\nare almost indistinguishable",
            xy=(4.2, 2.05), xytext=(5.2, 1.35),
            arrowprops=dict(arrowstyle="->", color=COLORS["gray"]))
ax.set_xlim(0, 9)
ax.set_ylim(0, 3.4)
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_title("Linearization: replacing a curve by its tangent line")
ax.legend(loc="lower right", fontsize=9)
savefig(fig, "part1", "ch06-linearization")

# print linearization check used in prose
print("sqrt(4.2) =", np.sqrt(4.2), " L(4.2) =", 2 + 0.2 / 4)

# ------------------------------------------------------------- ch06-newton
fig, ax = plt.subplots(figsize=(7, 4.6))
g = lambda s: s**2 - 2
gp = lambda s: 2 * s
t = np.linspace(0.9, 2.3, 300)
ax.plot(t, g(t), color=COLORS["blue"], label="$f(x) = x^2 - 2$")
ax.axhline(0, color="k", lw=0.8)
x = 2.0
xs = [x]
for i in range(2):
    s = np.linspace(x - 0.9, x + 0.25, 20)
    ax.plot(s, g(x) + gp(x) * (s - x), color=COLORS["red"], lw=1.4)
    ax.plot([x, x], [0, g(x)], ls=":", color=COLORS["gray"], lw=1.2)
    ax.plot(x, g(x), "o", color="k", ms=5, zorder=6)
    x = x - g(x) / gp(x)
    xs.append(x)
    ax.plot(x, 0, "v", color=COLORS["green"], ms=8, zorder=6)
ax.plot(np.sqrt(2), 0, "*", color=COLORS["purple"], ms=14, zorder=6,
        label="root $\\sqrt{2}$")
ax.annotate("$x_0=2$", (2.0, -0.35), ha="center")
ax.annotate("$x_1=1.5$", (1.5, -0.35), ha="center")
ax.annotate("$x_2\\approx1.4167$", (1.4167, 0.16), ha="center", fontsize=9)
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_title("Newton's method: slide down tangent lines to the root")
ax.legend(loc="upper left")
savefig(fig, "part1", "ch06-newton")

# print Newton iterates for sqrt(2) used in the chapter table
x = 2.0
print("Newton iterates for x^2 - 2 = 0:")
for k in range(5):
    print(f"x_{k} = {x:.12f}   error = {abs(x - np.sqrt(2)):.3e}")
    x = x - (x**2 - 2) / (2 * x)

print("Part 1 figures complete.")
