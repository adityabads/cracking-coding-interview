# One Away
# There are three types of edits that can be performed on strings: insert a
# character, remove a character, or replace a character. Given two strings,
# write a function to check if they are one edit (or zero edits) away.
#
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false

import unittest


def one_away(s1: str, s2: str) -> bool:
    """Returns true if `s1` and `s2` are one char different"""
    # make `s1` the smaller string
    diff = len(s1) - len(s2)
    if abs(diff) > 1:
        return False
    if diff > 0:
        s1, s2 = s2, s1
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            # true iff can remove char or replace char
            # (removing char equivalent to inserting char)
            return s1[i:] == s2[i+1:] or s1[i+1:] == s2[i+1:]
    return True


class TestOneAway(unittest.TestCase):
    def test_one_away(self):
        trues = [
            ["", ""],
            ["a", ""],
            ["", "a"],
            ["pale", "pale"],
            ["pale", "ple"],
            ["pale", "pales"],
            ["pale", "pald"],
            ["pale", "bale"]
        ]

        falses = [
            ["pale", "plea"],   # not all palindromes count
            ["", "ac"],
            ["ac", ""],
            ["pale", "bake"],
            ["pal", "pull"]
        ]

        for s1, s2 in trues:
            with self.subTest(s1=s1, s2=s2):
                self.assertTrue(one_away(s1, s2))
        for s1, s2 in falses:
            with self.subTest(s1=s1, s2=s2):
                self.assertFalse(one_away(s1, s2))


if __name__ == "__main__":
    unittest.main()
