"""
Poisson Deliverable

Cameron Dolly
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson


# Define function to simulate binomial process
def simulateBinomial():
  # Set number of trials and probability of success
  n = 1000
  p = 0.025
  # Generate 1000 binomial trials and return outcomes
  outcomes = np.random.binomial(n, p, size=1000)
  return outcomes


# Simulate binomial process and count outcomes
results = simulateBinomial()
counts = np.bincount(results)
# Calculate fraction of trials for each outcome
fractions = counts / 1000

# Generate x-values for Poisson pmf
x = np.arange(0, 1001)
# Calculate Poisson pmf with lambda = 25
poissonPMF = poisson.pmf(x, mu=25)

# Plot bar chart of binomial fractions and Poisson pmf
plt.bar(range(len(fractions)), fractions, label="Binomial")
plt.plot(x, poissonPMF, 'r-', label="Poisson")
# Set x-axis limits to zoom in on part around 25
plt.xlim([0, 75])
plt.xlabel("Number of Heads")
plt.ylabel("Fraction of Trials / Probability")
plt.title("Binomial Process Simulation and Poisson PMF")
plt.legend()
plt.savefig('BinomialAndPoissonSimulaton.pdf', bbox_inches="tight")
