import csv
import math
from statistics import mean, stdev, NormalDist

ALPHA = 0.05

# Read input data from test7_1.csv
x = []
with open("test7_1.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        x.append(float(row["x1"]))

# Fit normal distrubution
mu = mean(x)
sigma = stdev(x)

# Expected Shortfall (ES) lower tail 
z = NormalDist().inv_cdf(ALPHA)
phi = math.exp(-0.5 * z *z) / math.sqrt(2 * math.pi)
es = mu - sigma * (phi / ALPHA)

# Results
es_absolute = abs(es)
es_diff_from_mean = abs(es - mu)

print("ES Absolute,ES Diff from Mean")
print(f"{es_absolute},{es_diff_from_mean}")