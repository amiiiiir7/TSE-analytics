import jdatetime
from tse_analytics.windows import calculation_windows


def test_calculation_windows():
    result = calculation_windows(jdatetime.date(1405, 8, 24))
    assert result == {
        "1m": "1405-07-24",
        "3m": "1405-05-24",
        "6m": "1405-02-24",
        "1y": "1404-08-24",
    }


def test_calculation_windows_crosses_year():
    result = calculation_windows(jdatetime.date(1405, 2, 10))
    assert result == {
        "1m": "1405-01-10",
        "3m": "1404-11-10",
        "6m": "1404-08-10",
        "1y": "1404-02-10",
    }