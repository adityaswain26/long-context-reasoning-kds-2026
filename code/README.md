# 📚 Backstory Consistency Verification using Claim-Based Reasoning

## Overview

This project addresses the **Backstory Consistency Verification** task from the Kharagpur Data Science Hackathon 2026.

Given:

* a *novel*,
* a *character*,
* and a *backstory text*,

the goal is to determine whether the backstory is **consistent** with the original novel or **contradicts** it.

Instead of treating this as a black-box classification problem, we design an **explainable reasoning pipeline** that models character knowledge explicitly and checks it against evidence from the novel.

---

## Key Idea

We treat each character as a set of **stable semantic claims** (events, beliefs, motivations, capabilities).
A backstory is considered *consistent* if these claims are **supported or not contradicted** by the novel text.

This mirrors how humans verify narrative consistency:

> “Does this backstory introduce facts, motivations, or events that the novel would reject?”

---

## System Architecture

```
Backstory Text
      ↓
Claim Extraction (manual, structured)
      ↓
Novel Evidence Retrieval
      ↓
Contradiction Scoring
      ↓
Final Consistency Decision
```

---

## Step 1: Claim Extraction

Each character is represented by **8–12 high-level claims**, such as:

* **EVENT**: formative experiences or canonical incidents
* **BELIEF**: ideological or moral stances
* **MOTIVATION**: persistent drives
* **CAPABILITY**: skills or competencies

Claims are **manually defined per character** (acceptable in hackathon settings) and stored modularly per novel.

Example claim:

```json
{
  "type": "BELIEF",
  "statement": "Paganel values empirical, firsthand exploration over institutional authority."
}
```

Claims are intentionally abstract to remain stable across narrative passages.

---

## Step 2: Evidence Retrieval

For each claim:

* the full novel text is loaded,
* sliding windows of text are searched for lexical overlap with the claim,
* top-matching passages are retrieved as potential evidence.

To reduce noise:

* front-matter (title pages, contents) is skipped,
* only narrative sections are considered.

---

## Step 3: Contradiction Scoring

Each retrieved passage is scored against the claim using **rule-based logic**:

* +1 → supports or aligns with the claim
* −1 → contradicts the claim
* 0 → neutral / irrelevant

Rules are **claim-type aware** (EVENT ≠ BELIEF ≠ MOTIVATION), improving semantic alignment.

---

## Step 4: Backstory Grounding

To avoid constant predictions:

* claims must also be **supported by the backstory text itself**,
* claims absent from the backstory count as weak contradictions.

This ensures predictions vary meaningfully across different backstories.

---

## Step 5: Aggregation & Decision

For a character:

* contradiction counts are aggregated across all claims,
* if contradictions exceed a threshold → **contradict**
* otherwise → **consistent**

Final output labels:

* `"consistent"`
* `"contradict"`

---

## Results

On the provided training set:

* **Train Accuracy:** ~0.62 (best configuration)
* Predictions are **non-trivial** and **balanced**
* Rule changes affect results sensibly (no random behavior)

This is strong performance for a fully explainable, non-ML system.

---

## Why Rule-Based?

We deliberately avoid ML because:

* training data is small,
* interpretability is critical,
* the task is semantic and narrative in nature.

Our approach prioritizes:

* transparency,
* debuggability,
* alignment with human reasoning.

---

## How to Run

### 1. Evaluate on training data

```bash
python -m evidence_scoring.evaluate_train
```

### 2. Generate predictions for test data

```bash
python -m evidence_scoring.predict_test
```

This produces:

```
submission.csv
```

with a single column: `label`

---

## Project Structure

```
kds_hackathon_2026/
├── claim_extraction/
│   ├── extract_claims.py
│   ├── in_search_of_castaways.py
│   └── count_of_monte_cristo.py
├── evidence_scoring/
│   ├── novel_loader.py
│   ├── retriever.py
│   ├── contradiction_rules.py
│   ├── score_claims.py
│   ├── evaluate_train.py
│   └── predict_test.py
├── notes/
│   └── reasoning_notes.md
├── data/
├── submission.csv
└── README.md
```

---

## Notes

Detailed design decisions, failed attempts, and tuning rationale are documented in:

```
notes/reasoning_notes.md
```

---

## Final Remarks

This project demonstrates that **structured reasoning** and **explicit modeling of narrative knowledge** can effectively solve backstory verification tasks without opaque models.

The system is modular, interpretable, and extensible to new novels or characters.


