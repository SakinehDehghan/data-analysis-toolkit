\"\"\"Data loader module for various file formats.\"\"\"
import csv
import json
import os

def load_csv(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    with open(filepath, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def load_json(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    with open(filepath, mode='r', encoding='utf-8') as f:
        return json.load(f)

def safe_cast_numeric(rows, columns):
    \"\"\"Converts specified string columns to float safely.\"\"\"
    for row in rows:
        for col in columns:
            if col in row and row[col] is not None and row[col] != "":
                try:
                    row[col] = float(row[col])
                except (ValueError, TypeError):
                    row[col] = None
    return rows
