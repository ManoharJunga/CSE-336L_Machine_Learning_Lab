import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Attempts': [1, 3, 2, 4],
    'Score': [80, 65, 90, 75]
}

df = pd.DataFrame(data)

# Select rows where the number of attempts is greater than 2
selected_rows = df[df['Attempts'] > 2]

# Display the selected rows
print("Original DataFrame:")
print(df)

print("\nSelected rows with more than 2 attempts:")
print(selected_rows)
