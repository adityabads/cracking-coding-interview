# Draw Line
# A monochrome screen is stored as a single array of bytes, allowing eight
# consecutive pixels to be stored in one byte. The screen has width w,
# where w is divisible by 8 (that is, no byte will be split across rows).
# The height of the screen, of course, can be derived from the length of the
# array and the width. Implement a function that draws a horizontal line from
# (x1, y) to (x2, y). The method signature should look something like:
# drawline(byte[] screen, int width, int x1, int x2, int y)

import unittest


def draw_line(screen: int, length: int, width: int, x1: int, x2: int, y: int) -> int:
    """Draw line from (x1, y) to (x2, y), 1-indexed starting from upper left"""
    mask = 0
    for _ in range(x1, x2 + 1):
        mask |= (1 << (width - y))
        mask <<= width
    for _ in range(length - x2 - 1):
        mask <<= width
    return screen | mask


def visualize(screen: int, width: int) -> None:
    n = bin(screen)[2:]
    for i, val in enumerate(n):
        print(val, end=" ")
        if (i + 1) % width == 0:
            print()
    print()


class TestDrawLine(unittest.TestCase):
    def test_draw_line(self):
        screen = 1 << 127
        length = 8
        width = 16
        tests = [
            [3, 4, 5],
            [2, 7, 9],
            [2, 4, 1],
            [4, 4, 1],
            [1, 1, 8]
        ]
        for x1, x2, y in tests:
            newscreen = draw_line(screen, length, width, x1, x2, y)
            visualize(newscreen, width)


if __name__ == "__main__":
    unittest.main()
