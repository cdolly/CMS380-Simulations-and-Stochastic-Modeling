"""
Poisson Deliverable

Cameron Dolly
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
import random


def simulate_binomial():
  n = 1000
  p = 0.025
  heads = sum(1 for i in range(n) if random.random() < p)
  return heads


# Simulate the binomial process 1000 times and record the number of heads in each trial
n = 1000
results = [simulate_binomial() for i in range(n)]

# Compute the frequency of each outcome
counts = np.bincount(results, minlength=n + 1)
freqs = counts / n

# Plot the frequency of each outcome
plt.plot(freqs, '-o', label='Binomial PMF')

# Plot the Poisson pmf with lambda = 25
lam = 25
x = np.arange(0, n + 1)
poissonPmf = poisson.pmf(x, lam)
plt.plot(poissonPmf, label=f'Poisson PMF (λ={lam})')

# Set plot labels and legend
plt.xlabel('Trials')
plt.ylabel('Probability')
plt.title('Binomial and Poisson PMFs')
plt.legend()
plt.savefig("BinomialSimulaton.pdf", bbox_inches="tight")
