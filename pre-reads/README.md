# CS229 Study Group — Pre-reads

These are short **"read this before the lecture"** notes. Each one takes 5–15
minutes and refreshes a single piece of **background mathematics** that an
upcoming lecture assumes you already know.

They deliberately contain **only the math** — linear algebra, calculus,
probability, a little information theory — and *not* the machine-learning ideas
built on top of it. The lectures do that part. The goal here is that when the
lecturer writes a gradient, a Gaussian, or a dot product on the board, none of the
notation is new.

### How to use them

1. Read the note for the upcoming lecture (see the table below).
2. Work through the numeric examples with a pen — don't just read them.
3. Try the **"Check yourself"** questions at the end of each note.
4. If a note still feels shaky, review that topic properly *before* the lecture.

### Reading index

| When | Note | Math it covers |
|---|---|---|
| Before Lecture 1 | [00_before_course_begins.md](00_before_course_begins.md) | Vectors, matrices, derivatives, probability — the whole baseline |
| Before Lecture 2 | [L02_partial_derivatives_gradient.md](L02_partial_derivatives_gradient.md) | Partial derivatives and the gradient vector |
| Before Lecture 3 | [L03_sigmoid_function.md](L03_sigmoid_function.md) | The logistic (sigmoid) function and its derivative |
| Lecture 4 | — | — |
| Before Lecture 5 | [L05_bayes_rule_gaussian.md](L05_bayes_rule_gaussian.md) | Bayes' rule and the Gaussian (normal) distribution |
| Before Lecture 6 | [L06_dot_products_svm_geometry.md](L06_dot_products_svm_geometry.md) | Dot products as projections; distance from a point to a hyperplane |
| Lectures 7–9 | — | — |
| Before Lecture 10 | [L10_entropy_decision_trees.md](L10_entropy_decision_trees.md) | Logarithms, entropy, and information |
| Lecture 11 | — | — |
| Before Lecture 12 | [L12_chain_rule_backprop.md](L12_chain_rule_backprop.md) | The chain rule through a chain of nested functions |
| Lecture 13 | — | — |
| Before Lecture 14 | [L14_jensens_inequality_em.md](L14_jensens_inequality_em.md) | Convex / concave functions and Jensen's inequality |
| Lectures 15–16 | — | — |
| Before Lecture 17 | [L17_markov_chains_mdp.md](L17_markov_chains_mdp.md) | Markov chains and stochastic (transition) matrices |
| Lectures 18–20 | — | — |

### Formatting notes

- Math is written with `$…$` / `$$…$$` and renders automatically on GitHub.
- Diagrams use [Mermaid](https://mermaid.js.org/) fenced code blocks, which GitHub
  renders inline.
- Plots live in [`figures/`](figures/) and are regenerated with:
  ```
  python pre-reads/figures/make_figures.py
  ```
