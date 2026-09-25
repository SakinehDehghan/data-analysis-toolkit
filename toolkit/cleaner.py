\"\"\"Data cleaning and preprocessing module.\"\"\"

def drop_missing(rows, key):
    \"\"\"Remove rows where key is None or empty.\"\"\"
    return [r for r in rows if r.get(key) not in (None, "")]

def fill_missing(rows, key, strategy="mean"):
    values = [r[key] for r in rows if isinstance(r.get(key), (int, float))]
    if not values:
        return rows
    fill_value = sum(values) / len(values) if strategy == "mean" else 0.0
    for r in rows:
        if r.get(key) is None:
            r[key] = round(fill_value, 2)
    return rows
