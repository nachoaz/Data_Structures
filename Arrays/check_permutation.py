# given two strings, check if one is a permutation of the other

# string_a is a permutation of string_b if it's made up of the same letters,
# just in different order.

# to determine if string_a and string_b are made up of the same characters, we
# could compare sorted(string_a) and sorted(string_b).
# another thing we could do is to compare character counts.
# the first approach would take O(nlogn) time (using timsort), but would either
# require that we alter the input or that we make a copy of it (making a copy
# would require O(n) space where n is the length of the string
# the second approach would require making a dictionary, which would require
# O(n) space, and would require making n constant-time checks, and so would take
# O(n) time.
# therefore, we choose the second approach but short-circuit if the strings
# aren't of same length

from collections import defaultdict

def get_char_counts(my_string):
    counts = defaultdict(int)
    for char in my_string:
        counts[char] += 1

    return counts

def check_permutation(string_a, string_b):
    if len(string_a) != len(string_b):
        return False
    else:
        a_counts = get_char_counts(string_a)
        b_counts = get_char_counts(string_b)
        
        return all([a_counts[char] == b_counts[char] for char in string_a])

def main():
    # testing
    test_inputs = [
            ('hello', 'elloh'),
            ('terminal', 'nalimert'),
            ('cat', 'dog'),
            ('house', ' house')
            ]

    correct_outputs = [
            True,
            True,
            False,
            False
            ]

    for i, test_input in enumerate(test_inputs):
        if check_permutation(*test_input) == correct_outputs[i]:
            print "Test #{} passed.".format(i+1)
        else:
            print "ATTENTION: Test #{} failed".format(i+1)


if __name__ == '__main__':
    main()
