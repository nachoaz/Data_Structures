# stack.py
"""
Simple linked_list-based implementation of a stack.
"""


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack(object):
    def __init__(self, node=None):
        self.top = node

    def push(self, data):
        self.top = Node(data, next=self.top)

    def pop(self):
        if self.top is not None:
            node_to_pop = self.top
            data_to_return = node_to_pop.data
            self.top = node_to_pop.next
            del node_to_pop
        else:
            data_to_return = None

        return data_to_return

    def peek(self):
        return self.top.data if self.top is not None else None

    def is_empty(self):
        return self.top is None
