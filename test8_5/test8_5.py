import csv
import math
from scipy import stats

ALPHA = 0.05

# Read input data from test7_2.csv
x = []
with open("test7_2.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        x.append(float(row["x1"]))
        
# Fit T-Distribution returning (df, loc, scale)
df, loc, scale = stats.t.fit(x)

# Expected shortfall from T distribution
q = stats.t.ppf(ALPHA, df)
pdf_q = stats.t.pdf(q, df)

numerator = df + q**2
denominator = df - 1

es_std = -(numerator / denominator) * (pdf_q / ALPHA)

# Transform to original fitted location/scale
es = loc + scale * es_std

es_absolute = abs(es)
es_diff_from_mean = abs(es - loc)

print("ES Absolute,ES Diff from Mean")
print(f"{es_absolute:.6f},{es_diff_from_mean:.6f}")