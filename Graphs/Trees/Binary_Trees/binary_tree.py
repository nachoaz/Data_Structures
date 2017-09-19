# binary_tree.py

""" Defines the BinaryTreeNode and BinaryTree classes"""


class BinaryTreeNode(object):
    
    def __init__(self, data=None, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        return "Node with data {}."format(self.data) else "Empty node."


class BinaryTree(object):
    
    def __init__(self, root=None):
        self.root = root
