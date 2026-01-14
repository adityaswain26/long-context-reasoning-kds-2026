import os
from evidence_scoring.pathways_store import NovelStore
# Map book names to local novel text files
BOOK_TO_FILE = {
    "In Search of the Castaways": "/home/adity/kds_hackathon_2026/data/In search of the castaways.txt",
    "The Count of Monte Cristo": "/home/adity/kds_hackathon_2026/data/The Count of Monte Cristo.txt",
}

def load_novel(book_name: str) -> NovelStore:
    """
    Load and return the full novel text for a given book.
    """
    if book_name not in BOOK_TO_FILE:
        raise ValueError(f"Unknown book: {book_name}")

    path = BOOK_TO_FILE[book_name]

    if not os.path.exists(path):
        raise FileNotFoundError(f"Novel file not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    return NovelStore(text)
