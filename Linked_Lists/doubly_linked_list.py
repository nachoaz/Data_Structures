# doubly_linked_list.py


class DoublyLinkedListNode():
    """A node with data and next and prev attributes"""
    def __init__(self, dat, next_node=None, prev_node=None):
        self.data = dat
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return "| {} |".format(self.data)

    def __repr__(self):
        return self.__str__()


def DoublyLinkedList():
    """A doubly linked list with a head and a tail attribute"""
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        """Takes O(n) time, O(n) space.""" # O(n) space, right? string grows
        if self.is_empty():
            str_to_return = "List is empty!"
        else:
            current_node = self.head
            str_to_return = str(current_node)

            while current_node.next:
                current_node = current_node.next
                str_to_return += " --> " + str(current_node)

        return str_to_return
            
    def __repr__(self):
        """Takes O(n) time, O(n) space.""" # O(n) space, right? string grows
        return self.__str__()

    def __len__(self):
        """Takes O(n) time, O(1) space."""
        length = 0
        
        if not self.is_empty():
            current_node = self.head
            length += 1

            while current_node.next:
                current_node = current_node.next
                length += 1

        return length

    def is_empty(self):
        """Takes O(1) time, O(1) space."""
        return self.head is None

    def insert_val_at_head(self, val):
        """Takes O(1) time, O(1) space"""
        previous_head = self.head
        self.head = DoublyLinkedListNode(val, next_node=previous_head)
        if previous_head is not None:
            previous_head.prev = self.head

    def insert_val_at_tail(self, val):
        """Takes O(1) time, O(1) space"""
        previous_tail = self.tail
        self.tail = DoublyLinkedListNode(val, prev_node=previous_tail)
        if previous_tail is not None:
            previous_tail.next = self.tail

    def remove_from_head(self):
        """Takes O(1) time, O(1) space"""
        if self.is_empty():
            print("Nothing to remove! List is empty.")
        else:
            node_to_remove = self.head
            self.head = node_to_remove.next
            self.head.prev =  None
            del node_to_remove

    def remove_from_tail(self):
        """Takes O(1) time, O(1) space"""
        if self.is_empty():
            print("Nothing to remove! List is empty.")
        else:
            node_to_remove = self.tail
            self.tail = node_to_remove.prev
            self.tail.next = None
            del node_to_remove
