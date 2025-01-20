def is_printable(s: bytes) -> bool:
    try:
        decoded = s.decode("utf-8")
        if all(c.isprintable() or c == "\n" for c in decoded):
            return True
        return False
    except Exception:
        return False


ENGLISH_FREQ = {
    b" ": 12.17,
    b".": 6.57,
    b"a": 6.09,
    b"b": 1.05,
    b"c": 2.84,
    b"d": 2.92,
    b"e": 11.36,
    b"f": 1.79,
    b"g": 1.38,
    b"h": 3.41,
    b"i": 5.44,
    b"j": 0.24,
    b"k": 0.41,
    b"l": 2.92,
    b"m": 2.76,
    b"n": 5.44,
    b"o": 6.00,
    b"p": 1.95,
    b"q": 0.24,
    b"r": 4.95,
    b"s": 5.68,
    b"t": 8.03,
    b"u": 2.43,
    b"v": 0.97,
    b"w": 1.38,
    b"x": 0.24,
    b"y": 1.30,
    b"z": 0.03,
}


def score(ptext: bytes) -> float:
    def disqualifying(c):
        return True if (c < 0x20 and c != 0x0A) or c >= 0x7F else False

    # calcuate character counts
    counts: dict[bytes, int] = {}
    for c in ptext:
        if disqualifying(c):
            return 0xFFFFFFFF
        c = bytes([c])
        c = c.lower() if c.isalpha() else b" " if c.isspace() else b"."

        if c not in ENGLISH_FREQ:
            continue

        counts[c] = counts.setdefault(c, 0) + 1

    # calculate a score using chi-squared
    text_len = sum(counts.values())
    total_score = 0
    for c, actual_count in counts.items():
        expected_count = ENGLISH_FREQ[c] * 0.01 * text_len
        chi_square = ((actual_count - expected_count) ** 2) / expected_count
        total_score += chi_square
    return total_score


def hamming_distance(a: bytes, b: bytes) -> int:
    distance = abs(len(a) - len(b)) * 8
    return sum(bin(a ^ b).count("1") for a, b in zip(a, b)) + distance

def print_hexdump(b: bytes) -> None:
    for offset in range(0, len(b), 16):
        chunk = b[offset:offset + 16]
        hex_part = " ".join(f"{byte:02x}" for byte in chunk)
        ascii_part = "".join(chr(byte) if 32 <= byte <= 126 else '.' for byte in chunk)
        print(f"{offset:08x}  {hex_part:<48}  |{ascii_part}|")
