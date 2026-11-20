import jdatetime

WINDOW_MONTHS = {"1m": 1, "3m": 3, "6m": 6, "1y": 12}


def calculation_windows(reference_date: jdatetime.date) -> dict[str, str]:
    """Return the start date of each fixed calculation window.

    reference_date: today or any past date. It is the end of every window.
    Returns: a dict with keys "1m", "3m", "6m", "1y". Each value is the start
    date of that window as a Jalali string ("YYYY-MM-DD").
    """
    result = {}
    for name, month_back in WINDOW_MONTHS.items():
        year = reference_date.year
        month = reference_date.month - month_back
        if month <= 0:
            month += 12
            year -= 1
        result[name] = f"{year}-{month:02d}-{reference_date.day:02d}"
    return result


if __name__ == "__main__":
    today = jdatetime.date.today()
    print(calculation_windows(today))
