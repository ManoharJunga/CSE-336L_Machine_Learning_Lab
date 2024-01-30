import pandas as pd

# Create a Pandas Series
data = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5])

# Find the most frequent value
most_frequent_value = data.mode().iloc[0]

# Replace everything else with 'Other'
data.replace(data[data != most_frequent_value], 'Other', inplace=True)

# Print the original series and the modified series
print("Original Series:")
print(data)
