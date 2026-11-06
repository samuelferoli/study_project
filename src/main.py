from src.config import BASE_DIR, RAW_DATA_DIR, CLEAN_DATA_DIR, ensure_directories
from src.extractor import read_json_file

ensure_directories()

print(RAW_DATA_DIR.resolve())

json_path = RAW_DATA_DIR / "transactions.json"

json_return = read_json_file(json_path)

users = {row["user_id"] for row in json_return}

print(users)

total_brl = 0.0
for row in json_return:
    if row["currency"] == "BRL" and row["status"] == "completed":
        total_brl += row["amount"]

print(total_brl)

total_brl = sum(
    row["amount"] 
    for row in json_return 
    if row["currency"] == "BRL" and row["status"] == "completed")