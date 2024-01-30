import pandas as pd

# Create a dictionary with data and index labels
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

index_labels = ['Person1', 'Person2', 'Person3', 'Person4']

# Create a DataFrame from the dictionary with index labels
df = pd.DataFrame(data, index=index_labels)

# Display the DataFrame
print(df)
