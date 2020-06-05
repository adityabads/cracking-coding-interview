# String Compression
# Implement a method to perform basic string compression
# using the counts of repeated characters. For example, the string aabcccccaaa
# would become a2b1c5a3. If the "compressed" string would not become smaller
# than the original string, your method should return the original string.
# You can assume the string has only uppercase and lowercase letters (a - z).

import unittest


def compress(s: str) -> str:
    """Compresses repeated characters if would make a shorter string"""
    if not s:
        return s

    # count repeated characters, store in array
    compressed = []
    count = 0
    for i in range(len(s)):
        if i != 0 and s[i] != s[i - 1]:
            compressed.append(f"{s[i - 1]}{count}")
            count = 0
        count += 1
    compressed.append(f"{s[-1]}{count}")

    # return compressed string if shorter than original
    return min(s, "".join(compressed), key=len)


class TestStringCompression(unittest.TestCase):
    def test_compress(self):
        tests = [
            ["", ""],
            ["a", "a"],
            ["aa", "aa"],
            ["abc", "abc"],
            ["aaa", "a3"],
            ["aabcccccaaa", "a2b1c5a3"]
        ]

        for string, expected in tests:
            with self.subTest(string=string):
                self.assertEqual(compress(string), expected)


if __name__ == "__main__":
    unittest.main()
