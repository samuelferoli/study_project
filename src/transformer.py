from src.extractor import read_csv_file
from src.config import BASE_DIR, RAW_DATA_DIR, CLEAN_DATA_DIR

csv_path = RAW_DATA_DIR / "users.csv"
csv_dict = read_csv_file(csv_path)

def clean_users_data(raw_users: list[dict]) -> tuple[list[dict], list[dict]]:
    try:
        if not 


