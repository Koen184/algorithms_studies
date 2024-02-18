# MERGESORT


# merging function to use in mergesort function
def merge(left, right):
    # checking if lists are empty - if list is empty, there is nothing to merge
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    sorted_array = []
    left_index = 0
    right_index = 0

    # sorting numbers and checking if one of the pages is empty
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1

        if right_index == len(right):
            sorted_array.extend(left[left_index:])
            break
        if left_index == len(left):
            sorted_array.extend(right[right_index:])
            break
    # returning sorted array
    return sorted_array


def merge_sort(array):
    # too small arrays can't be sorted
    if len(array) <= 1:
        return array

    middle = len(array) // 2

    # recursion
    left = merge_sort((array[:middle]))
    right = merge_sort((array[middle:]))

    return merge(left, right)


