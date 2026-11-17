# TSE-analytics

A Python project for collecting and analyzing Tehran Stock Exchange (TSE) data.

## Current Features

- Fetch historical price data for a selected stock.
- Explore price data using Pandas.
- Inspect dataset structure, data types, missing values, and duplicate dates.
- Generate basic statistical summaries.
- Compute the start dates of fixed comparison windows (1 month, 3 months, 6 months, 1 year) in the Jalali calendar.

## Technologies

- Python
- Pandas
- finpy-tse
- jdatetime
- pytest

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

## Run tests

```bash
python -m pytest
```

## Design decisions

- Stocks are compared over fixed windows that end on the same date: 1 month, 3 months, 6 months and 1 year. Dates are Jalali.
- If a stock was closed on the start date of a window, the first trading day after it is used as the start price.
- Returns will be calculated from adjusted prices.

## Roadmap

- [x] Environment and repository setup
- [x] Fetch and explore price history
- [ ] Reusable functions and first tests
- [ ] Data-quality checks
- [ ] Several symbols and local cache
- [ ] EPS and DPS data
- [ ] Ratios and stock screener
- [ ] Price charts
- [ ] Packaging and v0.1 release

## Note

This project is under development. Data availability and accuracy depend on external data sources and should be verified before use in financial analysis.
