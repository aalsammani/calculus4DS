"""Figures for Part IV (Chapters 15-20): linear algebra. Prints the
verification numbers quoted in the chapter prose."""

import numpy as np
import matplotlib.pyplot as plt

from bookstyle import apply_style, savefig, COLORS

apply_style()


def arrow(ax, start, end, color, label=None, lw=2.2, ls="-", zorder=5):
    ax.annotate("", xy=end, xytext=start, zorder=zorder,
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                linestyle=ls, shrinkA=0, shrinkB=0))
    if label:
        mid = (np.asarray(start) + np.asarray(end)) / 2
        ax.annotate(label, mid, fontsize=12, color=color,
                    xytext=(4, 4), textcoords="offset points")


# ------------------------------------------------ ch15-vector-operations
fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.2))
ax = axes[0]
u, v = np.array([3, 1]), np.array([1, 2])
arrow(ax, (0, 0), u, COLORS["blue"], "$\\mathbf{u}$")
arrow(ax, (0, 0), v, COLORS["green"], "$\\mathbf{v}$")
arrow(ax, u, u + v, COLORS["green"], lw=1.4, ls="--")
arrow(ax, v, u + v, COLORS["blue"], lw=1.4, ls="--")
arrow(ax, (0, 0), u + v, COLORS["red"], "$\\mathbf{u}+\\mathbf{v}$")
ax.set_xlim(-0.5, 5)
ax.set_ylim(-0.5, 3.6)
ax.set_aspect("equal")
ax.set_title("Addition: tip-to-tail / parallelogram")
ax = axes[1]
w = np.array([2, 1])
for c, col in [(2, COLORS["red"]), (1, COLORS["blue"]),
               (-1, COLORS["gray"])]:
    arrow(ax, (0, 0), c * w, col, f"${c}\\mathbf{{w}}$" if c != 1
          else "$\\mathbf{w}$")
ax.set_xlim(-2.8, 4.6)
ax.set_ylim(-1.6, 2.6)
ax.set_aspect("equal")
ax.set_title("Scalar multiplication: stretch, shrink, flip")
savefig(fig, "part4", "ch15-vector-operations")

# ------------------------------------------------ ch16-dot-projection
a = np.array([4.0, 1.0])
b = np.array([2.0, 3.0])
proj = (a @ b) / (a @ a) * a
fig, ax = plt.subplots(figsize=(5.6, 4.2))
arrow(ax, (0, 0), a, COLORS["blue"], "$\\mathbf{a}$")
arrow(ax, (0, 0), b, COLORS["green"], "$\\mathbf{b}$")
arrow(ax, (0, 0), proj, COLORS["red"],
      "$\\mathrm{proj}_{\\mathbf{a}}\\mathbf{b}$", lw=3)
ax.plot([b[0], proj[0]], [b[1], proj[1]], ls=":", color=COLORS["gray"])
ax.set_xlim(-0.4, 4.8)
ax.set_ylim(-0.6, 3.6)
ax.set_aspect("equal")
ax.set_title("The dot product measures alignment; projection is its shadow")
savefig(fig, "part4", "ch16-dot-projection")
na, nb = np.linalg.norm(a), np.linalg.norm(b)
cos_th = (a @ b) / (na * nb)
print("a.b =", a @ b, " |a| =", na, " |b| =", nb)
print("cos theta =", cos_th, " theta deg =", np.degrees(np.arccos(cos_th)))
print("projection =", proj)

# ------------------------------------------------ ch16-cross-product
fig = plt.figure(figsize=(5.8, 4.6))
ax = fig.add_subplot(projection="3d")
u3 = np.array([2.0, 0.5, 0.0])
v3 = np.array([0.5, 2.0, 0.0])
c3 = np.cross(u3, v3)
for vec, col, lab in [(u3, COLORS["blue"], "$\\mathbf{u}$"),
                      (v3, COLORS["green"], "$\\mathbf{v}$"),
                      (c3, COLORS["red"],
                       "$\\mathbf{u}\\times\\mathbf{v}$")]:
    ax.quiver(0, 0, 0, *vec, color=col, arrow_length_ratio=0.08, lw=2)
    ax.text(*(vec * 1.08), lab, fontsize=12, color=col)
verts = np.array([[0, 0, 0], u3, u3 + v3, v3])
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
ax.add_collection3d(Poly3DCollection([verts], alpha=0.25,
                                     facecolor=COLORS["sky"]))
ax.set_xlim(0, 3); ax.set_ylim(0, 3); ax.set_zlim(0, 4)
ax.set_title("$\\mathbf{u}\\times\\mathbf{v}$: perpendicular to both;\n"
             "length = parallelogram area")
savefig(fig, "part4", "ch16-cross-product")
print("cross:", c3, " area:", np.linalg.norm(c3))

# ------------------------------------------------ ch17-matrix-transform
A = np.array([[1.0, 1.0], [0.0, 1.5]])
square = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]).T
img = A @ square
fig, axes = plt.subplots(1, 2, figsize=(9.4, 4.2), sharex=True, sharey=True)
axes[0].plot(*square, color=COLORS["blue"])
axes[0].fill(*square, alpha=0.25, color=COLORS["sky"])
arrow(axes[0], (0, 0), (1, 0), COLORS["red"], "$\\mathbf{e}_1$")
arrow(axes[0], (0, 0), (0, 1), COLORS["green"], "$\\mathbf{e}_2$")
axes[0].set_title("Unit square, basis vectors")
axes[1].plot(*img, color=COLORS["blue"])
axes[1].fill(*img, alpha=0.25, color=COLORS["sky"])
arrow(axes[1], (0, 0), A[:, 0], COLORS["red"], "$A\\mathbf{e}_1$")
arrow(axes[1], (0, 0), A[:, 1], COLORS["green"], "$A\\mathbf{e}_2$")
axes[1].set_title("Image under $A$: columns are where the basis lands")
for ax in axes:
    ax.set_aspect("equal")
    ax.set_xlim(-0.4, 2.7)
    ax.set_ylim(-0.4, 2.1)
savefig(fig, "part4", "ch17-matrix-transform")

# ------------------------------------------------ ch18-row-column-picture
fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.2))
# system: x + 2y = 5 ; 3x - y = 1  -> solution (1, 2)
xs = np.linspace(-1, 4, 100)
ax = axes[0]
ax.plot(xs, (5 - xs) / 2, color=COLORS["blue"], label="$x + 2y = 5$")
ax.plot(xs, 3 * xs - 1, color=COLORS["green"], label="$3x - y = 1$")
ax.plot(1, 2, "o", color="k", zorder=6)
ax.annotate("$(1, 2)$", (1.1, 2.1), fontsize=11)
ax.set_ylim(-2, 5)
ax.legend(fontsize=9)
ax.set_title("Row picture: lines meeting at the solution")
ax = axes[1]
c1, c2, b_vec = np.array([1, 3]), np.array([2, -1]), np.array([5, 1])
arrow(ax, (0, 0), c1, COLORS["blue"], "$\\mathbf{a}_1$")
arrow(ax, (0, 0), c2, COLORS["green"], "$\\mathbf{a}_2$")
arrow(ax, (0, 0), b_vec, COLORS["red"], "$\\mathbf{b}$")
arrow(ax, c1 * 1, c1 + 2 * c2, COLORS["green"], lw=1.3, ls="--")
ax.set_xlim(-0.6, 6)
ax.set_ylim(-2.4, 4)
ax.set_aspect("equal")
ax.set_title("Column picture: $1\\,\\mathbf{a}_1 + 2\\,\\mathbf{a}_2 "
             "= \\mathbf{b}$")
savefig(fig, "part4", "ch18-row-column-picture")
print("system check:", np.linalg.solve(np.array([[1, 2], [3, -1]]),
                                       np.array([5, 1])))

# ------------------------------------------------ ch19-determinant-area
fig, ax = plt.subplots(figsize=(5.6, 4.4))
M = np.array([[3.0, 1.0], [1.0, 2.0]])
sq = np.array([[0, 0], [1, 0], [1, 1], [0, 1]]).T
par = M @ sq
ax.fill(*sq, alpha=0.35, color=COLORS["gray"], label="unit square, area 1")
ax.fill(*par, alpha=0.35, color=COLORS["sky"],
        label=f"image, area $=\\det=|{np.linalg.det(M):.0f}|$")
arrow(ax, (0, 0), M[:, 0], COLORS["blue"], "$(3,1)$")
arrow(ax, (0, 0), M[:, 1], COLORS["green"], "$(1,2)$")
ax.set_aspect("equal")
ax.set_xlim(-0.4, 4.6)
ax.set_ylim(-0.4, 3.5)
ax.legend(fontsize=9, loc="upper left")
ax.set_title("The determinant is the area-scaling factor")
savefig(fig, "part4", "ch19-determinant-area")
print("det [[3,1],[1,2]] =", np.linalg.det(M))

# ------------------------------------------------ ch20-eigen-directions
A = np.array([[2.0, 1.0], [1.0, 2.0]])
th = np.linspace(0, 2 * np.pi, 200)
circ = np.vstack([np.cos(th), np.sin(th)])
ell = A @ circ
fig, ax = plt.subplots(figsize=(6.0, 4.8))
ax.plot(*circ, color=COLORS["gray"], lw=1.2, label="unit circle")
ax.plot(*ell, color=COLORS["blue"], lw=1.6, label="image under $A$")
e1 = np.array([1, 1]) / np.sqrt(2)
e2 = np.array([1, -1]) / np.sqrt(2)
arrow(ax, (0, 0), 3 * e1, COLORS["red"],
      "$\\lambda_1=3$ direction", lw=2.4)
arrow(ax, (0, 0), 1 * e2, COLORS["green"],
      "$\\lambda_2=1$ direction", lw=2.4)
arrow(ax, (0, 0), e1, COLORS["red"], lw=1.2, ls="--")
ax.set_aspect("equal")
ax.set_xlim(-3.4, 3.9)
ax.set_ylim(-3.0, 3.0)
ax.legend(fontsize=9, loc="lower right")
ax.set_title("Eigenvectors: the directions $A$ only stretches\n"
             "$A = [[2,1],[1,2]]$ maps the circle to an ellipse")
savefig(fig, "part4", "ch20-eigen-directions")
vals, vecs = np.linalg.eig(A)
print("eigvals:", vals)
print("eigvecs (columns):\n", vecs)

# Markov steady state for ch20
P = np.array([[0.9, 0.2], [0.1, 0.8]])
vals, vecs = np.linalg.eig(P)
print("Markov eigvals:", vals)
v = vecs[:, np.argmax(vals)]
print("steady state:", v / v.sum())
state = np.array([1.0, 0.0])
for _ in range(50):
    state = P @ state
print("after 50 steps from (1,0):", state)

print("Part 4 figures complete.")
