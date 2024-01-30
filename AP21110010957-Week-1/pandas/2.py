import pandas as pd

# Create a Pandas Series
data = {'A': 10, 'B': 20, 'C': 30, 'D': 40, 'E': 50}
series_data = pd.Series(data)

# Set the condition (e.g., values greater than 30)
condition = series_data > 30

# Create a subset based on the condition
subset = series_data[condition]

# Print the original series and the subset
print("Original Series:")
print(series_data)

print("\nSubset based on condition:")
print(subset)
