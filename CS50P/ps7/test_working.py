import pytest
from working import convert

def test_string():
    with pytest.raises(ValueError):
        convert("Hello")
        convert("cat")
        convert("9:15 AM to o8:15 PM")

def test_valid_time():
    assert convert("09 AM to 02:00 PM") == "09:00 to 14:00"
    assert convert("8:47 PM to 3:21 PM") == "20:47 to 15:21"
    assert convert("7:15 AM to 3 PM") == "07:15 to 15:00"
    assert convert("10:11 AM to 12:01 AM") == "10:11 to 00:01"


def test_invalid_time():
    with pytest.raises(ValueError):
        convert("10:60 AM to 5:60 PM")
        convert("9:45 PM to 12:60 PM")
        convert("12:60 AM to 11:13 AM")