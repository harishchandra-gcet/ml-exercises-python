# The Sigmoid Function

The sigmoid function maps any real number to a value between 0 and 1.

Formula:
```
g(z) = 1 / (1 + e^(-z))
```

Values:
```
g(0)  = 1 / (1 + e^0)  = 1 / 2      = 0.500
g(2)  = 1 / (1 + e^-2) = 1 / 1.135  = 0.881
g(-2) = 1 / (1 + e^2)  = 1 / 8.389  = 0.119
```

Properties:
- Large positive z produces an output close to 1.
- Large negative z produces an output close to 0.
- z = 0 produces an output of exactly 0.5.

The result is an S-shaped curve. In logistic regression, z = θᵀx, so the model output is a probability that increases smoothly as the weighted sum of the inputs increases.
