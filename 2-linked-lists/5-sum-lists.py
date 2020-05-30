# Sum Lists
# You have two numbers represented by a linked list, where each node contains
# a single digit. The digits are stored in reverse order, such that the 1's
# digit is at the head of the list. Write a function that adds the two numbers
# and returns the sum as a linked list.
# EXAMPLE
# Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.
#
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.
# EXAMPLE
# Input:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is, 617 + 295.
# Output: 9 -> 1 -> 2. That is, 912.

from linkedlist import LinkedList
import unittest


def add_lists(this: LinkedList, that: LinkedList):
    addlst = []
    thisptr = this.head
    thatptr = that.head
    carry = 0
    while thisptr is not None or thatptr is not None:
        selfval = thisptr.val if thisptr is not None else 0
        otherval = thatptr.val if thatptr is not None else 0
        add = selfval + otherval + carry
        addlst.append(add % 10)
        carry = add // 10
        if thisptr is not None:
            thisptr = thisptr.next
        if thatptr is not None:
            thatptr = thatptr.next
    if carry > 0:
        addlst.append(carry)
    return LinkedList(addlst)


class TestSumLists(unittest.TestCase):
    def test_add(self):
        tests = [
            [0, 0],
            [2, 3],
            [7, 5],
            [617, 295],
            [897, 586],
            [1, 183],
            [182, 2030]
        ]

        for x, y in tests:
            add = str(x + y)[::-1]
            add = " ".join(add)
            x = str(x)[::-1]
            y = str(y)[::-1]
            x = [int(dig) for dig in x]
            y = [int(dig) for dig in y]
            self.assertEqual(str(add_lists(LinkedList(x), LinkedList(y))), add)


if __name__ == "__main__":
    unittest.main()
