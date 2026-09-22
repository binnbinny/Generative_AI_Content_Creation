import pandas as pd
from pathlib import Path

# Project root
project_root = Path(__file__).resolve().parent.parent

# Input file
input_path = project_root / "data" / "raw" / "story_dataset.csv"

# Output file
output_path = project_root / "data" / "processed" / "story_dataset_clean.csv"

# Load dataset
df = pd.read_csv(input_path)

print("===== STORY DATA CLEANING =====")
print("Original rows:", len(df))

# Clean text fields
df["prompt"] = df["prompt"].fillna("").str.strip()
df["content"] = df["content"].fillna("").str.strip()

# Remove missing/empty prompt or content
before_missing = len(df)

df = df[
    (df["prompt"] != "") &
    (df["content"] != "")
].copy()

removed_missing = before_missing - len(df)

print("Removed missing/empty records:", removed_missing)

# Remove exact duplicate prompt + content combinations
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

# Save cleaned dataset
output_path.parent.mkdir(parents=True, exist_ok=True)

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