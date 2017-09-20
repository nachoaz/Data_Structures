Trees
=====

Trees are a special case of Graphs. A free tree (or simply a 'tree') is an
undirected, connected, acyclic graph. If an undirected graph is acyclic but
disconnected, it's called a 'forest', and the connected components of that
forest are trees.

Some Facts About Trees (Properties)
-----------------------------------
Note: any of these implies any of the others.
  1. G is a free tree
  2. Any two vertices in G are connected by a unique simple path.
  3. G is connected, but if any edge is removed from G then the resulting graph
     is disconnected.
  4. G is connected, and |E| = |V| - 1
  5. G is acyclic, and |E| = |V| - 1
  6. G is acyclic, but if any edge is added to G, then the resulting graph
     contains a cycle.

Rooted Trees and Ordered Trees
------------------------------
A rooted tree is a tree in which one of the nodes r (the 'root') is
distinguished from the others. We call any node y in the simple path from r to x
an 'ancestor' of x. If y is an ancestor of x, then x is a 'descendant' of y.
(Note that because of this definition, we have the silly implication that a node
x is both an ancestor and a descendant of itself - this is why we have terms
like 'proper ancestor' and 'proper descendant'.) A 'subtree rooted at x' is the
tree induced by the descendants of x (this tree is rooted at x).

The last edge on the simple path from r to x connects the 'parent' of x to its
'child' (x). If two nodes have the same parent, they're said to be 'siblings'. A
node with no children is a 'leaf' or 'external node'. A nonleaf node is an
'internal node'. In the context of a rooted tree, the degree of a node x is the
number of children x has. (Note: in 'free' trees - and in undirected graphs in
general - the degree of a node is simply the number of adjacent vertices or
equivalently the number of edges incident on it. In a 'rooted' tree, however,
the degree is the number of children - the parent of a node does not count
toward its degree.)

The length of the simple path from r to x is the 'depth' of x, and the length of
the simple path from r to the deepest leaf node is the 'height' of the tree.
(This means the number of levels on a tree is equal to 1 + the height of the
tree.)

An 'ordered tree' is a rooted tree in which the children of each node are
ordered. That is, if a node has k children, then there's a first child, a second
child, ..., and a kth child.

Some Terminology
----------------
A 'complete k-ary tree' is a k-ary tree in which every level of the tree is
fully filled, except for perhaps the last level. To the extent that the last
level is filled, it is filled left to right.

A 'full k-ary tree' is a k-ary tree in which every node has either zero or two
children. That is, no nodes have only one child.

A 'perfect k-ary tree' is a k-ary tree that is both full and complete. All leaf
nodes will be at the same level, and this level has the maximum number of nodes.
A perfect k-ary tree of n nodes has lg(n+1) levels (where lg(n+1) means logbase2
of (n + 1)).
