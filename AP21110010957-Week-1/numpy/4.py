import numpy as np

# Create a NumPy array
my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Specify the filename to save to
filename = 'my_array.txt'

# Save the array to a text file
np.savetxt(filename, my_array, delimiter=' ')

print(f"The array has been saved to '{filename}'.")
