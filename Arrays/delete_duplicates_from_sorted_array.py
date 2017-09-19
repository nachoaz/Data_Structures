# delete_duplicates_from_sorted_array.py

# Write a program which takes a sorted array and updates it so that all
# duplicates have been removed and the remaining elements have been shifted left
# to fill the emptied indices. Return the number of valid elements. Many
# languages have functions for performing this operation-- you cannot use these
# functions. Note: there are no requirements as to the values beyond the last
# valid element.

def delete_duplicates_from_sorted_array(arr):
    """Receives a sorted array and returns array with duplicates removed (with
    zero padding after the last valid element), as well as the number of valid
    elements.

    Example:
      input: [2, 3, 5, 5, 7, 11, 11, 11, 13]
      output: 6 (and arr is now [2, 3, 5, 7, 11, 13, 0, 0, 0]
    """
    if not arr:
        return 0

    flag_index = 1
    for i in range(1, len(arr)):
        if arr[flag_index-1] != arr[i]:
            arr[flag_index] = arr[i]
            flag_index += 1

    for j in range(flag_index, len(arr)):
        arr[j] = 0

    return flag_index - 1
