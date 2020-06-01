# Three in One
# Describe how you could use a single array to implement three stacks

import random
import unittest


class ThreeStacks:
    """Class implementing three stacks with one array"""

    def __init__(self, stack_size: int = 10):
        """Init three stacks, each with initial allocated size `stack_size`"""
        self.stack_size = stack_size
        self.arr = [None] * stack_size * 3
        self.bottoms = [i * stack_size for i in range(3)]
        self.tops = [i * stack_size for i in range(3)]

    def push(self, stackno: int, val) -> None:
        """Push `val` onto stack number `stackno` (1, 2, or 3)"""
        i = stackno - 1
        if self.tops[i] - self.bottoms[i] == self.stack_size:
            raise Exception("push called on full stack {stackno}")
        self.arr[self.tops[i]] = val
        self.tops[i] += 1

    def pop(self, stackno: int):
        """Pop top element off stack number `stackno` (1, 2, or 3)"""
        i = stackno - 1
        if self.tops[i] == self.bottoms[i]:
            raise Exception("pop called on empty stack {stackno}")
        self.tops[i] -= 1
        return self.arr[self.tops[i]]


class TestThreeStacks(unittest.TestCase):
    def test_each_stack(self):
        stack_size = 10
        for stackno in range(1, 4):
            with self.subTest(stackno=stackno):
                arr = [random.randint(0, 5) for i in range(stack_size)]
                stacks = ThreeStacks(stack_size)
                for val in arr:
                    stacks.push(stackno, val)
                with self.assertRaises(Exception):
                    stacks.push(stackno, 0)
                for val in reversed(arr):
                    self.assertEqual(stacks.pop(stackno), val)
                with self.assertRaises(Exception):
                    stacks.pop(stackno)

    def test_stacks(self):
        stack_size = 10
        arr = [[],  # for simple test indexing
               [i for i in range(stack_size)],
               [i for i in reversed(range(stack_size))],
               [random.randint(0, 5) for i in range(stack_size)]]
        stacks = ThreeStacks(stack_size)
        for i in range(stack_size):
            for stackno in range(1, 4):
                with self.subTest(i=i, stackno=stackno):
                    stacks.push(stackno, arr[stackno][i])
        for stackno in range(1, 4):
            with self.assertRaises(Exception):
                stacks.push(stackno, 0)
        for i in reversed(range(stack_size)):
            for stackno in range(1, 4):
                with self.subTest(i=i, stackno=stackno):
                    self.assertEqual(stacks.pop(stackno), arr[stackno][i])
        for stackno in range(1, 4):
            with self.assertRaises(Exception):
                stacks.pop(stackno)


if __name__ == "__main__":
    unittest.main()
