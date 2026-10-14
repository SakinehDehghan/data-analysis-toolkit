# Data Analysis Toolkit 📊

A modular and lightweight Python toolkit for descriptive statistics, data cleaning, ASCII visualizations, and report generation.

## Quick Start

`ash
# Clone the repository
git clone https://github.com/SakinehDehghan/data-analysis-toolkit.git
cd data-analysis-toolkit

# Run the sample analysis
python main.py
`

## Features

- **Statistical Analysis:** Mean, Median, Variance, Standard Deviation, Pearson Correlation.
- **Data Preprocessing:** Handle missing values, filter outliers with IQR.
- **Visuals in Terminal:** Render ASCII histograms and bar charts directly in console.
- **Reporting:** Export markdown and JSON summary reports.
- **Automated CI:** GitHub Actions workflow included.

## Running Tests

`ash
pytest
`
"@
git add README.md
git commit -m "docs: add detailed usage guide and CLI examples"

# Commit 29
Set-Content -Path "LICENSE" -Value @"
MIT License

Copyright (c) 2026 Sakineh Dehghan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
