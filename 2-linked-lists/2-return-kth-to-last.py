# Return Kth to Last
# Implement an algorithm to find the kth to last element of a singly linked list.

import unittest


class Node:
    """Node class for LinkedList"""

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    """Linked list class"""

    def __init__(self, arr=None):
        """Inits linked list with values in `arr`"""
        curr = None
        if arr is not None:
            for i in reversed(range(len(arr))):
                n = Node(arr[i])
                n.next = curr
                curr = n
        self.head = curr

    def get_to_last(self, k):
        """Returns kth to last value in linked list"""
        if k <= 0:
            return None
        kth = self.head
        last = self.head
        i = 0
        while last is not None:
            if i < k:
                i += 1
            else:
                kth = kth.next
            last = last.next
        return kth.val if i == k else None

    def __str__(self):
        vals = []
        curr = self.head
        while curr != None:
            vals.append(str(curr.val))
            curr = curr.next
        return " ".join(vals)


class TestRemoveDups(unittest.TestCase):
    def test_remove_dups(self):
        lst = LinkedList()
        self.assertIsNone(lst.get_to_last(1))
        lst = LinkedList([1])
        self.assertEqual(lst.get_to_last(1), 1)
        self.assertIsNone(lst.get_to_last(2))
        lst = LinkedList([1, 2, 3, 4, 5])
        self.assertEqual(lst.get_to_last(1), 5)
        self.assertEqual(lst.get_to_last(2), 4)
        self.assertEqual(lst.get_to_last(5), 1)


if __name__ == "__main__":
    unittest.main()
