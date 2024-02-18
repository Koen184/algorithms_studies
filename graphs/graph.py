import matplotlib.pyplot as plt
import math


class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            for start_vertex in self.graph:
                if vertex in self.graph[start_vertex]:
                    self.graph[start_vertex].remove(vertex)
        else:
            print('There is no such vertex in the graph')

    def add_edge(self, start_vertex, end_vertex, length):
        if start_vertex in self.graph:
            self.graph[start_vertex].append((end_vertex, length))
        else:
            self.graph[start_vertex] = [(end_vertex, length)]

    def remove_edge(self, start_vertex, end_vertex):
        if start_vertex in self.graph and end_vertex in [edge[0] for edge in self.graph[start_vertex]]:
            edges = self.graph[start_vertex]
            for value, edge in enumerate(edges):
                if edge[0] == end_vertex:
                    del edges[value]
                    break
        else:
            print('There is no such edge in the graph')

    def get_vertices(self):
        return list(self.graph.keys())

    def get_edges(self):
        edges = []
        for start_vertex in self.graph:
            for end_vertex in self.graph[start_vertex]:
                edges.append((start_vertex, end_vertex))
        return edges

    def depth_first_search(self, start_vertex):
        visited = set()
        if start_vertex in self.graph:
            self._dfs_help_method(start_vertex, visited)

    def _dfs_help_method(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')

        if vertex in self.graph:
            for neighbor in self.graph[vertex]:
                if neighbor[0][0] not in visited:
                    self._dfs_help_method(neighbor[0][0], visited)

    def breadth_first_search(self, start_vertex):
        visited = set()
        queue = [start_vertex]
        visited.add(start_vertex)
        start_index = 0
        end_index = 1

        while start_index < end_index:
            vertex = queue[start_index]
            start_index += 1
            print(vertex, end=' ')

            if vertex in self.graph:
                for neighbor in self.graph[vertex]:
                    if neighbor[0][0] not in visited:
                        visited.add(neighbor[0][0])
                        queue.append(neighbor[0][0])
                        end_index += 1

    # Metoda transformująca graf — zmieniająca kierunki połączeń, potrzebna do Algorytmu Kosaraju
    def transpose_graph(self):
        transposed = Graph()
        for vertex in self.graph:
            transposed.add_vertex(vertex)
        for start_vertex in self.graph:
            for edge in self.graph[start_vertex]:
                end_vertex = edge[0]
                length = edge[1]
                transposed.add_edge(end_vertex, start_vertex, length)
        return transposed

    def kosaraju(self):
        visited = set()
        stack_vertex = []

        # Przetwarzanie DFS -> potrzebne było 2, bo moje opierało się o printowanie wierzchołków, a nie ich zapisywaniu
        # więc potrzebna była 2 metoda DFS dla Kosaraju, aby tworzyła odpowiednią listę
        # Przerobiona została metoda _dfs_help_method, aby nie pisać kodu od nowa i umieszczona w metodzie, ponieważ
        # tylko tu będzie ona potrzebna -> wcześniejsze DFS pozostaje nienaruszone
        def dfs(vertex):
            visited.add(vertex)
            if vertex in self.graph:
                for neighbor in self.graph[vertex]:
                    if neighbor[0][0] not in visited:
                        dfs(neighbor[0][0])
            stack_vertex.append(vertex)

        for vertex in self.graph:
            if vertex not in visited:
                dfs(vertex)

        transposed_graph = self.transpose_graph()
        transposed_graph = transposed_graph.graph
        visited = set()

        # Przetwarzanie DFS w transponowanym grafie
        # Po raz kolejny przerobiona odpowiednio metoda _dfs_help_method
        def dfs_transposed(vertex, element):
            visited.add(vertex)
            element.append(vertex)
            if vertex in transposed_graph:
                for neighbor in transposed_graph[vertex]:
                    if neighbor[0][0] not in visited:
                        dfs_transposed(neighbor[0][0], element)

        # Znalezienie silnie spójnych składowych
        strongly_connected_elements = []
        while stack_vertex:
            vertex = stack_vertex.pop()
            if vertex not in visited:
                element = []
                dfs_transposed(vertex, element)
                strongly_connected_elements.append(element)

        return strongly_connected_elements

    # Nie bede oszukiwał, w przypadku rysowania z kodem mocno pomógł mi chatgpt, ale aby umieć sobie wyobrazić lepiej
    # operacje, które wykonujemy, potrzebowałem miejscami podejrzeć jak wygląda ten utworzony graf i te metody
    # mają to na celu
    def draw(self):
        plt.figure()
        pos = self.calculate_positions()
        for start_vertex in self.graph:
            for edge in self.graph[start_vertex]:
                end_vertex = edge[0]
                length = edge[1]
                plt.arrow(pos[start_vertex][0], pos[start_vertex][1], pos[end_vertex][0] - pos[start_vertex][0],
                          pos[end_vertex][1] - pos[start_vertex][1], color='gray', length_includes_head=True,
                          head_width=0.1)
                plt.text((pos[start_vertex][0] + pos[end_vertex][0]) / 2,
                         (pos[start_vertex][1] + pos[end_vertex][1]) / 2,
                         str(length), ha='center', va='center', fontsize=10, fontweight='bold', color='red')
        for vertex, coordinates in pos.items():
            plt.text(coordinates[0], coordinates[1], vertex, ha='center', va='center', fontsize=12, fontweight='bold',
                     bbox=dict(facecolor='lightblue', edgecolor='gray', boxstyle='circle'))
        plt.axis('off')
        plt.show()

    def calculate_positions(self):
        num_vertices = len(self.graph)
        positions = {}
        angle = 2 * 3.14159 / num_vertices
        radius = 1
        for i, vertex in enumerate(self.graph.keys()):
            x = radius * 0.9 * 0.5 * (1 + 5 * i / num_vertices) * math.cos(i * angle)
            y = radius * 0.9 * math.sin(i * angle)
            positions[vertex] = (x, y)
        return positions

    def __str__(self):
        return str(self.graph)


# # # TEST
# g = Graph()
#
# g.add_vertex('A')
# g.add_vertex('B')
# g.add_vertex('C')
# g.add_vertex('D')
# g.add_vertex('E')
# g.add_vertex('F')
# g.add_vertex('G')
# g.add_vertex('H')
#
# g.remove_vertex('A')
# g.remove_vertex('F')
#
# g.add_edge('A', 'B', 4)
# g.add_edge('A', 'H', 2)
# g.add_edge('B', 'C', 3)
# g.add_edge('C', 'D', 2)
# g.add_edge('D', 'A', 1)
# g.add_edge('D', 'B', 2)
# g.add_edge('D', 'C', 3)
# g.add_edge('D', 'E', 4)
# g.add_edge('E', 'F', 4)
# g.add_edge('F', 'G', 7)
# g.add_edge('G', 'E', 6)
#
# g.remove_edge('D', 'B')
# g.remove_edge('D', 'H')
#
# print('Vertices:', g.get_vertices())
# print('Edges:', g.get_edges())
# print('Graph:', g)
#
# # Rysowanie grafu
# g.draw()
#
# # DFS
# print("Depth First Search:")
# g.depth_first_search('C')
# print("\n")
#
# # BFS
# print("Breadth First Search:")
# g.breadth_first_search('C')
# print("\n")
#
# # Algorytm Kosaraju
# print("Strongly Connected Components:")
# scc = g.kosaraju()
# for element in scc:
#     print(element)
