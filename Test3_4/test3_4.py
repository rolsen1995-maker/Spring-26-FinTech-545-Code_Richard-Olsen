import pandas as pd
import numpy as np 

def proj_psd(A: np.ndarray) -> np.ndarray:
    """Symmetric projection of A on the PSD cone."""
    A = (A + A.T) / 2
    vals, vecs = np.linalg.eigh(A)
    vals[vals < 0] = 0
    return vecs @ np.diag(vals) @ vecs.T


def proj_unit_diag(A) -> np.ndarray:
    """Force the diagonal of A to be 1."""
    A = (A + A.T) / 2
    np.fill_diagonal(A, 1.0)
    return (A + A.T) / 2


def higham_near_psd_cov(A: np.ndarray, max_iter: int = 1000, tol: float = 1e-12) -> np.ndarray:
    """
    Higham algorithm to find the nearest PSD covariance matrix, keeping original diagonal.
    """
    A = (A + A.T) / 2
    Y = A.copy()
    delta_S = np.zeros_like(A)
    prev_gamma = np.inf
    
    for _ in range(max_iter):
        R = Y - delta_S
        X = proj_psd(R)
        delta_S = X - R
        Y = proj_unit_diag(X)
        
        gamma = np.linalg.norm(Y - A, ord="fro")
        if abs(gamma - prev_gamma) < tol:
            break
        prev_gamma = gamma
        
    return (Y + Y.T) / 2

# Load correlation matrix from Test 1.4
df = pd.read_csv("testout_1.4.csv")
A_in = df.to_numpy()

A_out = higham_near_psd_cov(A_in)

# Print the resulting PSD matrix
print(pd.DataFrame(A_out, columns=df.columns))