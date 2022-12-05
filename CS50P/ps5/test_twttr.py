"""
Since 'twttr.py' is in another directory, I need the following two
lines to retrieve the file. If you place the file 'twttr.py' in the
same directory as 'test_twttr.py', then comment these two lines
"""
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'ps2'))

from twttr import shorten
"""
Make sure 'twttr.py' is in the same folder as this file
"""
def test_one_word():
    assert shorten("Twitter") == "Twttr"

def test_long_phrase():
    assert shorten("What's your name?") == "Wht's yr nm?"

def test_number():
    assert shorten("CS50") == "CS50"

def test_different_case():
    assert shorten("HELLO, my world of bEaUtiEs") == "HLL, my wrld f bts"
