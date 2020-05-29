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
        self.assertTrue(is_perm("", ""))
        self.assertTrue(is_perm("abcdee", "abcdee"))
        self.assertTrue(is_perm("abcdee", "bdecae"))
        self.assertTrue(is_perm("abcdee", "eecbad"))

        self.assertFalse(is_perm("", "a"))
        self.assertFalse(is_perm("a", ""))
        self.assertFalse(is_perm("abcdee", "eEcbad"))
        self.assertFalse(is_perm("abcdee", "bdeecb"))
        self.assertFalse(is_perm("abc", "abcb"))


if __name__ == "__main__":
    unittest.main()
