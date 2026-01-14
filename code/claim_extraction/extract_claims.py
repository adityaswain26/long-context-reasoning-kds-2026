import pandas as pd 
from typing import List,Dict
from .in_search_of_castaways import (
    paganel_claims,
    aryton_claims,
    thalcave_claims,
    koumou_claims
)

from .count_of_monte_cristo import (
    noirtier_claims,
    faria_claims
)


# Step 1.1 : Load CSV
def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

# Step 1.2: Group by (book_name, char)
def group_backstories(df: pd.DataFrame):
    return df.groupby(["book_name", "char"])

# Step 1.3: Merge content into one backstory
def merge_backstory(group: pd.DataFrame) -> str:
    group = group.sort_values("id")
    return " ".join(group["content"].astype(str).tolist())

# Step 1.4 Extract Claims (Manual/Rule-based)
def extract_claims(backstory_text: str, book: str, char: str) -> List[Dict]:
    
    book = book.strip()
    char =" ".join(char.strip().split())
    
    if book == "In Search of the Castaways":
        if char == "Jacques Paganel":
            return paganel_claims()
        elif char == "Tom Ayrton/Ben Joyce":
            return aryton_claims()
        elif char == "Thalcave":
            return thalcave_claims()
        elif char == "Kai-Koumou":
            return koumou_claims()
        
    elif book == "The Count of Monte Cristo":
        if char == "Noirtier":
            return noirtier_claims()
        elif char == "Faria":
            return faria_claims()
    print(f"[WARN] No claims found for : {book} | {char}")
    return []

# Step 1.5: Run Step pipeline
def run_step1(csv_path: str):
    df = load_data(csv_path)
    grouped = group_backstories(df)

    all_claims = {}

    for (book, char), group in grouped:
        backstory = merge_backstory(group)
        claims = extract_claims(backstory, book, char)

        all_claims[(book, char)] = claims

        print(f"\n=== {book} | {char} ===")
        for c in claims:
            print(c)

    return all_claims

if __name__ == "__main__":
    run_step1("/home/adity/kds_hackathon_2026/data/train.csv")