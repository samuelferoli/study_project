from pathlib import Path
import json
import csv

def read_json_file(file_path: Path) -> list[dict]:
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def read_csv_file(file_path: Path) -> list[dict]:
    with open(file_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)
        
