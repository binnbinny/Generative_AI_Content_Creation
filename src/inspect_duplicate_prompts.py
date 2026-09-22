import pandas as pd

# Load the Story dataset
file_path = "../data/raw/story_dataset.csv"
df = pd.read_csv(file_path)

print("===== DUPLICATE PROMPT INSPECTION =====")

# Find prompts that appear more than once
duplicate_prompts = df[df["prompt"].duplicated(keep=False)].copy()

# Sort so identical prompts appear together
duplicate_prompts = duplicate_prompts.sort_values("prompt")

# Group by prompt
for prompt, group in duplicate_prompts.groupby("prompt", sort=False):

    print("\n" + "=" * 80)
    print("PROMPT:")
    print(prompt)

    print("\nNumber of stories for this prompt:", len(group))

    for _, row in group.iterrows():
        print("\n--- Record ID:", row["id"], "---")
        print("Story:")
        print(row["content"][:1000])
        print("...")

print("\n" + "=" * 80)
print("Total records with repeated prompts:", len(duplicate_prompts))
print("Number of unique repeated prompts:", duplicate_prompts["prompt"].nunique())
print("\n===== INSPECTION COMPLETE =====")