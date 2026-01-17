# Test 7_1 Assignment
# Write a function to fit a normal distribution and ensure your output is expected.

# There will be scratch code used during development
# Function will be at the bottom of the file

import math 

"""
# Load values from source file
values = []
file_name = "test7_1.csv"
file = open(file_name, "r")
lines = file.readlines()
file.close()

# Skip header // clean lines // convert to float
for line in lines[1:]:
    clean_line = line.strip()
    
    if clean_line == "":
        continue
    
    number = float(clean_line)
    values.append(number)
    
print("How many numbers:", len(values))

# Calculate Mean
total = 0
for x in values:
    total = total + x
    
count = len(values)
mean = total / count

print("Mean:", mean)

# Calculate Variance
squared_total = 0

for x in values:
    diff = x - mean
    diff_squared = diff * diff
    squared_total = squared_total + diff_squared
    
variance = squared_total / (count - 1)

print("Variance:", variance)

# Calculate Standard Deviation
std_dev = math.sqrt(variance)

print("Standard Deviation:", std_dev)
"""

# Function to fit normal distribution
def fit_normal_distribution(values):
    # Calculate Mean
    total = 0
    for x in values:
        total = total + x
        
    count = len(values)
    mean = total / count
    
    # Calculate Variance
    squared_total = 0
    for x in values:
        diff = x - mean
        squared_total = squared_total + (diff * diff)
        
    variance = squared_total / (count - 1)
    
    #Calculate Standard Deviation
    std_dev = math.sqrt(variance)
    
    return mean, std_dev