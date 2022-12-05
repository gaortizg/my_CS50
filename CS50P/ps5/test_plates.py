"""
Since 'plates.py' is in another directory, I need the following two
lines to retrieve the file. If you place the file 'plates.py' in the
same directory as 'test_plates.py', then comment these two lines
"""
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'ps2'))

from plates import is_valid

def test_valid_plate():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_no_end_number():
    assert is_valid("CS50P") == False

def test_symbols():
    assert is_valid("PI3.14") == False

def test_short_str():
    assert is_valid("H") == False

def test_long_str():
    assert is_valid("OUTATIME") == False
