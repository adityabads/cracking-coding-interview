from abc import ABC, abstractmethod
from test_generator import generate_tests
from typing import Callable
import unittest


class AbstractStack(ABC):
    """Abstract stack class"""

    @abstractmethod
    def __str__(self):
        """Returns space-separated string of values in stack, top to bottom"""
        pass

    @abstractmethod
    def push(self, val) -> None:
        """Adds `val` to top of stack"""
        pass

    @abstractmethod
    def pop(self):
        """Removes and returns top value in stack"""
        pass

    @abstractmethod
    def peek(self):
        """Returns top value in stack without removing"""
        pass

    @abstractmethod
    def isempty(self) -> bool:
        """Returns true iff stack is empty"""
        pass


class Stack(AbstractStack):
    """Stack class"""

    class Node:
        """Node class for Stack"""

        def __init__(self, val, nxt=None):
            self.val = val
            self.next = nxt

        def __str__(self):
            return str(self.val)

    def __init__(self, arr=None):
        """Inits stack with vals in `arr`"""
        self.top = None
        self.length = 0
        if arr is not None:
            for val in arr:
                self.push(val)

    def __iter__(self):
        curr = self.top
        while curr is not None:
            yield curr.val
            curr = curr.next

    def __len__(self):
        return self.length

    def __str__(self):
        """Returns space-separated string of values in stack, top to bottom"""
        return " ".join([str(val) for val in self])

    def push(self, val) -> None:
        """Adds `val` to top of stack"""
        n = self.Node(val)
        if not self.isempty():
            n.next = self.top
        self.top = n
        self.length += 1

    def pop(self):
        """Removes and returns top value in stack"""
        if self.isempty():
            raise Exception("Called pop on empty stack")
        self.length -= 1
        val = self.top.val
        self.top = self.top.next
        return val

    def peek(self):
        """Returns top value in stack without removing"""
        if self.isempty():
            raise Exception("Called peek on empty stack")
        return self.top.val

    def isempty(self) -> bool:
        """Returns true iff stack is empty"""
        return self.length == 0


def test_stack(make_stack: Callable[[], AbstractStack]):
    """Tests stack functions push(), peek(), pop(), isempty(),
    where `make_stack` returns a new stack"""

    class TestStack(unittest.TestCase):
        def test_stack_add(self):
            tests = generate_tests()
            for test in tests:
                with self.subTest(test=test):
                    stack: AbstractStack = make_stack()
                    self.assertTrue(stack.isempty())
                    for val in test:
                        stack.push(val)
                        self.assertFalse(stack.isempty())
                        self.assertEqual(stack.peek(), val)

        def test_stack_remove(self):
            tests = generate_tests()
            for test in tests:
                with self.subTest(test=test):
                    stack: AbstractStack = make_stack(test)
                    for val in reversed(test):
                        self.assertFalse(stack.isempty())
                        self.assertEqual(stack.peek(), val)
                        self.assertEqual(stack.pop(), val)
                    self.assertTrue(stack.isempty())
                    with self.assertRaises(Exception):
                        stack.pop()

        def test_stack_add_remove(self):
            tests = generate_tests()
            test1, test2, test3 = tests[-1], tests[-2], tests[-3]
            stack: AbstractStack = make_stack(test1)
            self.assertEqual(stack.pop(), test1[-1])
            for val in test2:
                stack.push(val)
            self.assertEqual(stack.pop(), test2[-1])
            self.assertEqual(stack.pop(), test2[-2])
            for val in test3:
                stack.push(val)
            for val in reversed(test3):
                self.assertEqual(stack.pop(), val)
            for val in reversed(test2[:len(test2)-2]):
                self.assertEqual(stack.pop(), val)
            for val in reversed(test1[:len(test1)-1]):
                self.assertEqual(stack.pop(), val)

    return TestStack


class TestBaseStack(test_stack(lambda x=None: Stack(x))):
    pass


if __name__ == "__main__":
    unittest.main()
