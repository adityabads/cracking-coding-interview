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

    def partition(self, x: int):
        """Partitions linked list so all elements >= x are at the end"""
        # partition index := number of values smaler than x
        part_ind = 0
        curr = self.head
        while curr is not None:
            val = curr.val
            if val < x:
                part_ind += 1
            curr = curr.next
        # move rightptr to partition index
        leftptr = self.head
        rightptr = self.head
        for i in range(part_ind):
            rightptr = rightptr.next
        # swap values between before/after partition index if appropriate
        while rightptr is not None:
            while rightptr is not None and rightptr.val >= x:
                rightptr = rightptr.next
            if leftptr is not None and leftptr.val < x:
                leftptr = leftptr.next
            if rightptr is not None:
                leftptr.val, rightptr.val = rightptr.val, leftptr.val

    def is_partitioned(self, x: int) -> bool:
        """Returns true iff linked list partitioned on `x`"""
        frontpart = True
        curr = self.head
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

    def __str__(self):
        vals = []
        curr = self.head
        while curr != None:
            vals.append(str(curr.val))
            curr = curr.next
        return " ".join(vals)


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
                lst = LinkedList(arr)
                self.assertTrue(lst.is_partitioned(i))
                lst.partition(i)
                self.assertTrue(lst.is_partitioned(i))
            for i in falseparts:
                lst = LinkedList(arr)
                self.assertFalse(lst.is_partitioned(i))
                lst.partition(i)
                self.assertTrue(lst.is_partitioned(i))

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
            self.assertTrue(all(lst.is_partitioned(i) for i in trueparts))
            self.assertFalse(any(lst.is_partitioned(i) for i in falseparts))


if __name__ == "__main__":
    unittest.main()
