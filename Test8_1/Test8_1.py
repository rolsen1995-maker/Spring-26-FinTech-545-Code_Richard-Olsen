import numpy as np
from statistics import NormalDist

# Input Data
data = np.genfromtxt("test7_1.csv", delimiter=",", skip_header=1)

# Normal Data Parameters
mu = np.mean(data)
sigma = np.std(data, ddof=1)

# 95% VaR
alpha = 0.05
z = NormalDist().inv_cdf(alpha)

# VaR calculations
var_absolute = -(mu + sigma * z)
var_diff_from_mean = var_absolute + mu

print("VaR Absolute, VaR Diff from Mean")
print(f"{var_absolute},{var_diff_from_mean}")