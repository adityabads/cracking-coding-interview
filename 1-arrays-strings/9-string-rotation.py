# String Rotation
# Assume you have a method `is_substring` which checks if one word is a substring
# of another. Given two strings, `s1` and `s2`, write code to check if `s2` is a
# rotation of `s1` using only one call to `is_substring` (e.g., "waterbottle"
# is a rotation of "erbottlewat").

import unittest


def is_rotated(s1: str, s2: str) -> bool:
    """Returns true iff s1 and s2 are rotations of each other"""
    if len(s1) != len(s2):
        return False
    return is_substring(s1, s2 * 2)


def is_substring(s1: str, s2: str) -> bool:
    """Returns true iff `s1` is a substring of `s2`"""
    # (To satisfy the problem)
    return s1 in s2


class TestStringRotation(unittest.TestCase):
    def test_is_rotated(self):
        trues = [
            ["", ""],
            ["waterbottle", "erbottlewat"],
            ["waaawa", "wawaaa"],
            ["waaawa", "aawawa"],
            ["aaaaaa", "aaaaaa"]
        ]

        falses = [
            ["", "a"],
            ["a", ""],
            ["aawaaaw", "aaawawa"],
            ["aawaaw", "aaawawa"]
        ]

        for s1, s2 in trues:
            self.assertTrue(is_rotated(s1, s2))
        for s1, s2 in falses:
            self.assertFalse(is_rotated(s1, s2))


if __name__ == "__main__":
    unittest.main()
