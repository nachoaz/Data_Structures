# min_heap_using_lib.py


import heapq

class MinHeap(object):

    def __init__(self, items=None):
        self.heap = items
        if items:
            self.heap = items
            heapq.heapify(self.heap)

    def insert(self, item):
        heapq.heappush(self.heap, item)

    def extract_min(self):
        heapq.heappop(self.heap)

    def min(self):
        return self.heap[0] if self.heap else None
