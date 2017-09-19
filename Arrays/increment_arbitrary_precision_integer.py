# Input: an array of digits encoding a decimal number D
# Output: an array of digits encoding D + 1

# Example:
# <1,2,9> ---> \my_funct\ --> <1,3,0>

######

def increment_arbitrary_precision_integer(arr):
    """Increments the list representation of integer by one.

    Takes O(n), where n is length of arr.

    Args:
        arr: A list representing integer D.

    Returns:
        A list representing int D + 1.
    """
    # the most work this can do is going through entire list doing constant time operations. so this is O(n)
    for i in xrange(1, len(arr)+1):
        if arr[-i] + 1 == 10:
            arr[-i] = 0
        else:
            arr[-i] += 1
            break

    arr = [1] + arr if arr[0] == 0 else arr

    return arr

# testing
test_inputs = [
    [1,2,8],
    [1,2,9],
    [9,9,9]
    ]

correct_outputs = [
    [1,2,9],
    [1,3,0],
    [1,0,0,0]
    ]

for i, array in enumerate(test_inputs):
    if increment_arbitrary_precision_integer(array) == correct_outputs[i]:
        print 'Test #{} passed.'.format(i+1)
    else:
        print 'ATTENTION: Test #{} failed.'.format(i+1)
