# Intersection
# Given two (singly) linked lists, determine if the two lists intersect. Return
# the intersecting node. Note that the intersection is defined based on
# reference, not value. That is, if the kth node of the first linked list is
# the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.

from linkedlist import LinkedList
import unittest


def intersects(this: LinkedList, that: LinkedList) -> bool:
    """Returns true iff linked lists intersect"""
    thisptr = this.head
    thatptr = that.head
    # make thisptr point to the longer list
    diff = len(this) - len(that)
    if diff < 0:
        thisptr, thatptr = thatptr, thisptr
    # make both pointers equal length from the end
    # if lists intersect anywhere, then both lists must have the same end
    for i in range(abs(diff)):
        thisptr = thisptr.next
    while thisptr is not None and thatptr is not None:
        if thisptr == thatptr:
            return True
        thisptr = thisptr.next
        thatptr = thatptr.next
    return False


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
            lst1.extend(lstend)
            lst2.extend(lstend)
            self.assertTrue(intersects(lst1, lst2) and intersects(lst2, lst1))
        for arr1, arr2 in falses:
            lst1 = LinkedList(arr1)
            lst2 = LinkedList(arr2)
            self.assertFalse(intersects(lst1, lst2) or intersects(lst2, lst1))


if __name__ == "__main__":
    unittest.main()
