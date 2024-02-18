from graph import Graph
from tabulate import tabulate
import sys


def dijkstra(graph, start):
    # Ustawiamy odległości jako bardzo duża liczba — maxsize
    distance = {node: sys.maxsize for node in graph}
    distance[start] = 0

    visited = set()

    while visited != set(graph):
        # Gdy jesteśmy w jakimś wierzchołku, wybieramy kolejny, który jest najbliżej i jeszcze nie jest odwiedzony
        current_node = min((node for node in graph if node not in visited), key=lambda x: distance[x])
        visited.add(current_node)

        # Aktualizujemy obliczoną trasę
        for neighbor, weight in graph[current_node]:
            if distance[current_node] + weight < distance[neighbor]:
                distance[neighbor] = distance[current_node] + weight

    return distance


# Funkcja dodatkowa, aby ładnie przerobić wynikowy słownik odległości na tabelę
def dict_to_table(dict):
    keys = sorted(dict.keys())
    headers = [''] + keys
    rows = []
    for key1 in keys:
        row = [key1]
        for key2 in keys:
            if key2 in dict[key1]:
                value = dict[key1][key2]
            else:
                value = '-'
            row.append(value)
        rows.append(row)
    return tabulate(rows, headers, tablefmt='grid')


# TEST
g = Graph()

g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')
g.add_vertex('F')
g.add_vertex('G')

# Stworzyłem implementacje, która tworzy graf skierowany, dlatego, aby mieć możliwość swobodnego przemieszczania się po
# nim, potrzebne było utworzenie krawędzi w obie strony
g.add_edge('A', 'B', 5)
g.add_edge('A', 'G', 5)
g.add_edge('B', 'A', 5)
g.add_edge('B', 'G', 5)
g.add_edge('B', 'D', 3)
g.add_edge('B', 'C', 3)
g.add_edge('C', 'B', 3)
g.add_edge('C', 'D', 1)
g.add_edge('D', 'C', 1)
g.add_edge('D', 'B', 3)
g.add_edge('D', 'G', 3)
g.add_edge('D', 'F', 4)
g.add_edge('D', 'E', 5)
g.add_edge('E', 'D', 5)
g.add_edge('E', 'F', 2)
g.add_edge('F', 'E', 2)
g.add_edge('F', 'D', 4)
g.add_edge('F', 'G', 5)
g.add_edge('G', 'F', 5)
g.add_edge('G', 'D', 3)
g.add_edge('G', 'B', 5)
g.add_edge('G', 'A', 5)

print('Vertices:', g.get_vertices())
print('Edges:', g.get_edges())
print('Graph:', g)

# Rysowanie grafu
g.draw()

# Dijkstra
# Implementacja Dijsktry oblicza odległości jedynie z zadanego 1 wierzchołka, więc należy ją uruchomić dla każdego
# obecnego w grafie wierzchołka, a następnie złączyć wyniki w jeden słownik, aby utworzyć na jego podstawie tabelę
start_node_A = 'A'
distances_A = dijkstra(g.graph, start_node_A)
start_node_B = 'B'
distances_B = dijkstra(g.graph, start_node_B)
start_node_C = 'C'
distances_C = dijkstra(g.graph, start_node_C)
start_node_D = 'D'
distances_D = dijkstra(g.graph, start_node_D)
start_node_E = 'E'
distances_E = dijkstra(g.graph, start_node_E)
start_node_F = 'F'
distances_F = dijkstra(g.graph, start_node_F)
start_node_G = 'G'
distances_G = dijkstra(g.graph, start_node_G)

dijkstra_values = {start_node_A: distances_A,
                   start_node_B: distances_B,
                   start_node_C: distances_C,
                   start_node_D: distances_D,
                   start_node_E: distances_E,
                   start_node_F: distances_F,
                   start_node_G: distances_G}

print('\nDijkstra calculated distances (in dictionary):')
print(dijkstra_values)

print('\nDijkstra calculated distances (in table):')
print(dict_to_table(dijkstra_values))

