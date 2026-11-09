# Data Analysis Toolkit

An academic, pure-Python toolkit for statistical data analysis, descriptive modeling, data sanitization, and automated reporting.

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)]()
[![Affiliation](https://img.shields.io/badge/Affiliation-Shahid%20Beheshti%20University-green.svg)](https://en.sbu.ac.ir/)

---

## Overview

The **Data Analysis Toolkit** is designed for rigorous statistical computation, robust exploratory data analysis (EDA), and automated report synthesis. Developed with zero external runtime dependencies, it provides verified implementations of standard parametric and non-parametric statistics, missing value imputation protocols, and outlier detection mechanisms.

### Core Objectives
* **Deterministic Computation:** Pure-Python mathematical and statistical routines ensuring cross-platform repeatability.
* **Data Sanitization & Hygiene:** Standardized protocols for handling missing observations, type inference, and boundary verification.
* **Lightweight Terminal Diagnostics:** Console-based diagnostic histograms and sparkline distributions for rapid inspection.
* **Reproducible Reporting:** Programmatic generation of Markdown, JSON, and tabular CSV analytical summaries.

---

## Theoretical & Methodological Foundations

The toolkit implements the following core statistical methodologies:

1. **Location Estimators:**
   * Arithmetic Mean: $\bar{x} = \frac{1}{n} \sum_{i=1}^n x_i$
   * Weighted Mean: $\bar{x}_w = \frac{\sum w_i x_i}{\sum w_i}$
   * Median and robust percentiles.
   * Geometric and Harmonic central tendencies.

2. **Dispersion & Association:**
   * Sample Variance ($s^2$) with Bessel's correction ($n-1$ denominator).
   * Standard Deviation ($s$).
   * Pearson Product-Moment Correlation Coefficient ($r_{xy}$).

3. **Anomaly & Outlier Identification:**
   * Tukey's Interquartile Range (IQR) Rule: Fences at $[Q_1 - 1.5 \cdot \text{IQR}, Q_3 + 1.5 \cdot \text{IQR}]$.
   * Standardized Z-Score criterion ($|z| > 3.0$).

---

## Repository Structure

```plaintext
data-analysis-toolkit/
├── toolkit/                  # Core package implementation
│   ├── __init__.py           # Package namespace and version metadata
│   ├── config.py             # Numerical thresholds and parameters
│   ├── loader.py             # Delimited and structured data loaders
│   ├── cleaner.py            # Preprocessing, imputation, and outlier filters
│   ├── stats.py              # Statistical estimation functions
│   ├── visualizer.py         # Terminal diagnostic visualizations
│   ├── exporter.py           # Structured analytical export utilities
│   ├── validator.py          # Data schema and type integrity checkers
│   └── exceptions.py         # Domain-specific exception definitions
├── data/                     # Demonstration datasets
│   ├── sales_data.csv        # Tabular bivariate dataset
│   └── customer_metrics.json # Semi-structured metrics records
├── tests/                    # Verification and test suites
│   ├── test_loader.py        # Loader and sanitization test cases
│   └── test_stats.py         # Statistical calculation test cases
├── .github/workflows/        # Continuous integration workflows
├── CHANGELOG.md              # Version and modification records
├── CONTRIBUTING.md           # Collaboration and contribution guidelines
├── requirements.txt          # Development dependencies
├── setup.py                  # Package specification
├── LICENSE                   # Licensing terms
└── README.md                 # Primary project documentation
```

---

## Getting Started

### Prerequisites
* Python 3.8 or higher
* Git

### Installation

Clone the repository to your local environment:

```bash
git clone https://github.com/SakinehDehghan/data-analysis-toolkit.git
cd data-analysis-toolkit
```

Optionally, initialize an isolated virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

Install verification dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

### Command-Line Execution
Run the integrated analytical demonstration pipeline:

```bash
python main.py
```

### Programmatic API
Import modules directly into research scripts or workflows:

```python
from toolkit.loader import load_csv, safe_cast_numeric
from toolkit.stats import calculate_summary, calculate_pearson_correlation
from toolkit.visualizer import render_ascii_histogram

# Load and cast tabular observations
records = load_csv("data/sales_data.csv")
safe_cast_numeric(records, ["units_sold", "revenue"])

# Extract variables
units = [r["units_sold"] for r in records if r["units_sold"] is not None]
revenue = [r["revenue"] for r in records if r["revenue"] is not None]

# Compute summary statistics and association
stats_summary = calculate_summary(units)
correlation = calculate_pearson_correlation(units, revenue)

# Render terminal distribution
print(render_ascii_histogram(units, bins=4))
```

---

## Verification & Testing

The package includes automated tests covering statistical accuracy and data handling edge cases:

```bash
pytest
```

---

## License

This project is licensed under the terms of the **MIT License**. Refer to the [LICENSE](LICENSE) file for complete details.

---

## Author & Academic Affiliation

**Sakineh Dehghan**  
Department of Statistics, Shahid Beheshti University (SBU)  
* Email: [Sa_dehghan@Sbu.ac.ir](mailto:Sa_dehghan@Sbu.ac.ir)  
* GitHub: [@SakinehDehghan](https://github.com/SakinehDehghan)
