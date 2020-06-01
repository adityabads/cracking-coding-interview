# Delete Middle Node
# Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly
# linked list, given only access to that node.
#
# EXAMPLE
# lnput: the node c from the linked list a->b->c->d->e->f
# Result: nothing is returned, but the new linked list looks like a->b->d->e->f

from linkedlist import LinkedList
import unittest


def delete_middle_node(n: LinkedList.Node) -> None:
    """Deletes Node `n` in middle of linked list"""
    n.val = n.next.val
    n.next = n.next.next


class TestRemoveDups(unittest.TestCase):
    def test_remove_dups(self):
        lst = LinkedList("abcdef")
        self.assertEqual(str(lst), "a b c d e f")
        delete_middle_node(lst.head.next.next)
        self.assertEqual(str(lst), "a b d e f")
        delete_middle_node(lst.head.next.next.next)
        self.assertEqual(str(lst), "a b d f")
        delete_middle_node(lst.head.next)
        self.assertEqual(str(lst), "a d f")
        delete_middle_node(lst.head.next)
        self.assertEqual(str(lst), "a f")


if __name__ == "__main__":
    unittest.main()
