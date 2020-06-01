# Queue via Stacks
# Implement a MyQueue class which implements a queue using two stacks.

from myqueue import AbstractQueue, test_queue
from mystack import Stack
import unittest


class QueueUsingStacks(AbstractQueue):
    def __init__(self, arr=None):
        self.addstack = Stack()
        self.removestack = Stack()
        if arr is not None:
            for val in arr:
                self.add(val)

    def __iter__(self):
        for val in self.removestack:
            yield val
        added = []
        for val in self.addstack:
            added.append(val)
        for val in reversed(added):
            yield val

    def __len__(self):
        return self.length

    def __str__(self):
        """Returns space-separated string of values in queue, front to back"""
        vals = []
        for val in self:
            vals.append(str(val))
        return " ".join(vals)

    def add(self, val) -> None:
        """Adds `val` to end of queue"""
        self.addstack.push(val)

    def remove(self):
        """Removes and returns first value in queue"""
        if self.isempty():
            raise Exception("Called remove on empty queue")
        if self.removestack.isempty():
            self.__push_add_to_remove()
        return self.removestack.pop()

    def peek(self):
        """Returns first value in queue without removing"""
        if self.isempty():
            raise Exception("Called peek on empty queue")
        if self.removestack.isempty():
            self.__push_add_to_remove()
        return self.removestack.peek()

    def isempty(self) -> bool:
        """Returns true iff queue is empty"""
        return self.addstack.isempty() and self.removestack.isempty()

    def __push_add_to_remove(self) -> None:
        """Moves all elements in `addstack` to `removestack`, inverting order"""
        while not self.addstack.isempty():
            val = self.addstack.pop()
            self.removestack.push(val)


class TestQueueUsingStacks(test_queue(lambda x=None: QueueUsingStacks(x))):
    pass


if __name__ == "__main__":
    unittest.main()
