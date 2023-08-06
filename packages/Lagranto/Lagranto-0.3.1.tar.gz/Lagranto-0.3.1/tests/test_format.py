from datetime import datetime

import pytest

from lagranto import formats

from .paths import asciifile


def test_get_ascii_header_variables():
    """header is read and split correctly"""

    header, variables, ntime = formats.get_ascii_header_variables(asciifile)

    header_exp = [
        "Reference",
        "date",
        "20001014_0600",
        "/",
        "Time",
        "range",
        "-1800",
        "min",
    ]
    variables_exp = ["time", "lon", "lat", "z", "QV"]

    assert header == header_exp
    assert variables == variables_exp
    assert ntime == 31


# =============================================================================


def test_header_to_date_full():
    """start date is read correctly from full header"""

    header = [
        "Reference",
        "date",
        "20001014_0600",
        "/",
        "Time",
        "range",
        "-1800",
        "min",
    ]

    result = formats.header_to_date(header)
    expected = datetime(2000, 10, 14, 6, 0)
    assert result == expected


@pytest.mark.parametrize(
    "header, expected",
    [
        (["", "", "20001014_0600"], datetime(2000, 10, 14, 6, 0)),
        (["", "", "20001014", "06"], datetime(2000, 10, 14, 6, 0)),
        (["", "", "XXX", "YYY"], datetime(1970, 1, 1)),
    ],
)
def test_header_to_date(header, expected):
    """test the correct date is determined"""

    result = formats.header_to_date(header)
    assert result == expected


# =============================================================================


def test_hhmm_to_hours_deprecated():
    with pytest.raises(ValueError, match="'hhmm_to_hours' is  deprecated:"):
        formats.hhmm_to_hours(0)


@pytest.mark.parametrize(
    "time, expected",
    [
        [b"00.00", 0.0],
        [b"01.00", 1.0],
        [b"10.00", 10.0],
        [b"01.30", 1.5],
        [b"10.01", 10 + 1.0 / 60],
        [b"-01.00", -1.0],
        [b"-10.00", -10.0],
        [b"-01.30", -1.5],
        [b"-10.01", -(10 + 1.0 / 60)],
    ],
)
def test_hhmm_to_frac_hour(time, expected):

    result = formats.hhmm_to_frac_hour(time)
    assert result == expected

    result = formats.hhmm_to_frac_hour(float(time))
    assert result == expected
