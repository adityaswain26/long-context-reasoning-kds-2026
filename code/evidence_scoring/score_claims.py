from typing import List, Dict

from evidence_scoring.novel_loader import load_novel
from evidence_scoring.retriever import retrieve_passages
from evidence_scoring.contradiction_rules import score_claim_against_passage


def score_character(book: str, claims: list, backstory_text: str) -> int:
    novel_store = load_novel(book)        # <-- Pathways-backed store
    novel_text = novel_store.get_text()   # <-- extract text from Pathways
    contradiction_count = 0

    backstory_lower = backstory_text.lower()

    for claim in claims:
        # Check if backstory supports this claim
        claim_terms = claim["statement"].lower().split()[:6]

        if not any(t in backstory_lower for t in claim_terms):
            contradiction_count += 1
            continue

        passages = retrieve_passages(novel_text, claim)
        claim_score = sum(
            score_claim_against_passage(claim, p) for p in passages
        )

        if claim_score < 0:
            contradiction_count += 1

    return 0 if contradiction_count >= 4 else 1


     