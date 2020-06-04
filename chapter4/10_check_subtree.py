# Check Subtree
# T1 and T2 are two very large binary trees, with T1 much bigger than T2.
# Create an algorithm to determine if T2 is a subtree of T1. A tree T2 is a
# subtree of T1 if there exists a node n in T1 such that the subtree of n
# is identical to T2. That is, if you cut off the tree at node n, the two
# trees would be identical.

from collections import deque
from mybinarytree import TreeNode, make_binary_tree
import unittest


def is_subtree(t1: TreeNode, t2: TreeNode) -> bool:
    """Returns if `t2` is a subtree of `t1` (by values, not reference)"""
    if t2 is None:
        return True
    if t1 is None:
        return False
    q = deque([t1])
    while q:
        n = q.popleft()
        if n.val == t2.val and is_matching_tree(n, t2):
            return True
        if n.left is not None:
            q.append(n.left)
        if n.right is not None:
            q.append(n.right)
    return False


def is_matching_tree(t1: TreeNode, t2: TreeNode) -> bool:
    """Returns true iff `t1` and `t2` are the same trees (by values, not reference)"""
    if t1 is None and t2 is None:
        return True
    elif t1 is None or t2 is None:
        return False
    elif t1.val != t2.val:
        return False
    return is_matching_tree(t1.left, t2.left) and is_matching_tree(t1.right, t2.right)


class TestCheckSubtree(unittest.TestCase):
    def test_check_has_subtree(self):
        tree1 = make_binary_tree([i for i in range(1, 8)])
        tree2 = make_binary_tree([2, 4, 5])
        tree3 = make_binary_tree([i for i in range(1, 7)])
        trues = [
            [tree1, tree1],
            [tree1, tree1.left],
            [tree1.left, tree1.left.left],
            [tree1, tree1.right.left],
            [tree1, tree2],
            [tree1, None],
            [None, None]
        ]
        falses = [
            [tree1.left, tree1],
            [tree1.left.left, tree1.left],
            [tree1.left, tree1.right],
            [tree1.right, tree1.left],
            [tree2, tree1],
            [tree1, tree3],
            [None, tree1]
        ]
        for t1, t2 in trues:
            with self.subTest(t1=t1.val if t1 is not None else None,
                              t2=t2.val if t2 is not None else None):
                self.assertTrue(is_subtree(t1, t2))
        for t1, t2 in falses:
            with self.subTest(t1=t1.val if t1 is not None else None,
                              t2=t2.val if t2 is not None else None):
                self.assertFalse(is_subtree(t1, t2))


if __name__ == "__main__":
    unittest.main()
