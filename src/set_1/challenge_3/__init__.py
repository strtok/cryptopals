from cryptopals.xor import xor
from cryptopals.text import score
from base64 import b16decode


def main():
    ctext = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    ctext_bytes = b16decode(ctext, casefold=True)

    for key in range(255):
        xor_key = bytes(key for _ in range(len(ctext_bytes)))
        ptext = xor(ctext_bytes, xor_key)
        if score(ptext) < 50:
            print(f"candidate key '0x{key:x}': '{ptext}'")


if __name__ == "__main__":
    main()
