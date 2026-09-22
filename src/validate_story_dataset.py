import pandas as pd

# Load the Story dataset
file_path = "data/raw/story_dataset.csv"
df = pd.read_csv(file_path)

print("===== STORY DATASET VALIDATION =====")

# Number of rows and columns
print("\nNumber of rows:", len(df))
print("Number of columns:", len(df.columns))

# Column names
print("\nColumns:")
print(df.columns.tolist())

# Missing values
print("\nMissing values:")
print(df.isnull().sum())

# Duplicate prompts
print("\nDuplicate prompts:", df["prompt"].duplicated().sum())

# Duplicate content
print("Duplicate stories:", df["content"].duplicated().sum())

# Categories
print("\nCategories:")
print(df["category"].value_counts())

# Show first 5 records
print("\nFirst 5 records:")
print(df.head())

print("\n===== VALIDATION COMPLETE =====")