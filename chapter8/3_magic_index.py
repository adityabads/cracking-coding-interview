# Magic Index
# A magic index in an array A[0 ... n-1] is defined to be an index such that
# A[i] = i. Given a sorted array of distinct integers, write a method to find
# a magic index, if one exists, in array A.
#
# FOLLOW UP
# What if the values are not distinct?

from typing import List
import unittest

# where mid = (i+j)//2,
# f(arr, i, j) =    None,               i >= j
#                   mid,                arr[mid] == mid
#                   f(arr, mid+1, j),   arr[mid] < mid
#                   f(arr, i, mid),     otherwise


def magic_index_recursive(arr: List[int], i: int = 0, j: int = None) -> int:
    if j is None:
        j = len(arr)-1
    if i > j:
        return None
    mid = (i + j) // 2
    if arr[mid] == mid:
        return mid
    elif arr[mid] < mid:
        return magic_index_recursive(arr, mid+1, j)
    else:
        return magic_index_recursive(arr, i, mid-1)


def magic_index(arr: List[int], i: int = 0, j: int = None) -> int:
    if j is None:
        j = len(arr)-1
    while i <= j:
        mid = (i + j) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            i = mid+1
        else:
            j = mid-1
    return None


class TestMagicIndex(unittest.TestCase):
    def test_magic_index(self):
        trues = [
            # array, magic indices
            [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]],
            [[-5, -3, 2, 5, 7], [2]],
            [[0, 4, 7, 9], [0]],
            [[-9, -5, 1, 3, 4], [3, 4]]
        ]
        falses = [
            [1, 2, 3, 4, 5],
            [-5, -3, 3, 4],
            [-9, -5, 1, 2, 3]
        ]
        for arr, indices in trues:
            with self.subTest(arr=arr):
                self.assertIn(magic_index_recursive(arr), indices)
                self.assertIn(magic_index(arr), indices)
        for arr in falses:
            with self.subTest(arr=arr):
                self.assertIsNone(magic_index_recursive(arr))
                self.assertIsNone(magic_index(arr))


if __name__ == "__main__":
    unittest.main()
