from datasets import load_dataset
import pandas as pd
from pathlib import Path

dataset = load_dataset(
    "andrewelawrence/writingPrompts-merged",
    split="train[:1000]"
)

df = dataset.to_pandas()

story_df = pd.DataFrame({
    "id": range(1, len(df) + 1),
    "category": "Story",
    "prompt": df["prompt"],
    "content": df["story"],
    "source": "Hugging Face: andrewelawrence/writingPrompts-merged"
})

output_path = Path("data/raw/story_dataset.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)

story_df.to_csv(output_path, index=False, encoding="utf-8")

print("Story dataset downloaded successfully!")
print("Number of rows:", len(story_df))
print("Saved to:", output_path)
print("Columns:", story_df.columns.tolist())
print("\nFirst 5 records:")
print(story_df.head())