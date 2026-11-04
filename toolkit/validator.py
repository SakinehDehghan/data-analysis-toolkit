\"\"\"Data validator module.\"\"\"

def validate_schema(rows, required_columns):
    if not rows:
        return False
    for col in required_columns:
        if col not in rows[0]:
            return False
    return True
