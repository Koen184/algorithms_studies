# SELECTION SORT

# fuckja znajdujaca minimalna wartosc, potrzebna do uzycia w algorytmie selection sort
def minimal_value(list, starting_point):
    x = starting_point

    for i in range(x + 1, len(list)):
        if list[i] < list[x]:
            x = i
    return x


# funkcja sortujaca metoda selection sort
def selection_sort(list):
    for i in range(len(list)):
        minimal = minimal_value(list, i)
        save_value_1 = list[i]
        save_value_2 = list[minimal]
        list[i] = save_value_2
        list[minimal] = save_value_1
    return list
