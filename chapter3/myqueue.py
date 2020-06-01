from abc import ABC, abstractmethod
from test_generator import generate_tests
from typing import Callable
import unittest


class AbstractQueue(ABC):
    """Abstract queue class"""

    @abstractmethod
    def __str__(self):
        """Returns space-separated string of values in queue, front to back"""
        pass

    @abstractmethod
    def add(self, val) -> None:
        """Adds `val` to end of queue"""
        pass

    @abstractmethod
    def remove(self):
        """Removes and returns first value in queue"""
        pass

    @abstractmethod
    def peek(self):
        """Returns first value in queue without removing"""
        pass

    @abstractmethod
    def isempty(self) -> bool:
        """Returns true iff queue is empty"""
        pass


class Queue(AbstractQueue):
    """Queue class"""

    class Node:
        """Node class for Queue"""

        def __init__(self, val, nxt=None):
            self.val = val
            self.next = nxt

        def __str__(self):
            return str(self.val)

    def __init__(self, arr=None):
        """Inits queue with vals in `arr`"""
        self.front = None
        self.back = None
        self.length = 0
        if arr is not None:
            for val in arr:
                self.add(val)

    def __iter__(self):
        curr = self.front
        while curr is not None:
            yield curr.val
            curr = curr.next

    def __len__(self):
        return self.length

    def __str__(self):
        """Returns space-separated string of values in queue, front to back"""
        return " ".join([str(val) for val in self])

    def add(self, val) -> None:
        """Adds `val` to end of queue"""
        n = self.Node(val)
        if self.isempty():
            self.front = n
        else:
            self.back.next = n
        self.back = n
        self.length += 1

    def remove(self):
        """Removes and returns first value in queue"""
        if self.isempty():
            raise Exception("Called pop on empty stack")
        self.length -= 1
        val = self.front.val
        self.front = self.front.next
        return val

    def peek(self):
        """Returns first value in queue without removing"""
        if self.isempty():
            raise Exception("Called peek on empty stack")
        return self.front.val

    def isempty(self) -> bool:
        """Returns true iff queue is empty"""
        return self.length == 0


def test_queue(make_queue: Callable[[], AbstractQueue]):
    """Tests queue functions add(), peek(), remove(), isempty(),
    where make_queue() returns a new queue"""
    class TestQueue(unittest.TestCase):
        def test_queue_add(self):
            tests = generate_tests()
            for test in tests:
                with self.subTest(test=test):
                    q: AbstractQueue = make_queue()
                    self.assertTrue(q.isempty())
                    for val in test:
                        q.add(val)
                        self.assertFalse(q.isempty())
                        self.assertEqual(q.peek(), test[0])

        def test_queue_remove(self):
            tests = generate_tests()
            for test in tests:
                with self.subTest(test=test):
                    q: AbstractQueue = make_queue(test)
                    for val in test:
                        self.assertFalse(q.isempty())
                        self.assertEqual(q.peek(), val)
                        self.assertEqual(q.remove(), val)
                    self.assertTrue(q.isempty())
                    with self.assertRaises(Exception):
                        q.remove()

        def test_queue_add_remove(self):
            tests = generate_tests()
            test1, test2, test3 = tests[-1], tests[-2], tests[-3]
            q: AbstractQueue = make_queue(test1)
            self.assertEqual(q.remove(), test1[0])
            for val in test2:
                q.add(val)
            self.assertEqual(q.remove(), test1[1])
            self.assertEqual(q.remove(), test1[2])
            for val in test3:
                q.add(val)
            for val in test1[3:]:
                self.assertEqual(q.remove(), val)
            for val in test2:
                self.assertEqual(q.remove(), val)
            for val in test3:
                self.assertEqual(q.remove(), val)

    return TestQueue


class TestBaseQueue(test_queue(lambda x=None: Queue(x))):
    pass


if __name__ == "__main__":
    unittest.main()
