from cryptopals.text import score, hamming_distance, profile_for, obj_encode, obj_decode
from pytest import approx


def test_score():
    assert score(b"This is a normal English phrase") == approx(13.01431)
    assert score(b"zzjfiejimaifnizzzzzszisfjeizzzz") == approx(15598.14137)


def test_hamming_distance():
    assert hamming_distance(b"foo", b"foob") == 8
    assert hamming_distance(b"foob", b"foo") == 8
    assert hamming_distance(b"this is a test", b"wokka wokka!!!") == 37


def test_profile_for():
    assert profile_for("strtok@gmail.com") == "email=strtok@gmail.com&uid=10&role=user"
    assert (
        profile_for("strtok@==gm&&ail.com") == "email=strtok@gmail.com&uid=10&role=user"
    )


def test_obj_encode_decode():
    assert obj_decode(obj_encode({"foo": "10", "bar": "20"})) == {
        "foo": "10",
        "bar": "20",
    }
