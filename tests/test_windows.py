import jdatetime
from tse_analytics.windows import window_start_dates


def test_window_start_dates():
    result = window_start_dates(jdatetime.date(1405, 8, 24))
    assert result == {
        "1m": "1405-07-24",
        "3m": "1405-05-24",
        "6m": "1405-02-24",
        "1y": "1404-08-24",
    }


def test_window_start_dates_crosses_year():
    result = window_start_dates(jdatetime.date(1405, 2, 10))
    assert result == {
        "1m": "1405-01-10",
        "3m": "1404-11-10",
        "6m": "1404-08-10",
        "1y": "1404-02-10",
    }