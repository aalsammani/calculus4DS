# Getting Started

This chapter takes care of two practical matters before the mathematics begins: setting up Python, and learning to read the book's visual conventions.

## Setting up Python

The book uses standard scientific Python throughout: **NumPy** for arrays and numerical computation {cite}`harris2020numpy`, **Matplotlib** for plots {cite}`hunter2007matplotlib`, **SymPy** for exact symbolic mathematics {cite}`meurer2017sympy`, and occasionally **SciPy** {cite}`virtanen2020scipy` when a well-tested numerical routine is genuinely the right tool. Nothing else is required.

Two setup routes work equally well.

**Route 1: local installation.** Install Python 3.10 or later from [python.org](https://www.python.org) or via [Anaconda](https://www.anaconda.com/download), then in a terminal:

```bash
pip install numpy scipy sympy matplotlib jupyterlab
jupyter lab
```

**Route 2: no installation.** Open [Google Colab](https://colab.research.google.com) in a browser. Every package the book uses is preinstalled there, and each notebook page in this book carries a launch button that opens it directly in Colab.

Verify your setup by running this cell. It exercises each library once:

```python
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x = sp.symbols('x')
print(sp.diff(x**2, x))          # symbolic derivative: expect 2*x
print(np.dot([1, 2], [3, 4]))    # dot product: expect 11

plt.plot(np.linspace(0, 1, 50) ** 2)
plt.title("If you can see a parabola, you are ready.")
plt.show()
```

If the two printed lines read `2*x` and `11` and a curve appears, you are ready.

## Reading the book: visual conventions

The book uses a small, fixed set of colored panels. Each has one job.

```{prf:definition} What a definition panel looks like
:label: def-demo
Definition panels state the precise meaning of a term. Everything else in the book is built on these, so read them slowly.
```

```{prf:theorem} What a theorem panel looks like
:label: thm-demo
Theorem panels state results that are always true (under their stated hypotheses) and that you will use repeatedly.
```

```{prf:example} What a worked example looks like
:label: ex-demo
Worked examples show complete solutions with every intermediate step. They come in graded sequences: fundamental first, then intermediate, then applied or conceptual.
```

```{admonition} Common Mistakes
:class: warning
Warning panels flag errors that students make so predictably that naming them in advance prevents most of them. When you catch yourself mid-mistake and remember one of these panels, the panel has done its job.
```

```{admonition} Data Science Connection
:class: tip
These short panels explain why a concept matters for quantitative and data science work — why derivatives measure sensitivity, why matrices hold datasets, why Taylor polynomials power numerical libraries. They motivate; they do not turn this into a machine learning course.
```

```{admonition} Looking Ahead
:class: seealso
These panels point to where an idea reappears in later chapters or later courses, so you know which investments pay off where.
```

Hints and solutions to exercises live behind collapsible panels:

````{admonition} Hint
:class: dropdown
Click a panel like this one only after a genuine attempt. Hints nudge; they do not solve.
````

````{admonition} Solution
:class: dropdown
Solution panels show complete reasoning, not just answers. Compare your work line by line, not merely your final number.
````

## Exercise tiers

Every section ends with exercises in a consistent progression:

**Quick Check** — one-line questions testing whether you absorbed the definitions. **Basic Practice** — direct application of a rule or formula. **Intermediate Practice** — multi-step problems combining ideas. **Conceptual Understanding** — explain, compare, or interpret. **Python Practice** — short computations reinforcing the mathematics. **Visualization Practice** — draw and investigate. **Challenge** — for readers who want more. Chapter-ending **Cumulative Review** problems deliberately reach back to earlier chapters, because mathematical skill decays without spaced retrieval.

You do not need to do every exercise. You do need to do exercises from every tier you intend to be tested on — reading mathematics is not the same as being able to produce it.

## A note on calculators and computers

In this course Python plays the role a good lab plays in a science course. The rule the book follows, and the rule you should follow, is: **hand first, machine second.** Every Python segment is preceded by the same computation done manually, and the code's first job is always to confirm the hand result. When the two disagree, one of them is wrong, and finding out which is one of the most instructive things you can do.
