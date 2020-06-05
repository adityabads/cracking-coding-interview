# Check Balanced
# Implement a function to check if a binary tree is balanced. For the purposes
# of this question, a balanced tree is defined to be a tree such that the
# heights of the two subtrees of any node never differ by more than one.

from mybinarytree import TreeNode, make_binary_tree
import unittest


def is_balanced(root: TreeNode) -> bool:
    """Returns true iff binary tree is balanced (as defined above)"""
    return _is_balanced_util(root)[0]


def _is_balanced_util(root: TreeNode) -> (bool, int):
    """Returns true iff binary tree is balanced, and height of tree"""
    if not root:
        return True, 0
    leftbalanced, leftheight = _is_balanced_util(root.left)
    rightbalanced, rightheight = _is_balanced_util(root.right)
    balanced = leftbalanced and rightbalanced and abs(
        leftheight - rightheight) <= 1
    return balanced, max(leftheight, rightheight) + 1


class TestCheckBalanced(unittest.TestCase):
    def test_is_balanced(self):
        balanced = [
            [i for i in range(1, 7)],
            [i for i in range(1, 8)],
            [i for i in range(1, 9)],
            [i for i in range(1, 10)],
            [1, 2, 3, 4, 5, 6, None, 7]
        ]
        unbalanced = [
            [1, 2, 3, 4, 5, None, None, 7],
            [1, 2, None, 4],
            [1, None, 3, None, None, None, 7]
        ]
        for arr in balanced:
            with self.subTest(arr=arr):
                tree = make_binary_tree(arr)
                self.assertTrue(is_balanced(tree))
        for arr in unbalanced:
            with self.subTest(arr=arr):
                tree = make_binary_tree(arr)
                self.assertFalse(is_balanced(tree))


if __name__ == "__main__":
    unittest.main()
