import sys


def prim(graph):
    # Wybór wierzchołka startowego
    start_node = next(iter(graph))
    visited = set([start_node])
    edges = []
    minimum_spanning_tree = []

    while len(visited) != len(graph):
        min_weight = sys.maxsize
        min_edge = None

        # Szukamy najbliższego wierzchołka, do już drzewa tworzonego przez już odwiedzone wierzchołki
        for node in visited:
            for neighbor, weight in graph[node]:
                if neighbor not in visited and weight < min_weight:
                    min_weight = weight
                    min_edge = (node, neighbor, weight)

        # Dodawanie znalezionego wierzchołka do drzewa
        if min_edge:
            edges.append(min_edge)
            minimum_spanning_tree.append(min_edge)
            visited.add(min_edge[1])

    return minimum_spanning_tree


def kruskal(graph):
    edges = []
    minimum_spanning_tree = []
    sets = {node: set([node]) for node in graph.keys()}

    # Tworzymy i sortujemy listę krawędzi w grafie
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors:
            edges.append((node, neighbor, weight))

    edges.sort(key=lambda x: x[2])

    for edge in edges:
        node1, node2, weight = edge
        set1 = sets[node1]
        set2 = sets[node2]

        # Dodawanie kolejnych wierzchołków do drzewa, jeśli te, nie utworzą cyklu
        if set1 != set2:
            minimum_spanning_tree.append((node1, node2, weight))

            new_set = set1.union(set2)
            for node in new_set:
                sets[node] = new_set

    return minimum_spanning_tree
