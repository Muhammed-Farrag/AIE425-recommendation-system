"""
config.py — All constants and paths for Phase 1 Data Foundation Pipeline.

Centralising everything here means phase1_data_foundation.py never has
magic numbers or hard-coded paths, making config changes instant and safe.
"""

from pathlib import Path

# ---------------------------------------------------------------------------
# Directory layout
# ---------------------------------------------------------------------------
DATA_ROOT_DIR: Path = Path("backend/data")
DATA_RAW_DIR: Path = DATA_ROOT_DIR / "raw"
DATA_PROCESSED_DIR: Path = DATA_ROOT_DIR / "processed"
DATA_PIPELINE_DIR: Path = DATA_ROOT_DIR / "pipeline"

# ---------------------------------------------------------------------------
# Amazon Reviews dataset — direct HTTPS download from HuggingFace CDN.
# The UCSD mirror (deepyeti.ucsd.edu) is unreliable; HF CDN is stable.
# Same JSONL schema, no `datasets` library needed — plain urllib download.
# Python 3.11: use built-in tomllib if config moves to TOML in future.
# All type hints in this project use Python 3.10+ union syntax (X | Y).
# ---------------------------------------------------------------------------
REVIEWS_URL: str = (
    "https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023"
    "/resolve/main/raw_review_Electronics.jsonl.gz"
)
METADATA_URL: str = (
    "https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023"
    "/resolve/main/raw_meta_Electronics.jsonl.gz"
)

# Raw .json.gz files kept on disk as a recovery point
RAW_REVIEWS_FILENAME: str = "raw_reviews_2018.json.gz"
RAW_METADATA_FILENAME: str = "raw_metadata_2018.json.gz"

# Parquet caches built from the .json.gz files (skip re-parse on next run)
RAW_REVIEWS_PARQUET: str = "raw_reviews_2018.parquet"
RAW_METADATA_PARQUET: str = "raw_metadata_2018.parquet"

# ---------------------------------------------------------------------------
# Processed output file names  (unchanged — downstream code uses these)
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Processed output file names
# ---------------------------------------------------------------------------
INTERACTIONS_FILE: str = "users_interactions.parquet"
FEATURES_FILE: str = "products_features.parquet"
TEXT_FILE: str = "products_text.parquet"
ENCODERS_FILE: str = "category_encoders.pkl"
SUMMARY_FILE: str = "data_summary.json"

# ---------------------------------------------------------------------------
# k-core filtering
# Iterative because a single pass can leave orphaned nodes on either side.
# ---------------------------------------------------------------------------
KCORE_MIN_INTERACTIONS: int = 5
KCORE_MAX_ITERATIONS: int = 20

# ---------------------------------------------------------------------------
# Price bucketing thresholds (USD)
# Boundaries chosen to reflect typical consumer-electronics price tiers.
# ---------------------------------------------------------------------------
PRICE_BUDGET_MAX: float = 30.0      # < $30  → "budget"
PRICE_MID_MAX: float = 100.0        # $30–$100 → "mid-range"
PRICE_PREMIUM_MAX: float = 300.0    # $100–$300 → "premium"
                                    # > $300    → "luxury"

# ---------------------------------------------------------------------------
# Text processing
# ---------------------------------------------------------------------------
# Products whose combined full_text is shorter than this are too sparse
# to be useful in any NLP-based recommender.
TEXT_MIN_LENGTH: int = 10

# ---------------------------------------------------------------------------
# Category hierarchy
# ---------------------------------------------------------------------------
CATEGORY_MAX_LEVELS: int = 3

# ---------------------------------------------------------------------------
# Parquet I/O settings
# snappy gives good speed/size trade-off; pyarrow is the canonical engine.
# ---------------------------------------------------------------------------
PARQUET_ENGINE: str = "pyarrow"
PARQUET_COMPRESSION: str = "snappy"

# ---------------------------------------------------------------------------
# Pipeline metadata
# ---------------------------------------------------------------------------
PIPELINE_VERSION: str = "1.0"
