import unittest


class Stack:
    """Stack class that keeps track of min element"""

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

    def __len__(self):
        return self.length

    def __str__(self):
        """Returns string of values from stack top to bottom"""
        vals = []
        curr = self.top
        while curr is not None:
            vals.append(str(curr))
            curr = curr.next
        return " ".join(vals)

    def push(self, val):
        """Adds value to top of stack"""
        n = self.Node(val)
        if not self.isempty():
            n.next = self.top
        self.top = n
        self.length += 1

    def pop(self):
        """Removes and returns top value from stack"""
        if self.isempty():
            raise Exception("Called pop on empty stack")
        self.length -= 1
        val = self.top.val
        self.top = self.top.next
        return val

    def peek(self):
        """Returns top value from stack without removing"""
        if self.isempty():
            raise Exception("Called peep on empty stack")
        return self.top.val

    def isempty(self) -> bool:
        """Returns true iff stack is empty"""
        return self.length == 0


class TestLinkedList(unittest.TestCase):
    def test_stack(self):
        arr = [i for i in range(5)]
        stack = Stack(arr)
        self.assertEqual(str(stack), " ".join(map(str, reversed(arr))))
        for val in reversed(arr):
            self.assertEquals(stack.peek(), val)
            self.assertEqual(stack.pop(), val)
        with self.assertRaises(Exception):
            stack.pop()


if __name__ == "__main__":
    unittest.main()
