Heap
====

Description
-----------
A _heap_ is a specialized binary tree. Specifically, it's a complete binary tree
in which the keys must satisfy the _heap property_--the key at each node is
greater than or equal to the keys stored in its subtree (in the case of a
max-heap; the _heap property_ in the case of a min-heap is similarly defined).

The heap data structure is useful not only for implementing heapsort (a sorting
algorithm which combines the advantages of insertionsort and mergesort - it
sorts in-place, and does so in O(nlogn) time) with a max-heap, but also for
implementing an efficient priority queue with a min-heap.

Note: heapsort is a good algorithm, but a good implementation of quicksort
usually beats it in practice. Nevertheless, we can still use heaps for many
applications, including most notably as an efficient priority queue.

Generally, you'll want to use heaps for "find the _k_
largest/smallest"-kinds-of-problems; for these, use a min heap or a max heap,
respectively. Use a heap when all you care about is the largest or smallest
elements, and you don't need fast lookups, deletes (other than
`extract_min`/`extract_max`, or searches for arbitrary elements.

Implementation
--------------
A (binary) heap is typically implemented using an array-like object (either a
plain-vanilla array or a dynamically-resizable array). Each node of the heap
corresponds to an element of the array. An array _A_ that represents a heap is
an object with two attributes: _A_.length (which gives us the number of
elements in _A_), and _A_.heap-size (which tells us how many elements in the
heap are stored within the array _A_). That is, although _A_[1,...,_A_.length]
may contain numbers, only _A_[1,...,_A_.heap-size] (where 1<= _A_.heap-size <=
_A_.length) are valid elements of the heap. 

Time Complexity of Core Operations
---------------------------------- 
A min-heap supports O(logn) insertions (`insert`), O(1) time lookup for the min
element (`min`), and O(logn) deletion of the min element (`extract_min`).

### Insertion
To insert an item into a min heap, we start by inserting the element at the
bottommost-rightmost spot (so as to maintain the 'complete-tree property'. We
then 'fix' or _heapify_ (more specifically, _min-heapify_) by swapping the new
element with its parent (if necessary), and repeat as needed until we find an
appropriate spot for the new element (such that the 'min-heap property' is
maintained). So we 'bubble-up' or 'float-up' the new element.

### Extract Min
To extract the min, we simply take the value at the top of the heap (which is
guaranteed to be the minimum value in the set); the tricky part, though, is what
is to be done afterward. (It's not that tricky.) We start by swapping the last
element in the heap (the bottommost, rightmost element) with the minimum of the
heap (which will be at the root). We can then safely extract the
newly-moved-to-the-last-spot min element, and now we have to let the
newly-moved-to-the-first-spot element 'float-down' to its correct spot (so that
the 'min-heap' property remains.

Time Complexity of Auxilary Operations
--------------------------------------
### Swap
Considering that the heap is implemented using an array 'under the hood', a swap
operation takes O(1) time and O(1) space.

### Float Up / Float Down
The running time of min/max 'heapify' can be described by the recurrence T(n) <=
T(2n/3) + O(1), which --by the Master Theorem-- simplifies to O(logn).
Alternatively, we can characterize the running time of these operations on a
node of height _h_ as O(_h_) (because it'll move at most _h_ times).
