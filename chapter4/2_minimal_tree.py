# Minimal Tree
# Given a sorted (increasing order) array with unique integer elements, write
# an algorithm to create a binary search tree with minimal height.

from mybinarytree import TreeNode, level_traverse_iterative
from typing import List
import unittest


def make_minimal_bst(arr: List[int], i: int = 0, j: int = None) -> TreeNode:
    if j is None:
        j = len(arr)
    n = None
    if i < j:
        mid = (i + j) // 2
        n = TreeNode(arr[mid])
        n.left = make_minimal_bst(arr, i, (i + j) // 2)
        n.right = make_minimal_bst(arr, (i + j) // 2 + 1, j)
    return n


class TestMinimalTree(unittest.TestCase):
    def test_make_minimal_bst(self):
        arrs = [
            [i for i in range(1, 7)],
            [i for i in range(1, 8)],
            [i for i in range(1, 9)],
            [i for i in range(1, 10)],
            [i for i in range(1, 11)],
            [i for i in range(1, 12)],
        ]
        for arr in arrs:
            tree = make_minimal_bst(arr)
            level_traverse_iterative(tree)


if __name__ == "__main__":
    unittest.main()
