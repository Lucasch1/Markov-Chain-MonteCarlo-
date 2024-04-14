import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def f(x):
    return 0.5 * np.exp(-np.abs(x))


def metropolis_hastings(N, s):
    x = np.zeros(N)
    x[0] = np.random.normal(0, 1)

    for i in range(1, N):
        x_star = np.random.normal(x[i-1], s)
        r = f(x_star) / f(x[i-1])
        u = np.random.uniform(0, 1)

        if np.log(u) < np.log(r):
            x[i] = x_star
        else:
            x[i] = x[i-1]
    return x


# Sample
N = 10000
s = 1

samples = metropolis_hastings(N, s)

# Plot - Histogram
plt.hist(samples, bins=50, density=True, alpha=0.5, label='Histogram')

# Plot - kernel density
kde = norm(np.mean(samples), np.std(samples)).pdf
x_vals = np.linspace(-10, 10, 100)
plt.plot(x_vals, kde(x_vals), color='red', label='Kernel Density Plot')

# Probability density function
plt.plot(x_vals, f(x_vals), color='green', label='f(x)')
plt.legend()
plt.xlabel('x')
plt.ylabel('Density')
plt.title('Histogram and kernel Density Plot')
plt.show()

# Mean and standard deviation
sample_mean = np.mean(samples)
sample_std = np.std(samples)
print('Mean:', sample_mean)
print('Standard deviation:', sample_std)

# Function to calculate the Rb


def calculate_Rb(N, s, J):
    chains = []
    chainsMean = []
    chainsVar = []
    for i in range(J):
        chains.append(metropolis_hastings(N, s))
        chainsMean.append(np.mean(chains[i]))
        chainsVar.append(np.var(chains[i]))
    overallMean = np.mean(chainsMean)
    overalVar = np.mean(chainsVar)
    sum = 0
    for i in range(J):
        sum += (chainsMean[i] - overallMean)**2

    b = sum/J

    r = np.sqrt((b + overalVar) / overalVar)

    return r


# Rb = calculate_Rb(N=2000, s=0.001, J=4)
Rbs = []
sS = []

for s in np.arange(0.001, 1, 0.01):
    Rb = calculate_Rb(N=2000, s=s, J=4)
    print('Rb:', Rb)
    Rbs.append(Rb)
    sS.append(s)
plt.plot(sS, Rbs)
plt.xlabel('s')
plt.ylabel('R Values')
plt.title('R values VS s')
plt.show()

# print('Rb:', Rb)
