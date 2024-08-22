#!/usr/bin/python3
"""UTF-8 Validation"""


def get_leading_set_bits(num):
    """Returns the number of leading 1 bits in an integer."""
    set_bits = 0
    helper = 1 << 7  # 10000000
    while helper & num:
        set_bits += 1
        helper >>= 1
    return set_bits


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding."""
    bits_count = 0

    for byte in data:
        if bits_count == 0:
            bits_count = get_leading_set_bits(byte)

            if bits_count == 0:
                continue

            if bits_count == 1 or bits_count > 4:
                return False
        else:
            # Check if the byte follows the format 10xxxxxx
            if not (byte & (1 << 7) and not (byte & (1 << 6))):
                return False

        bits_count -= 1

    return bits_count == 0

