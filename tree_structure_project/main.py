from matplotlib import pyplot as plt
import numpy as np
import time
import sys

from heap_sort import heap_sort
from bst import BinarySearchTree

sys.setrecursionlimit(2500)

# creating lists of functions, names and sizes of vectors
functions = [heap_sort, BinarySearchTree]
functions_names = ['heap_sort', 'bst']
value_list = [100, 200, 500, 1000, 2000]

# creating lists to which the results will be saved
result_heap = []
result_bst = []
results = [result_heap, result_bst]

# the main loop of the algorithm, calculates the average sorting time for all functions and vector sizes in turn
for function in functions:

    for value in value_list:
        count_average = []

        if functions.index(function) == 0:
            for i in range(100):
                array = np.random.randint(0, 5000, value)

                start = time.perf_counter_ns()
                function(array)
                finish = time.perf_counter_ns()

                t = finish - start
                count_average.append(t)

        else:
            for i in range(100):
                array = np.arange(1, value + 1)
                np.random.shuffle(array)

                bst = function(value // 2)

                for number in array:
                    bst.insert(number)

                arr_search = np.random.choice(array, 10, replace=False)

                start = time.perf_counter_ns()
                for number in arr_search:
                    bst.search(number)
                finish = time.perf_counter_ns()

                t = finish - start
                count_average.append(t)

        # calculating the average and converting it from nanoseconds to seconds and saving it to the results
        average_ns = sum(count_average) / 100
        average_s = average_ns / 1_000_000_000
        average_s = round(average_s, 8)
        results[functions.index(function)].append([value, average_s])

        print('Performed a check for ', functions_names[functions.index(function)], ' for the array size of: ', value)

# creating graphs for each sorting algorithm
# to better visualize the BST graph, I recommend commenting out the heap sort plot
plt.plot([value[0] for value in result_heap], [average[1] for average in result_heap],
         label='Heap sort', color='#E39DE3')
plt.plot([value[0] for value in result_bst], [average[1] for average in result_bst],
         label='Binary search tree', color='#7B68EE')

# editing the graph
plt.title('HEAP SORT & BINARY SEARCH TREE')
plt.xlabel('Array size')
plt.ylabel('Time [s]')
plt.legend()

# showing the graph
plt.show()
