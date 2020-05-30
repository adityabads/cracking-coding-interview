# Palindrome
# Implement a function to check if a linked list is a palindrome.

from collections import deque
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

    def is_palindrome(self) -> bool:
        """Returns true iff linked list is a palindrome"""
        stack = deque()
        curr = self.head
        while curr is not None:
            stack.append(curr.val)
            curr = curr.next
        curr = self.head
        while curr is not None:
            if curr.val != stack.pop():
                return False
            curr = curr.next
        return True

    def __str__(self):
        vals = []
        curr = self.head
        while curr != None:
            vals.append(str(curr.val))
            curr = curr.next
        return " ".join(vals)


class TestPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        trues = ["", "a", "aba", "abba", "racecar", "tacocat"]
        falses = ["abBa", "rac ecar", "billy"]

        for test in trues:
            lst = LinkedList(test)
            self.assertTrue(lst.is_palindrome())
        for test in falses:
            lst = LinkedList(test)
            self.assertFalse(lst.is_palindrome())


if __name__ == "__main__":
    unittest.main()
