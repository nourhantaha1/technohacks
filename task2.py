import pandas as pd

# Read the dataset from the CSV file
df = pd.read_csv('Iris.csv')

# Remove duplicates
df.drop_duplicates(inplace=True)

# Print the updated dataset without duplicates
print(df)