Queues
======

Description
-----------
A queue works in a 'first-in, first-out' (FIFO) way. Use them when you want to
hold a set of things together, and you know that the order in which you'll need
to extract and use those things is FIFO. Their two basic operations are _push_
(which can be thought of as `insert_right` or more simply `append`), and _pop_
(which can be thought of as `extract_left`). (Observe that you could also do
_push_ and _pop_ operations by `prepend`ing and `extract_right`ing.)

Many times, you'll only want to do `append` and `extract_left`
operations on a queue and so you won't care about how long it takes to do a
lookup because you won't be doing any _anyway_; with this in mind, a linked-list
implementation is often best. (Also, a linked-list implementation *does not*
require big blocks of contiguous memory, wheras an array-based implementation
would.)

Time Complexity of Operations
-----------------------------
These are assuming we're using a linked-list 'under the hood', and that this
linked-list has both a `head` and a `tail` pointer.

### Append (_Push_)
This takes O(1) time and O(1) space.

### Extract Left (_Pop_)
This takes O(1) time and O(1) space.

### Peek
This returns whatever is at the top of the queue, without actually popping it
from the queue. Its time cost is O(1).
