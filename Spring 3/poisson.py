"""
Poisson Deliverable

Cameron Dolly
"""
import matplotlib.pyplot as plt
import random


def simulate_binomial():
  n = 1000
  p = 0.025
  num_heads = 0
  for i in range(n):
    if random.random() < p:
      num_heads += 1
  return num_heads


def simulate_poisson(lam, k):

  # Definition of a poisson distribution
  #  Expected Value = Lamba
  # With lamba = 25 and k = 1000, over time the expected value would be lamba, or 25

  expectedValues = []
  for i in range(1, k + 1):
    expectedValues.append(lam)

  return expectedValues


# Simulate the binomial process 1000 times and record the number of heads in each trial
n = 1000
resultsBin = [simulate_binomial() for i in range(n)]
# Poisson pmf with lambda = 25
lam = 25
resultsPoisson = simulate_poisson(lam, n)

averagesBin = []
total = 0
for i in range(len(resultsBin)):
  total += resultsBin[i]
  averagesBin.append(total / (i + 1))

# Plot the frequency of outcomes
plt.plot(averagesBin, label='Binomial')

plt.plot(resultsPoisson, label=f'Poisson PMF (λ={lam})')

# Set plot labels and legend
plt.xlabel('Trials')
plt.ylabel('Number of Heads')
plt.title('Binomial and Poisson PMFs')
plt.legend()
plt.savefig("BinomialAndPoissonSimulaton.pdf", bbox_inches="tight")
