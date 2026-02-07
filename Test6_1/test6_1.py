import pandas as pd


# Load data
df = pd.read_csv("test6.csv")

prices = df.select_dtypes(include="number")
returns = prices.pct_change()

# Include date 
out = pd.concat([df["Date"], returns], axis=1).iloc[1:].reset_index(drop=True)

# Print Result
print(out)