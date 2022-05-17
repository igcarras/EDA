from graph import AdjacentVertex
from graph import Graph
import queue
import math

class Graph2(Graph):

# ------------------------------------------- NÚMERO MÍNIMO DE ARTISTA -------------------------------------------------

    def min_number_edges(self, start, end):

        if start not in self._vertices.keys():
            print(start, ' does not exist!')
            return
        if end not in self._vertices.keys():
            print(end, ' does not exist!')
            return
        visited = {}
        camino_nuevo, queue = [], []
        distancia = 0
        visited[start] = True
        queue.append(start)
        for v in self._vertices.keys():
            visited[v] = False
        while len(queue) > 0 and end not in queue:
            s = queue.pop(0)
            for ady in self._vertices[s]:
                if visited[ady.vertex] == False:
                    camino_nuevo.append(ady.vertex)
                    visited[ady.vertex] = True
            if len(queue) == 0:
                queue = camino_nuevo.copy()
                camino_nuevo.clear()
                distancia += 1
        if end in queue:
            return distancia
        else:
            return 0

# --------------------------------------------------- TRANSPUESTO ------------------------------------------------------

    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self"""

        if self._directed == False:
            return self
        else:
            graph = Graph2(self._vertices)
            for i in self._vertices:
                for j in self._vertices[i]:
                    graph.add_edge(j.vertex, i, 1)
            return graph


# ---------------------------------------------- FUERTEMENTE CONECTADO -------------------------------------------------

    def DFS(self, vertex, visited, lista_nueva):
        if vertex not in visited:
            visited.append(vertex)
            lista_nueva.append(vertex)
            for j in self._vertices[vertex]:
                self.DFS(j.vertex, visited, lista_nueva)

    def is_strongly_connected(self):
        for vertex in self._vertices.keys():
            lista_nueva = []
            visited = []
            self.DFS(vertex, visited, lista_nueva)
            if len(self._vertices) != len(lista_nueva):
                return False
        return True