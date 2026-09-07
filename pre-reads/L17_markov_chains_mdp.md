# Markov Chains

A Markov chain describes a system that moves between states, where the probability of the next state depends only on the current state.

Example, a two-state weather chain:
```
P(Sunny → Sunny) = 0.8      P(Sunny → Rainy) = 0.2
P(Rainy → Sunny) = 0.4      P(Rainy → Rainy) = 0.6
```

Starting from a Sunny day, the probability distribution over states after each day:
```
Day 0: [P(Sunny)=1, P(Rainy)=0]

Day 1:
P(Sunny) = 1*0.8 = 0.8
P(Rainy) = 1*0.2 = 0.2
→ [0.8, 0.2]

Day 2:
P(Sunny) = 0.8*0.8 + 0.2*0.4 = 0.64 + 0.08 = 0.72
P(Rainy) = 0.8*0.2 + 0.2*0.6 = 0.16 + 0.12 = 0.28
→ [0.72, 0.28]
```
After two days, starting from Sunny, the probability of Rain is 0.28. Each step is a matrix-vector multiplication of the current state distribution by the transition probabilities.

A Markov Decision Process extends this model by adding an action taken at each state and a reward received as a result. Value iteration and policy iteration are algorithms that compute the action to take at each state that maximizes total expected reward, using repeated updates of this form.
