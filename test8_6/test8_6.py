import csv
import math
import numpy as np
from scipy import stats

ALPHA = 0.05
N_SIM = 100000

# Read input data from test7_2.csv
x = []
with open("test7_2.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        x.append(float(row["x1"]))
        
# Fit T-Distribution returning (df, loc, scale)
df, loc, scale = stats.t.fit(x)

# Simulate from T-Distribution
sims = stats.t.rvs(df, loc=loc, scale=scale, size=N_SIM)

# Empirical ES lower tail
sims_sorted = np.sort(sims)
k = int(np.ceil(ALPHA * len(sims_sorted)))
es = sims_sorted[:k].mean()

es_absolute = abs(es)
sim_mean = sims.mean()
es_diff_from_mean = abs(es - sim_mean)

print("ES Absolute,ES Diff from Mean")
print(f"{es_absolute},{es_diff_from_mean}")