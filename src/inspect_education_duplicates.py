import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
file_path = project_root / "data" / "raw" / "education_dataset.csv"

df = pd.read_csv(file_path)

print("===== EDUCATION DUPLICATE PROMPT INSPECTION =====")

df["prompt_clean"] = df["prompt"].fillna("").str.strip()

duplicate_prompts = df[
    (df["prompt_clean"] != "") &
    (df["prompt_clean"].duplicated(keep=False))
].sort_values("prompt_clean")

print("Records belonging to repeated prompts:", len(duplicate_prompts))
print("Unique repeated prompts:", duplicate_prompts["prompt_clean"].nunique())

for prompt, group in duplicate_prompts.groupby("prompt_clean"):

    print("\n" + "=" * 80)
    print("PROMPT:")
    print(prompt)

    for _, row in group.iterrows():
        print("\nRecord ID:", row["id"])
        print("Content:")
        print(row["content"])

print("\n===== INSPECTION COMPLETE =====")