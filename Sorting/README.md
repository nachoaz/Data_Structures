Sorting
=======

Why sorting?
------------
Sorting is often done as a preprocessing step to make searching a collection
faster, and to identify items that are similar.

Summary
-------
It's easy to come up with a naive sorting algorithm that will run in O(n^2)
time. A number of sorting algorithms run in O(nlogn) time (such as mergesort,
quicksort, and heapsort); choosing amongst these depends on the problem, though,
as each has its advantages and disadvantages.

Mergesort, for example, is stable (meaning entries which are equal appear in
their original order) but is not in-place (requires additional space); quicksort
is in-place but runs at O(n^2) time in the worst case; heapsort is in-place but
not stable. Note that --as is mentioned in the description of Heaps-- a
well-implemented quicksort is usually the best choice; a lot of library
impementations are based on quicksort. (Python's `sort`, though, uses
Timsort).

Some sorting algorithms (such as counting sort) exploit the fact that not all
elements of the set to be sorted are unique.

Tips
----
  * For small n (i.e. arrays of 10 or fewer elements), insertion sort is a good
    option; it's easy to implement and it'll run faster (on small inputs) than
    its asymptotically superior counterparts. (Think of Rob Pike's #3).
  * If an array is 'kind of sorted' (that is, each element is at most k spots
    from where it should be), then you can sort that array in O(nlogk) time
    using a min heap. <-- Consider heaps for sorting problems, they're often
    helpful.
