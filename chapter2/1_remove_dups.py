# Remove Dups
# Write code to remove duplicates from an unsorted linked list.
#
# FOLLOWUP
# How would you solve this problem if a temporary buffer is not allowed?

from linkedlist import LinkedList
import unittest


def remove_dups(lst: LinkedList) -> None:
    """Removes duplicate vals from linked list"""
    seen = set()
    prev = None
    curr = lst.head
    while curr:
        if curr.val in seen:
            prev.next = curr.next
        else:
            seen.add(curr.val)
            prev = curr
        curr = curr.next


class TestRemoveDups(unittest.TestCase):
    def test_remove_dups(self):
        tests = [
            [None, ""],
            [[], ""],
            [[1, 2, 3, 4, 5], "1 2 3 4 5"],
            [[1, 2, 3, 1, 4, 5], "1 2 3 4 5"],
            [[1, 2, 3, 4, 4, 4, 5], "1 2 3 4 5"],
            [[1, 2, 1, 3, 4, 1, 5, 2, 5, 4, 3, 5], "1 2 3 4 5"],
        ]

        for arr, expected in tests:
            with self.subTest(arr=arr):
                lst = LinkedList(arr)
                remove_dups(lst)
                self.assertEqual(str(lst), expected)


if __name__ == "__main__":
    unittest.main()
