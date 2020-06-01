# Sort Stack
# Write a program to sort a stack such that the smallest items are on the top.
# You can use an additional temporary stack, but you may not copy the elements
# into any other data structure (such as an array). The stack supports the
# following operations: push(), pop(), peek(), and isempty().

from mystack import AbstractStack, Stack
import unittest


def sort_stack(stack: AbstractStack) -> None:
    temp = Stack()
    while not stack.isempty():
        val = stack.pop()
        if temp.isempty() or val >= temp.peek():
            # move vals to temp stack if in `val` order
            temp.push(val)
        else:
            # move temp stack back to original, adding `val` in right place
            inserted = False
            while not temp.isempty():
                tempval = temp.pop()
                stack.push(tempval)
                if not inserted and (temp.isempty() or val >= temp.peek()):
                    stack.push(val)
                    inserted = True

    # move back to original
    while not temp.isempty():
        stack.push(temp.pop())


class TestSortStack(unittest.TestCase):
    def test_sort_stack(self):
        tests = [
            [1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9],
            [3, 1, 5, 9, 4, 2, 1, 7, 6, 5, 8],
            [4, 9, 7, 1, 2, 6, 5, 3, 1, 8, 5],
            [9, 8, 1, 7, 6, 5, 5, 4, 3, 2, 1]
        ]
        expected = [1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9]

        stack = Stack()
        sort_stack(stack)

        for test in tests:
            with self.subTest(test=test):
                stack = Stack(test)
                sort_stack(stack)
                for val in expected:
                    self.assertEqual(stack.pop(), val)


if __name__ == "__main__":
    unittest.main()
