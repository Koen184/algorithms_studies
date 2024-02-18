from matplotlib import pyplot as plt
import numpy as np
import time
import sys

from quick_sort import quick_sort
from merge_sort import merge_sort
from counting_sort import counting_sort

sys.setrecursionlimit(5000)

# creating lists of functions, names and sizes of vectors
functions = [quick_sort, merge_sort, counting_sort]
functions_names = ['quick_sort', 'merge_sort', 'counting_sort']
value_list = [100, 500, 1000, 3000, 5000]

# creating lists to which the results will be saved
result_quick = []
result_merge = []
result_counting = []
results = [result_quick, result_merge, result_counting]

# the main loop of the algorithm, calculates the average sorting time for all functions and vector sizes in turn
for function in functions:

    for value in value_list:
        count_average = []

        for i in range(100):
            array = np.random.randint(0, 5000, value)

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


# creating lists to which the pessimistic results will be saved
result_quick_p = []
result_merge_p = []
result_counting_p = []
results_p = [result_quick_p, result_merge_p, result_counting_p]

# the loop of the algorithm, calculates the pessimistic sorting time for all functions and vector sizes in turn
for function in functions:

    for value in value_list:
        if functions_names[functions.index(function)] == 'quick_sort':
            array = sorted(np.random.randint(0, 5000, value))
        elif functions_names[functions.index(function)] == 'counting_sort':
            array = np.random.permutation(value * 10)[:value]
        else:
            array1 = np.random.randint(0, 5000, int(value / 2))
            array2 = np.random.randint(0, 5000, int(value / 2))
            array = np.concatenate((array1, array2))

        start = time.perf_counter_ns()
        sort_test = function(array)
        finish = time.perf_counter_ns()

        pessimistic_time = finish - start
        pessimistic_time = pessimistic_time / 1_000_000_000
        pessimistic_time = round(pessimistic_time, 5)

        results_p[functions.index(function)].append([value, pessimistic_time])


print('Pessimistic sorting done')


# creating lists to which the optimistic results will be saved
result_quick_o = []
result_merge_o = []
result_counting_o = []
results_o = [result_quick_o, result_merge_o, result_counting_o]

# the loop of the algorithm, calculates the optimistic sorting time for all functions and vector sizes in turn
for function in functions:

    for value in value_list:
        if functions_names[functions.index(function)] == 'quick_sort':
            random_value = np.random.randint(0, 5000)
            array = [random_value for _ in range(value)]
        elif functions_names[functions.index(function)] == 'counting_sort':
            array = sorted(np.random.randint(0, int(value / 2), value))
        else:
            array = sorted(np.random.randint(0, 5000, value))

        start = time.perf_counter_ns()
        sort_test = function(array)
        finish = time.perf_counter_ns()

        optimistic_time = finish - start
        optimistic_time = optimistic_time / 1_000_000_000
        optimistic_time = round(optimistic_time, 5)

        results_o[functions.index(function)].append([value, optimistic_time])


print('Optimistic sorting done')


# creating graphs for each sorting algorithm
plt.subplot(2, 2, 1)
plt.plot([value[0] for value in result_quick], [average[1] for average in result_quick],
         label='Quick sort', color='#E39DE3')
plt.plot([value[0] for value in result_merge], [average[1] for average in result_merge],
         label='Merge sort', color='#A8EAFC')
plt.plot([value[0] for value in result_counting], [average[1] for average in result_counting],
         label='Counting sort', color='#3CC1A9')

# editing the graph
plt.title('Execution time charts for sorting algorithms')
plt.ylabel('Time [s]')
plt.legend()


# creating graphs for each sorting algorithm
plt.subplot(2, 2, 2)
plt.plot([value[0] for value in result_quick], [average[1] for average in result_quick],
         label='Average', color='#E39DE3')
plt.plot([value[0] for value in result_quick_p], [time[1] for time in result_quick_p],
         label='Pessimistic', color='#AD71B4')
plt.plot([value[0] for value in result_quick_o], [time[1] for time in result_quick_o],
         label='Optimistic', color='#F2C8F2')

# editing the graph
plt.title('Quick sort')
plt.legend()


# creating graphs for each sorting algorithm
plt.subplot(2, 2, 3)
plt.plot([value[0] for value in result_merge], [average[1] for average in result_merge],
         label='Average', color='#A8EAFC')
plt.plot([value[0] for value in result_merge_p], [time[1] for time in result_merge_p],
         label='Pessimistic', color='#00D8FF')
plt.plot([value[0] for value in result_merge_o], [time[1] for time in result_merge_o],
         label='Optimistic', color='#00C1FF')

# editing the graph
plt.title('Merge sort')
plt.xlabel('Array size')
plt.ylabel('Time [s]')
plt.legend()


# creating graphs for each sorting algorithm
plt.subplot(2, 2, 4)
plt.plot([value[0] for value in result_counting], [average[1] for average in result_counting],
         label='Average', color='#3CC1A9')
plt.plot([value[0] for value in result_counting_p], [time[1] for time in result_counting_p],
         label='Pessimistic', color='#1E8279')
plt.plot([value[0] for value in result_counting_o], [time[1] for time in result_counting_o],
         label='Optimistic', color='#74DAC9')

# editing the graph
plt.title('Counting sort')
plt.xlabel('Array size')
plt.legend()


# showing graphs
plt.show()
