import numpy as np

# Read Input Data
cov = np.genfromtxt("test5_3.csv", delimiter=",", skip_header=1)
if cov.shape != (5, 5):
    raise ValueError("Expected a 5x5 covariance matrix")

def higham_psd(a, max_iter=100, tol=1e-10):
    a = (a + a.T) / 2
    diag_target = np.diag(a).copy()
    
    y = a.copy()
    delta_s = np.zeros_like(a)
    
    for _ in range(max_iter):
        y_prev = y.copy()
        
        r = y - delta_s
        
        # Project to PSD cone 
        w, v = np.linalg.eigh(r)
        w[w < 0] = 0
        x = v @ np.diag(w) @ v.T
        
        delta_s = x -r
        
        # Project to matrices with original diagonal
        y = x.copy()
        np.fill_diagonal(y, diag_target)
        y = (y + y.T) / 2
        
        if np.linalg.norm(y - y_prev, ord="fro") <= tol * np.linalg.norm(y_prev, ord="fro"):
            break
        
        
    return y

# Higham fix
cov_fixed = higham_psd(cov)

# Simulation Rules
mean = np.zeros(5)
num_sims = 100000

# Run fixed covariance simulation
simulated_data = np.random.multivariate_normal(mean, cov_fixed, num_sims)

# Compute covariance
sample_cov = np.cov(simulated_data, rowvar=False)

print("Sample covariance matrix:")
print(sample_cov)