import pandas as pd
import numpy as np

# Load covariance from 2.1 and correlation from 2.2
cov_matrix2_1 = pd.read_csv("testout_2.1.csv")
corr_matrix2_2 = pd.read_csv("testout_2.2.csv")

# Standard Deviations from diagonal of covariance matrix
std = np.sqrt(np.diag(cov_matrix2_1.to_numpy()))

# Reconstruct covariance from correlation and standard deviations
cov_matrix2_3 = corr_matrix2_2.to_numpy() * np.outer(std, std)

cov_matrix2_3_df = pd.DataFrame(cov_matrix2_3, columns=cov_matrix2_1.columns, index=cov_matrix2_1.index)

# Print the reconstructed covariance matrix
print(cov_matrix2_3_df)