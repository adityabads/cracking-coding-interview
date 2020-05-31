import unittest


class Stack:
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
        """Returns string of values from stack top to bottom"""
        vals = []
        for val in self:
            vals.append(str(val))
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
            raise Exception("Called peek on empty stack")
        return self.top.val

    def isempty(self) -> bool:
        """Returns true iff stack is empty"""
        return self.length == 0


def test_stack(stack):
    """Tests stack.push(), stack.peek(), stack.pop(), stack.isempty()"""
    class TestStack(unittest.TestCase):
        def test_stack(self):
            test = [1, 3, 7, 4, 2, 9, 1, 5, 6, 5, 8]
            self.assertTrue(stack.isempty())
            for i in range(len(test)):
                stack.push(test[i])
                self.assertFalse(stack.isempty())
                self.assertEqual(stack.peek(), test[i])
                self.assertEqual(str(stack), " ".join(
                    map(str, reversed(test[:i+1]))))
            for i in range(len(test)):
                self.assertFalse(stack.isempty())
                self.assertEqual(str(stack), " ".join(
                    map(str, reversed(test[:len(test)-i]))))
                self.assertEqual(stack.peek(), test[-i-1])
                self.assertEqual(stack.pop(), test[-i-1])
            self.assertTrue(stack.isempty())
            with self.assertRaises(Exception):
                stack.pop()

    return TestStack


class TestBaseStack(test_stack(Stack())):
    pass


if __name__ == "__main__":
    unittest.main()
