# Entropy

Entropy measures the impurity, or uncertainty, of a set of labels.

Formula:
```
H(S) = -Σ pᵢ log₂(pᵢ)
```
A value of 0 indicates a perfectly pure set (all one class). Higher values indicate a more mixed set.

Example 1, an evenly split set:
```
p(yes) = 0.5, p(no) = 0.5

H = -[0.5 * log₂(0.5) + 0.5 * log₂(0.5)]
  = -[0.5*(-1) + 0.5*(-1)]
  = 1.0 bit
```

Example 2, a mostly uniform set (9 positive, 1 negative out of 10):
```
p(yes) = 0.9, p(no) = 0.1

H = -[0.9 * log₂(0.9) + 0.1 * log₂(0.1)]
  = -[0.9*(-0.152) + 0.1*(-3.322)]
  = -[-0.137 - 0.332]
  = 0.469 bits
```

Decision trees select each split by computing information gain, the reduction in entropy produced by that split. A split producing mostly pure groups, as in Example 2, has higher information gain than one leaving the data mixed, as in Example 1.
