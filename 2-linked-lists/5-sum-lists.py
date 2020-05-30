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

import unittest


class Digit:
    """Digit node class for Number"""

    def __init__(self, val):
        self.val = int(val)
        self.next = None


class Number:
    """Holds non-negative integers, storing digits in a linked list in reverse order"""

    def __init__(self, num):
        """Inits linked list, storing digits in `arr` in reverse order"""
        if isinstance(num, int):
            num = str(num)
        curr = None
        if num is not None:
            for digit in num:
                d = Digit(digit)
                d.next = curr
                curr = d
        self.head = curr

    def __add__(self, other):
        addlst = []
        selfptr = self.head
        otherptr = other.head
        carry = 0
        while selfptr is not None or otherptr is not None:
            selfval = selfptr.val if selfptr is not None else 0
            otherval = otherptr.val if otherptr is not None else 0
            add = selfval + otherval + carry
            addlst.append(add % 10)
            carry = add // 10
            if selfptr is not None:
                selfptr = selfptr.next
            if otherptr is not None:
                otherptr = otherptr.next
        if carry > 0:
            addlst.append(carry)
        return Number(addlst)

    def __str__(self):
        vals = []
        curr = self.head
        while curr != None:
            vals.append(str(curr.val))
            curr = curr.next
        return "".join(vals)


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
            self.assertEqual(str(Number(x) + Number(y)), str(x + y))


if __name__ == "__main__":
    unittest.main()
