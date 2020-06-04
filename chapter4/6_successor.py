# Successor
# Write an algorithm to find the "next" node (i.e., in-order successor) of a
# given node in a binary search tree. You may assume that each node has a link
# to its parent.

from mybinarytree import TreeNode, make_binary_tree
import unittest


def successor(n: TreeNode) -> TreeNode:
    """Returns in-order successor of node in binary tree"""
    if n is None:
        return None
    # if right subtree, return leftmost child of right subtree
    if n.right is not None:
        n = n.right
        while n.left is not None:
            n = n.left
        return n
    # else, backtrack until find new right subtree
    while n.parent is not None and n.parent.right is n:
        n = n.parent
    return n.parent


class TestSuccessor(unittest.TestCase):
    def test_successor(self):
        tree = make_binary_tree([1, 2, 3, 4, 5, 6, None, 7])
        self.assertEqual(successor(tree.left).val, 5)
        self.assertEqual(successor(tree.left.left).val, 2)
        self.assertEqual(successor(tree.left.right).val, 1)
        self.assertEqual(successor(tree).val, 6)
        self.assertEqual(successor(tree.right.left).val, 3)
        self.assertIsNone(successor(tree.right))


if __name__ == "__main__":
    unittest.main()
