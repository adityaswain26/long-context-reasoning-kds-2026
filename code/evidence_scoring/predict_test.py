import pandas as pd

from claim_extraction.extract_claims import extract_claims
from evidence_scoring.score_claims import score_character


def predict_test(csv_path: str, output_path: str):
    df = pd.read_csv(csv_path)

    predictions = []

    for _, row in df.iterrows():
        story_id = row["id"]
        book = row["book_name"]
        char = row["char"]
        backstory_text = row["content"]

        claims = extract_claims(backstory_text, book, char)
        pred = score_character(book, claims, backstory_text)

        # Map numeric prediction to label string
        predictions.append({
            "story_id": story_id,
            "prediction": int(pred)
        })


    submission = pd.DataFrame(predictions)


    submission.to_csv(output_path, index=False)
    print(f"Submission file saved to: {output_path}")


if __name__ == "__main__":
    predict_test("data/test.csv", "results.csv")
