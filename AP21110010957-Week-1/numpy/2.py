import numpy as np

# Create an array with missing data
array_with_missing_data = np.array([1.0, 2.0, np.nan, 4.0, np.nan, 6.0])

# Find missing data in the array
missing_indices = np.isnan(array_with_missing_data)

# Print the array and the indices of missing data
print("Array with missing data:", array_with_missing_data)
print("Indices of missing data:", missing_indices)
