import random
import string
import time
from matplotlib import pyplot as plt
from prim_kruskal import prim
from prim_kruskal import kruskal


# Funkcja generująca losowy graf — z powodu mojej, nie do końca optymalnej implementacji grafu (używanie go do tego
# zadania byłoby męczarnią), zdecydowałem się losować słownik, który będzie służył jako graf
def generate_random_graph(value_vertices):
    if value_vertices <= 0:
        return {}

    vertices = list(string.ascii_uppercase[:value_vertices])
    random_graph = {vertex: [] for vertex in vertices}

    for i, vertex in enumerate(vertices):
        distances = random.choices(range(1, value_vertices + 1), k=value_vertices)
        counts = random.choices(range(1, value_vertices + 1), k=value_vertices)

        for j, neighbor in enumerate(vertices):
            if i != j:
                distance = distances[j]
                count = counts[j]
                random_graph[vertex].extend([(neighbor, distance)] * count)

    # Funkcja czasami duplikowała niektóre połączenia — nie do końca wiem dlaczego, ale działo się to, dlatego dodana
    # jest ta pętla, która w razie ich wystąpienia usunie je — z listy tworzy zbiór, operacja ta automatycznie usuwa
    # powtarzające się wartości, a następnie utworzony zbiór przypisuje się listy ścieżek jako nowa wartość
    for vertex in random_graph:
        random_graph[vertex] = list(set(random_graph[vertex]))

    return random_graph


# Tradycyjny kod do uruchamiania i tworzenia wykresów
if __name__ == "__main__":
    monte_carlo = 100
    sizes = [5, 10, 15, 20]

    result_prim = []
    result_kruskal = []

    # Prim Algorithm
    print('Prim Algorithm')
    for i in range(monte_carlo):
        result = []
        for size in sizes:
            graph = generate_random_graph(size)

            start = time.perf_counter_ns()
            prim(graph)
            finish = time.perf_counter_ns()

            t = (finish - start)
            result.append(t)

        result_prim.append(result)
        print('Performed ', i + 1, ' check')

    # Kruskal Algorithm
    print('Kruskal Algorithm')
    for i in range(monte_carlo):
        result = []
        for size in sizes:
            graph = generate_random_graph(size)

            start = time.perf_counter_ns()
            kruskal(graph)
            finish = time.perf_counter_ns()

            t = (finish - start)
            result.append(t)

        result_kruskal.append(result)
        print('Performed ', i + 1, ' check')

    print(result_prim)
    print(result_kruskal)

    # Tworzenie wykresów — Prim Algorithm
    plt.subplot(1, 2, 1)

    averages = [sum(column) / len(column) for column in zip(*result_prim)]
    plt.plot(sizes, averages, color='#FF0000')

    for results in result_prim:
        plt.plot(sizes, results, color='#E39DE3')

    plt.plot(sizes, averages, color='#FF0000')
    plt.title('Prim Algorithm')
    plt.xlabel('Size of graph')
    plt.ylabel('Time (ns)')
    plt.legend(['Average of results', 'Monte Carlo results'], loc='upper left')

    # Tworzenie wykresów — Kruskal Algorithm
    plt.subplot(1, 2, 2)

    averages = [sum(column) / len(column) for column in zip(*result_kruskal)]
    plt.plot(sizes, averages, color='#FF0000')

    for results in result_kruskal:
        plt.plot(sizes, results, color='#E39DE3')

    plt.plot(sizes, averages, color='#FF0000')
    plt.title('Kruskal Algorithm')
    plt.xlabel('Size of graph')
    plt.ylabel('Time (ns)')
    plt.legend(['Average of results', 'Monte Carlo results'], loc='upper left')

    # Wyświetlanie wykresów
    plt.show()

    # Porównanie średnich wyników na jednym wykresie
    averages = [sum(column) / len(column) for column in zip(*result_prim)]
    plt.plot(sizes, averages, color='#00FFFF')

    averages = [sum(column) / len(column) for column in zip(*result_kruskal)]
    plt.plot(sizes, averages, color='#FF0000')

    plt.title('Prim & Kruskal Algorithm - Comparison')
    plt.xlabel('Size of graph')
    plt.ylabel('Time (ns)')
    plt.legend(['Average of Prim Algorithm', 'Average of Kruskal Algorithm'], loc='upper left')
    # Wyświetlanie wykresu
    plt.show()
