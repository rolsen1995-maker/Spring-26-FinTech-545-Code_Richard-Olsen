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

# Demeaned data
X_centered = X - mu

# Weighted covariance
cov_matrix = (weights[:, None, None] * np.einsum("ti,tj->tij", X_centered, X_centered)).sum(axis=0)

# Print results
cov_df = pd.DataFrame(cov_matrix, columns=data.columns, index=data.columns)
print(cov_df)