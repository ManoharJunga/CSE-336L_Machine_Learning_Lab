import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Attempts': [1, 3, 2, 4],
    'Score': [80, 65, 90, 75],
    'Qualify': ['yes', 'no', 'yes', 'no']
}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Replace 'yes' and 'no' in the 'Qualify' column with True and False
df['Qualify'] = df['Qualify'].replace({'yes': True, 'no': False})

# Display the DataFrame after replacement
print("\nDataFrame after replacing 'yes' and 'no' with True and False in 'Qualify' column:")
print(df)
