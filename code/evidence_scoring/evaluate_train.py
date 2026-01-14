import pandas as pd

from claim_extraction.extract_claims import extract_claims
from evidence_scoring.score_claims import score_character


def evaluate_train(csv_path: str):
    df = pd.read_csv(csv_path)

    correct = 0
    total = 0

    for _, row in df.iterrows():
        book = row["book_name"]
        char = row["char"]
        label_map = {
            "consistent": 1,
            "contradict": 0
        }
        true_label = label_map[row["label"]]

        # Step 1: get claims
        backstory_text = row["content"]
        claims = extract_claims(backstory_text, book, char)

        if not claims:
            continue  # safety skip

        # Step 2: score consistency
        pred_label = score_character(book, claims, backstory_text)

        if pred_label == true_label:
            correct += 1

        total += 1

    accuracy = correct / total if total > 0 else 0
    print(f"Train Accuracy: {accuracy:.3f} ({correct}/{total})")


if __name__ == "__main__":
    evaluate_train("/home/adity/kds_hackathon_2026/data/train.csv")
