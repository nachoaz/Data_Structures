Heap
====

Description
-----------
A _heap_ is a specialized binary tree. Specifically, it's a complete binary tree
in which the keys must satisfy the _heap property_--the key at each node is
greater than or equal to the keys stored in its subtree (in the case of a
max-heap; the _heap property_ in the case of a min-heap is similarly defined).

Time Complexity of Operations
-----------------------------
A max-heap supports O(logn) insertions (`insert`), O(1) time lookup for the max
element (`max`), and O(logn) deletion of the max element (`extract_max`).
