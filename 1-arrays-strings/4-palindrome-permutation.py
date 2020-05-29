# Palindrome Permutation
# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters. The palindrome does not need to be
# limited to just dictionary words.
#
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.)

from collections import defaultdict
import unittest


def is_palin_perm(s: str) -> bool:
    """Return true iff `s` is a permutation of a palindrome (or empty)"""
    d = defaultdict(int)
    for c in s:
        if c.isalpha():
            d[c.lower()] += 1
    # must be even number of every letter, excepting at most one letter
    isoddcount = False
    for c in d:
        if d[c] % 2 == 1:
            if isoddcount:
                return False
            isoddcount = True
    return True


class TestPalindromePermutation(unittest.TestCase):
    def test_is_palin_perm(self):
        self.assertTrue(is_palin_perm(""))
        self.assertTrue(is_palin_perm("a"))
        self.assertTrue(is_palin_perm("Aa"))
        self.assertTrue(is_palin_perm("aaB"))
        self.assertTrue(is_palin_perm("TacOcat"))
        self.assertTrue(is_palin_perm("Tact Coa"))
        self.assertTrue(is_palin_perm("Raecca r"))
        self.assertTrue(is_palin_perm("raceecar"))

        self.assertFalse(is_palin_perm("Raeccb r"))
        self.assertFalse(is_palin_perm("Raeca r"))
        self.assertFalse(is_palin_perm("aloha"))


if __name__ == "__main__":
    unittest.main()
