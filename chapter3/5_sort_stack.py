# Sort Stack
# Write a program to sort a stack such that the smallest items are on the top.
# You can use an additional temporary stack, but you may not copy the elements
# into any other data structure (such as an array). The stack supports the
# following operations: push(), pop(), peek(), and isempty().

from mystack import AbstractStack, Stack
import random
import unittest


def sort_stack(stack: AbstractStack) -> None:
    tempstack = Stack()
    while not stack.isempty():
        val = stack.pop()
        while not tempstack.isempty() and tempstack.peek() > val:
            # move vals back to original until `val` can be inserted
            stack.push(tempstack.pop())
        tempstack.push(val)

    # move back to original
    while not tempstack.isempty():
        stack.push(tempstack.pop())


class TestSortStack(unittest.TestCase):
    def test_sort_stack(self):
        tests = [
            [],
            [0],
            [i for i in range(10)],
            [i for i in reversed(range(10))],
        ]
        # random with duplicates
        tests.extend([[random.randint(0, 15) for i in range(20)]
                      for j in range(10)])

        for test in tests:
            with self.subTest(test=test):
                stack = Stack(test)
                sort_stack(stack)
                test.sort()
                for val in test:
                    self.assertEqual(stack.pop(), val)


if __name__ == "__main__":
    unittest.main()
