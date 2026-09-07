# Mathematical Foundations for CS229

## 1. Linear Algebra

### Vectors
A vector is an ordered list of numbers, representing a point or direction in space. Vectors are typically written as columns of numbers.

Example:
```
a = [1, 2, 3]
```

### Dot Product
The dot product of two vectors of equal length is computed by multiplying corresponding entries and summing the results.

Formula:
```
a · b = a1*b1 + a2*b2 + ... + an*bn
```

Example:
```
a = [1, 2, 3], b = [4, 5, 6]
a · b = (1)(4) + (2)(5) + (3)(6) = 4 + 10 + 18 = 32
```

The dot product measures the similarity in direction between two vectors and is used to compute weighted sums of inputs, which appear throughout linear and logistic regression.

### Matrices
A matrix is a rectangular array of numbers arranged in rows and columns. A matrix with m rows and n columns is called an m x n matrix.

### Matrix-Vector Multiplication
When a matrix is multiplied by a vector, each row of the matrix is dotted with the vector to produce one entry of the output.

Example:
```
X = [[1, 2],
     [1, 3]]

θ = [2, 1]

Xθ = [(1)(2)+(2)(1), (1)(2)+(3)(1)] = [4, 5]
```

In CS229, X is called the design matrix. Each row of X represents one training example, and each column represents one feature. θ is the parameter (weight) vector. The product Xθ produces a prediction for every training example in a single operation.

A second example with three features per example (the first column is a constant 1, used as a bias term):
```
X = [[1, 2, 3],
     [1, 0, 1]]

θ = [1, 2, -1]

Row 1: (1)(1) + (2)(2) + (3)(-1) = 1 + 4 - 3 = 2
Row 2: (1)(1) + (0)(2) + (1)(-1) = 1 + 0 - 1 = 0

Xθ = [2, 0]
```

### Transpose
The transpose of a matrix flips its rows and columns. If X is m x n, then Xᵀ is n x m.

Example:
```
X  = [[1, 2],
      [1, 3]]

Xᵀ = [[1, 1],
      [2, 3]]
```

### XᵀX
The product XᵀX appears in the closed-form solution for linear regression. It converts a rectangular matrix into a square matrix.

Example, using the X above:
```
XᵀX = [[1,1],       [[1,2],
        [2,3]]   x    [1,3]]

Row 1: (1)(1)+(1)(1)=2 ,  (1)(2)+(1)(3)=5
Row 2: (2)(1)+(3)(1)=5 ,  (2)(2)+(3)(3)=13

XᵀX = [[2, 5],
       [5, 13]]
```

## 2. Calculus

### Derivative
The derivative of a function measures its rate of change: the slope of the function at a given point.

Power rule: if f(x) = x^n, then f'(x) = n * x^(n-1)

Example:
```
f(x) = x²
f'(x) = 2x
At x = 3: f'(3) = 2(3) = 6
```
At x = 3, the function is increasing at a rate of 6 units of output per unit of input.

### Partial Derivatives (preview)
When a function has more than one input variable, a partial derivative measures the rate of change with respect to one variable while holding the others fixed. This is covered in full before Lecture 2.

### Chain Rule
The chain rule computes the derivative of a composite function: one function nested inside another. It states that the derivative equals the derivative of the outer function (evaluated at the inner function) multiplied by the derivative of the inner function.

Formula: if f(x) = h(g(x)), then f'(x) = h'(g(x)) * g'(x)

Example:
```
f(x) = (3x + 1)²
Let g(x) = 3x + 1, h(u) = u²
h'(u) = 2u

f'(x) = h'(g(x)) * g'(x) = 2(3x+1) * 3 = 6(3x+1)

At x = 1: f'(1) = 6(3(1)+1) = 6(4) = 24
```

A second example:
```
f(x) = e^(2x)
Let g(x) = 2x, h(u) = e^u
f'(x) = h'(g(x)) * g'(x) = e^(2x) * 2 = 2e^(2x)

At x = 0: f'(0) = 2e^0 = 2
```

The chain rule is applied repeatedly in backpropagation, where a loss function depends on several nested layers of computation.

## 3. Probability

### Random Variables
A random variable represents the outcome of a random process. It can be discrete (for example, a die roll) or continuous (for example, a height measurement).

### Probability Notation
P(x) denotes the probability of event x. Probabilities range from 0 (impossible) to 1 (certain), and the probabilities of all possible outcomes of a random variable sum to 1.

Example:
```
A fair six-sided die has outcomes {1,2,3,4,5,6}, each with P(x) = 1/6.
```

### Expectation
The expected value, E[X], is the long-run average value of a random variable, weighted by probability.

Formula:
```
E[X] = Σ x * P(x)
```

Example:
```
E[X] for a fair die = (1)(1/6)+(2)(1/6)+(3)(1/6)+(4)(1/6)+(5)(1/6)+(6)(1/6)
= (1+2+3+4+5+6)/6 = 21/6 = 3.5
```

### Conditional Probability
Conditional probability, P(A|B), is the probability of event A occurring given that event B has already occurred.

Formula:
```
P(A|B) = P(A ∩ B) / P(B)
```

Example, rolling a fair die:
```
A = "the roll is even" = {2,4,6}
B = "the roll is greater than 3" = {4,5,6}
A ∩ B = {4,6}

P(B) = 3/6 = 0.5
P(A ∩ B) = 2/6 = 0.333

P(A|B) = 0.333 / 0.5 = 0.667
```

A second example, drawing one card from a standard 52-card deck:
```
A = "card is a King" (4 outcomes)
B = "card is a face card" (12 outcomes: J, Q, K in each of 4 suits)
A ∩ B = "card is a King" (4 outcomes, since every King is a face card)

P(B) = 12/52 = 0.231
P(A ∩ B) = 4/52 = 0.077

P(A|B) = 0.077 / 0.231 = 0.333
```

### Independence
Two events are independent if the occurrence of one does not change the probability of the other:
```
P(A|B) = P(A)
```
This assumption underlies the "naive" independence assumption in Naive Bayes classifiers.

---

Additional topics used later in the course, including Bayes' theorem, the Gaussian distribution, entropy, and Markov chains, are covered in separate notes placed before the lectures that use them.
