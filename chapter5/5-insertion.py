# Insertion
# You are given two 32-bit numbers, N and M, and two bit positions, i and j.
# Write a method to insert M into N such that M starts at bit j and ends at
# bit i. You can assume that the bits j through i have enough space to fit all
# of M. That is, if M = 10011, you can assume that there are at least 5 bits
# between j and i. You would not, for example, have j = 3 and i = 2, because
# M could not fully fit between bit 3 and bit 2.
#
# EXAMPLE
# Input:  N = 10000000000, M = 10011, i = 2, j = 6
# Output: N = 10001001100

import unittest


def insert(n: int, m: int, i: int, j: int) -> int:
    # clear bits i through j
    # mask = ...111110000011
    #          ind:  j+1 i
    mask = (-1 << (j + 1)) | ((1 << i) - 1)
    # alternatively, mask = -1 ^ ((1 << (j + 1)) - 1) ^ ((1 << i) - 1)
    return (n & mask) | (m << i)


class TestInsertion(unittest.TestCase):
    def test_insert(self):
        tests = [
            # n, m, i, j, expected
            [0b10000000000, 0b10011, 2, 6, 0b10001001100],
            [0b11111111111, 0b10011, 2, 6, 0b11111001111],
            [0b10101010101, 0b10011, 2, 6, 0b10101001101]
        ]
        for n, m, i, j, expected in tests:
            with self.subTest(n=bin(n), m=bin(m), i=i, j=j):
                self.assertEqual(insert(n, m, i, j), expected)


if __name__ == "__main__":
    unittest.main()
