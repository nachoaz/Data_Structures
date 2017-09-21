Data Structures
===============

Purpose
-------
The purpose of this repo is to house exercises that I've done to get practice
with different data structures.

Know the meaning of asymtotic tight bounds, and keep in mind the relationship
between costs. To help with this, use this image provided by
[bigocheatsheet.com](http://bigocheatsheet.com/):
<img src="/images/big_o_viz.png" width=200>


Main Idea Data Structures
-------------------------
In computer science, sets (of things in general) are dynamic: they can grow,
shrink, or otherwise change over time. We need different ways of representing
and manipulating sets on a computer, based on what we'd like to do with those
sets; in other words, the best way to implement a dynamic set depends on the
operations that must be supported. This is what data structures are (ways to
implement a dynamic set to support the operations which the application at hand
demands).

Summary Data Structures
-----------------------
Here's a summary that I've adapted from the excellent summary provided by
[interviewcake](https://goo.gl/DHbaPJ).

Arrays have fast lookups but slow inserts and deletions (unless they're
`appends` and `extract_right`s); in addition to this, an unattractive thing
about arrays is not only that array items need to be the same size, but also
that you need to specify how many of these items the array should hold --and you
need to do so in advance. (This is because of how arrays live in memory and how
they're accessed; they're a big contiguous block of memory cells and --to know
where within that block to find a particular item-- they need to be made up of
items of the same size).

One way to get around the all-items-must-be-the-same-size requirement is to make
your array hold _pointers_ to items; this way, item sizes can vary. (The price
you pay for doing this is that items will now be spread throughout the
computer's memory, and so you won't get blazing-fast-thanks-to-CPU-caching
lookups as you would with plain-vanilla arrays).

To get around the must-know-number-of-items-in-advance requirement, you can
instead use a linked list or a dynamic array. A linked list supports fast
appends, prepends, and extract-lefts and extract-rights, but you don't get fast
lookups with a linked list. With a dynamic array, on the other hand, you get
fast lookups but expensive prepends and extract-lefts.

Fast lookups are important to have (at least it seems that the need for fast
lookups shows up in a lot of applications); it's especially useful when you can
look things up fast not just by indices, but by arbitrary _keys_. Hash tables
allow you to do this. They also support fast inserts (anywhere), fast deletions
(anywhere), and fast searches (anywhere). (Consider that searches in arrays and
linked lists are typically expensive cause you have to traverse the data
structure asking "is this it? is this it? is this it?") The 'unattractive' side
of hash tables is the fact that you run the risk of a 'collision' (i.e. that two
keys map to the same value); in practice, however, this is rare and so we can
wave our hands and say that the aforementioned operations take constant time.

Tips on Shopping for Data Structures
------------------------------------
It's all about knowing what's important in the problem you're working on.  What
does your data structure need to do quickly? What can you afford for it to do
slowly? Think about which operations you'll perform frequently, and which
operations you won't do at all. Know what each data structure has to offer, and
know what it is that your problem needs.


Main Idea Algorithms
--------------------
The main idea behind the subject of algorithms is that ["there's more than one
way to peel an orange."](https://goo.gl/jRLxCp)
