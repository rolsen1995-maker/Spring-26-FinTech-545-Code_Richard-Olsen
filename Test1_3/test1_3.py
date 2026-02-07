import pandas as pd

# Load the data, keep everything, including missing values
data = pd.read_csv("test1.csv")

# Calculate the covariance matrix using pairwise complete observations
cov_matrix = data.cov()

# Print the results 
print(cov_matrix)