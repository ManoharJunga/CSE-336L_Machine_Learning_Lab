import pandas as pd

# Create a Pandas Series
data = pd.Series(['apple', 'banana', 'cherry', 'date'])

# Calculate the number of characters in each word
word_lengths = data.apply(lambda x: len(x))

# Print the original series and the calculated word lengths
print("Original Series:")
print(data)

print("\nNumber of characters in each word:")
print(word_lengths)
