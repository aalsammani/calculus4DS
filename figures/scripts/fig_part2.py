"""Figures for Part II (Chapters 7-11): integration. Also prints the
verification numbers quoted in the chapter prose."""

import numpy as np
import matplotlib.pyplot as plt

from bookstyle import apply_style, savefig, COLORS

apply_style()

# --------------------------------------------------------- ch07-riemann-sums
f = lambda t: t**2
fig, axes = plt.subplots(1, 3, figsize=(10.2, 3.4), sharey=True)
t = np.linspace(0, 1, 300)
n = 10
edges = np.linspace(0, 1, n + 1)
w = edges[1] - edges[0]
titles = ["left endpoints", "midpoints", "right endpoints"]
samples = [edges[:-1], (edges[:-1] + edges[1:]) / 2, edges[1:]]
sums = []
for ax, title, s in zip(axes, titles, samples):
    ax.plot(t, f(t), color=COLORS["blue"], zorder=5)
    ax.bar(edges[:-1], f(s), width=w, align="edge",
           color=COLORS["sky"], alpha=0.55, edgecolor=COLORS["blue"], lw=0.8)
    total = float(np.sum(f(s) * w))
    sums.append(total)
    ax.set_title(f"{title}: sum $= {total:.4f}$", fontsize=10.5)
    ax.set_xlabel("$x$")
axes[0].set_ylabel("$y$")
fig.suptitle("Riemann sums for $\\int_0^1 x^2\\,dx$ with $n=10$ rectangles "
             "(true value $1/3$)", y=1.04)
savefig(fig, "part2", "ch07-riemann-sums")
print("Riemann n=10 left/mid/right:", [f"{s:.4f}" for s in sums])
for n_ in [10, 100, 1000]:
    e_ = np.linspace(0, 1, n_ + 1)
    m_ = (e_[:-1] + e_[1:]) / 2
    print(f"midpoint n={n_}: {np.sum(f(m_)) * (1/n_):.8f}")

# --------------------------------------------------------- ch07-signed-area
fig, ax = plt.subplots()
t = np.linspace(0, 2 * np.pi, 400)
ax.plot(t, np.sin(t), color=COLORS["blue"])
ax.axhline(0, color="k", lw=0.8)
ax.fill_between(t, np.sin(t), 0, where=np.sin(t) >= 0,
                color=COLORS["green"], alpha=0.35)
ax.fill_between(t, np.sin(t), 0, where=np.sin(t) <= 0,
                color=COLORS["red"], alpha=0.35)
ax.annotate("$+2$", (np.pi / 2, 0.4), ha="center", fontsize=13)
ax.annotate("$-2$", (3 * np.pi / 2, -0.45), ha="center", fontsize=13)
ax.set_xticks([0, np.pi, 2 * np.pi])
ax.set_xticklabels(["0", "$\\pi$", "$2\\pi$"])
ax.set_xlabel("$x$")
ax.set_title("The definite integral counts area with sign: "
             "$\\int_0^{2\\pi}\\sin x\\,dx = 0$")
savefig(fig, "part2", "ch07-signed-area")

# --------------------------------------------------------- ch07-accumulation
fig, axes = plt.subplots(2, 1, figsize=(7, 5.4), sharex=True)
t = np.linspace(0, 2.4, 300)
axes[0].plot(t, f(t), color=COLORS["blue"])
xstop = 1.6
mask = t <= xstop
axes[0].fill_between(t[mask], f(t)[mask], color=COLORS["sky"], alpha=0.5)
axes[0].annotate("$A(x)$ = shaded area", (0.62, 0.9))
axes[0].axvline(xstop, color=COLORS["gray"], ls="--", lw=1.2)
axes[0].set_ylabel("$f(t) = t^2$")
axes[1].plot(t, t**3 / 3, color=COLORS["green"])
axes[1].plot(xstop, xstop**3 / 3, "o", color="k", zorder=5)
axes[1].axvline(xstop, color=COLORS["gray"], ls="--", lw=1.2)
axes[1].set_ylabel("$A(x) = x^3/3$")
axes[1].set_xlabel("$x$")
axes[0].set_title("Accumulated area is itself a function of the right endpoint")
savefig(fig, "part2", "ch07-accumulation")

# ------------------------------------------------------ ch08-substitution
fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.6))
a = np.sqrt(np.pi / 2)
t = np.linspace(0, a, 300)
g = 2 * t * np.cos(t**2)
axes[0].plot(t, g, color=COLORS["blue"])
axes[0].fill_between(t, g, color=COLORS["sky"], alpha=0.5)
axes[0].set_title("$\\int_0^{\\sqrt{\\pi/2}} 2x\\cos(x^2)\\,dx$")
axes[0].set_xlabel("$x$")
u = np.linspace(0, np.pi / 2, 300)
axes[1].plot(u, np.cos(u), color=COLORS["green"])
axes[1].fill_between(u, np.cos(u), color=COLORS["green"], alpha=0.3)
axes[1].set_title("$\\int_0^{\\pi/2} \\cos u\\,du$  (same area $=1$)")
axes[1].set_xlabel("$u = x^2$")
fig.suptitle("Substitution reshapes the region without changing its area",
             y=1.03)
savefig(fig, "part2", "ch08-substitution-areas")
# numeric check of both areas
from scipy.integrate import quad
A1, _ = quad(lambda s: 2 * s * np.cos(s**2), 0, a)
A2, _ = quad(np.cos, 0, np.pi / 2)
print("substitution areas:", A1, A2)

# ----------------------------------------------------- ch09-area-between
fig, ax = plt.subplots(figsize=(5.8, 4.2))
t = np.linspace(-0.15, 1.15, 300)
ax.plot(t, t, color=COLORS["blue"], label="$y = x$")
ax.plot(t, t**2, color=COLORS["orange"], label="$y = x^2$")
s = np.linspace(0, 1, 200)
ax.fill_between(s, s**2, s, color=COLORS["sky"], alpha=0.5)
ax.annotate("area $= \\dfrac{1}{6}$", (0.52, 0.32), fontsize=12)
ax.plot([0, 1], [0, 1], "o", color="k", ms=4, zorder=5)
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_title("Region between $y=x$ (top) and $y=x^2$ (bottom)")
ax.legend(loc="upper left")
savefig(fig, "part2", "ch09-area-between")

# ------------------------------------------------------------ ch09-disk
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

fig = plt.figure(figsize=(9.6, 3.9))
ax1 = fig.add_subplot(1, 2, 1)
t = np.linspace(0, 4, 200)
ax1.plot(t, np.sqrt(t), color=COLORS["blue"], label="$y=\\sqrt{x}$")
ax1.fill_between(t, np.sqrt(t), color=COLORS["sky"], alpha=0.4)
x0 = 2.5
ax1.plot([x0, x0], [0, np.sqrt(x0)], color=COLORS["red"], lw=3,
         label="radius $=\\sqrt{x}$")
ax1.set_xlabel("$x$")
ax1.set_ylabel("$y$")
ax1.set_title("Region to rotate about the $x$-axis")
ax1.legend(loc="upper left", fontsize=9)
ax2 = fig.add_subplot(1, 2, 2, projection="3d")
X = np.linspace(0, 4, 60)
TH = np.linspace(0, 2 * np.pi, 60)
X, TH = np.meshgrid(X, TH)
R = np.sqrt(X)
ax2.plot_surface(X, R * np.cos(TH), R * np.sin(TH), alpha=0.7,
                 color=COLORS["sky"], edgecolor="none")
th = np.linspace(0, 2 * np.pi, 80)
r0 = np.sqrt(x0)
ax2.plot(np.full_like(th, x0), r0 * np.cos(th), r0 * np.sin(th),
         color=COLORS["red"], lw=2.5)
ax2.set_title("The solid: each slice is a disk of area $\\pi x$")
ax2.set_xlabel("$x$")
ax2.set_box_aspect((2.2, 1, 1))
savefig(fig, "part2", "ch09-disk-solid")

# ------------------------------------------------------------ ch09-shell
fig, ax = plt.subplots(figsize=(5.8, 4.0))
t = np.linspace(0, 1, 200)
ax.plot(t, t - t**2, color=COLORS["blue"], label="$y = x - x^2$")
ax.fill_between(t, t - t**2, color=COLORS["sky"], alpha=0.4)
x0 = 0.65
ax.plot([x0, x0], [0, x0 - x0**2], color=COLORS["red"], lw=3,
        label="shell: radius $x$, height $x-x^2$")
ax.annotate("", xy=(0.06, 0.26), xytext=(x0, 0.26),
            arrowprops=dict(arrowstyle="<->", color=COLORS["gray"]))
ax.annotate("radius $x$", (0.28, 0.275), fontsize=9, color=COLORS["gray"])
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_title("Shell method: rotate vertical strips about the $y$-axis")
ax.legend(loc="upper right", fontsize=9)
savefig(fig, "part2", "ch09-shell")
V_disk = np.pi * quad(lambda s: s, 0, 4)[0]
V_shell = 2 * np.pi * quad(lambda s: s * (s - s**2), 0, 1)[0]
print("disk volume 8*pi =", V_disk, " shell volume pi/6 =", V_shell,
      np.pi / 6)

# ------------------------------------------------ ch10-trig-sub-triangle
fig, ax = plt.subplots(figsize=(5.2, 3.6))
ax.plot([0, 4, 4, 0], [0, 0, 3, 0], color=COLORS["blue"], lw=2)
ax.annotate(r"$\theta$", (0.75, 0.16), fontsize=13)
ax.annotate(r"adjacent $=\sqrt{a^2 - x^2}$", (1.15, -0.42), fontsize=10)
ax.annotate(r"opposite $= x$", (4.1, 1.4), fontsize=10)
ax.annotate(r"hypotenuse $= a$", (1.15, 1.95), fontsize=10, rotation=37)
ax.set_xlim(-0.5, 6.4)
ax.set_ylim(-0.9, 3.4)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title(r"Reference triangle for $x = a\sin\theta$", fontsize=11)
savefig(fig, "part2", "ch10-trig-sub-triangle")

# ------------------------------------------------ ch11-trap-vs-simpson
fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.6), sharey=True)
g = lambda s: np.sin(s)
t = np.linspace(0, np.pi, 300)
n = 4
xk = np.linspace(0, np.pi, n + 1)
axes[0].plot(t, g(t), color=COLORS["blue"], zorder=5)
axes[0].fill_between(t, g(t), color=COLORS["sky"], alpha=0.25)
for i in range(n):
    axes[0].plot(xk[i:i+2], g(xk[i:i+2]), color=COLORS["red"], lw=1.8)
axes[0].plot(xk, g(xk), "o", color="k", ms=4, zorder=6)
axes[0].set_title(f"Trapezoid rule, $n={n}$: straight chords")
axes[0].set_xlabel("$x$")
axes[1].plot(t, g(t), color=COLORS["blue"], zorder=5)
axes[1].fill_between(t, g(t), color=COLORS["sky"], alpha=0.25)
for i in range(0, n, 2):
    xs = xk[i:i+3]
    c = np.polyfit(xs, g(xs), 2)
    ss = np.linspace(xs[0], xs[2], 60)
    axes[1].plot(ss, np.polyval(c, ss), color=COLORS["green"], lw=1.8)
axes[1].plot(xk, g(xk), "o", color="k", ms=4, zorder=6)
axes[1].set_title(f"Simpson's rule, $n={n}$: parabolic arcs")
axes[1].set_xlabel("$x$")
savefig(fig, "part2", "ch11-trap-vs-simpson")

# ----------------------------------------------------- ch11-error-scaling
def trap(g, a, b, n):
    x = np.linspace(a, b, n + 1)
    y = g(x)
    h = (b - a) / n
    return h * (y[0] / 2 + y[1:-1].sum() + y[-1] / 2)

def simpson(g, a, b, n):
    x = np.linspace(a, b, n + 1)
    y = g(x)
    h = (b - a) / n
    return h / 3 * (y[0] + 4 * y[1:-1:2].sum() + 2 * y[2:-2:2].sum() + y[-1])

ns = np.array([4, 8, 16, 32, 64, 128, 256])
errT = np.array([abs(trap(np.sin, 0, np.pi, n) - 2) for n in ns])
errS = np.array([abs(simpson(np.sin, 0, np.pi, n) - 2) for n in ns])
fig, ax = plt.subplots()
ax.loglog(ns, errT, "o-", color=COLORS["red"], label="trapezoid error")
ax.loglog(ns, errS, "s-", color=COLORS["green"], label="Simpson error")
ax.loglog(ns, errT[0] * (ns[0] / ns) ** 2, ":", color=COLORS["red"],
          lw=1, label="slope $-2$ guide")
ax.loglog(ns, errS[0] * (ns[0] / ns) ** 4, ":", color=COLORS["green"],
          lw=1, label="slope $-4$ guide")
ax.set_xlabel("number of subintervals $n$")
ax.set_ylabel("absolute error for $\\int_0^{\\pi}\\sin x\\,dx = 2$")
ax.set_title("Error scaling: trapezoid $\\sim n^{-2}$, Simpson $\\sim n^{-4}$")
ax.legend(fontsize=9)
savefig(fig, "part2", "ch11-error-scaling")
print("trap errors:", [f"{e:.2e}" for e in errT])
print("simpson errors:", [f"{e:.2e}" for e in errS])
print("trap n=4,8:", trap(np.sin, 0, np.pi, 4), trap(np.sin, 0, np.pi, 8))
print("simpson n=4:", simpson(np.sin, 0, np.pi, 4))

print("Part 2 figures complete.")
