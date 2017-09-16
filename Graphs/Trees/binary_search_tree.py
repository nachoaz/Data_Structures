"""Defines BinarySearchTree class"""

from __future__ import division
from math import ceil

class Node(object):
    """A node that's part of the BST"""

    def __init__(self, dat=None):
        self.data = dat
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self):
        return "Node with data {}.".format(self.data)


class BinarySearchTree(object):
    """A BST"""

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def insert(self, dat):
        node_to_insert = Node(dat)
        current_nodes_parent = None
        current_node = self.root

        while current_node is not None:
            current_nodes_parent = current_node

            if node_to_insert.data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right

        node_to_insert.parent = current_nodes_parent

        if current_nodes_parent is None:
            self.root = node_to_insert # tree was empty
        elif node_to_insert.data < current_nodes_parent.data:
            current_nodes_parent.left = node_to_insert
        else:
            current_nodes_parent.right = node_to_insert

        self.size += 1

    def _is_empty(self):
        return self.root is None

    def _min_for_subtree_rooted_at(self, root):
        """Returns min (leftmost node) of (sub)tree rooted at root."""
        current_node = root
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def min(self):
        return _min_for_subtree_rooted_at(self.root)

    def search(self, dat):
        """Returns node that contains data dat if such node is present.
        If no such node is present, returns None."""
        current_node = self.root
            
        while (current_node is not None) and (current_node.data != dat):
            if dat < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right
            
        return current_node

    def predecessor(self, dat):
        pass

    def successor(self, dat):
        """Returns node that is successor of node that has data dat.
        If no node has data dat, returns None.
        If node that has data dat has no successor, returns None."""

        subject_node = self.search(dat)

        if subject_node.right is not None:
            # if subject_node has right subtree, successor is min of that tree 
            return _min_for_subtree_rooted_at(subject_node.right)
        else:
            # if subject_node doesn't have right subtree, successor is first
            # ancestor-whose-left-child-is-on-root-to-subject-node-path
            current_node = subject_node
            current_ancestor = current_node.parent
            
            while not (current_ancestor.left == current_node):
                current_node = current_ancestor
                current_ancestor = current_node.ancestor

            if current_ancestor.data >= subject_node.data:
                return current_ancestor
            else:
                return None

    def _preorder_traversal(self, root):
        if root is not None:
            print root.data
            _preorder_traversal(root=root.left)
            _preorder_traversal(root=root.right)

    def _inorder_traversal(self, root):
        if root is not None:
            _inorder_traversal(root=root.left)
            print root.data
            _inorder_traversal(root=root.right)

    def _postorder_traversal(self, root):
        if root is not None:
            _postorder_traversal(root=root.left)
            _postorder_traversal(root=root.right)
            print root.data

    def traverse(self, order="in"):
        if order == "pre":
            self._preorder_traversal(self.root)
        elif order == "in":
            self._inorder_traversal(self.root)
        elif order == "post":
            self._postorder_traversal(self.root)
        else:
            raise Exception("ERROR: order must be one of 'pre', 'in', or \
            'post'.")
    
    def delete(self, dat):
        node_to_delete = self._find_node_given_data(dat)

        # if node_to_delete has no children, remove it by modifying its parent
        # to replace node_to_delete with None as its child


        # if node_to_delete has just one child, we elevate that child to take
        # node_to_delete's place by modifying node_to_delete's parent to replace
        # node_to_delete by node_to_delete's only child

        # if node_to_delete has two children, we find its successor and have the
        # successor take node_to_delete's place

    def get_tree_info(self):
        """Returns a list of lists. Each list contains the nodes of the tree at
        the corresponding depth level"""
        if self._is_empty():
            raise Exception("ERROR: tree is empty!")

        tree_info = list()
        tree_info_nodes = list()
        current_depth = 0

        tree_info_nodes.append([self.root])
        tree_info.append([self.root.data])
        keep_going = True

        while keep_going:
            tree_info_nodes.append(list())
            tree_info.append(list())

            for i in xrange(2**current_depth):
                current_node = tree_info_nodes[current_depth][i]

                if current_node is not None and current_node.left is not None:
                    tree_info_nodes[current_depth + 1].append(current_node.left)
                    tree_info[current_depth + 1].append(current_node.left.data)
                else:
                    tree_info_nodes[current_depth + 1].append(None)
                    tree_info[current_depth + 1].append(None)

                if current_node is not None and current_node.right is not None:
                    tree_info_nodes[current_depth + 1].append(current_node.right)
                    tree_info[current_depth + 1].append(current_node.right.data)
                else:
                    tree_info_nodes[current_depth + 1].append(None)
                    tree_info[current_depth + 1].append(None)

            current_depth += 1

            if not any(tree_info_nodes[current_depth]):
                keep_going = False
                del tree_info_nodes[current_depth]
                del tree_info[current_depth]

        return tree_info

    @property
    def height(self):
        if self.root is None:
            raise Exception("ERROR: Tree is empty!")
        else:
            return self._get_height_of_subtree_rooted_at(self.root)

    def _get_height_of_subtree_rooted_at(self, root):
        if root is None:
            return -1
        else:
            left_height = self._get_height_of_subtree_rooted_at(root.left)
            right_height = self._get_height_of_subtree_rooted_at(root.right)
            return max(left_height, right_height) + 1

    def __repr__(self):
        """Returns string to print on console to represent tree."""

        def get_last_lists_contents(tree_height, node_info):
            leaves_str = ''
            for i, element in enumerate(node_info[-1]):
                element = element if element is not None else ' '
                if (i+1) % 2 == 1:
                    leaves_str += str(element)
                else:
                    leaves_str += ' '*3 + str(element) + ' '

            return  leaves_str[:-1] if len(leaves_str) > 1 else leaves_str

        tree_node_info = self.get_tree_info()

        # the maximum possible width of a tree with height h is 2^h, and
        # there'll be (h+1) + h lines to print ((h+1) of nodes, h of edges)
        height = self.height
        translated_height = int((height + 1) + height)
        translated_width = int(2**height + (0.5*2**height-1) + \
                           3*(0.5*2**height))
        
        str_to_return = ''
        for i in xrange(len(tree_node_info) - 1):
            for element in tree_node_info[i]:
                element = element if element is not None else ' '
                str_to_return += "{0:^{1}}".format(str(element),
                            translated_width // 2**i)
                if element != tree_node_info[i][-1]:
                    str_to_return += ' '
                else:
                    str_to_return += '\n'
            current_width = translated_width // 2**i
            num_of_dashes = int((current_width // 2) - ceil((current_width // 2)
                        / 2) - 1)
            left_half = "{0:>{1}}".format('/' + '-'*num_of_dashes,
                        current_width // 2)
            right_half = "{0:<{1}}".format('-'*num_of_dashes + '\\',
                        current_width // 2)
            combined_string = left_half + ' ' + right_half
            
            string_to_insert = combined_string
            
            for k in range(2**(i+1)):
                if tree_node_info[i+1][k] is not None:
                    if (k+1) % 2 == 1:
                        str_to_return += left_half
                    else:
                        str_to_return += right_half
                else:
                    str_to_return += ' '*int((current_width // 2))
                if k != 2**(i+1) - 1:
                    str_to_return += ' '
                else:
                    str_to_return += '\n'

        str_to_return += get_last_lists_contents(height, tree_node_info)

        return str_to_return

