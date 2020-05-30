# Rotate Matrix
# Given an image represented by an NxN matrix, where each pixel in the image
# is 4 bytes, write a method to rotate the image by 90 degrees clockwise.
# Can you do this in place?

from typing import List
import unittest


def rotate_matrix(mat: List[List[int]]):
    """Rotates matrix `mat` clockwise 90 degrees"""
    n = len(mat)
    # iterate over each square "layer", starting from outer layer and moving inward
    for i in range(n // 2):
        # iterate over matrix entries on each edge
        for j in range(i, n - i - 1):
            # 4-way swap matrix entries between edges
            top = mat[i][j]
            mat[i][j] = mat[-j - 1][i]
            mat[-j - 1][i] = mat[-i - 1][-j - 1]
            mat[-i - 1][-j - 1] = mat[j][-i - 1]
            mat[j][-i - 1] = top


class TestRotateMatrix(unittest.TestCase):
    def test_rotate_matrix(self):
        tests = [
            [[
                [0]
            ], [
                [0]
            ]], [[
                [1, 2],
                [3, 4]
            ], [
                [3, 1],
                [4, 2]
            ]], [[
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ], [
                [7, 4, 1],
                [8, 5, 2],
                [9, 6, 3]
            ]]
        ]

        for matrix, rotated in tests:
            rotate_matrix(matrix)
            self.assertEqual(matrix, rotated)


if __name__ == "__main__":
    unittest.main()
