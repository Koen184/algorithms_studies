#RADIX SORT

#funkcja sortujaca na podstawie danego miejsca cyfry w liczbie do wykorzystania pozniej w fukcji sortujacej metodą radix sort
def sort(list, place):
    lenght = len(list)
    result = [0] * lenght
    count = [0] * 10
    
    #zliczenie liczby elementów
    for i in range (0, lenght):
        index = list[i] // place
        count[index % 10] += 1
        
    #zliczenie całkowitej liczby elementów
    for i in range(1, 10):
        count[i] += count[i - 1]
        
    #ulozenie liczb na podstawie ustawienia cyfr na danym miejscu w posortowanej kolejnosci
    while lenght - 1 >= 0:
        index = list[lenght - 1] // place
        result[count[index % 10] - 1] = list[lenght - 1]
        count[index % 10] -= 1
        lenght -= 1
        
    #zwracanie listy z ulozonymi elementami
    for i in range (0, len(list)):
        list[i] = result[i]
        

#funkcja sortujaca metoda radix sort
def radix_sort(list):
    max_value = max(list)
    place_value = 1
        
    while max_value // place_value > 0:
        sort(list, place_value)
        place_value *= 10
        
    return list


        
#testowanie
test = [2, 16, 4, 3, 6, 7, 12, 231, 343, 341, 987, 123, 98, 129, 1934, 33]
sort_test = radix_sort(test)

print(sort_test)