import pandas as pd

# Read input data
data = pd.read_csv('test1.csv')

# Only include rows with all values
data_complete = data.dropna()

# Calculate covariance matrix
cov_matrix = data_complete.cov()

# Print output
print(cov_matrix)