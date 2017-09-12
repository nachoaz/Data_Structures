# stack_with_max_api
"""
Implements a stack with a O(1)-time operation to get the max of the stack.
"""

from stack import Node, Stack


class StackWithMaxAPI(Stack):
    def __init__(self, node=None):
        super(StackWithMaxAPI, self).__init__(node)
        self.maxs = Stack(node)

    def push(self, data):
        super(StackWithMaxAPI, self).push(data)
        if data >= self.max():
            self.maxs.push(data)

    def pop(self):
        popped_val = super(StackWithMaxAPI, self).pop()
        if popped_val == self.max():
            self.maxs.pop()
        return popped_val

    def max(self):
        return self.maxs.peek() if self.maxs.top is not None else float('-inf')
