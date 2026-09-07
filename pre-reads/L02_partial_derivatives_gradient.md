# Partial Derivatives and the Gradient

## Partial Derivative
For a function of multiple variables, a partial derivative is the derivative taken with respect to one variable while holding all other variables constant.

Example:
```
f(x, y) = x² + 3xy

∂f/∂x = 2x + 3y
∂f/∂y = 3x

At (x, y) = (1, 2):
∂f/∂x = 2(1) + 3(2) = 8
∂f/∂y = 3(1) = 3
```

## Gradient
The gradient of a function, written ∇f, is a vector containing all of its partial derivatives. It points in the direction of steepest increase of the function.

```
∇f(1, 2) = [8, 3]
```

## Gradient Descent
Gradient descent is an optimization method that updates parameters by moving in the direction opposite the gradient.

```
θ := θ - α∇f(θ)
```

α is the learning rate, controlling the size of each step. This update rule is used to minimize the cost function in linear regression.
