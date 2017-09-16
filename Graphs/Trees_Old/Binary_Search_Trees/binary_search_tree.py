
class Node(object):
    """
    Attributes
        - left: left child
        - right: right child
        - parent: parent
        - value: value
    """
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value

    def __repr__(self):
        return "Node with value: %s" % self.value

class BinarySearchTree(object):
    """
    (Generic) Binary Search Tree
    *******************
    *   Description   *
    *******************
    Typically, we use a Binary Search Tree when we have a list (or collection) of numbers, and need to be able to do all (or most) of these things: (1) check if a number is in the list (search), (2) insert a new number into the list, (3) delete a number from the list, (4) get the smallest number from that list, (5) get the largest number from that list, (6) get the successor of a number within that list, (7) get the predecessor of a number within that list.

    (Terminology: given y, x is the predecessor of y if it's the number to the left of x in the sorted list (where list was sorted in nondecreasing order). Similary, z (the successor) is to the right.)

    Note, however, that in practice we don't use Binary Search Trees unless we know they'll be perfectly balanced; this is because if we don't have the guarantee that it'll be perfectly balanced, then the BST might only yield 'fair' (aka O(n)) performance for these operations (this occurs in the worst case, which is when the BST is perfectly imbalanced). This is why the generic BST is more of a base model for more specialized data structures, such as Red-Black trees (and other variations of BSTs that follow a 'balanced' scheme).

    Red-Black trees are a special case of Binary Search Trees which DO have the guarantee of being (approximately) balanced.

    Question: Doing an inorder-tree-walk on a BST gives you the keys (or values, whatever you want) of the BST in sorted order. If I have a list (or collection) of numbers, can't I use a BST to sort that list in O(n) time?
    Answer: No. It costs O(n) to do the inorder-tree-walk, yes. But it also costs O(n) to build the BST in the first place.

    ***************
    *   Methods   *
    ***************
    The methods of an object of type BinarySearchTree (as defined by my class) are:
    is_empty(), find_element(value), get_min(), get_max(), predecessor(value), successor(value), insert(value), delete(value), values()

    *************************************
    *   Time Complexity of Operations   *
    *************************************
    NOTE: h is height of the tree. h can be at best floor(log(n)) (or simply logn) (if tree perfectly blanced), or at worst O(n) (if not balanced)

    access: (same as search)
    search: O(h) because sought-after-node found by following simple path to sought-after-node (which may or may not be at deepest level)
    insert: O(h) because to insert a node X, we follow a simple path, asking: should X be in the right subtree here or in the left? Since path is simple, it's at most length h.
    delete: O(h) because to delete a node Z, we have three cases (if Z no children, simply remove Z), (if Z one child, remove Z and elevate child to take Z's position), (if Z two children, find Z's successor Y - which will be in Z's right subtree - and have Y take Z's position).
    get_min: O(h) because min found by following a simple path to deepest leftmost node
    get_max: O(h) because max found by following a simple path from root to deepest rightmost node
    predecessor: O(h) because predecessor found by either following a simple path UP from (given) origin node or a simple path DOWN from (given) origin node(If the left subtree of node x is nonempty, then the successor of x is just the rightmost node in x’s left subtree. If the left subtree of node x is empty and x has a successor y, then y is the lowest ancestor of x whose right child is also an ancestor of x.)
    successor: O(h) because successor found through similar process as predecessor (If the right subtree of node x is nonempty, then the successor of x is just the leftmost node in x’s right subtree. If the right subtree of node x is empty and x has a successor y, then y is the lowest ancestor of x whose left child is also an ancestor of x.)
    values: O(n) because this requires traversing the entire tree
    """
    def __init__(self):
        self.root = None
        self.len = 0

    def __len__(self):
        return self.len

    def is_empty(self):
        return self.root == None

    def _preorder(self, node, values):
        if node != None:
            values.append(node)
            self._preorder(node.left, values)
            self._preorder(node.right, values)

    def _inorder(self, node, values):
        if node != None:
            self._inorder(node.left, values)
            values.append(node.value)
            self._inorder(node.right, values)

    def _postorder(self, node, values):
        if node != None:
            self._inorder(node.left, values)
            self._inorder(node.right, values)
            values.append(node.value)

    def values(self, order = 'in'):
        'lists the values in the specified order: \'pre\', \'in\' (default), or \'post\''
        values = []
        if order == 'in': self._inorder(self.root, values)
        elif order == 'pre': self._preorder(self.root, values)
        elif order == 'post': self._postorder(self.root, values)
        return values

    def _search(self, root, value):
        if root is None or root.value == value:
            return root
        if value < root.value:
            return self._search(root.left, value)
        else:
            return self._search(root.right, value)

    def find_element(self, value):
        'searches the BST for a node with a given value and returns it'
        return self._search(self.root, value)

    def get_min(self, x):
        'returns the node with the minimum value in the subtree rooted at x'
        while x.left != None:
            x = x.left
        return x

    def get_max(self, x):
        'returns the node with the maximum value in the subtree rooted at x'
        while x.right != None:
            x = x.right
        return x

    def successor(self, in_value):
        'returns the node that would be to the right of in_value on a sorted list of values'

    def predecessor(self, in_value):
        'returns the node that would be to the left of in_value on a sorted list of values'

    def insert(self, value):
        # my code here

    def delete(self, value):
        # my code here
