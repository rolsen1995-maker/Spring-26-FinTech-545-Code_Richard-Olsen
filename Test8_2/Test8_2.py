import numpy as np
from scipy.stats import t

# Load Data
data = np.genfromtxt("test7_2.csv", delimiter=",", skip_header=1)

# Fit a T Distribution to data
df, loc, scale = t.fit(data)

# 95% VaR
alpha = 0.05
q = t.ppf(alpha, df, loc=loc, scale=scale)

var_absolute = -q
var_diff_from_mean = var_absolute + loc

print("VaR Absolute, VaR Diff from Mean")
print(f"{var_absolute},{var_diff_from_mean}")