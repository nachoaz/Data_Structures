# implement an algorithm to determine if a string has all unique characters.
from collections import Counter, defaultdict

my_string = raw_string('Please enter string.')

counts = Counter(my_string) # O(n) time operation
result = 'Yes' if any([count > 1 for count in counts.keys()]) else 'No'

print "Is the string made up of all unique characters? {0}".format(result)

counts = defaultdict(int)
for char in my_string:
    counts[char] += 1

result = 'Yes' if any([count > 1 for count in counts.keys()]) else 'No'

# what if you cannot use additional data structures?

