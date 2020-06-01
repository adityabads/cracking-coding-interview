# Partition
# Write code to partition a linked list around a value x, such that all nodes
# less than x come before all nodes greater than or equal to x. If x is
# contained within the list, the values of x only need to be after the elements
# less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.
#
# EXAMPLE
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

from linkedlist import LinkedList
import unittest


def partition(lst: LinkedList, x) -> None:
    """Partitions linked list so all values >= x are at the end"""
    curr = lst.tail = lst.head
    while curr is not None:
        nxt = curr.next
        curr.next = None
        if curr.val < x:
            curr.next = lst.head
            lst.head = curr
        else:
            lst.tail.next = curr
            lst.tail = curr
        curr = nxt

    if lst.tail is not None:
        lst.tail.next = None


def is_partitioned(lst: LinkedList, x) -> bool:
    """Returns true iff linked list partitioned on `x`"""
    frontpart = True
    curr = lst.head
    while curr is not None:
        val = curr.val
        # detect if partition reached (val >= x)
        if frontpart and val >= x:
            frontpart = False
        # all values after partiion must be >= x
        elif not frontpart and val < x:
            return False
        curr = curr.next
    return True


class TestPartition(unittest.TestCase):
    def test_partition(self):
        tests = [
            # array, valid partitions, invalid partitions
            [None, [1, 5, 7], []],
            [[1, 2, 3, 4, 5, 6, 7, 8], [-1, 3, 4.5, 7, 9], []],
            [[9, 8, 2, 4, 7, 6, 3, 5], [], [3, 7, 4, 9]],
            [[3, 5, 8, 5, 10, 2, 1], [], [5, 2, 9]]
        ]

        for arr, trueparts, falseparts in tests:
            for i in trueparts:
                with self.subTest(arr=arr, truepart=i):
                    lst = LinkedList(arr)
                    self.assertTrue(is_partitioned(lst, i))
                    partition(lst, i)
                    self.assertTrue(is_partitioned(lst, i))
            for i in falseparts:
                with self.subTest(arr=arr, falsepart=i):
                    lst = LinkedList(arr)
                    self.assertFalse(is_partitioned(lst, i))
                    partition(lst, i)
                    self.assertTrue(is_partitioned(lst, i))

    def test_is_partitioned(self):
        tests = [
            # array, valid partitions, invalid partitions
            [None, [0, 1, 5], []],
            [[1], [0, 1, 2], []],
            [[1, 2, 3, 4, 5, 6, 7, 8], [-1, 3, 4.5, 7, 9], []],
            [[3, 5, 8, 5, 10, 2, 1], [], [5, 2, 9]],
            [[3, 1, 2, 10, 5, 5, 8], [5, 4], [8, 6, 3, 10]]
        ]

        for arr, trueparts, falseparts in tests:
            lst = LinkedList(arr)
            self.assertTrue(all(is_partitioned(lst, i) for i in trueparts))
            self.assertFalse(any(is_partitioned(lst, i) for i in falseparts))


if __name__ == "__main__":
    unittest.main()
