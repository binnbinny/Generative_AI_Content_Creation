import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent

input_path = project_root / "data" / "raw" / "marketing_dataset.csv"
output_path = project_root / "data" / "processed" / "marketing_dataset_clean.csv"

df = pd.read_csv(input_path)

print("===== MARKETING DATA CLEANING =====")
print("Original rows:", len(df))

# Remove leading/trailing spaces
df["prompt"] = df["prompt"].fillna("").str.strip()
df["content"] = df["content"].fillna("").str.strip()

# Remove empty records
before_missing = len(df)

df = df[
    (df["prompt"] != "") &
    (df["content"] != "")
].copy()

removed_missing = before_missing - len(df)

print("Removed missing/empty records:", removed_missing)

# Remove exact duplicate prompt + content pairs
before_duplicates = len(df)

df = df.drop_duplicates(
    subset=["prompt", "content"],
    keep="first"
).copy()

removed_duplicates = before_duplicates - len(df)

print("Removed exact duplicate records:", removed_duplicates)

# Reset IDs
df = df.reset_index(drop=True)
df["id"] = range(1, len(df) + 1)

# Create output folder if needed
output_path.parent.mkdir(
    parents=True,
    exist_ok=True
)

# Save cleaned dataset
df.to_csv(
    output_path,
    index=False,
    encoding="utf-8"
)

print("\nCleaned rows:", len(df))
print("Saved to:", output_path)

print("\nRemaining missing values:")
print(df.isnull().sum())

print("\n===== CLEANING COMPLETE =====")