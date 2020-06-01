from collections import deque
import unittest


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class BinaryTree:
    def __init__(self, arr=None):
        self.root = None
        if arr:
            self.root = BinaryTree.__insert_level_order(arr, self.root, 0)

    @staticmethod
    def __insert_level_order(arr, n: Node, i: int) -> None:
        """Inserts `arr[i]` into tree at node `n` recursively in level order"""
        root = None
        if i < len(arr) and arr[i] is not None:
            # return desired node if in range
            root = Node(arr[i])
            # left node should have value `arr[2*i+1]`
            root.left = BinaryTree.__insert_level_order(
                arr, root.left, 2*i + 1)
            # right node should have value `arr[2*i+2]`
            root.right = BinaryTree.__insert_level_order(
                arr, root.right, 2*i + 2)
        return root

    def height_iterative(self) -> int:
        """Returns height of binary tree starting at `n` iteratively"""
        q = deque([self.root])
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
                if n.left is not None:
                    q.append(n.left)
                if n.right is not None:
                    q.append(n.right)
                nodesinlevel -= 1

    def height_recursive(self) -> int:
        """Returns height of binary tree starting at `n` recursively"""
        return BinaryTree.__height_util(self.root)

    @staticmethod
    def __height_util(n: Node) -> int:
        """Returns height of binary tree starting at `n`"""
        if n is None:
            return 0
        return max(BinaryTree.__height_util(n.left), BinaryTree.__height_util(n.right)) + 1

    def in_traverse_iterative(self) -> None:
        """Performs in-order iterative traversal through tree"""
        n = self.root
        stack = []
        while n is not None or stack:
            if n is not None:
                stack.append(n)
                n = n.left
            else:
                n = stack.pop()
                print(n, end=" ")
                n = n.right
        print()

    def pre_traverse_iterative(self) -> None:
        """Performs pre-order iterative traversal through tree"""
        stack = [self.root]
        while stack:
            n = stack.pop()
            if n is not None:
                # visit before children
                print(n, end=" ")
                stack.append(n.right)
                stack.append(n.left)
        print()

    def post_traverse_iterative(self) -> None:
        """Performs post-order iterative traversal through tree"""
        printstack = []
        stack = [self.root]
        while stack:
            n = stack.pop()
            if n is not None:
                # delay visiting until after children
                printstack.append(n)
                stack.append(n.left)
                stack.append(n.right)
        while printstack:
            print(printstack.pop(), end=" ")
        print()

    def level_traverse_iterative(self) -> None:
        """Performs level-order iterative traversal through tree"""
        q = deque([self.root])
        while q:
            n = q.popleft()
            if n is not None:
                print(n, end=" ")
                q.append(n.left)
                q.append(n.right)
        print()

    def in_traverse_recursive(self) -> None:
        """Performs in-order traversal through tree recursively"""
        BinaryTree.__in_traverse_util(self.root)
        print()

    def pre_traverse_recursive(self) -> None:
        """Performs pre-order traversal through tree recursively"""
        BinaryTree.__pre_traverse_util(self.root)
        print()

    def post_traverse_recursive(self) -> None:
        """Performs post-order traversal through tree recursively"""
        BinaryTree.__post_traverse_util(self.root)
        print()

    def level_traverse_recursive(self) -> None:
        """Performs level-order traversal through tree recursively"""
        h = self.height_recursive()
        for i in range(1, h+1):
            BinaryTree.__level_traverse_util(self.root, i)
        print()

    @staticmethod
    def __in_traverse_util(n: Node) -> None:
        if n is not None:
            BinaryTree.__in_traverse_util(n.left)
            print(n, end=" ")
            BinaryTree.__in_traverse_util(n.right)

    @staticmethod
    def __pre_traverse_util(n: Node) -> None:
        if n is not None:
            print(n, end=" ")
            BinaryTree.__pre_traverse_util(n.left)
            BinaryTree.__pre_traverse_util(n.right)

    @staticmethod
    def __post_traverse_util(n: Node) -> None:
        if n is not None:
            BinaryTree.__post_traverse_util(n.left)
            BinaryTree.__post_traverse_util(n.right)
            print(n, end=" ")

    @staticmethod
    def __level_traverse_util(n: Node, level: int) -> None:
        if n is not None and level >= 1:
            if level == 1:
                print(n, end=" ")
            else:
                BinaryTree.__level_traverse_util(n.left, level-1)
                BinaryTree.__level_traverse_util(n.right, level-1)


class TestBinaryTree(unittest.TestCase):
    def test_binary_tree(self):
        arrs = [[i for i in range(1, 6)],
                [i for i in range(1, 8)],
                [i for i in range(1, 9)],
                [i for i in range(1, 10)],
                [1, 2, 3, 4, 5, 6, 7, 8, None, 9, 10]]
        for arr in arrs:
            print("---------------------------")
            print(arr)
            tree = BinaryTree(arr)
            print("IN ORDER")
            tree.in_traverse_recursive()
            tree.in_traverse_iterative()
            print("PRE ORDER")
            tree.pre_traverse_recursive()
            tree.pre_traverse_iterative()
            print("POST ORDER")
            tree.post_traverse_recursive()
            tree.post_traverse_iterative()
            print("LEVEL ORDER")
            tree.level_traverse_recursive()
            tree.level_traverse_iterative()
            self.assertEqual(tree.height_iterative(), len(bin(len(arr))[2:]))
            self.assertEqual(tree.height_recursive(), len(bin(len(arr))[2:]))


if __name__ == "__main__":
    unittest.main()
