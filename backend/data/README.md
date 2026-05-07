# backend/data/

Data directory for the Phase 1 Data Foundation pipeline (Amazon Reviews 2018, UCSD).

---

## Directory Layout

```
backend/data/
├── pipeline/
│   ├── __init__.py
│   ├── config.py                  ← all constants and paths
│   ├── phase1_data_foundation.py  ← main pipeline script
│   └── requirements.txt           ← pinned dependencies
├── raw/
│   ├── raw_reviews_2018.json.gz   ← downloaded .json.gz kept as recovery point
│   ├── raw_reviews_2018.parquet   ← Parquet cache (skip re-parse on next run)
│   ├── raw_metadata_2018.json.gz
│   └── raw_metadata_2018.parquet
└── processed/
    ├── users_interactions.parquet
    ├── products_features.parquet
    ├── products_text.parquet
    ├── category_encoders.pkl
    └── data_summary.json
```

---

## Data Flow

```
UCSD (Electronics_5.json.gz)           →  raw/raw_reviews_2018.parquet
UCSD (meta_Electronics.json.gz)        →  raw/raw_metadata_2018.parquet
        ↓                   ↓
        └─────── MERGE ───────┘
                   ↓
            CLEANING PIPELINE
       (dedup → text filter → price
        → ratings → categories → k-core)
                   ↓
     ┌───────────┼───────────┐
     ↓             ↓             ↓
users_         products_      products_
interactions   features       text
.parquet       .parquet       .parquet
     └───────────┼───────────┘
                   ↓
        consumed by all 3 recommender modules
```

---

## Output Table Schemas

### users_interactions.parquet
| Column | Type | Description |
|---|---|---|
| user_id | string | Anonymized user identifier |
| product_id | string | Product identifier (asin) |
| rating | float | 1.0 – 5.0 |
| timestamp | int | Unix timestamp |
| helpful_votes | int | Upvote count from [upvotes, total] array |
| verified_purchase | bool | Whether purchase was verified |
| interaction_type | category | "love" ≥4.0 / "neutral" =3.0 / "dislike" <3.0 |
| days_since_epoch | int | timestamp / 86400 for time-aware CF |

Sorted by `(user_id, timestamp)`. Unique on `(user_id, product_id)`.

### products_features.parquet
| Column | Type | Description |
|---|---|---|
| product_id | string | Product identifier |
| title | string | Product title |
| brand | category | From `brand` field in 2018 metadata; "Unknown" if null |
| price | float | Normalized price (USD) |
| price_was_imputed | bool | True if price was filled by brand-level median |
| price_bucket | category | budget / mid-range / premium / luxury |
| category_l1/l2/l3 | int | Label-encoded category levels |
| category_l1/l2/l3_name | category | Human-readable category levels |
| avg_rating | float | Metadata average rating (or computed mean) |
| rating_count | int | Number of ratings from metadata |
| avg_rating_norm | float | MinMax-scaled avg_rating [0, 1] |
| rating_count_norm | float | MinMax-scaled log1p(rating_count) [0, 1] |
| price_norm | float | MinMax-scaled price [0, 1] |

One row per product. Unique on `product_id`.

### products_text.parquet
| Column | Type | Description |
|---|---|---|
| product_id | string | Product identifier |
| title | string | Raw cleaned title |
| description | string | Raw description (list joined to string) |
| features | string | Raw features (list joined to string) |
| full_text | string | Concatenated + cleaned text for vectorization |
| text_length | int | Character count of full_text |
| token_count | int | Approximate word count of full_text |

One row per product. `product_id` matches `products_features` exactly.

---

## How to Run

### Install dependencies
```bash
pip install -r backend/data/pipeline/requirements.txt
```

### Run the pipeline
```bash
# From the project root
python -m backend.data.pipeline.phase1_data_foundation
```

The pipeline will:
1. Download `.json.gz` files from UCSD via HTTP (skipped if `.json.gz` already exists)
2. Parse JSONL line-by-line using stdlib `gzip` + `json` — no HuggingFace dependency
3. Save Parquet caches (skipped on subsequent runs if caches exist)
4. Merge reviews + metadata on `product_id` (already normalised by parsers)
5. Run the full cleaning pipeline (dedup, price, ratings, categories, k-core)
6. Build the three output tables
7. Save all files to `backend/data/processed/`

### Check pipeline status (from Python)
```python
from backend.data.pipeline.phase1_data_foundation import get_pipeline_status

status = get_pipeline_status()
print(status["status"])   # "complete" | "partial" | "not_started"
print(status["summary"])  # contents of data_summary.json
```

---

## Data Source

Dataset: Amazon Product Reviews 2018 (McAuley Lab, UCSD)
Category: Electronics (5-core filtered)

Download source (automatic on first run):
  Reviews:  http://deepyeti.ucsd.edu/jmcauley/datasets/amazon_v2/categoryFilesSmall/Electronics_5.json.gz
  Metadata: http://deepyeti.ucsd.edu/jmcauley/datasets/amazon_v2/metaFiles2/meta_Electronics.json.gz

Format: JSONL (.json.gz) — one JSON object per line

Differences from 2023 version:
- Uses `asin` not `parent_asin` as product identifier
- Uses `brand` not `store` for seller/manufacturer name
- `description` is a plain string, not a list
- No pre-computed `average_rating` in metadata (computed from reviews)
- No HuggingFace dependency — pure stdlib download (`urllib` + `gzip`)

Citation:
  Justifying recommendations using distantly-labeled reviews and
  fine-grained aspects. Jianmo Ni, Jiacheng Li, Julian McAuley.
  EMNLP 2019.

---

## Expected Output Sizes (after 5-core filtering)

| Table | Rows (approx.) |
|---|---|
| users_interactions | 1.2M – 1.7M |
| products_features | 60K – 120K |
| products_text | 60K – 120K |

Disk usage: ~100 MB–300 MB total (Parquet + snappy compression).
RAM required during pipeline run: ~2–4 GB.

---

## Troubleshooting

### UCSD server unreachable
```
ConnectionError: Cannot reach UCSD servers. Check internet connection.
```
- Check your internet connection.
- The UCSD servers occasionally have downtime. Wait a few minutes and retry.
- If a partial `.json.gz` file was created, delete it from `raw/` before retrying
  (the pipeline cleans up partial files automatically on failure, but verify).

### Disk space error during download
- `Electronics_5.json.gz` (reviews) is ~500 MB–1 GB compressed.
- `meta_Electronics.json.gz` (metadata) is ~2–4 GB compressed.
- Ensure at least 10 GB free before running.

### Out-of-memory during merge / cleaning
- Peak RAM during merge is ~2–4 GB for the 5-core dataset.
- Close other applications before running.

### 0 rows after merge
```
ValueError: Merge produced 0 rows.
```
- Verify that both files are Electronics category (not two different categories).
- The `asin` values in `meta_Electronics.json.gz` must overlap with those in
  `Electronics_5.json.gz`. These are from the same 2018 UCSD release.

### High malformed-line count in metadata
- The 2018 metadata file contains some Python-literal strings (single quotes)
  that are not valid JSON. Skipping up to ~2% of lines is normal and expected.
- If >10% of lines fail, the file may be corrupt — delete it and re-download.

### Partial pipeline state
If `data_summary.json` is missing but some parquet files exist, the status will be `"partial"`.
Re-run the pipeline to regenerate all files cleanly.
