Binary Search Trees
===================

Description
-----------
A 'Binary Search Tree' is a binary tree that adheres to the following principle
(or convention): Let x be node in a binary search tree. If y is a node in the
left subtree of x, then y.key <= x.key If z is a node to the right subtree of
x, then z.key >= x.key.

Binary search trees are good 'all terrain' data struture; they support the basic
operations (search, insertion, deletion) and have a few added attractive
features (they can give you the min and max of a set, and they can give you the
predecessor and successor of any given element of the set). However --due to the
potential imbalance in their structure-- they carry out all of these operations
in at worst O(n) time and log(n) at best (actually, they carry out the
operations in precisely O(h), where h is the height); so their efficiency is
hinged on how well they're balanced. Because there's no guarantee that the BST
is going to be balanced, the operations might take as long as O(n); so the
generic BST is more of a springboard onto more specialized versions of BSTs. One
of these such specialized versions are Red-Black trees, which use a 'color'
attribute on each node to guarantee (approximate) balance, which in turn
guarantees 'good' (O(logn)) performance on the basic operations.

Applications
------------
A typical application of BSTs is searching (they allow for 'fast' searches,
unlike arrays and linked-lists). A hash table also supports 'fast'(er) searches,
but a BST goes further and offers the ability to find the min and max elements,
and to find the next largest/next smallest element. Both BSTs and hash tables
use O(n) space for storage (in practice BSTs use slightly more storage than hash
tables do, although it's still linear relative to the input).
