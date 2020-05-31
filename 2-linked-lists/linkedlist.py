import unittest


class Node:
    """Node class for LinkedList"""

    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

    def __str__(self):
        return str(self.val)


class LinkedList:
    """Linked list class"""

    def __init__(self, arr=None):
        """Inits linked list with values in `arr`"""
        self.head = None
        self.tail = None
        self.length = 0
        if arr is not None:
            for val in arr:
                self.append(val)

    def __len__(self):
        return self.length

    def __str__(self):
        vals = []
        curr = self.head
        while curr is not None:
            vals.append(str(curr))
            curr = curr.next
        return " ".join(vals)

    def append(self, val):
        """Append new node with value `val` to linked list"""
        self.append_node(Node(val))

    def append_node(self, n: Node):
        """Append node `n` to linked list"""
        if self.length == 0:
            self.head = n
        else:
            self.tail.next = n
        self.tail = n
        self.length += 1

    def extend(self, other):
        """Extend linked list with other linked list"""
        if other is not None:
            self.append_node(other.head)


class TestLinkedList(unittest.TestCase):
    def test_len(self):
        lst = LinkedList()
        self.assertEqual(len(lst), 0)
        lst.append(3)
        self.assertEqual(len(lst), 1)
        lst = LinkedList("abcde")
        self.assertEqual(len(lst), 5)

    def test_str(self):
        tests = [
            [None, ""],
            [[], ""],
            [[1], "1"],
            [[1, 2, 3, 4, 5], "1 2 3 4 5"]
        ]

        for arr, expected in tests:
            self.assertEqual(str(LinkedList(arr)), expected)

    def test_append_node(self):
        tests = [
            ["123", "456", "1 2 3 4 5 6", "4 5 6"],
            [None, "123", "1 2 3", "1 2 3"],
            ["123", None, "1 2 3", ""],
            ["1", "23", "1 2 3", "2 3"],
            ["12", "3", "1 2 3", "3"]
        ]

        for arr1, arr2, expected1, expected2 in tests:
            lst1 = LinkedList(arr1)
            lst2 = LinkedList(arr2)
            lst1.extend(lst2)
            self.assertEqual(str(lst1), expected1)
            self.assertEqual(str(lst2), expected2)


if __name__ == "__main__":
    unittest.main()
