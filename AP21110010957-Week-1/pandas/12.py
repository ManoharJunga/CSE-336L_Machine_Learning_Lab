import pandas as pd
import numpy as np

# Create a DataFrame with infinite values
data = {
    'A': [1, 2, np.inf, 4],
    'B': [5, np.inf, 7, 8],
    'C': [9, 10, 11, 12]
}

df = pd.DataFrame(data)

# Display the original DataFrame with infinite values
print("Original DataFrame with infinite values:")
print(df)

# Replace infinite values with NaN
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# Remove rows containing NaN (you can also use df.dropna(axis=1) to remove columns)
df = df.dropna()

# Display the DataFrame after removing infinite values
print("\nDataFrame after removing infinite values:")
print(df)
