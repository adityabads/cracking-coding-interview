from collections import deque
import unittest


class TreeNode:
    """Node class for binary tree"""

    def __init__(self, val, left=None, right=None, parent=None, size=1):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.size = size

    def __str__(self):
        return str(self.val)

    def __len__(self):
        return self.size


def make_binary_tree(arr) -> TreeNode:
    """Returns a binary tree with values in `arr`"""
    root = None
    if arr:
        root = _insert_level_order(arr, root, 0)
    return root


def _insert_level_order(arr, n: TreeNode, i: int) -> None:
    """Inserts `arr[i]` into tree at node `n` recursively in level order"""
    root = None
    if i < len(arr) and arr[i]:
        # return desired node if in range
        root = TreeNode(arr[i])
        # left node should have value `arr[2*i+1]`
        root.left = _insert_level_order(arr, root.left, 2*i + 1)
        if root.left:
            root.left.parent = root
            root.size += root.left.size
        # right node should have value `arr[2*i+2]`
        root.right = _insert_level_order(arr, root.right, 2*i + 2)
        if root.right:
            root.right.parent = root
            root.size += root.right.size
    return root


def height_iterative(n: TreeNode) -> int:
    """Returns height of binary tree starting at `n` iteratively"""
    q = deque([n])
    height = 0
    while True:
        # height when no nodes left in level
        nodesinlevel = len(q)
        if nodesinlevel == 0:
            return height
        else:
            height += 1
        while nodesinlevel > 0:
            n = q.popleft()
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
            nodesinlevel -= 1


def height_recursive(n: TreeNode) -> int:
    """Returns height of binary tree starting at `n` recursively"""
    if not n:
        return 0
    return max(height_recursive(n.left), height_recursive(n.right)) + 1


def in_traverse_iterative(n: TreeNode) -> None:
    """Performs in-order iterative traversal through tree"""
    stack = []
    while n or stack:
        if n:
            stack.append(n)
            n = n.left
        else:
            n = stack.pop()
            print(n, end=" ")
            n = n.right
    print()


def pre_traverse_iterative(n: TreeNode) -> None:
    """Performs pre-order iterative traversal through tree"""
    stack = [n]
    while stack:
        n = stack.pop()
        if n:
            # visit before children
            print(n, end=" ")
            stack.append(n.right)
            stack.append(n.left)
    print()


def post_traverse_iterative(n: TreeNode) -> None:
    """Performs post-order iterative traversal through tree"""
    printstack = []
    stack = [n]
    while stack:
        n = stack.pop()
        if n:
            # delay visiting until after children
            printstack.append(n)
            stack.append(n.left)
            stack.append(n.right)
    while printstack:
        print(printstack.pop(), end=" ")
    print()


def level_traverse_iterative(n: TreeNode) -> None:
    """Performs level-order iterative traversal through tree"""
    q = deque([n])
    while q:
        n = q.popleft()
        if n:
            print(n, end=" ")
            q.append(n.left)
            q.append(n.right)
    print()


def in_traverse_recursive(n: TreeNode) -> None:
    """Performs in-order traversal through tree recursively"""
    if n:
        in_traverse_recursive(n.left)
        print(n, end=" ")
        in_traverse_recursive(n.right)


def pre_traverse_recursive(n: TreeNode) -> None:
    """Performs pre-order traversal through tree recursively"""
    if n:
        print(n, end=" ")
        pre_traverse_recursive(n.left)
        pre_traverse_recursive(n.right)


def post_traverse_recursive(n: TreeNode) -> None:
    """Performs post-order traversal through tree recursively"""
    if n:
        post_traverse_recursive(n.left)
        post_traverse_recursive(n.right)
        print(n, end=" ")


def level_traverse_recursive(n: TreeNode) -> None:
    """Performs level-order traversal through tree recursively"""
    h = height_recursive(n)
    for i in range(1, h+1):
        _level_traverse_util(n, i)


def _level_traverse_util(n: TreeNode, level: int) -> None:
    if n and level >= 1:
        if level == 1:
            print(n, end=" ")
        else:
            _level_traverse_util(n.left, level-1)
            _level_traverse_util(n.right, level-1)


class TestBinaryTree(unittest.TestCase):
    def test_binary_tree(self):
        arrs = [[i for i in range(1, 7)],
                [i for i in range(1, 8)],
                [i for i in range(1, 9)],
                [i for i in range(1, 10)],
                [1, 2, 3, 4, 5, 6, None, 7]]
        for arr in arrs:
            print("---------------------------")
            print(arr)
            tree = make_binary_tree(arr)
            print("IN ORDER")
            in_traverse_recursive(tree)
            print()
            in_traverse_iterative(tree)
            print("PRE ORDER")
            pre_traverse_recursive(tree)
            print()
            pre_traverse_iterative(tree)
            print("POST ORDER")
            post_traverse_recursive(tree)
            print()
            post_traverse_iterative(tree)
            print("LEVEL ORDER")
            level_traverse_recursive(tree)
            print()
            level_traverse_iterative(tree)
            self.assertEqual(height_iterative(tree), len(bin(len(arr))[2:]))
            self.assertEqual(height_recursive(tree), len(bin(len(arr))[2:]))

    def test_parent(self):
        tree = make_binary_tree([i for i in range(1, 8)])
        tests = [
            [tree, None],
            [tree.left, tree],
            [tree.left.left, tree.left],
            [tree.left.right, tree.left],
            [tree.right, tree],
            [tree.right.left, tree.right],
            [tree.right.right, tree.right]
        ]
        for node, parent in tests:
            with self.subTest(node=node.val):
                self.assertIs(node.parent, parent)

    def test_size(self):
        tree = make_binary_tree([i for i in range(1, 9)])
        tests = [
            [tree, 8],
            [tree.left, 4],
            [tree.left.left, 2],
            [tree.left.left.left, 1],
            [tree.left.right, 1],
            [tree.right, 3],
            [tree.right.left, 1],
            [tree.right.right, 1]
        ]
        for node, size in tests:
            with self.subTest(node=node.val):
                self.assertEqual(len(node), size)


if __name__ == "__main__":
    unittest.main()
