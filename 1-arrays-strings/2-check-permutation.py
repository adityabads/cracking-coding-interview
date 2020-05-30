# Check Permutation
# Given two strings, write a method to decide if one is a permutation of the other.

from collections import defaultdict
import unittest


def is_perm(s1: str, s2: str) -> bool:
    """Returns true iff `s1` and `s2` are permutations of another"""
    if len(s1) != len(s2):
        return False
    d = defaultdict(int)
    for c in s1:
        d[c] += 1
    for c in s2:
        d[c] -= 1
    for c in d:
        if d[c] != 0:
            return False
    return True


class TestCheckPermutation(unittest.TestCase):
    def test_is_perm(self):
        trues = [
            ["", ""],
            ["abcdee", "abcdee"],
            ["abcdee", "bdecae"],
            ["abcdee", "eecbad"]
        ]

        falses = [
            ["", "a"],
            ["a", ""],
            ["abcdee", "eEcbad"],   # case sensitive
            ["abcdee", "bdeecb"],
            ["abc", "abcb"]
        ]

        for s1, s2 in trues:
            self.assertTrue(is_perm(s1, s2))
        for s1, s2 in falses:
            self.assertFalse(is_perm(s1, s2))


if __name__ == "__main__":
    unittest.main()
