import math
import sys
from graph import AdjacentVertex
from graph import Graph

class Graph2(Graph):
    def min_number_edges(self, start: str, end: str) -> int:
        """para desarrollar este método se ha utilizado el agoritmo de dijkstra,
        que busca el camino mínimo entre estart y end, pero se ha implementado con alguna modificación:
        el peso de las aristas ha pasado a ser 1, independientemente de lo que pese cada una en realidad.
        De esta manera se va contabilizando el número de aristas que tiene el camino en vez de su peso
        """
        if start not in self._vertices.keys():
            print(start, ' does not exist!!!')
            return None, None
        if end not in self._vertices.keys():
            print(end, ' does not exist!!!')
            return None, None

        distances, previous = self.dijkstra(start)
        if distances[end] == math.inf:
            return 0

        result = [end]
        prev = previous[end]
        while prev is not None:
            result.insert(0, prev)
            prev = previous[prev]

        return distances[end]

    def min_distance(self, distances: dict, visited: dict) -> int:
        """returns the vertex (index) whose associated value in
        the dictionary distances is the smallest value. We
        only consider the set of vertices that have not been visited"""
        # Initialize minimum distance for next node
        min_distance = math.inf
        min_vertex = None

        # returns the vertex with minimum distance from the non-visited vertices
        for vertex in self._vertices.keys():
            if distances[vertex] <= min_distance and not visited[vertex]:
                min_distance = distances[vertex]  # update the new smallest
                min_vertex = vertex  # update the index of the smallest

        return min_vertex

    def dijkstra(self, origin: object) -> None:
        visited = {}  # for each vertex (key), the value is a boolean indicating if the vertex has been visited
        previous = {}  # for each vertex (key), the value is the previous node in the minimum path from origin
        distances = {}  # for each vertex (key), the value is minimum distance in the minimum path from origin

        # initialize dictionaries
        for v in self._vertices.keys():
            visited[v] = False
            previous[v] = None
            distances[v] = math.inf

        # The distance from origin to itself is 0
        distances[origin] = 0

        for _ in range(len(self._vertices)):
            # pick the non-visited vertex with minimum distance
            u = self.min_distance(distances, visited)
            visited[u] = True
            # get the adjacent vertices of u
            for adj in self._vertices[u]:
                i = adj.vertex
                w = 1
                # for non-visited vertex, we have to check if its distance is greater than the distance from u
                if not visited[i] and distances[i] > distances[u] + w:
                    # we must update because its distance is greater than the new distance
                    distances[i] = distances[u] + w
                    previous[i] = u

        # Finally, we print the minimum path from origin to the other vertices
        self.print_solution(distances, previous, origin)

        return distances, previous

    def print_solution(self, distances: dict, previous: dict, origin: object):
        print("Minimum path from ", origin)

        for i in self._vertices.keys():
            if distances[i] == sys.maxsize:
                print("There is not path from ", origin, ' to ', i)
            else:
                # minimum_path is the list which contains the minimum path from origin to i
                minimum_path = []
                prev = previous[i]
                # this loop helps us to build the path
                while prev is not None:
                    minimum_path.insert(0, prev)
                    prev = previous[prev]

                # we append the last vertex, which is i
                minimum_path.append(i)

                # we print the path from v to i and the distance
                print(origin, '->', i, ":", minimum_path, distances[i])

    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self"""
        #creo un nuevo grafo
        #newGraph = Graph()
        #guardo los vértices del viejo grafo en el nuevo
        for i in range(len(self._vertices)):
            newGraph = Graph(self._vertices.keys())

        #redirijo las aristas
        for v in self._vertices.keys():
            for j in self._vertices.keys():
                if self.contain_edge(v, j):
                    newGraph.add_edge(j, v)
            #si el vertice A.keys contain edje(i, v)
            #newgraph.add_edge(v,i)

        return newGraph


    def is_strongly_connected(self) -> bool:
        """Esta función verifica si el grafo está fuertemente conectado.
         Un grafo dirigido es fuertemente conexo cuando para cualquier
         par de vértices u y v, siempre hay un camino de u a v.
         Si el grafo no es dirigido, la función devuelve True si el grafo es
         conexo, es decir, hay un camino desde cualquier vértice a cualquier otro.

        para desarrollar la función, recorro todos los vertices del grafo y compruebo si hay camino de una arista a otra
        apoynadonos en el metodo mi_number_edges implementado anteriormente
        """
        if self != None:
            for v in self._vertices.keys():
                for n in self._vertices.keys():
                    if v!=n:
                        if self.min_number_edges(v,n)==0:
                            return False
            return True
        else:
            print('El grafo no existe')
            return False

