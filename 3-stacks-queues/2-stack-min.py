# Stack Min
# How would you design a stack which, in addition to push and pop, has a
# function min which returns the minimum element? Push, pop and min should all
# operate in 0(1) time.

from stack import Stack
import unittest


class TestStackMin(unittest.TestCase):

    def test_min(self):
        tests = [
            [1, 2, 3, 4, 5, 5, 6, 7, 8, 9],
            [5, 6, 3, 5, 8, 9, 2, 5, 1, 7],
            [4, 9, 3, 8, 5, 2, 4, 1, 5, 7],
            [9, 8, 7, 6, 5, 5, 4, 3, 2, 1]
        ]

        for test in tests:
            stack = Stack()
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
