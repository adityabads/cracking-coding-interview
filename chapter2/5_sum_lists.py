# Sum Lists
# You have two numbers represented by a linked list, where each node contains
# a single digit. The digits are stored in reverse order, such that the 1's
# digit is at the head of the list. Write a function that adds the two numbers
# and returns the sum as a linked list.
#
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
import random
import unittest


def add_lists(lst1: LinkedList, lst2: LinkedList) -> LinkedList:
    # make ptr1 point to longer list
    ptr1 = lst1.head
    ptr2 = lst2.head
    if len(lst1) < len(lst2):
        ptr1, ptr2 = ptr2, ptr1

    # add lists
    result = LinkedList()
    carry = 0
    while ptr1:
        add = ptr1.val + ptr2.val + carry if ptr2 else ptr1.val + carry
        result.append(add % 10)
        carry = add // 10
        ptr1 = ptr1.next
        ptr2 = ptr2.next if ptr2 else None
    if carry > 0:
        result.append(carry)
    return result


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
        tests.extend([[random.randint(0, 1000) for j in range(2)]
                      for i in range(10)])

        for x, y in tests:
            with self.subTest(x=x, y=y):
                add = str(x + y)[::-1]
                add = " ".join(add)
                x = str(x)[::-1]
                y = str(y)[::-1]
                x = [int(dig) for dig in x]
                y = [int(dig) for dig in y]
                self.assertEqual(
                    str(add_lists(LinkedList(x), LinkedList(y))), add)
                self.assertEqual(
                    str(add_lists(LinkedList(y), LinkedList(x))), add)


if __name__ == "__main__":
    unittest.main()
