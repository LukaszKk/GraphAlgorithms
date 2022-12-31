import sys
from queue import Queue


class Graph:
    def __init__(self, vertices):
        self.vertices_count = vertices
        self.edges = [[-1 for _ in range(vertices)]
                      for _ in range(vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

    def dijkstra(self, start_vertex):
        dist = {v: sys.maxsize for v in range(self.vertices_count)}
        dist[start_vertex] = 0

        pq = Queue()
        pq.put(start_vertex)

        while not pq.empty():
            current_vertex = pq.get()
            self.visited.append(current_vertex)

            for neighbor in range(self.vertices_count):
                if self.edges[current_vertex][neighbor] != -1:
                    distance = self.edges[current_vertex][neighbor]
                    if neighbor not in self.visited:
                        old_distance = dist[neighbor]
                        new_distance = dist[current_vertex] + distance
                        if new_distance < old_distance:
                            pq.put(neighbor)
                            dist[neighbor] = new_distance

        print(dist)


if __name__ == "__main__":
    graph = Graph(9)
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 2, 7)
    graph.add_edge(1, 3, 2)

    graph.dijkstra(0)
