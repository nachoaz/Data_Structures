# (Generic) Binary Search Tree
##  Description
Typically, we use a Binary Search Tree when we have a list (or collection)
of numbers, and ned to be able to do all (or most) of these things:
  1. check if a number is in the list search.
  2. insert a new number into the list
  3. delete a number from the list
  4. get the smallest number from that list
  5. get the largest number from that list
  6. get the successor of a number within that list
  7. get the predecessor of a number within that list

Some terminology: given y, x is the predecessor of y if it's the number to
the left of x in the sorted list (where list was sorted in nondecreasing
order). Similarly, z (the successor) is to the right.

Note, however, that in practice we don't use Binary Search Trees unless we
know they'll be perfectly balaned; this is because if we don't have the
guarantee that it'll be perfectly balanced, then the BST might only yield
'fair' (or, more specifically, O(n)) performance for these operations (this
occurs in the worst case, which is when the BST is perfectly imbalanced).
This is why the generic BST is more of a base model for more specialized
data structures, such as Red-Black trees (and other variations of BSTs that
follow a 'balanced' scheme).

Question: Doing an inorder-tree-walk on a BST gives you the keys (or values,
whatever you want) of the BST in sorted order. So if I have a list (or
collection) of numbers, can't I use a BST to sort that list in O(n) time?

Answer: No. It costs to do O(n) to do the inorder-tree-walk, yes. But it'll
also have cost O(n) to build the BST in the first place.


## Time Complexity of Operations
NOTE: h is height of the tree. h can be at best floor(log(n)) (or simply logn)
(which occurs if tree perfectly blanced), or at worst n (if perfectly
imbalanced).

  1. access: (same as search)
  2. search: O(h) because sought-after-node is found by following simple path to
     sought-after-node (which may or may not be at the deepest level of the
     BST).
  3. insert: O(h) because to insert a node X, we follow a simple path, asking:
     should X be in the right subtree here or in the left subtree? Since the
     path is a simple path, its length is at most h.
  4. delete: O(h) because to delete a node Z, we have three cases:
    1. if Z has no children, simply remove Z
    2. if Z has one child, remove Z and elevate that child to take Z's position
    3. if Z has two children, find Z's successor Y --which will be in Z's right
       subtree-- and have Y take Z's position
  5. min: O(h) because min is found by following a simple path from root to
     leftmost node
  6. max: O(h) because max is found by following a simple path from root to
     rightmost node.
  7. predecessor(`x`): O(h) because predecessor is found by either:
    1. following a simple path _up_ from `x` or
    2. following a simple path _down_ from `x`
     If the left subtree of `x` is nonempty, then the successor of
     `x` is just the rightmost node in `x`'s left subtree.
     If the left subtree of `x` is empty and `x` has a predecessor `y`, then `y`
     is the lowest ancestor  of `x` whose right child is also an ancestor of `x`
  8. successor(`x`): O(h) because successor found through similar process as
     predecessor.
     If the right subtree of `x` is nonempty, then the successor of `x` is just
     the leftmost node in x's right subtree.
     If the right subtree of `

access: (same as search)
search: O(h) because sought-after-node found by following simple path to sought-after-node (which may or may not be at deepest level)
insert: O(h) because to insert a node X, we follow a simple path, asking: should X be in the right subtree here or in the left? Since path is simple, it's at most length h.
delete: O(h) because to delete a node Z, we have three cases (if Z no children, simply remove Z), (if Z one child, remove Z and elevate child to take Z's position), (if Z two children, find Z's successor Y - which will be in Z's right subtree - and have Y take Z's position).
get_min: O(h) because min found by following a simple path to deepest leftmost node
get_max: O(h) because max found by following a simple path from root to deepest rightmost node
predecessor: O(h) because predecessor found by either following a simple path UP from (given) origin node or a simple path DOWN from (given) origin node(If the left subtree of node x is nonempty, then the successor of x is just the rightmost node in x’s left subtree. If the left subtree of node x is empty and x has a successor y, then y is the lowest ancestor of x whose right child is also an ancestor of x.)
successor: O(h) because successor found through similar process as predecessor (If the right subtree of node x is nonempty, then the successor of x is just the leftmost node in x’s right subtree. If the right subtree of node x is empty and x has a successor y, then y is the lowest ancestor of x whose left child is also an ancestor of x.)
values: O(n) because this requires traversing the entire tree
