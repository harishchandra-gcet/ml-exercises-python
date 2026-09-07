# Dot Products and Distance to a Hyperplane

## Dot Product as Projection Length
The dot product w · x gives the length of the projection of x onto the direction of w, scaled by the length of w.

Example:
```
w = [3, 4], x = [1, 1]

w · x = (3)(1) + (4)(1) = 7
||w|| = √(3² + 4²) = √25 = 5

Projection length = (w · x) / ||w|| = 7 / 5 = 1.4
```

## Distance from a Point to a Hyperplane
A hyperplane is defined by wᵀx + b = 0. The distance from a point to the hyperplane is:

```
distance = |wᵀx + b| / ||w||
```

Example:
```
w = [3, 4], b = -5, x = (4, 3)

wᵀx + b = (3)(4) + (4)(3) - 5 = 12 + 12 - 5 = 19
||w|| = 5

distance = 19 / 5 = 3.8
```

A support vector machine selects the hyperplane (w, b) that maximizes the smallest such distance across all data points, called the margin.
