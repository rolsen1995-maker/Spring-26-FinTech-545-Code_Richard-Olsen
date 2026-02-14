import numpy as np

# Read input data
cov_matrix = np.genfromtxt("test5_1.csv", delimiter=",", skip_header=1)

if cov_matrix.shape != (5, 5):
    raise ValueError("Expected a 5x5 covariance matrix")

# Simulation Rules
mean = np.zeros(5)
num_sims = 100000

# Run simulation, multivariate normal
simulated_data = np.random.multivariate_normal(mean, cov_matrix, num_sims)

# Compute covariance sample 
sample_cov = np.cov(simulated_data, rowvar=False)

print("Sample covariance matrix:")
print(sample_cov)