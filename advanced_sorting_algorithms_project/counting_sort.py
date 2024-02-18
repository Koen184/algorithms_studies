# COUNTING SORT


def counting_sort(array):
    # too small arrays can't be sorted
    if len(array) <= 1:
        return array

    # creating count and output array
    count_array = [0] * (max(array) + 1)
    output_array = []

    # counting elements in given array
    for number in array:
        count_array[number] += 1

    # sorting
    for index, number in enumerate(count_array):
        if number != 0:
            for i in range(number):
                output_array.append(index)

    # returning sorted array
    return output_array


