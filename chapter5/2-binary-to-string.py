# Binary to String
# Given a real number between O and 1 (e.g., 0.72) that is passed in as a double,
# print the binary representation. If the number cannot be represented accurately
# in binary with at most 32 characters, print "ERROR".

import unittest


def to_binary_string(n: float) -> str:
    if n <= 0 or n >= 1:
        raise Exception("to_binary_string() requires float between 0 and 1")
    result = ["."]
    frac = 0.5
    while n > 0:
        if len(result) >= 32:
            return "ERROR"
        n *= 2
        if n >= 1:
            result.append("1")
            n -= 1
        else:
            result.append("0")
    return "".join(map(str, result))


class TestBinaryString(unittest.TestCase):
    def test_to_binary_string(self):
        self.assertEqual(to_binary_string(.5), ".1")
        self.assertEqual(to_binary_string(.25), ".01")
        self.assertEqual(to_binary_string(.125), ".001")
        self.assertEqual(to_binary_string(.625), ".101")
        self.assertEqual(to_binary_string(.1), "ERROR")


if __name__ == '__main__':
    unittest.main()
