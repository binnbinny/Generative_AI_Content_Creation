from datasets import load_dataset
import pandas as pd
from pathlib import Path

dataset = load_dataset(
    "Mariia1234/adaption-education-qa-pairs-v1",
    split="train"
)

df = dataset.to_pandas()

education_df = pd.DataFrame({
    "id": range(1, len(df) + 1),
    "category": "Education",
    "prompt": df["enhanced_prompt"],
    "content": df["enhanced_completion"],
    "source": "Hugging Face: Mariia1234/adaption-education-qa-pairs-v1"
})

output_path = Path("data/raw/education_dataset.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)

education_df.to_csv(
    output_path,
    index=False,
    encoding="utf-8"
)

print("Education dataset downloaded successfully!")
print("Number of rows:", len(education_df))
print("Saved to:", output_path)
print("Columns:", education_df.columns.tolist())

print("\nFirst 5 records:")
print(education_df.head())