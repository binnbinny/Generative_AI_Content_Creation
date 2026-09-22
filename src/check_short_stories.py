import pandas as pd

# Load the Story dataset
file_path = "../data/raw/story_dataset.csv"
df = pd.read_csv(file_path)

print("===== SHORT / EMPTY STORY CHECK =====")

# Remove leading/trailing spaces before checking length
df["content_clean"] = df["content"].fillna("").str.strip()

# Count words in each story
df["word_count"] = df["content_clean"].str.split().str.len()

# Find empty stories
empty_stories = df[df["content_clean"] == ""]

# Find very short stories
# Here we use fewer than 20 words as the threshold
short_stories = df[
    (df["word_count"] > 0) &
    (df["word_count"] < 20)
]

print("\nEmpty stories:", len(empty_stories))
print("Very short stories (<20 words):", len(short_stories))

# Show empty stories
if len(empty_stories) > 0:
    print("\n===== EMPTY STORIES =====")
    print(empty_stories[["id", "prompt", "content"]])

# Show short stories
if len(short_stories) > 0:
    print("\n===== VERY SHORT STORIES =====")

    for _, row in short_stories.iterrows():
        print("\nRecord ID:", row["id"])
        print("Word count:", row["word_count"])
        print("Prompt:", row["prompt"])
        print("Story:", row["content"])

print("\n===== CHECK COMPLETE =====")