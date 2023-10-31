import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/kaggle/input/iris/Iris.csv')
df.info()

# Cleaning data'Removing nulls and duplicates if it exist'
df = df.dropna()
df = df.drop_duplicates()

# Count the occurrences of each species
species_counts = sns.countplot(x=df['Species'])
plt.xlabel('Species')
plt.ylabel('Count')
plt.title('Bar Chart of Iris Species Counts')
plt.show()

# Create a pie chart of species distribution
species_counts = df['Species'].value_counts()
species_labels = set(df['Species'])
plt.figure(figsize=(8, 6))
plt.pie(species_counts, labels=species_labels, autopct='%1.1f%%', startangle=140)
plt.title('Species Distribution')
plt.axis('equal')
plt.show()
# Create histograms for sepal length, sepal width, and petal length
fig, axes = plt.subplots(4, 1, figsize=(10, 25))

for i, feature in enumerate(df.columns[1:5]):
    axes[i].hist(df[feature], bins=10, edgecolor='k', alpha=0.7)
    axes[i].set_xlabel(f'{feature} (cm)')
    axes[i].set_ylabel('Frequency')
    axes[i].set_title(f'Histogram of {feature} in Iris Dataset')

# Adjust the spacing between subplots
plt.tight_layout()

plt.show()