import pandas as pd

file_path = "data/raw/education_dataset.csv"

df = pd.read_csv(file_path)

print("===== EDUCATION DATASET VALIDATION =====")

print("\nNumber of rows:", len(df))
print("Number of columns:", len(df.columns))

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate prompts:", df["prompt"].duplicated().sum())
print("Duplicate content:", df["content"].duplicated().sum())

print("\nCategories:")
print(df["category"].value_counts())

print("\nN/A content:", (df["content"].fillna("").str.strip().str.upper() == "N/A").sum())

print("\nEmpty prompts:", (df["prompt"].fillna("").str.strip() == "").sum())
print("Empty content:", (df["content"].fillna("").str.strip() == "").sum())

print("\nFirst 5 records:")
print(df.head())

print("\n===== VALIDATION COMPLETE =====")