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
    diff = len(s1) - len(s2)
    if diff < -1 or diff > 1:
        return False
    # make `s1` the smaller string
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
        self.assertTrue(one_away("", ""))
        self.assertTrue(one_away("a", ""))
        self.assertTrue(one_away("", "a"))
        self.assertTrue(one_away("pale", "pale"))
        self.assertTrue(one_away("pale", "ple"))
        self.assertTrue(one_away("pales", "pale"))
        self.assertTrue(one_away("pale", "pald"))
        self.assertTrue(one_away("pale", "bale"))

        self.assertFalse(one_away("pale", "plea"))
        self.assertFalse(one_away("", "ac"))
        self.assertFalse(one_away("ac", ""))
        self.assertFalse(one_away("pale", "bake"))
        self.assertFalse(one_away("pal", "pull"))


if __name__ == "__main__":
    unittest.main()
