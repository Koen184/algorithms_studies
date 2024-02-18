import random


# Tworzenie losowych preferencji na podstawie listy kobiet, mężczyzn oraz wartości mającej oznaczać ile preferencji
# posiada każda z kobiet
def generate_preferences(women, men, num_preferences):
    preferences = {}
    for woman in women:
        random.shuffle(men)
        preferences[woman] = men[:num_preferences]
    return preferences


# Funkcja dobierająca stabilne małżeństwa — nie działa na grafach, ponieważ nie umiałem sobie z tym poradzić, posiadając
# swoją implementację grafów — naprawdę średnio się do tego nadawała
# Z tego powodu funkcja, opiera się o zadane tablice, prezentujące kobiety oraz mężczyzn
# Kobietom losowane są preferencje, za pomocą funkcji powyżej
# Sam algorytm prezentuje zasadę działania prawdziwego algorytmu, który powinien opierać się o grafy dwudzielne
# Mam nadzieję, że takie uproszczenie nie będzie dużym problemem, ale po prostu nie wychodziło mi zrobienie tego
# zadania o grafy tworzone za pomocą mojej implementacji klasy graf
def tinder(women, men):
    preferences = generate_preferences(women, men, num_preferences=4)   # <- tutaj można zmieniać ilość preferencji
    matches = {}

    print(preferences)

    flag = 0

    while len(matches) < len(women):
        flag += 1
        for woman in women:
            if woman not in matches:
                free_woman = woman
                break

        for man in preferences[free_woman]:
            if man not in matches.values():
                matches[free_woman] = man
                break

        # Losowość preferencji sprawia, że nie zawsze znajdzie się rozwiązanie, będzie niemożliwe utworzenie par
        # dla każdej z kobiet/mężczyzn, dlatego po 100 nieudanych iteracjach pętli while zostanie ona przerwana
        # Zapobiega to działaniu pętli w nieskończoność, w razie wystąpienia takiego przypadku
        if flag == 100:
            print('Mimo wykonania: ', flag, ' iteracji pętli WHILE, nie udało się znaleźć par dla wszystkich :c')
            break

    return matches, flag


# Przykładowe dane
women = [0, 1, 2, 3, 4]
men = [0, 1, 2, 3, 4]

# Kojarzenie małżeństw
matches, count = tinder(women, men)

# Wyświetlanie wyników
print('\n')
for women, men in matches.items():
    print(f"Women{women + 1} ---> Men{men + 1}")

print('\n')
print('Wyniki uzyskane po: ', count, ' przejściach pętli WHILE')
