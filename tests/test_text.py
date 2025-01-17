from cryptopals.text import score, hamming_distance
from pytest import approx


def test_score():
    assert score(b"This is a normal English phrase") == approx(13.01431)
    assert score(b"zzjfiejimaifnizzzzzszisfjeizzzz") == approx(15598.14137)


def test_hamming_distance():
    assert hamming_distance(b"foo", b"foob") == 8
    assert hamming_distance(b"foob", b"foo") == 8
    assert hamming_distance(b"this is a test", b"wokka wokka!!!") == 37
