# Random Node
# You are implementing a binary tree class from scratch which, in addition to
# insert, find, and delete, has a method getRandomNode() which returns a random
# node from the tree. All nodes should be equally likely to be chosen. Design
# and implement an algorithm for getRandomNode, and explain how you would
# implement the rest of the methods.

from mybinarytree import TreeNode, make_binary_tree
import random
import unittest


def get_random_node(root: TreeNode) -> TreeNode:
    while root is not None:
        leftsize = root.left.size if root.left is not None else 0
        rightsize = root.right.size if root.right is not None else 0
        rand = random.randint(0, leftsize + rightsize)
        if rand == 0:
            break
        elif rand <= leftsize:
            root = root.left
        else:
            root = root.right
    return root

# The other methods will be implemented as usual, as in `mybst.py`


class TestRandomNode(unittest.TestCase):
    def test_get_random_node(self):
        tree = make_binary_tree([4, 2, 6, 1, 3, 5, 7])
        for i in range(30):
            print(get_random_node(tree), end=" ")
        print()


if __name__ == "__main__":
    unittest.main()
