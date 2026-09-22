import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
file_path = project_root / "data" / "raw" / "marketing_dataset.csv"

df = pd.read_csv(file_path)

print("===== MARKETING DATASET VALIDATION =====")
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

print("\nEmpty prompts:", (df["prompt"].fillna("").str.strip() == "").sum())
print("Empty content:", (df["content"].fillna("").str.strip() == "").sum())

print("\nFirst 5 records:")
print(df.head())

print("\n===== VALIDATION COMPLETE =====")