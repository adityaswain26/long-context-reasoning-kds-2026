import re
from typing import List

def retrieve_passages(
        novel_text: str,
        claim: dict,
        window_size: int = 400
) -> List[str]:
    """
    Retrieve candidate passages from the novel relevant to a claim.
    Very simple keyword-based sliding window.
    """
    novel_text = novel_text[5000:]
    statement = claim["statement"].lower()

    # crude keyword extraction: meaningful words only
    keywords = [
        w for w in re.findall(r"\w+", statement)
        if len(w) > 4
    ]

    passages = []

    text_lower = novel_text.lower()

    for  kw in keywords:
        idx = text_lower.find(kw)
        if idx == -1:
            continue

        start = max(0, idx - window_size)
        end = min(len(novel_text), idx + window_size)

        passages.append(novel_text[start:end])

        #we only need a  few passages
        if len(passages) >= 3:
            break

    return passages