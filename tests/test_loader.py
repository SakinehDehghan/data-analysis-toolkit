import os
from toolkit.loader import load_csv, safe_cast_numeric

def test_load_csv():
    rows = load_csv("data/sales_data.csv")
    assert len(rows) > 0
    assert "units_sold" in rows[0]

def test_safe_cast():
    sample = [{"val": "12.5"}, {"val": "invalid"}]
    safe_cast_numeric(sample, ["val"])
    assert sample[0]["val"] == 12.5
    assert sample[1]["val"] is None
