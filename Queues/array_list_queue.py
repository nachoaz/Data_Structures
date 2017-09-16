# queue.py
"""
Implements an array-list-(list)-based queue.
"""


class Queue(object):
    def __init__(self):
        self._data = []

    def __repr__(self):
        if self.empty():
            return "Empty queue."
        else:
            return str(self._data)

    def empty(self):
        return len(self._data) == 0

    def enqueue(self, x):
        self._data.append(x)

    def dequeue(self):
        if self.empty():
            raise IndexError("dequeue(): empty queue.")
        else:
            return self._data.pop(0)
    
    def peekfront(self):
        if self.empty():
            raise IndexError("peekfront(): empty queue.")
        else:
            return self._data[0]

    def peekback(self):
        if self.empty():
            raise IndexError("peekback(): empty queue.")
        else:
            return self._data[-1]
