# Next Number
# Given a positive integer, print the next smallest and the next largest number
# that have the same number of 1 bits in their binary representation

import unittest


def get_next(n: int) -> int:
    """Returns minimum larger int with equal number of 1 bits"""
    reached_rightmost_1 = False
    flipbit = None                  # flip rightmost 0 left of a 1
    count_1s_right_of_flipbit = 0
    i = 0
    copyn = n
    while copyn > 0:
        bit = copyn & 1
        if bit == 1:
            if not reached_rightmost_1:
                reached_rightmost_1 = True
            else:
                count_1s_right_of_flipbit += 1
        elif bit == 0 and reached_rightmost_1:
            flipbit = i
            break
        i += 1
        copyn >>= 1
    if flipbit is None:
        flipbit = i

    # turn on flipbit, move all ones to the right of flipbit to the end
    return ((n | (1 << flipbit)) & (-1 << flipbit)) | ~(-1 << count_1s_right_of_flipbit)


def get_prev(n: int) -> int:
    """Returns maximum smaller int with equal number of 1 bits"""
    reached_rightmost_0 = None
    flipbit = None                  # flip rightmost 1 left of 0
    count_0s_right_of_flipbit = 0
    i = 0
    copyn = n
    while copyn > 0:
        bit = copyn & 1
        if bit == 0:
            if not reached_rightmost_0:
                reached_rightmost_0 = True
            else:
                count_0s_right_of_flipbit += 1
        elif bit == 1 and reached_rightmost_0:
            flipbit = i
            break
        i += 1
        copyn >>= 1
    if flipbit is None:
        flipbit = i

    # turn off flipbit, move all zeros right of flipbit to the end
    return ((n & ~(1 << flipbit)) | ~(-1 << flipbit)) & (-1 << count_0s_right_of_flipbit)


class TestNextNumber(unittest.TestCase):
    def test_get_prev(self):
        tests = [
            [0b100100, 0b100010],
            [0b001100, 0b001010],
            [0b110001, 0b101100],
            [0b000011, 0b000011]
        ]
        for n, prev in tests:
            with self.subTest(n=bin(n)):
                print(bin(get_prev(n)))
                self.assertEqual(get_prev(n), prev)

    def test_get_next(self):
        tests = [
            [0b100100, 0b101000],
            [0b001100, 0b010001],
            [0b110001,  0b110010],
            [0b000011,  0b000101]
        ]
        for n, next_ in tests:
            with self.subTest(n=bin(n)):
                self.assertEqual(get_next(n), next_)


if __name__ == "__main__":
    unittest.main()
