# Long-Context Narrative Consistency Reasoning (KDS Hackathon 2026)

This project implements an evidence-grounded reasoning system to verify whether character backstories are logically consistent with long-form literary narratives.

## Key Ideas
- Claim extraction from backstories (events, beliefs, motivations, capabilities)
- Retrieval of supporting or contradicting passages from full novels
- Rule-based contradiction scoring
- Conservative decision logic to avoid unsupported assumptions

## Why this matters
Instead of learning dataset shortcuts, this system reasons directly over source texts, prioritizing robustness and explainability over raw accuracy.

## Tech Stack
- Python
- Pathway (document ingestion & authoritative store)
- Pandas
- Rule-based NLP + retrieval

## Structure
- `claim_extraction/` – manual + structured claim schemas per character
- `evidence_scoring/` – retrieval, contradiction rules, scoring
- `run.sh` – end-to-end execution
- `Report.pdf` – full methodology and discussion

## Notes
This was built as a solo submission with a focus on correctness, long-context handling, and transparency.
