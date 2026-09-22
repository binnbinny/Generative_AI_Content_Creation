import pandas as pd
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

from text_generator import TextGenerator


# ==================================================
# 1. LOAD TEST DATASET
# ==================================================

test_path = "data/splits/test.csv"

df = pd.read_csv(test_path)

print("===== BLEU BASELINE EVALUATION =====")
print("Total records available:", len(df))


# ==================================================
# 2. CREATE BALANCED 30-RECORD SAMPLE
# ==================================================

marketing_df = df[df["category"] == "Marketing"].head(10)

story_df = df[df["category"] == "Story"].head(10)

education_df = df[df["category"] == "Education"].head(10)


sample_df = pd.concat(
    [
        marketing_df,
        story_df,
        education_df
    ],
    ignore_index=True
)


print("\n===== SAMPLE SELECTION =====")
print("Marketing records:", len(marketing_df))
print("Story records:", len(story_df))
print("Education records:", len(education_df))
print("Total sample records:", len(sample_df))


# ==================================================
# 3. INITIALIZE TEXT GENERATOR
# ==================================================

generator = TextGenerator()

smooth = SmoothingFunction().method1


# ==================================================
# 4. STORE RESULTS
# ==================================================

results = []


# ==================================================
# 5. GENERATE TEXT AND CALCULATE BLEU
# ==================================================

for index, row in sample_df.iterrows():

    category = row["category"]

    prompt = row["prompt"]

    reference = row["content"]

    print(
        f"\nProcessing record {index + 1}/"
        f"{len(sample_df)} ({category})..."
    )

    try:

        # Generate text using Qwen
        generated = generator.generate(prompt)

        # Convert reference and generated text
        # into lowercase word tokens
        reference_tokens = reference.lower().split()

        generated_tokens = generated.lower().split()

        # Calculate BLEU score
        score = sentence_bleu(
            [reference_tokens],
            generated_tokens,
            smoothing_function=smooth
        )

        # Store result
        results.append(
            {
                "id": row["id"],
                "category": category,
                "prompt": prompt,
                "reference": reference,
                "generated": generated,
                "bleu_score": score
            }
        )

        print("BLEU:", round(score, 4))

    except Exception as e:

        print("ERROR:", e)

        results.append(
            {
                "id": row["id"],
                "category": category,
                "prompt": prompt,
                "reference": reference,
                "generated": "",
                "bleu_score": 0.0
            }
        )


# ==================================================
# 6. CREATE RESULTS DATAFRAME
# ==================================================

results_df = pd.DataFrame(results)


# ==================================================
# 7. SAVE INDIVIDUAL RESULTS
# ==================================================

output_path = "results/bleu_evaluation_results.csv"

results_df.to_csv(
    output_path,
    index=False,
    encoding="utf-8"
)

print("\nResults saved to:")
print(output_path)


# ==================================================
# 8. CALCULATE OVERALL BLEU
# ==================================================

overall_bleu = results_df["bleu_score"].mean()


# ==================================================
# 9. CALCULATE CATEGORY-WISE BLEU
# ==================================================

marketing_bleu = results_df[
    results_df["category"] == "Marketing"
]["bleu_score"].mean()


story_bleu = results_df[
    results_df["category"] == "Story"
]["bleu_score"].mean()


education_bleu = results_df[
    results_df["category"] == "Education"
]["bleu_score"].mean()


# ==================================================
# 10. DISPLAY FINAL RESULTS
# ==================================================

print("\n==========================================")
print("        BLEU BASELINE RESULTS")
print("==========================================")

print(
    "\nTotal records evaluated:",
    len(results_df)
)

print(
    "\nOverall BLEU:",
    round(overall_bleu, 4)
)

print(
    "Marketing BLEU:",
    round(marketing_bleu, 4)
)

print(
    "Story BLEU:",
    round(story_bleu, 4)
)

print(
    "Education BLEU:",
    round(education_bleu, 4)
)

print("\n==========================================")
print("       EVALUATION COMPLETE")
print("==========================================")