# Rotate Matrix
# Given an image represented by an NxN matrix, where each pixel in the image
# is 4 bytes, write a method to rotate the image by 90 degrees counterclockwise.
# Can you do this in place?

from typing import List
import unittest


def rotate_matrix(mat: List[List[int]]):
    """Rotates matrix `mat` counterclockwise 90 degrees"""
    n = len(mat)
    # iterate over each square "layer", starting from outer layer and moving inward
    for i in range(n // 2):
        # iterate over matrix entries on each edge
        for j in range(n - 2 * i - 1):
            # 4-way swap matrix entries between edges
            coords = [(i, j)]
            for k in range(1, 4):
                coords.append(rotate_coord(
                    coords[k - 1][0], coords[k - 1][1], n))
            temp = mat[coords[3][0]][coords[3][1]]
            for k in reversed(range(1, 4)):
                mat[coords[k][0]][coords[k][1]
                                  ] = mat[coords[k - 1][0]][coords[k - 1][1]]
            mat[coords[0][0]][coords[0][1]] = temp


def rotate_coord(x: int, y: int, n: int) -> (int, int):
    """Returns (x, y) indices rotated counterclockwise 90 degrees in n-by-n matrix"""
    center = (n - 1) / 2
    x -= center
    y -= center
    x, y = -1 * y, x
    x += center
    y += center
    return int(x), int(y)


class TestRotateMatrix(unittest.TestCase):
    def test_rotate_matrix(self):
        tests = [
            [
                [[0]],
                [[0]]
            ],
            [
                [[1, 2], [3, 4]],
                [[2, 4], [1, 3]]
            ],
            [
                [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
            ]
        ]

        for matrix, rotated in tests:
            rotate_matrix(matrix)
            self.assertEqual(matrix, rotated)

    def test_rotate_coord(self):
        tests = [
            [(0, 0, 1), (0, 0)],
            [(0, 0, 2), (1, 0)],
            [(0, 1, 2), (0, 0)],
            [(1, 0, 2), (1, 1)],
            [(1, 1, 2), (0, 1)],
            [(0, 0, 3), (2, 0)],
            [(0, 1, 3), (1, 0)],
            [(0, 2, 3), (0, 0)],
            [(1, 0, 3), (2, 1)],
            [(1, 1, 3), (1, 1)],
            [(1, 2, 3), (0, 1)],
            [(2, 0, 3), (2, 2)],
            [(2, 1, 3), (1, 2)],
            [(2, 2, 3), (0, 2)]
        ]

        for (x, y, n), rotated in tests:
            self.assertEqual(rotate_coord(x, y, n), rotated)


if __name__ == "__main__":
    unittest.main()
