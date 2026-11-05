from src.config import BASE_DIR, RAW_DATA_DIR, CLEAN_DATA_DIR, ensure_directories

ensure_directories()

print(RAW_DATA_DIR.resolve())

file_path = RAW_DATA_DIR / "test_raw.txt"

file_path.touch()

print(file_path.exists())