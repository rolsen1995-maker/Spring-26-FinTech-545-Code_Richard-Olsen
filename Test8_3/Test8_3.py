import numpy as np
from scipy.stats import t

# Load Data
data = np.genfromtxt("test7_2.csv", delimiter=",", skip_header=1)

# Fit T Distribution
df, loc, scale = t.fit(data)

alpha = 0.05
num_sims = 100000

# Simulate returns and compute VaR from simulation
sim = t.rvs(df, loc=loc, scale=scale, size=num_sims)
q_sim = np.quantile(sim, alpha)

var_absolute = -q_sim
var_diff_from_mean = var_absolute + loc


print("VaR Absolute, VaR Diff from Mean")
print(f"{var_absolute},{var_diff_from_mean}")