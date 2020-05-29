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
        lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8])
        self.assertTrue(lst.is_partitioned(6))
        lst.partition(6)
        self.assertTrue(lst.is_partitioned(6))
        lst = LinkedList([9, 8, 2, 4, 7, 6, 3, 5])
        self.assertFalse(lst.is_partitioned(4))
        lst.partition(4)
        self.assertTrue(lst.is_partitioned(4))
        lst = LinkedList([3, 5, 8, 5, 10, 2, 1])
        self.assertFalse(lst.is_partitioned(5))
        lst.partition(5)
        self.assertTrue(lst.is_partitioned(5))

    def test_is_partitioned(self):
        lst = LinkedList()
        self.assertTrue(lst.is_partitioned(0))
        lst = LinkedList([1])
        self.assertTrue(lst.is_partitioned(0))
        self.assertTrue(lst.is_partitioned(2))
        lst = LinkedList([1, 2, 3, 7, 4, 8, 9])
        self.assertTrue(lst.is_partitioned(2))
        self.assertTrue(lst.is_partitioned(3.5))
        self.assertTrue(lst.is_partitioned(4))
        self.assertFalse(lst.is_partitioned(7))
        lst = LinkedList([3, 5, 8, 5, 10, 2, 1])
        self.assertFalse(lst.is_partitioned(5))
        lst = LinkedList([3, 1, 2, 10, 5, 5, 8])
        self.assertTrue(lst.is_partitioned(5))


if __name__ == "__main__":
    unittest.main()
