from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = BASE_DIR / "data_raw"
CLEAN_DATA_DIR = BASE_DIR / "data_clean"

def ensure_directories():
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
    CLEAN_DATA_DIR.mkdir(parents=True, exist_ok=True)
