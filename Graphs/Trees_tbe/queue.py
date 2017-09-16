"""Defines the SinglyLinkedListQueue and the ArrayQueue classes"""

from singly_linked_list import HeadAndTailPtrSinglyLinkedList

class SinglyLinkedListQueue(object):
    """A queue implemented using a linked list as underlying data structure.
    As such, there's no limit on how many elements it can hold.

    Use this when you don't know the max number of elements your queue could
    possibly hold. Push and Pop operations both take O(1) time and O(1) space.
    """

    def __init__(self, max_digits_in_element=4):
        self.length = 0
        self.digits = max_digits_in_element
        self.items = HeadAndTailPtrSinglyLinkedList()


    def _is_empty(self):
        return self.items._is_empty()


    def __repr__(self):
        if self._is_empty():
            raise Exception("ERROR: Queue is empty")
        else:
            str_to_return = ''
            ceil_floor_pattern = ' -' + '-'*self.digits + '- '

            str_to_return += ceil_floor_pattern*self.length + '\n'
            
            current_node = self.items.head

            while current_node.next is not None:
                str_to_return += "| {0:>{1}} |".format(current_node.data, 
                                                       self.digits)
                current_node = current_node.next

            str_to_return += "| {0:>{1}} |".format(current_node.data,
                    self.digits)

            str_to_return += '\n' + ceil_floor_pattern*self.length + '\n'

            return str_to_return
    

    def enqueue(self, item):
        """Push item onto queue. O(1) operation."""
        self.items.insert_at_tail(item)
        self.length += 1

    def dequeue(self):
        """Pop item at head of queue. O(1) operation."""
        if self._is_empty():
            raise Exception("ERROR: Queue is empty")
        else:
            self.items.remove_from_head()
            self.length -= 1


class ArrayQueue(object):
    """A queue implemented using an array as underlying data structure.
    As such, (attempting to) insert an element once array is full will cause a
    queue overflow.

    Use this when you know the max number of elements your queue could possibly
    hold. Push and Pop operations both take O(1) time and O(1) space.

    Args:
        capacity: the capacity you want your queue to hold.
        max_digits_in_element: the max num. of digits an element can have
    """

    def __init__(self, capacity=10, max_digits_in_element=4):
        self.cap = capacity
        self.length = 0
        self.items = [None]*self.cap
        self.digits = max_digits_in_element
        self.head = 0
        self.tail = 0

    
    def _is_full(self):
        return self.length == self.cap


    def _is_empty(self):
        return self.length == 0


    def __repr__(self):
        if self._is_empty():
            raise Exception("ERROR: Queue is empty!")
        else:
            str_to_return = ''

            ceil_floor_pattern = ' -' + '-'*self.digits + '- '

            str_to_return += ceil_floor_pattern*self.length + '\n'
            
            if self.head < self.tail:
                for item in self.items[self.head:self.tail]:
                    str_to_return += "| {0:>{1}} |".format(item, self.digits)
            else:
                # head >= tail, so queue wrapped around (if equal, queue full)
                for item in self.items[self.head:] + self.items[:self.tail]:
                    str_to_return += "| {0:>{1}} |".format(item, self.digits)

            str_to_return += '\n' + ceil_floor_pattern*self.length + '\n'

            return str_to_return


    def enqueue(self, item):
        """Push an item onto the queue. O(1) operation."""

        if self._is_full():
            raise Exception("ERROR: Queue Overflow!")
        else:
            self.items[self.tail] = item

            if self.tail != (self.cap - 1):
                self.tail += 1
            else:
                self.tail = 0

            self.length += 1


    def dequeue(self):
        """Pop item from queue. O(1) operation."""

        if self._is_empty():
            raise Exception("ERROR: Queue Underflow!")
        else:
            item_to_pop = self.items[self.head]

            if self.head != (self.cap - 1):
                self.head += 1
            else:
                self.head = 0

            self.length -= 1
            
            return item_to_pop
