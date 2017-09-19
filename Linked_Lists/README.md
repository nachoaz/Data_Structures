Linked Lists
============

Description
-----------
A linked list is a collection of values chained together in memory. In contrast
to arrays (in which elements live in a contiguous block of memory), these values
may or may not live far apart from each other in memory. This is accomplished by
having each element of the chain point to where the next one lives (and having
some pointer letting us know where the first element --the 'head'-- of the list
is).

Sometimes you'll want to navigate both forward and in reverse through a linked
list (like when you want to get the _k_th-to-last item on the list); in these
circumstances, its convenient to use a doubly-linked list.

Time Complexity of Operations
-----------------------------
### Prepend
Unlike in arrays, prepends in linked lists are cheap (constant time, constant
space). A prepend is done by building the node to insert (with its pointer
pointing to what is currently the head node), and reassigning the `head` pointer
to point at the newly-inserted node.

### Append
Assuming we're using a `tail` pointer, appends in linked lists are cheap
(constant time, constant space). This is done by building the node to insert,
reassigning the `next` pointer of the node that is currently at the tail of the
list to point to the to-be-inserted node, and then reassigning the `tail`
pointer (if we're using one) to point to the newly-inserted node.

If we're not using a `tail` pointer, then we have to find the tail (which takes
O(n) time, where n is the number of elements in the linked list). Then we
proceed as before.

### Access
In contrast to arrays, access in a linked list (except for when you're accessing
the head or the tail node, which you'll have pointers to), is slow. It takes
O(_i_) time to get the _i_th element in the list.
