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

# Sort the DataFrame by 'Name' in descending order, then by 'Score' in ascending order
sorted_df = df.sort_values(by=['Name', 'Score'], ascending=[False, True])

# Display the sorted DataFrame
print("\nDataFrame sorted by 'Name' in descending order, then by 'Score' in ascending order:")
print(sorted_df)
