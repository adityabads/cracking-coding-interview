# Is Unique
# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

import unittest


def all_chars_unique(s: str) -> bool:
    """Returns true iff all chars in `s` are unique (or empty)"""
    bitvec = 0
    for c in s:
        if bitvec & (1 << ord(c)):
            return False
        bitvec |= (1 << ord(c))
    return True


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
