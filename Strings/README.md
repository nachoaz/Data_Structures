Strings
=======

Description
-----------
A `char` can be represented in memory as a single byte (and so uses only one
memory address). A string is a a contiguous block of memory slots (each
representing a char); that is, a string is an array of chars. So how should we
store an array of strings? It'd be an array or arrays. We'd need the arrays to
be of a fixed size (to be able to '_predict_' the addresses of the char at the
beginning of each string) (thus limiting the length of the strings they
represent, and we might end up wasting a lot of space by not using up the memory
slots towards the end of each array. A better alternative would be an array of
pointers. These pointers would let us know where to look for each
array-that-represents-a-string; this would allow us to not need to agree on a
particular size that all the arrays should have -- by doing this, we'd not only
solve the problem of having to limit the length of strings, but also we'd solve
the problem of wasting memory space.
