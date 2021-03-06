# Return Kth to Last
# Implement an algorithm to find the kth to last element of a singly linked list.

from linkedlist import LinkedList
import unittest


def get_to_last(lst: LinkedList, k: int):
    """Returns kth to last value in linked list"""
    if k <= 0 or k > lst.length:
        return None
    kth = lst.head
    last = lst.head
    for i in range(k):
        last = last.next
    while last:
        kth = kth.next
        last = last.next
    return kth.val


class TestRemoveDups(unittest.TestCase):
    def test_remove_dups(self):
        lst = LinkedList()
        self.assertIsNone(get_to_last(lst, 1))
        lst = LinkedList([1])
        self.assertEqual(get_to_last(lst, 1), 1)
        self.assertIsNone(get_to_last(lst, 2))
        lst = LinkedList([1, 2, 3, 4, 5])
        self.assertEqual(get_to_last(lst, 1), 5)
        self.assertEqual(get_to_last(lst, 2), 4)
        self.assertEqual(get_to_last(lst, 5), 1)


if __name__ == "__main__":
    unittest.main()
