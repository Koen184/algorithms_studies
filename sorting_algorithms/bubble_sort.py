import numpy as np #biblioteka potrzebna do działania algorytmu bubble sort

#BUBBLE SORT

#funkcja sortujaca metoda insertion sort
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


#testowanie
test = [2, 16, 4, 3, 6, 7, 12]
sort_test = bubble_sort(test)

print(sort_test)
