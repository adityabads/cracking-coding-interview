# Intersection
# Given two (singly) linked lists, determine if the two lists intersect. Return
# the intersecting node. Note that the intersection is defined based on
# reference, not value. That is, if the kth node of the first linked list is
# the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.

from linkedlist import LinkedList
import unittest


def intersection(lst1: LinkedList, lst2: LinkedList) -> bool:
    """Returns intersecting node iff linked lists intersect, else None"""
    # make ptr1 point to the longer list
    ptr1 = lst1.head
    ptr2 = lst2.head
    diff = len(lst1) - len(lst2)
    if diff < 0:
        ptr1, ptr2 = ptr2, ptr1

    # make both pointers equal length from the end
    # if lists intersect anywhere, then both lists must have the same end
    for i in range(abs(diff)):
        ptr1 = ptr1.next
    while ptr1 is not ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    return ptr1


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
            self.assertEqual(intersection(lst1, lst2), lstend.head)
            self.assertEqual(intersection(lst2, lst1), lstend.head)
        for arr1, arr2 in falses:
            lst1 = LinkedList(arr1)
            lst2 = LinkedList(arr2)
            self.assertIsNone(intersection(lst1, lst2))
            self.assertIsNone(intersection(lst2, lst1))


if __name__ == "__main__":
    unittest.main()
