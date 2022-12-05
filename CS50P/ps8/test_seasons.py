from datetime import date
import pytest
from seasons import convert

def test_invalid_dates():
    with pytest.raises(ValueError):
        convert(date.fromisoformat("19-08-1980"))
        convert(date.fromisoformat("cat"))
        convert(date.fromisoformat("1987/10/17"))


# In the following tests, change dates accordingly
def test_valid_dates():
    # 1 year ago
    assert convert(date.fromisoformat("2021-12-04")) == 365
    # 2 years ago
    assert convert(date.fromisoformat("2020-12-04")) == 730
    # 1 day ago
    assert convert(date.fromisoformat("2022-12-03")) == 1