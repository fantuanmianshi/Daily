"""
Implement the following operations of a queue using stacks.

    push(x) -- Push element x to the back of queue.
    pop() -- Removes the element from in front of queue.
    peek() -- Get the front element.
    empty() -- Return whether the queue is empty.

Notes:
* You must use only standard operations of a stack -- which means only push to
  top, peek/pop from top, size, and is empty operations are valid.

* Depending on your language, stack may not be supported natively. You may
  simulate a stack by using a list or deque (double-ended queue), as long as
  you use only standard operations of a stack.

* You may assume that all operations are valid (for example, no pop or peek
  operations will be called on an empty queue).
"""


class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack1.insert(0, x)        

    # @return nothing
    def pop(self):
        if self.stack2:
            return self.stack2.pop(0)

        while self.stack1:
            self.stack2.insert(0, self.stack1.pop(0))

        if self.stack2:
            return self.stack2.pop(0)
        return None

    # @return an integer
    def peek(self):
        if self.stack2:
            return self.stack2[0]

        while self.stack1:
            self.stack2.insert(0, self.stack1.pop(0))

        if self.stack2:
            return self.stack2[0]
        return None

    # @return an boolean
    def empty(self):
        return not (self.stack1 or self.stack2)
