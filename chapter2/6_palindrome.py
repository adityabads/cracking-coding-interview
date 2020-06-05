# Palindrome
# Implement a function to check if a linked list is a palindrome.

from collections import deque
from linkedlist import LinkedList
import unittest


def is_palindrome(lst: LinkedList) -> bool:
    """Returns true iff linked list is a palindrome"""
    stack = deque()
    curr = lst.head
    while curr:
        stack.append(curr.val)
        curr = curr.next
    curr = lst.head
    while curr:
        if curr.val != stack.pop():
            return False
        curr = curr.next
    return True


class TestPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        trues = ["", "a", "aba", "abba", "racecar", "tacocat"]
        falses = ["abBa", "rac ecar", "billy"]

        for test in trues:
            with self.subTest(test=test):
                lst = LinkedList(test)
                self.assertTrue(is_palindrome(lst))
        for test in falses:
            with self.subTest(test=test):
                lst = LinkedList(test)
                self.assertFalse(is_palindrome(lst))


if __name__ == "__main__":
    unittest.main()
