"""Figures for Part V (Chapters 21-25): multivariable calculus. Prints
verification numbers quoted in the chapter prose."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

from bookstyle import apply_style, savefig, COLORS

apply_style()

# ------------------------------------------- ch21-parametric-motion
t = np.linspace(0, 2 * np.pi, 300)
x, y = np.cos(t), np.sin(t)
fig, axes = plt.subplots(1, 2, figsize=(9.8, 4.4))
ax = axes[0]
ax.plot(x, y, color=COLORS["blue"])
for tk in [0.0, np.pi / 3, 2.4]:
    p = np.array([np.cos(tk), np.sin(tk)])
    v = np.array([-np.sin(tk), np.cos(tk)])
    ax.annotate("", xy=p + 0.55 * v, xytext=p,
                arrowprops=dict(arrowstyle="-|>", color=COLORS["red"], lw=2))
    ax.plot(*p, "o", color="k", ms=4)
ax.set_aspect("equal")
ax.set_title("Circular motion $\\mathbf{r}(t)=(\\cos t, \\sin t)$:\n"
             "velocity $\\mathbf{r}'(t)$ is tangent")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")

ax = axes[1]
v0, alpha = 20.0, np.radians(50)
tt = np.linspace(0, 2 * v0 * np.sin(alpha) / 9.8, 200)
ax.plot(v0 * np.cos(alpha) * tt, v0 * np.sin(alpha) * tt - 4.9 * tt**2,
        color=COLORS["green"])
ax.set_title("Projectile: $\\mathbf{r}(t)=(v_0\\cos\\alpha\\, t,\\ "
             "v_0\\sin\\alpha\\, t - 4.9t^2)$")
ax.set_xlabel("$x$ (m)")
ax.set_ylabel("$y$ (m)")
savefig(fig, "part5", "ch21-parametric-motion")
T = 2 * v0 * np.sin(alpha) / 9.8
print("flight time:", T, " range:", v0 * np.cos(alpha) * T,
      " max height:", (v0 * np.sin(alpha))**2 / (2 * 9.8))

# ------------------------------------------- ch22-surface-contours
xg = np.linspace(-2, 2, 120)
X, Y = np.meshgrid(xg, xg)
Z = X**2 + Y**2
fig = plt.figure(figsize=(10.0, 4.4))
ax = fig.add_subplot(1, 2, 1, projection="3d")
ax.plot_surface(X, Y, Z, cmap=cm.viridis, alpha=0.9, linewidth=0)
ax.set_title("Surface $z = x^2 + y^2$")
ax.set_xlabel("$x$"); ax.set_ylabel("$y$")
ax2 = fig.add_subplot(1, 2, 2)
cs = ax2.contour(X, Y, Z, levels=[0.5, 1, 2, 3, 4, 5, 6], cmap=cm.viridis)
ax2.clabel(cs, fontsize=8)
ax2.set_aspect("equal")
ax2.set_title("Its contour map: level curves $x^2+y^2=c$")
ax2.set_xlabel("$x$"); ax2.set_ylabel("$y$")
savefig(fig, "part5", "ch22-surface-contours")

# saddle for ch22 as well
Z2 = X**2 - Y**2
fig = plt.figure(figsize=(10.0, 4.4))
ax = fig.add_subplot(1, 2, 1, projection="3d")
ax.plot_surface(X, Y, Z2, cmap=cm.coolwarm, alpha=0.9, linewidth=0)
ax.set_title("Saddle $z = x^2 - y^2$")
ax.set_xlabel("$x$"); ax.set_ylabel("$y$")
ax2 = fig.add_subplot(1, 2, 2)
cs = ax2.contour(X, Y, Z2, levels=np.arange(-3, 3.5, 1), cmap=cm.coolwarm)
ax2.clabel(cs, fontsize=8)
ax2.set_aspect("equal")
ax2.set_title("Saddle contours: hyperbolas crossing at the origin")
savefig(fig, "part5", "ch22-saddle")

# ------------------------------------------- ch23-gradient-field
f = lambda X, Y: X**2 + 2 * Y**2
xg = np.linspace(-2, 2, 200)
X, Y = np.meshgrid(xg, xg)
fig, ax = plt.subplots(figsize=(6.2, 5.2))
cs = ax.contour(X, Y, f(X, Y), levels=[0.5, 1, 2, 3.5, 5, 7],
                cmap=cm.viridis)
ax.clabel(cs, fontsize=8)
qx = np.linspace(-1.8, 1.8, 9)
QX, QY = np.meshgrid(qx, qx)
GX, GY = 2 * QX, 4 * QY
n = np.hypot(GX, GY) + 1e-12
ax.quiver(QX, QY, GX / n, GY / n, color=COLORS["red"], scale=22, width=0.004)
ax.set_aspect("equal")
ax.set_title("Gradient field of $f = x^2 + 2y^2$:\n"
             "arrows $\\perp$ contours, pointing uphill")
ax.set_xlabel("$x$"); ax.set_ylabel("$y$")
savefig(fig, "part5", "ch23-gradient-field")
# directional derivative check: f=x^2*y at (2,1) toward (3,4)/5
gx, gy = 2 * 2 * 1, 2**2
print("grad x^2y at (2,1):", (gx, gy),
      " D_u f =", (gx * 3 + gy * 4) / 5,
      " max rate:", np.hypot(gx, gy))

# ------------------------------------------- ch24-double-integral-boxes
f24 = lambda X, Y: 4 - X - Y
n = 6
xs = np.linspace(0, 1, n + 1)
ys = np.linspace(0, 2, n + 1)
fig = plt.figure(figsize=(6.4, 5.0))
ax = fig.add_subplot(projection="3d")
Xs, Ys = np.meshgrid(np.linspace(0, 1, 40), np.linspace(0, 2, 40))
ax.plot_surface(Xs, Ys, f24(Xs, Ys), alpha=0.35, color=COLORS["sky"])
total = 0.0
for i in range(n):
    for j in range(n):
        xm, ym = (xs[i] + xs[i + 1]) / 2, (ys[j] + ys[j + 1]) / 2
        h = f24(xm, ym)
        total += h * (xs[1] - xs[0]) * (ys[1] - ys[0])
        ax.bar3d(xs[i], ys[j], 0, xs[1] - xs[0], ys[1] - ys[0], h,
                 alpha=0.55, color=COLORS["orange"], edgecolor="w",
                 linewidth=0.3, shade=True)
ax.set_title("Double integral as volume: boxes under $z = 4 - x - y$")
ax.set_xlabel("$x$"); ax.set_ylabel("$y$")
savefig(fig, "part5", "ch24-double-integral-boxes")
print("midpoint 6x6 box sum:", total, " exact:", 5.0)

# ------------------------------------------- ch25-polar-element
fig, axes = plt.subplots(1, 2, figsize=(9.8, 4.6))
ax = axes[0]
for r in [0.5, 1.0, 1.5, 2.0]:
    th = np.linspace(0, 2 * np.pi, 200)
    ax.plot(r * np.cos(th), r * np.sin(th), color=COLORS["gray"], lw=0.8)
for th0 in np.arange(0, 2 * np.pi, np.pi / 6):
    ax.plot([0, 2.2 * np.cos(th0)], [0, 2.2 * np.sin(th0)],
            color=COLORS["gray"], lw=0.8)
th = np.linspace(np.pi / 6, np.pi / 3, 50)
for rr in [1.2, 1.6]:
    ax.plot(rr * np.cos(th), rr * np.sin(th), color=COLORS["red"], lw=2.2)
for th0 in [np.pi / 6, np.pi / 3]:
    ax.plot([1.2 * np.cos(th0), 1.6 * np.cos(th0)],
            [1.2 * np.sin(th0), 1.6 * np.sin(th0)],
            color=COLORS["red"], lw=2.2)
ax.set_aspect("equal")
ax.set_title("Polar grid; a polar rectangle\n$dA = r\\,dr\\,d\\theta$")
ax = axes[1]
th = np.linspace(0, 2 * np.pi, 400)
r = 1 + np.cos(th)
ax.plot(r * np.cos(th), r * np.sin(th), color=COLORS["blue"], lw=2)
ax.set_aspect("equal")
ax.set_title("The cardioid $r = 1 + \\cos\\theta$")
savefig(fig, "part5", "ch25-polar-element")

# numeric checks for ch24/ch25
from scipy import integrate
val, _ = integrate.dblquad(lambda y, x: x * y**2, 0, 1, 0, 2)
print("iint x y^2 over [0,1]x[0,2]:", val, " exact 4/3 =", 4 / 3)
val2, _ = integrate.dblquad(lambda y, x: 4 - x - y, 0, 1, 0, 2)
print("volume 4-x-y:", val2)
# cardioid area: (1/2) int (1+cos)^2 = 3pi/2
th = np.linspace(0, 2 * np.pi, 200001)
print("cardioid area:", np.trapezoid(0.5 * (1 + np.cos(th))**2, th),
      " 3pi/2 =", 3 * np.pi / 2)
# gaussian via polar
print("int e^{-x^2}:", integrate.quad(lambda x: np.exp(-x**2),
                                      -np.inf, np.inf)[0],
      " sqrt(pi) =", np.sqrt(np.pi))
print("Part 5 figures complete.")
