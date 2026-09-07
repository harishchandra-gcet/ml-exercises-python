# Jensen's Inequality

For a concave function f, such as the logarithm, the average of the function is less than or equal to the function of the average:
```
E[f(X)] ≤ f(E[X])
```
For a convex function, the inequality is reversed.

Example: X takes value 1 with probability 0.5 and value 9 with probability 0.5.
```
E[X] = 0.5(1) + 0.5(9) = 5
log(E[X]) = log(5) = 1.609

E[log X] = 0.5*log(1) + 0.5*log(9)
         = 0.5*0 + 0.5*2.197
         = 1.099
```
Result: E[log X] = 1.099, which is less than or equal to log(E[X]) = 1.609.

The Expectation-Maximization algorithm needs to maximize a log-likelihood containing a log of a sum, which is difficult to optimize directly. Jensen's inequality is used to construct a lower bound on this quantity by swapping the log and the expectation, and that lower bound is maximized instead.
