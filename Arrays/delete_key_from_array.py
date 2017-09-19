# Implement a function which takes as input an array and a key, and updates the array so that all occurrences of the input key have been removed and the remaining elements have been shifted left to fill the emptied indices. Return the number of remaining elements. There are no requirements as to the values stored beyond the last valid element.

# Example:
# <5,3,7,11,2,3,13,5,7>, 3 --> |my_funct| --> 7 (and it's now <5,7,11,2,13,5,7>)

def remove_from_array(arr, key):
    """Removes all occurrences of key from arr, returns number of remaining elements.

    Takes O(n) time and O(1) space.

    Arguments:
        arr: List from which all ocurrences of key are removed. (Note: because lists are mutable, the list passed here actually gets altered.)
        key: What it is that should be removed from arr.

    Returns:
        An integer representing the number of remaining elements in arr.
    """
    count = 0

    for i in xrange(len(arr)):
        if arr[i] != key:
            arr[i - count] = arr[i]
        else:
            count += 1

    print arr[:len(arr) - count]

    return len(arr) - count


# testing
test_inputs = [
    ([5,3,7,11,2,3,13,5,7], 3),
    ([5,3,3,3,3,3,3,3,3,7], 3),
    ([3,3,3,3,3,3,3,3,3,5], 3),
    ([3,3,3,3,3,3,3,3,3,3], 3)
    ]

correct_outputs = [7, 2, 1, 0]

for i, test_input in enumerate(test_inputs):
    if remove_from_array(*test_input) == correct_outputs[i]:
        print 'Test #{} passed.'.format(i+1)
    else:
        print 'ATTENTION: Test #{} failed.'.format(i+1)
