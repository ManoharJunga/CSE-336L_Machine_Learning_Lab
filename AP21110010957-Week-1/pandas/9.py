import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Attempts': [1, 3, 2, 4],
    'Score': [80, 65, 90, 75]
}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Append a new row 'k' to the DataFrame
new_row_values = ['Kathy', 2, 85]
df.loc['k'] = new_row_values

# Display the DataFrame after adding the new row
print("\nDataFrame after adding a new row 'k':")
print(df)

# Delete the added row 'k' and return the original DataFrame
original_df = df.drop('k')

# Display the original DataFrame after deleting the added row
print("\nOriginal DataFrame after deleting the new row 'k':")
print(original_df)
