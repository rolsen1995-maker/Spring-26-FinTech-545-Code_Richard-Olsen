# Test 7_3 Assignment 
# Write a function for a T regression and ensure your output is expected. 

# There will be scratch code used during development
# Function will be at the bottom of the file

# Load inputs from source file, seperate X and Y

"""
import numpy as np

file_name = "test7_3.csv"
file = open(file_name, "r")
lines = file.readlines()
file.close()

X = []
Y = []

for line in lines[1:]:
    parts = line.strip().split(",")
    
    x1 = float(parts[0])
    x2 = float(parts[1])
    x3 = float(parts[2])
    Y_value = float(parts[3])
    
    x_row = [x1, x2, x3]
    y_value = Y_value
    
    X.append(x_row)
    Y.append(y_value)
    
print("Number of observations:", len(X))
print("First X row:", X[0])
print("First Y value:", Y[0])

# T Regression using a package

import statsmodels.api as sm
from statsmodels.miscmodels.tmodel import TLinearModel

# Convert list to arrays
X_matrix = np.array(X)
Y_vector = np.array(Y)

# Add intercept column (constant)
X_matrix = sm.add_constant(X_matrix)

# T Regression model
t_model = TLinearModel(Y_vector, X_matrix)
t_results = t_model.fit(disp=False)

# Extract outputs in expected format
Alpha = t_results.params[0]
B1 = t_results.params[1]
B2 = t_results.params[2]
B3 = t_results.params[3]
nu = t_results.params[4]
sigma = t_results.params[5]

mu = 0

print("mu:", mu)
print("sigma:", sigma)
print("nu:", nu)
print("Alpha:", Alpha)
print("B1:", B1)
print("B2:", B2)
print("B3:", B3)
"""

# Function for T Regression
def t_regression(X, Y):
    import numpy as np
    import statsmodels.api as sm
    from statsmodels.miscmodels.tmodel import TLinearModel
    
    X_matrix = np.array(X)
    Y_vector = np.array(Y)
    
    X_matrix = sm.add_constant(X_matrix)
    
    t_model = TLinearModel(Y_vector, X_matrix)
    t_results = t_model.fit(disp=False)
    
    Alpha = t_results.params[0]
    B1 = t_results.params[1]
    B2 = t_results.params[2]
    B3 = t_results.params[3]
    nu = t_results.params[4]
    sigma = t_results.params[5]
    mu = 0.0
    
    return mu, sigma, nu, Alpha, B1, B2, B3