import numpy as np

# Read input data
cov = np.genfromtxt("test5_3.csv", delimiter=",", skip_header=1)
if cov.shape != (5, 5):
    raise ValueError("Expected a 5x5 covariance matrix")

# PSD Fix
eigvals, eigvecs = np.linalg.eigh(cov)
eigvals[eigvals < 0] = 0
cov_fixed = eigvecs @ np.diag(eigvals) @ eigvecs.T

# Simulation Rules
mean = np.zeros(5)
num_sims = 100000

# Run fixed covariance simulation
simulated_data = np.random.multivariate_normal(mean, cov_fixed, num_sims)

# Compute covariance output
sample_cov = np.cov(simulated_data, rowvar=False)

print("Sample covariance matrix")
print(sample_cov)