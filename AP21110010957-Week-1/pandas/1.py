import pandas as pd

# Create a Pandas Series with lists as elements
series_of_lists = pd.Series([[1, 2, 3], [4, 5], [6, 7, 8]])

# Use the explode function to convert the Series of lists to one Series
result_series = series_of_lists.explode()

# Print the original Series and the result
print("Original Series:")
print(series_of_lists)

print("\nResulting Series:")
print(result_series)
