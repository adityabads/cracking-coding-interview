# Stack Min
# How would you design a stack which, in addition to push and pop, has a
# function min which returns the minimum element? Push, pop and min should all
# operate in 0(1) time.

from stack import Stack
import unittest


class StackMin:
    """Stack class that keeps track of min element"""

    def __init__(self, arr=None):
        """Inits stack with vals in `arr`"""
        self.stack = Stack()
        if arr:
            for val in arr:
                self.push(val)

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        """Returns string of values from stack top to bottom"""
        vals = []
        curr = self.stack.top
        while curr is not None:
            vals.append(str(curr.val[0]))
            curr = curr.next
        return " ".join(vals)

    def push(self, val):
        """Adds value (and min value) to top of stack"""
        minval = val if len(self.stack) == 0 else min(
            self.stack.peek()[1], val)
        self.stack.push((val, minval))

    def pop(self):
        """Removes and returns top value from stack"""
        return self.stack.pop()[0]

    def peek(self):
        """Returns top value from stack without removing"""
        return self.stack.peek()[0]

    def min(self):
        """Returns minimum value in stack"""
        if len(self.stack) == 0:
            raise Exception("Called min on empty stack")
        return self.stack.peek()[1]


class TestStackMin(unittest.TestCase):

    def test_min(self):
        tests = [
            [1, 2, 3, 4, 5, 5, 6, 7, 8, 9],
            [5, 6, 3, 5, 8, 9, 2, 5, 1, 7],
            [4, 9, 3, 8, 5, 2, 4, 1, 5, 7],
            [9, 8, 7, 6, 5, 5, 4, 3, 2, 1]
        ]

        for test in tests:
            stack = StackMin()
            for i in range(len(test)):
                stack.push(test[i])
                self.assertEqual(stack.min(), min(test[:i+1]))
            for i in range(len(test)):
                self.assertEqual(stack.min(), min(test[:len(test)-i]))
                stack.pop()
            with self.assertRaises(Exception):
                stack.min()

    def test_stack(self):
        arr = [i for i in range(5)]
        stack = StackMin(arr)
        self.assertEqual(str(stack), " ".join(map(str, reversed(arr))))
        for val in reversed(arr):
            self.assertEquals(stack.peek(), val)
            self.assertEqual(stack.pop(), val)
        with self.assertRaises(Exception):
            stack.pop()


if __name__ == "__main__":
    unittest.main()
