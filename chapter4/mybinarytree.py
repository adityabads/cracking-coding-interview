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
        """Inserts `arr[i]` into tree at node `n`, using level order"""
        root = None
        if i < len(arr) and arr[i] is not None:
            root = Node(arr[i])
            root.left = BinaryTree.__insert_level_order(
                arr, root.left, 2 * i + 1)
            root.right = BinaryTree.__insert_level_order(
                arr, root.right, 2 * i + 2)
        return root

    def pre_traverse_iterative(self) -> None:
        print()

    def in_traverse_iterative(self) -> None:
        print()

    def post_traverse_iterative(self) -> None:
        print()

    def level_traverse_iterative(self) -> None:
        q = deque([self.root])
        while q:
            n = q.popleft()
            if n is not None:
                print(n, end=" ")
                q.append(n.left)
                q.append(n.right)
        print()

    def in_traverse_recursive(self) -> None:
        BinaryTree.__in_traverse_util(self.root)
        print()

    def pre_traverse_recursive(self) -> None:
        BinaryTree.__pre_traverse_util(self.root)
        print()

    def post_traverse_recursive(self) -> None:
        BinaryTree.__post_traverse_util(self.root)
        print()

    def level_traverse_recursive(self) -> None:
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


class TestBinaryTree(unittest.TestCase):
    def test_binary_tree(self):
        tree = BinaryTree([1, 2, 3, 4, 5, 6, 7, 8, None, 9, 10])
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


if __name__ == "__main__":
    unittest.main()
