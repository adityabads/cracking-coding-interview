# Validate BST
# Implement a function to check if a binary tree is a binary search tree.

from mybinarytree import TreeNode, make_binary_tree
import unittest


def is_bst(root: TreeNode) -> bool:
    """Returns true iff root is a binary search tree"""
    return _is_bst_util(root)[0]


def _is_bst_util(root: TreeNode) -> (bool, int, int):
    """Returns true iff root is a binary search tree, and max and min values in tree"""
    if root is None:
        return True, float("inf"), float("-inf")
    isleftbst, leftmin, leftmax = _is_bst_util(root.left)
    isrightbst, rightmin, rightmax = _is_bst_util(root.right)
    isbst = isleftbst and isrightbst and leftmax <= root.val and root.val < rightmin
    return isbst, min(leftmin, root.val, rightmin), max(leftmax, root.val, rightmax)


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
