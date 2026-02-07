import pandas as pd 
import numpy as np

# Load the data
data = pd.read_csv('test2.csv')

# EWMA decay factor
lam = 0.97

# Observations
T = len(data)

# Create EWMA weights
weights = np.array([(1 - lam) * (lam ** (T - 1 - t)) for t in range(T)])
weights = weights / weights.sum()

# Numpy conversion
X = data.to_numpy()

# Weighted mean
mu = (weights[:, None] * X).sum(axis=0)

# Demean
Xc = X - mu

# Weighted variances
var = (weights[:, None] * (Xc ** 2)).sum(axis=0)
std = np.sqrt(var)

# Standardize
Z = Xc / std

# Weighted correlation matrix
corr_matrix = (weights[:, None, None] * np.einsum("ti,tj->tij", Z, Z)).sum(axis=0)

# Print results
corr_df = pd.DataFrame(corr_matrix, columns=data.columns, index=data.columns)
print(corr_df)