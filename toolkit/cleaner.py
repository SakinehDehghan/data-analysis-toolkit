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

def detect_outliers_iqr(values, threshold=1.5):
    sorted_v = sorted(values)
    n = len(sorted_v)
    if n < 4:
        return []
    q1 = sorted_v[int(0.25 * n)]
    q3 = sorted_v[int(0.75 * n)]
    iqr = q3 - q1
    lower_bound = q1 - (threshold * iqr)
    upper_bound = q3 + (threshold * iqr)
    return [v for v in sorted_v if v < lower_bound or v > upper_bound]

def rename_columns(rows, mapping):
    for r in rows:
        for old_col, new_col in mapping.items():
            if old_col in r:
                r[new_col] = r.pop(old_col)
    return rows

def remove_duplicates(rows, key):
    seen = set()
    unique = []
    for r in rows:
        val = r.get(key)
        if val not in seen:
            seen.add(val)
            unique.append(r)
    return unique

def detect_outliers_zscore(numbers, threshold=3.0):
    if len(numbers) < 2:
        return []
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1)
    std = math.sqrt(variance)
    if std == 0:
        return []
    return [x for x in numbers if abs((x - mean) / std) > threshold]
