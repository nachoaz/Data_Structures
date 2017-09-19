# binary_search_tree.py

""" Defines BinarySearchTree class."""


from math import ceil

class Node(object):
    """A node that's part of the BST"""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        if self.data:
            return "Node with data {}.".format(self.data)
        else:
            return "Empty node."


class BinarySearchTree(object):
    """A BST.
    The key stored at a node is greater than or equal to the keys stored at the
    nodes of its left subtree and less than or equal to the keys stored in the
    nodes of its right subtree.
    """

    def __init__(self):
        self.root = None
    

    def insert(self, data):
        pass
