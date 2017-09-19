# min_heap.py


class MaxHeap(object):
    
    def __init__(self, items=None):
        self.items = list()
        if items:
            self.build_heap(items)

    def _left_ix(self, ix):
        return 2*ix + 1

    def _right_ix(self, ix):
        return 2*ix + 2

    def _parent(self, ix):
        return math.floor((ix-1) / 2.0)

    def _swap(self, ix1, ix2):
        self.items[ix1], self.items[ix2] = self.items[ix2], self.items[ix1]

    def build_heap(self, items):
        for i in items:
            self.items.append(i)
            self.bubble_up(len(self.items)-1)

    def bubble_up(self, ix):
        parent_ix = self._parent_ix(ix)

        while parent_ix and self.items[ix] > self.items[parent_ix]:
            self._swap_itemsp(ix, parent_ix)
            ix, parent_ix = parent_ix, self._parent_ix(parent_ix)


    def bubble_down(self, ix):
        l_ix, r_ix = self._left_ix(ix), self._right_ix(ix)

        while (l_ix or r_ix) and (self.items[ix] < self.items[r_ix] or
                                  self.items[ix] < self.items[l_ix):
            great_c_ix = l_ix if self.items[l_ix] > self.items[r_ix] else r_ix
            self._swap(ix, great_c_ix)
            ix = great_c_ix
            l_ix, r_ix = self._left_ix(ix), self.right_ix(ix)

    def insert(self, data):
        # Place at leftmost position of lowest level to keep complete-tree prop
        self.items.append(data)
        # Bubble up to maintain min-heap property
        self.bubble_up(len(self.items)-1)

    def max(self):
        return self.items[0] if self.items[0] else None

    def extract_min(self):
        # Replace min with lowest-level-leftmost-item
        self._swap(0, len(self.items)-1)
        max_item = self.items.pop()
        self.bubble_down(0)
        return max_item
