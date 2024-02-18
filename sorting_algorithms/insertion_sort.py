#INSERTION SORT

#funkcja sortujaca metoda insertion sort
def insertion_sort(list):
    for i in range(1, len(list)):
        x = i

        #sortowanie wartosci poprzez zapisywanie wartosci i wpisywanie ich w nowe miejsca
        while x > 0 and list[x - 1] > list[x]:
            save_value_1 = list[x]
            save_value_2 = list[x - 1]
            list[x - 1] = save_value_1
            list[x] = save_value_2
            x -= 1
    return list


#testowanie
test = [2, 16, 4, 3, 6, 7, 12]
sort_test = insertion_sort(test)

print(sort_test)