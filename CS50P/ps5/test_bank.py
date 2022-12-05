"""
Since 'bank.py' is in another directory, I need the following two
lines to retrieve the file. If you place the file 'bank.py' in the
same directory as 'test_bank.py', then comment these two lines
"""
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'ps1'))

from bank import value

def test_hello():
    assert value("Hello") == "$0"

def test_hello_name():
    assert value("Hello, Newman") == "$0"

def test_start_h():
    assert value("How you doing?") == "$20"

def test_no_start_h():
    assert value("What's happening?") == "$100"
