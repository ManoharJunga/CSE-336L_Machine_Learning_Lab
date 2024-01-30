import numpy as np

# Create two arrays
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([1, 5, 7, 9])

# Check whether each element of array1 is present in array2
result = np.isin(array1, array2)

# Print the original arrays and the result
print("Array 1:", array1)
print("Array 2:", array2)
print("Is each element of array1 present in array2:", result)
