from numb3rs import validate

def test_string():
    assert validate("cat") == False
    assert validate("broom") == False
    assert validate("Hello") == False

def test_bad_ip():
    assert validate("1192.1168.11.11") == False
    assert validate("375.456.7689.65454.23") == False
    assert validate("128.263.5.4") == False
    assert validate("256.256.256.256") == False


def test_valid_ip():
    assert validate("172.16.112.1") == True
    assert validate("128.123.5.4") == True
    assert validate("1.0.5.255") == True
    assert validate("254.253.252.251") == True