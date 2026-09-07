"""
Regenerate every figure used by the pre-read notes.

    python pre-reads/figures/make_figures.py

Figures are written as PNGs next to this script. They use a solid white
background so they stay readable in both GitHub light and dark themes.
"""
import os

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))

plt.rcParams.update({
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "savefig.facecolor": "white",
    "font.size": 12,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

BLUE = "#1f77b4"
ORANGE = "#ff7f0e"
GREEN = "#2ca02c"
RED = "#d62728"
GREY = "#555555"


def save(fig, name):
    path = os.path.join(HERE, name)
    fig.savefig(path, dpi=110, bbox_inches="tight")
    plt.close(fig)
    print("wrote", os.path.relpath(path))


# --------------------------------------------------------------------------
def tangent_line():
    x = np.linspace(-1, 5, 200)
    f = x ** 2
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x, f, color=BLUE, lw=2, label=r"$f(x)=x^2$")
    x0 = 3.0
    slope = 2 * x0
    ax.plot(x, f[np.argmin(abs(x - x0))] + slope * (x - x0),
            color=RED, lw=2, ls="--", label=f"tangent at x=3 (slope {slope:.0f})")
    ax.plot([x0], [x0 ** 2], "o", color=RED)
    ax.annotate("rise/run = 6", (x0, x0 ** 2), (3.4, 4), color=RED,
                arrowprops=dict(arrowstyle="->", color=RED))
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title("The derivative is the slope of the tangent line")
    ax.legend()
    save(fig, "tangent_line.png")


def partials_contour():
    x = np.linspace(-3, 3, 400)
    y = np.linspace(-3, 3, 400)
    X, Y = np.meshgrid(x, y)
    Z = X ** 2 + 3 * X * Y
    fig, ax = plt.subplots(figsize=(5.6, 5))
    cs = ax.contour(X, Y, Z, levels=15, cmap="viridis")
    ax.clabel(cs, inline=True, fontsize=8)
    px, py = 1.0, 2.0
    gx, gy = 2 * px + 3 * py, 3 * px            # (8, 3)
    n = np.hypot(gx, gy)
    ax.plot([px], [py], "o", color=RED)
    ax.annotate("", (px + gx / n, py + gy / n), (px, py),
                arrowprops=dict(arrowstyle="->", color=RED, lw=2))
    ax.text(px + 0.1, py + 0.15, r"$\nabla f=(8,3)$", color=RED)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(r"$f(x,y)=x^2+3xy$   with gradient at $(1,2)$")
    save(fig, "partials_contour.png")


def partial_slice():
    """A 2-D surface and the 1-D slice you get by moving along one axis."""
    x = np.linspace(-3, 3, 200)
    fig, ax = plt.subplots(figsize=(6, 4))
    y_fixed = 1.0
    f_along_x = x ** 2 + 3 * x * y_fixed          # f(x, 1)
    ax.plot(x, f_along_x, color=BLUE, lw=2,
            label=r"$f(x,\,y{=}1)=x^2+3x$")
    x0 = 1.0
    slope = 2 * x0 + 3 * y_fixed                   # partial wrt x at (1,1) = 5
    base = x0 ** 2 + 3 * x0 * y_fixed
    ax.plot(x, base + slope * (x - x0), color=RED, ls="--", lw=2,
            label=fr"tangent, slope $\partial f/\partial x = {slope:.0f}$")
    ax.plot([x0], [base], "o", color=RED)
    ax.set_xlabel("x")
    ax.set_ylabel("f")
    ax.set_title("A partial derivative is the slope along one axis")
    ax.legend()
    save(fig, "partial_slice.png")


def hyperplane_distance():
    fig, ax = plt.subplots(figsize=(5.6, 5))
    # line 3x + 4y - 5 = 0  ->  y = (5 - 3x)/4
    xs = np.linspace(-1, 6, 10)
    ax.plot(xs, (5 - 3 * xs) / 4, color=BLUE, lw=2, label=r"$w^\top x + b = 0$")
    p = np.array([4.0, 3.0])
    w = np.array([3.0, 4.0])
    b = -5.0
    signed = (w @ p + b) / np.hypot(*w)            # 19 / 5 = 3.8
    foot = p - signed * w / np.hypot(*w)
    ax.plot([p[0]], [p[1]], "o", color=RED)
    ax.text(p[0] + 0.15, p[1], "point x", color=RED)
    ax.plot([p[0], foot[0]], [p[1], foot[1]], color=RED, ls=":", lw=2)
    mid = (p + foot) / 2
    ax.text(mid[0] + 0.1, mid[1], f"distance = {signed:.1f}", color=RED)
    ax.annotate("", p + w / np.hypot(*w), p,
                arrowprops=dict(arrowstyle="->", color=GREY, lw=2))
    ax.text(*(p + w / np.hypot(*w) + 0.1), "w (normal)", color=GREY)
    ax.set_xlim(-1, 6)
    ax.set_ylim(-1, 6)
    ax.set_aspect("equal")
    ax.set_title("Distance from a point to a line/hyperplane")
    ax.legend(loc="upper right")
    save(fig, "hyperplane_distance.png")


def sigmoid_fig():
    z = np.linspace(-8, 8, 400)
    g = 1 / (1 + np.exp(-z))
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(z, g, color=BLUE, lw=2)
    for zz in (-2, 0, 2):
        gg = 1 / (1 + np.exp(-zz))
        ax.plot([zz], [gg], "o", color=RED)
        ax.annotate(fr"$\sigma({zz})={gg:.3f}$", (zz, gg),
                    (zz + 0.4, gg - 0.12), color=RED)
    ax.axhline(0.5, color=GREY, ls=":", lw=1)
    ax.axvline(0, color=GREY, ls=":", lw=1)
    ax.set_xlabel("z")
    ax.set_ylabel(r"$\sigma(z)$")
    ax.set_title(r"Sigmoid  $\sigma(z)=\dfrac{1}{1+e^{-z}}$")
    save(fig, "sigmoid.png")


def sigmoid_derivative_fig():
    z = np.linspace(-8, 8, 400)
    g = 1 / (1 + np.exp(-z))
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(z, g, color=BLUE, lw=2, label=r"$\sigma(z)$")
    ax.plot(z, g * (1 - g), color=ORANGE, lw=2,
            label=r"$\sigma'(z)=\sigma(z)\,(1-\sigma(z))$")
    ax.set_xlabel("z")
    ax.set_title("Sigmoid and its derivative")
    ax.legend()
    save(fig, "sigmoid_derivative.png")


def gaussian_fig():
    x = np.linspace(-6, 8, 400)

    def normal(x, mu, s):
        return np.exp(-((x - mu) ** 2) / (2 * s ** 2)) / (s * np.sqrt(2 * np.pi))

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x, normal(x, 0, 1), color=BLUE, lw=2, label=r"$\mu=0,\ \sigma=1$")
    ax.plot(x, normal(x, 2, 1), color=GREEN, lw=2, label=r"$\mu=2,\ \sigma=1$")
    ax.plot(x, normal(x, 0, 2), color=ORANGE, lw=2, label=r"$\mu=0,\ \sigma=2$")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title("Gaussian: mean shifts it, standard deviation widens it")
    ax.legend()
    save(fig, "gaussian.png")


def entropy_fig():
    p = np.linspace(1e-6, 1 - 1e-6, 400)
    H = -(p * np.log2(p) + (1 - p) * np.log2(1 - p))
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(p, H, color=BLUE, lw=2)
    for pp in (0.5, 0.9):
        HH = -(pp * np.log2(pp) + (1 - pp) * np.log2(1 - pp))
        ax.plot([pp], [HH], "o", color=RED)
        ax.annotate(f"p={pp}, H={HH:.2f}", (pp, HH), (pp - 0.02, HH - 0.18), color=RED)
    ax.set_xlabel("p  (fraction of the positive class)")
    ax.set_ylabel("entropy  H  (bits)")
    ax.set_title("Binary entropy: highest at a 50/50 split, zero when pure")
    save(fig, "entropy_binary.png")


def projection_fig():
    fig, ax = plt.subplots(figsize=(5.2, 5))
    wu = np.array([0.6, 0.8])          # unit vector along w
    w = wu * 4.5                       # display length for the w arrow
    x = np.array([1.0, 3.0])
    ax.annotate("", w, (0, 0), arrowprops=dict(arrowstyle="->", color=BLUE, lw=2))
    ax.text(w[0] * 1.02, w[1] * 1.02, "w", color=BLUE)
    ax.annotate("", x, (0, 0), arrowprops=dict(arrowstyle="->", color=GREEN, lw=2))
    ax.text(x[0] - 0.35, x[1] + 0.1, "x", color=GREEN)
    proj_len = x.dot(wu)
    proj = proj_len * wu
    ax.plot([x[0], proj[0]], [x[1], proj[1]], color=GREY, ls=":", lw=1.5)
    ax.annotate("", proj, (0, 0), arrowprops=dict(arrowstyle="->", color=RED, lw=3))
    ax.text(proj[0] + 0.15, proj[1] - 0.35,
            f"projection of x onto w\nlength = w·x / ||w|| = {proj_len:.1f}", color=RED)
    ax.set_xlim(-1, 4.5)
    ax.set_ylim(-1, 4.5)
    ax.set_aspect("equal")
    ax.set_title(r"$w\cdot x$ = (projection length) $\times\ \|w\|$")
    save(fig, "vector_projection.png")


def jensen_fig():
    x = np.linspace(0.3, 9.5, 400)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x, np.log(x), color=BLUE, lw=2, label=r"$\log x$ (concave)")
    x1, x2 = 1.0, 9.0
    ax.plot([x1, x2], [np.log(x1), np.log(x2)], "o-", color=RED,
            label="chord (average of the two points)")
    ax.plot([5], [np.log(5)], "s", color=GREEN)
    ax.plot([5], [0.5 * (np.log(x1) + np.log(x2))], "s", color=RED)
    ax.annotate(r"$\log(E[X])=1.61$", (5, np.log(5)), (5.2, 0.9), color=GREEN)
    ax.annotate(r"$E[\log X]=1.10$", (5, 0.5 * (np.log(x1) + np.log(x2))),
                (5.2, 0.2), color=RED)
    ax.set_xlabel("x")
    ax.set_title(r"Jensen: for a concave $f$,  $E[f(X)] \leq f(E[X])$")
    ax.legend(loc="lower right")
    save(fig, "jensen.png")


def markov_fig():
    days = np.arange(0, 8)
    P = np.array([[0.8, 0.2], [0.4, 0.6]])
    state = np.array([1.0, 0.0])
    hist = [state.copy()]
    for _ in days[1:]:
        state = state @ P
        hist.append(state.copy())
    hist = np.array(hist)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(days, hist[:, 0], "o-", color=ORANGE, label="P(Sunny)")
    ax.plot(days, hist[:, 1], "o-", color=BLUE, label="P(Rainy)")
    ax.axhline(2 / 3, color=ORANGE, ls=":", lw=1)
    ax.axhline(1 / 3, color=BLUE, ls=":", lw=1)
    ax.set_xlabel("day")
    ax.set_ylabel("probability")
    ax.set_title("Markov chain converges to a stationary distribution")
    ax.legend()
    save(fig, "markov_convergence.png")


if __name__ == "__main__":
    tangent_line()
    partials_contour()
    partial_slice()
    hyperplane_distance()
    sigmoid_fig()
    sigmoid_derivative_fig()
    gaussian_fig()
    entropy_fig()
    projection_fig()
    jensen_fig()
    markov_fig()
