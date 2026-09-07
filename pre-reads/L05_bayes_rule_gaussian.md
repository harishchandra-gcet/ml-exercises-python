# Bayes' Rule and the Gaussian Distribution

## Bayes' Rule

Formula:
```
P(A|B) = P(B|A) * P(A) / P(B)
```

Example, a medical test:
```
Disease prevalence: P(D) = 0.01
Test sensitivity: P(positive | D) = 0.99
False positive rate: P(positive | not D) = 0.05

P(positive) = P(positive|D)*P(D) + P(positive|not D)*P(not D)
            = (0.99)(0.01) + (0.05)(0.99)
            = 0.0099 + 0.0495
            = 0.0594

P(D|positive) = P(positive|D)*P(D) / P(positive)
              = 0.0099 / 0.0594
              = 0.167
```
A positive result on a 99%-accurate test corresponds to roughly 16.7% actual probability of disease, because the base rate of the disease is low.

## The Gaussian (Normal) Distribution

Formula, standard case with mean 0 and variance 1:
```
f(x) = (1 / √(2π)) * e^(-x²/2)
```

Values:
```
f(0) = (1/2.507) * e^0    = 0.399
f(1) = (1/2.507) * e^-0.5 = 0.242
```

The Gaussian distribution is a symmetric bell-shaped curve, highest at the mean and decreasing on either side. Gaussian Discriminant Analysis assumes the features of each class follow this distribution, with a separate mean per class, and classifies a new point according to which class's distribution assigns it higher probability.
