# singly_linked_list.py


class SinglyLinkedListNode():
    """A node with a data and next attribute."""
    def __init__(self, dat, next_node=None):
        self.data = dat
        self.next = next_node

    def __str__(self):
        return "| {} |".format(self.data)

    def __repr__(self):
        return self.__str__()


class SinglyLinkedList():
    """A singly linked list with only a head attribute."""
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.is_empty():
            list_string = "List is empty!"
        else:
            current_node = self.head

            list_string = str(current_node)
            while current_node.next:
                list_string += " --> " + str(current_node.next)
                current_node = current_node.next

        return list_string

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        length = 0
        current_node = self.head
        while current_node is not None:
            length += 1
            current_node = current_node.next

        return length

    def is_empty(self):
        """Returns true if list is empty. Takes O(1) time, O(1) space."""
        return self.head is None

    def insert_val_at_head(self, val):
        """Inserts val at head of linked list. Takes O(1) time, O(1) space."""
        previous_head = self.head
        self.head = SinglyLinkedListNode(val, next_node=previous_head)

    def insert_val_at_tail(self, val):
        """Inserts val at tail of linked list. Takes O(n) time, O(1) space."""
        if self.is_empty():
            self.head = SinglyLinkedListNode(val)
        else:
            current_node = self.head

            while current_node.next:
                current_node = current_node.next

            current_node.next = SinglyLinkedListNode(val)

    def remove_from_head(self):
        """Removes node at head of linked list. Takes O(1) time, O(1) space."""
        if self.is_empty():
            print("Nothing to remove! List is empty.")
        else:
            node_to_remove = self.head
            self.head = node_to_remove.next
            node_to_remove.next = None
            del node_to_remove

    def remove_from_tail(self):
        """Removes node at tail of linked list. Takes O(n) time, O(1) space."""
        if self.is_empty():
            print("Nothing to remove! List is empty.")
        else:
            behind_node = self.head

            if behind_node.next:
                ahead_node = behind_node.next

                while ahead_node.next:
                    behind_node = behind_node.next
                    ahead_node = ahead_node.next

                behind_node.next = None
                del ahead_node

            else:
                self.head = None
                del behind_node
