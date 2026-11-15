import jdatetime

WINDOW_MONTHS = {"1m": 1, "3m": 3, "6m": 6, "1y": 12}

def window_start_dates(end_date: jdatetime.date) -> dict[str, str]:
    result = {}
    for name, month_back in WINDOW_MONTHS.items():
        year = end_date.year
        month = end_date.month - month_back
        if month <= 0:
            month += 12
            year -= 1
        result[name]= f"{year}-{month:02d}-{end_date.day:02d}"
    return result

if __name__ == "__main__":
    today = jdatetime.date.today()
    print(window_start_dates(today))
