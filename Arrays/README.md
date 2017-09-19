Arrays
======

Description
-----------
An array is a contiguous block of memory. Given an array `arr`, `arr[i]` denotes
the _(i + 1)_th object stored in the array. Sometimes, an array might get filled
up and would thus need to be resized (this can occur every now and then). When
this happens, it's handled by allocating a new array with additional memory (a
constant factor times the size of the original array), and copying over the
entries from the original array. What this implies is that the worst-case time
cost of insertion is big but the average time cost for insertion is constant
since resizing is infrequent.

Time Complexity of Operations
-----------------------------
### Access
Retreiving and updating `arr[i]` takes O(1) time (because you know _exactly_
where in memory what you want to update or retrieve lives).

### `append` (or `insert_at_end`)
Assuming that _knowing_ (or _getting_) the next available address takes O(1),
then inserting a value into an array that isn't full takes constant time: simply
write it into the next available adress. When the array is full, though, we have
to resize it to make room for the value-to-insert (allocate a new array a
constant factor --say two-- times the size of the original array, copy
everything over, and delete the original array).

So the worst-case (the array-is-full-case) time cost is O(n), where n is the
size of the original array. But why can we say the average time cost is O(1)?
Imagine that we're inserting _m_ values into an array. What's the time cost of
doing that? Well, it's the cost of carrying out the actual inserts plus the cost
of carrying out any resizing operations that we might need to do. (For
simplicity, let's assume that whenever we resize we double).  The former is
O(_m_) because each insert costs O(1) and there's _m_ of them. How much do the
doubling operations cost?

### `prepend` (or `insert_at_start`)
Inserting a value into the start of an array that isn't full takes O(m) time
(where m is the number of addresses in the array that have been used). This is
because to insert at the start, you have to move everything over one spot to the
right (which takes O(m) time) and then write the value you want to insert at the
leftmost address. Note that if the array is full, we must re-allocate to a new
array (although --by a similar argument as for re-allocation due to
`insert_at_end` this will still take O(m) time).

### `delete_at_i`
Deleting an element at index _i_ from an array of length _n_ is O(_n - i_).

### `insert_at_i`
Inserting an element at index _i_ in an array of length _n_ is O(_n - i_).
