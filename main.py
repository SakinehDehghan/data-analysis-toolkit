\"\"\"CLI entry point for Data Analysis Toolkit.\"\"\"
from toolkit.loader import load_csv, safe_cast_numeric
from toolkit.stats import calculate_summary, calculate_pearson_correlation
from toolkit.visualizer import render_ascii_histogram
from toolkit.exporter import export_markdown_report

def main():
    print(\"=== Data Analysis Toolkit ===\")
    data = load_csv(\"data/sales_data.csv\")
    safe_cast_numeric(data, [\"units_sold\", \"revenue\"])
    
    units = [r[\"units_sold\"] for r in data if r[\"units_sold\"] is not None]
    rev = [r[\"revenue\"] for r in data if r[\"revenue\"] is not None]
    
    print(\"\nUnits Sold Summary:\", calculate_summary(units))
    print(\"Revenue Summary:\", calculate_summary(rev))
    print(f\"Correlation: {calculate_pearson_correlation(units, rev):.4f}\")
    print(\"\nHistogram (Units Sold):\")
    print(render_ascii_histogram(units, bins=4))
    
    export_markdown_report(\"Sales Analysis\", {\"Units Sold\": calculate_summary(units), \"Revenue\": calculate_summary(rev)}, \"reports/sales_report.md\")
    print(\"\nReport generated at reports/sales_report.md\")

if __name__ == '__main__':
    main()
