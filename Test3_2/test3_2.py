import pandas as pd
import numpy as np

# Load correlation matrix from Test 1.4
C = pd.read_csv("testout_1.4.csv").to_numpy()

# Eigen decomposition
vals, vecs = np.linalg.eigh(C)

# Negative eigenvalues set to zero
vals[vals < 0] = 0

# Rebuild PSD matrix
C_psd = vecs @ np.diag(vals) @ vecs.T

# Fix the diagnol to 1
d = np.sqrt(np.diag(C_psd))
C_psd = C_psd / np.outer(d, d)

# Print the resulting PSD matrix
cols = ["x1", "x2", "x3", "x4", "x5"]
print(pd.DataFrame(C_psd, columns=cols))