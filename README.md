# TSE-analytics

A Python project for collecting and analyzing Tehran Stock Exchange (TSE) data.

## Current Features

- Fetch historical price data for a selected stock.
- Explore price data using Pandas.
- Inspect dataset structure, data types, missing values, and duplicate dates.
- Generate basic statistical summaries.

## Technologies

- Python
- Pandas
- finpy-tse

## Installation

Clone the repository:

```bash
git clone https://github.com/amiiiiir7/TSE-analytics.git
cd TSE-analytics
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

```bash
python explore_price.py
```

The current example retrieves historical price data for the Iranian stock symbol `خودرو`.

## Planned Features

- Historical price analysis and visualization
- EPS and DPS data
- Dividend and financial ratios
- Stock screening tools

## Note

This project is under development. Data availability and accuracy depend on external data sources and should be verified before use in financial analysis.