# Intersection
# Given two (singly) linked lists, determine if the two lists intersect. Return
# the intersecting node. Note that the intersection is defined based on
# reference, not value. That is, if the kth node of the first linked list is
# the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.

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

    def intersects(self, other) -> bool:
        """Returns true iff linked lists intersect"""
        selfptr = self.head
        otherptr = other.head
        # make selfptr point to the longer list
        diff = len(self) - len(other)
        if diff < 0:
            selfptr, otherptr = otherptr, selfptr
        # make both pointers equal length from the end
        # if lists intersect anywhere, then both lists must have the same end
        for i in range(abs(diff)):
            selfptr = selfptr.next
        while selfptr is not None and otherptr is not None:
            if selfptr == otherptr:
                return True
            selfptr = selfptr.next
            otherptr = otherptr.next
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


class TestIntersection(unittest.TestCase):
    def test_intersects(self):
        trues = [
            # list 1, list 2, end
            ["aa", "aa", "aa"],
            ["aaa", "", "def"],
            ["", "aaa", "def"],
            ["jkc", "f", "oks"],
        ]
        falses = [
            ["", ""],
            ["abc", ""],
            ["", "abc"],
            ["aaaa", "aaaa"],
            ["bdeaa", "cflaa"],
            ["abc", "edsabc"]
        ]

        for arr1, arr2, arrend in trues:
            lst1 = LinkedList(arr1)
            lst2 = LinkedList(arr2)
            lstend = LinkedList(arrend)
            lst1.append(lstend.head)
            lst2.append(lstend.head)
            self.assertTrue(lst1.intersects(lst2) and lst2.intersects(lst1))
        for arr1, arr2 in falses:
            lst1 = LinkedList(arr1)
            lst2 = LinkedList(arr2)
            self.assertFalse(lst1.intersects(lst2) or lst2.intersects(lst1))

    def test_append(self):
        tests = [
            ["123", "456", "1 2 3 4 5 6", "4 5 6"],
            [None, "123", "1 2 3", "1 2 3"],
            ["123", None, "1 2 3", ""],
            ["1", "23", "1 2 3", "2 3"],
            ["12", "3", "1 2 3", "3"]
        ]

        for arr1, arr2, expected1, expected2 in tests:
            lst1 = LinkedList(arr1)
            lst2 = LinkedList(arr2)
            lst1.append(lst2.head)
            self.assertEqual(str(lst1), expected1)
            self.assertEqual(str(lst2), expected2)


if __name__ == "__main__":
    unittest.main()
