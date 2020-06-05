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

from linkedlist import LinkedList
import unittest


def has_loop(lst: LinkedList) -> bool:
    """Returns true iff linked list has a loop"""
    slow = lst.head
    if slow:
        fast = lst.head.next
    else:
        return False
    while fast and fast.next:
        if slow is fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False


class TestLoopDetection(unittest.TestCase):
    def test_has_loop(self):
        tests = ["abcdef", "abcabc", "aaaa"]
        for test in tests:
            with self.subTest(test=test):
                lst = LinkedList(test)
                self.assertFalse(has_loop(lst))
                lst.append_node(lst.head)
                self.assertTrue(has_loop(lst))
                lst = LinkedList(test)
                lst.append_node(lst.head.next)
                self.assertTrue(has_loop(lst))
                lst = LinkedList(test)
                lst.append("a")
                self.assertFalse(has_loop(lst))


if __name__ == "__main__":
    unittest.main()
