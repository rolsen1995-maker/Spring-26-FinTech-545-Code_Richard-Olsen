import pandas as pd

# Import the data
data = pd.read_csv("test1.csv")

# Remove rows with missing values
data_complete = data.dropna()

# Calculate the covariance matrix
cov_matrix = data_complete.cov()

# Convert covariance to correlation 
corr_matrix = cov_matrix.corr()

# Print the result 
print(corr_matrix)