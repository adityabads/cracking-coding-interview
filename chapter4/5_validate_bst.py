# Validate BST
# Implement a function to check if a binary tree is a binary search tree.

from mybinarytree import TreeNode, make_binary_tree
from mybst import make_bst, is_bst
import unittest


class TestValidateBST(unittest.TestCase):
    def test_is_bst(self):
        bsts = [
            [8, 4, 10, 2, 6, None, 20],
            [6, 6, 10, 2, None, 9, 20],
            [6, 4, 7, 2, 5, None, 20]
        ]
        not_bsts = [
            [8, 4, 10, 2, 6, 20],
            [8, 4, 10, 2, 12, None, 20],
            [8, 4, 8, 2, 6, None, 20],
            [1, 2, 3, 4, 5]
        ]

        for arr in bsts:
            with self.subTest(arr=arr):
                tree = make_binary_tree(arr)
                self.assertTrue(is_bst(tree))
        for arr in not_bsts:
            with self.subTest(arr=arr):
                tree = make_binary_tree(arr)
                self.assertFalse(is_bst(tree))
                tree = make_bst(arr)
                self.assertTrue(is_bst(tree))


if __name__ == "__main__":
    unittest.main()
