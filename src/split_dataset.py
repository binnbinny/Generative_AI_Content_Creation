import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split

# Project root
project_root = Path(__file__).resolve().parent.parent

# Input files
story_path = project_root / "data" / "processed" / "story_dataset_clean.csv"
education_path = project_root / "data" / "processed" / "education_dataset_clean.csv"
marketing_path = project_root / "data" / "processed" / "marketing_dataset_clean.csv"

# Output folder
output_dir = project_root / "data" / "splits"
output_dir.mkdir(parents=True, exist_ok=True)

# Load datasets
story_df = pd.read_csv(story_path)
education_df = pd.read_csv(education_path)
marketing_df = pd.read_csv(marketing_path)

print("===== DATASET SPLITTING =====")

print("\nStory records:", len(story_df))
print("Education records:", len(education_df))
print("Marketing records:", len(marketing_df))

# Combine all datasets
combined_df = pd.concat(
    [story_df, education_df, marketing_df],
    ignore_index=True
)

print("\nTotal combined records:", len(combined_df))

# 80% Training, 20% temporary
train_df, temp_df = train_test_split(
    combined_df,
    test_size=0.20,
    random_state=42,
    stratify=combined_df["category"]
)

# Split remaining 20% into
# 10% Validation and 10% Test
validation_df, test_df = train_test_split(
    temp_df,
    test_size=0.50,
    random_state=42,
    stratify=temp_df["category"]
)

# Reset indexes
train_df = train_df.reset_index(drop=True)
validation_df = validation_df.reset_index(drop=True)
test_df = test_df.reset_index(drop=True)

# Save files
train_df.to_csv(
    output_dir / "train.csv",
    index=False,
    encoding="utf-8"
)

validation_df.to_csv(
    output_dir / "validation.csv",
    index=False,
    encoding="utf-8"
)

test_df.to_csv(
    output_dir / "test.csv",
    index=False,
    encoding="utf-8"
)

print("\n===== SPLIT RESULTS =====")

print("Training set:", len(train_df))
print("Validation set:", len(validation_df))
print("Test set:", len(test_df))

print("\nTraining category distribution:")
print(train_df["category"].value_counts())

print("\nValidation category distribution:")
print(validation_df["category"].value_counts())

print("\nTest category distribution:")
print(test_df["category"].value_counts())

print("\nFiles saved to:")
print(output_dir)

print("\n===== SPLITTING COMPLETE =====")