# Is Unique
# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

import unittest


def all_chars_unique(s: str) -> bool:
    """Returns true iff all chars in `s` are unique (or empty)"""
    bitvec = 0
    for c in s:
        if in_bitvec(bitvec, ord(c)):
            return False
        bitvec = add_to_bitvec(bitvec, ord(c))
    return True


def in_bitvec(bitvec: int, ind: int) -> bool:
    """Returns true iff bit `ind` is switched on in `bitvec`"""
    return (bitvec & (1 << ind)) != 0


def add_to_bitvec(bitvec: int, ind: int) -> int:
    """Returns `bitvec` with bit `ind` switched on"""
    return bitvec | (1 << ind)


class TestIsUnique(unittest.TestCase):
    def test_all_chars_unique(self):
        trues = ["", "a", "abc", "Aabc;3"]
        falses = ["aa", "aabc;3", "abc3;3"]

        for test in trues:
            with self.subTest(test=test):
                self.assertTrue(all_chars_unique(test))
        for test in falses:
            with self.subTest(test=test):
                self.assertFalse(all_chars_unique(test))


if __name__ == "__main__":
    unittest.main()
