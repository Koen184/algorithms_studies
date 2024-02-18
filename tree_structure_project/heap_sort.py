from treev2 import BinaryTree


def heap_sort(array):
    if len(array) <= 0:
        return array

    root = []
    heap = BinaryTree(array)

    array = heap.get_tree()

    root.append(array[0])
    array = array[1:]

    return root + heap_sort(array)




