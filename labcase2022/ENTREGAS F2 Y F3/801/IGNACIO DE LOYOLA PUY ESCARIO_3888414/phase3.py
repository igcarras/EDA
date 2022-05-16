from graph import AdjacentVertex
from graph import Graph
import sys

class Graph2(Graph):
    def min_number_edges(self, start: str, end: str) -> int:
        if self.contain_edge(start, end) != 0:
            return 1
        elif start == end:
            return 0
        elif self._directed and len(self._vertices[start]) == 0:
            return 0
        else:
            visited = {}
            distance = {}
            for v in self._vertices.keys():
                visited[v] = False
                distance[v] = sys.maxsize
            distance[start] = 0
            while not visited[end]:
                u = self.min_distance(distance, visited)
                visited[u] = True
                for adj in self._vertices[u]:
                    i = adj.vertex
                    w = adj.weight
                    if not visited[i] and distance[i] > distance[u] + w:
                        distance[i] = distance[u] + w
            return distance[end]

    def min_distance(self, distances: dict, visited: dict) -> int:
        min_distance = sys.maxsize
        min_vertex = None
        for vertex in self._vertices.keys():
            if distances[vertex] <= min_distance and not visited[vertex]:
                min_distance = distances[vertex]
                min_vertex = vertex
        return min_vertex


    def transpose(self) -> 'Graph2':
        g2 = Graph2(self._vertices.keys())
        for v in self._vertices.keys():
            for adj in self._vertices[v]:
                g2.add_edge(adj.vertex, v)
        return g2

    def is_strongly_connected(self) -> bool:
        result = True
        for v in self._vertices.keys():
            if not result:
                return result
            result = result and self.connected(v)
        return result

    def connected(self, start):
        InitialList = []
        FinalList = []
        visited = {}
        for v in self._vertices.keys():
            visited[v] = False
            InitialList.append(v)
        visited[start] = True
        FinalList.append(start)
        self.visitAdjacents(start, visited, FinalList)
        return len(FinalList) == len(InitialList)

    def visitAdjacents(self, vertex, visited, FinalList: list):
        for adj in self._vertices[vertex]:
            if not visited[adj.vertex]:
                visited[adj.vertex] = True
                FinalList.append(adj.vertex)
                self.visitAdjacents(adj.vertex, visited, FinalList)