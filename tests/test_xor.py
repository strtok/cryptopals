from base64 import b16encode, b64decode
from cryptopals.xor import find_key, find_keysize, xor16, xor
from itertools import cycle


def test_xor16():
    assert (
        xor16(
            "1c0111001f010100061a024b53535009181c",
            "686974207468652062756c6c277320657965",
        )
        == "746865206b696420646f6e277420706c6179"
    )

    assert (
        b16encode(
            xor(
                b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal",
                cycle(b"ICE"),
            )
        )
        .decode("utf-8")
        .lower()
        == "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    )


def test_find_keysize():
    ctext = b64decode(
        "AzA7IiwxOGU4ISBrPyQmICA9PzxrJyswLjc9NjMuPiokLiF5MisvciExOyA3NyAlJmU7JWUtOyAiIGU5JDExNjc4ciQgaycwITEjcm0wIjYpPyQyOyszayQ1JzciMSw1JywtKmxncichP2UxNiQnJi0tazUsIzUiNzZ0LDc2JGU6Jyw3ICkgcyQlNmU2LiIwPWU8Myk/Iis+czEjNzcxKiMtNjdlchUhOzUwNjZrNSA6Ljc4PykycjIxIiIxc32p0tZlfWU2KWVjYmtmeKfZwHVlZnB0ICJwczYjPTcgJzx5MiM/Nzd0KSwrJy1nciExOyA3NywlNWU7JWUtOyBrMDcxLiF3"
    )
    assert find_keysize(ctext, range(2, 42)) == 9
    assert find_keysize(ctext, range(2, 42), nresults=3) == [9, 36, 27]


def test_find_key():
    ptext = b"PUPPIES LIKE WAFFLES IN THE MORNING FOR BREAKFAST AND THIS IS A VERY LONG STORY ABOUT PUPPIES AND THEIR LOVE FOR BREAKFAST FOODS THAT INCLUDE BUTTER AND MAPLE SYRUP AND ALL THE DELICIOUS THINGS THAT DOGS NEED TO SURVIVE ON A DAY TO DAY BASIS"
    ctext = xor(ptext, cycle(b"SEKRET"))
    assert find_key(ctext, 6) == b"SEKRET"
