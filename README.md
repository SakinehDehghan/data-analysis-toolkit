# Data Analysis Toolkit 📊

<div align="center">

<p align="center">
  <strong>A lightweight, pure-Python toolkit for statistical data analysis, preprocessing, ASCII visual reporting, and automated workflows.</strong>
</p>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Version" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Version-1.0.1-blue?style=for-the-badge" alt="Version" /></a>
  <a href="#"><img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Coverage-100%25-brightgreen?style=for-the-badge" alt="Coverage" /></a>
</p>

<p align="center">
  <a href="#about-the-project">About</a> •
  <a href="#features">Features</a> •
  <a href="#project-structure">Structure</a> •
  <a href="#getting-started">Getting Started</a> •
  <a href="#usage">Usage</a> •
  <a href="#running-tests">Tests</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#license">License</a>
</p>

</div>

---

## 📖 About The Project

**Data Analysis Toolkit** is a standalone, dependency-free Python toolkit engineered to simplify descriptive statistical analysis, dataset cleaning, and console-friendly visualizations. It provides quick insights into tabular data without the heavy overhead of large third-party libraries.

### Key Highlights:
- ⚡ **Pure Python & Zero External Dependencies:** Runs instantly on any standard Python 3.8+ environment.
- 📈 **Terminal ASCII Visuals:** Generates histograms, sparklines, and metric comparison charts directly in the console.
- 🛡️ **Robust Data Hygiene:** Outlier filtering via IQR and Z-Score, safe numeric typecasting, and configurable missing-value imputation.
- 📑 **Multi-Format Exporting:** Seamlessly exports reports in Markdown, JSON, and CSV formats.

---

## ✨ Features

- [x] **Descriptive Statistics:** Calculate Mean, Median, Variance, Standard Deviation, Weighted Mean, Harmonic Mean, Geometric Mean, and Pearson Correlation.
- [x] **Data Cleaning & Validation:** IQR and Z-Score outlier detection, duplicate removal, column renaming, and schema verification.
- [x] **Lightweight Visualizations:** In-console ASCII histograms, bar charts, and horizontal sparklines.
- [x] **Flexible Data Loaders:** Streamlined loading for CSV, TSV, and JSON formats with batch dataset support.
- [x] **Automated Reporting:** Generate professional Markdown, CSV, and JSON statistical reports.
- [x] **Automated CI/CD:** GitHub Actions workflow included for automated testing on every push.

---

## 🏗️ Project Structure

```plaintext
data-analysis-toolkit/
├── toolkit/                # Core toolkit package
│   ├── __init__.py         # Package entry and versioning
│   ├── config.py           # Configuration parameters and thresholds
│   ├── loader.py           # CSV, TSV, and JSON data loaders
│   ├── cleaner.py          # Data cleaning, imputing, and outlier filters
│   ├── stats.py            # Comprehensive statistical calculations
│   ├── visualizer.py       # ASCII histograms, sparklines, and charts
│   ├── exporter.py         # Markdown, JSON, and CSV report exporters
│   ├── validator.py        # Schema and column validator
│   └── exceptions.py       # Domain-specific exception classes
├── data/                   # Sample datasets for testing
│   ├── sales_data.csv      # Sample sales records
│   └── customer_metrics.json # Sample customer performance metrics
├── tests/                  # Automated unit test suite
│   ├── test_loader.py      # Data loading and cleaning tests
│   └── test_stats.py       # Statistical function tests
├── .github/workflows/      # GitHub Actions CI workflow (ci.yml)
├── CHANGELOG.md            # Release history and updates
├── CONTRIBUTING.md         # Open-source contribution guidelines
├── requirements.txt        # Development and testing requirements
├── setup.py                # Package installation and distribution
├── LICENSE                 # MIT License
└── README.md               # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SakinehDehghan/data-analysis-toolkit.git
   cd data-analysis-toolkit
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux/macOS:
   source .venv/bin/activate
   ```

3. Install testing dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 💡 Usage

### CLI Execution
Run the end-to-end demo directly from your terminal:
```bash
python main.py
```

### Programmatic Python API
```python
from toolkit.loader import load_csv, safe_cast_numeric
from toolkit.stats import calculate_summary, calculate_pearson_correlation
from toolkit.visualizer import render_ascii_histogram

# 1. Load data
rows = load_csv("data/sales_data.csv")
safe_cast_numeric(rows, ["units_sold", "revenue"])

# 2. Extract series and calculate summary
units = [r["units_sold"] for r in rows if r["units_sold"] is not None]
summary = calculate_summary(units)
print("Summary:", summary)

# 3. Render terminal histogram
print(render_ascii_histogram(units, bins=4))
```

---

## 🧪 Running Tests

To run the automated test suite with pytest:
```bash
pytest
```

---

## 🤝 Contributing

Contributions are welcome! Please review [CONTRIBUTING.md](./CONTRIBUTING.md) for details on our code of conduct and the submission process.

---

## 📜 License

Distributed under the **MIT License**. See [LICENSE](./LICENSE) for details.

---

## 👤 Author

**Sakineh Dehghan**
- GitHub: [@SakinehDehghan](https://github.com/SakinehDehghan)
- Email: stats.data.official@gmail.com
