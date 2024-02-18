# BUBBLE SORT
import numpy as np


# funkcja sortujaca metoda bubble sort
def bubble_sort(list):
    length = len(list)

    for i in range(length - 1):
        save_list = list.copy()

        # sortowanie wartosci poprzez zapisywanie wartosci i wpisywanie ich w nowe miejsca
        for j in range(length - 1 - i):
            if list[j] > list[j + 1]:
                save_value_1 = list[j]
                save_value_2 = list[j + 1]
                list[j + 1] = save_value_1
                list[j] = save_value_2

        if all(np.equal(list, save_list)):
            break

    return list
