"""Implements HeadAndTailPtrSinglyLinkedList and
HeadPtrSinglyLinkedListClasses"""

class SinglyLinkedListNode(object):
    """Node for singly linked list"""

    def __init__(self, dat=None, next_node=None):
        self.data = dat
        self.next = next_node

    def __repr__(self):
        return "SinglyLinkedListNode with data {0}".format(self.data)


class HeadAndTailPtrSinglyLinkedList(object):
    """Singly linked list with both a head and tail pointer.
    
    This type of list is useful for when implementing a queue.
    
    When implementing a queue, enqueue by inserting at tail, dequeue by removing
    from head.
    """

    def __init__(self):
        self.head = None
        self.tail = None


    def _is_empty(self):
        return (self.head is None) and (self.tail is None)


    def insert_at_tail(self, dat):
        """Insert node at tail of list. O(1) operation."""
        node_to_insert =SinglyLinkedListNode(dat)

        if self._is_empty():
            self.head = node_to_insert
            self.tail = self.head
        else:
            node_currently_at_tail = self.tail
            node_currently_at_tail.next = node_to_insert
            self.tail = node_to_insert


    def remove_from_head(self):
        """Remove node at head of list. O(1) operation."""
        if self._is_empty():
            raise Exception("ERROR: List is empty!")
        else:
            node_to_remove = self.head
            self.head = node_to_remove.next
            node_to_remove.next = None
            del node_to_remove
            
            # if deleted node was head, update tail attribute
            if self.head is None:
                self.tail = self.head


    def __repr__(self):
        if self._is_empty():
            raise Exception("ERROR: List is empty!")
        else:
            str_to_return = ''

            current_node = self.head

            while current_node.next is not None:
                str_to_return += "| {0} | --> ".format(current_node.data)
                current_node = current_node.next

            str_to_return += "| {0} |".format(current_node.data)

            return str_to_return


class HeadPtrSinglyLinkedList():
    pass

