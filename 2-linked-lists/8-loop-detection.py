# Loop Detection
# Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.
#
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
# as to make a loop in the linked list.
#
# EXAMPLE
# Input: A -> B -> C - > D -> E -> C [the same C as earlier]
# Output: C

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
        self.head = None
        self.tail = None
        self.length = 0
        if arr is not None:
            for val in arr:
                self.append(Node(val))

    def has_loop(self) -> bool:
        """Returns true iff linked list has a loop"""
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def append(self, n: Node):
        if self.length == 0:
            self.head = n
        elif self.length == 1:
            self.head.next = n
        else:
            self.tail.next = n
        self.tail = n
        self.length += 1

    def __len__(self):
        return self.length

    def __str__(self):
        vals = []
        curr = self.head
        while curr != None:
            vals.append(str(curr.val))
            curr = curr.next
        return " ".join(vals)


class TestLoopDetection(unittest.TestCase):
    def test_has_loop(self):
        tests = ["abcdef", "abcabc", "aaaa"]
        for test in tests:
            lst = LinkedList(test)
            self.assertFalse(lst.has_loop())
            lst.append(lst.head)
            self.assertTrue(lst.has_loop())
            lst = LinkedList(test)
            lst.append(lst.head.next)
            self.assertTrue(lst.has_loop())
            lst = LinkedList(test)
            lst.append(Node("a"))
            self.assertFalse(lst.has_loop())


if __name__ == "__main__":
    unittest.main()
