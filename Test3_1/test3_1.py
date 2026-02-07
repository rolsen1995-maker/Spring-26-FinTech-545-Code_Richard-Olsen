import pandas as pd
import numpy as np

# load covariance (from 1.3)
A = pd.read_csv("testout_1.3.csv").to_numpy()

# convert covariance -> correlation
std = np.sqrt(np.diag(A))
corr = A / np.outer(std, std)

# eigenvalue clip on correlation
vals, vecs = np.linalg.eigh(corr)
vals[vals < 0] = 0
corr_psd = vecs @ np.diag(vals) @ vecs.T

# force diagonal back to 1 (renormalize)
d = np.sqrt(np.diag(corr_psd))
corr_psd = corr_psd / np.outer(d, d)

# convert back to covariance using original std devs
A_psd = corr_psd * np.outer(std, std)

cols = ["x1", "x2", "x3", "x4", "x5"]
print(pd.DataFrame(A_psd, columns=cols))