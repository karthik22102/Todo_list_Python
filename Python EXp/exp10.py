import pandas as pd

# Load the dataset
url = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"
df = pd.read_csv(url)

# 1. Read the first 8 rows
print("First 8 rows of the dataset:")
print(df.head(8))

# 2. Display column names
print("\nColumn names:")
print(df.columns)

# 3. Fill missing values with column mean
df_filled = df.fillna(df.mean(numeric_only=True))
print("\nDataset after filling missing values:")
print(df_filled.head(8))

# 4. Remove rows containing any missing values
df_cleaned = df.dropna()
print("\nDataset after removing rows with missing values:")
print(df_cleaned.head(8))

# 5. Group the data by species
grouped = df_cleaned.groupby("species")

# 6. Calculate mean, min, and max of Sepal length
print("\nStatistics for Sepal Length:")
print("Mean:", df_cleaned["sepal_length"].mean())
print("Min:", df_cleaned["sepal_length"].min())
print("Max:", df_cleaned["sepal_length"].max())

###########################################


#pd.read_csv(url): Loads the dataset.
#df.head(8): Displays the first 8 rows.
#df.columns: Prints column names.
#df.fillna(df.mean(numeric_only=True)): Fills missing values with the mean.
#df.dropna(): Removes rows with missing values.
#df.groupby("species"): Groups data by species.
#df["sepal_length"].mean() / min() / max(): Computes statistics.