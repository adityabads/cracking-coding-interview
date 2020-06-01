# Stack of Plates
# Imagine a (literal) stack of plates. If the stack gets too high, it might
# topple. Therefore, in real life, we would likely start a new stack when the
# previous stack exceeds some threshold. Implement a data structure SetOfStacks
# that mimics this. SetOfStacks should be composed of several stacks and should
# create a new stack once the previous one exceeds capacity. SetOfStacks.push()
# and SetOfStacks.pop() should behave identically to a single stack (that is,
# pop() should return the same values as it would if there were just a single stack).
#
# FOLLOW UP
# Implement a function popAt(int index) which performs a pop operation on a
# specific sub-stack.

from mystack import AbstractStack, Stack, test_stack
import unittest


class SetOfStacks(AbstractStack):
    """Set of stacks, each with a maximum size, behaving like a single stack"""

    def __init__(self, arr=None, max_stack_size: int = 5):
        """Inits set of stacks with values in `arr` and max stack size"""
        self.stackset = Stack()
        self.length = 0
        self.MAXSIZE = max_stack_size
        if arr is not None:
            for val in arr:
                self.push(val)

    def __len__(self):
        return self.length

    def __str__(self):
        """Returns space-separated string of values in stack, top to bottom"""
        vals = []
        currstack = self.stackset.top
        while currstack is not None:
            vals.append(str(currstack))
            currstack = currstack.next
        return " ".join(vals)

    def push(self, val):
        """Adds `val` to top of set of stacks, creating new stack if necessary"""
        if self.isempty() or len(self.stackset.peek()) == self.MAXSIZE:
            s = Stack([val])
            self.stackset.push(s)
        else:
            self.stackset.peek().push(val)
        self.length += 1

    def pop(self):
        """Removes and returns top value in set of stacks"""
        if self.isempty():
            raise Exception("Called pop on empty stack")
        val = self.stackset.peek().pop()
        if self.stackset.peek().isempty():
            self.stackset.pop()
        self.length -= 1
        return val

    def peek(self):
        """Returns top value in set of stacks without removing"""
        return self.stackset.peek().peek()

    def isempty(self):
        """Returns true iff stack is empty"""
        return self.length == 0


class TestSetOfStacks(test_stack(lambda x=None: SetOfStacks(x))):
    pass


if __name__ == "__main__":
    unittest.main()
