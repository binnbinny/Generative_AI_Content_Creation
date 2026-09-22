import pandas as pd

file_path = "data/splits/test.csv"

df = pd.read_csv(file_path)

print("===== TEST DATASET INSPECTION =====")

print("\nNumber of rows:", len(df))

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())

print("\nFirst 3 records:")
print(df[["prompt", "content"]].head(3).to_string(index=False))

print("\nCategory distribution:")
print(df["category"].value_counts())

print("\n===== INSPECTION COMPLETE =====")