import pandas as pd

# Create a Pandas Series
data = pd.Series([1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50])

# Find the positions of numbers that are multiples of 5
positions_of_multiples_of_5 = data.index[data % 5 == 0].tolist()

# Print the original series and the positions of multiples of 5
print("Original Series:")
print(data)

print("\nPositions of numbers that are multiples of 5:")
print(positions_of_multiples_of_5)
