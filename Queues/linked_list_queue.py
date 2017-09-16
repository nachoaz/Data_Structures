# queue.py
"""
Implements a linked-list-based queue.
"""


class Node(object):
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Queue(object):
    def __init__(self, node=None):
        self.front = node
        self.back = node

    def enqueue(self, data):
        if self.empty():
            self.front = self.back = Node(data)
        else:
            orig_back = self.back
            self.back = Node(data, next=orig_back)
            orig_back.prev = self.back

    def dequeue():
        if self.empty():
            raise IndexError("pop(): empty queue")
        else:
            orig_front = self.front
            self.front = prev_front.prev
            self.front.next = None
            del orig_front

    def peek():
        if self.empty():
            return None
        else:
            return self.front.data

    def empty():
        return self.front is None
