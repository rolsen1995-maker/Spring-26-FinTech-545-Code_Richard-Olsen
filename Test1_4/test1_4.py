import pandas as pd

# Load the data, keep everything, including missing values
data = pd.read_csv("test1.csv")

# Pairwise correlation 
corr_matrix = data.corr()

# Print the correlation matrix
print(corr_matrix)