Hash Tables
===========

Description
-----------
A hash table is a data structure that uses a hashing function to map a key to an
integer and thus allows for not only constant-time lookups, but also
constant-time inserts and deletions. (Recall that a selling point of arrays is
that they have constant-time lookups, but that their major drawbacks are
expensive inserts --unless they're `append`s-- and expensive deletions --unless
they're `extract_right`s; another thing that's unattractive about arrays is that
their size must be specified ahead of time.)

It turns out that quick lookups are often very important (i.e. that we end up
needing quick lookups in a lot of applications).

Think about hashing functions to realize the weakness of a hash table: a wrench
is thrown into the hash table when two keys are mapped (by the hash function) to
the same value. How do we deal with this? What is usually done is that there'll
be a pointer to a linked list at the address that the key is mapped to, and the
linked list will have the values. Most of the time, _there *won't* be a
'collision'_, and the linked list will consist of only one node. However, it's
possible that more than one key does get mapped to the same address; in this
case, the linked list will have more than one node (but probably still very few
of them). So there is _no guarantee_ that lookups, inserts, and deletions will
be constant time _in theory_ because collisions may occur. We can push this even
further and say that if we're awfully lucky, all of our keys will map to the
same value, and so --if we have _n_ items-- we'll have a length-_n_ linked list
to traverse every time we want to look up a value. (So in this case, our hash
table would reduce to a linked list for practical purposes).  In practice,
however, people use super-cool hash functions and collisions are rare enough
that we can say that _on average_ lookups are O(1) time on a hash table.
