"""
Design a stack that supports push, pop, top, and retrieving the minimum element
in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Tag: Stack, Data Structure
"""


class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, number):
        # Notice: we need to push min stack too if the number is equal to
        # current minimum value.
        if not self.min_stack or number <= self.min_stack[-1]:
            self.min_stack.append(number)
        self.stack.append(number)

    def pop(self):
        val = self.stack.pop()
        if self.min_stack and self.min_stack[-1] == val:
            self.min_stack.pop()
        return val

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]
