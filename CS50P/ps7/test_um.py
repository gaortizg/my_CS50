from um import count

def test_valid_um():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2


def test_invalid_um():
    assert count("Instrument") == 0
    assert count("Album") == 0
    assert count("Drink some rum with that") == 0
    assert count("The circumstances of the album") == 0