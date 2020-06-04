# Validate BST
# Implement a function to check if a binary tree is a binary search tree.

from mybinarytree import TreeNode, make_binary_tree
import unittest


def is_bst(root: TreeNode, minval: float = float("-inf"), maxval: float = float("inf")) -> bool:
    """Returns true iff root is a binary search tree with all nodes in (minval, maxval)"""
    if root is None:
        return True
    if root.val <= minval or root.val > maxval:
        return False
    return is_bst(root.left, minval, root.val) and is_bst(root.right, root.val, maxval)


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


if __name__ == "__main__":
    unittest.main()
