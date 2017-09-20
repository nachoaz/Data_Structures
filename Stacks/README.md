Stacks
======

Description
-----------
A stack works in a 'last-in, first-out' (LIFO) way. They're for when you want to
hold a set of things together, and you know that the order in which you'll need
to extract and use those things is LIFO. Their two basic operations are _push_
(which can be thought of as `insert_right` or more simply `append`), and _pop_
(which can be thought of as `extract_right`).

You can implement a stack using either an array, a dynamically-rezisable array,
or a linked-list 'under the hood'. Which should you use? Recall that dynamic
arrays have fast lookups and fast (on average) appends, but slow prepends (and
that their size must not be established ahead of time). Arrays also have fast
lookpus and fast (always, as long as there's memory space available) appends,
but have slow prepends and their size *must* be established ahead of time.
Linked-lists have fast prepends and appends (assuming you're using a linked-list
with both a `head` and a `tail` pointer), but slow lookups. So if you know an
upper bound on how many items will be on the stack at any given time, use an
array. If you don't have such an upper bound, then use either a linked list (if
you don't care for looking up items within the stack --i.e. querying "what's the
third item on the stack?"-- _and_ you want the _guarantee_ that appends will be
constant-time), or use a dynamic array (if you for some reason _do_ want to be
looking up items within the stack, and you're willing to pay for that by
exposing yourself to the possibility that _sometimes_ an append on your stack
will take more than O(1) time --i.e. that it'll be constant only _on average_).

Many times, though, you'll only want to do `append` and `extract_left`
operations on a stack and so you won't care about how long it takes to do a
lookup because you won't be doing any _anyway_; with this in mind, a linked-list
implementation is often best. (Also, a linked-list implementation *does not*
require big blocks of contiguous memory, wheras an array-based implementation
would.)

Time Complexity of Operations
-----------------------------
### Append (_Push_)
Regardless of whether you're using an array, dynamically-resizable array, or
linked list 'under the hood', an append will cost O(1) time and O(1) space.
Note, however, that if you're using an array 'under the hood' to implement your
stack, then you run the risk of having a _stack overflow_ occur (that is, it
might happen that the array you're using to represent your stack gets full --
whenever you try to push one more thing onto it it'll 'overflow').

### Extract Right (_Pop_)
The time cost of this operation is O(1) regardless of what data structure you're
using 'under the hood' to implement your stack (assuming that if you're using a
linked-list, that linked-list has a `tail` pointer).

### Peek
This returns whatever is at the top of the stack, without actually popping it
from the stack. Its time cost is O(1) regardelss of what data structure your
stack is using 'under the hood'.
