from typing import Dict

def score_claim_against_passage(claim: Dict, passage: str) -> int:
    claim_text = claim["statement"].lower()
    passage_text = passage.lower()
    claim_type = claim["type"]

    # --- SUPPORT ---
    # if key terms from claim appear together
    key_terms = claim_text.split()[:6]
    if sum(1 for w in key_terms if w in passage_text) >= 2:
        return +1

    # --- CONTRADICTIONS ---
    if claim_type == "EVENT":
        if "never" in passage_text or "no such" in passage_text:
            return -1

    if claim_type == "BELIEF":
        if "repented" in passage_text or "abandoned" in passage_text:
            return -1

    if claim_type == "MOTIVATION":
        if "indifferent" in passage_text or "without concern" in passage_text:
            return -1

    return 0
