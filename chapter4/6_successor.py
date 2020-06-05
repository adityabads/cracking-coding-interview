# Successor
# Write an algorithm to find the "next" node (i.e., in-order successor) of a
# given node in a binary search tree. You may assume that each node has a link
# to its parent.

from mybinarytree import TreeNode, make_binary_tree
import unittest


def in_order_successor(n: TreeNode) -> TreeNode:
    """Returns in-order successor of node in binary tree"""
    if not n:
        return None
    # if right subtree, return leftmost child of right subtree
    if n.right:
        n = n.right
        while n.left:
            n = n.left
        return n
    # else, backtrack until find new right subtree
    while n.parent and n.parent.right is n:
        n = n.parent
    return n.parent


class TestSuccessor(unittest.TestCase):
    def test_successor(self):
        tree = make_binary_tree([1, 2, 3, 4, 5, 6, None, 7])
        tests = [
            # node, successor
            [tree.left, tree.left.right],
            [tree.left.left, tree.left],
            [tree.left.left.left, tree.left.left],
            [tree.left.right, tree],
            [tree, tree.right.left],
            [tree.right.left, tree.right],
            [tree.right, None],
            [None, None]
        ]
        for node, successor in tests:
            with self.subTest(node=node.val if node else None):
                self.assertIs(in_order_successor(node), successor)


if __name__ == "__main__":
    unittest.main()
