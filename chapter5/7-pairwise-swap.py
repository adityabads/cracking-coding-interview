# Pairwise Swap
# Write a program to swap odd and even bits in an integer with as few
# instructions as possible (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3
# are swapped, and so on).

import unittest


def pairwise_bit_swap(n: int) -> int:
    """Returns `n` with odd and even bits swapped"""
    # 0b0101 == 0x5, 0b1010 == 0xA,
    oddmask = 0x55555555
    evenmask = 0xAAAAAAAA
    return ((n & oddmask) << 1) | ((n & evenmask) >> 1)


class TestPairwiseSwap(unittest.TestCase):
    def test_pairwise_bit_swap(self):
        tests = [
            # n, expected
            [0b11111111, 0b11111111],
            [0b00000000, 0b00000000],
            [0b10101010, 0b01010101],
            [0b10010110, 0b01101001],
            [0b10000100, 0b01001000]
        ]

        for n, expected in tests:
            self.assertEqual(pairwise_bit_swap(n), expected)
            self.assertEqual(expected, pairwise_bit_swap(n))


if __name__ == "__main__":
    unittest.main()
