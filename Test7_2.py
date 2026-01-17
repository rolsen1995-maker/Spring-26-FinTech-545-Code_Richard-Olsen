# Test7_2 Assignment
# Write a function to fit a T distribution and ensure your output is expected. 

# There will be scratch code used during development
# Function will be at the bottom of the file

import math

"""
# Load inputs from source file 
values = []
file_name = "test7_2.csv"
file = open(file_name, "r")
lines = file.readlines()
file.close()

for line in lines[1:]:
    clean_line = line.strip()
    if clean_line == "":
        continue
    
    number = float(clean_line)
    values.append(number)
    
print("How many numbers:", len(values))

# Compute Mu 
total = 0
for x in values:
    total = total + x
    
count = len(values)
mu = total / (count)

print("Mu:", mu)

# Compute Sigma
squared_total = 0

for x in values:
    diff = x - mu
    diff_squared = diff * diff
    squared_total = squared_total + diff_squared
    
variance = squared_total / (count - 1)
sigma = math.sqrt(variance)

print("sigma:", sigma)

# Fit T distribution using package
from scipy import stats

params = stats.t.fit(values)

nu = params[0]
mu_t = params[1]
sigma_t = params[2]

print("mu:", mu_t)
print("sigma:", sigma_t)
print("nu:", nu)
"""

def fit_t_distribution(values):
    from scipy import stats
    
    params = stats.t.fit(values)
    
    nu = params[0]
    mu = params[1]
    sigma = params[2]
    
    return mu, sigma, nu