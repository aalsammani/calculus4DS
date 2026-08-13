"""Shared Matplotlib style for every figure in the CSCI 504 textbook.

Import this module at the top of each figure script:

    from bookstyle import apply_style, savefig, COLORS

The palette is colorblind-safe (based on the Okabe-Ito palette), and all
figures use the same fonts, line weights, and grid so the book has a
consistent visual identity.
"""

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt

# Okabe-Ito colorblind-safe palette.
COLORS = {
    "blue": "#0072B2",
    "orange": "#E69F00",
    "green": "#009E73",
    "red": "#D55E00",
    "purple": "#CC79A7",
    "sky": "#56B4E9",
    "yellow": "#F0E442",
    "gray": "#666666",
}

BOOK_ROOT = Path(__file__).resolve().parents[2] / "book"


def apply_style() -> None:
    """Set global rcParams for a clean, readable textbook look."""
    mpl.rcParams.update(
        {
            "figure.figsize": (7.0, 4.2),
            "figure.dpi": 110,
            "savefig.dpi": 160,
            "savefig.bbox": "tight",
            "font.size": 11,
            "font.family": "DejaVu Sans",
            "mathtext.fontset": "dejavusans",
            "axes.titlesize": 12,
            "axes.labelsize": 11,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": True,
            "grid.alpha": 0.25,
            "grid.linewidth": 0.6,
            "lines.linewidth": 2.0,
            "legend.frameon": False,
        }
    )


def savefig(fig, part: str, name: str) -> Path:
    """Save a figure into book/<part>/figures/<name>.png and report the path."""
    outdir = BOOK_ROOT / part / "figures"
    outdir.mkdir(parents=True, exist_ok=True)
    path = outdir / f"{name}.png"
    fig.savefig(path)
    plt.close(fig)
    print(f"wrote {path.relative_to(BOOK_ROOT.parent)}")
    return path
