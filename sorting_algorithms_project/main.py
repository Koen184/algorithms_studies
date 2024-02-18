from matplotlib import pyplot as plt
import numpy as np
import time

from selection_sort import selection_sort
from insertion_sort import insertion_sort
from bubble_sort import bubble_sort

# creating lists of functions, names and sizes of vectors
functions = [selection_sort, insertion_sort, bubble_sort]
functions_names = ['selection_sort', 'insertion_sort', 'bubble_sort']
value_list = [100, 500, 1000, 3000, 5000]

# creating lists to which the results will be saved
result_selection = []
result_insertion = []
result_bubble = []
results = [result_selection, result_insertion, result_bubble]

# the main loop of the algorithm, calculates the average sorting time for all functions and vector sizes in turn
for function in functions:

    for value in value_list:
        count_average = []

        for i in range(100):
            array = np.random.randint(-5000, 5000, value)

            start = time.perf_counter_ns()
            sort_test = function(array)
            finish = time.perf_counter_ns()

            t = finish - start
            count_average.append(t)

        # calculating the average and converting it from nanoseconds to seconds and saving it to the results
        average_ns = sum(count_average) / 100
        average_s = average_ns / 1_000_000_000
        average_s = round(average_s, 5)
        results[functions.index(function)].append([value, average_s])

        print('Performed a check for ', functions_names[functions.index(function)], ' for the array size of: ', value)


print(result_selection)
print(result_insertion)
print(result_bubble)

# creating graphs for each sorting algorithm
plt.plot([value[0] for value in result_selection], [average[1] for average in result_selection],
         label='Selection sort', color='#E39DE3')
plt.plot([value[0] for value in result_insertion], [average[1] for average in result_insertion],
         label='Insertion sort', color='#A8EAFC')
plt.plot([value[0] for value in result_bubble], [average[1] for average in result_bubble],
         label='Bubble sort', color='#3CC1A9')

# editing the graph
plt.title('Execution time charts for sorting algorithms')
plt.xlabel('Array size')
plt.ylabel('Time [s]')
plt.legend()

# showing the graph
plt.show()
