import pandas as pd
import numpy as np


def chol_psd(A: np.ndarray, eps: float = 1e-12) -> np.ndarray:
    """
    Cholesky-like root for PSD matrices. If diagonal pivot is ~=0, set that column to 0.
    """
    A = np.array(A, dtype=float)
    A = (A + A.T) / 2
    
    n = A.shape[0]
    L = np.zeros((n, n), dtype=float)
    
    for j in range(n):
        # Diagonal
        s = 0.0
        for k in range(j):
            s += L[j, k] * L[j, k]
            
        d = A[j, j] - s
        
        if d < 0 and abs(d) <= eps:
            d = 0.0
            
        if d <= 0.0:
            # PSD case: pivot is 0 => set entire column to 0
            L[j, j] = 0.0
            for i in range(j + 1, n):
                L[i, j] = 0.0
            continue
        
        L[j, j] = np.sqrt(d)
        
        for i in range(j + 1, n):
            s = 0.0
            for k in range(j):
                s += L[i, k] * L[j, k]
                
            num = A[i, j] - s
            L[i, j] = num / L[j, j]
            
    return L


df = pd.read_csv("testout_3.1.csv")
A = df.to_numpy()

L = chol_psd(A)

print(pd.DataFrame(L, columns=df.columns))