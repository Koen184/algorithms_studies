# QUICKSORT


def quick_sort(array):
    # too small arrays can't be sorted
    if len(array) <= 1:
        return array

    smaller, equal, larger = [], [], []

    # selecting pivot
    pivot = array[0]

    # sorting numbers to the 3 groups, smaller, equal and larger than pivot
    for number in array:
        if number < pivot:
            smaller.append(number)
        elif number == pivot:
            equal.append(number)
        else:
            larger.append(number)

    # final result and continuation of sorting smaller and larger elements
    return quick_sort(smaller) + equal + quick_sort(larger)
