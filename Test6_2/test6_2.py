import pandas as pd
import numpy as np 


df = pd.read_csv("test6.csv")

# Only numeric columns 
prices = df.select_dtypes(include="number")

# Log Returns
log_returns = np.log(prices / prices.shift(1))

# Add date and drop first row
out = pd.concat([df["Date"], log_returns], axis=1).iloc[1:].reset_index(drop=True)

# Print results 
print(out)