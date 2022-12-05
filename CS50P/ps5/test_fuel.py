"""
Since 'fuel.py' is in another directory, I need the following two
lines to retrieve the file. If you place the file 'fuel.py' in the
same directory as 'test_fuel.py', then comment these two lines
"""
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'ps3'))

import pytest
from fuel import convert, gauge
"""
Make sure to comment the following lines in 'fuel.py': 
21, 30, 33, 34, and 36, so that 'pytest' can raise the
errors addressed here
"""

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_invalid_input():
    with pytest.raises(ValueError):
        convert("Hello")

def test_convert():
    assert convert("1/4") == 25
    assert convert("0/4") == 0
    assert convert("2/3") == 66
    assert convert("3/2") == 150
    assert convert("4/4") == 100
    assert convert("1/9") == 11

def test_gauge():
    assert gauge(.75) == "E"
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(45) == "45%"
    assert gauge(105) == "F"
    assert gauge(0) == "E"
