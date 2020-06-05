# List of Depths
# Given a binary tree, design an algorithm which creates a list of all the
# nodes at each depth (e.g., if you have a tree with depth D, you'll have D lists).

from collections import deque
from mybinarytree import TreeNode, make_binary_tree
from typing import List
import unittest


def list_of_depths(root: TreeNode) -> List[TreeNode]:
    """Return list of nodes at each depth of tree"""
    # modified level-order traversal
    nodes = []
    q = deque([root])
    while q:
        num_nodes_in_level = len(q)
        nodes_in_level = []
        while num_nodes_in_level > 0:
            n = q.popleft()
            nodes_in_level.append(n)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
            num_nodes_in_level -= 1
        nodes.append(nodes_in_level)
    return nodes


class TestListOfDepths(unittest.TestCase):
    def test_list_of_depths(self):
        arrs = [[i for i in range(1, 7)],
                [i for i in range(1, 8)],
                [i for i in range(1, 9)],
                [i for i in range(1, 10)],
                [1, 2, 3, 4, 5, 6, None, 7]]
        for arr in arrs:
            tree = make_binary_tree(arr)
            depths = list_of_depths(tree)
            for depth in depths:
                for node in depth:
                    print(node, end=" ")
                print()
            print()


if __name__ == "__main__":
    unittest.main()
