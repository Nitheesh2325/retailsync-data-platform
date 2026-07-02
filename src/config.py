DB_PATH = "retailsync.db"

RAW_DATA_PATH = "data/raw/orders.csv"

CLEAN_DATA_PATH = "data/staging/clean_orders.csv"

LOG_FILE = "logs/pipeline.log"

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = BASE_DIR / "data" / "raw" / "orders.csv"
STAGING_DATA_PATH = BASE_DIR / "data" / "staging" / "clean_orders.csv"
DB_PATH = BASE_DIR / "retailsync.db"
LOG_FILE = BASE_DIR / "logs" / "pipeline.log"