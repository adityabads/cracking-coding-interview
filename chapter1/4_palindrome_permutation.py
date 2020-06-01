# Palindrome Permutation
# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters. The palindrome does not need to be
# limited to just dictionary words.
#
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.)

from collections import Counter
import unittest


def is_palin_perm(s: str) -> bool:
    """Return true iff `s` is a permutation of a palindrome (or empty)"""
    # must be even number of every letter, excepting at most one letter
    counts = Counter(s.lower())
    isoddcount = False
    for c in counts:
        if c.isalpha() and counts[c] % 2 == 1:
            if isoddcount:
                return False
            isoddcount = True
    return True


class TestPalindromePermutation(unittest.TestCase):
    def test_is_palin_perm(self):
        trues = ["", "a", "Aa", "aab", "TaCocat",
                 "Tact Coa ", "Raecca r", "raceecar"]
        falses = ["abc", "Raeccb r", "Raeca r", "aloha"]

        for test in trues:
            with self.subTest(test=test):
                self.assertTrue(is_palin_perm(test))
        for test in falses:
            with self.subTest(test=test):
                self.assertFalse(is_palin_perm(test))


if __name__ == "__main__":
    unittest.main()
