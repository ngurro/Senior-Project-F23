# Senior-Project-F23
[README_Senior_Project.md](https://github.com/user-attachments/files/34093889/README_Senior_Project.md)
# Pet Adoption Recommendation System

**Fall 2023 Senior Project | Natural Language Processing & Similarity-Based Matching**

## Overview

This project explores how natural language processing (NLP) can help match prospective dog adopters with shelter animals based on stated preferences and animal characteristics.

The prototype combines animal records associated with PVAS (Palm Valley Animal Society) and pet-related text datasets, including Reddit-derived preference descriptions. Python scripts experiment with extracting structured attributes from free-form text using GPT-3.5 Turbo, then comparing text-based profiles using count-vector representations and cosine similarity. The matching script produces a CSV containing candidate matches and similarity scores.

**Project status:** Historical academic prototype (Fall 2023). The repository contains experimental scripts and intermediate datasets, not a packaged or independently validated production application. Results should be reviewed by a person rather than treated as adoption recommendations that have been assessed for suitability.

## Problem and approach

Shelter animal descriptions and prospective adopters' preferences are often recorded in different formats. This project explores a simple workflow for making those sources more comparable:

1. **Prepare data.** Read and format shelter records and adopter-preference text stored in CSV files.
2. **Extract attributes.** Use prompt-based GPT-3.5 Turbo experiments to identify or normalize information such as breed, size, temperament, and personality from unstructured descriptions.
3. **Vectorize text.** Use Keras's `Tokenizer` to transform the combined records into count-based feature vectors.
4. **Rank candidate matches.** Compute cosine similarity between adopter-preference vectors and shelter-record vectors, retaining up to three high-scoring candidates for each preference record.
5. **Export results.** Save comparisons and matched-record information to `recommendationOutput.csv` for inspection.

This is **content-based similarity matching**, not a supervised machine-learning classifier or an experimentally verified recommendation engine.

## Technologies and methods

- **Python** for data preparation, API experiments, and matching logic
- **CSV, pandas, and NumPy** for tabular data processing and output
- **Keras Tokenizer** for count-based text vectorization
- **Cosine similarity** for comparing vectorized records
- **OpenAI GPT-3.5 Turbo API** (historical scripts) for prompt-based attribute extraction and normalization
- **python-dotenv** for loading an API key from a local environment file

## Key files

| File | Purpose |
| --- | --- |
| `pow_model.py` | Core similarity-matching experiment: loads PVAS and Reddit-formatted datasets, vectorizes text, computes cosine similarity, and exports recommendations. |
| `opai.py` | Early prompt-based experiment for extracting pet-adoption preferences from free-form text. |
| `cluster.py` | Experimental GPT-based grouping of dog descriptions by breed, size, and temperament. |
| `bridgeconnections.py` | Experiment for normalizing temperament descriptions into categories. |
| `twitteropai.py` | Additional experimental attribute-extraction script using social-media-style pet descriptions. |
| `PVAS Abridged.csv`, `RedditDataFormatted2.csv` | Inputs referenced by the matching script. |
| `recommendationOutput.csv` | Example exported matching results committed to the repository. |
| `archive/` | Archived project materials. |

Other CSV/XLSX files contain source, intermediate, or exploratory data. Not every file is necessary to understand the matching workflow.

## Exploring the project

The simplest way to review the work is to inspect `pow_model.py` alongside the input CSV files and the committed `recommendationOutput.csv`.

**Reproducibility note:** The scripts preserve their original Fall 2023 experimental state. Some use hard-coded relative paths such as `Senior-Project-F23\\...`, and the GPT scripts use an older OpenAI Python SDK interface (`openai.ChatCompletion.create`). They may require path changes, compatible historical package versions, and additional input files before execution. The repository does not currently provide a verified one-command setup or test suite.

If adapting the GPT experiments, create a local `.env` file with the variable expected by the original scripts:

```dotenv
OPENAI=your_api_key_here
```

Never commit the `.env` file or API keys to version control. Review API usage and costs before running the scripts; modern OpenAI SDKs use a different interface.

## Interpretation and limitations

- **Similarity is not suitability.** A high cosine-similarity score does not prove that a dog is a safe or appropriate match for a particular household.
- **No verified ranking metrics are reported.** The repository does not establish precision@k, recall@k, user satisfaction, or a validated recommendation accuracy.
- **Simple text features.** Count-based vectors do not reliably capture context, negation, or nuanced preferences.
- **Model-generated attributes need review.** GPT-produced classifications may be incomplete or incorrect.
- **Experimental implementation.** Paths, error handling, package compatibility, and output formatting would need additional work to make the workflow reusable.
- **Data stewardship.** Confirm permission to redistribute source records and remove any personal or sensitive information before sharing datasets publicly.

## Potential next steps

- Refactor the scripts into reusable data ingestion, text processing, matching, and export modules.
- Add a requirements file, portable file paths, sample anonymized input records, and automated tests.
- Establish a labeled set of acceptable matches and report retrieval metrics such as precision@3.
- Compare count vectors against TF-IDF and sentence embeddings.
- Add safeguards to distinguish missing information from inferred attributes.
- Provide a small reproducible example and a visualization of candidate match explanations.

## Academic context

Developed as a senior project to explore the application of NLP and similarity-based retrieval to shelter pet adoption. The repository represents a prototype and learning process rather than a deployed adoption service.
