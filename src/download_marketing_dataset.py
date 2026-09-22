from datasets import load_dataset
import pandas as pd
from pathlib import Path

dataset = load_dataset(
    "suehuynh/marketing-instruct-4k",
    split="train[:1000]"
)

df = dataset.to_pandas()

marketing_df = pd.DataFrame({
    "id": range(1, len(df) + 1),
    "category": "Marketing",
    "prompt": df["enhanced_prompt"],
    "content": df["enhanced_completion"],
    "source": "Hugging Face: suehuynh/marketing-instruct-4k"
})

output_path = Path(__file__).resolve().parent.parent / "data" / "raw" / "marketing_dataset.csv"
output_path.parent.mkdir(parents=True, exist_ok=True)

marketing_df.to_csv(
    output_path,
    index=False,
    encoding="utf-8"
)

print("Marketing dataset downloaded successfully!")
print("Number of rows:", len(marketing_df))
print("Saved to:", output_path)
print("Columns:", marketing_df.columns.tolist())

print("\nFirst 5 records:")
print(marketing_df.head())