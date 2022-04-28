# -*- coding: utf-8 -*-
# Examen Ordinario 24 Mayo 2021
# La clase MyGraph es una implementación basada en diccionarios para representar un grafo dirigido no ponderado.
# Para simplificar el problema, supondremos que los vértices son números enteros no negativos (0,1,2,..).
# Implementa la función minimum_path, que reciba dos vértices,
# start y end, y devuelve una lista de Python con los vértices
# que forman el camino mínimo desde start a end,
# ambos inclusive.
# La función minimum_path debe utilizar
# el algoritmo de camino mínimo de Dijkstra.

import math


class MyGraph:
    def __init__(self, n: int) -> None:
        """ Create a graph with n vertices (0,1,...,n-1) """
        self._vertices = {}
        for i in range(n):
            self._vertices[i] = []

    def check_vertex(self, v: int) -> bool:
        """ checks if v is a vertex"""
        if v not in range(len(self._vertices)):
            print(v, " is not a vertex!!!")
            return False
        return True

    def add_connection(self, i: int, j: int) -> None:
        """ adds a connection from i to j"""
        if not self.check_vertex(i) or not self.check_vertex(j):
            return 

        self._vertices[i].append(j)

    def min_distance(self, distances, visited):
        """This functions returns the vertex (index) whose associated value in
        the dictionary distances is the smallest value. We
        only consider the set of vertices that have not been visited"""
        # Initialize minimum distance with a very big number
        min_distance = math.inf

        # returns the vertex with minimum distance from the non-visited vertices
        for vertex in self._vertices.keys():
            if distances[vertex] <= min_distance and not visited[vertex]:
                min_distance = distances[vertex]  # update the new smallest
                min_vertex = vertex  # update the index of the smallest

        return min_vertex

    def dijkstra(self, origin):
        """"This function takes a vertex v and calculates its mininum path
        to the rest of vertices by using the Dijkstra algoritm"""

        visited = {}  # visited is a dictionary whose keys are the verticies of our graph.
        previous = {}  # this dictionary will save the previous vertex for the key in the minimum path
        distances = {}  # This dictionary will save the accumulate distance from the  origin to the vertex (key)

        for v in self._vertices.keys():
            visited[v] = False
            previous[v] = None
            distances[v] = math.inf

        # The distance from origin to itself is 0
        distances[origin] = 0

        for _ in range(len(self._vertices)):
            # Pick the vertex with the minimum distance vertex.
            # u is always equal to origin in first iteration
            u = self.min_distance(distances, visited)

            visited[u] = True

            # we must visit all adjacent vertices (neighbours) for u
            for v in self._vertices[u]:
                if not visited[v]  and distances[v] > distances[u] + 1:
                    # we must update because its distance is greater than the new distance
                    distances[v] = distances[u] + 1
                    previous[v] = u

                    # finally, we print the minimum path from origin to the other vertices
        return distances, previous

    def minimum_path(self, start: int, end: int) -> list:
        """returns the shortest path from start to end and its distance"""
        print("Smallest path from ", start, " to ", end)

        if not self.check_vertex(start) or not self.check_vertex(end):
            return None, None

        distances, previous = self.dijkstra(start)
        if distances[end] == math.inf:
            print("There is not path from {} to {}".format(start, end))
            return None, math.inf

        minimum_path = []
        prev = previous[end]
        while prev:
            minimum_path.insert(0, prev)
            prev = previous[prev]

        minimum_path.append(end)

        return minimum_path, distances[end]

    def __str__(self):
        result = ''
        for u in self._vertices.keys():
            result += '\n' + str(u) + ' \t: '
            for v in self._vertices[u]:
                result += str(v) + ','
            result = result[0:-1]

        return result


if __name__ == '__main__':
    # Now, we use the implementation to represent this directed and unweighted graph:
    # <img src='https://www.researchgate.net/publication/319327358/figure/fig8/AS:631663130337280@1527611634108/Figura-52-Ejemplo-de-Grafo-Dirigido-No-Ponderado-Extraido-de-Fre10.png'/>
    
    g = MyGraph(8)
    # vertex = 0 is not connected
    # Now, we add the edges
    g.add_connection(1, 2)
    g.add_connection(1, 3)
    g.add_connection(1, 4)
    
    g.add_connection(2, 4)
    g.add_connection(2, 5)
    g.add_connection(3, 6)
    g.add_connection(4, 3)
    g.add_connection(4, 6)
    g.add_connection(4, 7)
    g.add_connection(5, 4)
    g.add_connection(5, 7)
    g.add_connection(7, 6)
    print(g)

    path, d = g.minimum_path(0, 1)
    print(path, "distance: ", d)

    path, d = g.minimum_path(2, 7)
    print(path, "distance: ", d)
    print()
    # <img src='https://www.researchgate.net/profile/Wladimir-Tavares/publication/318252493/figure/fig8/AS:668258659225604@1536336688129/Figura-31-Grafo-ponderado-direcionado-G-r-onde-r-1-2-3-4-5-6.png'>
    
    g = MyGraph(7)
    # the vertex 0 is not connected
    # Now, we add the edges
    g.add_connection(1, 2)
    g.add_connection(1, 5)
    g.add_connection(2, 3)
    g.add_connection(3, 4)
    g.add_connection(3, 6)
    g.add_connection(4, 5)
    g.add_connection(4, 6)
    g.add_connection(5, 6)
    
    print(g)
    
    path, d = g.minimum_path(0, 1)
    print(path, "distance: ", d)
    
    path, d = g.minimum_path(1, 4)
    print(path, "distance: ", d)
    
    path, d = g.minimum_path(1, 6)
    print(path, "distance: ", d)
    
    path, d = g.minimum_path(3, 6)
    print(path, "distance: ", d)
