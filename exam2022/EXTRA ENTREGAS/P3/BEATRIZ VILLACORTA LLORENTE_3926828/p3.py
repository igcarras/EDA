import math
import sys

"""
Name:
NIA:
group:
"""

class AdjacentIsland:
        def __init__(self, i: int, h: int, d: int) -> None:
            """This constructor creates a 3-tuple where
            we save the connected island, the height of the
            bridge, and the length of the bridge"""
            self._island = i
            self._height = h
            # height
            self._distance = d  # length of the bridge

        def __str__(self):
            return '('+str(self._island) + ", " + str(self._height)+ ", " + str(self._distance)+')'

class Archipelago:

    def __init__(self, n: int) -> None:
        """As the (names) ids of islands are number from 0
        to n-1, we do not need a dictionary.
        We simply need to use a Python list
        where we can save the adjacent islands for each island"""
        self._num = n
        self._adjacent_islands = [None] * n  # will be a list of lists
        print(self._adjacent_islands)

    def _neigbours(self, vertex: int) -> list:
        lst_neigbours = []
        if self._adjacent_islands[vertex] is not None:
            for adj in self._adjacent_islands[vertex]:
                lst_neigbours.append(adj._island)
        return lst_neigbours

    def add_bridge(self, i1: int, i2: int, h: int, d: int) -> None:
        """i1, i2: islands to be connected.
            h: height of the bridge that connects both islands
            d: length of the bridge that connects both islands"""
        if i1 not in range(self._num):
            print(i1, " is not an island!!!")
            return
        if i2 not in range(self._num):
            print(i2, " is not an island!!!")
            return
        if i1 == i2:
            print('loops are not allowed')
            return
        if h <= 0:
            print(h, ' the height should be positive')
            return
        if d <= 0:
            print(d, ' the length should be positive')
            return

        # print("adding ", i1, i2, h, d)

        if i1 in self._neigbours(i2):
            print("Error: already exist bridge between {} and {}".format(i1,i2))
            return
        if i2 in self._neigbours(i1):
            print("Error: already exist bridge between {} and {}".format(i2,i1))
            return

        if self._adjacent_islands[i1] is None:
            #  create the empty list
            self._adjacent_islands[i1] = []
        if self._adjacent_islands[i2] is None:
            #  create the empty list
            self._adjacent_islands[i2] = []

        self._adjacent_islands[i1].append(AdjacentIsland(i2, h, d))
        self._adjacent_islands[i2].append(AdjacentIsland(i1, h, d))

    def __str__(self) -> str:
        """ returns a string containing the graph"""
        result_str = ''
        for v in range(self._num):
            result_str += '\n' + str(v) + ': '
            if self._adjacent_islands[v] is not None:
                for adj in self._adjacent_islands[v]:
                    result_str += str(adj) + ", "

            if result_str.endswith(", "):
                result_str = result_str[:-2]
        return result_str

    def accessible_from(self, i: int, h: int) -> list:
        # recibe isla y altura de marea
        # devuelve lista con las islas que tienen h mayor
        # y que son accesibles desde i
        # recorro la lista de adjacentes de i
        lista_ac = []
        vecinos = self._neigbours(i)
        for j in vecinos:
            if vecinos[j]._height > h:
                lista_ac.append(self._neigbours[j])
        return lista_ac





    def dijkstra(self, origin):
        """"This function takes a vertex v and calculates its mininum path
        to the rest of vertices by using the Dijkstra algoritm"""

        # we use a Python list of boolean to save those nodes that have already been visited
        # Mark all the vertices as not visited
        visited = {}
        for v in self.vertices.keys():
            visited[v] = False

        # this list will save the previous vertex
        previous = {}
        for v in self.vertices.keys():
            previous[v] = -1

        # This array will save the accumulate distance from v to each node
        distances = {}
        for v in self.vertices.keys():
            distances[v] = sys.maxsize

        # The distance from v to itself is 0
        distances[origin] = 0

        for n in range(len(self.vertices)):
            # Pick the vertex with the minimum distance vertex.
            # u is always equal to v in first iteration
            u = self.minDistance(distances, visited)
            # Put the minimum distance vertex in the shotest path tree
            visited[u] = True

            # Update distance value of the u's adjacent vertices only if the current
            # distance is greater than new distance and the vertex in not in the shotest path tree
            for i in self.vertices[u]:
                if visited[i] == False and distances[i] > distances[u] + 1:
                    distances[i] = distances[u] + 1
                    previous[i] = u

                    # finally, we print the minimum path from v to the other vertices

        # self.printSolution(distances,previous,origin)
        return distances, previous


    def minimum_path(self, start: int, end: int, tide : int = 0) -> (list, int):
        # Initilaize minimum distance for next node
        min = sys.maxsize

        # recibe parámetro h (metros que ha subido la marea)
        # start isla
        # end isla
        # busca el camino mínimo
        # compruebo cuantos vértivos son accesibles
        accesibles = self.accessible_from(start, tide)
        # ahora busco el camino mínimo

        min = math.inf
                # returns the vertex with minimum distance from the non-visited vertices
        return minimumPath, distances[end]
    de minimumPath()
        for v in accesibles[v]:
            if distances[vertex] <= min and visited[vertex] == False:
                min = distances[vertex]  # update the new smallest
                min_vertex = vertex  # update the index of the smallest

        return min_vertex




if __name__ == '__main__':
    g3 = Archipelago(7)
    g3.add_bridge(0, 1, 2, 3)
    g3.add_bridge(0, 2, 5, 10)
    g3.add_bridge(1, 2, 3, 2)
    g3.add_bridge(1, 3, 3, 3)
    g3.add_bridge(2, 3, 4, 10)
    g3.add_bridge(2, 4, 5, 3)
    g3.add_bridge(3, 4, 4, 4)

    print(g3)

    island = 0
    for island in range(7):
        for height in range(6):
            print('accessible_from {} with height {}'.format(island, height))
            result = g3.accessible_from(island, height)
            print(result)
        print()


    path, d = g3.minimum_path(0, 4, 1)
    print(path, d)

    print(g3.minimum_path(0, 3, 5))

    print(g3.minimum_path(2, 3, 1))
