# Flip Bit to Win
# You have an integer and you can flip exactly one bit from a 0 to a 1.
# Write code to find the length of the longest sequence of 1s you could create.
#
# EXAMPLE
# Input: 1775 (or: 11011101111)
# Output: 8

import unittest


def flip_bit_to_win(n: int) -> int:
    """Returns length of the longest sequence of 1s by flipping one bit"""
    maxlen = 0
    prevgrouplen = 0
    thisgrouplen = 0
    while n > 0:
        bit = n & 1
        if bit == 1:
            thisgrouplen += 1
        else:
            maxlen = max(maxlen, prevgrouplen + thisgrouplen + 1)
            prevgrouplen = thisgrouplen
            thisgrouplen = 0
        n >>= 1
    maxlen = max(maxlen, prevgrouplen + thisgrouplen + 1)
    return maxlen


class TestFlipBitToWin(unittest.TestCase):
    def test_flip_bit_to_win(self):
        tests = [
            # n, expected
            [0b11011101111, 8],
            [0b00000000000, 1],
            [0b11111111111, 12],
            [0b11000111001, 4],
            [0b11001110110, 6]
        ]
        for n, expected in tests:
            with self.subTest(n=bin(n)):
                self.assertEqual(flip_bit_to_win(n), expected)


if __name__ == "__main__":
    unittest.main()
