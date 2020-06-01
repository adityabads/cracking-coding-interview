# Stack Min
# How would you design a stack which, in addition to push and pop, has a
# function min which returns the minimum element? Push, pop and min should all
# operate in 0(1) time.

from mystack import AbstractStack, Stack, test_stack
import unittest


class StackMin(AbstractStack):
    """Stack class that keeps track of min element"""

    def __init__(self, arr=None):
        """Inits stack with vals in `arr`"""
        self.stack = Stack()
        if arr:
            for val in arr:
                self.push(val)

    def __iter__(self):
        for (val, minval) in self.stack:
            yield val

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        """Returns string of values in stack, top to bottom"""
        vals = []
        for val in self:
            vals.append(str(val))
        return " ".join(vals)

    def push(self, val):
        """Adds `val` (and current min value) to top of stack"""
        minval = val if self.isempty() else min(self.min(), val)
        self.stack.push((val, minval))

    def pop(self):
        """Removes and returns top value in stack"""
        return self.stack.pop()[0]

    def peek(self):
        """Returns top value in stack without removing"""
        return self.stack.peek()[0]

    def isempty(self):
        return self.stack.isempty()

    def min(self):
        """Returns minimum value in stack"""
        if self.isempty():
            raise Exception("Called min on empty stack")
        return self.stack.peek()[1]


class TestStackMin(test_stack(lambda x=None: StackMin(x))):

    def test_min(self):
        tests = [
            [1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9],
            [5, 6, 3, 5, 8, 9, 2, 1, 5, 1, 7],
            [4, 9, 3, 8, 5, 2, 4, 1, 5, 7, 1],
            [9, 8, 7, 6, 5, 5, 4, 3, 2, 1, 1]
        ]

        for test in tests:
            with self.subTest(test=test):
                stack = StackMin()
                for i in range(len(test)):
                    stack.push(test[i])
                    self.assertEqual(stack.min(), min(test[:i+1]))
                for i in range(len(test)):
                    self.assertEqual(stack.min(), min(test[:len(test)-i]))
                    stack.pop()
                with self.assertRaises(Exception):
                    stack.min()


if __name__ == "__main__":
    unittest.main()
