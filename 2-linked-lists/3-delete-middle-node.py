# Delete Middle Node
# Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly
# linked list, given only access to that node.
#
# EXAMPLE
# lnput: the node c from the linked list a->b->c->d->e->f
# Result: nothing is returned, but the new linked list looks like a->b->d->e->f

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

    def delete_middle_node(self, n: Node):
        """Deletes Node `n` in middle of linked list"""
        n.val = n.next.val
        n.next = n.next.next

    def __str__(self):
        vals = []
        curr = self.head
        while curr != None:
            vals.append(str(curr.val))
            curr = curr.next
        return " ".join(vals)


class TestRemoveDups(unittest.TestCase):
    def test_remove_dups(self):
        lst = LinkedList("abcdef")
        lst.delete_middle_node(lst.head.next.next)
        self.assertEqual(str(lst), "a b d e f")
        lst.delete_middle_node(lst.head.next.next.next)
        self.assertEqual(str(lst), "a b d f")
        lst.delete_middle_node(lst.head.next)
        self.assertEqual(str(lst), "a d f")

    def test_linked_list(self):
        lst = LinkedList()
        self.assertEqual(str(lst), "")
        lst = LinkedList([])
        self.assertEqual(str(lst), "")
        lst = LinkedList([1])
        self.assertEqual(str(lst), "1")
        lst = LinkedList("abcdef")
        self.assertEqual(str(lst), "a b c d e f")


if __name__ == "__main__":
    unittest.main()
