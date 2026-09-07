# Chain Rule Through Multiple Steps

Backpropagation applies the chain rule across a sequence of computations. The following is a single-neuron example.

Setup: input x = 1, weight w = 0.5, target output y = 1.

Forward pass:
```
z = w * x = 0.5 * 1 = 0.5
a = sigmoid(z) = 1/(1+e^-0.5) = 0.622
L = (a - y)² = (0.622 - 1)² = 0.143
```
L is the loss, measuring the error between prediction and target.

Backward pass, computing dL/dw one link at a time:
```
dL/da = 2(a - y) = 2(0.622 - 1) = -0.756

da/dz = a(1 - a) = 0.622 * 0.378 = 0.235

dz/dw = x = 1

dL/dw = dL/da * da/dz * dz/dw
      = (-0.756) * (0.235) * (1)
      = -0.178
```

dL/dw gives the direction and magnitude used to update the weight: w := w - α * dL/dw. This is the chain rule applied across three steps rather than two. In a full network, the same pattern repeats across every layer, computed backward from the loss toward the input, which is the origin of the term backpropagation.
