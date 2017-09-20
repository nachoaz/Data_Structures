Binary Search Trees
===================

Description
-----------
A 'Binary Search Tree' is a binary tree that adheres to the following principle
(or convention): Let x be node in a binary search tree. If y is a node in the
left subtree of x, then y.key <= x.key If z is a node to the right subtree of
x, then z.key >= x.key.

The big idea behind binary search trees is that they support the basic
operations (search, insertion, deletion) and have a few added attractive
features (they can give you the min and max of a set, and they can give you the
predecessor and successor of any given element of the set), but - due to the
potential imbalance in their structure - they carry out all of these operations
in at worst O(n) time (and log(n) at best - actually, they carry out the
operations in precisely O(h) - where h is the height - but because there's no
guarantee that the bst is going to be balanced, the operations might take as
long as O(n)), the generic BST is more of a springboard onto more specialized
versions of bsts. One of these such specialized versions are Red-Black trees,
which use a 'color' attribute on each node to guarantee (approximate) balance,
which in turn guarantees 'good' (O(log(n))) performance on the basic
operations.
