# Conversion
# Write a function to determine the number of bits you would need to flip to
# convert integer A to integer B.
#
# EXAMPLE
# Input: 29 (or: 11101), 15 (or: 01111)
# Output: 2

import unittest


def bits_different(a: int, b: int) -> int:
    """Returns number of different bits between `a` and `b`"""
    xor = a ^ b
    diffbits = 0
    while xor > 0:
        if xor & 1 == 1:
            diffbits += 1
        xor >>= 1
    return diffbits


class TestConversion(unittest.TestCase):
    def test_bits_different(self):
        tests = [
            # a, b, expected
            [0b11101, 0b01111, 2],
            [0b11001, 0b00001, 2],
            [0b10101, 0b10101, 0]
        ]

        for a, b, expected in tests:
            self.assertEqual(bits_different(a, b), expected)
            self.assertEqual(bits_different(b, a), expected)


if __name__ == "__main__":
    unittest.main()
