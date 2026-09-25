\"\"\"Data cleaning and preprocessing module.\"\"\"

def drop_missing(rows, key):
    \"\"\"Remove rows where key is None or empty.\"\"\"
    return [r for r in rows if r.get(key) not in (None, "")]
