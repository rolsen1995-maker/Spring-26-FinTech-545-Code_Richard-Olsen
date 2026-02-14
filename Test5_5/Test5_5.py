import numpy as np

# Read input data
cov = np.genfromtxt("test5_2.csv", delimiter=",", skip_header=1)
if cov.shape != (5, 5):
    raise ValueError("Expected a 5x5 covariance matrix")

# Eigen decomposition
eigvals, eigvecs = np.linalg.eigh(cov)

# Sort eiganvalues/vectors descending
idx = np.argsort(eigvals)[::-1]
eigvals = eigvals[idx]
eigvecs = eigvecs[:, idx]

# 99% Explanation 
total_var = eigvals.sum()
var_ratio = np.cumsum(eigvals) / total_var
k = np.searchsorted(var_ratio, 0.99) + 1

eigvals_k = eigvals[:k]
eigvecs_k = eigvecs[:, :k]

# Simulation Rules
mean = np.zeros(k)
num_sims = 100000

# Simulate PCA space
sim_pca = np.random.multivariate_normal(mean, np.diag(eigvals_k), num_sims)

# Transform to original space
sim_data = sim_pca @ eigvecs_k.T

# Output
sample_cov = np.cov(sim_data, rowvar=False)

print("Sample covariance matrix:")
print(sample_cov)