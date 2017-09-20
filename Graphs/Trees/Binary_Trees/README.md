Binary Trees
============

Description
-----------
A 'binary tree' is a rooted tree in which each node either doesn't have
children, or has at most 2 children. Of the nodes that do have children, each
has a 'left subtree' and a 'right subtree'. With the exception of the root node,
all nodes have a parent.

Some Terminology
----------------
Any node _p_ might have up to two children: a left child (_l_), and a right
child (_r_); _p_ is said to be the _parent_ of _l_ and _r_, and _l_ and _r_ are
themselves the _root_ of _p_'s _left subtree_ and _right subtree_.

All nodes except for the root node have a unique parent.

For any node, there exists a unique sequence of nodes from the root to that node
with each node in that sequence being a _child_ of the previous node. (This
sequence can be called the _search path_ from the root to the node. A node _a_
is said to be an _ancestor_ of node _d_ if _a_ lies in the _search path_ from
the root to _d_. If a node is an _ancestor_ of _d_, then we say _d_ is a
_descendant_ of that node. (And so _d_ is both an ancestor and a descendant of
itself). With this we can define a _leaf_: a _leaf_ is a node that has no
descendants other than itself.

The _depth_ of a node _n_  is the number of nodes on the search path from the
root to it, not including _n_ itself. The _height_ of the binary tree is the
maximum depth of any node in that tree. A _level_ of a tree consists of all the
nodes at the same depth.

A left-skewed tree is a tree in which no nodes have a right child; a
right-skewed tree is a tree in which no nodes have a left child.

Traversals
----------
There are three common ways to traverse a tree:
  1. In-order: traverse the left subtree, visit the root, and traverse the right
     subtree.
  2. Pre-order: visit the root, traverse the left subtree, and traverse the
     right subtree.
  3. Post-order: traverse the left subtree, traverse the right subtree, and
     visit the root.

Note that these traversals can be defined recursively. (Remember, though, if
you're going to implement these recursively, be aware of the space requirements
implied by the call stack. See a visualization of each below.

![In-order Traversal](./images/inorder_traversal.svg)
